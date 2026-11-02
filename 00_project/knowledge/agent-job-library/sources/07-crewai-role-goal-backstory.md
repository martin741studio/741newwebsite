# 07 — CrewAI: Agents (role / goal / backstory) and "Crafting Effective Agents"

Type: framework documentation (multi-agent). Fetched 2026-11-03.
URLs: https://docs.crewai.com/en/concepts/agents · https://docs.crewai.com/en/guides/agents/crafting-effective-agents

## Key content
- Required fields: role ("the agent's function and expertise"), goal ("the individual objective that guides decision-making"), backstory ("context and personality"). Optional: tools, guardrail, max_iter (default 20), max_execution_time, max_retry_limit (2), allow_delegation (False).
- Role: "Be specific and specialized: instead of 'Writer', use 'Technical Documentation Specialist'"; "Align with real-world professions."
- Goal: "clear and outcome-focused", "emphasize quality standards", "incorporate success criteria".
- Backstory: "establish expertise", "define working style and values".
- "Specialists over generalists": a focused agent gives clearer output and more consistent performance.
- Task anatomy: description (process, scope, constraints) + expected_output (format, structure, quality criteria, examples). "Single purpose, single output." Avoid "god tasks".
- Common mistakes: unclear instructions, god tasks, missing expected output.

## Assessment for 741
New vs. video: "goal with success criteria" and "expected output per task" are fields Tyler lacks; the explicit caps (max iterations, max retries, max execution time) are the runtime version of an approval gate on cost; "allow_delegation=False" by default is a rule about who may start other agents.
Marketing: the backstory field is persona theatre; evidence for its value is anecdotal. 741 should keep backstory to one line of working style, not a biography.
Usable for 741: add "goal with success criterion" and "expected output" to the block; add "may delegate to: [list or none]" and "caps: runs per day / spend per run / retries" fields; keep roles as real professions (Ops manager, Editor, Watchman).
