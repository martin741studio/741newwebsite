# D02 — Cloud sessions (Claude Code on the web)

- Author/org: Anthropic (Claude Code docs)
- Type: official doc (living page)
- Publish date: living doc, counted as current on fetch date
- URL: https://code.claude.com/docs/en/claude-code-on-the-web (plus https://code.claude.com/docs/en/cloud-environments)
- Fetch date: 2026-10-13

## Extract (own words)

- A cloud session is a Claude Code session on an Anthropic VM (Ubuntu 24.04, x86_64). It keeps running after the laptop closes. Start it from claude.ai/code, the mobile Code tab, Desktop (choose Cloud), or `claude --cloud "task"`.
- Plans: Pro, Max, Team, and Enterprise premium or Chat + Claude Code seats.
- VM size: 4 vCPU, 16 GB RAM, 30 GB disk. Bigger jobs may be stopped. The doc points to Remote Control or self-hosted for more.
- Repo access needs GitHub (GitHub App or `/web-setup`). Without a GitHub remote, `claude --cloud` uploads a bundle of the local repo, but results cannot be pushed back to a non-GitHub remote.
- What does NOT carry over: user `~/.claude/CLAUDE.md`, user skills/agents/commands, user plugins, MCP servers added at local or user scope. Repo `.claude/skills`, `.claude/agents` and a committed `.mcp.json` do carry over. A setup script can write a `~/.claude/CLAUDE.md`.
- You pick the permission mode per session. Cloud sessions ignore `dontAsk` and `bypassPermissions` set in settings files.
- Follow-ups from any machine: `claude -p "message" --cloud <session-id>` queues a message and exits. Useful for a script that nudges a running session.
- Idle sessions stop and the VM is reclaimed. A session waiting for an MCP connector approval counts as idle and can expire. Reopening restores the conversation, not running background work or a self-paced `/loop`.
- Cloud sessions share the account's rate limits with all other Claude use. Parallel tasks use limits in proportion.
- Commands time out after 2 minutes by default (Claude can ask for up to 10). Setup scripts are cached only if they finish in about 5 minutes. Interactive SSO logins do not work in a cloud session.

## IF/THEN rules for 741

1. IF a night task only needs a GitHub repo plus connectors, THEN a cloud session or routine is the zero-server option. It costs nothing beyond plan usage.
2. IF the task depends on Martin's user-level skills or CLAUDE.md, THEN commit the needed skills into the repo `.claude/` folder or write them with a setup script. Otherwise the cloud run does not see them.
3. IF a cloud session will wait for Martin's approval on a connector call, THEN expect it may expire overnight. Prefer tasks that end in a draft and a card, not a pending tool approval.
4. IF a task needs a logged-in browser or SSO, THEN do not put it in a cloud session.

## Limits / caveats

- Network is allowlisted by default (see D01). Many client hosts need a Custom allowlist.
- The doc gives no exact idle-expiry time.
