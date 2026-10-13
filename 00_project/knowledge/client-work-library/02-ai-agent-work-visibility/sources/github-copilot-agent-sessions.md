# GitHub Copilot: manage and track agent sessions

- URL: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/manage-and-track-agents
- Type: official doc
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- An "agents panel" is on every GitHub page. An "agents page" lists all running and past sessions in one place.
- The list shows sessions that you started. It also shows sessions where another user asked Copilot to work on your work.
- Each repository has an Agents tab. Cloud agent sessions are shared by default with all people who have repository access.
- A session opens a log and an overview. The overview shows progress, token usage, and session length.
- The log shows the reasoning of the agent and the tools it used to explore, change, and validate the work.
- Copilot is the author of each commit. The human who started the task is co-author. Each commit message links to the session log for review and audit.
- A human can steer a running session with a follow-up message. Each steering message costs AI credits.
- A human can stop a session. The stop keeps the commits that the agent already pushed.
- Users can archive cloud sessions, but they cannot delete them. This keeps a durable record.
- Users can ask Copilot Chat questions about their past sessions, if session sync is on.

## Gaps / bias notes
- The page gives no fixed list of session statuses.
- The page does not say who must approve the pull request. Repository rules control this.
- Older doc versions use the name "coding agent". Newer versions use "cloud agent".
