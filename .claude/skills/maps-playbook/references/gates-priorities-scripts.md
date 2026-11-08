# maps-playbook: status, priority, gates, caps, scripts, tests, registry

Detail moved out of SKILL.md. Runbooks per measure group are in `runbooks.md`.

## Status values

`done`, `partly`, `missing`, `n/a`, `unknown`. Evidence older than the rule shows `unknown` and keeps `last_known_status`. `client_stated` never sets `done`. Task states: `proposed`, `approved`, `blocked`, `in_progress`, `done`, `verified`.

## Priority

`score = impact x confidence / (effort + risk)`. Gaps only. Dependencies override the score. Days 1 to 30: clean-up check, profile basics (G01 to G03, G05 to G08; G04 follows in month 2), review engine (G14, G15, G17, G18), citations (O01 to O05). Month 2 onwards: pages, links, monitoring. Quick wins = top 5 P1 measures with a controllable audit driver. A stale `unknown` gets a check task, not a change task.

## Gates (full text in the catalogue)

1 DBA name · 2 reviews (no filter, no per-star bonus, consent for mail and SMS) · 3 Reddit burying OUT · 4 paid links · 5 HWG · 6 spam reports · 7 profiles · 8 address · 9 tracking number · 10 abandoned forms · 11 best-of lists.

## Caps

Monthly refresh: 2 EUR paid data and 200 Falcon credits. Scans only after Martin's go. Never retry a scan. Free reads have no cap. Log paid calls in `cost_ledger.jsonl`. Stop at the cap.

## Test scenarios

1. Obvious: "/maps-playbook Praxis Suriya" loads the skill, runs Step 0, finds IDs and evidence without asking Martin.
2. Paraphrase: "Was fehlt noch, damit Hüwel in Nürnberg auf Maps Platz 1 kommt? Prüf auch, was schon erledigt ist." loads the skill and builds a matrix with a top-5 list.
3. Must not trigger: "Mach ein Maps-Audit für Stürzl" (audit), "Trag Hüwel bei Gelbe Seiten ein" (Citations module), "Schreib den Text für die Leistungsseite" (seo-page-optimizer).

## Scripts

All run with `python3 -I` from the repo root. `build_sheet.py` needs a venv with XlsxWriter (system Python is locked): `python3 -m venv <dir> && <dir>/bin/pip install XlsxWriter`.

- `scripts/validate_catalog.py <catalog>`: checks the 77 measures, gates, runbooks, dependency cycles.
- `scripts/validate_run.py <catalog> <matrix> [tasks]`: evidence, age by `rule_source`, confidence, n/a reasons, gate flags, score check.
- `scripts/score.py <catalog> <matrix> <out tasks> [driver.json]`: ranked tasks. Unknown cells get check tasks.
- `scripts/build_sheet.py <catalog> <matrix> <tasks> <out.xlsx> [label]`: client workbook, 7 tabs.
- `scripts/render_board.py <catalog> <matrix> <tasks> <out.html> [conflicts.json]`: internal board. Reference output: `assets/board-prototype.html`.
- `scripts/falcon_read.py tools | schema <tool> | call <tool> '<json>' [out.json]`: read-only Local Falcon over the MCP endpoint, for sessions without the MCP configured. Key from `.env`, never printed. Refuses scans. Use `getLocalFalconGbp*` and `listLocalFalconGbp*` for live GBP data (needs the OAuth-connected place ID).
- `references/runbooks.md`: 21 runbooks, one per measure group.

## Registry entry (2026-10-11)

Every run of this workflow is recorded in the workflow registry. The Excel `~/Desktop/Workflow-Uebersicht.xlsx` shows per client whether the workflow ran, its state, the last run, Martin's approval and the folder links.
- At the start or end of a run: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py upsert --client "<client>" --workflow phone --status "in Arbeit|Trockenlauf|fertig, Freigabe offen" --local <folder> --drive <url> --result <file>`
- When Martin approves the result: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py approve --client "<client>" --workflow phone` in the same turn, then tell Martin the sheet was updated. A hook reminds Claude when a message sounds like an approval.
Workflow id: `phone` (Get the phone to ring / Maps Playbook).

## Registry: automatic (2026-10-11)

The overview Excel `~/Desktop/Workflow-Uebersicht.xlsx` updates itself. A Stop hook runs `workflow_registry.py sync --quiet` after every turn. You do not call `upsert` for normal progress. Keep `matrix.json` in the run folder with the fields `client` and `as_of`. A folder name with `dryrun` marks a test run.
For any other file layout, write `_run.json` in the run folder (schema in `00_project/workflow-registry/README.md`). Only the approval stays manual: when Martin approves a result, run `approve` in the same turn and say that the Excel is updated.

