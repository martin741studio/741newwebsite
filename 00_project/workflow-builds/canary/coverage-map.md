# 1.4 Coverage map — what 741 already has for canaries (2026-10-14)

Read-only inventory by an Explore agent (repo, skills, LaunchAgents, crontab, memory, Supabase read-only). No secret values here, only paths and variable names.

## A. Existing checks
| What | Where | State | Reuse |
|---|---|---|---|
| Supabase keep-alive (GitHub Action, daily) | `.github/workflows/supabase-keepalive.yml` | live; fails only on host unreachable | cloud-cron pattern without laptop. Risk: GitHub disables schedules after 60 days without repo activity (failure map F11) |
| Tracking spec M25 site uptime / M26 form present, rules R1/R2 | `00_project/tracking-workflow.md` §4, §7, §12; `tracking-metric-catalog.json` | designed, NOT built | closest design for website + form canaries; planned runner Supabase pg_cron + edge functions (D17); alert table `tracking_alerts` |
| Supabase pg_cron | 741-portal `cron.job` | only `meta-campaigns-sync` (every 3 h, succeeding). Memory says `portal-weekly-monday` + `portal-admin-digest` exist — they do NOT | canary can read `cron.job_run_details` |
| Night Shift pulse | `reporting/night-shift/pulse.log` | live | heartbeat pattern |
| Daily standup | LaunchAgent `studio.741.standup` 08:05 weekdays | live, gaps when laptop sleeps | yellow-alert delivery point |
| Listings poller | LaunchAgent `studio.741.listings-poller` every 10 min | live | a canary can watch its log for staleness |
| Post-deploy curl rule | memory ftp-deploy-stray-public-html.md | manual | same URL list as a canary |
| Security checklist §9 | `website-security-checklist.md` | "Must: uptime monitoring on the production domain" — not done for any site | requirement source |

Not found anywhere: UptimeRobot, Better Stack, Healthchecks.io, Uptime Kuma, Pushover, ntfy config. **There is no uptime monitoring today.**

## B. Alert channels
| Channel | State |
|---|---|
| Telegram bot @Socials741_bot | sending works: `scripts/telegram-send.py`, `.secrets/telegram-741.env` (TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID). File mode 644 (flagged in laptop check S4). |
| Resend alerts@741.studio → martin@741.studio | decided in automation-build §7, Night Shift N16, tracking D10. Send-only key NOT created yet (Martin step, runbook 1.6). |
| Supabase notify-* edge functions | live, mail Martin per lead → "no lead mail for N days" is a cheap heartbeat signal |
| Claude app push (Remote Control) | only while Remote Control is active |
| WhatsApp API / SMS / Twilio / Pushover / ntfy / Slack | none set up |
| Quiet hours | Night Shift N8: no alarm after 22:00. Canary needs its own rule for the 1-hour target. |

## C. Night Shift v2, Morning Grill, Command Center
- Night Shift v2 runs Mon–Fri 17:30/20:30, stops 22:45, only with a queue file; agents may not use curl; laptop sleeps from 23:02 (`studio.741.night-shift-sleep`). **Not a host for live checks.** Usable for deep read-only follow-ups (class public_audit).
- Morning Grill: `scan.py` source **S8_tracking is an empty placeholder** ("tracking workflow not built yet") → natural slot for canary state. Card format `decision-card.template.json`; ledger `state/cards.json`; Command Center live tab on clients.741.studio (`cc-block.js`). Grill = daily digest, not the 1-hour path.

## D. Automation Build (designed 2026-10-11, NOT installed)
`00_project/automation-workflow.md`: L5 test gate, L6 go-live = "canary, alerts, daily reconciliation, runbook"; §7: "Canary: first real record end-to-end with readback, check again after 24 h"; "platform error alerts go to martin@741.studio (Zapier error notifications, n8n error workflow)"; "Daily reconciliation: count source events vs target records… Mismatch = alert… A failed read = alert 'unreadable'"; "Owner after go-live: 741 monitors as part of the retainer". Reconciliation runner never built. Templates: `templates/golive-checklist.md` (alert path + reconciliation + canary lines), `runbook-de.md`, `rollback-plan.md`. Failure map F7 (silent failure, no alert) and F11 (unattended infra breaks) = canary test cases.
→ **The canary workflow is the missing "L6 monitor" half of Automation Build.** Reuse its rules and templates; do not re-specify them.

## E. Registry
`workflow_registry.py add-workflow --workflow canary --name "…"`. **Gotcha:** `sync` scans only `00_project/assets/**` and `00_project/prospects/**` → canary run markers go to `00_project/assets/<client-slug>/canary/<run>/_run.json` (or `00_project/assets/741studio/canary/`).

## F. Google Ads read access
No Ads API (no developer token, no OAuth), no Ads MCP. Reads only via Chrome UI (741studio18@gmail.com, "confirm it's you" walls) or GA4 cost data where linked (Kamil). Live accounts: Bali Healing 239-394-2913 (prepaid, balance ≈ 5 days on 13.10.), Kamil 992-981-4693, Suriya 499-126-8644 (paused), 741 own 534-995-9699. Stürzl planned. Meta: read token + pg_cron sync exist.
→ Ads canary needs a read path: Google Ads script inside each account (runs at Google, mails/webhooks out) or Ads API with developer token. Decide at design.

## G. Client systems worth a canary (first pass)
741 Studio (741.studio, LPs, 741-leads inserts + notify-* functions, GitHub Actions, LaunchAgents) · Portal clients.741.studio (10 edge functions incl. Hüwel `site-form`) · Suriya (WP, /termin-buchen/ CF7 + Fluent Forms; Novamira connection failing) · Hüwel (GitHub Pages, forms via `site-form`) · Stürzl (Joomla, contact form; Ads planned) · Dumann (Wix) · Brasse (WP, Novamira) · Bali Healing (Wix, WhatsApp only, Ads live with prepaid balance) · Rabenmütter (Shopify, Admin API) · Johni Jaya Motor (WP, Novamira) · Kamil (2 WP sites, Ads live, casino-spam on Kraft) · **Marcel (Skool funnel Zap 378535838, Gewinnspiel Zap 382522671, Tally, KlickTipp, Pipedrive)** · me&you (2 LPs to go live) · Talkinfive (go.talkinfive.com, GitHub deploy) · Taxi Nürnberg (Joomla, preisrechner 403 risk via Admin Tools; Cloudflare blocks curl on HTML).

## H. Schedulers that exist
Desktop tasks: morning-grill-0600 (06:13), morning-grill-1700. LaunchAgents: standup, listings-poller, night-shift-v2, night-shift-sleep. GitHub Actions: keepalive, monthly reports. pg_cron: meta-campaigns-sync. No cloud routines.

## I. Secret hygiene (names only, outside this build — follow-up)
World-readable `.secrets/telegram-741.env`, `meta-741.env`, `apify.env`; Smartlead key in 2 scheduled-task SKILL.md files; portal logins in 2 memory files; Taxi FTP password in a script. A canary must not copy this pattern: credentials only in a vault / 600 files, read-only scopes.

## Reuse decision
- Reuse: Automation Build L6 rules + templates, tracking M25/M26 spec, Morning Grill S8 slot + card format + Command Center, Telegram sender, Resend alerts@ plan, registry, Night Shift for deep follow-ups.
- Build new: an always-on check runner (off-laptop), an external watcher, a phone-push channel that breaks Do-Not-Disturb, the canary registry, the incident skill.
