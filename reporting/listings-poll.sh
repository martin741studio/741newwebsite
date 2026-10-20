#!/bin/bash
# Listings-Inbox-Poller-Runner (LaunchAgent, alle 10 Min).
# Interim auf dem Laptop; später auf den Dev-VPS umziehen.
set -euo pipefail
DIR="/Users/martindrendel/741website"
cd "$DIR"
OUT="$DIR/reporting/standup"; mkdir -p "$OUT"
echo "=== $(date '+%F %T') ===" >> "$OUT/listings-poll.log"
/opt/homebrew/bin/node reporting/listings-inbox-poller.mjs >> "$OUT/listings-poll.log" 2>&1 || echo "poller exit $?" >> "$OUT/listings-poll.log"
