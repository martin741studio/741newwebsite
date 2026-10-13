# O4 — Away from the desk: Remote Control, mobile app, push, channels

- URLs: https://code.claude.com/docs/en/remote-control , https://code.claude.com/docs/en/mobile , https://code.claude.com/docs/en/channels , https://code.claude.com/docs/en/whats-new/2026-w34
- Type: official docs (living pages)
- Publish date: living docs. W34 digest covers Aug 17–21, 2026
- Fetch date: 2026-10-13 (remote-control, mobile, channels). W34 from repo copy 2026-10-11

## Remote Control

- Connects claude.ai/code or the Claude iOS/Android app to a Claude Code session that runs on the Mac. Code, files, MCP servers stay local.
- Start: `claude remote-control` (server mode, many sessions, default capacity 32), `claude --remote-control` / `--rc` (interactive), or `/remote-control` inside a session (also in Desktop and VS Code).
- Since week 34 (Aug 2026) a machine running `claude remote-control` shows as a device card in the app's Code tab. You can start a new session on the Mac from the phone. Remote Control left research preview then.
- Auto-connect for all sessions: `/config` "Enable Remote Control for all sessions" or `remoteControlAtStartup: true` in user settings.
- Needs Pro/Max/Team/Enterprise with claude.ai login. No API keys. Not with `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`.
- The Mac must stay on and the `claude` process must keep running. Sleep or network loss: reconnects on wake. Server mode gives up after about 10 minutes of network outage.
- From the phone: Manual, Accept edits, Plan, Auto modes. No Bypass permissions.
- Photos and files sent from the phone land on the Mac (`~/.claude/uploads/`).

## Push notifications

- Only while Remote Control is active. Two `/config` toggles: "Push when Claude decides" and "Push when actions required".
- Claude decides when to push (task done, decision needed). You can ask in the prompt: "notify me when ...". No per-event configuration.
- Pushes are skipped while you type in the connected terminal. `CLAUDE_CLIENT_PRESENCE_FILE` can suppress pushes while you are at the Mac.

## Mobile app as client

- The app is a client, not a place where code runs. It reaches cloud sessions, Projects, Remote Control sessions, and Dispatch (Pro/Max).
- If the Mac will be off, use cloud sessions or Projects. Remote Control and Dispatch need the Mac on.

## Channels (research preview)

- An MCP server pushes events into a running session. Telegram, Discord, iMessage plugins included. Two-way chat bridge possible.
- Events only arrive while the session is open. For always-on, run Claude in a persistent process.

## Why it matters

Martin can answer the morning grill from the phone. The grill session should run on the Mac with Remote Control on, so the decision prompts reach the phone as pushes.

Short quote: "your computer has to stay on and the claude process has to keep running"
