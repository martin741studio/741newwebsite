#!/bin/bash
# Server -> laptop: copy one night's results (REVIEW.md, state.json, items/, critic/) for the morning grill.
set -euo pipefail
DAY="${1:-$(TZ=Asia/Makassar date -v-1d +%F 2>/dev/null || date -d yesterday +%F)}"
REPO="$(cd "$(dirname "$0")/../../.." && pwd)"
DEST="$REPO/reporting/night-shift/server-$DAY"
mkdir -p "$DEST"
scp -q -r -o BatchMode=yes "741-agents-01:/home/nightshift/741website/reporting/night-shift/$DAY/." "$DEST/" || { echo "no server results for $DAY (Nachtlauf fehlt)"; exit 1; }
scp -q -o BatchMode=yes "741-agents-01:/home/nightshift/.browser-display/health/heartbeat.json" "$DEST/heartbeat.json" || true
echo "results $DAY -> $DEST"; ls "$DEST"
