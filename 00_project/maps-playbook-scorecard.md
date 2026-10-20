# Maps-playbook: scorecard (self-score, 2026-10-11)

Scale: `00_project/knowledge/workflow-library/_derived/scorecard.md`. Ship needs 80 percent and no zero in A or D. N/A lines are left out.

| Line | Score | Note |
| --- | --- | --- |
| A1 block fits | 2 | Skill with checkpoints, forked context |
| A2 rules in the right place | 1 | Hard rules sit in the skill. No hook yet for the "no change before Checkpoint C" rule |
| A3 side effects flagged | 1 | Martin chose natural-phrase triggers, so `disable-model-invocation` is not set. Gates inside the body protect side effects. Deviation documented |
| A4 Cowork or routine enablement | n/a | Manual start only |
| B1 use cases | 2 | 4 use cases in the design note |
| B2 tests before body | 2 | 5 scenarios written before the body |
| B3 hard task solved by hand | 2 | Suriya dry run, 77 rows, 13 catalogue fixes extracted |
| B4 inputs, deliverable, out of scope | 2 | Spec sections 1 and 3 |
| B5 degrees of freedom | 2 | Scripts for status, score, validation, Sheet. Heuristics for task wording |
| C1 description | 2 | 741 characters, WHAT, WHEN, NOT |
| C2 name | 2 | `maps-playbook` |
| C3 size and references | 2 | 85 lines. Runbooks one level deep, with TOC |
| C4 checklist | 2 | Copyable, with 3 checkpoints |
| C5 scripts | 1 | 5 scripts exist. `build_matrix.py` (audit feed to status) is not written. The agent does Step 2 |
| C6 output template | 1 | File list and Sheet design exist. No example pairs |
| C7 terms | 1 | Mostly one term per concept. Not reviewed by a second reader |
| C8 MCP tools qualified | 2 | Full names in `allowed-tools` |
| D1 runnable check | 2 | `validate_catalog.py`, `validate_run.py` |
| D2 loop stated | 1 | "Fix until 0 errors" in Step 3 |
| D3 unattended gating | 1 | Stop rules in text. No hook or reviewer subagent |
| D4 evidence in report | 2 | Validator output, screenshots, Drive link |
| D5 trigger tests passed | **0** | Written, not run in a fresh session |
| D6 baseline with and without | **0** | Not done. Compare with the Suriya week-1 path |
| F1 message draft and Drive link | 2 | Step 8 |
| F2 per-change go | 2 | Checkpoint C |
| F3 verified data only | 2 | Evidence and age rules, validator |
| F4 STE | 2 | Replies and docs in STE |
| F5 no method sources named | 2 | None named in client-safe output |

Total: 43 of 54 = **79.6 percent**. Blocking zeros: D5, D6.
Decision: **fix first.** Run T1 to T5 in a fresh session, do the baseline, write `build_matrix.py`, then re-score. Expected after that: above 85 percent.
