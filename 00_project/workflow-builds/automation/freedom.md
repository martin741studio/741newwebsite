# 2.5 Degrees of freedom per step (automation-completion)

Reusing the automation-build scorecard's B5 decision (already scored 2/2: "fragile steps
are scripts; build steps are heuristics") and making it explicit per step, including the
two items new since 2026-10-14:

| Step | Freedom | Why |
|---|---|---|
| Inventory (P0) | heuristic | which lists to open, what counts as "full" varies by tool |
| Spec (P1) | template, filled by heuristic | exact template in `templates/automation-spec-de.md`; content is judgment |
| Go/no-go at checkpoints | zero freedom | hook-enforced: no `go spec` text, no phase change |
| Zapier AI draft (P3a) | high freedom to draft, zero freedom on the gate | Copilot/Agents may propose anything; whether the account is right, whether the draft counts as evidence, and whether its own "tested"/"published" language counts — all scripted/fixed, never a judgment call |
| Live/test data separation | zero freedom | hard rule since 2026-10-14: never test on anything live; hook-checkable via TEST markers |
| Click work (P3) | heuristic path-finding, zero freedom on the readback | how to reach a field varies by tool; that a readback happens after every write does not |
| Class G/M actions | zero freedom | `automation_guard.py` denies by rule, not by judgment |
| Done/live claim | zero freedom | `automation_done_gate.py` blocks on a missing/failing report, regardless of wording |
| Verifier subagent | heuristic (what to re-check) inside a fixed mandate (try to refute, report only correctness gaps) |
| Runbook/handover text | heuristic, within a fixed template and language rule (German, STE-equivalent, no team names) |

This table itself needed no new design — it is the automation-build design, restated
step-by-step to confirm nothing was missed before re-scoring.
