# Backlink DACH — scorecard 2026-10-13

Workflow: `backlink` (Backlink DACH). Skill `~/.claude/skills/backlink-dach/SKILL.md`. Process doc `00_project/backlink-workflow-dach.md` (v1.1).
Template: `00_project/knowledge/workflow-library/_derived/scorecard.md`. Previous score: 47.8 % (2026-10-11).
Scored by: Claude (side session of the morning-grill chat). Internal document.

## What changed since 2026-10-11

1. Border (Martin, 2026-10-13): all of pillar A belongs to the Citations module, also niche directories (jameda, Doctolib, theralupa …). This workflow owns pillars B–E. Doc section 3.0 is now a read-only hand-over check. `build_sheet.py` refuses a Säule-A row.
2. Run file: `00_project/assets/<slug>/backlink/<YYYY-MM-DD>/_run.json`, written by the new `scripts/write_run.py`. Doc section 2.4.
3. `build_sheet.py` uses XlsxWriter, not openpyxl (Drive conversion fault of 2026-10-11).
4. Lock removed (Martin, 2026-10-13, card answer "Sperre raus + Stopp"): `disable-model-invocation` is gone. A start gate replaces it: loaded from Martin's own words, the skill stops after Step 0 (read only) and waits for go.
5. Skill: checkpoint output template, verification loop, Supabase `execute_sql` (SELECT only) in `allowed-tools`, pilot-folder note.
6. Doc: contents line, use cases (0.1), stale note about openpyxl closed.

## Test evidence

### Script checks (2026-10-13)

| Check | Input | Result |
| --- | --- | --- |
| `build_sheet.py` pass case | 4 rows (B, B, D, B/D placeholder) | exit 0, 4 rows, 6 data validations, freeze at A5, headers incl. "DR (approx.)" |
| `build_sheet.py` fail case | jameda as A-niche, row without Quelle, row without Kontakt + unknown status | exit 1, 4 errors listed, no file written |
| `write_run.py` | Hüwel pilot, `--date 2026-10-11` | wrote `00_project/assets/huewel/backlink/2026-10-11/_run.json`; `workflow_registry.py sync` read it ("local aus _run.json", "note aus _run.json") |
| `write_run.py` bad status | `--status bogus` | argparse error, nothing written |

### Trigger tests (fresh `claude -p`, `--tools Skill Read`, `--permission-mode default`, no MCP, cwd 741website)

| # | Prompt | Lock on (old) | Lock off, first test | Final skill (lock off + start gate) |
| --- | --- | --- | --- | --- |
| 1 | "Backlink-Workflow für Hüwel starten, Budget 0" | pass: found the skill via memory, Skill call blocked, gave Martin the `/backlink-dach` line | pass: loaded `backlink-dach` | pass: loaded `backlink-dach`, read the doc and the pilot folder, stopped with 2 questions (budget 0 vs. 500 €, client mail). No API call. |
| 2 | "schau mal, welche Links wir für Suriya noch bauen können" | **fail**: no skill, answered from memory, proposed citations work | pass: loaded `backlink-dach`, stopped on the Hüwel-first rollout rule | pass: loaded `backlink-dach`, stopped on the Hüwel-first rollout rule and asked for an override |
| 3 | "trag Hüwel bei Gelbe Seiten ein" | pass: no `backlink-dach` (citations path, NAP data) | pass: no skill | pass: no `backlink-dach` (citations path, browser skill) |
| 4 | "trag Hüwel bei jameda ein" (border) | pass: no `backlink-dach` (citations path) | pass: no skill | pass: no `backlink-dach` (citations path, asked which jameda task) |

Logs: session scratchpad `trig/*.jsonl` (not kept in the repo).

### Baseline with vs. without skill (Hüwel pilot data, read only)

Same prompt both times: checkpoint state for Hüwel from the pilot folder in worktree great-easley-4f6970, read only, no API, no writes. With skill = `/backlink-dach <prompt>` (`--tools Skill Read Glob Grep`). Without = `--disable-slash-commands` (`--tools Read Glob Grep`). Model in both: claude-sonnet-5.

| Measure | With skill | Without skill |
| --- | --- | --- |
| Duration | 78 s | 60 s |
| Cost | 0.228 $ | 0.200 $ |
| Output tokens | 6,119 | 4,546 |
| Input tokens (incl. cache) | 216,898 | 153,428 |
| Tool calls | not visible (fork subagent, no session persistence); report names 8 files read | 10 (memory, glob, 7 pilot files, AskUserQuestion) |
| Read the process doc (source of truth) | yes | no |
| Correct state (Checkpoint 2 passed, Sheet v5, waits for Verband answer + Säule C) | yes | yes |
| Flagged stale local `targets.md` (v2) vs. Sheet (v5) | yes | yes |
| Pillar A hand-over visible | yes (missing `handover-citations.md`) | no |
| Säule C needs Checkpoint 4 before money | yes | yes |
| Said what it did not do (no call, no send, no write) | yes | no |
| Fixed checkpoint format | partly (own 5 sections, sources listed, no "Beleg" line) | no |
| Corrections Martin would need (rubric misses of 7) | 0.5 | 3 |

Both runs reported `build_sheet.py` as "still openpyxl". The cause was a stale note in the doc, not the script. The note is fixed.

Result: the skill costs about 14 % more and 18 s more. It removes about 2.5 corrections per run: it reads the process doc, it shows the pillar A hand-over, and it states what it did not do.

## Score (0 missing · 1 partly · 2 done · n/a not applicable)

### A. Fit

| # | Score | Reason |
| --- | --- | --- |
| A1 | 2 | Skill with `context: fork` and 4 checkpoints fits a long, gated, per-client run. |
| A2 | 2 | Procedure in the skill and doc. Enforcement by `allowed-tools` (no mail or payment tool) and by the script validators. |
| A3 | 1 | Lock removed by Martin's choice. A start gate (stop after read-only Step 0) protects the first API call and Drive write instead. |
| A4 | 2 | Personal skill for local Claude Code, not for Cowork or routines. Path is in memory `backlink-dach-workflow.md`. |

### B. Design

| # | Score | Reason |
| --- | --- | --- |
| B1 | 2 | 3 use cases in doc section 0.1 (new client, resume, buy path). |
| B2 | 1 | The 3 test scenarios were written after the body (2026-10-11), not before. |
| B3 | 2 | Hüwel v1–v4 by hand, then `gap-analysis.mjs` and `build_sheet.py` extracted. |
| B4 | 2 | Inputs, Sheet deliverable and out-of-scope (pillar A, page content, CRO) stated. |
| B5 | 2 | Scripts for gap, Sheet and run file. Heuristics for the local research. |

### C. SKILL.md quality

| # | Score | Reason |
| --- | --- | --- |
| C1 | 2 | Third person, WHAT + WHEN, real German and English triggers, negative trigger incl. niche directories. |
| C2 | 2 | `backlink-dach`. |
| C3 | 2 | Body about 110 lines. Detail in the doc, one level deep. Doc has a contents line. |
| C4 | 2 | Copyable checklist with 4 checkpoints. |
| C5 | 2 | 3 scripts, each exits with a clear message on bad input. Limits are named flags (`--limit`, 8-competitor minimum with `--force`). |
| C6 | 1 | Strict checkpoint template exists. Only one outreach example (Verein, du). No Sie example pair. |
| C7 | 1 | Pilot-specific text (Hüwel-first rule, pilot folder in a worktree) will age. |
| C8 | 2 | MCP tools fully qualified in `allowed-tools`. Dependencies named: `uv`, `node`, `.secrets/dataforseo.env`, Supabase. |

### D. Verification

| # | Score | Reason |
| --- | --- | --- |
| D1 | 2 | `build_sheet.py` validator, `write_run.py` status choices, gap script minimum. |
| D2 | 2 | "Verification loop" section: run, fix, run again, proceed only at exit 0. |
| D3 | n/a | No unattended run. Step 5 is not scheduled. Every step stops at a checkpoint. |
| D4 | 2 | Checkpoint template line 5 "Beleg" (script output, screenshot, link). |
| D5 | 2 | Final skill: 4 of 4 pass (obvious, paraphrase, unrelated, jameda border). With the old lock the paraphrase failed. |
| D6 | 2 | Baseline above, with numbers. |

### E. Unattended and scheduled

n/a for all 7 lines. The workflow has no routine or scheduled task. Re-score E when Step 5 (monthly report) gets a schedule.

### F. 741 house rules

| # | Score | Reason |
| --- | --- | --- |
| F1 | 2 | Checkpoint 2 gives the Sheet link. Step 3 gives the client mail with copy-paste text. |
| F2 | n/a | The workflow never changes a live website. |
| F3 | 2 | `[FEHLT]` rule, "never fabricate an email", DR labelled as approximation. |
| F4 | 1 | Skill and run outputs in STE. The doc has many long sentences from v1. |
| F5 | 2 | "741 Link-Raster", no method sources in client files. |
| F6 | 2 | `_run.json` via `write_run.py`, read by `sync` (tested). Workflow id `backlink` exists. |
| F7 | n/a | No visual client deliverable. Sheet is internal, client mail is plain text. |

## Result

Total: 49 / 54 → 90.7 %. Blocking zeros: 0.
Decision: ship. 90.7 % is above the 80 % bar, no zero in A or D. Checkpoint 2 of the creation workflow (Martin's ship go) is still open.

Open (not blocking):
1. B2 and C6: add a Sie outreach example (Verband or Presse) next to the Verein example.
2. F4: rewrite the long v1 sentences of the doc in STE.
3. Hüwel pilot folder is only in worktree great-easley-4f6970. Move it to main when that worktree is cleaned up.
4. Hand-over list of the Hüwel pilot (doc section 3.0) still needs to reach the Citations module chat.
