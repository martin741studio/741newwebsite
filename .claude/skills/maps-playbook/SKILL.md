---
name: maps-playbook
description: Runs the 741 Maps growth playbook for a local-SEO client. Checks 77 measures against evidence, marks each done, partly, missing, n/a or unknown, and turns gaps into ranked, gated task proposals. Trigger on "/maps-playbook <client>", "Maps-Playbook für <Kunde>", "was fehlt, damit <Kunde> auf Maps Platz 1 kommt", "Maßnahmen-Matrix", "was haben wir schon umgesetzt", or monthly refresh. Not for the audit (maps-audit) or clean-up (un-burning).
context: fork
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(python3:*), Bash(node:*), Bash(curl:*), Bash(git:*)
---

# maps-playbook

Source of truth: `00_project/maps-playbook-workflow.md`. Read it at the start of every run. Catalogue: `00_project/maps-playbook-measure-catalog.json` (77 measures). Design: `00_project/maps-playbook-design-note.md`, sheet: `00_project/maps-playbook-sheet-design.md`, report: `00_project/maps-playbook-report-wireframe.md`.
This skill is the build-up layer. It runs after the audit (diagnosis) and after un-burning (clean-up). Do not repeat their checks. Read their fields.

## Critical

- Nothing changes on a client asset (GBP, site, directories, ads) before Checkpoint C. Even with access: only note it.
- Every matrix cell has evidence (type, reference, date) and a confidence. No guess. No evidence gives `unknown`. Run `scripts/validate_run.py` before you show any matrix.
- Gates are not yours to decide. A gate measure needs its gate proof and Martin's go. Never send mail, never buy links, never ask customers for reviews, never reply to reviews.
- Gates 1-11: DBA name · reviews (no filter, no per-star bonus, consent for mail and SMS) · Reddit burying OUT · paid links · HWG · spam reports · profiles · address · tracking number · abandoned forms · best-of lists. Full text in the catalogue.

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

## Rules in short

- Status: `done`, `partly`, `missing`, `n/a`, `unknown`. Stale evidence shows `unknown` and keeps `last_known_status`. `client_stated` never sets `done`.
- Priority: `score = impact x confidence / (effort + risk)`, gaps only, dependencies override. Days 1-30: clean-up check, profile basics (G01-G03, G05-G08; G04 month 2), review engine (G14, G15, G17, G18), citations (O01-O05). Month 2+: pages, links, monitoring. A stale `unknown` gets a check task, not a change task.
- Caps (monthly refresh): 2 EUR paid data, 200 Falcon credits. Scans only after Martin's go. Never retry a scan. Log paid calls in `cost_ledger.jsonl`. Stop at the cap.
- Hard rules: collect and plan only until Checkpoint C. Master NAP wins over any generated pack. Client answers reviews. No Falcon auto-posts. Falcon only through the MCP (`scripts/falcon_read.py` is the read-only fallback). Sheets are XlsxWriter xlsx, never CSV, never openpyxl. Client mails only by Airmailer and never without Martin's go. Replies in STE. Client text in German prose, "du" for du clients.
- Martin guide (2026-10-12): rules in `00_project/assets/brand/martin-guide/README.md`. On the client board: point at the top 5 tasks, think at open gates. Max 1 callout per section, first person, every number with source and date, desktop and mobile screenshot.

Details (task states, script list with arguments, venv for `build_sheet.py`, test scenarios, registry): `references/gates-priorities-scripts.md`.

## Output

Per run: `run.json`, `matrix.json`, `tasks.json`, `evidence/`, `manifest.json`, `report/internal.html`, `report/client.html`, `matrix.xlsx`, `delta.json`, `change_log.jsonl`, `cost_ledger.jsonl`. Layout and drive rules: workflow spec section 11. The registry Excel updates itself through the Stop hook; keep `matrix.json` with `client` and `as_of`. Approval is manual: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py approve --client "<client>" --workflow phone` in the same turn.

## Verification (end of every run)

Run the validators. Open `report/internal.html` and the Sheet in Chrome and take a screenshot of each. Report the validator output, the screenshots and the Drive link. If a validator fails, fix and run it again. Do not report "done" without the output.

## References

- `references/gates-priorities-scripts.md`: priority detail, scripts, tests, registry
- `references/runbooks.md`: 21 runbooks, one per measure group
