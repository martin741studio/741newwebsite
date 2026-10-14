# Decisions — canary (Martin's answers on AskUserQuestion cards)

## Round 1 (2026-10-14, ~06:25 WITA)
- C1 Alert channel: **"Telegram only"** (my recommendation was Pushover + Telegram). → Bot @Socials741_bot exists (`scripts/telegram-send.py`). Consequence: Telegram cannot break iOS Focus by itself. Setup step: allow Telegram (or the alert chat) in every Focus incl. Sleep, and test at night. No acknowledge button from Telegram itself → the canary adds an inline "OK, ich übernehme" button (bot callback) or a reply as acknowledgement.
- C2 Night rule: **"SEV1 pages 24/7 (Recommended)"** — only "lead path of a live client is broken" (form, funnel, Zap off, site down) pages at any hour, after the agent tried its safe fix. Everything else waits for 06:13.
- C3 Escalation: **"Martin first, Dinakar backup (Recommended)"** — Dinakar gets the page with runbook + diagnosis if Martin does not acknowledge within 10 min.
- C4 Check runner: **"Own server (Hetzner)"** (my recommendation was SaaS + Supabase). → Self-hosted checks on the planned Hetzner server. The server does not exist yet (night-shift-server: no Hetzner account; SSH key ready). Open: what runs until the server exists, and who watches the server (outside heartbeat).

## Round 2 (2026-10-14, ~06:30 WITA)
- C5 Until the server: **"Interim on free tools (Recommended)"** — UptimeRobot free (5-min site/form checks) + Zapier Manager "New Zap Error" / "Zap Turned Off" → Telegram chat. Off-laptop. Moves to the server later.
- C6 Watch the watcher: **"No outside watcher"** (my recommendation was a Healthchecks.io heartbeat). → Accepted risk: a dead server stays unnoticed until the 06:13 grill. Mitigation inside the design at no extra tool: the 06:13 grill shows "last canary run" age and turns red if > 30 min. Revisit after the first server outage.
- C7 Test records: **"No, count real entries (Recommended)"** — no synthetic test data in client systems in daily checks. Reconciliation of real entries (source vs target) + platform error push. Test entries only in the go-live gate of Automation Build.
- C8 Ads read path: **"Ads script per account (Recommended)"** — read-only Google Ads script per account (Bali, Kamil, Suriya, 741), hourly, posts to Telegram; plus MCC email alerts for disapprovals and billing. Only `search()`/`report()`; never mutate, never labels.

## Round 3 (2026-10-14, ~06:40 WITA) — hand-run gos
- C9 Zapier push: **"Go, create it (Recommended)"** — G1 go: create ONE Zapier Manager Zap in Marcel's Zapier: "New Zap Error" + "Zap Turned Off" → Martin's Telegram chat. Changes none of Marcel's existing Zaps.
- C10 Read keys: **"You ask Marcel, I draft (Recommended)"** — I draft a short message; Marcel gives a Tally API key + a read Pipedrive API token via LastPass. Keys later go to a 600-mode file on the server, never into a chat or a form.
- C11 Dinakar path: **"Group '741 Canary' (Recommended)"** — Telegram group with Martin, Dinakar and the bot. SEV1 → Martin's private chat first; after 10 min without tap → group post with @Dinakar.
- C12 UptimeRobot: **"I create it now (Recommended)"** — Martin signs up (martin@741.studio) and connects Telegram; then I add the monitors in his logged-in Chrome.

## Round 4 (2026-10-14, ~06:47 WITA)
- C13 Bot token: **"New '741 Canary' bot (Recommended)"** — Martin creates a separate alert bot in @BotFather and pastes its token himself at Zapier "Sign in" (Zap 383443160 in Marcel's Zapier). The social bot @Socials741_bot stays out of client accounts.
- Test alert 06:33 via @Socials741_bot: Martin: **"need to set up telegram for it first"** → Telegram is not set up on his phone yet. No ack measured. Hand-run alert test repeats with the new bot after setup. (Finding: the channel was not ready; an alert path must be proven on the phone before it counts.)

## Round 5 (2026-10-14, ~07:05 WITA) — hand-run result
- Both Zapier Manager alert Zaps for Marcel are LIVE (G1 executed): "New Zap Error" and "Zap Turned Off" → Martin's Telegram ("741 Canary" bot, private chat). Test messages sent and the first one confirmed received by Martin.
- Bot token handling: Martin created the bot and pasted the token into Zapier himself (I never touch client-facing credential fields); I only read and stored the token locally after that, in a 600-mode file, and read the chat ID via the Bot API.

## Round 6 (2026-10-14, ~13:50 WITA) — Dinakar escalation built
- C14 Build the Dinakar group now: **"Yes, build it now (Recommended)"** — Martin created the Telegram group "741 Canary" (chat id -5487070427) himself, added the canary bot and Dinakar (@DhoniMSD516, provided by Martin directly, no memory file had it).
- C15 How to add Dinakar: **"I'll type his @username or phone here"** — @DhoniMSD516.
- `alert.py` upgraded: on no-ack within `--escalate-after-min`, auto-posts to the group with an @-mention, exit code 4 (ESCALATED). Tested live with a 6-second window — real send, real no-ack, real escalation post confirmed in the group. No real page sent for a fictional incident otherwise.

## Round 7 (2026-10-14, ~08:35 WITA, via the morning grill)
- C16 UptimeRobot notification channel: Martin, live in the grill chat: "use email alerts as the default notification method going forward, not an app" — the iOS app route tried for Marcel's incident didn't work well for him. Settled, not an open gap: UptimeRobot's free plan has no Telegram option anyway (only app push, Pushover, Discord, Google Chat, e-mail). Email stays the channel for UptimeRobot checks; Telegram stays the channel for the Zapier Manager pushes and alert.py escalation. Applied to canaries.json notes for all 3 UptimeRobot-runner checks.

## Round 8 (2026-10-15) — server heartbeat (requested by the Night Shift session)
- C17 Meta-monitoring design: 741-agents-01 (Hetzner, now live per the Night Shift session's v3 autonomy rework) gets a heartbeat check. Design chosen without a new Martin card (follows the already-researched pattern, see canary-research-2026-10-14.md "IF the automation computes..." / architecture file "check-the-checker"): Healthchecks.io (free, 20 checks) — an external, independent service, never routed through our own alert.py/Telegram, so a real server outage can't silence its own alarm. Sending side (Night Shift session's job): `curl -fsS -m 10 --retry 3 https://hc-ping.com/<uuid>` on a fixed schedule, not only after real work. Alert channel: Healthchecks.io's own email to martin@741.studio (matches C16, no new channel type). Severity SEV2 (internal infra, no live client lead-path affected). Escalation: Martin only — answering the Night Shift session's open question, no Dinakar backup for server-infra issues, that would be noise since he doesn't manage the server.
- Row added to canaries.json: `741-server-heartbeat`, status planned, BLOCKED on Martin creating the Healthchecks.io account (I may not create accounts).
