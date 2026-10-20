#!/usr/bin/env bash
# Gate tests: the good fixture must pass every gate, the bad fixture (scenario T6) must fail G1 to G5.
cd "$(dirname "$0")/.." || exit 2
PASS=0; FAIL=0
ok()  { echo "ok   $1"; PASS=$((PASS+1)); }
bad() { echo "FAIL $1"; FAIL=$((FAIL+1)); }
python3 scripts/run_gates.py tests/fixture-good >/dev/null 2>&1 && ok "good fixture passes G1-G5" || bad "good fixture passes G1-G5"
python3 scripts/run_gates.py tests/fixture-bad  >/dev/null 2>&1 && bad "bad fixture must fail" || ok "bad fixture fails"
for g in "G1 facts" "G2 legal" "G3 seo" "G4 style" "G5 slop"; do
  python3 - "$g" <<'PY' && ok "T6: bad fixture fails $g" || bad "T6: bad fixture fails $g"
import json, sys
d = json.load(open("tests/fixture-bad/04-gates/gates.json"))
name = [k for k in d["gates"] if k.startswith(sys.argv[1])][0]
sys.exit(0 if not d["gates"][name]["pass"] else 1)
PY
done
python3 scripts/deslop_de.py --text "Wir sind ganzheitlich und nahtlos für Sie da." >/dev/null && bad "deslop_de catches German tells" || ok "deslop_de catches German tells"
python3 scripts/deslop_de.py --text "Das Finanzamt hat geschrieben. Jetzt zählt, was Sie vorher klären. Rufen Sie an, bevor Sie antworten." >/dev/null; [ $? -le 1 ] && ok "deslop_de runs on short clean text" || bad "deslop_de runs on short clean text"
python3 scripts/diff_claims.py diff tests/fixture-good/03-draft/draft-v1.md tests/fixture-bad/03-draft/draft-v1.md tests/fixture-good/01-brief/claims.json >/dev/null && bad "claim diff must catch a changed text" || ok "claim diff catches a changed text"
python3 scripts/check_legal.py --text "Wir sind spezialisiert und garantieren Straffreiheit." --mode brao >/dev/null && bad "legal catches BRAO terms" || ok "legal catches BRAO terms"
python3 scripts/check_legal.py --text "Die Behandlung heilt Migräne." --mode hwg >/dev/null && bad "legal catches HWG terms" || ok "legal catches HWG terms"
python3 scripts/wordcount.py tests/fixture-good/03-draft/draft-v1.md --bestand 60 >/dev/null && ok "wordcount floor" || bad "wordcount floor"
echo "passed $PASS, failed $FAIL"; [ "$FAIL" -eq 0 ]
# G6 hard checks (fixture-g6 must fail H2 late answer, H3 no source, H5 stuffing, H6 no date, H7 no credential, PAA)
OUT="$(python3 scripts/seo_coverage.py tests/fixture-g6 --json)"
for k in "H2 Direkt-Antwort beginnt zu spät" "H3 Vertiefungs-Block" "H5 Keyword-Stuffing" "H6 Seite zitiert" "H7 keine belegte" "PAA nicht beantwortet" "PAA verworfen ohne Grund"; do
  echo "$OUT" | grep -q "$k" && ok "G6 catches: $k" || bad "G6 catches: $k"
done
