# N07 — Healthchecks.io: heartbeat monitoring ("dead man's switch") as a one-person-run product

- Org/author: SIA Monkey See Monkey Do (Healthchecks.io), a one-person company
- Type: official product docs (About page, FAQ)
- Publish date: living pages; counted as current on fetch date. The "one-man company" and reliability framing are the product's own current self-description.
- URL: https://healthchecks.io/about , https://healthchecks.io/faq
- Fetch date: 2026-10-15

## Extract (own words)

- The pattern: the monitored system must check in (send a heartbeat) at a configured interval; Healthchecks.io alerts when a check-in is *missed*, not when a failure is actively reported — this is explicitly called "heartbeat monitoring," and it catches silent failures (a process that stops running entirely, or hangs with no error) that outside-in uptime polling (e.g. UptimeRobot hitting a URL) cannot see, because there is no URL to poll for "did my cron job run."
- Each check has a configurable **period** and **grace time** — tuning these per job is the direct lever against false alarms (a job that's merely running a bit long vs. one that's actually dead).
- Alerts can route to PagerDuty or other existing channels instead of building a second notification path.
- The product itself is run by one person, and its own About page is candid about the operational risk of that: "the database fail-over process is manual, and the ops team consists of a single person, so multi-hour or even multi-day outages are possible," despite a track record of >99.9% uptime since 2015 (best-effort, not a guarantee). This is the vendor's own disclosure, not a third-party criticism.
- It is open-source (BSD-licensed) and self-hostable.

## IF/THEN rules for 741

1. IF 741-agents-01's systemd units are confirmed "active" by systemd but 741 has no independent proof the underlying work is actually happening (the exact gap decisions.md and canary/SKILL.md both flag as open: "no outside watcher for the runner itself"), THEN add a heartbeat check: have the night-shift runner (and the persistent `claude remote-control` session) ping a dead-man's-switch endpoint after each real unit of work, with a period/grace window tuned to the job's own cadence, rather than trusting systemd's own status report.
2. IF 741 is deciding whether to build a second monitoring stack for 741-agents-01 server health, THEN don't — canary/SKILL.md already owns outage-watch and alerting (Telegram escalation, SEV1 paging, allowlist-gated self-heal); the server's own heartbeat should feed into that same alerting path as one more check row, not a separate system with its own thresholds and fatigue risk.
3. IF Martin picks a dead-man's-switch tool for this, THEN know even the category's own reference implementation is explicit that a one-person operation can have a multi-hour or multi-day outage of the *monitor itself* — this is exactly the scenario 741's canary decisions.md already flagged (C6, "no outside watcher for the runner itself... revisit after first real outage") and it argues for a second, independent, low-effort check (e.g. a free-tier external uptime ping on the dead-man's-switch service's own status, or simply noticing a daily digest stopped arriving) rather than a single point of truth.

## Caveats

- No 2026-dated source found specifically on "alert fatigue for solo founders" (searched directly); the fatigue-reduction levers above (period/grace tuning, routing to one existing channel) are the product's own documented mechanism, not a dated best-practice study.
