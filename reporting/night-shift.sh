#!/bin/bash
# 741 Night Shift — page specs + audits, staged for morning review.
# Lauf: reporting/night-shift.sh   (LaunchAgent studio.741.night-shift, Mo–Fr 20:00, Fenster 20:00–22:59)
# Spec: .claude/skills/night-shift/SKILL.md · Blueprint: 00_project/night-shift-blueprint.md
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

# Concurrency lock: exactly one run at a time. A manual test (NIGHT_ALLOW_ANYTIME=1) that
# overlaps the 20:00 LaunchAgent trigger caused two processes to race on the same day's
# output folder (found 2026-09-15). Atomic mkdir; stale locks (>4h, i.e. a crashed run)
# are cleared automatically so a dead lock can never block future nights.
LOCKDIR="$DIR/reporting/night-shift/.lock"
if ! mkdir "$LOCKDIR" 2>/dev/null; then
  if [ -f "$LOCKDIR/pid" ] && [ -n "$(find "$LOCKDIR" -maxdepth 0 -mmin +240 2>/dev/null)" ]; then
    echo "[$(date '+%F %T')] stale lock (>4h) — clearing and taking over" >> "$DIR/reporting/night-shift/night-shift.log"
    rm -rf "$LOCKDIR"; mkdir "$LOCKDIR"
  else
    echo "[$(date '+%F %T')] another night-shift run is already in progress (lock held by pid $(cat "$LOCKDIR/pid" 2>/dev/null)) — exiting" | tee -a "$DIR/reporting/night-shift/night-shift.log"
    exit 0
  fi
fi
echo $$ > "$LOCKDIR/pid"
trap 'rm -rf "$LOCKDIR"' EXIT

DAY=$(date +%F)
OUT="$DIR/reporting/night-shift/$DAY"; mkdir -p "$OUT"/{specs,audits,critic}
LOG="$DIR/reporting/night-shift/night-shift.log"
MODEL="${NIGHT_MODEL:-claude-sonnet-5}"
MAX_TURNS="${NIGHT_MAX_TURNS:-40}"
MAX_INVOCATIONS=14; USED=0

# Evening window: 20:00–22:59 only. NIGHT_ALLOW_ANYTIME=1 bypasses (manual daytime test run).
WINDOW_START_H=20; WINDOW_END_H=23   # run must START before hour 23 (i.e. within 20:00–22:59)
NOW_H=$(date +%H | sed 's/^0//')
if [ "${NIGHT_ALLOW_ANYTIME:-0}" != "1" ]; then
  if [ "$NOW_H" -lt "$WINDOW_START_H" ] || [ "$NOW_H" -ge "$WINDOW_END_H" ]; then
    echo "[$(date '+%F %T')] outside evening window ($WINDOW_START_H:00–$((WINDOW_END_H-1)):59) — not starting. Use NIGHT_ALLOW_ANYTIME=1 to force." | tee -a "$LOG"
    exit 0
  fi
fi
# Hard stop at 23:00 regardless of the 3h budget, so a late start can't run past the window.
TODAY_2300=$(date -v23H -v0M -v0S +%s 2>/dev/null || date -d "$(date +%F) 23:00:00" +%s)
BUDGET_DEADLINE=$(( $(date +%s) + 3*3600 ))
if [ "${NIGHT_ALLOW_ANYTIME:-0}" = "1" ]; then
  DEADLINE=$BUDGET_DEADLINE
else
  DEADLINE=$BUDGET_DEADLINE
  [ "$TODAY_2300" -lt "$DEADLINE" ] && DEADLINE=$TODAY_2300
fi
# Global `node` is v26.x, which crashes the bundled claude-code CLI (Node 26 API break in a
# vendored auth dependency). Use the known-good Homebrew node@22 explicitly. Re-check with
# `node -v` if this ever needs to move; see memory night-shift-agent for the 2026-09-15 finding.
CLAUDE_NODE=/opt/homebrew/opt/node@22/bin/node
CLAUDE=/usr/local/bin/claude

log(){ echo "[$(date '+%F %T')] $*" | tee -a "$LOG"; }
over_budget(){ [ "$USED" -ge "$MAX_INVOCATIONS" ] || [ "$(date +%s)" -ge "$DEADLINE" ]; }
run(){ # run <role> <prompt>  — one fresh-context invocation
  USED=$((USED+1)); log "invocation $USED/$MAX_INVOCATIONS: $1"
  "$CLAUDE_NODE" "$CLAUDE" -p "$2" --model "$MODEL" --max-turns "$MAX_TURNS" \
    --permission-mode acceptEdits --output-format text 2>>"$LOG" || log "$1 exited $?"
}

[ -f "$OUT/state.json" ] || echo "{\"date\":\"$DAY\",\"model\":\"$MODEL\",\"budget\":{\"pages_max\":6,\"invocations_max\":$MAX_INVOCATIONS,\"invocations_used\":0},\"plan\":[],\"pages\":{},\"stopped_reason\":null}" > "$OUT/state.json"
log "=== night shift $DAY start (model $MODEL) ==="

# 0. Fetch Supabase context via REST/curl — the standalone `claude -p` CLI has NO Supabase
#    MCP tool (that only exists inside the Desktop-app-launched interactive session). Bash
#    fetches everything up front so Planner/Executor only ever Read a local file.
fetch_context(){
  set -a; . "$DIR/.secrets/standup.env"; set +a
  local TOKEN; TOKEN=$(curl -s --max-time 20 -X POST "$SUPABASE_URL/auth/v1/token?grant_type=password" \
    -H "apikey: $SUPABASE_ANON" -H "Content-Type: application/json" \
    -d "{\"email\":\"$STANDUP_EMAIL\",\"password\":\"$STANDUP_PASSWORD\"}" \
    | python3 -c "import sys,json;print(json.load(sys.stdin).get('access_token',''))")
  [ -n "$TOKEN" ] || { log "fetch_context: login failed"; return 1; }
  local H=(-H "apikey: $SUPABASE_ANON" -H "Authorization: Bearer $TOKEN")
  curl -s --max-time 20 "${H[@]}" "$SUPABASE_URL/rest/v1/programs?status=eq.running&select=id,client_id,start_date,end_date,clients(id,name)" > "$OUT/_programs.json"
  curl -s --max-time 20 "${H[@]}" "$SUPABASE_URL/rest/v1/tasks?status=neq.done&track=eq.B&select=id,client_id,week,track,title,status&order=week,sort" > "$OUT/_tasks.json"
  curl -s --max-time 20 "${H[@]}" "$SUPABASE_URL/rest/v1/report_feedback?verdict=eq.aenderung&select=id,client_id,report_slug,section_key,comment,created_at&order=created_at.asc" > "$OUT/_feedback_raw.json"
  curl -s --max-time 20 "${H[@]}" "$SUPABASE_URL/rest/v1/client_locations?nap_status=eq.locked&select=client_id,business_name,street,postal_code,city,country,phone,primary_category" > "$OUT/_nap.json"
  local LEDGER="$DIR/reporting/night-shift/processed-feedback.json"
  [ -f "$LEDGER" ] || echo "[]" > "$LEDGER"
  python3 - "$OUT" "$LEDGER" <<'PYEOF'
import json,sys,os
out,ledger_path=sys.argv[1],sys.argv[2]
def load(name):
    try: return json.load(open(os.path.join(out,name)))
    except Exception: return []
programs=load("_programs.json"); tasks=load("_tasks.json")
feedback=load("_feedback_raw.json"); nap=load("_nap.json")
processed=set(json.load(open(ledger_path))) if os.path.exists(ledger_path) else set()
by_client={p['client_id']: p for p in programs if isinstance(p,dict) and 'client_id' in p}
ctx={
  "programs": programs,
  "tasks": [t for t in tasks if isinstance(t,dict) and t.get('client_id') in by_client],
  "feedback_open": [f for f in feedback if isinstance(f,dict) and f.get('id') not in processed and f.get('client_id') in by_client],
  "nap_locked": nap,
}
json.dump(ctx, open(os.path.join(out,"context.json"),"w"), indent=2, default=str)
print(f"context.json: {len(ctx['programs'])} programs, {len(ctx['tasks'])} open tasks, {len(ctx['feedback_open'])} open feedback, {len(ctx['nap_locked'])} locked NAP")
PYEOF
  rm -f "$OUT"/_programs.json "$OUT"/_tasks.json "$OUT"/_feedback_raw.json "$OUT"/_nap.json
}
fetch_context || { log "fetch_context failed — aborting run"; exit 1; }
log "context fetched: $(cat "$OUT/context.json" | python3 -c 'import json,sys;c=json.load(sys.stdin);print(len(c["programs"]),"programs,",len(c["tasks"]),"tasks,",len(c["feedback_open"]),"feedback")')"

# 1. Planner — reads context.json directly, no Supabase tool needed/available
run PLANNER "Use the night-shift skill as PLANNER. Working dir: $OUT. Read state.json and context.json (already fetched — programs/tasks/feedback_open/nap_locked; do NOT try to query Supabase yourself, no MCP tool for it exists in this invocation). Build plan.json from context.json (max 2 clients, max 3 pages each, open feedback first) and update state.json. Do not write content."

# 2. Executor + Critic per page
PAGES=$(python3 -c "import json;p=json.load(open('$OUT/plan.json'));print(len(p))" 2>/dev/null || echo 0)
log "planned pages: $PAGES"
i=0
while [ "$i" -lt "$PAGES" ] && [ "$i" -lt 6 ]; do
  over_budget && { log "budget reached before page $i"; break; }
  attempt=1
  while [ "$attempt" -le 2 ]; do
    over_budget && break
    rm -f "$OUT/.verdict_$i"
    run EXECUTOR "Use the night-shift skill as EXECUTOR. Working dir: $OUT. Read state.json and plan.json; process plan item index $i (attempt $attempt). If attempt 2, read the critic fail list first. Assemble the data package (seo-page-optimizer references/data-package.md), write the spec/audit file, update state.json."
    over_budget && break
    run CRITIC "Use the night-shift skill as CRITIC. Working dir: $OUT. Grade plan item index $i against seo-page-optimizer references/scoring-rubric.md and the six hard checks. Write critic/<client>/<slug>.json and set state.json pages[...].status to pass or retry. Then write the single word pass or retry (nothing else) to $OUT/.verdict_$i -- this is how the runner decides whether to stop or try again; it must match your verdict exactly. Never edit the spec."
    PASS=$(cat "$OUT/.verdict_$i" 2>/dev/null | tr -d "[:space:]")
    [ "$PASS" = "pass" ] && break
    attempt=$((attempt+1))
  done
  i=$((i+1))
done

# 3. Reviewer (always runs, even after a breaker)
run REVIEWER "Use the night-shift skill as REVIEWER. Working dir: $OUT. Read state.json, plan.json and all critic files. Write REVIEW.md in the blueprint format (00_project/night-shift-blueprint.md §5) and append one summary line to $DIR/reporting/night-shift/LOG.md. Do not edit any spec."
log "=== night shift $DAY end · invocations $USED ==="
echo "→ $OUT/REVIEW.md"
