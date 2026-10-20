# Maps growth playbook: workflow spec (workflow `maps-playbook`)

Status: DESIGN APPROVED by Martin at checkpoint 1 (2026-10-11). Version 0.1. Nothing is installed. No table is created. Nothing is written to Drive.
Language: STE. German labels are the words of Martin's board. Field keys and metadata names are English.
Companion files: `maps-playbook-design-note.md` (use cases, decisions, tests), `maps-playbook-coverage-map.md`, `maps-playbook-measure-catalog.json` (77 measures), `maps-playbook-sheet-design.md`, `maps-playbook-report-wireframe.md`, `maps-playbook-schema.draft.sql`, `maps-playbook-skill/` (skill draft).

## Contents

1. Goal and scope
2. Interfaces
3. Inputs and trigger
4. Pipeline and checkpoints
5. Status logic and evidence rules
6. How the matrix is computed
7. Priority and plan
8. Gates
9. Execution and approval rules
10. Cost and caps
11. Outputs
12. Data model
13. Hard rules
14. Success measures
15. Done criteria and tests
16. Open questions

---

## 1. Goal and scope

Goal: put the client at the top of Google Maps, and make the website rank and convert. The playbook is the **build-up layer**. It runs after the audit has diagnosed and after un-burning has cleaned up.

It does four things:
1. It checks each of the 77 measures against evidence that already exists (Drive audits and sheets, audit run files, Falcon reports, portal data) and against live checks.
2. It marks each measure `done`, `partly`, `missing`, `n/a` or `unknown`.
3. It turns gaps into ranked task proposals with a gate, an owner type and a cost.
4. It tracks the client approval, the execution batch and the re-check.

Out of scope: diagnosis (audit), clean-up of harm (un-burning), page content ranking (content pool), page copy (`seo-page-optimizer`), CRO prototype (`cro-homepage`), backlink outreach (`backlink-dach`), directory submission (Citations module). The playbook **calls** these. It does not copy their steps.

## 2. Interfaces

| Neighbour | Role | Playbook takes | Playbook gives |
| --- | --- | --- | --- |
| Audit (`audit-workflow-spec.md`) | Diagnosis | Field status, evidence ID and date for every measure with an audit feed (69 of 77). Driver result `B11.09` and fit check `B11.08` | A re-audit request when key fields are red, missing or older than the age rule |
| Un-burning (`un-burning-workflow.md`) | Removes harm. Its bedrock check says when growth SEO may start | `harm-register.json` and the bedrock light per area (A to E). Check IDs `UB.A01` to `UB.E05`. Measures with `unburn_checks` in the catalogue (G01, G02, G04, G20 to G22, W13, W14, W18, W19, W34, O02 to O04, O16, O19) wait while a matching harm item is open | A list of harm found while checking. The playbook never fixes harm. Boundary: harm (exists and damages) = un-burning. Gap (missing and would add growth) = playbook |
| Content pool (`content-pool-design-note.md`) | Ranks page content | Pool items for page measures (W09 to W15, W26 to W31) | Page tasks with status. The pool decides what to write. The playbook tracks if it exists |
| `seo-page-optimizer`, `cro-homepage` | Write and build pages | Nothing | Task with target page and measure ID |
| `backlink-dach`, Citations module | Links and directories | Target sheets, `client_citations` status | Tasks for O01 to O16 with phase and gate |
| 90-day program | Client timeline | Open: file is missing | Tasks use the same phase labels (`d1-30`, `m2+`, `later`) |
| Portal and night shift | Task list, overnight content specs | Access grants, open tasks | Approved tasks. Night shift reads only content tasks. It never publishes |

Rule: the playbook never recomputes an audit field. If an audit field is missing or stale, the playbook asks for an audit re-run or a live check of that one field, and it labels the result `derived`.

## 3. Inputs and trigger

Trigger: `/maps-playbook <client>` or natural phrases such as "Maps-Playbook für Suriya" or "Was fehlt, damit Hüwel auf Maps Platz 1 kommt?".
Martin gives: client name and niche (health, trades and local services, law and tax). Nothing else.
The agent finds itself: portal client ID, Drive folder, NAP master record, Place ID, last audit run, Falcon reports, `client_citations`, access grants. It asks only for what no file holds. It marks the rest `[FEHLT]`.

## 4. Pipeline and checkpoints

```
Step 0  Readiness gate     client, niche, IDs, Drive folder, audit evidence, un-burning state, access grants
Step 1  Evidence harvest   Drive audits and sheets, audit run JSON, Falcon reports (free), portal, GSC and GA4. Live checks where stale
Step 2  Status matrix      build_matrix.py assigns status from audit feed and rules. Agent fills measures without a feed
Step 3  Validate           validate_run.py: evidence, date, age, gate flags, no guess
        == CHECKPOINT A: Martin reads the one-page board. Corrections are counted ==
Step 4  Gaps to tasks      score.py writes tasks.json. The agent adds action text. validate_run.py checks it
Step 5  Client bundle      client-safe report page with approval boxes. No tool names, no team names. HWG check
        == CHECKPOINT B: Martin releases the bundle to the client ==
        (client approves the bundle)
        == CHECKPOINT C: Martin gives one go per execution batch ==
Step 6  Execute and log    agent tasks run with access. Humans send outreach and review asks. Every change is logged
Step 7  Re-check           re-check changed and stale cells. Falcon by rhythm. Delta board
Step 8  Deliver            Drive link, screenshot as file, client message draft (ich form, no call offers)
```

Unattended: Steps 0 to 4. The run stops on a failed gate, a missing access or a spend over the cap.
Between the checkpoints agents run alone. No client asset changes before Checkpoint C.

Step 0 detail (readiness gate):
- If an audit run exists and is younger than its age rules: use it.
- If not: use Drive audits and sheets as evidence with their age. Check live where stale. Suggest an audit re-run if the key fields (B05.02, B05.06, B10.01, B13.01, B13.02) are red or missing.
- Read the un-burning bedrock check. Client ready for growth SEO = areas A to E green or grey, and C, D, E green. If not ready: still build the matrix, but mark every measure with open `unburn_checks` as `blocked_by: un-burning` and cite the harm row ID. Do not plan these measures. Others may start.
- Shared first client: Praxis Suriya is also the first client of un-burning. Reuse its baselines (`00_project/assets/un-burning/praxis-suriya/baseline/`). Never run a check twice.
- Readiness for paid links (O13): review pace and on-page must be solid. If not, mark `blocked`.

## 5. Status logic and evidence rules

| Status | Meaning |
| --- | --- |
| `done` | In place. Evidence is fresh |
| `partly` | A part is in place. The finding names what is missing |
| `missing` | Not in place |
| `n/a` | Not relevant. The finding names the reason (niche rule, no premises, not allowed, OUT) |
| `unknown` | No data, or evidence older than the age rule. Never a guess |

Task states are separate: `proposed`, `approved`, `blocked` (names the blocker), `in_progress`, `done`, `verified`. A measure becomes `done` only when new evidence shows it. A finished task is not evidence.

Evidence rules:
1. Every status cell has at least one evidence item: type, reference, date, note.
2. Each evidence item has a role. `rule_source` carries the status and sets the age. `secondary_claim` (memory note, portal task marked done, draft text) never sets status or age. Default: `rule_source`.
3. Reference means a file path, Drive file ID, URL, Falcon report key, audit field with run ID, or a table and row ID. A screenshot is a file in the run folder.
4. Types and age rules: `live` 30 days, `scan` 60 days, `document` 180 days. Legal facts (name, address, licence) are documents.
5. If the newest `rule_source` evidence is older than its rule, the cell shows `unknown`. The old status stays in `last_known_status`.
6. Confidence: `verified` (read from the source today or inside the rule), `derived` (computed from verified fields), `client_stated` (client said so, no proof). `client_stated` never sets `done`.
7. Conflicts between sources are findings. Example: an old aggregator pack shows an old business name while the master record shows another. The matrix reports the conflict and uses the master record.
8. Volume 0 means no data. The agent runs the autocomplete check first.
9. **Absence.** A 741-side artefact (page, document, config) that is missing from repo, Drive and Supabase after a logged search is `missing`. A client-side fact with no data is `unknown`. A portal task marked done is a claim, not proof.
10. **Default off.** A measure with `default_off` (G10 for health, G13, W24) is `n/a` until Martin switches it on for the client.
11. **Needs audit.** Measures with `needs_audit` (G06, G07, G17, W07, W15) cannot be `done` without audit data (driver category, leader pace, local points, approved tree). Without it they stay `partly` or `unknown`.

## 6. How the matrix is computed

1. **Feed measures** (audit feed present): feed status = worst of the feed fields. Red gives `missing`. Yellow gives `partly`. Grey gives `n/a`. Unknown gives `unknown`. `done` needs all feed fields green.
2. **Outcome versus process.** An outcome field alone does not prove a process measure. Example: review pace (B05.03) green does not set G14 (review process) `done`. G14 needs process evidence (client form, staff rule, card in use). The catalogue marks these with automation code `E` or `D`.
3. **Measures without a feed** (G04, G10 to G16, G19 to G22 and others): the agent reads the evidence sources named in the catalogue. No source gives `unknown`.
4. **Niche rule.** The catalogue field `niche_rules` can set `n/a` or tighten a check. Example: G10 for a Heilpraktikerin is `n/a` by HWG default.
5. **Gate measures** show the gate flag in the matrix. A gate measure never goes to Step 6 without its gate proof.
6. **Driver rule.** For G06, G07, G08, G14, G15 and G17 the impact comes from the audit driver result (`B11.09`). If the audit shows a controllable driver gap, impact is 5. If reviews are not a driver in this market, G14 and G17 drop to impact 3.

`build_matrix.py` does steps 1 to 5. The agent does the evidence work for step 3.

## 7. Priority and plan

`score = impact x confidence / (effort + risk)`

| Part | Scale | Source |
| --- | --- | --- |
| impact | 1 to 5 | Catalogue `impact_base`. Driver measures use the audit result (section 6, rule 6) |
| confidence | 0.5 to 1 | `verified` 1, `derived` 0.75, `client_stated` 0.5 |
| effort | S 1, M 2.5, L 4.5 | Catalogue `effort` |
| risk | 0 to 3 | DO 0. Gate 2. High gates (1, 2, 4, 7, 8) 3 |

Rules:
- Only gaps (`missing`, `partly`, `unknown`) get a task. `done` and `n/a` do not.
- Dependencies override the score. A task with an open dependency is `blocked`, not ranked.
- Phase `d1-30` comes first: clean-up check, profile basics (G01 to G03, G05 to G08; G04 follows in month 2), review engine (G14, G15, G17, G18), citations (O01 to O05). From month 2: pages, links, monitoring, conversion. `later` waits for Martin.
- **Top-of-Maps quick wins** = top 5 by score among P1 measures with a controllable audit driver.
- Health clients: every task with gate 5 shows "HWG check" as its first step.
- A measure that is `unknown` (stale or no data) gets a **check task** (effort S, no gate), not a change task. A blocked measure keeps its blocker.

## 8. Gates

The catalogue holds the full text (`gates` in the JSON). Short form:

| Gate | Rule |
| --- | --- |
| 1 DBA name | Only a real legal designation that shows on signage, imprint and site. Audit field `B13.03` stays red until proof exists |
| 2 Reviews | Ask every customer. No filter. No per-star bonus (OUT). Mail or SMS requests need consent. A BGH ruling treats an unrequested review mail as unlawful advertising (checked 11.10.2026, not legal advice) |
| 3 Reddit | Burying is OUT. Watch and answer with real help |
| 4 Paid links | Only the `backlink-dach` buy path. Label every paid article. Donation for a link counts as paid |
| 5 Health | HWG check on photos, offers, prices, project reports, embedded reviews |
| 6 Spam reports | Genuine and documented only. Evidence log first |
| 7 Profiles | Only own real locations and own former profiles |
| 8 Address | Only a real eligible address. Service-area profiles keep their setting |
| 9 Tracking number | Main number stays primary. Dynamic numbers show only after consent |
| 10 Abandoned forms | No data stored before consent. Health data off |
| 11 Best-of lists | Neutral criteria. No fake ranking. Labelled as own list |

A gate task needs: the proof named in `gate_text`, the matrix cell, and Martin's go inside Checkpoint C. The agent never decides a gate alone.

## 9. Execution and approval rules

| Who | May do alone | Needs a go | Never |
| --- | --- | --- | --- |
| Agent | Read sources, free Falcon reads, live checks, build matrix, score, draft texts, specs, mail drafts, report pages (local files) | Edit GBP or site with access (Checkpoint C). Upload to Drive. Write to a table. Run a paid scan | Send mail or messages. Buy links. Ask customers for reviews. Post content without go. Reply to reviews. Click CAPTCHAs |
| 741 team | Execute approved tasks. Send outreach by Airmailer | — | Change a gate measure without the gate proof |
| Client | Approve the bundle. Give photos, review asks, decisions, access | — | — |

Approval chain: client approves the bundle on the report page, then Martin gives one go per execution batch (one pillar group, a listed set of changes). Each change is logged with before and after, date, executor and evidence ID. Nothing runs outside the listed batch. One go does not cover the next batch.
Website changes follow the rule "no website changes without go": per batch, never in place on a live page for page swaps (see memory `page-swap-never-edit-live`).
GBP edits: Chrome with the manager account. Known limits are in memory `praxis-suriya-client` (save needs two clicks, Google rate limit after many saves).

## 10. Cost and caps

| Item | Cap per monthly refresh |
| --- | --- |
| Paid data (DataForSEO) | 2 EUR |
| Falcon credits | 200. Scans only after Martin's go. One 7x7 Google scan costs 49 credits. Never retry a scan |
| Free reads (Falcon reports and live GBP reads, Drive, Supabase SELECT, Autocomplete, live site) | No cap |

Local Falcon access: if the session has no Local Falcon MCP, use `scripts/falcon_read.py` (direct JSON-RPC to `mcp.localfalcon.com`, key from `.env`, read-only allowlist). For OAuth-connected places the `getLocalFalconGbp*` and `listLocalFalconGbp*` tools read the live profile, services, posts, media and reviews.

A first matrix (kickoff) costs no paid data if audit evidence exists. If a live check needs a paid call, the agent asks first. `cost_ledger.jsonl` logs every paid call. The script stops at the cap. Spend above the cap needs Martin's go.

## 11. Outputs

Per run, in `00_project/assets/maps-playbook/<client-slug>/<YYYY-MM-DD>-<mode>/` (modes: `kickoff`, `refresh`, `quickwins`):

| File | Content |
| --- | --- |
| `run.json` | Header: client, niche, mode, catalogue version, caps, cost, counts |
| `matrix.json` | 77 rows: status, evidence, age, stale flag, finding, task hint, blocker |
| `tasks.json` | Ranked task proposals with score parts, gate, owner type, dependencies, state |
| `evidence/` + `manifest.json` | Raw files with hash, source, date |
| `report/internal.html` | One-page board for Martin, pillar views, evidence index |
| `report/client.html` | Client-safe bundle. Draft until Checkpoint B |
| `sheet-view.json` and `matrix.xlsx` | Source for the Sheet (built by `build_sheet.py`, XlsxWriter) |
| `delta.json` | Refresh only: what changed since the last run |
| `change_log.jsonl` | Step 6 only: every change |
| `cost_ledger.jsonl` | Paid calls |

Drive (after Martin's go): client folder, subfolder `Maps-Playbook`. File name pattern `[Maps-Playbook] <Typ> <YYYY-MM-DD>`. Old versions go to `_archiv` (never overwrite). The Sheet follows `maps-playbook-sheet-design.md`. Drive MCP creates files and cannot write cells. Use Chrome for cell edits. Verify the converted Sheet by screenshot.
Portal tab: later, after the tables exist.
The report layout is in `maps-playbook-report-wireframe.md`. Martin reads page 1 in 30 seconds.

## 12. Data model

Draft SQL in `maps-playbook-schema.draft.sql`. Not applied. Tables: `playbook_runs`, `measure_status`, `playbook_tasks`, `playbook_evidence`, `playbook_change_log`. The catalogue stays a JSON file with a version number. Rules:
- A client instance stores `catalog_version`.
- A measure is never deleted. It gets `deprecated_in`.
- A catalogue upgrade writes a diff: new measures, changed rules, deprecated measures. New measures start as `unknown` in every client instance.
- Prospects may have no client ID (same rule as the audit tables).
- Evidence rows keep a drill path: matrix cell, evidence ID, source file or URL, date, hash.

## 13. Hard rules

1. Nothing changes on a client asset before Checkpoint C. Any extra change needs its own go.
2. Every cell has evidence, date and confidence. No guess. Missing data is `unknown` or `[FEHLT]`.
3. Client-safe output has no tool names and no team names. Use "Google-Daten" and "Maps-Messung". Address form from the client record (du for Suriya).
4. Health clients: HWG check. No cure promise. Law and tax: own advertising law.
5. Reviews: the client answers. 741 gives templates. No Falcon auto-posts or auto-replies. No filter. No per-star incentive.
6. Own review numbers (count, rating, age, replies) come from the Google profile in Chrome, never from Falcon (Falcon only as a hint for competitors). Falcon only through the MCP. Never retry a scan. Same grid and radius within a client series.
7. Real NAP only. The master record wins over any generated pack.
8. Outreach and review asks are sent by humans. Client emails only by Airmailer and never without Martin's go.
9. Sheets are formatted xlsx built with XlsxWriter. Never CSV. Never openpyxl for a Drive upload.
10. Give the Drive link with every delivery, plus a screenshot as a file.
11. Replies in STE. Client text in normal German prose. "du" with German clients. Client messages in "ich" form.

## 14. Success measures

| Measure | Target | How measured |
| --- | --- | --- |
| Falcon SoLV gain | Up against baseline on priority-1 keywords. Same grid and radius | Falcon report vs baseline |
| Calls and route requests | Up month on month | GBP insights |
| Review pace | Moving to 2x leader | Falcon review data (B05.03, B11.03) |
| Corrections at Checkpoint A | Under 3 per matrix | Count in `run.json` |
| Unsourced cells | 0 | `validate_run.py` |
| Manual checks saved | Fewer hand checks per client than the week-1 path | Compare time with the Suriya week-1 run |

## 15. Done criteria and tests

The workflow is shippable when:
1. Catalogue validates (`validate_catalog.py` gives 0 errors).
2. A dry run on Praxis Suriya gives 77 rows, each with evidence or `unknown`. The summary lists every catalogue defect it found.
3. The report prototype renders and passes a screenshot check.
4. The three tests pass in a fresh session (see design note section 9): T1 and T2 load the skill, T3 to T5 do not.
5. The skill scores 80 percent or more on `scorecard.md`, with no zero in section A or D.
6. Martin says "go" at the ship checkpoint.

## 16. Open questions

1. Four source files exist only in worktrees. Merge them or confirm the paths.
2. The 90-day program file is missing. Give the path.
3. Review requests by mail or SMS: confirm the legal basis with a lawyer if one exists.
4. Tracking number provider for DACH: not chosen.
5. The tables of the audit are not applied yet. The playbook tables follow the same go.
6. Un-burning has no files yet. The interface is set from its brief. Re-check when its spec exists.

## Registry entry (2026-10-11)

Every run of this workflow is recorded in the workflow registry. The Excel `~/Desktop/Workflow-Uebersicht.xlsx` shows per client whether the workflow ran, its state, the last run, Martin's approval and the folder links.
- At the start or end of a run: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py upsert --client "<client>" --workflow phone --status "in Arbeit|Trockenlauf|fertig, Freigabe offen" --local <folder> --drive <url> --result <file>`
- When Martin approves the result: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py approve --client "<client>" --workflow phone` in the same turn, then tell Martin the sheet was updated. A hook reminds Claude when a message sounds like an approval.
Workflow id: `phone` (Get the phone to ring / Maps Playbook).

## Registry: automatic (2026-10-11)

The overview Excel `~/Desktop/Workflow-Uebersicht.xlsx` updates itself. A Stop hook runs `workflow_registry.py sync --quiet` after every turn. You do not call `upsert` for normal progress. Keep `matrix.json` in the run folder with the fields `client` and `as_of`. A folder name with `dryrun` marks a test run. `sync` reads the file; do not edit the registry by hand.
For any other file layout, write `_run.json` in the run folder (schema in `00_project/workflow-registry/README.md`). Only the approval stays manual: when Martin approves a result, run `approve` in the same turn and say that the Excel is updated.

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: on the client view of the board: point at the top 5 tasks, think at open gates. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
