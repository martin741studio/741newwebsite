# 2.4 Pipeline — canary (2026-10-14)

Shapes from patterns.md §4: 4.8 scheduled brief (detect → decide → verify → post → confirm → ledger), 4.4 plan-validate-execute (self-heal and registry changes), 4.1 gates. Decisions C1–C8.

```
 ┌──────────── LAYER 1 · DETECT (deterministic, always on, no LLM, no laptop) ────────────┐
 │ Interim (C5, from today)                     │ Target (C4, when the Hetzner server runs)  │
 │ • UptimeRobot free: L checks (HTTP+keyword), │ • runner.py (systemd timer, every 5 min)   │
 │   5 min, 2 fails → Telegram                  │   executes registry checks L / S / R       │
 │ • Zapier Manager Zap per client account:     │ • confirmed fail (2×) → alert.py           │
 │   "New Zap Error" + "Zap Turned Off" → Tg    │ • UptimeRobot stays as 2nd location        │
 │ • Ads script per account (hourly, read-only) │ • Ads scripts unchanged                    │
 └──────────────────────────────┬──────────────────────────────────────────────────────────┘
                                │ alert payload (what, since, check id)
 ┌──────────── LAYER 2 · ALERT + ESCALATE (C1, C2, C3) ───────────────────────────────────┐
 │ Telegram @Socials741_bot → Martin (private chat), button "✅ Übernommen"                 │
 │ SEV1 (live lead path broken) pages 24/7 · SEV2/3 wait for 06:13 grill                    │
 │ no ack in 10 min → Dinakar (Telegram) with runbook + diagnosis   [needs listener: server] │
 └──────────────────────────────┬──────────────────────────────────────────────────────────┘
                                │ Martin opens chat / runner calls `claude -p "/canary incident <id>"`
 ┌──────────── LAYER 3 · TRIAGE + SELF-HEAL (/canary skill, incident mode) ───────────────┐
 │ 1 registry row + runbook  2 re-check (failed read = unreadable)  3 diagnose read-only    │
 │ 4 allow-listed fix? ──yes──► plan → validate (allowlist.py) → execute once → re-check    │
 │                     └─no / fails──► decision card: what, since, impact, fix, go needed   │
 │ ◆ GO (Martin): any write into a client system, any login, any Ads action                 │
 └──────────────────────────────┬──────────────────────────────────────────────────────────┘
 ┌──────────── LAYER 4 · RECORD + LEARN ──────────────────────────────────────────────────┐
 │ incidents/<date>-<id>.md (detect/alert/ack/restore times) · results.json · _run.json     │
 │ 06:13 grill S8: red/yellow per client, runner age (C6: red > 30 min), coverage gaps,     │
 │ blockers without owner > 1 h · post-incident note + 1 new/changed check                  │
 └─────────────────────────────────────────────────────────────────────────────────────────┘

 ADD MODE (UC1):  read lead path → pick checks (catalogue) → registry row → validate
                  → ◆ GO (create in client account / switch on) → run once → test alert
                  → measure ack → _run.json
```

## Martin checkpoints (◆ = waits for "go")
| # | When | What Martin decides |
|---|---|---|
| CP1 | after design | this pipeline, use cases, test scenarios |
| G1 | add mode | create the Zapier Manager Zap in a client's Zapier, install an Ads script, switch a check on |
| G2 | incident mode | any self-heal that writes into a client system (replay into CRM, re-enable Zap, edit Zap), any login |
| G3 | incident mode | any Ads action (pause campaign to stop wasted spend) — reasoned go only, never by the canary |
| CP2 | after tests | scorecard + one real output |

## Hard limits (enforced in skill Critical + allowlist.py)
No Ads change. No website change. No client message. No email except via Airmailer with go (alerts use Telegram, not email). No credential typing. Read-only credentials where possible.

## Known gaps in the interim (until the server)
- No ack listener → escalation to Dinakar after 10 min cannot be timed. Interim: Dinakar joins the alert path once he has the bot chat (open item); Martin acknowledges by answering in chat.
- No outside watcher for the runner (C6) → grill shows runner age.
- Telegram cannot break iOS Focus → Martin allows Telegram in Sleep/Focus (setup step S-1), tested at night.
