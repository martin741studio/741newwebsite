# 1.5 Research note — canary (2026-10-14)

**Block:** hybrid. Deterministic always-on monitors detect (not the laptop, not an LLM). An alert webhook starts the `/canary` agent (routine API trigger, official "alert triage" pattern, routines.md:33) for triage, one safe self-heal and escalation. The same skill adds canaries to one registry. (block-choice.md)

**3 rules that shape the design**
1. Detection cannot be an agent: routines run at most hourly, desktop tasks skip while the Mac sleeps (routines.md:143, desktop-scheduled-tasks.md:68). An external monitor detects; it pings the routine `/fire` endpoint. (ops-library architecture §Reference)
2. Alert only on confirmed failure (2–3 consecutive fails or a 2nd location), keep a recovery period, and treat a failed read as "unreadable", never as "zero" (canary-research rules 1–3; automation-workflow.md §1.6; rules.md R6.2).
3. Self-heal = allow-listed, reversible, once; verify with the external check, not with the fix call's 200 OK; else escalate owner → backup → Martin (5 min per level). Ads, websites, credentials, client messages always need a human go (canary-research rule 8–9; Martin's hard limits).

**1 pattern:** patterns.md 4.8 "scheduled brief" + 4.4 plan-validate-execute → monitor → webhook → agent reads registry row + runbook → re-check → allowed fix → re-check → incident log → card to the Command Center; post-incident: "every outage becomes a canary" + launch gate (no go-live without a passing end-to-end canary and a tested alert route).

**Time budget (1-hour cap, worst case, from the architecture file):** uptime 4 detect + 1 alert + 15 ack + 30 mitigate + 3 verify + 7 reserve; form/funnel 13+1+15+24+3+4; heartbeat 15+1+15+22+3+4. Agent triage runs in parallel with the acknowledgement.

**Marcel case → signals (incident-marcel-2026-10-13.md):** Zapier Manager "New Zap Error" + "Zap Turned Off" → 741 webhook (S2); Zap state poll (S3); Tally submissions vs Pipedrive stage 66 / KlickTipp tag reconciliation (S4); page + form liveness (S5); launch gate (S1); open-blocker aging (S6).

**Reuse (coverage-map.md):** Automation Build L6 rules + templates (canary = its missing monitor half), tracking M25/M26 spec, Morning Grill S8 slot + cards + Command Center, Telegram sender, Resend alerts@ plan, registry (`_run.json` under 00_project/assets/<client>/canary/).

**Tools found (to decide with Martin):** HTTP checks UptimeRobot (free 50 × 5 min, commercial use allowed; Solo $10/mo = 60 s) or Better Stack; heartbeats Healthchecks.io free (20 jobs); phone alert Pushover priority 2 (repeats until ack, $4.99 once per platform) — only Pushover p2 and repeated calls break iOS Focus; Telegram group as team feed; SMS to Indonesia and WhatsApp API are poor fits. Ads: Google Ads script per account (read-only `search()`/`report()`), no API token today.

**Open questions (→ grill cards):** alert channel; quiet hours vs 1-hour target (night = DACH daytime); who is backup on-call; where the runner lives (Supabase pg_cron/edge function vs Hetzner server vs SaaS only); synthetic form test records in client CRMs (yes / only daily with cleanup / no, reconciliation only); Ads read path (script per account vs API token); how much to spend per month.
