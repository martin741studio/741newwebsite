# Scorecard: Automation Build (2026-10-11, before install)

Scored with `00_project/knowledge/workflow-library/_derived/scorecard.md`. 0 missing · 1 partly · 2 done · n/a not scored.

| # | Score | Note |
|---|---|---|
| A1 | 2 | Skill (slash only) + hooks + scripts + verifier subagent, per patterns.md §3 |
| A2 | 2 | No CLAUDE.md line needed; procedure in skill; enforcement in 3 hooks |
| A3 | 2 | `disable-model-invocation: true` |
| A4 | n/a | Not for Cowork or routines (needs local Chrome and hooks) |
| B1 | 2 | 3 use cases in `design-note.md` |
| B2 | 2 | Scenarios in the design note before the body; `test-scenarios.md` |
| B3 | 1 | Real Skool build replayed through the guard (paper). No new live run yet |
| B4 | 2 | Inputs, deliverables, out-of-scope in `automation-workflow.md` |
| B5 | 2 | Fragile steps are scripts (`run_state.py`, `check_report.py`, hooks); build steps are heuristics |
| C1 | 2 | WHAT + WHEN + NOT, real trigger phrases |
| C2 | 2 | `automation-build` |
| C3 | 2 | SKILL.md ~70 lines; spec has a table of contents |
| C4 | 2 | Checklist P0–P7 |
| C5 | 2 | Scripts run, not read; clear exit codes; 95 sandbox tests |
| C6 | 1 | Checkpoint output template given; no input/output example pairs yet |
| C7 | 2 | One term per class (read, test_write, G, M) |
| C8 | 1 | MCP tools named by server in the spec, not fully qualified in SKILL.md |
| D1 | 2 | `check_report.py`, readback rule, verifier |
| D2 | 2 | "Max 3 fix attempts, until PASS" |
| D3 | 2 | Stop hook (proven in the real harness) |
| D4 | 2 | Evidence files are a gate condition |
| D5 | 0 | Trigger tests S1–S3 need the installed skill |
| D6 | 0 | Baseline needs one real run with and without the skill |
| E1–E7 | n/a | The build skill is not unattended. The daily reconciliation runner (not built yet) gets its own E-score |
| F1 | 1 | Client message draft yes; Drive link not yet part of the handover (portal page instead) |
| F2 | 2 | Per-action go, hook-enforced |
| F3 | 2 | Inventory + second check for every "missing" |
| F4 | 2 | STE in working docs; German client prose in runbook and protocol |
| F5 | 2 | Test protocol rule: no team names, no method sources |
| F6 | 2 | `add-workflow automation` done; `_run.json` written by `run_state.py`; dry run visible as Trockenlauf |

Total: 48 / 56 = 85.7 %. Blocking zeros: D5, D6.

Decision: fix first. After Martin's install go: install skill and hooks, run S1–S3 in a fresh session, run one real build (Marcel Gewinnspiel or the next automation) with the skill and compare with the Skool build history (corrections, tool calls, failed go-lives).
