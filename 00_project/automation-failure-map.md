# Automation failure map (final v1, 2026-10-11)

Purpose: list the ways an agent fails on automation work at 741, with the real case from memory and the safety layer that catches it.

Grilling result (Martin, 2026-10-11): all four clusters hurt equally, so all four are top priority: **fake done** (F1–F3), **live damage** (F4–F6, F8), **silent breakage** (F7, F10, F11), **wrong facts** (F9, F12, F13). No failure was added. Workflow: `00_project/automation-workflow.md`.

Layers (starting hypothesis): L0 spec · L1 environment and live switch · L2 action classes and approval · L3 snapshot and rollback · L4 click and API readback · L5 test gate · L6 go-live, monitoring, handover.

| # | Failure | Real 741 case (memory file, date) | Layer that catches it |
|---|---|---|---|
| F1 | Claims "done" without an end-to-end run | Marcel Zap v1 published "live" with 2 critical bugs (KlickTipp 406, Pipedrive 400): no contact, no tag, no mails (marcel-rosenbach-client, 2026-09-03). Newsletter test and send broke silently with HTTP 503: `NEWSLETTER_ADMIN_SECRET` was never set (newsletter-backend, 2026-08-30). Night shift was "armed", first real run crashed on Node 26 and OAuth 401 (night-shift-agent, 2026-09-15) | L5 test gate + Stop hook |
| F2 | Trusts a click without reading the state back | 8 of 9 KlickTipp mails "built", subject and body never saved (marcel-rosenbach-client, 2026-09-03). Menu checked with curl, live menu invisible (verify-ui-in-rendered-state, 2026-10-07). ONLY INSIDE "Save" sent empty content, module stayed empty (only-inside-cms-build). Sheets popup swallowed all typing, tool said "Typed" (local-seo-sheet-workflow) | L4 readback after every UI step |
| F3 | Trusts an API "200 OK" | Shopify REST SEO metafields: HTTP 200, nothing saved (shopify-admin-api-rabenmuetter, 2026-09-06) | L4 read the record back after every write |
| F4 | Writes to live without a clear go | 3 live changes on Suriya from "do it on the website as well" (no-website-changes-without-go, 2026-09-02). Email to Franziska sent without explicit go (email-sending-rules, 2026-09-29) | L2 action classes + PreToolUse hook |
| F5 | Wrong account or environment | "Test mail to me" from Hüwel's client login goes to Hüwel's real inbox (huewel-newsletter-build). Recruiting email via Gmail, not Airmailer (email-sending-airmailer). Built-in browser without logins (always-external-chrome-browser, 2026-10-11). BCC on old Gmail after a context summary (email-sending-rules) | L1 environment preflight: account, from-address, project ID |
| F6 | Side effect destroys data | `git add -A` from `/tmp` deleted all Hüwel images (huewel-site-workflow, 2026-10-07). Revision postmeta write reset live Suriya page (wp-revision-postmeta-trap, 2026-10-07). Page swap dropped 5 contact forms, enquiries stopped (suriya-conversion-paths-must-stay, 2026-09-24) | L3 snapshot + diff before and after |
| F7 | Silent failure, no alert | 741-leads DB auto-paused, insert failed, leads lost with no mail (leadgen-funnel-infra, 2026-08-05). Meta tab shows 0 leads because no CAPI, reads like "no leads" (meta-ads-live-tab) | L6 heartbeat + alert; "unreadable" is never "zero" |
| F8 | Test data or test settings leak into live, or tests are skipped to avoid junk data | All early Zap tests skipped "no junk data in Marcel's accounts" (marcel-rosenbach-client, 2026-09-01). Test leads fire real notify mails (leadgen-funnel-infra). Skool prices set to $1/$2/$3 for tests, must go back to $59/$99/$199 (marcel-rosenbach-client). Demo users left in team area (team-outreach-area) | L1 TEST markers + L6 cleanup checklist |
| F9 | Wrong conclusion from a partial view | Pipedrive pipeline "missing", it existed (client-questions-verify-first, 2026-09-01). Pixel regex said "no tracking" (leadgen-funnel-infra). "GA4 not installed", it was (franziska-rabenmuetter-client, 2026-10-10) | L0 full inventory; every negative claim needs a second check |
| F10 | Stops halfway, partial state is lost | Marcel Zap draft with a placeholder tag and a title without a space; test prices to reset (marcel-rosenbach-client). Open steps spread over memory files | L3 change log + run state file (`_run.json`) |
| F11 | Unattended infra breaks | DataForSEO IP whitelist changes break crons (citations-listings-module, franziska). GitHub disables schedules after 60 days (leadgen-funnel-infra). `crontab` hangs in sandbox (daily-client-standup) | L6 preflight + canary + heartbeat |
| F12 | Access rules are wrong | `daily_standup()` v1 let any client read all clients (daily-client-standup, fixed). Contract block German for English clients (team-outreach-area) | L5 role-based tests (admin, client, anon) |
| F13 | Credentials in clear text | Smartlead API key written in a memory file (smartlead-cold-email). Portal password sent in chat (franziska-rabenmuetter-client) | Credentials policy + secret-scan hook |
| F14 | Duplicates on retry | No real incident in memory. Good patterns exist: unique `conversation_id` (ai-phone-agent), atomic event count (newsletter-backend), dedup by email (Marcel spec) | L5 idempotency test (run twice, same result) |
| F15 | No rollback plan, no handover | Suriya rollback on 2026-09-02 was manual, same day. Marcel's Zaps are kept by the client's tech person, no runbook in memory | L3 rollback plan + L6 runbook |

Good patterns already in use (keep them): `live_send_enabled=false` until go (huewel-newsletter-build) · staging first, live only after go (portal-single-file-workflow) · Zap stays draft, test with "Test trigger" (marcel-rosenbach-client) · Martin enters tokens, agent never touches the value (meta-ads-live-tab) · `guard_upload.py` PreToolUse hook that asks (cro-workflow-tooling) · night shift never publishes, never mails (night-shift-agent).

## Replay proof

The real Skool funnel build (2026-09-01 to 09-04) was replayed through the guard code: `00_project/assets/marcel/automation/skool-funnel/replay.md`. The replay found one guard gap (raw DELETE through MCP), fixed the same day.
