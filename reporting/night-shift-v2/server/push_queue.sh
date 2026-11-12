#!/bin/bash
# Laptop -> server: copy tonight's CONFIRMED queue file to 741-agents-01 (Tailscale SSH).
# Called by the evening grill right after build_night_queue.py --write. No file = no night run (N34).
set -euo pipefail
DAY="${1:-$(TZ=Asia/Makassar date +%F)}"
REPO="$(cd "$(dirname "$0")/../../.." && pwd)"
Q="$REPO/reporting/night-shift/queue/$DAY.json"
[ -f "$Q" ] || { echo "no confirmed queue $Q, nothing pushed"; exit 1; }
scp -q -o BatchMode=yes "$Q" 741-agents-01:/home/nightshift/741website/reporting/night-shift/queue/
ssh -o BatchMode=yes 741-agents-01 "chown nightshift:nightshift /home/nightshift/741website/reporting/night-shift/queue/$DAY.json && ls -l /home/nightshift/741website/reporting/night-shift/queue/$DAY.json"
echo "queue $DAY on the server"
