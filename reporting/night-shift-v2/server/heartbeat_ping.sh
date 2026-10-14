#!/bin/bash
# 741-agents-01 -> Healthchecks.io dead-man's-switch (canary check 741-server-heartbeat).
# Pings on a FIXED schedule regardless of whether any real task ran — proves the
# machine + scheduler are alive, independent of task success (canary-workflow spec).
# UUID file is dropped in by hand once Martin creates the Healthchecks.io account
# and canary-workflow sends the real check UUID; until then this is a harmless no-op.
set -u
UUID_FILE="/home/nightshift/741website/.secrets/healthchecks-uuid.txt"
LOG="/home/nightshift/.browser-display/health/heartbeat-ping.log"
mkdir -p "$(dirname "$LOG")"

if [ ! -s "$UUID_FILE" ] || grep -q "PLACEHOLDER" "$UUID_FILE" 2>/dev/null; then
  echo "[$(date '+%F %T')] stubbed: no real Healthchecks.io UUID in $UUID_FILE yet, skipping ping" >> "$LOG"
  exit 0
fi

UUID=$(cat "$UUID_FILE" | tr -d '[:space:]')
RESULT=$(curl -fsS -m 10 --retry 3 "https://hc-ping.com/$UUID" 2>&1)
echo "[$(date '+%F %T')] pinged hc-ping.com/${UUID:0:8}... result: $RESULT" >> "$LOG"
