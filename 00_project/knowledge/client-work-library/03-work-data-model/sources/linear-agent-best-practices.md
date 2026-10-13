# Linear Developers: Agent best practices
- URL: https://linear.app/developers/agent-best-practices
- Type: Official API documentation (guidance)
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- The issue has a separate Issue.delegate field for the agent. The agent sets itself as delegate when no delegate exists.
- If an automation (not a human) delegates the issue, the issue stays in triage. A human then decides the assignment.
- When a human delegates an issue that is not yet started, the agent moves it to the first status of the "started" type.
- The agent sends a thought activity in 10 seconds as a first reply. It can send follow-ups for 30 minutes before the session goes stale.
- The agent rebuilds the conversation from agent activities, not from comments. The reason: users can edit comments, but activities stay fixed.
- The agent sends an elicitation when it needs input, an error when it fails, and a response when it finishes.
- On a response, Linear also writes a comment in the issue thread. The human sees the result where they already work.
- Gaps / bias notes: The guide does not state a general rule on human accountability. It does not cover links to pull requests. It targets coding agents.
