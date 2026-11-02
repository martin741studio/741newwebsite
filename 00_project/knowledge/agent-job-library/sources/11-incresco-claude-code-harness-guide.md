# 11 — Incresco: "Claude Code as an Agent Harness: The Complete Practitioner's Guide"

Type: practitioner guide (Claude partner), 2026-10-11, every behaviour checked against Claude Code docs and marked "our practice" where not. Fetched 2026-11-03.
URL: https://www.increscotech.com/blog/claude-code-agent-harness-complete-guide

## Key content
- A harness answers five questions: what does the agent know before it starts, what may it touch, how does it know it is finished, who checks the result, what happens to the lesson when it is wrong.
- Roles: lead session builds the harness; subagents do bounded work (one step, inputs, check); "the human owns the goal and the last approval."
- Task brief fields: task, deliverable and location, acceptance checks, source material, allowed changes, run limit ("three attempts per step, or one hour").
- "If you would be upset to see it skipped even once, it is not an instruction. It is a hook. A prompt is for judgment only."
- Permissions: "Ask before publishing, sending or spending"; "Choose how tight to be by what a mistake would cost, not by how much you trust the agent today."
- Verification gating levels: in the prompt → /goal → Stop hook → second opinion. "If you cannot verify it, do not ship it." Verification table per requirement: verdict pass/fail/unresolved + evidence; "leave missing evidence visible instead of rounding it up."
- Feedback ladder (where a rule lives): a CLAUDE.md line → path-scoped rule → skill → hook → reviewer/Stop check. Loop: correct → if the same mistake appears twice, write the rule at the right rung → clear and retry → prune.
- Completion: every item points to observable evidence; partial status with exact steps left, "not a confident summary that hides the gap."
- Delivery: "match human attention to the cost of undoing a change."

## Assessment for 741
New vs. video: the rule ladder and the "twice → rung" rule are the drift-control mechanism; the brief field list adds "allowed changes" and "run limit"; the completion rule forbids the confident-summary failure that 741 has seen (claims without data).
Marketing: Incresco services pitch at the end; the body is sourced.
Usable for 741: job-description sections "Allowed changes" and "Run limit"; the weekly review's output is a ladder decision per mistake (prose line / rule file / skill / hook); the review template carries pass/fail/unresolved with evidence, no rounding up. Also matches 741's existing homeostasis rule in the creation workflow (repeated chat corrections become skill edits).
