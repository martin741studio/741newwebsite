# Scorecard — goals-data-architecture (2026-10-15)

## A. Fit
| # | Check | Score |
| --- | --- | --- |
| A1 | Block matches the job (script inside the existing morning-grill skill) | 2 |
| A2 | Always-on rules stay in CLAUDE.md; this is a procedure inside the skill | 2 |
| A3 | Side-effect skill has `disable-model-invocation: true` | 1 (pre-existing gap: morning-grill already had side effects and no flag before this build; not introduced by this change, noted not fixed) |
| A4 | Committed to the repo (`00_project/morning-grill-skill/`) | 2 |

## B. Design
| # | Check | Score |
| --- | --- | --- |
| B1 | 2–3 use cases with trigger/steps/tools/result | 2 (4 written) |
| B2 | 3 test scenarios before the body | 2 (5 written, 2 must-not-trigger) |
| B3 | One hard task solved by hand, approach extracted | 2 (2 hand tasks: goal-sheet regen, NAP trace) |
| B4 | Inputs, deliverable, out-of-scope stated | 2 (hard limits, NAP-only scope) |
| B5 | Degrees of freedom match fragility | 2 (table in pipeline.md) |

## C. SKILL.md quality
| # | Check | Score |
| --- | --- | --- |
| C1 | WHAT + WHEN + negative trigger | 2 (unchanged, still accurate) |
| C2 | Naming conventions | 2 (unchanged) |
| C3 | Body under 500 lines, references one level deep | 2 |
| C4 | Checklist Claude ticks | 2 (step 3c integrated) |
| C5 | Deterministic steps are scripts, handle errors | 2 |
| C6 | Output template given | 2 (existing goal-sheet template still holds) |
| C7 | One term per concept, no time-sensitive text | 2 |
| C8 | MCP tools fully qualified / dependencies listed | 2 (scripts use direct REST/Sheets API, not MCP — correct, scripts run outside the MCP-calling process) |

## D. Verification
| # | Check | Score |
| --- | --- | --- |
| D1 | A check Claude can run | 2 (`--check-only`, reconcile output) |
| D2 | Loop stated, fix until it passes | 2 (2 real bugs found + fixed via the functional test) |
| D3 | Unattended runs gated | 2 (judgment writes never run in the 06:00/17:00 task) |
| D4 | Evidence demanded in the report | 2 (command output in trigger-tests.md / functional-test.md) |
| D5 | Trigger tests passed (obvious / paraphrase / must-not) | 1 (ran the deterministic scripts for real; S2/S3/S5 reasoned from the actual SKILL.md wording rather than a separate fresh-session phrase test, since there is no new natural-language trigger to test) |
| D6 | Baseline with vs. without | 2 (baseline.md) |

## E. Unattended and scheduled
| # | Check | Score |
| --- | --- | --- |
| E1 | Self-contained, states success + time zone | 2 |
| E2 | Per-source bookmarks, not fixed windows | 2 (full regeneration by design — no bookmark needed) |
| E3 | Failed reads reported as unreadable | 2 |
| E4 | Posts count as sent only after confirmation | 2 (archive log written only after a successful file write) |
| E5 | Read-only credentials, spend cap | 1 (code-level read-only discipline, not a DB-role guarantee — the reused credential is admin-role; noted as a future hardening) |
| E6 | Preferences re-read from a store the agent cannot edit | 2 (overlay file) |
| E7 | Runs opened and read, not judged by status alone | 2 |

## F. 741 house rules
| # | Check | Score |
| --- | --- | --- |
| F1 | Client message + Drive link where a deliverable exists | 2 (n/a — no client deliverable in this build) |
| F2 | Per-change go before a live website change | 2 (n/a — no website touched) |
| F3 | Every data point verified, no guesses | 2 (backfill traced to Martin's own words; ambiguous dates computed and shown, not guessed) |
| F4 | STE in replies and artifacts | 2 |
| F5 | No method sources named in client material | 2 (n/a — no client material) |
| F6 | Shows up in the overview Excel by itself | 2 (n/a at this phase — internal fix to morning-grill, which already has its own `_run.json` visibility; no new client-facing workflow run to register) |
| F7 | Martin guide where a client/prospect sees the deliverable | 2 (n/a, confirmed by the brief: system/data-architecture fix, no client or prospect ever sees it) |

## Result
Total: 71 / 74 → 95.9 %. Blocking zeros: 0.
Decision: ship (no zero in A or D; both open items are 1s, noted as future hardening, not blocking).
