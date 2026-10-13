# Check catalogue — pick checks by type when adding a canary (UC1)

Walk the client's lead path (page → form → automation → CRM/ESP → Ads) and pick one row per hop that can break silently. Not every system needs every type.

## L — Liveness (HTTP + keyword)
What: a page or endpoint answers 200 and contains an expected marker (e.g. the form embed URL).
When: every public page in the lead path (landing page, booking page, form page).
Interval: 1–5 min once on a runner; today verified by hand with curl (see hand-run.md), added to UptimeRobot once the account exists (decision C12).
Threshold: 2 consecutive failures, or a 2nd location disagreeing — never alert on one failed check (canary-research rule 1).
Example: `marcel-gewinnspiel-page`, `marcel-gewinnspiel-form` in canaries.json.

## S — State (is the automation switched on?)
What: Zap/Make scenario/n8n workflow is active, not paused or disabled.
When: any automation that must always run.
How: Zapier — Zapier Manager push (type E) covers this already; a poll (`GET /v2/zap-runs`, experimental, needs OAuth scope `zap:runs`) is a fallback. Make — `GET /scenarios` for `isActive`/`isinvalid` (no deactivation webhook exists). n8n — `GET /api/v1/workflows?active=true`.
Threshold: state = off/paused/inactive.

## E — Error push (the platform tells us)
What: the automation platform's own error/deactivation signal, pushed to us instead of polled.
When: always prefer this over polling when the platform offers it — it is the fastest detection (minutes, not a check interval).
How (Zapier): one Zapier Manager Zap per trigger per client account — "New Zap Error" and "Zap Turned Off" — → Telegram. Build steps: `references/zapier-manager-setup.md`.
How (Make): no deactivation webhook in the docs; use "Deactivation" email preference (Profile → Email preferences → Organizations) forwarded, or poll S instead.
How (n8n): a shared Error Trigger workflow (Options → Settings → Error workflow) with an HTTP alert step.
Caveat: Autoreplay delays Zapier's error push until the last retry finishes (canary-research rule 4) — still the fastest option available.
Example: `marcel-gewinnspiel-zaperror`, `marcel-gewinnspiel-zapoff`.

## R — Reconciliation (absence of signal / dead-man's switch)
What: count real events at the source vs the target over a window; a failed read is "unreadable", never "0" (rule R6.2).
When: whenever a silent partial failure is possible — an automation can run green while data lands wrong (Marcel's case: tag not found, mails never started).
How: read-only API key per system (Tally, Pipedrive, KlickTipp, …). Never a browser session (unreliable — see hand-run.md Tally finding) and never a synthetic test record in the client's CRM unless Martin specifically approves it for a go-live gate (decision C7).
Threshold: any gap in the window.
Example: `marcel-gewinnspiel-reconciliation` (blocked on keys, see note in canaries.json).

## A — Ads (read-only)
What: campaign stopped, zero spend, disapproved ad, empty balance, conversion tracking stale.
When: any client with a live Google Ads account.
How: a read-only Google Ads script per account (`search()`/`report()` only, never `mutate()`, never the official Link Checker's label writes) + MCC email notifications (Admin → Notifications → Full hierarchy) for disapprovals/billing. No API developer token exists yet (2026-10-14) — scripts run inside each account, no token needed.
Never: any Ads mutation — hard limit, reasoned go only (never by a canary).
Checks: `campaign.primary_status_reasons`, `ad_group_ad.policy_summary.approval_status = DISAPPROVED`, `metrics.impressions/cost_micros = 0` on an enabled campaign, `metrics.conversion_last_received_request_date_time` staleness, account balance/billing status. Leave out the last ~3 h of data (Ads stats lag).

## Picking the severity
- SEV1 (pages 24/7, after one self-heal attempt): a live client's lead path is broken right now (form, funnel, site down, Zap off).
- SEV2 (grill + Martin during the day): degraded but the lead path still works (reconciliation gap, slow page, one failed run others succeeded).
- SEV3 (grill only): informational, coverage gaps, false-alarm review.
