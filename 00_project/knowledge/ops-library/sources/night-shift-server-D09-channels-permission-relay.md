# D09 — Channels and permission relay (approve by phone via Telegram/Discord)

- Author/org: Anthropic (Claude Code docs)
- Type: official docs (living pages; channels are in research preview)
- Publish date: living docs, counted as current on fetch date
- URLs: https://code.claude.com/docs/en/channels , https://code.claude.com/docs/en/channels-reference
- Fetch date: 2026-10-13
- Relation to existing library: O4 lists channels; the permission-relay details here are new.

## Extract (own words)

- A channel is an MCP server that pushes events into a running Claude Code session. Telegram, Discord, iMessage and a test "fakechat" plugin are in the preview. Events only arrive while the session is open, so an always-on setup needs a background process or persistent terminal.
- Channels work with a claude.ai login **or a Console API key**. Not on Bedrock, Vertex or Foundry. Team/Enterprise must enable them.
- Each channel plugin keeps a sender allowlist. Unknown senders are dropped silently. Pairing: the bot sends a code; you approve it in the session.
- **Permission relay:** when a tool needs approval, the local dialog opens and, in parallel, the channel can forward the prompt to the phone. Whichever answer comes first wins. Covers tool approvals like Bash, Write, Edit. Trust and MCP consent dialogs do not relay.
- The relayed request has a 5-letter ID (no letter "l"), the tool name, a description, and an input preview (up to 3,500 code points per field; credentials masked from v2.1.234). The reply is `yes <id>` or `no <id>`. A verdict counts only for that one call.
- Anyone who can reply through the channel can approve tool use. Only declare relay if the channel authenticates the sender.
- During the preview, `--channels` only accepts plugins on Anthropic's allowlist. Custom channels need `--dangerously-load-development-channels`.

## IF/THEN rules for 741

1. IF the server session runs on an API key (so Remote Control is not possible), THEN use the Telegram channel with permission relay as the phone approval path.
2. IF Telegram relay is on, THEN allowlist only Martin's Telegram ID and keep the bot token on the server only.
3. IF a card needs more than yes/no (options a/b/c), THEN send it as a channel message and let Claude parse the reply. Use relay only for tool approvals.
4. IF the night shift must survive restarts, THEN run the channel session under tmux or a service. A closed session receives nothing.

## Limits / caveats

- Research preview. Flag syntax and protocol may change.
- Relay shows the command preview; long commands are cut to start and end around a marker.
