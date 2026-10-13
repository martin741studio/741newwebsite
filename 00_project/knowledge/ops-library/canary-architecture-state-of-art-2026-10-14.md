# Canary architecture: state of the art for outage detection and response (2026-10-14)

## Purpose

This file gives the architecture and the process for the 741 outage system. The goal is simple. No client outage lasts longer than 1 hour. Agents run checks, try a safe self-heal, and page a human if the self-heal fails.

- Scope: architecture and process only. Tool lists are in a separate file from another agent.
- Business context: 741 Digital Solutions LLC. Martin is in Bali (WITA, UTC+8). The team is small. Account count from the brief: 10-15. Each account has a website, forms or funnels, Zapier/Make automations and Google Ads.
- Fetch date: 2026-10-14.
- Freshness rule: non-doc sources are from 2026-07-14 or later. Official docs, vendor docs and the Google SRE books are living references. The table labels them so.
- Dates: each date comes from the page or from the page metadata. "Flag" marks a date with a limit.
- Rule format: "IF ... THEN ... (Src: n)". Rules marked "741 proposal" are our design choice. They come from the sources but are not a direct quote of one source.

## Sources

| # | Title | URL | Date | Takeaway |
|---|---|---|---|---|
| 1 | Google SRE Book: Monitoring Distributed Systems | https://sre.google/sre-book/monitoring-distributed-systems/ | living reference | Black-box tests what users see. Page on symptoms, not causes. A page must need urgent human action. |
| 2 | Google SRE Book: Being On-Call | https://sre.google/sre-book/being-on-call/ | living reference | 5 min response for user-facing services, 30 min for others. Primary plus secondary as fall-through. Aim for 1 alert per incident. |
| 3 | Google SRE Workbook: Alerting on SLOs | https://sre.google/workbook/alerting-on-slos/ | living reference | Judge alerts by precision, recall, detection time and reset time. Page at 2 % budget in 1 h or 5 % in 6 h. Ticket at 10 % in 3 days. |
| 4 | Google SRE Book: Postmortem Culture | https://sre.google/sre-book/postmortem-culture/ | living reference | Postmortem triggers include a monitoring failure, a manual intervention and data loss. Blameless means no blame on a person. |
| 5 | Google SRE: Incident Metrics in SRE (Š. Davidovič) | https://sre.google/resources/practices-and-processes/incident-metrics-in-sre/ | living reference (no year on page) | MTTx averages are poor for decisions and trends. Use better measures. |
| 6 | PagerDuty Incident Response docs: Severity Levels | https://response.pagerduty.com/before/severity_levels/ | living reference | SEV-1 to SEV-5 map to page, low-urgency page or ticket. If unsure, use the higher severity. |
| 7 | Prometheus docs: Alertmanager | https://prometheus.io/docs/alerting/latest/alertmanager/ | living reference | Grouping, inhibition and silences. HA setup deduplicates alerts. |
| 8 | Healthchecks.io docs: Configuring checks | https://healthchecks.io/docs/configuring_checks/ | living reference | A heartbeat check has a period and a grace time. Silence after grace means "down". |
| 9 | Nobl9 docs: Time slices error budget method | https://docs.nobl9.com/guides/slo-guides/time-slices | living reference | Only bad time slices (for example bad minutes) burn the budget. This suits low-traffic services. |
| 10 | Anthropic Claude Code docs: routines, desktop scheduled tasks (verified in `_derived/claude-tooling-facts.md` and `_derived/night-shift-server-facts.md`) | https://code.claude.com/docs/en/routines , https://code.claude.com/docs/en/desktop-scheduled-tasks | living reference, fetched 2026-10-11 / 2026-10-13 | Cloud routines: 1 h minimum interval, API `/fire` trigger, no permission picker. Local tasks skip runs while the Mac sleeps. |
| 11 | Anthropic Claude Code docs: Hooks guide (repo copy) | https://code.claude.com/docs/en/hooks-guide | living reference, fetched 2026-10-11 | A `PreToolUse` hook can block a tool call (exit code 2). This is a hard gate outside the model. |
| 12 | Vercel KB: Build an incident response sre agent with eve | https://vercel.com/kb/guide/eve-incident-sre-agent | vendor doc, living reference (no date) | Read-only access by default. Allow-listed tools. Each finding links to its evidence. |
| 13 | OpenAI Cookbook: Build an SRE agent for incident response | https://developers.openai.com/cookbook/examples/agents_api/apps/sev_bot/readme | vendor doc, living reference | Agent investigates, then asks a responder to approve a rollback. Runbooks mount read-only. Credentials stay outside the sandbox. |
| 14 | CloudThinker: What is agentic remediation? | https://www.cloudthinker.io/what-is-agentic-remediation | vendor doc, living reference (no reliable date) | Detect, Analyze, Remediate, Verify. Autonomy levels L1-L4 per runbook. A failed verify rolls back and pages a human. |
| 15 | sre.wang: Postmortem action items tracking | https://www.sre.wang/en/posts/sre-postmortem-action-items-tracking/ | 2026-07-21 | Each action item gets owner, due date and acceptance criteria. Small teams review open items weekly. |
| 16 | Rootly: Where AI helps (and fails) across the incident lifecycle | https://rootly.com/ai-sre-guide/lifecycle | 2026-07-23 (last updated) | AI acts only on narrow, reversible failures. Allow-list by service, severity and reversibility. Verify after each action. Feed postmortems into detection rules. |
| 17 | Rootly: AI SRE FAQ | https://rootly.com/ai-sre-guide/frequently-asked-questions | 2026-07-23 (last updated) | Staged adoption: read-only context first, approval-gated actions next, narrow autonomy last. |
| 18 | ClickHouse: AI SRE agents: can AI run your on-call? | https://clickhouse.com/resources/engineering/ai-sre-agents | 2026-07-29 (last-modified metadata; flag: no visible date) | AI SRE agents automate the investigation. Humans keep the judgement. Remediation stays behind approval in most setups. |
| 19 | Playcode: Software production readiness checklist | https://playcode.io/blog/production-readiness-checklist | 2026-08-01 (updated) | Verify monitoring and alerts before launch. Each gate has an owner and evidence. Have a rollback plan. |
| 20 | Pingvera: Monitoring as code for web agencies | https://pingvera.com/blog/monitoring-as-code-web-agencies.html | 2026-08-08 | Per-monitor fields for agencies: severity, owner, client ID, route, maintenance window, exception with expiry, disabled reason with expiry. |
| 21 | Rework: Best AI agents for DevOps in 2026, ranked by blast radius | https://resources.rework.com/tools/ai-agents/best-ai-agents-for-devops-2026 | 2026-08-17 (updated) | Rank agents by what they can change. Approval modes: ask, deny, pre-approved per action type. |
| 22 | Rootly: Alert management guide (2026) | https://rootly.com/alert-management | 2026-08-17 (last updated) | Alerts must be actionable and owned. Group duplicates. Put service, symptom and evidence in the alert. Review noisy alerts. |
| 23 | TestMu AI: Smoke testing checklist | https://www.testmuai.com/learning-hub/smoke-testing/ | 2026-08-18 (updated; flag: first published 2025-09-26) | Run a reduced smoke suite on production after each deploy. Each escaped defect adds a new smoke case. |
| 24 | Dash0: What is MTTD, MTTA and MTTR? | https://www.dash0.com/knowledge/what-is-mttd-mtta-and-mttr | 2026-08-21 (modified 2026-09-28) | Total outage = detect + acknowledge + resolve. Escalate 5 min to primary, 5 min to secondary. Look at worst incidents, not means. |
| 25 | Anthropic: The AI-native SDLC playbook | https://claude.com/resources/articles/the-ai-native-sdlc-playbook | 2026-08-21 (metadata; page shows Oct 8, 2026) | Hooks are deterministic gates. Log every hook decision. Measure gate violations. |
| 26 | Elastic: Human-in-the-loop automation for SRE incident response | https://www.elastic.co/observability-labs/blog/incident-response-automation-human-approval-gate | 2026-08-26 | Approval gate shows evidence and proposal. Stale requests fail closed. The record keeps the evidence, the reviewer input, the branch that ran and the verify result. |
| 27 | Aident: How to replay failed webhooks safely | https://aident.ai/blog/replay-failed-webhooks-safely-hookdeck | 2026-08-27 | Prove idempotency. Replay one event first. Verify the side effect. Then replay the batch. |
| 28 | Haktan Suren: WordPress contact form monitoring guide | https://www.haktansuren.com/wordpress-form-monitoring/ | 2026-09-02 | Canary form submissions with a unique marker. Assert downstream (mail delivered, CRM record). Do not rely on WP-Cron for idle sites. |
| 29 | DigitXL: Detect broken tracking before campaigns suffer | https://www.digitxl.com.au/blog/how-can-marketing-teams-detect-broken-tracking/ | 2026-09-03 (metadata) | Compare traffic, form starts, conversion events and CRM leads. A drop in one layer only means broken tracking. |
| 30 | Skofi: Why automations fail in production | https://skofi.tech/insights/why-automations-break | 2026-09-10 (modified 2026-10-04) | Silent stops are the main risk. Add a heartbeat to anything scheduled. Use a stable key and upsert to stop duplicate writes on retry. |
| 31 | Checkme.dev: Monitoring false positives, 8 fixes | https://checkme.dev/2026/09/11/monitoring-false-positives/ | 2026-09-11 | Consecutive failures, a control location, regional baselines, grouping, severity split, context in alerts, retire useless alerts. |
| 32 | Motadata: On-call rotation and escalation policy guide | https://www.motadata.com/blog/on-call-rotation | 2026-10-12 | P1: 5 min per escalation level. Use 3-4 levels so an alert cannot die with one person. Small teams page only for critical services. |
| 33 | ITGix: GenAI for incident resolution | https://itgix.com/blog/genai-for-incident-resolution-an-ai-sre-approach/ | 2026-10-13 | The investigation agent is read-only by construction, with separate credentials. Actions get a dry-run preview, human approval and an audit trail. |
| 34 | OnPage: After-hours IT support on-call process | https://www.onpage.com/after-hours-it-support-how-to-build-a-reliable-on-call-process/ | 2026-10-13 | Only critical severities wake people after hours. Unacknowledged alerts escalate automatically. |

Dropped for freshness: a CloudQA synthetic-monitoring guide (first published 2026-03-23), an Improvado anomaly guide (no exact date), a SiteInformant false-positive page (no date).

## 1. SLO and error budget, scaled down to a small agency

1. IF you set the "1 hour max" goal, THEN define it as a cap per incident from failure start to restored service. Track it as three parts: time to detect, time to acknowledge, time to restore. (Src: 24, 5)
2. IF you report incident speed, THEN do not report means. Log the timestamps of each incident. Report the count of incidents over 60 min and the worst incident each month. (Src: 5, 24)
3. IF a client has low traffic, THEN do not alert on real-user error rates. Use synthetic canary results in time slices. A failed slice burns budget, a passed slice does not. (Src: 3, 9)
4. IF you need an error budget per client, THEN use 60 bad minutes per client per month for Tier A paths (741 proposal). One full-length incident uses the whole budget. That triggers a postmortem and reliability work before new feature work for that client. (Src: 3, 9)
5. IF you design the budget split, THEN give detection the smallest share you can buy. Detection is set by configuration before the incident starts. Acknowledgement and repair depend on people. (Src: 24)
6. IF the worst incidents spend most time in detection or acknowledgement, THEN fix monitoring or paging first, not runbooks. (Src: 24)
7. IF a customer reports an outage before your monitors do, THEN count it as a monitoring failure. MTTD only measures incidents that you detected. (Src: 4, 24)

## 2. Check design

1. IF a check can page a human, THEN make it black-box. It must test what the visitor sees: page loads, form submits, lead arrives. Use white-box signals (logs, run history) for diagnosis and early warning. (Src: 1)
2. IF a funnel has a form, THEN run a synthetic transaction end to end. Submit a test record with a unique marker. Assert the downstream result: mail delivered, CRM record created, automation run logged. (Src: 28)
3. IF a canary writes test records, THEN tag each record with the marker and exclude the marker in CRM views and analytics. Never import a canary lead into Ads conversions. Delete or archive test records on a schedule. (Src: 28, 29)
4. IF an event is expected on a schedule (Zap/Make run, nightly job, agent run), THEN add a heartbeat (dead man's switch). Set period and grace time. Silence after grace opens an incident. (Src: 8, 30)
5. IF volume matters (leads per day, conversions per click), THEN add passive reconciliation. Compare inputs with outputs across layers: clicks, sessions, form starts, conversion events, CRM leads. A drop in one layer only points to a broken step, not to lower demand. (Src: 29)
6. IF a check fails once, THEN do not page yet. Confirm with an immediate re-run from a second location, or with 2-3 consecutive failures. Use a control location to tell a site outage from a network problem. (Src: 31)
7. IF a check alternates between pass and fail (flapping), THEN group the transitions into one incident. Add a recovery rule: close the incident only after several consecutive passes. (Src: 31, 7)
8. IF you plan work (deploy, plugin update, migration), THEN open a maintenance window with an end time. Checks keep running and recording, but alerts are muted. Every window and every exception has an expiry. (Src: 20, 7)
9. IF the checks run on a laptop, THEN they are not detection. Local scheduled tasks skip runs while the Mac sleeps, and cloud routines run at most once per hour. Put detection in an external always-on monitor. Use agents for triage, self-heal, reconciliation and reporting. (Src: 10)
10. IF a monitor or agent can stop without noise, THEN watch the watcher. Each agent run ends with a heartbeat ping to a second, independent provider. An hourly cloud routine checks that the primary monitor reported recently. A weekly fire drill trips a test monitor and times the page to acknowledgement. (Src: 8, 10, 4)

## 3. Alert design and escalation

1. IF you define severities, THEN keep three levels. SEV1 = Tier A path down (site, form, lead automation, Ads landing page): page now. SEV2 = partial or degraded: page in client hours, else ticket. SEV3 = ticket (SSL or domain expiry, tracking drift). IF unsure, THEN use the higher level. (Src: 6, 34)
2. IF an alert is not urgent, actionable and in need of human thought, THEN make it a ticket for the morning grill, not a page. (Src: 1, 2, 22)
3. IF a SEV1 page fires, THEN escalate with a 5-minute timeout per level: owner, then backup, then Martin. Use 3-4 levels so an alert cannot die with one person. (Src: 24, 32, 2)
4. IF an alert is acknowledged but nothing happens, THEN re-page after a fixed time. Fast acknowledgement with slow repair is "ack-and-forget". Track both numbers. (Src: 24)
5. IF one failure causes many alerts, THEN group them into one incident per client asset. Inhibit child alerts (form canary, heartbeat) while the parent (site down) fires. Aim for 1 alert per incident. (Src: 7, 2, 31)
6. IF you write the alert text, THEN include: what broke (client, asset, check), since when, impact (lead path, Ads spend at risk), evidence, runbook link, self-heal status and the proposed next action. (Src: 22, 31, 12)
7. IF an alert pages often without action, THEN review it weekly. Tune it, turn it into a ticket, or retire it. (Src: 22, 31)
8. IF a page goes out after client hours, THEN wake people only for SEV1. Client hours in DACH fall in the Bali afternoon and evening, so set the rota to WITA times (741 proposal). (Src: 34, 32)

## 4. Self-healing with guardrails

1. IF the agent investigates, THEN give it read-only access with separate credentials. The agent that acts uses a different, narrow tool set. (Src: 33, 12, 17)
2. IF a fix is reversible, bounded to one client asset and idempotent, THEN it can run without approval. Examples: re-run the canary, purge a cache, replay one failed automation event, re-trigger a webhook, re-run a missed scheduled job. (Src: 16, 27)
3. IF a fix touches Ads (pause, budget, bids), DNS, plugins, content, credentials, client messages or data deletion, THEN it needs a human go. Ads changes always need Martin's reasoned go. (Src: 16, 21; 741 hard rule)
4. IF you replay failed events, THEN prove idempotency first. Replay one event, verify the side effect and check for duplicates. Only then replay the batch. (Src: 27, 30)
5. IF the agent takes any action, THEN verify by re-running the failed check. IF verify fails, THEN roll back where possible and page a human. Allow at most one automatic attempt per incident (741 proposal). (Src: 14, 16)
6. IF an action needs approval, THEN send a card with evidence, proposed action, expected result and a deadline. A stale request fails closed and does not run later. (Src: 26, 13)
7. IF a rule must never break, THEN enforce it outside the model with a `PreToolUse` hook that blocks the call. Log every hook decision. (Src: 11, 25)
8. IF the agent runs as a cloud routine fired by an alert webhook, THEN remove all unneeded connectors and limit the network allow-list. Routines have no permission picker. Treat the alert payload as untrusted data. (Src: 10)
9. IF you add autonomy, THEN promote one runbook at a time. Start at "propose only", then "act with approval", then "act alone within limits". Promote only after a record of verified passes. (Src: 14, 17)
10. IF an agent acts or writes an analysis, THEN keep an append-only audit log: trigger, evidence, action, approver, verify result. Every claim in an analysis cites a tool call. (Src: 33, 26)

## 5. Registry (service catalog for checks)

1. IF a check exists, THEN it has one row in the registry. A check without an owner and a runbook does not page. (Src: 20, 22)
2. IF you build the registry, THEN store it as code in the repo (YAML or JSON) and review changes like code. (Src: 20)
3. IF an exception or a disabled check exists, THEN record the reason and an expiry date. An expired exception re-enables the check or raises a ticket. (Src: 20)

Fields per check:

| Field | Example | Why (Src) |
|---|---|---|
| `check_id`, `client_id`, `asset` | `ruether-form-contact`, `ruether`, URL or Zap ID | Routing and grouping (20) |
| `check_type` | `uptime` / `synthetic` / `heartbeat` / `reconciliation` | Design choice (1, 8, 29) |
| `tier`, `severity` | `A`, `SEV1` | Page or ticket (6) |
| `interval`, `timeout` | `1m`, `30s` | Detection time (3) |
| `confirm_rule` | `2 consecutive` or `re-run from 2nd region` | False positives (31) |
| `grace` (heartbeats) | `15m` | Dead man's switch (8) |
| `recovery_rule` | `3 consecutive passes` | Flapping, reset time (3, 31) |
| `maintenance_window` | reference + end time | Planned work (20) |
| `owner`, `backup`, `escalation` | names + `5m` per level | Acknowledgement (24, 32) |
| `runbook_url` | link to runbook file | Faster repair (22) |
| `self_heal_action`, `autonomy_level`, `max_attempts` | `replay_one_event`, `L2`, `1` | Guardrails (14, 16) |
| `verify_check` | `check_id` to re-run | Verify step (14) |
| `test_marker` | marker string for canary records | Clean data (28) |
| `alert_route` | channel + page target | Routing (20) |
| `last_result`, `last_run_at`, `last_heartbeat` | `pass`, timestamp | Watch the watcher (8) |
| `last_incident`, `created_from_incident` | incident IDs | Canary loop (16, 23) |
| `exception_id` + `exception_expiry`, `disabled_reason` + `disabled_expiry` | text + date | No silent drift (20) |
| `template_version`, `review_date` | `v3`, date | Audits (20) |

## 6. Post-incident and launch gates

1. IF an incident breaks the 1-hour cap, loses leads, needs manual work, or a client finds it first, THEN write a postmortem. (Src: 4)
2. IF you write a postmortem, THEN keep it to one page and keep it blameless: timeline, impact, contributing causes, what worked, action items. Focus on systems, not people. (Src: 4, 15)
3. IF a postmortem has action items, THEN each item has one owner, a due date and an acceptance test. Review open items in the weekly meeting. (Src: 15)
4. IF the incident was found late or by a person, THEN one action item is always "add or change the check that would have caught it earlier". Link the new check with `created_from_incident`. Every outage becomes a canary. (Src: 16, 23, 4)
5. IF you launch a site, form, funnel or automation, THEN it needs a registry row, a passing end-to-end canary, a tested alert route and a rollback or fallback plan. No launch without these. (Src: 19, 20, 23)
6. IF you deploy a change to a live client asset, THEN run the reduced canary suite against production right after the deploy. (Src: 23)
7. IF you sign off a launch, THEN check the run history too, not one pass. Require 24 h of green canary runs (741 proposal). (Src: 19, 23)

## Reference architecture for a small agency

### Components

1. **External monitors (always on, not on the laptop).** Uptime and keyword checks at 1-min intervals from 2+ regions. Synthetic form canaries every 10 min. Heartbeat endpoints for each automation and each agent run.
2. **Reconciliation agent (hourly cloud routine).** It compares clicks, sessions, form events, CRM leads and automation run counts per client against a baseline. It raises SEV2/SEV3 tickets. It also checks that the primary monitor reported recently.
3. **Monitor registry (repo, YAML/JSON).** This is the single source of truth for checks, owners, runbooks, self-heal actions and escalation. Monitors and agents read from it.
4. **Alert router.** It groups, inhibits, routes by severity and runs the escalation chain owner → backup → Martin at 5 min per level. It sends one webhook per incident to the triage agent.
5. **Triage and self-heal agent.** Alert webhook fires a cloud routine through the API. Investigation is read-only. One allow-listed reversible action per incident. Verify by re-running the check. Gated actions go out as approval cards with a deadline. Hooks block forbidden tools.
6. **Watcher of the watcher.** A second provider receives heartbeats from every agent run. A weekly fire drill trips a test check and times the path from page to acknowledgement.
7. **Incident log and postmortem loop.** Timestamps per incident, audit log of agent actions, one-page postmortem, and a new or changed registry row per incident. The morning grill shows open items.

### Data flow

```
client asset ──(1-min HTTP / 10-min canary / heartbeat)──► external monitor
      │                                                         │ confirm (2nd region or re-run)
      │                                                         ▼
      │                                                   alert router ──► page owner → backup → Martin (5 min each)
      │                                                         │
      │                                                         └─webhook─► triage agent (cloud routine, read-only)
      │                                                                       │ allow-listed action? yes → act once → re-run check
      │                                                                       │ no / verify fails → approval card or human
      ▼                                                                       ▼
reconciliation agent (hourly) ──► tickets ──► morning grill        audit log + incident log ──► postmortem ──► new check in registry
every agent run ──heartbeat──► second provider (watcher of the watcher)
```

### Time budget for the 1-hour cap (SEV1, worst case, minutes)

| Phase | Uptime / keyword check | Form or funnel canary | Automation heartbeat |
|---|---|---|---|
| Detect (interval x confirm) | 4 (1-min interval, 2-3 failures, 2nd region) | 13 (10-min interval + immediate re-run) | 15 (period + grace) |
| Alert delivery | 1 | 1 | 1 |
| Agent triage + 1 safe self-heal (runs in parallel with acknowledgement, timebox 10) | (0, parallel) | (0, parallel) | (0, parallel) |
| Acknowledge: owner 5 → backup 5 → Martin 5 | 15 | 15 | 15 |
| Mitigate with runbook or fallback | 30 | 24 | 22 |
| Verify (re-run the failed check) | 3 | 3 | 3 |
| Reserve | 7 | 4 | 4 |
| **Total** | **60** | **60** | **60** |

Notes on the budget:

- The typical case is much shorter. The page reaches the owner in the first 5 minutes, so the acknowledgement time is usually 5, not 15.
- "Mitigate" means restore the lead path, not fix the root cause. Examples: switch to a fallback form, replay held leads, restore the last working version. A permanent fix can follow in business hours.
- Cloud routines cannot detect within budget (1 h minimum interval). The external monitor must detect. The routine starts only on the alert webhook.
- Reconciliation checks find slow damage (tracking drift, lower lead counts). They are SEV2/SEV3 and are outside the 1-hour cap.
- Pausing Ads that send traffic to a broken page is a mitigation. It still needs Martin's go under the 741 rule, so the alert card must offer it as a ready decision.
