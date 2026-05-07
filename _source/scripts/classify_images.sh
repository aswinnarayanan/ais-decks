#!/bin/bash
# Classify and name images via headless `claude -p`.
#
# Usage:
#   ./classify_images.sh [--limit N] [--resume]
#
# Reads:  _source/extracted/_image_manifest.json (unique image reps)
# Writes: _source/extracted/_rename_proposals.json (incrementally)
#
# Each call to claude is a fresh session, so there's no cumulative image limit.

set -uo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
MANIFEST="$ROOT/_source/extracted/_image_manifest.json"
PROPOSALS="$ROOT/_source/extracted/_rename_proposals.json"
ASSETS="$ROOT/_source/extracted/assets"
RESIZED="$ROOT/_source/extracted/_resized"

LIMIT=0
RESUME=0
for arg in "$@"; do
  case "$arg" in
    --limit) shift; LIMIT="$1"; shift ;;
    --limit=*) LIMIT="${arg#*=}" ;;
    --resume) RESUME=1 ;;
  esac
done

mkdir -p "$RESIZED"

# Init proposals file if missing
if [[ ! -f "$PROPOSALS" || $RESUME -eq 0 ]]; then
  echo "{}" > "$PROPOSALS"
fi

# Get list of representatives to process
REPS=$(python3 -c "
import json
m = json.load(open('$MANIFEST'))
done = json.load(open('$PROPOSALS'))
for x in m:
    if x['representative'] not in done:
        print(x['representative'])
")

TOTAL=$(echo "$REPS" | grep -c . || true)
if [[ $LIMIT -gt 0 ]]; then
  REPS=$(echo "$REPS" | head -n "$LIMIT")
  echo "Processing $LIMIT of $TOTAL remaining"
else
  echo "Processing $TOTAL remaining"
fi

PROMPT='Look at this image and reply with ONLY a single-line JSON object (no code fences, no prose):
{"name": "kebab-case-descriptive-name", "category": "<one of: logos, icons, diagrams, screenshots, figures, photos, graphics, misc>"}

Categories:
- logos: brand/organisation logos (e.g. "nif-logo", "kubernetes-logo")
- icons: generic stock icons (e.g. "icon-laptop", "icon-cloud")
- diagrams: technical/architectural illustrations (e.g. "neurodesk-architecture")
- screenshots: UI/file-listing screen captures (e.g. "screenshot-vscode-extension")
- figures: scientific figures, plots, brain renders (e.g. "brain-cortical-thickness-map")
- photos: people, events, venues
- graphics: decorative (e.g. "winding-road-graphic", "sciget-mascot-bilby")
- misc: unclassifiable

Use kebab-case. Be specific. No file extension.'

i=0
for rep in $REPS; do
  i=$((i+1))
  src="$ASSETS/$rep"
  if [[ ! -f "$src" ]]; then
    echo "[$i] MISSING: $rep" >&2
    continue
  fi

  # Resize copy to <=1024px if larger, leave SVGs alone
  ext="${rep##*.}"
  resized="$RESIZED/$rep"
  if [[ "$ext" == "svg" || "$ext" == "SVG" ]]; then
    cp "$src" "$resized"
  else
    sips -Z 1024 "$src" --out "$resized" >/dev/null 2>&1 || cp "$src" "$resized"
  fi

  # Call claude headless
  out=$(claude -p "$PROMPT

Image: @$resized" 2>/dev/null || true)

  # Extract JSON (first {...} on a line)
  json=$(echo "$out" | grep -oE '\{[^}]*"name"[^}]*\}' | head -1)

  if [[ -z "$json" ]]; then
    echo "[$i/$TOTAL] PARSE-FAIL: $rep — raw: $(echo "$out" | head -1)" >&2
    continue
  fi

  # Merge into proposals
  python3 -c "
import json, sys
proposals = json.load(open('$PROPOSALS'))
entry = json.loads('''$json''')
name = entry['name']
cat = entry['category']
ext = '$ext'.lower()
proposals['$rep'] = f'{cat}/{name}.{ext}'
json.dump(proposals, open('$PROPOSALS', 'w'), indent=2)
print(f'[{$i}/{$TOTAL}] $rep → {cat}/{name}.{ext}')
"
done

echo "Done. Proposals: $PROPOSALS"
