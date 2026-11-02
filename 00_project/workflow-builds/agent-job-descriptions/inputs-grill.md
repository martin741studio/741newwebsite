# Inputs grill — agent-job-descriptions (Step 0.0)

Pre-filled 2026-11-03 from the chat-base brief. Confirmed by Martin: PENDING (card Q7 at Checkpoint 1, round 1).

## Job
Input: the roster of 741 agents (sessions, scheduled tasks, registry) and the agent-job library.
Transform: for each agent, write one job description (title, goal, trigger, duties, data, tools with risk rating, actions alone, actions with go, never-lines with enforcement rung, caps, delegation, report shape, manager, review day, edge cases), validated by a script; keep a roster; run a weekly review with a grade from outside.
Output: `agent-jobs/<agent-id>.md` per agent, placed where that agent loads it; `agent-jobs/roster.md`; weekly review files; applied rung fixes.
Who uses it: Martin (manager) and every 741 agent (reads its own description every session/run).

## Runtime Surface
Terminal / Claude Code skill `.claude/skills/agent-job-descriptions/`, triggered in a chat (write mode) and from the morning grill on the review day (review mode).

## Cadence
Write mode on demand (first batch now, then per new agent). Review mode weekly on a fixed day (Q4).

## Hard Limits
- Never a second approval system: every gate maps onto the go-gate hook or a card with "Go" (memory `go-gate-hook-needs-typed-go`).
- Never places or edits a file another agent loads without a card "Go" for that file.
- Never edits hooks or settings (go-gate denies it anyway); hook changes are proposed, done in a separate turn.
- The agent never grades itself; grades come from Martin or a fresh reviewer from evidence.
- Standing house rules apply (STE, slop 5/5, cards not prose lists, no tool names in client text).
