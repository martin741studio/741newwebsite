---
name: maps-playbook
description: Run the 741 Maps growth playbook for a local-SEO client. Checks 77 measures (Google profile, website and conversion, off-page and PR) against existing evidence in Drive audits, sheets and live data. Marks each measure done, partly, missing, n/a or unknown. Turns gaps into ranked, gated task proposals. Trigger on "/maps-playbook <client>", "Maps-Playbook für <Kunde>", "was fehlt, damit <Kunde> auf Maps Platz 1 kommt", "Maßnahmen-Matrix", "was haben wir schon umgesetzt", or a monthly refresh. Do NOT use for the diagnosis audit (maps-audit), for clean-up of harm (un-burning), for page copy (seo-page-optimizer), for the homepage prototype (cro-homepage), for backlink outreach (backlink-dach) or for directory entries (Citations module).
context: fork
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(python3:*), Bash(node:*), Bash(curl:*), Bash(git:*)
---

# maps-playbook

Source of truth: `00_project/maps-playbook-workflow.md`. Read it at the start of every run. Catalogue: `00_project/maps-playbook-measure-catalog.json` (77 measures). Runbooks: `references/runbooks.md`. Design decisions: `00_project/maps-playbook-design-note.md`. Sheet design: `00_project/maps-playbook-sheet-design.md`. Report layout: `00_project/maps-playbook-report-wireframe.md`.
This skill is the build-up layer. It runs after the audit (diagnosis) and after un-burning (clean-up). Do not repeat their checks. Read their fields.

## Critical

- Nothing changes on a client asset (GBP, site, directories, ads) before Checkpoint C. Even with access: only note it.
- Every matrix cell has evidence (type, reference, date) and a confidence. No guess. No evidence gives `unknown`. Run `scripts/validate_run.py` before you show any matrix.
- Gates are not yours to decide. A gate measure needs its gate proof and Martin's go. Never send mail, never buy links, never ask customers for reviews, never reply to reviews.

## Inputs

Martin gives the client name and the niche (health, trades and local services, law and tax). Find the rest yourself: portal client ID, Drive folder, master NAP record, Place ID, last audit run, Falcon reports, `client_citations`, access grants. Ask only for what no file holds. Mark it `[FEHLT]`.

## Workflow

Copy this checklist into your reply and tick it off:

- [ ] Step 0: Readiness gate. Client, niche, IDs, Drive folder, audit evidence, un-burning state, access. Create the run folder `00_project/assets/maps-playbook/<slug>/<date>-<mode>/`.
- [ ] Step 1: Evidence harvest. Read Drive audits and sheets (read only), audit run JSON, Falcon reports (free), portal rows. Live checks only where evidence is older than its age rule (live 30, scan 60, document 180 days).
- [ ] Step 2: Status matrix. Write `matrix.json` (77 rows). Feed measures: worst audit field decides. Outcome fields never prove a process measure. Niche rules can set `n/a`.
- [ ] Step 3: Validate. Run `python3 -I scripts/validate_catalog.py <catalog>` and `python3 -I scripts/validate_run.py <catalog> <matrix>`. Fix until 0 errors.
- [ ] **Checkpoint A.** Show Martin the one-page board. Count his corrections in `run.json`. Wait for "go".
- [ ] Step 4: Tasks. Run `python3 -I scripts/score.py <catalog> <matrix> tasks.json [driver.json]`. Add action text from `references/runbooks.md`. Run `validate_run.py` with the tasks file.
- [ ] Step 5: Client bundle (draft). Client-safe page with approval boxes. No tool names, no team names, no price. HWG check for health. Build the Sheet with `scripts/build_sheet.py` (XlsxWriter) and render the board with `scripts/render_board.py`. Screenshot both in Chrome.
- [ ] **Checkpoint B.** Martin releases the bundle to the client. Wait.
- [ ] **Checkpoint C.** After the client approves, Martin gives one go per execution batch. Write the batch list (tasks, gates, executor, cost) and wait.
- [ ] Step 6: Execute and log. Agent tasks only, inside the listed batch. Log every change in `change_log.jsonl` with before and after.
- [ ] Step 7: Re-check changed and stale cells. Falcon by rhythm (2 weeks after changes, AI monthly, trend quarterly). Write `delta.json`.
- [ ] Step 8: Deliver. Drive link (after Martin's go to upload), screenshot as a file, client message draft in "ich" form, no call offers.

Steps 0 to 4 run unattended. Stop on a failed gate, a missing access or a spend over the cap.

## Status values

`done`, `partly`, `missing`, `n/a`, `unknown`. Evidence older than the rule shows `unknown` and keeps `last_known_status`. `client_stated` never sets `done`. Task states: `proposed`, `approved`, `blocked`, `in_progress`, `done`, `verified`.

## Priority

`score = impact x confidence / (effort + risk)`. Gaps only. Dependencies override the score. Days 1 to 30: clean-up check, profile basics (G01 to G03, G05 to G08; G04 follows in month 2), review engine (G14, G15, G17, G18), citations (O01 to O05). Month 2 onwards: pages, links, monitoring. Quick wins = top 5 P1 measures with a controllable audit driver. A stale `unknown` gets a check task, not a change task.

## Gates (full text in the catalogue)

1 DBA name · 2 reviews (no filter, no per-star bonus, consent for mail and SMS) · 3 Reddit burying OUT · 4 paid links · 5 HWG · 6 spam reports · 7 profiles · 8 address · 9 tracking number · 10 abandoned forms · 11 best-of lists.

## Caps

Monthly refresh: 2 EUR paid data and 200 Falcon credits. Scans only after Martin's go. Never retry a scan. Free reads have no cap. Log paid calls in `cost_ledger.jsonl`. Stop at the cap.

## Hard rules

Collect and plan only until Checkpoint C. Master NAP wins over any generated pack. Client answers reviews. No Falcon auto-posts. Falcon only through the MCP. Sheets are XlsxWriter xlsx, never CSV, never openpyxl. Client mails only by Airmailer and never without Martin's go. Replies in STE. Client text in German prose, "du" for du clients.

## Output

Per run: `run.json`, `matrix.json`, `tasks.json`, `evidence/`, `manifest.json`, `report/internal.html`, `report/client.html`, `matrix.xlsx`, `delta.json`, `change_log.jsonl`, `cost_ledger.jsonl`. Layout and drive rules: workflow spec section 11.

## Verification (end of every run)

Run the validators. Open `report/internal.html` and the Sheet in Chrome and take a screenshot of each. Report the validator output, the screenshots and the Drive link. If a validator fails, fix and run it again. Do not report "done" without the output.

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

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: on the client view of the board: point at the top 5 tasks, think at open gates. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
