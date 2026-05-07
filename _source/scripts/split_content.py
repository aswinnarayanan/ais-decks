#!/usr/bin/env python3
"""
Split _source/extracted/content.md into content/<stream>/<topic>.md files.

The MAPPING below assigns each (deck, slide_num) to a destination.
Special destinations:
  "_skip"     — section-divider / roadmap slides (handled by SectionNav component)
  "_unsorted" — needs manual review
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SRC = ROOT / "_source" / "extracted" / "content.md"
DEST = ROOT / "content"
UNSORTED = ROOT / "_source" / "extracted" / "_unsorted.md"

MAPPING = {
    # === Sydney (49 slides) ===
    ("sydney", 1):  "_planning",                  # workshop planning notes
    ("sydney", 2):  "_planning",                  # presentation planning notes
    ("sydney", 3):  "speaker-intro.md",
    ("sydney", 4):  "_skip",                      # roadmap divider
    ("sydney", 5):  "motivation/finding-sharing-workflows.md",
    ("sydney", 6):  "motivation/challenges-in-analysis.md",
    ("sydney", 7):  "motivation/installing-software-pain.md",
    ("sydney", 8):  "_skip",                      # roadmap divider
    ("sydney", 9):  "support-acknowledgements.md", # contributors list
    ("sydney", 10): "neurodesk/what-is-neurodesk.md",
    ("sydney", 11): "_skip",                      # section nav transition
    ("sydney", 12): "neurodesk/reproducible-workflows.md",
    ("sydney", 13): "neurodesk/portable-infrastructure.md",
    ("sydney", 14): "neurodesk/portable-infrastructure.md",
    ("sydney", 15): "neurodesk/portable-infrastructure.md",
    ("sydney", 16): "neurodesk/uptake-community.md",
    ("sydney", 17): "_skip",                      # roadmap divider
    ("sydney", 18): "ais/fdri-context.md",
    ("sydney", 19): "ais/what-is-ais.md",
    ("sydney", 20): "ais/architecture.md",
    ("sydney", 21): "ais/architecture.md",
    ("sydney", 22): "ais/architecture.md",
    ("sydney", 23): "ais/architecture.md",
    ("sydney", 24): "ais/architecture.md",
    ("sydney", 25): "ais/architecture.md",
    ("sydney", 26): "ais/architecture.md",
    ("sydney", 27): "ais/architecture.md",
    ("sydney", 28): "ais/architecture.md",
    ("sydney", 29): "_skip",                      # roadmap divider
    ("sydney", 30): "neurodesk/ui-new-tools.md",
    ("sydney", 31): "neurodesk/cloud-servers.md",
    ("sydney", 32): "neurodesk/virtual-desktops.md",
    ("sydney", 33): "neurodesk/computational-notebooks.md",
    ("sydney", 34): "neurodesk/neurodesk-edu.md",
    ("sydney", 35): "future/webassembly.md",
    ("sydney", 36): "future/webassembly.md",
    ("sydney", 37): "future/coding-agents.md",
    ("sydney", 38): "future/streamline-translation.md",
    ("sydney", 39): "future/mri-cutting-edge.md",
    ("sydney", 40): "future/mri-cutting-edge.md",
    ("sydney", 41): "_skip",                      # removed
    ("sydney", 42): "_skip",                      # removed (image moved to sydney 44)
    ("sydney", 43): "ais/collaboration-models.md",
    ("sydney", 44): "ais/open-data-workflow.md",
    ("sydney", 45): "motivation/need-for-fair.md", # FAIR citation
    ("sydney", 46): "_skip",                      # roadmap divider
    ("sydney", 47): "_skip",                      # removed
    ("sydney", 48): "_skip",                      # moved earlier via INSERT_AFTER
    ("sydney", 49): "_skip",                      # removed

    # === Sciget (58 slides) ===
    ("sciget", 1):  "_skip",                      # cover (will rebuild)
    ("sciget", 2):  "_skip",                      # roadmap divider
    ("sciget", 3):  "motivation/need-for-fair.md",
    ("sciget", 4):  "motivation/challenges-in-analysis.md",
    ("sciget", 5):  "motivation/finding-sharing-workflows.md",
    ("sciget", 6):  "motivation/installing-software-pain.md",
    ("sciget", 7):  "_skip",                      # roadmap divider
    ("sciget", 8):  "support-acknowledgements.md", # contributors
    ("sciget", 9):  "neurodesk/what-is-neurodesk.md",
    ("sciget", 10): "_skip",                      # section nav transition
    ("sciget", 11): "neurodesk/reproducible-workflows.md",
    ("sciget", 12): "neurodesk/portable-infrastructure.md",
    ("sciget", 13): "_skip",                      # section nav
    ("sciget", 14): "_skip",                      # section nav
    ("sciget", 15): "_skip",                      # section nav
    ("sciget", 16): "ais/collaboration-models.md",
    ("sciget", 17): "neurodesk/uptake-community.md",
    ("sciget", 18): "_skip",                      # roadmap divider
    ("sciget", 19): "ais/community-workshops.md",  # NIF workshop announcement
    ("sciget", 20): "ais/what-is-ais.md",          # AIS goals
    ("sciget", 21): "ais/community-workshops.md",  # workshop announcement variant
    ("sciget", 22): "ais/what-is-ais.md",          # "What is AIS?" content
    ("sciget", 23): "ais/architecture.md",         # AIS platform diagram
    ("sciget", 24): "sciget/from-neurodesk-to-sciget.md",
    ("sciget", 25): "sciget/communities.md",
    ("sciget", 26): "neurodesk/ui-new-tools.md",
    ("sciget", 27): "sciget/github-actions-build.md",
    ("sciget", 28): "neurodesk/cloud-servers.md",
    ("sciget", 29): "neurodesk/virtual-desktops.md",
    ("sciget", 30): "sciget/cvmfs-distribution.md",
    ("sciget", 31): "neurodesk/computational-notebooks.md",
    ("sciget", 32): "ais/collaboration-models.md",
    ("sciget", 33): "motivation/need-for-fair.md", # FAIR citation
    ("sciget", 34): "_skip",                      # roadmap divider
    ("sciget", 35): "sciget/xnat-deployment.md",
    ("sciget", 36): "sciget/xnat-deployment.md",
    ("sciget", 37): "sciget/xnat-deployment.md",
    ("sciget", 38): "sciget/xnat-deployment.md",
    ("sciget", 39): "sciget/xnat-deployment.md",
    ("sciget", 40): "sciget/xnat-deployment.md",
    ("sciget", 41): "sciget/xnat-deployment.md",
    ("sciget", 42): "sciget/xnat-deployment.md",
    ("sciget", 43): "sciget/xnat-deployment.md",
    ("sciget", 44): "_skip",                      # roadmap divider
    ("sciget", 45): "sciget/communities.md",       # ecosystem collage
    ("sciget", 46): "sciget/communities.md",       # ecosystem collage (extended)
    ("sciget", 47): "roadmap.md",
    ("sciget", 48): "support-acknowledgements.md",
    ("sciget", 49): "support-acknowledgements.md",
    ("sciget", 50): "_skip",                       # removed
    ("sciget", 51): "_skip",                       # removed
    ("sciget", 52): "_skip",                       # removed
    ("sciget", 53): "_skip",                       # removed
    ("sciget", 54): "_skip",                       # removed
    ("sciget", 55): "_skip",                       # removed
    ("sciget", 56): "_skip",                       # removed
    ("sciget", 57): "_skip",                       # removed
    ("sciget", 58): "ais/neurodesk-on-ais-demo.md",  # MRI viewer
}


def split():
    text = SRC.read_text()
    # Split by slide marker
    parts = re.split(r"(<!-- ===== (\w+) slide (\d+) =====[^\n]*-->)", text)
    # parts: [preamble, marker, deck, num, body, marker, deck, num, body, ...]

    buckets: dict[str, list[str]] = {}
    skipped = []
    unmapped = []

    i = 1
    while i < len(parts):
        marker = parts[i]
        deck = parts[i + 1]
        num = int(parts[i + 2])
        body = parts[i + 3] if i + 3 < len(parts) else ""
        slide_block = marker + body

        target = MAPPING.get((deck, num))
        if target is None:
            unmapped.append((deck, num))
            target = "_unsorted"

        if target in ("_skip", "_planning"):
            skipped.append((deck, num))
        else:
            buckets.setdefault(target, []).append(slide_block.rstrip())

        i += 4

    DEST.mkdir(exist_ok=True)
    for target, blocks in buckets.items():
        if target == "_unsorted":
            continue
        out = DEST / target
        out.parent.mkdir(parents=True, exist_ok=True)
        title = out.stem.replace("-", " ").title()
        content = f"# {title}\n\n" + "\n\n".join(blocks) + "\n"
        out.write_text(content)

    if "_unsorted" in buckets:
        UNSORTED.write_text(
            "# Unsorted slides (manual review)\n\n"
            "These slides need topic assignment. After deciding, edit "
            "`_source/scripts/split_content.py` MAPPING and re-run.\n\n"
            + "\n\n".join(buckets["_unsorted"]) + "\n"
        )

    print(f"Wrote {len([t for t in buckets if t != '_unsorted'])} topic files")
    print(f"Skipped {len(skipped)} section-divider/roadmap slides")
    print(f"Unsorted: {len(buckets.get('_unsorted', []))} slides → {UNSORTED}")
    if unmapped:
        print(f"WARNING: {len(unmapped)} slides not in MAPPING: {unmapped[:5]}...")


if __name__ == "__main__":
    split()
