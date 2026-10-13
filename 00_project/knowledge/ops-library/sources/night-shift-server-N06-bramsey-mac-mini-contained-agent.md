# N06 — mac-mini-remote-control: a contained Claude Code agent on a home Mac mini

- Author/org: bramsey123 (individual, GitHub)
- Type: build log / open-source setup repo (v0.1)
- Publish date: repo created 2026-10-01, last push 2026-10-06 (verified via GitHub API)
- URL: https://github.com/bramsey123/mac-mini-remote-control
- Fetch date: 2026-10-13

## Extract (own words)

- Goal: a dedicated Mac mini runs Claude Code always on, driven from the phone, and contained so a confused or manipulated agent cannot reach the owner's accounts, data or backups.
- Layer 1: the agent runs as its own standard (non-admin) macOS user. No access to the owner's files, Keychain, browser sessions or sudo.
- Layer 2: root-owned managed settings the agent cannot edit: auto mode on, bypass off, no self-added permission rules or hooks.
- Layer 3: scoped secrets only: a password-manager service account limited to one vault, plus revocable, spend-limited API keys.
- Layer 4: every tool call goes to a log the agent cannot rewrite; a health check every 15 minutes verifies layers 1-3 and pushes to the phone on change; Time Machine backups out of the agent's reach.
- Layer 5: Tailscale (no open ports), SSH, and `claude remote-control` for the Claude app.
- Threat model notes: leaks cannot be undone, only revoked; Claude Code settings are enforced by Claude Code itself, so the OS account boundary is the real wall; deny rules on Read do not stop a shell `cat`; failed hooks do not block; the home IP makes all agent traffic traceable to the household.

## IF/THEN rules for 741

1. IF a Mac mini becomes the night machine, THEN create a separate non-admin `agent` user and give it only client-scoped, revocable keys. Martin's own Keychain and Chrome profile stay in his user.
2. IF safety settings matter, THEN put them in root-owned managed settings, so the agent cannot loosen them.
3. IF the night shift runs, THEN a separate health check (outside the agent) pushes to Martin's phone when a guard is off or the agent is silent.

## Limits / caveats

- One person's v0.1 repo, 0 stars at fetch. Strong design, not field-proven.
