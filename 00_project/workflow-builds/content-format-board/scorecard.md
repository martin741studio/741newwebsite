# Scorecard (step 4.5) — content-format-board, 2026-10-24

Scored against `00_project/knowledge/workflow-library/_derived/scorecard.md`. 0 = missing, 1 = partly, 2 = done. Section E (unattended/scheduled) not applicable: on-demand, Martin in the chat.

## A. Fit
| # | Check | Score | Evidence |
| --- | --- | --- | --- |
| A1 | Block matches the job (Skill, patterns.md §3 step 3) | 2 | research-note.md §1.1 |
| A2 | Always-on rules in CLAUDE.md, procedure in the skill, enforcement in scripts | 2 | SKILL.md + verify_board.py; no new CLAUDE.md lines needed |
| A3 | Side-effect skills have `disable-model-invocation: true` | 2 | No publish/send/deploy side effect; writes files under assets/ only; Martin's go per board is the gate (same reasoning as personal-posts, recorded in SKILL.md 3.2 note) |
| A4 | Committed to the repo | 2 | `.claude/skills/content-format-board/` (project skill), commit at 5.2 |
**A: 8/8**

## B. Design
| # | Check | Score | Evidence |
| --- | --- | --- | --- |
| B1 | 2–3 use cases | 2 | use-cases.md |
| B2 | 3 test scenarios before the body | 2 | test-scenarios.md (written at step 2.2, before SKILL.md) |
| B3 | One hard task by hand, approach extracted | 2 | hand-run.md → references/worked-example.md |
| B4 | Inputs, deliverable, out-of-scope stated | 2 | SKILL.md Inputs / Output template / description NOT list; inputs-grill.md |
| B5 | Degrees of freedom match fragility | 2 | pipeline.md §2.5: 5 scripts for the deterministic steps, heuristics for finding/mapping |
**B: 10/10**

## C. SKILL.md quality
| # | Check | Score | Evidence |
| --- | --- | --- | --- |
| C1 | description WHAT + WHEN + negative trigger | 2 | frontmatter; trigger tests passed |
| C2 | kebab-case name, no reserved words, no XML | 2 | `content-format-board` |
| C3 | Body < 500 lines, references one level deep | 2 | 57 lines; 4 references; playbook-notes.md has section headers A–I as its TOC |
| C4 | Checklist Claude copies and ticks | 2 | Workflow steps 1–10 |
| C5 | Deterministic steps are scripts Claude runs; errors handled | 2 | resolve_target (exit 2 on no match/ambiguous), label_map, log_research_calls, verify_board, run_log |
| C6 | Output template + examples | 2 | assets/board-template.md (strict) + worked-example.md + the real Little Frenchie board |
| C7 | One term per concept, one default with an escape hatch | 2 | label-map.json is the single term source; language default = client's site, override en/de |
| C8 | MCP tools fully qualified | 2 | `allowed-tools` names the firecrawl tools with their full server prefix |
**C: 16/16**

## D. Verification
| # | Check | Score | Evidence |
| --- | --- | --- | --- |
| D1 | A check Claude can run | 2 | scripts/verify_board.py (7 checks) |
| D2 | Loop: run → fix → repeat → only proceed on pass | 2 | SKILL.md step 8 "Only BOARD PASSED continues" |
| D3 | Unattended runs gated | 2 | Not unattended; Martin's go (step 9) gates every run — satisfied by design |
| D4 | Evidence demanded in the final report | 2 | step 8: verify output + research-call report in the reply; step 10 logs result path |
| D5 | Trigger tests passed | 2 | trigger-tests.md: 2 positive, 4 negative |
| D6 | Baseline comparison | 2 | baseline.md |
**D: 12/12**

## F. 741 house rules
| # | Check | Score | Evidence |
| --- | --- | --- | --- |
| F1 | Ends with client message draft + Drive link where a client deliverable exists | 1 | The board is pitch/planning material for Martin, not a client deliverable; no client message. Step 10 states the hand-off into the pitch. |
| F2 | Per-change go before live website changes | 2 | No live change in scope; per-board go enforced |
| F3 | Every data point verified or asked for | 2 | Critical rule 3; OPEN QUESTION markers; zero-hit queries reported; promise words blocked |
| F4 | STE in replies and artifacts | 2 | SKILL.md Critical + step 7; verifier WARNs on >20-word sentences and dashes |
| F5 | No method sources in client material | 2 | label map + banned-term scan (verifier FAILs) |
| F6 | Runs show in the overview Excel | 2 | `_run.json` in registry schema; `add-workflow` at 5.3a |
| F7 | Martin guide on client-facing deliverables | 1 | Board is a markdown proposal, not a rendered page; guide not placed (5.3b skipped with reason) |
**F: 12/14**

## Result
Total: 58 / 60 → **96.7 %**. Blocking zeros: **0** (none in A, none in D).
Decision: **ship** (pending Martin's go at checkpoint 2).
