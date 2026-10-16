# 1.1 Building block chosen (automation-completion)

Decision: do NOT design a new skill. Reuse the block already chosen for `automation-build`
on 2026-10-11 (design-note.md): Skill `/automation-build` (`disable-model-invocation: true`)
+ 3 hooks (`automation_session.py`, `automation_guard.py`, `automation_done_gate.py`) +
scripts (`run_state.py`, `check_report.py`) + a fresh verifier subagent.

Reason: that design was built specifically from the Marcel Rosenbach failure cases
(failure map F1-F15, `00_project/automation-failure-map.md`), got Martin's checkpoint-1
go on 2026-10-11, scored 85.7% (48/56), and was never installed. A second, independent
incident with the same client (Gewinnspiel Zap, 2026-10-08 to 10-14) shows the exact same
failure clusters it was built to stop: fake "done"/"live and tested" claims with skipped
tests, no readback, silent breakage, slow escalation. The design is not wrong or stale —
it is unused. Building a second, parallel skill would duplicate L0-L6 for no reason
(rule R0.2: don't rebuild what exists as a skill already).

Recommendation for "automation-completion": it is the REWORK/finish-and-install track for
`automation-build`, not a new workflow. This is flagged to Martin as a scope decision at
checkpoint 1 (see cp1 report), per the brief's instruction, because it changes what
"automation-completion" delivers (an install of an existing design vs. a new design).

Rules applied: R0.2 (save as a skill on the third repeat — already done), R0.5 (hook, not
prose, for zero-exception rules — already drafted), R2.10 (side effects → slash command
only — already in the draft frontmatter).
