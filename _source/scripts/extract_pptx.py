#!/usr/bin/env python3
"""
Extract text and media from one or more pptx files into a combined master.

Usage:
    python3 extract_pptx.py <output_dir> <slug1>=<pptx1> [<slug2>=<pptx2> ...]

Example:
    python3 extract_pptx.py _source/extracted/master \
        sydney=_source/sydney-2026-neurodesk-draft.pptx \
        sciget=_source/eresearch-2025-sciget-final.pptx

Output:
    <output_dir>/content.md            combined master markdown (all decks, with markers)
    <output_dir>/assets/               extracted PNG/JPEG/SVG, prefixed with <slug>-
    <output_dir>/_manual_review.md     flagged slides per deck
"""

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

RENDERABLE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
PROBLEM_EXTS = {".emf", ".wmf"}


def slugify(s: str, maxlen: int = 40) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s or "").strip("-").lower()
    return (s[:maxlen].rstrip("-")) or "untitled"


def parse_slide(slide_xml: bytes, rels_xml: bytes | None):
    root = ET.fromstring(slide_xml)

    rid_to_target = {}
    if rels_xml:
        rels_root = ET.fromstring(rels_xml)
        for rel in rels_root.findall("{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"):
            rid_to_target[rel.attrib["Id"]] = rel.attrib["Target"]

    title_text = None
    body_blocks = []
    images = []
    videos = []
    problem_media = []

    for sp in root.iter("{%s}sp" % NS["p"]):
        ph_type = None
        nv = sp.find("p:nvSpPr/p:nvPr/p:ph", NS)
        if nv is not None:
            ph_type = nv.attrib.get("type")

        paragraphs = []
        for p in sp.iter("{%s}p" % NS["a"]):
            runs = [t.text or "" for t in p.iter("{%s}t" % NS["a"])]
            text = "".join(runs).strip()
            ppr = p.find("a:pPr", NS)
            lvl = int(ppr.attrib.get("lvl", "0")) if ppr is not None else 0
            has_bullet = ppr is not None and ppr.find("a:buNone", NS) is None
            if text:
                paragraphs.append({"text": text, "level": lvl, "bullet": has_bullet})

        if not paragraphs:
            continue

        if ph_type in ("title", "ctrTitle") and title_text is None:
            title_text = " ".join(p["text"] for p in paragraphs)
        else:
            body_blocks.append(paragraphs)

    for blip in root.iter("{%s}blip" % NS["a"]):
        embed = blip.attrib.get("{%s}embed" % NS["r"])
        if not embed:
            continue
        target = rid_to_target.get(embed)
        if not target:
            continue
        ext = Path(target).suffix.lower()
        target_norm = target.replace("../", "")
        if ext in PROBLEM_EXTS:
            problem_media.append(target_norm)
        elif ext in RENDERABLE_EXTS:
            images.append(target_norm)

    for vf in root.iter("{%s}videoFile" % NS["a"]):
        link = vf.attrib.get("{%s}link" % NS["r"]) or vf.attrib.get("{%s}embed" % NS["r"])
        if link:
            target = rid_to_target.get(link)
            if target:
                videos.append(target.replace("../", ""))

    return {
        "title": title_text,
        "body_blocks": body_blocks,
        "images": images,
        "videos": videos,
        "problem_media": problem_media,
    }


def render_slide_md(deck_slug: str, slide_num: int, slide: dict, asset_prefix: str, rename_map: dict) -> str:
    out = []
    out.append(f"<!-- ===== {deck_slug} slide {slide_num} ===== -->")
    if slide["title"]:
        out.append(f"## {slide['title']}")
    else:
        out.append(f"## (untitled slide {slide_num})")
    out.append("")

    for block in slide["body_blocks"]:
        for p in block:
            indent = "  " * p["level"]
            if p["bullet"]:
                out.append(f"{indent}- {p['text']}")
            else:
                out.append(p["text"])
                out.append("")
        out.append("")

    for img in slide["images"]:
        fname = rename_map[(deck_slug, img)]
        out.append(f"![]({asset_prefix}/{fname})")
        out.append("")

    if slide["videos"]:
        for v in slide["videos"]:
            out.append(f"> **VIDEO (manual):** `{v}`")
        out.append("")

    if slide["problem_media"]:
        for pm in slide["problem_media"]:
            out.append(f"> **EMF/WMF (manual convert):** `{pm}`")
        out.append("")

    return "\n".join(out).rstrip() + "\n"


def extract_one(pptx_path: Path, deck_slug: str, assets_dir: Path):
    slides = []
    flagged = []
    rename_map = {}  # (deck_slug, original_target) -> new_filename

    with zipfile.ZipFile(pptx_path) as z:
        slide_names = sorted(
            [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
            key=lambda n: int(re.search(r"slide(\d+)\.xml", n).group(1)),
        )

        for sname in slide_names:
            slide_num = int(re.search(r"slide(\d+)\.xml", sname).group(1))
            rels_name = f"ppt/slides/_rels/slide{slide_num}.xml.rels"
            slide_xml = z.read(sname)
            rels_xml = z.read(rels_name) if rels_name in z.namelist() else None
            parsed = parse_slide(slide_xml, rels_xml)
            parsed["num"] = slide_num
            slides.append(parsed)

            title_slug = slugify(parsed.get("title"))
            for idx, img in enumerate(parsed["images"], start=1):
                key = (deck_slug, img)
                if key not in rename_map:
                    ext = Path(img).suffix.lower()
                    new_name = f"{deck_slug}-s{slide_num:02d}-{title_slug}-img{idx}{ext}"
                    rename_map[key] = new_name

            reasons = []
            if parsed["problem_media"]:
                reasons.append(f"EMF/WMF: {', '.join(parsed['problem_media'])}")
            if parsed["videos"]:
                reasons.append(f"video: {', '.join(parsed['videos'])}")
            if not parsed["title"] and not parsed["body_blocks"] and not parsed["images"]:
                reasons.append("empty extraction (likely all-graphic slide)")
            if len(parsed["images"]) >= 4:
                reasons.append(f"{len(parsed['images'])} images (likely collage)")
            if reasons:
                flagged.append((slide_num, parsed.get("title") or "(untitled)", reasons))

        for (slug, m), new_name in rename_map.items():
            arc = f"ppt/{m}" if not m.startswith("ppt/") else m
            if arc not in z.namelist():
                candidates = [n for n in z.namelist() if n.endswith(Path(m).name) and "media" in n]
                if candidates:
                    arc = candidates[0]
                else:
                    continue
            data = z.read(arc)
            (assets_dir / new_name).write_bytes(data)

    return slides, flagged, rename_map


def main(out_dir: Path, decks: list[tuple[str, Path]]):
    out_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = out_dir / "assets"
    assets_dir.mkdir(exist_ok=True)

    md_lines = [
        "# Master content (extracted from pptx)",
        "",
        "Combined source-of-truth markdown for AIS / Neurodesk / Sciget content.",
        "Each section below is one deck. Slide markers (`<!-- ===== deck slide N ===== -->`)",
        "preserve provenance back to the original pptx.",
        "",
        "Edit freely. Once topic boundaries are clear, split into `content/<stream>/<topic>.md`.",
        "",
    ]

    all_flagged = []

    for slug, pptx in decks:
        slides, flagged, rename_map = extract_one(pptx, slug, assets_dir)
        md_lines.append("---")
        md_lines.append("")
        md_lines.append(f"# Deck: {slug}")
        md_lines.append("")
        md_lines.append(f"_Source: `{pptx.name}` ({len(slides)} slides)_")
        md_lines.append("")
        for slide in slides:
            md_lines.append(render_slide_md(slug, slide["num"], slide, "./assets", rename_map))
        all_flagged.append((slug, pptx, len(slides), flagged))

    (out_dir / "content.md").write_text("\n".join(md_lines))

    review = ["# Manual review needed", ""]
    for slug, pptx, total, flagged in all_flagged:
        review.append(f"## {slug} (`{pptx.name}`) — {len(flagged)}/{total} slides flagged")
        review.append("")
        for num, title, reasons in flagged:
            review.append(f"- **slide {num}: {title}**")
            for r in reasons:
                review.append(f"  - {r}")
        review.append("")
    (out_dir / "_manual_review.md").write_text("\n".join(review))

    total_slides = sum(t for _, _, t, _ in all_flagged)
    total_flagged = sum(len(f) for _, _, _, f in all_flagged)
    print(f"Wrote {out_dir / 'content.md'}")
    print(f"Total slides: {total_slides}, flagged: {total_flagged}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    out = Path(sys.argv[1])
    decks = []
    for arg in sys.argv[2:]:
        slug, _, path = arg.partition("=")
        if not path:
            print(f"Bad arg: {arg} (expected slug=path)")
            sys.exit(1)
        decks.append((slug, Path(path)))
    main(out, decks)
