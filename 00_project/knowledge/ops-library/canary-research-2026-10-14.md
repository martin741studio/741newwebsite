# Canary workflow: research base (2026-10-14)

## Purpose

This file is the research base for the 741 workflow "canary". Agent-run checks find outages of client systems fast. A canary tries one safe self-heal. If the self-heal fails, the canary alerts a human. The goal: no outage lasts longer than 1 hour.

- Fetch date: 2026-10-14.
- Freshness rule: blog posts, articles and videos must be from 2026-07-14 or later. Official vendor docs are living pages. They count as current on the fetch date.
- "date unclear" means the page shows no reliable publish date. These sources have less weight. No rule depends only on them.
- Reused from this library: O1 and O2 (Claude Code routines and scheduling), N02 (phone push with ntfy), N05 (safe unattended runs). See `INDEX.md` and `night-shift-server-INDEX.md`.

## 1. Source table

### Topic 1: Synthetic, uptime and heartbeat monitoring

| # | Title | URL | Date | Takeaway |
|---|---|---|---|---|
| 1 | Healthchecks.io pricing | https://healthchecks.io/pricing/ | living doc, fetched 2026-10-14 | Free (Hobbyist) = 20 jobs. Business $20/mo = 100 jobs, 50 SMS/WhatsApp, 20 calls. |
| 2 | Healthchecks.io docs: configuring checks | https://healthchecks.io/docs/configuring_checks/ | living doc, fetched 2026-10-14 | Period + grace time, cron mode with time zone. A start signal makes grace a run-time cap. `/fail` and exit code give an immediate failure. |
| 3 | UptimeRobot pricing | https://uptimerobot.com/pricing/ | living doc, fetched 2026-10-14 | Free = 50 monitors at 5 min. Solo $10/mo at 60 s. Team $41/mo at 30 s. Heartbeat only on paid plans. |
| 4 | UptimeRobot terms + fair use | https://uptimerobot.com/terms/ , https://uptimerobot.com/terms-fair-use/ | living doc, fetched 2026-10-14 (changelog 2026-05-26) | Commercial use is allowed on all plans. Multi-account limit bypass is banned. |
| 5 | Better Stack pricing | https://betterstack.com/pricing | living doc, fetched 2026-10-14 | Free = 10 monitors and heartbeats, Slack + email only. Responder $34/mo ($29 yearly). |
| 6 | Better Stack: check frequency | https://betterstack.com/docs/uptime/check-frequency.md | living doc, fetched 2026-10-14 | 3 min on free, 30 s on paid. |
| 7 | Better Stack: confirmation and recovery period | https://betterstack.com/docs/uptime/confirmation-and-recovery-period/ | living doc, fetched 2026-10-14 | Confirmation period delays the incident. Recovery period keeps it open. One failed check resets the recovery countdown. |
| 8 | Cronitor pricing | https://cronitor.io/pricing | living doc, fetched 2026-10-14 | Free = 5 monitors at 5 min. Business = $2/monitor + $5/user per month, 30 s. |
| 9 | Cronitor: heartbeat and alerts docs | https://cronitor.io/docs/heartbeat-monitoring , https://cronitor.io/docs/alerts | living doc, fetched 2026-10-14 | `grace_seconds`, `failure_tolerance` (consecutive misses), `consecutive_alert_threshold` (surge protection). |
| 10 | Checkly pricing | https://www.checklyhq.com/pricing/ | living doc, fetched 2026-10-14 | Free = 10 monitors at 2 min, no SMS or phone. Starter $24/mo at 1 min. |
| 11 | Checkly: alerting and retries, heartbeats | https://www.checklyhq.com/docs/alerting-and-retries/ , https://www.checklyhq.com/docs/heartbeat-monitors/ | living doc, fetched 2026-10-14 | Fixed, linear or exponential retries. Alert after N failures or after X minutes. Reminders. Heartbeat grace period. |
| 12 | Uptime Kuma (GitHub) | https://github.com/louislam/uptime-kuma | living doc, fetched 2026-10-14 (release 2.5.6, 2026-10-09) | Self-hosted, free. 20-second intervals. Push (heartbeat) monitor. 110 notification providers. |
| 13 | Crontap: Dead man's switch, explained for developers | https://crontap.com/blog/dead-man-switch-explained-for-developers | 2026-09-04 | Grace 5–10 min for hourly jobs, 30–60 min for daily jobs. Alert at period + grace. Vendor blog. |
| 14 | Crontap: Introducing Crontap Heartbeats | https://crontap.com/blog/introducing-crontap-heartbeats | 2026-09-05 | A job that never starts gives no error. Only a missed ping catches it. Vendor blog. |
| 15 | n8n community: how do you find out when client workflows break? | https://community.n8n.io/t/those-of-you-managing-n8n-workflows-for-clients-how-do-you-find-out-when-something-breaks/304198 | 2026-07-21 | Agencies combine an Error Trigger with a heartbeat or stale-timestamp check. Tag failures as credential, API or logic. |
| 16 | Watchman Tower: uptime alerts and escalation | https://www.watchmantower.com/blog/uptime-monitoring-alerts-and-escalation | date unclear ("Updated: October 1, 2026") | 2 consecutive failures for small sites. SMS only for revenue-critical incidents. Down-weighted. |
| 17 | Hyperping: on-call scheduling for small teams | https://hyperping.com/blog/oncall-scheduling-small-teams | date unclear ("Last updated September 12, 2026") | Escalate to one backup after 10–15 min without acknowledgement. Down-weighted. |
| 18 | OnlineOrNot: best uptime monitoring tools 2026 | https://onlineornot.com/uptime-monitoring-tools | date unclear ("Last updated: September 15, 2026") | Route by severity. Use multi-region confirmation. Vendor page. Down-weighted. |

### Topic 2: Zapier, Make and n8n error and switch-off alerts

| # | Title | URL | Date | Takeaway |
|---|---|---|---|---|
| 19 | Zapier: manage notifications when errors occur | https://help.zapier.com/hc/en-us/articles/8496289225229 | living doc, fetched 2026-10-14 | Error emails go to the account email, default "Immediately". No error email when an error handler runs. |
| 20 | Zapier Manager integrations | https://zapier.com/apps/zapier-manager/integrations | living doc, fetched 2026-10-14 | 11 triggers, including "New Zap Error" and "Zap Turned Off". No "New Halted Task" trigger now. |
| 21 | Zapier: troubleshoot Zapier Manager | https://help.zapier.com/hc/en-us/articles/8496200014477 | living doc, fetched 2026-10-14 | Error triggers fire only after all Autoreplay attempts. They do not fire if error alerts are "Never". |
| 22 | Zapier: more time to fix Zaps that error | https://help.zapier.com/hc/en-us/articles/19532291509901 | living doc, fetched 2026-10-14 | Warning at 95% error rate with more than 20 runs in 7 days. Team 24 h, Company 72 h before turn-off. |
| 23 | Zapier: advanced error settings | https://help.zapier.com/hc/en-us/articles/14167175792909 | living doc, fetched 2026-10-14 | Default turn-off at 95% or more errors over 7 days. Company plan can "Keep running if errors occur". |
| 24 | Zapier: replay Zap runs | https://help.zapier.com/hc/en-us/articles/8496241726989 | living doc, fetched 2026-10-14 | Autoreplay on Professional, Team, Enterprise. Account toggle + per-Zap override. No retry count on the page. |
| 25 | Zapier: custom error handling | https://help.zapier.com/hc/en-us/articles/22495436062605 | living doc, fetched 2026-10-14 | Success path + Error path. Run shows "Stopped/Handled". Zapier Manager triggers still fire. |
| 26 | Zapier: Zap history | https://help.zapier.com/hc/en-us/articles/8496291148685 | living doc, fetched 2026-10-14 | Run data kept 60 days at most. |
| 27 | Zapier Workflow API: Get Zap Runs (experimental) | https://docs.zapier.com/api-reference/workflow/experimental/get-zap-runs | living doc, fetched 2026-10-14 | `GET https://api.zapier.com/v2/zap-runs`, OAuth scope `zap:runs`, filter by status. |
| 28 | Make: overview of error handling | https://help.make.com/Overview-of-error-handling | living doc, fetched 2026-10-14 | Default 3 consecutive errors before deactivation. Instant trigger: first error. Default handler: Rollback. |
| 29 | Make: scenario settings | https://help.make.com/scenario-settings | living doc, fetched 2026-10-14 | Setting "Errors before deactivation". Instant triggers ignore it. |
| 30 | Make: errors and warnings | https://help.make.com/Introduction-to-errors-and-warnings.md | living doc, fetched 2026-10-14 | Unhandled error = email. Deactivation = email. Warnings do not count. |
| 31 | Make: email preferences | https://help.make.com/manage-your-email-preferences.md | living doc, fetched 2026-10-14 | Profile > Email preferences > Organizations: Deactivation, Warning, Errors. Error digest after 5 min. |
| 32 | Make: error handlers | https://help.make.com/error-handlers.md , https://help.make.com/retry-error-handler.md | living doc, fetched 2026-10-14 | Current handlers: Skip, Retry, Resume, Commit, Rollback. |
| 33 | Make API: scenarios and logs | https://developers.make.com/api-documentation/api-reference/scenarios | living doc, fetched 2026-10-14 | `GET /scenarios` gives `isActive`, `isinvalid`, `isPaused`, `dlqCount`. Logs `?status=3` = errors. No deactivation webhook found. |
| 34 | n8n: handle errors, Error Trigger | https://docs.n8n.io/build/flow-logic/handle-errors-gracefully.md , https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger/ | living doc, fetched 2026-10-14 | Options > Settings > Error workflow. Runs only on automatic executions. No test with a manual run. |
| 35 | n8n API: executions and workflows | https://docs.n8n.io/connect/n8n-api/executions.md , https://docs.n8n.io/connect/n8n-api/workflow.md | living doc, fetched 2026-10-14 | `GET /api/v1/executions?status=error`. `activeVersionId` is null when a workflow is not active. |
| 36 | LowCode Agency: Zapier monitoring tips | https://www.lowcode.agency/blog/zapier-monitoring | 2026-09-24 | Watch trigger volume drops, not only errors. Note: its claim "no failure alerts by default" is wrong per Src 19. |
| 37 | workflowtestlab: Make scenario deactivated after an error | https://workflowtestlab.com/make-scenario-deactivated-after-error/ | date unclear (test dated 2026-08-21) | One unhandled error switched off a webhook scenario. Down-weighted. |

### Topic 3: Google Ads read-only monitoring

| # | Title | URL | Date | Takeaway |
|---|---|---|---|---|
| 38 | Google Ads scripts: limits | https://developers.google.com/google-ads/scripts/docs/limits | living doc, fetched 2026-10-14 | 30 min per run. MCC `executeInParallel`: 60 min, max 50 accounts. 250 scripts. |
| 39 | Google Ads scripts: manager scripts | https://developers.google.com/google-ads/scripts/docs/concepts/manager-scripts | living doc, fetched 2026-10-14 | Max 50 client accounts per `executeInParallel`. Closed and suspended accounts excluded by default. |
| 40 | Google Ads scripts: best practices | https://developers.google.com/google-ads/scripts/docs/best-practices | living doc, fetched 2026-10-14 | Use reports for bulk stats, not iterators. |
| 41 | Google Ads scripts: preview mode | https://developers.google.com/google-ads/scripts/docs/concepts/preview | living doc, fetched 2026-10-14 | Preview blocks only AdsApp changes. MailApp and sheet writes still run. |
| 42 | AdsApp and ExecutionInfo reference | https://developers.google.com/google-ads/scripts/docs/reference/adsapp/adsapp | living doc, fetched 2026-10-14 | Read: `search()`, `report()`. Write: `mutate()`, `mutateAll()`. `isPreview()` exists. |
| 43 | Google Ads scripts: solutions list | https://developers.google.com/google-ads/scripts/docs/solutions | living doc, fetched 2026-10-14 | 6 scripts. No disapproved-ads script, no MCC anomaly detector. |
| 44 | Account Anomaly Detector | https://developers.google.com/google-ads/scripts/docs/solutions/account-anomaly-detector | living doc, fetched 2026-10-14 | Compares with same-weekday average. Skips the last ~3 h. Max 1 email per alert type per day. Hourly. Read-only code. |
| 45 | Link Checker | https://developers.google.com/google-ads/scripts/docs/solutions/link-checker | living doc, fetched 2026-10-14 | NOT read-only. It writes and removes the label `LinkChecker_Done`. |
| 46 | Google Ads Help: automate tasks with scripts | https://support.google.com/google-ads/answer/188712 | living doc, fetched 2026-10-14 | Schedule options and 30 min timeout. |
| 47 | Google Ads API field reference v25 | https://developers.google.com/google-ads/api/fields/v25/campaign (and `ad_group_ad`, `customer`, `billing_setup`, `account_budget`, `conversion_action`, `metrics`) | living doc, fetched 2026-10-14 | Exact status enums. See section 3.3. |
| 48 | Google Ads API release notes | https://developers.google.com/google-ads/api/docs/release-notes | living doc, fetched 2026-10-14 | Latest v25.2 (2026-09-23). v26 announced. |
| 49 | Google Ads API access levels | https://developers.google.com/google-ads/api/docs/api-policy/access-levels | living doc, last updated 2026-09-30 | Test, Explorer (2,880 ops/day), Basic (15,000/day, brand verification), Standard. |
| 50 | Apps Script quotas | https://developers.google.com/apps-script/guides/services/quotas | living doc, fetched 2026-10-14 | MailApp 100 recipients/day (consumer), 1,500/day (Workspace). |
| 51 | Google Ads Help: email notifications | https://support.google.com/google-ads/answer/1704338 | living doc, fetched 2026-10-14 | "Disapproved ads and policy alerts" and "Campaign maintenance": all or critical. Billing alerts in Billing > Settings. |
| 52 | Google Ads Help: change email preferences | https://support.google.com/google-ads/answer/7541103 | living doc, fetched 2026-10-14 | Admin > Notifications > Email settings. |
| 53 | Google Ads Help: manager account notifications | https://support.google.com/google-ads/answer/7519926 | living doc, fetched 2026-10-14 | MCC > Admin > Notifications > Full hierarchy, per client or in bulk. |
| 54 | Google Ads Help: in-account notifications | https://support.google.com/google-ads/answer/7543712 | living doc, fetched 2026-10-14 | Bell icon. Red triangle = critical (ads not running, billing). |
| 55 | Digital Applied: Google Ads scripts + AI agents for account QA | https://www.digitalapplied.com/blog/google-ads-scripts-ai-agent-account-qa-2026 | 2026-07-16 | Start read-only (sheet + email). Send disapprovals at once, not weekly. |

### Topic 4: Alert channels to a phone in Indonesia

| # | Title | URL | Date | Takeaway |
|---|---|---|---|---|
| 56 | Pushover API | https://pushover.net/api | living doc, fetched 2026-10-14 | Priority 2 repeats until acknowledged. Retry ≥ 30 s, expire ≤ 10,800 s. Priority 1 bypasses quiet hours. 10,000 msgs/month. |
| 57 | Pushover pricing | https://pushover.net/pricing | living doc, fetched 2026-10-14 | $4.99 one-time per platform. Teams $5/user/month. |
| 58 | Pushover: override DND on Android | https://support.pushover.net/i258-overriding-do-not-disturb-on-android | living doc, date unclear | Add Pushover to the Android DND exceptions. |
| 59 | ntfy publish docs | https://docs.ntfy.sh/publish/ | living doc, fetched 2026-10-14 | Priority 5 = long vibration + pop-over on Android. Free: 250 msgs/day. Phone calls Pro only, English only. |
| 60 | ntfy pricing | https://ntfy.sh/#pricing | living doc, fetched 2026-10-14 | Supporter $5/mo, Pro $10/mo (20 calls), Business $20/mo. |
| 61 | ntfy phone docs (GitHub) | https://github.com/binwiederhier/ntfy/blob/0c617d1dca3daafad5f20e96c63323fbeaa14463/docs/subscribe/phone.md | living doc, fetched 2026-10-14 | Android: one channel per priority. Each channel can override DND. |
| 62 | ntfy known issues | https://docs.ntfy.sh/known-issues/ | living doc, fetched 2026-10-14 | iOS subscriptions can stop. Self-hosted needs `upstream-base-url`. |
| 63 | ntfy issue #1235: iOS critical alerts | https://github.com/binwiederhier/ntfy/issues/1235 | open issue, last comment 2026-10-10 | ntfy iOS has no Critical Alerts. |
| 64 | Telegram Bot FAQ | https://core.telegram.org/bots/faq | living doc, fetched 2026-10-14 | Free. About 1 msg/s per chat, 20 msgs/min per group. |
| 65 | Meta WhatsApp Cloud API pricing | https://developers.facebook.com/docs/whatsapp/pricing | living doc, fetched 2026-10-14 | Per-message pricing. Outside the 24 h window you need a paid template. Indonesia rate not retrieved. |
| 66 | Twilio WhatsApp pricing | https://www.twilio.com/en-us/whatsapp/pricing | living doc, fetched 2026-10-14 | Meta fee + $0.005 per message. |
| 67 | Twilio SMS pricing Indonesia | https://www.twilio.com/en-us/sms/pricing/id | living doc, fetched 2026-10-14 | $0.4414 per outbound segment. |
| 68 | Twilio SMS guidelines Indonesia | https://www.twilio.com/en-us/guidelines/id/sms | living doc, fetched 2026-10-14 | Registered alphanumeric sender ID needed (3–4 weeks). Lapses below 1,000 SMS per network per quarter. |
| 69 | Twilio Voice pricing Indonesia | https://www.twilio.com/en-us/voice/pricing/id | living doc, fetched 2026-10-14 | Outbound call to mobile $0.1066/min. Local number $23/mo. |
| 70 | Apple: allow or silence notifications for a Focus | https://support.apple.com/guide/iphone/allow-or-silence-notifications-for-a-focus-iph21d43af5b/ios | living doc, fetched 2026-10-14 | "Repeated calls" = 2+ calls from the same caller within 3 min. Emergency Bypass per contact. |
| 71 | Apple HIG: managing notifications | https://developer.apple.com/design/human-interface-guidelines/managing-notifications | living doc, fetched 2026-10-14 | Time Sensitive passes Focus, not the silent switch. Critical passes both. |
| 72 | Futurion (Omar Fenton): ntfy vs Pushover vs Gotify | https://futurion.blog/ntfy-vs-pushover-vs-gotify-which-homelab-alert-path-still-wakes-you/ | 2026-08-25 | Pushover emergency priority woke the author. Default ntfy is easy to miss in Focus. Test at night. |
| 73 | Pingwire: Slack vs Telegram vs ntfy vs Pushover | https://pingwire.dev/blog/slack-vs-telegram-vs-ntfy-vs-pushover-developer-alerts | 2026-08-15 | Telegram and ntfy have no acknowledgement and no escalation. Vendor blog. |
| 74 | Woopy: ntfy alternatives | https://woopy.dev/blog/ntfy-alternative/ | 2026-09-29 | Self-hosted ntfy without upstream can deliver hours late. Telegram has no priority levels. Vendor blog. |

### Topic 5: Agent-run checks and self-healing

| # | Title | URL | Date | Takeaway |
|---|---|---|---|---|
| 75 | Claude Code: Automate work with routines | https://code.claude.com/docs/en/routines.md | living doc, fetched 2026-10-14 | Minimum schedule interval 1 hour. API trigger `/fire` for alerting systems. No approvals during a run. Green status ≠ task success. |
| 76 | Claude Code: Run prompts on a schedule (/loop) | https://code.claude.com/docs/en/scheduled-tasks.md | living doc, fetched 2026-10-14 | Cloud 1 h, Desktop 1 min, /loop 1 min. Desktop and /loop need the machine on. /loop expires after 7 days. Jitter up to 30 min for hourly tasks. |
| 77 | Claude Code: Desktop scheduled tasks (library O2) | https://code.claude.com/docs/en/desktop-scheduled-tasks | living doc, fetched 2026-10-11 (repo copy) | Skipped while the Mac sleeps. One catch-up run on wake. |
| 78 | Mudassir Khan: AI agent incident response, a production runbook | https://mudassirkhan.me/blog/ai-agent-incident-response | 2026-08-27 (metadata; modified date 2026-08-18 is earlier, so slightly down-weighted) | Contain first. Narrowest control. Retry only safe, idempotent actions. Keep a way to disengage the agent. |
| 79 | HackerNoon (InduP): How I'd build a self-healing AI agent | https://hackernoon.com/how-id-build-a-self-healing-ai-agent-for-zero-touch-bug-remediation | 2026-10-04 | Deterministic rules start remediation, not the LLM. Allowlisted tools only. Verify system state, not a 200 OK. Escalate on mismatch. |
| 80 | Splunk (Pratik Bhavsar): output guardrails for agent incidents | https://www.splunk.com/en_us/blog/observability/output-guardrails-incident-response.html | 2026-09-04 | Act by severity × confidence: block, review, or log. Track false-positive rate. |
| 81 | Melta: Claude Code notifications on your phone (library N02) | https://getmelta.app/blog/claude-code-notifications-on-phone/ | 2026-10-02 | Hook → ntfy push. Use a long random topic. A push needs a one-tap way back in. |
| 82 | Matrix OS: run Claude Code overnight safely (library N05) | https://matrix-os.com/blog/run-claude-code-overnight-safely | 2026-08-14 | Explicit stop conditions. Remove credentials the agent does not need. End with a report. |

## 2. Rules per topic

### 2.1 Monitoring, heartbeats, alert fatigue

1. IF one HTTP check fails, THEN do not alert yet. Alert after 2–3 consecutive failures or a confirmation period. (Src: 7, 11)
2. IF a page alert (Pushover emergency or call) can fire, THEN require 2+ probe locations to agree first. Single-location failures go to the team feed only. (Src: 18, 16 — both date unclear; standard feature in 7, 11)
3. IF an incident flaps, THEN set a recovery period. One good check must not close it. (Src: 7)
4. IF a cron job, automation or canary runs on a schedule, THEN give it a heartbeat. Alert at period + grace. Grace: 5–10 min for hourly jobs, 30–60 min for daily jobs. (Src: 2, 13)
5. IF the job knows it failed, THEN ping `/fail` or send the exit code at once. Do not wait for the grace time. (Src: 2, 13)
6. IF a job can hang, THEN send a start signal. Grace time then caps the run time. (Src: 2)
7. IF a trigger can stop without an error (no new leads, no new runs), THEN add an "absence of signal" check: heartbeat, run count or stale timestamp. Error alerts do not catch silence. (Src: 14, 15, 36)
8. IF a heartbeat misses once without harm, THEN set a consecutive-miss tolerance and surge protection. (Src: 9)
9. IF the primary person does not acknowledge in 10–15 min, THEN escalate to one named backup. IF more than 20% of night pages need no action, THEN fix the thresholds. (Src: 17 — date unclear)

### 2.2 Zapier, Make, n8n

1. IF a Zap is business-critical, THEN build one Zapier Manager Zap on "New Zap Error" and "Zap Turned Off". Send it to a 741 webhook. Keep the error email on "Immediately". (Src: 19, 20)
2. IF Autoreplay is on, THEN expect late alerts. Zapier Manager error triggers fire only after the last replay. (Src: 21)
3. IF a Zap has an Error path, THEN put an alert step in that path. Zapier sends no error email when a handler runs. (Src: 25)
4. IF a Zap errors at 95% or more with more than 20 runs in 7 days, THEN Zapier warns and later turns it off (24 h Team, 72 h Company). The canary must check "on" status every day. (Src: 22, 23)
5. IF the Zapier Manager Zap and the failing Zap have different owners (Team plan), THEN the alert does not reach you. Give both the same owner. (Src: 21)
6. IF a read-only Zapier checker is needed, THEN poll `GET https://api.zapier.com/v2/zap-runs` for `error` and `halted`. The endpoint is experimental. (Src: 27)
7. IF a Make scenario starts with a webhook (instant trigger), THEN add error handlers to each module that can fail. The first unhandled error switches it off. (Src: 28, 29)
8. IF you must detect a switched-off Make scenario, THEN poll `GET /scenarios` and compare `isActive` with the expected list. Make has no deactivation webhook. Also turn on the "Deactivation" email per organization. (Src: 31, 33)
9. IF a client uses n8n, THEN link one shared Error Trigger workflow in Options > Settings > Error workflow. Also poll `GET /api/v1/executions?status=error` and check `activeVersionId`. (Src: 34, 35)

### 2.3 Google Ads (read-only)

1. IF a canary touches Google Ads, THEN it uses only `AdsApp.search()`, `AdsApp.report()` and selectors. No `mutate()`, `mutateAll()`, builders or labels. (Src: 42)
2. IF you reuse the official Link Checker, THEN strip the label logic first. It writes labels to the account. (Src: 45)
3. IF you test a script in preview, THEN guard MailApp and sheet writes with `isPreview()`. Preview blocks only AdsApp changes. (Src: 41)
4. IF you check "today" data, THEN leave out the last ~3 hours. Stats can be up to 3 h late. (Src: 44)
5. IF you need a zero-spend alert, THEN add your own check. The Anomaly Detector alerts on high cost only. Check enabled campaigns with `metrics.impressions = 0` or `metrics.cost_micros = 0`. (Src: 44, 47 — the gap is an inference from the documented alert direction)
6. IF an enabled campaign does not serve, THEN read `campaign.primary_status` and `campaign.primary_status_reasons`. `campaign.status` alone is not enough. (Src: 47)
7. IF an ad is disapproved, THEN alert at once from `ad_group_ad.policy_summary.approval_status = DISAPPROVED`. Do not wait for a weekly report. (Src: 47, 55)
8. IF conversion tracking can break silently, THEN alert when `metrics.conversion_last_received_request_date_time` is stale. (Src: 47)
9. IF billing can fail, THEN read `billing_setup.status` and `account_budget.status`, and keep Google's own billing emails on for a 741 address. Scripts have no native billing-failure alert. (Src: 47, 51)
10. IF clients are linked to the 741 MCC, THEN set "Disapproved ads and policy alerts" and "Campaign maintenance" via MCC > Admin > Notifications > Full hierarchy. One MCC script covers max 50 accounts per `executeInParallel`. (Src: 39, 53)

### 2.4 Alert channels to a phone in Bali

1. IF an alert must wake the owner through Focus or silent mode, THEN use Pushover priority 2 with Critical Alerts on. Test it at night with the sleep Focus on. (Src: 56, 72)
2. IF an alert is urgent but not critical, THEN use Pushover priority 1. It bypasses Pushover quiet hours and does not repeat. (Src: 56)
3. IF you use ntfy on iPhone, THEN expect Time Sensitive behaviour at most. Allow ntfy in each Focus. ntfy has no iOS Critical Alerts. (Src: 63, 71)
4. IF a team member uses Android with ntfy or Pushover, THEN set the app as a DND exception. (Src: 58, 61)
5. IF the last escalation step must work without mobile data, THEN place 2 calls within 3 min from one fixed number. Save it as a contact with Emergency Bypass. (Src: 69, 70)
6. IF you think about SMS to Indonesian numbers, THEN do not use it. It costs $0.4414 per segment and needs a registered sender ID that lapses at low volume. (Src: 67, 68)
7. IF you think about WhatsApp for alerts, THEN plan a paid utility template per alert. Script alerts fall outside the 24 h window. Setup effort is high. (Src: 65, 66)
8. IF the team needs a free, readable alert feed, THEN use a Telegram group. Stay under 20 msgs/min. It has no acknowledgement and no escalation. (Src: 64, 73)
9. IF the notifier runs on the host it watches, THEN move it. A host failure then kills the alert too. (Src: 72)
10. IF a push carries client data, THEN send only "alert: <client-id> <check-id>". Use a private channel or a long random ntfy topic. (Src: 81)

### 2.5 Agent-run checks and self-healing

1. IF detection must be fast (minutes), THEN do not use a cloud routine as the detector. Its minimum interval is 1 hour. Use an external monitor at 1–5 min. (Src: 75, 76)
2. IF the external monitor confirms an outage, THEN let it call the routine's API trigger (`/fire`) with the alert text. The routine prompt must say to act on the fire payload. (Src: 75)
3. IF the check needs local files or the 741 repo, THEN a Desktop task or `/loop` (1 min) works only while the Mac is awake. It is not a reliable 24/7 detector. (Src: 76, 77)
4. IF deterministic rules can decide "outage yes/no", THEN rules start the response, not the LLM. The agent diagnoses and runs allowlisted fixes only. (Src: 79)
5. IF a self-heal is possible, THEN allow only reversible, idempotent, pre-approved actions. Retry at most once with backoff. Never touch Google Ads, billing or client content. (Src: 78, 79, 82)
6. IF a fix was applied, THEN verify the real state (page loads, form posts, Zap is on) with the same external check. A 200 OK from the fix call is not proof. (Src: 79)
7. IF verification fails, the runbook has no match, or confidence is low, THEN escalate to a human at once. (Src: 79, 80)
8. IF a routine run shows green, THEN do not treat it as success. Green means "no infrastructure error" only. Read the result or a written status file. (Src: 75)
9. IF canaries run unattended, THEN remove connectors and credentials they do not need. Routines can use every tool of an included connector, writes included, without approval. (Src: 75, 82)
10. IF the canary itself stops, THEN nobody knows. Each canary run must ping its own heartbeat (dead-man's switch). (Src: 2, 14)

## 3. Comparison tables

### 3.1 Monitor tools

| Tool | Free tier | Min interval free / paid | Heartbeat (cron) | Alert channels | Paid entry |
|---|---|---|---|---|---|
| Healthchecks.io | 20 jobs | Heartbeat only. Period + grace per check | Yes, core product (cron + time zone, start, /fail) | Email, webhook, Telegram, Signal, ntfy, Pushover, Slack, Discord, Teams. SMS, WhatsApp, phone need credits (paid) | $20/mo (100 jobs, 50 SMS/WhatsApp, 20 calls). Supporter $5/mo |
| UptimeRobot | 50 monitors. Commercial use allowed | 5 min / 60 s (Solo), 30 s (Team) | Paid plans only | Email, Telegram, Pushover, Slack, Teams, Discord, webhook. SMS and voice need credits. Free: 5 integrations | Solo $10/mo ($9 yearly) |
| Better Stack Uptime | 10 monitors + heartbeats combined | 3 min / 30 s | Yes | Free: Slack + email. Paid: phone call, SMS, app push, webhook | Responder $34/mo ($29 yearly) |
| Cronitor | 5 monitors, 1 user | 5 min / 30 s | Yes (grace, failure tolerance) | Email, Slack, Discord, Teams, webhook, Telegram. SMS paid | $2/monitor + $5/user per month |
| Checkly | 10 monitors (heartbeats count) | 2 min / 1 min (Starter), 30 s (Team) | Yes (grace period) | Email, Slack, webhook. Paid: SMS (Starter), phone calls (Team). Telegram in docs | Starter $24/mo |
| Uptime Kuma (self-hosted) | Free, open source, no cap | 20 s | Yes (Push monitor) | 110 providers: Telegram, Pushover, ntfy, Signal, webhook, Twilio. WhatsApp via gateways | Server cost only. One location unless you run several |

### 3.2 Alert channels (phone in Bali, WITA)

| Channel | Cost | Setup effort | Breaks DND / Focus | Acknowledge + repeat | Indonesia notes |
|---|---|---|---|---|---|
| Pushover | $4.99 one-time per platform. 10,000 msgs/mo. Teams $5/user/mo | Low (one HTTP POST) | Yes. Priority 2 + iOS Critical Alerts. Android needs DND exception | Yes (priority 2 repeats until acknowledged, max 3 h) | Push over any data link. No issue found |
| ntfy (ntfy.sh) | Free 250/day. $5 / $10 / $20 per month | Very low (one curl) | Android yes (priority-5 channel). iOS: Focus only if allowed. No Critical Alerts | No | Calls on paid plans, English voice, country support not stated |
| Telegram bot | Free | Low (BotFather token) | Focus only if allowed. No critical alerts | No | No issue found |
| WhatsApp (Cloud API / Twilio) | Paid template per alert outside 24 h window. Twilio +$0.005 | High (business account, templates) | Focus only if allowed | No | Official Indonesia rate not retrieved |
| SMS (Twilio) | $0.4414 per segment | High (sender ID 3–4 weeks) | Focus only, sender cannot be a contact | No | Blocked without registration. Poor fit |
| Phone call (Twilio Voice) | $0.1066/min + $23/mo number | Medium | Yes, with Emergency Bypass or 2 calls within 3 min | The call itself | Works without mobile data |

## 4. Recommendation for 741 (draft for Martin's decision)

- **Monitor tool:** UptimeRobot for HTTP checks (free 50 monitors at 5 min; Solo $10/mo for 60 s). Healthchecks.io free for heartbeats (20 jobs): every canary run, cron and critical automation pings it. Both have Telegram, Pushover and webhook.
- **Alert channel:** Pushover for Martin. Priority 1 for "self-heal running", priority 2 (emergency, Critical Alerts on) for "self-heal failed". A Telegram group as the free team feed for Dinakar, Tantri and Gayo. A Twilio call is an optional last step later.
- **Agent part:** the external monitor detects. A cloud routine (`/fire` API trigger) diagnoses and tries one allowlisted self-heal. The monitor confirms recovery. The routine never changes Google Ads.
- **1-hour budget (example):** detect ≤ 15 min (5 min interval × 2–3 failures). Self-heal and verify ≤ 15 min. Human acknowledgement ≤ 15 min, else escalate to the backup.

## 5. Gaps and honest notes

- **Topic 1:** only 3 fresh practitioner sources (13, 14, 15). Three more show only "last updated" dates (16, 17, 18) and are down-weighted. The rules rest on vendor docs.
- **Topic 2:** only 1 fresh practitioner source (36), and it contains one wrong claim. Topic 2 rests on official docs. Zapier Autoreplay retry count and timing are not on the official page. Search snippets say 5 attempts; this is not verified.
- **Topic 3:** only 1 fresh practitioner source (55). Search Engine Land had no matching fresh article. The "hourly minimum" for scripts comes from a third party, not from Google. No official MCC anomaly detector or disapproved-ads script exists in the current solutions list.
- **Topic 4:** Meta's official WhatsApp rate for Indonesia was not retrieved (the rate page redirects). A third-party page (ChatMaxima, date unclear) claims Rp356.65 per utility message from 2026-10-01; this is not verified and not used. Pushover's iOS Critical Alerts behaviour is documented only in a 2020 blog post (dropped as too old). Test it on the real phone.
- **Topic 5:** no fresh source shows a Claude Code routine used as an uptime canary. The pattern "external monitor → routine `/fire`" comes from the routines doc example ("Alert triage"). Check that the monitor webhook can send the needed headers (`Authorization`, `anthropic-beta`, `anthropic-version`). If not, use a small relay. The `/fire` endpoint is under a beta header and can change.
- **Dropped as too old (checked dates):** upticknow (2026-03-14), sslshopper (2026-01-07), tallwatch (2026-06-06), cronbase.dev (2026-06-13), pingguard (2026-06-18), nurbak (2026-06-23), web-alert.io (2026-05-26), incident.io escalation (2026-06-11), n8n community monitoring thread (2026-06-30), crontap heartbeats vs uptime (2026-05-09), oneuptime (2026-03-02), hyperping false positives (2026-04-02), apistatuscheck n8n guide (2026-07-09), theadspend anomaly posts (2026-06-20, 2026-06-21), yeezypay (2026-03-13), ppc.io (2025-04-29), nilsrooijmans disapproval script (2022), Pushover iOS critical alerts blog (2020-02-26), bigiron (2026-05-10), tianpan.co runbook (2026-04-12), iamstackwell runbook (2026-03-08), runframe (2026-05-06), anhtu.dev (2026-06-03), augmentcode AI SRE (2026-05-24), gheware AI SRE (2026-04-04).
- **Left out (no date or low quality):** domain-monitor.io, witscode.com, notilens.com, agoradigest Q&A page, Zapier community threads.
