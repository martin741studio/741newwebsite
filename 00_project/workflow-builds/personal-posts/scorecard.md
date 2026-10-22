# Scorecard — personal-posts (4.5)

Scored against `00_project/knowledge/workflow-library/_derived/scorecard.md`. Section E (unattended/scheduled) excluded: this skill is always attended, Martin triggers every run (see 3.7 skip). F1, F2, F7 excluded as not applicable: this skill never produces a client/prospect-facing deliverable and never touches a live website.

## A. Fit

| # | Check | Score | Note |
| --- | --- | --- | --- |
| A1 | Block matches the job | 2 | Skill, matches R0.2 (repeat, on-demand, gated procedure) |
| A2 | Always-on vs. procedure vs. enforcement correctly placed | 2 | All procedure, in the skill; no hooks needed |
| A3 | Side-effect skills have `disable-model-invocation: true` | 2 | Deliberately OFF, documented reasoning (captions precedent, 4.1 finding): the only external send is conditional (cleanse.sh below 5/5), not guaranteed every run; Martin's go-per-post is the real gate |
| A4 | Skill committed/enabled where it's used | 2 | Project skill, `.claude/skills/personal-posts/`, committed with the repo |

**A: 8/8**

## B. Design

| # | Check | Score | Note |
| --- | --- | --- | --- |
| B1 | 2-3 use cases with trigger/steps/tools/result | 2 | 4 use cases written |
| B2 | 3 test scenarios before the body | 2 | `test-scenarios.md` |
| B3 | One hard task solved by hand, approach extracted | 2 | `hand-run.md`, extracted into `voice-profile.md` |
| B4 | Inputs, deliverable, out-of-scope stated | 2 | SKILL.md Inputs + negative triggers in description |
| B5 | Degrees of freedom match fragility | 2 | `decisions.md` table: scripts for slop/length/backlog/image render, heuristics for voice/claim-source |

**B: 10/10**

## C. SKILL.md quality

| # | Check | Score | Note |
| --- | --- | --- | --- |
| C1 | Description states WHAT+WHEN, negative trigger | 2 | |
| C2 | kebab-case, no reserved words | 2 | |
| C3 | Body under 500 lines, references one level deep | 2 | 53 lines; `references/voice-profile.md`, `platform-specs.md`, `strategy-notes.md` |
| C4 | Workflow is a checklist to copy/tick | 2 | 10-step checklist |
| C5 | Deterministic steps are scripts, run not read | 2 | `topic_backlog.py`, `check_lengths.py`, `verify_draft.py`, `build_personal_image.py`, `run_log.py` — all tested |
| C6 | Output template given | 2 | |
| C7 | One term per concept, no time-sensitive text | 2 | |
| C8 | MCP tools fully qualified | 2 | N/A, no MCP tools used (vacuously satisfied) |

**C: 16/16**

## D. Verification

| # | Check | Score | Note |
| --- | --- | --- | --- |
| D1 | A check Claude can run | 2 | `verify_draft.py` (slop + length + link check) |
| D2 | Loop stated: check -> fix -> repeat -> only proceed when it passes | 2 | Step 6, explicit |
| D3 | Unattended runs gated | 2 | N/A, always attended (vacuously satisfied) |
| D4 | Evidence demanded in the final report | 2 | Exit codes, `_run.json` entries |
| D5 | Trigger tests passed (obvious/paraphrase/negative) | 2 | `trigger-tests.md` — found and fixed a real `disable-model-invocation` defect before shipping |
| D6 | Baseline comparison done | 2 | `baseline.md` — 16 tool calls + verified gate + image vs. 0 tool calls, no image, self-report only |

**D: 12/12**

## F. 741 house rules (F1, F2, F7 excluded: no client/prospect deliverable, no website change)

| # | Check | Score | Note |
| --- | --- | --- | --- |
| F3 | Every data point verified or asked for | 2 | Step 3 claim check, `claims-need-real-data` |
| F4 | Replies in STE unless client prose | 2 | Enforced by this session's own project rule |
| F5 | No method sources named in client material | 2 | Internal rule IDs (C2.1 etc.) never appear in delivered post text |
| F6 | Runs show up in the overview Excel by themselves | 1 | `run_log.py` capability built and tested; registry `add-workflow` (5.3a) not yet run — will become 2 after that step |

**F: 7/8**

## Result

Total: 53 / 54 → **98%**. Blocking zeros: **none** (no 0 anywhere, sections A and D both clean).

Decision: **ship**, pending 5.3a (registry entry) to close the one open point (F6).
