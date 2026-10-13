# 2.1 Use cases — canary (2026-10-14)

Rule R1.1: trigger phrase, steps, tools, result. Decisions C1–C8 in decisions.md.

## UC1 — Add a canary (add mode)
- **Trigger:** "Set up a canary for <client/system>", "überwache <X>", "sag mir sofort, wenn <X> ausfällt", "canary add", or the go-live gate of Automation Build (L6) / a new launch.
- **Steps:**
  1. Read the registry (`canaries.json`) and the client memory. Identify the lead path: page → form → automation → CRM/ESP → Ads.
  2. Pick checks from the catalogue: L liveness (HTTP + keyword), S state (Zap/scenario on), E error push (Zapier Manager "New Zap Error" / "Zap Turned Off"), R reconciliation (source count vs target count per window, real entries only — C7), A Ads script (read-only — C8).
  3. Set interval, threshold (2 consecutive fails or 1 confirmed error push), severity (SEV1 only if a live lead path breaks — C2), self-heal id from the allow-list, escalation (Martin → Dinakar after 10 min — C3).
  4. Validate the registry row with `scripts/registry.py validate`.
  5. Martin's go for anything that is created in a client account (Zapier Manager Zap, Ads script) or switched on (G action).
  6. Run the check once, read the result. Fire ONE test alert, measure send → ack time.
  7. Write `_run.json` under `00_project/assets/<client-slug>/canary/<date>/`.
- **Tools:** registry script, curl, Zapier (Chrome / Zapier MCP when authorised), Telegram sender, UptimeRobot (interim, Martin's account), later the Hetzner runner.
- **Result:** registry row(s) + live check + test-alert proof (sent / acknowledged timestamps).

## UC2 — Handle an alert (incident mode)
- **Trigger:** an alert payload (Telegram/webhook text, Zapier error mail forwarded, UptimeRobot down event), or Martin: "canary alarm <client>", "was ist down?", "Marcel sagt, der Zap ist aus".
- **Steps:**
  1. Find the registry row. Re-check the signal from the runner (a failed read = "unreadable", never "ok" and never "zero").
  2. Diagnose read-only: run history, error text, last good time, impact (how many entries since).
  3. Self-heal only from the allow-list (e.g. re-run check, refresh cached lists, Zapier replay AFTER root cause is fixed and with go when it writes into a client CRM). Max one attempt. Verify with the external check.
  4. Else escalate: Telegram page to Martin (SEV1 24/7), Dinakar after 10 min without ack. One card: what broke, since when, impact, proposed fix, which go/login is needed.
  5. Log the incident (`incidents/<date>-<id>.md`): detect / alert / ack / restore times.
  6. Post-incident: one-page blameless note + one new or changed check ("every outage becomes a canary").
- **Tools:** registry, run history readers, Telegram, Command Center card, client chat hand-off.
- **Result:** restored lead path within 60 min, or a human holds it with a ready decision; incident log with times.

## UC3 — Daily watch and coverage review (review mode)
- **Trigger:** the 06:13 morning grill (S8 slot), "canary status", "welche Systeme sind nicht überwacht?", weekly review.
- **Steps:** read last check results + incidents; show red/yellow per client; show "last runner heartbeat" age (C6 mitigation: red if > 30 min); list live client systems without a canary (coverage gap) and blockers without owner older than 1 h (Marcel gap S6); false-alarm rate.
- **Tools:** registry, results file, morning-grill scan.py S8, Command Center.
- **Result:** one status block in the grill + cards only for red items and gaps.
