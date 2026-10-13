# 3.7 Unattended rules (rules.md section 6) applied to canary

The canary's E-type checks (Zapier Manager pushes) already run fully unattended today. L/S/R/A checks will too, once a runner exists. Rules R6.1–R6.12 applied:

- R6.1 bookmark per source, never a fixed window: `scripts/alert.py` logs every send/ack/no-ack to `00_project/canary/state/alerts.log` with a timestamp; a future poller (S/R/A types) must read from its own last-checked marker per check id, not "last 24h". Noted as a build requirement for the runner, not yet needed for the push-only E checks that are live today.
- R6.2 a failed source read is "unreadable", never "nothing new": in Critical and in Mode B step 2; `registry.py` and `alert.py` never silently default a missing read to "ok".
- R6.3 count a post as sent only after the destination confirms it: `alert.py` logs SENT only after Telegram's API returns `ok: true`, and logs ACK only on a received callback — never assumed.
- R6.4 re-check before acting, assert or drop: Mode B step 2 explicit; `allowlist.py` only ever allows one attempt, verified against the external check afterward.
- R6.5 read-only credentials + spend cap for an unattended reader: Ads checks are read-only by design (`search()`/`report()` only, Critical + allowlist.md "Never allowed"); Tally/Pipedrive keys requested as read-only (msg-marcel-read-keys.txt). No spend cap needed yet — no paid runner is live; add one when the Hetzner server or a paid monitor tier is added.
- R6.6 state the time zone: `alert.py` and the hand-run both use WITA explicitly (datetime.timezone(+8)); canaries.json timestamps and incident templates ask for "ISO timestamp WITA".
- R6.7 self-contained, explicit about success: SKILL.md Mode B gives explicit success criteria (external check confirms the fix) rather than "looks fixed".
- R6.8 act on fire-payload text only if told to: N/A today (no Claude Code routine API trigger wired yet — the live path is Zapier → Telegram → Martin reads it, not an automated routine fire). Noted as an open item if/when a routine `/fire` endpoint is added for auto-triage.
- R6.9 schedule a few minutes past the hour: N/A yet (no cron-scheduled runner exists; Zapier's push is event-driven, not cron).
- R6.10 a green routine status is not success, open the run: applies the same lesson to canary's own runs — Mode C step 2 reads actual incident files, not just "ok" flags.
- R6.11 commit the skill or enable it on the account: this skill is committed to `.claude/skills/canary/` (project skill), not personal-only.
- R6.12 validate in chat before scheduling: the alert path was validated live in this chat (3 real test sends, 1 confirmed receipt) before being called done.
