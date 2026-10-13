# D03 — Remote Control on an always-on machine (server mode, push, limits)

- Author/org: Anthropic (Claude Code docs)
- Type: official doc (living page)
- Publish date: living doc, counted as current on fetch date
- URL: https://code.claude.com/docs/en/remote-control
- Fetch date: 2026-10-13
- Relation to existing library: extends O4 with server facts.

## Extract (own words)

- Remote Control lets the Claude app or claude.ai/code drive a Claude Code session that runs on your own machine. Files, local MCP servers and tools stay on that machine. The machine must stay on and the `claude` process must keep running.
- Plans: Pro, Max, Team, Enterprise. API keys are not supported. It needs a full claude.ai login (`/login` or `claude auth login`). A `claude setup-token` token or `CLAUDE_CODE_OAUTH_TOKEN` fails with "requires a full-scope login token".
- Server mode: `claude remote-control`. Up to 32 concurrent sessions by default (`--capacity`). `--spawn worktree` gives each phone-started session its own git worktree. `--permission-mode` sets the starting mode. `--chrome` turns on Chrome in the server's sessions.
- On a remote machine the doc says to start `claude` inside tmux or screen, so the session survives an SSH disconnect.
- Server mode exits after about 10 minutes without network. An interactive session keeps retrying. A crashed server-mode session is served again when you message it from the phone (v2.1.238+).
- After a stop, `claude remote-control` (or `--continue`) brings sessions back for about four hours.
- Push to phone: two `/config` toggles, "Push when Claude decides" and "Push when actions required". No per-event setup. Pushes need Remote Control active.
- Permission prompts and AskUserQuestion stay open until answered. Other forwarded dialogs close after 5 minutes by default (`dialogExpiry`).
- A claude.ai connector that needs re-auth cannot be fixed from the phone. Run `claude mcp login "claude.ai <name>" --no-browser` over SSH, open the link on the phone, then `/mcp reconnect`.
- Optional "Trusted Devices" (beta, Pro/Max can turn it on): phone must be enrolled; after 18 hours a biometric step-up prompt appears.
- The transcript is stored on Anthropic servers while connected. Execution stays local. Only outbound HTTPS, no open ports.

## IF/THEN rules for 741

1. IF Martin wants to answer prepared cards from the phone with the agent on a server, THEN run `claude remote-control` under tmux on that server, signed in with his own claude.ai login (not setup-token, not an API key).
2. IF several clients run in parallel overnight, THEN use `--spawn worktree` so phone-started sessions do not edit the same files.
3. IF the server can lose network for more than 10 minutes, THEN wrap `claude remote-control` in a restart loop (systemd or launchd) and resume with `--continue`.
4. IF a night card must reach Martin, THEN turn on "Push when actions required" and keep cards as AskUserQuestion or permission prompts, because those never expire.

## Limits / caveats

- The doc says nothing about Linux desktops or headless servers beyond tmux advice. Remote Control itself needs no display.
- Some commands (`/plugin`, `/resume`) are local-only.
