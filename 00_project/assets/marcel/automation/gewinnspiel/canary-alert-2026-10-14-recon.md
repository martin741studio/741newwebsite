# Canary alert — marcel-gewinnspiel-recon, 2026-10-14

Signal: 6 Tally submissions, 0 Pipedrive deals in 60 minutes. Read-only triage. No live API/browser session in this run — no Zapier, Tally, Pipedrive, or KlickTipp check was done. Everything below is desk research from repo files, not a live read.

## What this check is (found, not pre-built)
System: Gewinnspiel funnel for Marcel Rosenbach. Tally form `2EMGve` (deep-nlp.com/gewinne-jetzt) → Zapier zap `382522671` → KlickTipp tag `15229620` + Pipedrive Pipeline 8 "GEWINNSPIEL 🎉 PRAC", entry stage 66 "🎉NLP-FREUND".
Source: `00_project/assets/marcel/automation/gewinnspiel/findings-2026-10-14.md` (today's own retro-check), `00_project/assets/marcel/automation/gewinnspiel/spec.md`, memory file `marcel-rosenbach-client.md`.

## Why this is probably not a new problem
Today's own retro-check (same file, run this morning) already found two matching defects on this exact zap:
- T6: Zapier disabled the zap after repeated errors and emailed only Marcel, not martin@741.studio. No alert reached 741.
- T5: idempotency failure — replay/retry creates a second Pipedrive deal per person (over-counts, does not explain a zero).

Today's morning-grill brief (`00_project/assets/morning-grill/2026-10-14/brief.md`) also logs, independently: "Marcel reports the Zap was switched off" (open item, unresolved). Two independent sources point the same way.

Working hypothesis, ranked:
1. (most likely) Zap `382522671` is OFF or disabled again — matches both the morning finding and Marcel's own report.
2. The zap is ON but failing on every run (KlickTipp or Pipedrive step error) — this exact funnel had two live-breaking field-mapping bugs on its sibling flow in September (KlickTipp 406, Pipedrive 400), so a recurrence is plausible.
3. Tally → Zapier webhook delivery itself is broken (less likely: Tally UI blocks malformed submissions client-side per T2 in the same findings file, so 6 submissions reaching Tally argues the trigger side is fine).
4. Real outage vs. test noise: unresolved — the same findings file flags unexplained failed runs from 13.10. 20:24–20:54 as still open (real participants or tests, unknown).

## What I did not do, and why
No Zapier/Pipedrive/Tally read was performed — I have no live API or browser session this run. I did not guess a fix and did not touch any live system. Re-enabling a zap is a class-G action ("switch on or publish") under `00_project/automation-workflow.md` §2 — it needs Martin's `go A<n>`, not a silent self-heal, even if I could reach it.

## Recommended next step (for whoever has live access)
1. Read-only: open Zap `382522671` history — is it ON or disabled? Read the last 6 run logs; find the KlickTipp/Pipedrive step error if any.
2. Read-only: Pipedrive Pipeline 8 — confirm 0 new deals since the alert window, independent of the Zapier task history (T-items in the findings file flagged Zapier's own return as the only readback so far — no independent Pipedrive login check done yet either).
3. If the zap is OFF: this is a G action to turn back on. Draft the ask to Martin, do not flip it without his go.
4. If zap is ON but erroring: diagnose the failing step (cap at 3 fix attempts per `automation-workflow.md` §9), then the same G-action gate applies to republishing a fix.
5. Either way: clean up anything the 6 stuck submissions caused once the real participants are known, and close the open T6 gap (alert mail to martin@741.studio, not just Marcel) so this class of failure stops needing a manual canary catch.

## Draft alert (not sent — for review only)
```text
Canary: Gewinnspiel-Funnel (Marcel) — 6 Tally-Anmeldungen, 0 neue Pipedrive-Deals in 60 Minuten.
Vermutung (ungeprüft, kein Live-Zugriff): Zap 382522671 aus oder fehlerhaft — deckt sich mit dem offenen Punkt "Marcel meldet, der Zap sei ausgeschaltet" und dem heutigen Befund, dass Zapier-Fehlermails nur an Marcel gehen.
Noch nicht live geprüft: Zap-Status, Pipedrive Pipeline 8, Tally-Zustellung.
```

## Severity (my own call, not from a scale I found defined anywhere)
Called this "high" — a client-facing lead funnel is silently not reaching the CRM, and it is a giveaway with a deadline, so delay costs real leads and Marcel already escalated once. Treated the previous day's known-fragile zap finding as upgrading confidence in the hypothesis, not as proof.
