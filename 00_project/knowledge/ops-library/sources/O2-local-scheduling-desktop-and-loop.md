# O2 — Local scheduling: Desktop scheduled tasks and /loop

- URLs: https://code.claude.com/docs/en/desktop-scheduled-tasks and https://code.claude.com/docs/en/scheduled-tasks
- Type: official docs (living pages)
- Publish date: living docs, no fixed date
- Fetch date: 2026-10-11 (repo copies, count as current)
- Local full copies: the files `desktop-scheduled-tasks.md` and `scheduled-tasks.md` in the repo folder for official Claude Code docs (workflow library)

## Comparison table from the docs (summarised)

| | Cloud routine | Desktop task | /loop |
|---|---|---|---|
| Runs on | Anthropic cloud | your Mac | your Mac |
| Mac must be on | no | yes | yes |
| Open session needed | no | no | yes |
| Local files | no (fresh clone) | yes | yes |
| Permission prompts | none (autonomous) | per task | inherits session |
| Minimum interval | 1 hour | 1 minute | 1 minute |

## Desktop scheduled tasks (local)

- Created in the Desktop Code tab: Routines > New routine > Local. Or ask Claude in any Desktop session in plain language.
- Presets: Manual, Hourly, Daily, Weekdays, Weekly. Other intervals by asking Claude.
- Runs only while the Desktop app is open and the Mac is awake. A run during sleep is skipped.
- "Keep computer awake" setting prevents idle sleep. Closing the lid still sleeps the Mac.
- Missed runs: on wake, Desktop runs one catch-up run for the most recent missed time in the last 7 days. Older misses are dropped. A 9:00 task can run at 23:00.
- Each task has its own permission mode. In Manual mode a missing permission stalls the run until you approve. Fix: click "Run now" once and choose "always allow".
- A small fixed delay (a few minutes) is added to stagger traffic.
- Each run starts a fresh session and shows under "Scheduled" in the sidebar with a desktop notification.
- Desktop scheduled task sessions cannot send or receive messages between desktop sessions through the app's session surface.
- A task can change its own schedule or prompt with the `update_scheduled_task` tool.
- Prompt lives at `~/.claude/scheduled-tasks/<name>/SKILL.md`. Schedule, folder, model are not in that file.
- Optional worktree toggle isolates each run from uncommitted changes.

## /loop and cron tools (session-scoped)

- `/loop 20m <prompt>` or `/loop` with self-paced interval. One-shot reminders by natural language.
- Fires only while Claude Code is running and idle. No catch-up for missed fires.
- Recurring tasks expire after 7 days (fire once more, then delete).
- A fixed jitter delay per task.
- Backgrounding the session (agent view) keeps `/loop` tasks running without a terminal.

## Why it matters

The Desktop task is the right tool for anything that needs local files (the 741 repo, portal staging, local scripts). It is not reliable for a fixed 07:00 slot unless the Mac is awake. The doc itself advises time guardrails in the prompt.

Short quote: "If your computer sleeps through a scheduled time, the run is skipped."
