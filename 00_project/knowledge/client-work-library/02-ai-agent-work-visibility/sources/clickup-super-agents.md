# ClickUp: Super Agent instructions, Skills, triggers, knowledge, and memory

- URL: https://help.clickup.com/hc/en-us/articles/37092796379927-Super-Agent-instructions-Skills-triggers-knowledge-and-memory ; audit log details from https://help.clickup.com/hc/en-us/articles/21929900448535-Workspace-audit-logs (search index only)
- Type: official doc
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- A Super Agent starts work in three ways: manual (mention, direct message, or task assignment), scheduled, or automated by an Automation.
- "Assign task" is a manual trigger. The agent appears as a task assignee, like a human teammate.
- Each trigger can carry its own extra instructions, in addition to the main instructions.
- The agent profile has five sections: Instructions and Skills, Triggers, Tools, Knowledge, and Memory.
- Knowledge lists the data the agent can use. Mentions of tasks, Docs, or Lists in the instructions add them to the knowledge.
- The agent asks for approval before it stores a "preference" memory from user feedback.
- Data shared with an agent becomes available to every person who can trigger it. This is a leak risk.
- The Workspace audit log records agent actions on tasks, such as assignee and status changes. A separate Agents log records edits to instructions, knowledge, and triggers (from the search index of the audit log article).
- When an admin deactivates an agent, its history and comments stay.

## Gaps / bias notes
- The main page has no status vocabulary for agent work and no review step.
- I could not fetch the audit log article (HTTP 403). Those details come from search snippets of the official help center.
- ClickUp writes for its own product. It gives no data on quality or errors.
