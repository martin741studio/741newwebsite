# O6 — Cowork: cloud move (6 Oct 2026), scheduled tasks, Dispatch

- URLs:
  - https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile (fetched 2026-10-13)
  - https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork (repo copy 2026-10-11)
  - https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork (repo copy 2026-10-11)
  - https://code.claude.com/docs/en/desktop#sessions-from-dispatch (fetched 2026-10-13)
- Type: official help articles (living pages)
- Local copies (older two): `00_project/knowledge/workflow-library/official-docs/cowork/`

## Cloud move

- Since 6 Oct 2026, new Cowork tasks on Pro and Max run in Anthropic cloud. The "Only on your computer" option was removed. There is no switch back.
- Tasks started on the computer before 6 Oct finish there. Scheduled tasks that already ran on the computer keep running there. New scheduled tasks run in the cloud.
- Team: beta, cloud on by default. Enterprise: admin-enabled.
- "Cowork is now just Claude": the Chat/Cowork switch disappears. Claude decides if a message is a quick answer or a task (gradual rollout).
- For new tasks that must run only on the computer, the article points to Claude Code in the Desktop app.

## Scheduled tasks (Cowork)

- Cadence presets: hourly, daily, weekly, weekdays, or manual. Approval mode and model are set per task.
- Run with no device online. Each run is its own Cowork session. Review under "Scheduled" in the sidebar on any surface.
- Use the connectors and skills of the Claude account. Plugins and account files also work.
- Local folders: a cloud session reaches connected folders on the Mac only while the Desktop app is open, and only if the session started on desktop or is a scheduled task. If the app is closed, the run continues without local files.
- Local connectors and plugins with local MCP servers work through the Desktop app only.

## Dispatch

- One persistent phone-to-desktop thread. Claude spins up Code sessions for development work and Cowork sessions for knowledge work. Push notification when done or when it needs a go-ahead.
- Needs the Mac awake and the Desktop app open. Pro/Max only.
- As of the 2026-10-13 fetch: "Dispatch isn't available to new users." Existing users can keep using it for now.
- App approvals in Dispatch-spawned Code sessions expire after 30 minutes.

## Why it matters

A Cowork scheduled task is the simplest no-code way to get a 07:00 brief from Gmail/Calendar/Drive/Notion connectors with the Mac off. It cannot read the local 741 repo unless the Desktop app is open. Do not build the new workflow on Dispatch: it is closed to new users.

Short quote: "Scheduled tasks run in the cloud, so they no longer need your computer to be awake."
