# Scorecard — Un-Burning (scored 2026-10-11 against `knowledge/workflow-library/_derived/scorecard.md`)

Scale: 0 missing, 1 partly, 2 done. Rule: ship at 80 percent or more with no 0 in section A or D. Section E does not apply (not scheduled).

| # | Score | Note |
| --- | --- | --- |
| A1 | 2 | Skill with gates fits a per-client procedure Martin triggers |
| A2 | 1 | Procedure is in the skill. Gates are prompt rules. A hook for "no live change without go" does not exist yet |
| A3 | 2 | `disable-model-invocation: true` |
| A4 | 2 | Not used in Cowork or routines. Personal skill only |
| B1 | 2 | Three use cases in `design-note.md` |
| B2 | 2 | Five test scenarios written before spec and skill body |
| B3 | 1 | The read-only dry run on Suriya is done. The execute phase was not solved by hand yet |
| B4 | 2 | Inputs, deliverable and out-of-scope stated in spec sections 1 and 4 |
| B5 | 2 | Scripts for validation, bedrock and report. Heuristics for page decisions |
| C1 | 2 | WHAT, WHEN, negative trigger, 702 characters |
| C2 | 2 | `un-burning`, no brackets in frontmatter |
| C3 | 2 | SKILL.md 75 lines. Prompts in `references/` |
| C4 | 2 | Checklist with gates |
| C5 | 2 | `validate_run.py`, `validate_changes.py`, `bedrock.py`, `build_report.py`. Thresholds are in the spec |
| C6 | 1 | Report layout is fixed. No input/output example pairs yet |
| C7 | 2 | One term per concept |
| C8 | 1 | Local Falcon MCP is named without a fully qualified tool name. It was not connected in the dry run |
| D1 | 2 | Validators and a rendered screenshot check |
| D2 | 2 | "Fix until VALID / WAVE OK" is in the skill |
| D3 | 2 | Not unattended. Gates are human |
| D4 | 2 | The final report demands command output, screenshot and Drive link |
| D5 | **0** | Trigger tests T1 to T5 were not run. The skill is not installed |
| D6 | **0** | No baseline comparison with and without the skill |
| F1 | 1 | Client message draft exists (access checklist). Drive link step is in the skill. No Drive upload yet (needs go) |
| F2 | 2 | GO-1, GO-2, GO-3. Per-change go |
| F3 | 2 | Evidence, source, date, confidence on every item. Validator enforces it |
| F4 | 2 | Notes and spec in STE. Client text in German prose |
| F5 | 2 | No method sources named. "741-Bereinigung" |

Total: 47 of 56 = 83.9 percent. Blocking zeros: D5 and D6.
Decision: **fix first.** The score passes 80 percent, but D5 and D6 are zero. After Martin's final go: install the skill, run T1 to T5 in a fresh session, run the baseline comparison, then re-score. Expected result after those two steps: 51 of 56 (91 percent).
Known gaps to close at the same time: a hook for the go rule (A2), example pairs (C6), a fully qualified Falcon tool name (C8).
