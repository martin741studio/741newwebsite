---
name: tracking
description: Runs 741 Proof Tracking and the Quarterly War Room for active clients - weekly card updates (GBP calls, form leads, GSC impressions), Local Falcon grid monitoring, early warning alerts (R1-R6, Y1-Y9), 90-day war-room pack. Use when Martin types /tracking <mode> <client>, or says "Tracking für <Kunde>", "Wochen-Update für Suriya", "Quartalsrunde vorbereiten", or asks for proof numbers or early warning checks. Not for website copy.
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3:*)
---

# Proof Tracking & Quarterly War Room (`tracking`)

Full specification: `/Users/martindrendel/741website/00_project/tracking-workflow.md`. Metric catalog: `references/metric-catalog.md`. Status block format: `references/output-format.md`.

## Critical

- **Zero guessed numbers.** Missing conversion data is written as "fehlt seit <Datum>". Cost per booked job stays blank rather than guessed.
- **No primary number overwrite.** The primary phone number on the Google Business Profile stays the real office line. Tracking relies on call clicks and the lead log.
- **Client gate.** Weekly cards and war-room sections stay draft until Martin releases them (GO-W, GO-M, GO-Q2). No unapproved portal updates.
- **Math only in scripts.** WoW/MoM, goal delta (actual minus goal) and alert evaluation run through `scripts/compute_weekly_metrics.py` and `scripts/check_alert_rules.py`, never in prompt text.

## Inputs

Client slug or name, and mode: `weekly` (weekly card + Loom), `check` (alert engine), `quarter` (90-day war room).

## Steps

```bash
python3 .claude/skills/tracking/scripts/compute_weekly_metrics.py --client <client>
python3 .claude/skills/tracking/scripts/check_alert_rules.py --client <client>
python3 .claude/skills/tracking/scripts/write_run.py --client <client> --checkpoint <mode> --status passed
```

1. Compute metrics (first command): current values, WoW %, goal delta.
2. Check alerts (second command). Red R1–R6: urgent mitigation box for Martin and a prepared email alert. Yellow Y1–Y9: log for the daily standup.
3. Synthesize.
   - `weekly`: 3-bullet plain-language summary in German (Ich-Form, du) for the portal "Ergebnisse" tab, plus 3 Loom talking points for Martin.
   - `quarter`: 90-day performance vs baseline pack with total leads, booked jobs, CAC and 3 strategic renewal options.
4. Write telemetry (third command).
5. CHECKPOINT: present draft and Loom points to Martin. Wait for GO-W / GO-Q1 before anything goes to the live portal.
