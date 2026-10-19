# Scorecard: captions (step 4.5, 2026-10-19)

Scored against `00_project/knowledge/workflow-library/_derived/scorecard.md`. Section E (unattended, scheduled) does not apply: Martin triggers every run and gives the go at the checkpoint. It is excluded from the total, as in the sales-call-prep and canary builds.

## A. Fit
| # | Check | Score | Note |
|---|---|---|---|
| A1 | Block matches the job | 2 | Skill, one repeatable procedure Martin triggers (patterns.md section 3, item 3) |
| A2 | Always-on in CLAUDE.md, procedure in skill, enforcement in script | 2 | Format and numbers enforced by `validate_captions.py`, slop by `deslop.py` |
| A3 | Side-effect skill has `disable-model-invocation: true` | 1 | Off on purpose, house convention since the canary build (natural triggers never fire with it on). The only side effect (Drive copy) sits behind Martin's go card. Not blocking. |
| A4 | Committed to the repo | 2 | `.claude/skills/captions/` |
**A = 7/8**

## B. Design
| # | Check | Score |
|---|---|---|
| B1 | 3 use cases with trigger, steps, tools, result | 2 |
| B2 | Test scenarios before the body | 2 |
| B3 | One task solved by hand, approach extracted (sample dump; 12 friction points became rules) | 2 |
| B4 | Inputs, deliverable, out-of-scope stated | 2 |
| B5 | Freedom matches fragility: 2 scripts, 3 heuristics | 2 |
**B = 10/10**

## C. SKILL.md quality
| # | Check | Score | Note |
|---|---|---|---|
| C1 | description WHAT + WHEN + negative trigger | 2 | 7 trigger phrases, 5 NOT cases; 4/4 trigger tests |
| C2 | kebab-case, no reserved words, no XML | 2 | |
| C3 | Body under 500 lines, references one level deep | 2 | Body 105 lines; references 26 to 64 lines |
| C4 | Checklist Claude copies and ticks | 2 | 8 steps |
| C5 | Deterministic steps are scripts Claude runs, with errors handled | 2 | `intake.py` (exit 2 on empty dump, versioning), `validate_captions.py` (verbose FAIL lines, limits as flags) |
| C6 | Output template and 2 to 3 example pairs | 2 | Template in assets, 4 pairs and 1 anti-example |
| C7 | One term per concept, no time-sensitive text | 2 | "block", "beat", "dump" used throughout |
| C8 | MCP tools fully qualified, dependencies listed | 2 | 4 Drive tools in `allowed-tools`, `references/drive.md` |
**C = 16/16**

## D. Verification
| # | Check | Score |
|---|---|---|
| D1 | A check Claude can run | 2 |
| D2 | Loop: run, fix, repeat, only proceed on PASS and 5/5 | 2 |
| D3 | Unattended runs gated | 2 (never unattended) |
| D4 | Evidence demanded in the final report (validator lines, slop line, path, Drive link) | 2 |
| D5 | Trigger tests: 4/4 | 2 |
| D6 | Baseline with vs without done | 2 |
**D = 12/12**

## F. 741 house rules
| # | Check | Score | Note |
|---|---|---|---|
| F1 | Drive link at the end | 2 | Step 8 reports path and viewUrl; no client message, no client |
| F2 | Per-change go before a live change | 2 | Go card before the only side effect; no website |
| F3 | Every data point verified | 2 | Validator for numbers, beats.md for words, "?" for unclear words |
| F4 | STE in skill and replies; captions are the prose artifact | 2 | |
| F5 | No method sources named | 2 | |
| F6 | Runs show up in the overview Excel | 2 | `_run.json` by `intake.py`; registry `add-workflow` in 5.3a |
| F7 | Martin guide where a client sees output | 2 | Not client-facing, not applicable |
**F = 14/14**

## Result
Total: 59 / 60 → 98.3 %. Blocking zeros: 0.
Decision: ship.
