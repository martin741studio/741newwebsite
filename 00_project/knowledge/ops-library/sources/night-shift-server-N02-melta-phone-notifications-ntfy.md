# N02 — Claude Code notifications on your phone (Remote Control push, hooks + ntfy)

- Author/org: Melta (vendor blog)
- Type: practitioner guide
- Publish date: 2026-10-02 (verified: JSON-LD datePublished)
- URL: https://getmelta.app/blog/claude-code-notifications-on-phone/
- Fetch date: 2026-10-13

## Extract (own words)

- Official path: Remote Control + the two push toggles in `/config`. Needs a claude.ai login, not an API key.
- Generic path: a `Notification` hook in `~/.claude/settings.json` that posts to a push service.
- Hook types: `permission_prompt` fires when an approval has waited about 6 seconds; `idle_prompt` fires about 60 seconds after Claude finished and you did not type. Both only fire when you seem away.
- `Stop` fires after every response, so it is noisy. `PermissionRequest` fires at once for approvals.
- ntfy: no sign-up; the topic name works like a password, so make it long and random (e.g. `openssl rand -hex 12`). Pushover is the paid option (one-time $4.99 per platform, 10,000 messages a month).
- Send only the short message text. Do not push file paths or the last answer to a public ntfy topic; self-host ntfy for anything sensitive.
- A push is not an answer. You still need a way back in: Remote Control, SSH into tmux, or a channel with permission relay.

## IF/THEN rules for 741

1. IF the server runs on an API key or setup-token (no Remote Control push), THEN add a `Notification` hook to ntfy with a random topic so Martin knows a card waits.
2. IF the push could contain client names or data, THEN self-host ntfy or use access tokens, and send only "card waiting: <client-id>".
3. IF a push arrives, THEN the reply path must be one tap away (Remote Control session link or Telegram relay). Design both together.

## Limits / caveats

- Vendor blog. Hook timings (6 s, 60 s) come from the author's reading of the hooks reference; not re-checked here.
