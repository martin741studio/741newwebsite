# Roadmap Schema Reference

This reference documents the fields and valid states of `roadmap.json`.

## Milestone States
- `completed`: Verified and done, evidence recorded.
- `in_progress` / `ready_for_execution`: Current active milestone.
- `pending`: Awaiting completion of prerequisite milestones.
- `blocked`: Blocked by external dependency (e.g. client access grant).

## Task States
- `ready`: Can be executed immediately by an agent.
- `in_progress`: Under active execution.
- `completed`: Executed and verified.
- `blocked`: Cannot proceed until blocker is cleared.

## Phase Alignment
- $M_1$: Maps to $P_2$ Audit
- $M_2$: Maps to $P_3$ Un-Burning / Quick-Wins
- $M_3$: Maps to $P_4$ Build-up & $P_5$ Content
- $M_4$: Maps to $P_6$ Tracking & Proof
