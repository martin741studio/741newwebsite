# Linear Developers: Developing the Agent Interaction
- URL: https://linear.app/developers/agent-interaction
- Type: Official API documentation (Developer Preview)
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- Linear creates an AgentSession each time a user mentions an agent or delegates an issue to it. One session is one agent run on one issue.
- Session states are pending, active, error, awaitingInput, complete and stale. Linear sets the state from the last activity that the agent sent. The agent does not set the state itself.
- The agent sends typed activities: thought, action (tool name, parameter, result), elicitation (question to the human), response (final result) and error.
- Only the human can create a prompt activity. This keeps human input and agent output apart in the log.
- Thought and action activities can be ephemeral. The next activity replaces them, so the log does not fill with noise.
- A session can carry a plan: a list of items with the status pending, inProgress, completed or canceled. An update replaces the full list.
- A session carries externalUrls as label and url pairs. Each url is unique in the list. A pull request shows up as one of these links.
- The webhook receiver must answer in 5 seconds. The agent must send a first activity in 10 seconds, or the session shows as unresponsive.
- Gaps / bias notes: The API is a Developer Preview and can change. The page does not cover idempotency keys, retries or event order. It is a vendor view for software teams, not for agencies.
