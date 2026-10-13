# N01 — Running Claude Code on a VPS: setup, requirements, and using it from your phone

- Author/org: Melta (mobile app for coding agents; vendor blog)
- Type: practitioner guide
- Publish date: 2026-10-02 (verified: JSON-LD datePublished and `<time datetime>` on page)
- URL: https://getmelta.app/blog/claude-code-on-a-vps/
- Fetch date: 2026-10-13

## Extract (own words)

- Why a VPS: always on, reachable from the phone, and separate from the personal laptop with its browser profiles.
- Minimum: Ubuntu 20.04+ / Debian 10+ / Alpine 3.19+, 4 GB RAM, x64 or ARM64, a supported country, a paid plan or Console account. Native installer, no Node needed.
- Work as a normal user, not root. Bypass mode refuses root. Small boxes may need 2 GB swap for the installer.
- Login options on a headless box: paste-code login, one-year `setup-token`, or an API key. `/status` shows which one is active.
- Keep sessions in tmux. Add three tmux lines so Shift+Enter and notifications pass through.
- Lock down SSH: keys only, no root login, and put SSH behind Tailscale with ufw denying all public inbound.
- Phone access: any SSH app over Tailscale plus `tmux attach`, or Remote Control (needs `/login`, process inside tmux).
- Ban risk: the guide found no official rule against running Claude Code on your own server. It flags three limits: no shared logins, plan limits assume "ordinary, individual usage", and automated access should use an API key or setup-token.

## IF/THEN rules for 741

1. IF Martin rents a server for the night shift, THEN start with 4 GB RAM, a non-root `agent` user, tmux, and Tailscale-only SSH before anything else.
2. IF the server holds client credentials, THEN never use `--dangerously-skip-permissions` there.
3. IF the team (Dinakar, Tantri, Gayo) also needs the server, THEN they need their own Claude logins. One Max login must not be shared.

## Limits / caveats

- Vendor blog promoting its own phone app. The setup facts match the official docs; the ban section is the author's reading of the terms, not Anthropic's.
