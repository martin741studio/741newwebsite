# Linear: AI agents, agent interaction, and agent best practices

- URL: https://linear.app/docs/agents-in-linear ; https://linear.app/developers/agent-interaction ; https://linear.app/developers/agent-best-practices
- Type: official doc (user doc + developer docs)
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- A user puts an agent in the Assignee field to delegate an issue. Linear then sets the agent as "delegate". The human stays the owner of the issue.
- Delegated issues stay in the human's "My issues" view. Custom views and Insights can filter and group by Delegate. This shows how much work agents get and finish.
- Each agent run is an "agent session". Linear creates it when a user mentions or delegates to an agent.
- Session states are pending, active, awaitingInput, error, complete, and stale. Linear sets the state from the last activity of the agent. The agent does not set the state by hand.
- Agents report through typed activities: thought, action (tool call with result), elicitation (question to the human), response (final output), and error.
- A session can carry a plan: a checklist with steps in pending, inProgress, completed, or canceled.
- A session can hold "external URLs" with a label, for example the pull request or the agent's own dashboard. This links the task to the evidence.
- Best practice: the agent moves the issue to the first "started" state when work begins. It sets itself as delegate so its role is clear.
- If an automation (not a human) delegated the issue, the agent keeps it in triage. A human then decides the assignment.
- The agent must answer within 10 seconds, or Linear shows it as unresponsive. After 30 minutes with no activity, the session becomes stale.
- Rebuild the history from agent activities, not from comments, because people can edit comments.
- Workspace and team "guidance" (markdown with history) tells all agents which repo, which review process, and which rules to use.

## Gaps / bias notes
- Linear builds for software teams. The model fits an agency only in part.
- The user doc does not say in plain words who is accountable. The ownership rule comes from the changelog wording and the delegate field design.
- Plans are a technology preview and can change.
