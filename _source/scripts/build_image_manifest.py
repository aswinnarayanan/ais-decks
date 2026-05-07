#!/usr/bin/env python3
"""Hash images, group by content, emit manifest of unique representatives + dupe groups."""
import hashlib
import json
import sys
from pathlib import Path

assets_dir = Path(sys.argv[1])
out_path = Path(sys.argv[2])

groups: dict[str, list[str]] = {}
for f in sorted(assets_dir.iterdir()):
    if not f.is_file():
        continue
    h = hashlib.sha256(f.read_bytes()).hexdigest()
    groups.setdefault(h, []).append(f.name)

manifest = []
for h, files in groups.items():
    # Pick alphabetically first as representative
    rep = files[0]
    manifest.append({"hash": h, "representative": rep, "all_files": files})

manifest.sort(key=lambda x: x["representative"])
out_path.write_text(json.dumps(manifest, indent=2))
print(f"Wrote {out_path}: {len(manifest)} unique images, {sum(len(m['all_files']) for m in manifest)} total files")
