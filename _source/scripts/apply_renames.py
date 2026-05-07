#!/usr/bin/env python3
"""Apply image renames: move unique files into category folders, rewrite content.md refs."""
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ASSETS = ROOT / "_source" / "extracted" / "assets"
MANIFEST = ROOT / "_source" / "extracted" / "_image_manifest.json"
PROPOSALS = ROOT / "_source" / "extracted" / "_rename_proposals.json"
CONTENT_MD = ROOT / "_source" / "extracted" / "content.md"

manifest = json.load(open(MANIFEST))
proposals = json.load(open(PROPOSALS))

# Build map: old_filename → new_path (category/name.ext)
# Same destination for all duplicates of the same hash.
old_to_new = {}
unmapped = []
for entry in manifest:
    rep = entry["representative"]
    new_path = proposals.get(rep)
    if not new_path:
        unmapped.append(rep)
        continue
    for f in entry["all_files"]:
        old_to_new[f] = new_path

print(f"Mapped {len(old_to_new)} files; {len(unmapped)} unmapped reps")

# Move unique files into category folders
moved = 0
for rep, new_path in [(e["representative"], proposals.get(e["representative"])) for e in manifest]:
    if not new_path:
        continue
    src = ASSETS / rep
    dst = ASSETS / new_path
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.exists() and not dst.exists():
        shutil.move(str(src), str(dst))
        moved += 1

# Remove the now-redundant duplicate files (same hash as rep, but original-named)
removed = 0
for entry in manifest:
    for f in entry["all_files"]:
        if f == entry["representative"]:
            continue
        p = ASSETS / f
        if p.exists():
            p.unlink()
            removed += 1

print(f"Moved {moved} unique files into category folders, removed {removed} duplicates")

# Rewrite content.md image refs
text = CONTENT_MD.read_text()
replaced = 0
for old, new in old_to_new.items():
    pattern = f"./assets/{old}"
    replacement = f"./assets/{new}"
    if pattern in text:
        text = text.replace(pattern, replacement)
        replaced += 1
CONTENT_MD.write_text(text)
print(f"Rewrote {replaced} image refs in content.md")
