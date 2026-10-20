# Workflow scorecard: cro-homepage (Track A)

Raster: `00_project/knowledge/workflow-library/_derived/scorecard.md`. Scored 2026-10-11 after the tooling upgrade (scripts, templates, tests, reviewer prompt, upload guard). Rule: ship at 80 % with no 0 in section A or D.

| # | Check | Score | Note |
| --- | --- | --- | --- |
| A1 | Right building block | 2 | skill plus workflow doc |
| A2 | Rules in CLAUDE.md, procedure in skill, enforcement in hooks | 2 | upload guard hook added (`scripts/guard_upload.py`) |
| A3 | Side-effect skills set to manual only | 1 | the skill writes to Martin's Drive only. Left on automatic triggering by decision |
| A4 | Enabled for Cowork or routines | 1 | not enabled. Not needed while Martin runs it in Claude Code. Needs Customize > Skills if that changes |
| B1 | Use cases written | 2 | |
| B2 | Test scenarios BEFORE the body | 1 | written after the fact (`tests/test-scenarios.md`) |
| B3 | One hard task solved by hand first | 2 | Dumann pilot |
| B4 | Inputs, deliverable, out-of-scope | 2 | |
| B5 | Degrees of freedom | 2 | fragile steps are scripts now |
| C1 | Description WHAT, WHEN, negative trigger | 2 | |
| C2 | Name rules | 2 | |
| C3 | Body under 500 lines, references one level deep, TOC over 100 lines | 2 | TOC added to the workflow doc |
| C4 | Checklist | 2 | `assets/templates/run-checklist.md` |
| C5 | Scripts run, not read | 2 | `scripts/` |
| C6 | Output templates and examples | 2 | `assets/templates/`, worked examples named |
| C7 | One term per concept, no time-sensitive text | 1 | the workflow doc holds many dated decision notes |
| C8 | MCP tools fully qualified | 1 | doc says "Drive tool", "Chrome" |
| D1 | Check Claude can run | 2 | `verify.py`, `measure.js`, `check_text.py` |
| D2 | Loop stated | 2 | in SKILL.md "Verify loop" |
| D3 | Unattended runs gated | 1 | optional fresh reviewer at Checkpoint 2. First test on the Adel run found 12 real gaps (score inflation, a wrong handoff line, a wrong number). Recommendation: make the reviewer standard for autonomous runs |
| D4 | Evidence in the final report | 2 | link, screenshot, report line |
| D5 | Trigger tests passed | **0** | written, not run |
| D6 | Baseline with and without | **0** | no baseline yet |
| F1 | Client message and Drive link | 2 | |
| F2 | Per-change go before live changes | n/a | no live changes |
| F3 | Data verified | 2 | [FEHLT] rule |
| F4 | STE in replies | 1 | client files are German prose, by design |
| F5 | No method sources in client material | 2 | checked in `verify.py` |

**Total: 43 of 54 = 80 %.** Blocking zeros: D5, D6. Decision: **fix first**, then ship. Fix = run `tests/test-scenarios.md` T1 to T6 in a fresh session and log the first baseline after the next real run (`run-metrics.md`). Re-score after 5 real runs.
