#!/usr/bin/env bash
# Rival-model cleanse for German copy (gate G5). Claude wrote the draft, GPT cleanses it.
#
#   scripts/cleanse_de.sh draft.md > cleansed.md 2> notes.txt
#   TIMEOUT=240 scripts/cleanse_de.sh draft.md > cleansed.md
#
# stdout = copy, stderr = change notes. Exit 124 on timeout, 127 if codex is missing, 66 on empty input.
# ALWAYS follow with: python3 scripts/diff_claims.py diff draft.md cleansed.md claims.json
#                     python3 scripts/deslop_de.py cleansed.md --claims claims.json
# The draft text goes to OpenAI. Final draft only, never client source documents.
# The slopmonster cleanse.sh stays unchanged; this script has its own German prompt.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
PROMPT_FILE="$HERE/../prompts/cleanse-de.txt"
TIMEOUT="${TIMEOUT:-180}"

[ $# -ge 1 ] && [ -f "$1" ] && [ -r "$1" ] || { echo "cleanse_de: cannot read ${1:-<no file>}" >&2; exit 66; }
DRAFT="$(cat "$1")"
[ -n "$(printf '%s' "$DRAFT" | tr -d '[:space:]')" ] || { echo "cleanse_de: draft is empty" >&2; exit 66; }
FULL="$(cat "$PROMPT_FILE")

$DRAFT"

find_bin() { command -v "$1" 2>/dev/null || { [ -x "$HOME/.local/bin/$1" ] && echo "$HOME/.local/bin/$1"; }; }
CODEX="$(find_bin codex || true)"
[ -n "$CODEX" ] || { echo "cleanse_de: codex CLI not found. G5 cannot pass with a rival model." >&2; exit 127; }

NOTES_SENTINEL='<<<SLOPMONSTER-NOTES>>>'
emit_copy() {
  awk -v s="$NOTES_SENTINEL" '
    $0 == s { seen = 1; next }
    seen    { notes = notes $0 "\n"; next }
            { body = body $0 "\n" }
    END {
      if (!seen) {
        printf "%s", body
        print "cleanse_de: WARNING no " s " line in the reply. Check the tail before you ship." > "/dev/stderr"
        exit 0
      }
      sub(/\n+$/, "", body)
      printf "%s\n", body
      if (notes != "") { print "" > "/dev/stderr"; print "cleanse_de: what changed -" > "/dev/stderr"; printf "%s", notes > "/dev/stderr" }
    }'
}

OUT="$(mktemp)"; trap 'rm -f "$OUT"' EXIT
"$CODEX" exec --skip-git-repo-check --sandbox read-only "$FULL" >"$OUT" 2>&1 </dev/null &
PID=$!; WAITED=0
while kill -0 "$PID" 2>/dev/null; do
  if [ "$WAITED" -ge "$TIMEOUT" ]; then kill -9 "$PID" 2>/dev/null; wait "$PID" 2>/dev/null; echo "cleanse_de: timed out after ${TIMEOUT}s" >&2; exit 124; fi
  sleep 2; WAITED=$((WAITED + 2))
done
wait "$PID"; RC=$?
RAW="$(cat "$OUT")"
[ "$RC" -eq 0 ] || { echo "cleanse_de: codex exited $RC" >&2; printf '%s\n' "$RAW" | tail -5 >&2; exit "$RC"; }
BODY="$(printf '%s\n' "$RAW" | awk '$0=="codex"{buf="";on=1;next} $0=="tokens used"{on=0;next} on{buf=buf $0 "\n"} END{printf "%s", buf}')"
if [ -n "$(printf '%s' "$BODY" | tr -d '[:space:]')" ]; then printf '%s\n' "$BODY" | emit_copy; else printf '%s\n' "$RAW" | emit_copy; fi
