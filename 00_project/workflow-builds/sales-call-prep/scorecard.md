# Scorecard — sales-call-prep (step 4.5)

Scored against `00_project/knowledge/workflow-library/_derived/scorecard.md`. Section E
(unattended/scheduled) is not applicable — this workflow is on-request only (Martin's cp1 go,
Q1=A) and never runs unattended — so it is excluded from the total, same treatment as the 3.7
and 4.4 skips.

## A. Fit
| # | Check | Score | Note |
| --- | --- | --- | --- |
| A1 | Block matches the job | 2 | Skill, per-prospect, per patterns.md §3 step 3 |
| A2 | Always-on in CLAUDE.md, procedure in skill, enforcement in hooks | 2 | "Never contact the prospect" is a Critical rule; nothing in the skill ever calls a send-capable tool |
| A3 | Side-effect skills have `disable-model-invocation: true` | 2 | Correctly has none — no side effects (Martin's go, Q3=A) |
| A4 | Enabled on claude.ai or committed to repo | 2 | Committed at `.claude/skills/sales-call-prep/` |
**A = 8/8**

## B. Design
| # | Check | Score |
| --- | --- | --- |
| B1 | 2-3 use cases | 2 |
| B2 | 3 test scenarios before the body | 2 |
| B3 | One hard task solved by hand, approach extracted | 2 |
| B4 | Inputs, deliverable, out-of-scope stated | 2 |
| B5 | Freedom matches fragility | 2 |
**B = 10/10**

## C. SKILL.md quality
| # | Check | Score | Note |
| --- | --- | --- | --- |
| C1 | description WHAT+WHEN+negative trigger | 2 | |
| C2 | kebab-case, no reserved words, no XML brackets | 2 | |
| C3 | Body < 500 lines, references one level deep, TOC if > 100 lines | 2 | Body 112 lines; both references under 100 lines, no TOC needed |
| C4 | Checklist Claude copies and ticks | 2 | |
| C5 | Deterministic steps are scripts Claude RUNS | 2 | `find_booking.py`, `verify_brief.py`, both tested, handle 0/1/>1-match and pass/fail |
| C6 | Output template + 2-3 example pairs where style matters | 1 | Template given, but only ONE worked example (Korinna), not 2-3 pairs — not blocking, noted for maintenance |
| C7 | One term per concept, no time-sensitive text, default + escape hatch | 2 | "741-Call-Raster"/"741-Einwand-Raster" used consistently |
| C8 | MCP tools fully qualified; dependencies listed | 2 | N/A — no MCP tools used, only Read/Grep/Glob/Bash |
**C = 15/16**

## D. Verification
| # | Check | Score |
| --- | --- | --- |
| D1 | A check Claude can run | 2 |
| D2 | Loop: check → fix → repeat → only proceed when it passes | 2 |
| D3 | Unattended runs gated | 2 (N/A, never unattended) |
| D4 | Evidence demanded in the final report | 2 |
| D5 | Trigger tests: obvious, paraphrase, unrelated does NOT trigger | 2 |
| D6 | Baseline with vs. without | 2 |
**D = 12/12**

## F. 741 house rules
| # | Check | Score | Note |
| --- | --- | --- | --- |
| F1 | Client message + Drive link where a client deliverable exists | 2 | N/A — never client-facing, by design |
| F2 | Per-change "go" before a live website change | 2 | N/A — no website touched |
| F3 | Every data point verified or asked for | 2 | claims.json tracing + fresh site-recheck check |
| F4 | STE in replies/artifacts unless client prose | 2 | Brief is short, active-voice German sentences (house convention for internal call notes); my own reports to the orchestrator are in English STE |
| F5 | No method sources named in client material | 2 | `verify_brief.py` enforces by script, confirmed on the real output |
| F6 | Runs show up in the overview Excel by themselves | 2 | `_run.json` written in step 6 |
| F7 | Martin guide where client/prospect sees the output | 2 | N/A — never seen by the prospect |
**F = 14/14**

## Result
Total: 59 / 60 → **98 %**. Blocking zeros: **none** (no 0 anywhere, let alone in A or D).
Decision: **ship**.

Only partial score: C6 (one worked example instead of 2-3). Noted as a maintenance item, not
a ship blocker — after a few more real runs, add a second worked example (a thin-case prospect
with no `baseline.md`) to `references/template.md`.
