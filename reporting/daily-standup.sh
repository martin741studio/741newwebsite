#!/bin/bash
# 741 Daily Client Standup — holt den Kundenstand aus Supabase und legt den Brief ab.
# Lauf: reporting/daily-standup.sh   (per cron werktags morgens)
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
set -a; . "$DIR/.secrets/standup.env"; set +a
OUT="$DIR/reporting/standup"; mkdir -p "$OUT"
DAY=$(date +%F)

TOKEN=$(curl -s --max-time 30 -X POST "$SUPABASE_URL/auth/v1/token?grant_type=password" \
  -H "apikey: $SUPABASE_ANON" -H "Content-Type: application/json" \
  -d "{\"email\":\"$STANDUP_EMAIL\",\"password\":\"$STANDUP_PASSWORD\"}" \
  | python3 -c "import sys,json;print(json.load(sys.stdin).get('access_token',''))")
[ -n "$TOKEN" ] || { echo "Login fehlgeschlagen" >&2; exit 1; }

curl -s --max-time 30 -X POST "$SUPABASE_URL/rest/v1/rpc/daily_standup" \
  -H "apikey: $SUPABASE_ANON" -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" -d '{}' > "$OUT/$DAY.json"

python3 "$DIR/reporting/render-standup.py" < "$OUT/$DAY.json" | tee "$OUT/$DAY.txt" > "$OUT/latest.txt"
echo "→ $OUT/$DAY.txt"
