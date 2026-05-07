#!/usr/bin/env python3
"""Detect and resolve name collisions in proposals, then move stranded files."""
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ASSETS = ROOT / "_source" / "extracted" / "assets"
MANIFEST_PATH = ROOT / "_source" / "extracted" / "_image_manifest.json"
PROPOSALS_PATH = ROOT / "_source" / "extracted" / "_rename_proposals.json"
CONTENT_MD = ROOT / "_source" / "extracted" / "content.md"

manifest = json.load(open(MANIFEST_PATH))
proposals = json.load(open(PROPOSALS_PATH))

# Find which reps have new_path collisions
target_to_reps = defaultdict(list)
for rep, new_path in proposals.items():
    target_to_reps[new_path].append(rep)

# For collisions, keep first rep at original name, append -2, -3 to others
fix_count = 0
for new_path, reps in target_to_reps.items():
    if len(reps) <= 1:
        continue
    # First wins. Add suffixes to others.
    for i, rep in enumerate(reps[1:], start=2):
        p = Path(new_path)
        new_name = f"{p.parent}/{p.stem}-{i}{p.suffix}"
        proposals[rep] = new_name
        fix_count += 1

# Save fixed proposals
json.dump(proposals, open(PROPOSALS_PATH, "w"), indent=2)
print(f"Fixed {fix_count} collisions")

# Build full old→new map (for ALL files via manifest dupe groups)
old_to_new = {}
for entry in manifest:
    rep = entry["representative"]
    new_path = proposals.get(rep)
    if not new_path:
        continue
    for f in entry["all_files"]:
        old_to_new[f] = new_path

# Now move any stranded files (still at root) to their proper destination
moved = 0
for entry in manifest:
    rep = entry["representative"]
    new_path = proposals.get(rep)
    if not new_path:
        continue
    src = ASSETS / rep
    dst = ASSETS / new_path
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.exists() and not dst.exists():
        shutil.move(str(src), str(dst))
        moved += 1
print(f"Moved {moved} stranded files into category folders")

# Rewrite content.md image refs (idempotent — only rewrite if pattern still matches old name)
text = CONTENT_MD.read_text()
replaced = 0
for old, new in old_to_new.items():
    pattern = f"./assets/{old}"
    replacement = f"./assets/{new}"
    if pattern in text:
        text = text.replace(pattern, replacement)
        replaced += 1
CONTENT_MD.write_text(text)
print(f"Rewrote {replaced} stale image refs in content.md")
