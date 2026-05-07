#!/usr/bin/env python3
"""Finalise assets after user reviewed _collisions/.
- Resolves rename collisions based on what user kept/deleted in _collisions/
- Re-extracts content.md cleanly from pptx
- Applies resolved renames + contributor slide patch
- Cleans up real assets dir
"""
import json
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
EXTRACTED = ROOT / "_source" / "extracted"
ASSETS = EXTRACTED / "assets"
REVIEW = EXTRACTED / "_collisions"
PROPOSALS_PATH = EXTRACTED / "_rename_proposals.json"
CONTENT_MD = EXTRACTED / "content.md"

proposals = json.load(open(PROPOSALS_PATH))
manifest = json.load(open(EXTRACTED / "_image_manifest.json"))

# === Step 1: derive resolved proposals from _collisions/ filesystem state ===
orig_groups = defaultdict(list)
for orig, new in proposals.items():
    base = re.sub(r"-\d+(\.[^.]+)$", r"\1", new)
    orig_groups[base].append((orig, new))

survived = set(p.name for p in REVIEW.iterdir())

# resolved_target: orig_filename → final new_path
resolved = {}
asset_renames = {}  # old_path → new_path (for files in _source/extracted/assets/)
asset_deletes = set()  # paths in assets to delete

for base, members in orig_groups.items():
    base_path = Path(base)
    if len(members) <= 1:
        # Not a collision group — keep as-is
        for orig, new in members:
            resolved[orig] = new
        continue

    members.sort(key=lambda x: x[1])
    # Determine kept indices via review filenames
    kept_specs = []  # (review_idx, orig, old_new)
    deleted_orig = []
    for i, (orig, new) in enumerate(members, start=1):
        review_name = f"{base_path.stem}-{i}{base_path.suffix}"
        if review_name in survived:
            kept_specs.append((i, orig, new))
        else:
            deleted_orig.append(orig)

    if not kept_specs:
        # All deleted somehow — fallback: treat first as canonical
        kept_specs = [members[0] + (members[0][1],)]

    # Renumber survivors: first → base, second → -2, third → -3...
    for new_idx, (orig_idx, orig, old_new) in enumerate(kept_specs, start=1):
        if new_idx == 1:
            final_path = base
        else:
            final_path = f"{base_path.parent}/{base_path.stem}-{new_idx}{base_path.suffix}"
        resolved[orig] = final_path
        if old_new != final_path:
            asset_renames[old_new] = final_path

    # Deleted variants: merge into the new base (first survivor's final_path)
    new_base = resolved[kept_specs[0][1]]
    for orig in deleted_orig:
        resolved[orig] = new_base
    # Mark old paths of deleted variants for cleanup
    for i, (orig, old_new) in enumerate(members, start=1):
        review_name = f"{base_path.stem}-{i}{base_path.suffix}"
        if review_name not in survived:
            asset_deletes.add(old_new)

# === Step 2: re-extract content.md (only) by running extract_pptx to temp ===
TMP = EXTRACTED / "_tmp_extract"
shutil.rmtree(TMP, ignore_errors=True)
subprocess.run(
    [
        "python3",
        str(ROOT / "_source" / "scripts" / "extract_pptx.py"),
        str(TMP),
        f"sydney={ROOT}/_source/sydney-2026-neurodesk-draft.pptx",
        f"sciget={ROOT}/_source/eresearch-2025-sciget-final.pptx",
    ],
    check=True,
    capture_output=True,
)
fresh_md = (TMP / "content.md").read_text()
shutil.rmtree(TMP)

# === Step 3: apply resolved proposals + dupe-group expansion to content.md ===
# Build per-file map (every file in every dupe group → its final path)
file_to_final = {}
for entry in manifest:
    rep = entry["representative"]
    final = resolved.get(rep)
    if not final:
        continue
    for f in entry["all_files"]:
        file_to_final[f] = final

text = fresh_md
replaced = 0
for old, new in file_to_final.items():
    pattern = f"./assets/{old}"
    replacement = f"./assets/{new}"
    if pattern in text:
        text = text.replace(pattern, replacement)
        replaced += 1
print(f"Rewrote {replaced} image refs")

# === Step 4: re-apply contributor slide replacement ===
new_body = """
# Neurodesk contributors

![](../shared/assets/contributor-map.png)

A global community of researchers, engineers, and supporters.

"""
text = re.sub(
    r"(<!-- ===== sydney slide 9 =====[^\n]*-->\n).*?(?=<!-- ===== sydney slide 10)",
    r"\1" + new_body + "\n",
    text, count=1, flags=re.DOTALL,
)
text = re.sub(
    r"(<!-- ===== sciget slide 8 =====[^\n]*-->\n).*?(?=<!-- ===== sciget slide 9)",
    r"\1" + new_body + "\n",
    text, count=1, flags=re.DOTALL,
)
CONTENT_MD.write_text(text)
print("Re-applied contributor slide patch")

# === Step 5: clean up assets dir (apply renames + deletions) ===
# Delete files marked for deletion
for p in asset_deletes:
    fp = ASSETS / p
    if fp.exists():
        fp.unlink()
# Apply renames
for old, new in asset_renames.items():
    op = ASSETS / old
    np = ASSETS / new
    if op.exists() and not np.exists():
        np.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(op), str(np))

# === Step 6: write resolved proposals ===
json.dump(resolved, open(PROPOSALS_PATH, "w"), indent=2)
print(f"Wrote {len(resolved)} resolved proposals")
print(f"Asset deletes: {len(asset_deletes)}, asset renames: {len(asset_renames)}")
