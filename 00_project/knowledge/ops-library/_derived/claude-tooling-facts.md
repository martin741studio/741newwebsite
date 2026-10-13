# Claude tooling facts for the morning grill (verified)

Each fact names the official doc and the fetch date. "Repo copy" means `00_project/knowledge/workflow-library/official-docs/` (fetched 2026-10-11). All docs are living pages. Re-check before you build.

## 1. What runs unattended, and where

| Tool | Runs on | Mac must be awake | Local files (741 repo) | Approval prompts | Min. interval |
|---|---|---|---|---|---|
| Cloud routine (Claude Code) | Anthropic cloud | No | No (fresh GitHub clone) | None, fully autonomous | 1 hour |
| Desktop scheduled task (Claude Code, "Local") | Mac | Yes, and Desktop app open | Yes | Per task mode. Manual mode stalls on a missing permission | 1 minute |
| `/loop` / cron in a session | Mac | Yes, and the session open + idle | Yes | Inherits the session | 1 minute |
| Cowork scheduled task (new since 6 Oct) | Anthropic cloud | No | Only while Desktop app is open | Approval mode per task | hourly preset |
| Dispatch | Mac | Yes, Desktop app open | Yes | Push for go-ahead | n/a |

Sources: desktop-scheduled-tasks + scheduled-tasks comparison table (repo copy, 2026-10-11). Routines (repo copy, 2026-10-11). Cowork help 15520349 (fetched 2026-10-13). Dispatch help 13947068 (repo copy 2026-10-11) and Desktop doc (fetched 2026-10-13).

## 2. Cloud routines — routines.md (repo copy 2026-10-11)

- Saved prompt + GitHub repos + cloud environment + connectors. Research preview.
- Triggers: schedule (hourly / daily / weekdays / weekly / one-off), API `/fire`, GitHub PR or release events.
- Minimum schedule interval 1 hour. Cron only via `/schedule update`. Enter times in local zone.
- On-the-hour starts may be several minutes late. The doc suggests e.g. 9:07.
- No permission picker. Every tool of every included connector, writes included, runs without asking. All connectors are included by default. Remove unneeded ones.
- Local MCP servers added with `claude mcp add` are not available. Use claude.ai connectors or a committed `.mcp.json`.
- Default network "Trusted" allowlist. Other hosts get 403 until you edit the environment.
- API/Run-now text arrives as untrusted data. The saved prompt must say to act on it.
- Green run status = no infrastructure error only. Open the run to check the result.
- Limits: 100 scheduled runs/hour/account; 30 Run now + API fires/hour/routine. Uses normal plan usage.
- Missing GitHub access: runs skipped up to 72 h, then the routine turns off.
- Create/manage at claude.ai/code/routines, Desktop Routines page (Cloud), or `/schedule` (CLI. Not inside a cloud session).

## 3. Desktop scheduled tasks — desktop-scheduled-tasks.md (repo copy 2026-10-11)

- Code tab > Routines > New routine > Local. Requires Desktop ≥ 1.1.5368. A folder is required.
- Presets Manual / Hourly / Daily / Weekdays / Weekly. Other intervals by asking Claude.
- Fires only while the app runs and the Mac is awake. Sleep = skipped run. "Keep computer awake" stops idle sleep. A closed lid still sleeps.
- On wake: exactly one catch-up run for the latest miss within 7 days. A 07:00 task can run at 23:00, so add time guardrails to the prompt.
- Manual-mode runs stall on a missing permission. Use "Run now" once and "always allow". MCP tools marked `requiresUserInteraction` stall every run.
- Each run = fresh session under "Scheduled" + desktop notification.
- These sessions cannot send or receive cross-session messages through the desktop app's session surface.
- Prompt file: `~/.claude/scheduled-tasks/<name>/SKILL.md`. A task can reschedule itself via `update_scheduled_task`.

## 4. /loop — scheduled-tasks.md (repo copy 2026-10-11)

- Session-scoped. Fires only while Claude Code runs and is idle. No catch-up.
- Recurring tasks expire after 7 days.
- Backgrounding the session into agent view keeps `/loop` tasks running without a terminal.

## 5. Cowork scheduled tasks and the 6 Oct change — Cowork help 15520349 (fetched 2026-10-13), 13854387 (repo copy 2026-10-11)

- From 6 Oct 2026 new Cowork tasks on Pro/Max run in the cloud. No switch back. Old local tasks and old local scheduled tasks keep running on the Mac.
- Scheduled tasks run "with no device online". Cadences: hourly, daily, weekly, weekdays, manual. Approval mode and model per task.
- Cloud sessions reach connected local folders only while the Desktop app is open and only if started on desktop or as a scheduled task. App closed = no local files.
- Local connectors and plugins with local MCP servers work only through the Desktop app.
- For new work that must stay on the Mac, the help article points to Claude Code in the Desktop app.

## 6. Dispatch — help 13947068 (repo copy 2026-10-11, note re-read 2026-10-13) and desktop.md (fetched 2026-10-13)

- Phone-to-Mac persistent thread. Spawns Code or Cowork sessions. Push when done or when it needs a go-ahead.
- Needs Mac awake + Desktop app open. Pro/Max only, not Team/Enterprise.
- "Dispatch isn't available to new users." Do not plan around it.

## 7. Remote Control and push — remote-control.md, mobile.md (fetched 2026-10-13), whats-new w34 (repo copy)

- Drive a Mac session from the Claude app or claude.ai/code. Code and files stay on the Mac.
- `claude remote-control` (server mode, up to 32 sessions), `claude --rc`, or `/remote-control`. Auto-connect: `/config` or `remoteControlAtStartup: true`.
- Since week 34 (Aug 2026): the Mac shows as a device card in the app. You can start a new session on the Mac from the phone. Out of research preview.
- Mac must stay on and `claude` must keep running. Reconnects after sleep. Server mode quits after about 10 minutes of network outage.
- Phone modes: Manual, Accept edits, Plan, Auto. Not Bypass.
- Push notifications only while Remote Control is active. Toggles in `/config`: "Push when Claude decides", "Push when actions required". Claude chooses when. You can ask "notify me when ...". No per-event config. Skipped while you type in the terminal. `CLAUDE_CLIENT_PRESENCE_FILE` can mute while you are at the Mac.
- Needs a claude.ai login (no API key), not with `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`.

## 8. Channels — channels.md (fetched 2026-10-13)

- Research preview. MCP server pushes events (Telegram, Discord, iMessage plugins) into a running session. Two-way possible.
- Events arrive only while the session is open.

## 9. /goal — goal.md (repo copy 2026-10-11)

- Keeps one session working until a small model judges the condition met or impossible. One goal per session, ≤ 4,000 characters.
- Evaluator reads only the transcript. It runs no commands.
- Add "or stop after N turns" to bound it. Does not change permission mode. Use auto mode for unattended turns.
- Works with `claude -p`, Desktop, Remote Control. Restored on resume.

## 10. Cross-session messaging — cross-session-messaging.md (repo copy 2026-10-11)

- On by default from v2.1.224 (macOS). `SendMessage` / `ListAgents`. `/list-agents` shows targets.
- Local: socket, not via Anthropic. Other machines and cloud sessions: via Remote Control.
- A message can never approve a permission or change config/CLAUDE.md. Slash commands inside do not run.
- `notify_when_idle` for local sessions, expires after 12 hours.

## 11. Agent view — agent-view.md (fetched 2026-10-13)

- `claude agents`: one table of background sessions (working / waiting on you / done). Research preview.
- Sessions are local: survive sleep, stop on shutdown. Each uses quota.

## 12. Projects — claude-projects.md (repo copy 2026-10-11)

- Coordinator conversation + cloud threads. "Waiting on you" in Overview. Project instructions and memory reach all threads. Routines tab.
- Public beta Pro/Max, gradual rollout. Threads default to Opus at high effort (expensive).
- A thread can run on the Mac via Remote Control when it needs local tools.

## Bottom line for Martin's setup

- **Runs with the Mac off:** cloud routine (needs inputs on GitHub or connectors) and Cowork scheduled task (connectors and account files only).
- **Needs the Mac awake:** Desktop scheduled task, `/loop`, agent view sessions, Remote Control, Dispatch, channels, any access to the local 741 repo or local scripts.
- **Phone interaction:** Remote Control + push (Mac on), or cloud sessions / Projects / Cowork (Mac off).
