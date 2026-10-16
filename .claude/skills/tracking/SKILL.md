---
name: tracking
description: Runs 741 Proof Tracking and Quarterly Strategy War Room for active clients - weekly card updates (GBP calls, form leads, GSC impressions), Local Falcon grid monitoring, early warning alerts (R1-R6, Y1-Y9), and 90-day quarterly war-room pack generation. Use when Martin types /tracking <mode> <client>, or asks for weekly tracking, proof numbers, early warning checks, or quarterly war room preparation ("Tracking für <Kunde>", "Wochen-Update für Suriya", "Quartalsrunde vorbereiten"). Do NOT use for one-off Local Falcon ranking scans (use ranking-tracking-master-prompt), and NOT for writing website copy.
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3:*)
---

# Proof Tracking & Quarterly War Room (`tracking`)

Full specification: `/Users/martindrendel/741website/00_project/tracking-workflow.md`.
Metric catalog: `references/metric-catalog.md`. Scripts: `scripts/`.

## Critical

- **Zero Guessed Numbers:** Never estimate missing conversion data. If a client has not updated booking status, write "fehlt seit <Datum>". Leave cost per booked job blank rather than guessing.
- **No Primary Number Overwrite:** The primary business phone number on Google Business Profile remains the real office line. Tracking relies on call clicks and the lead log.
- **Client Gate:** All weekly cards and war-room sections remain draft until Martin's explicit release (GO-W, GO-M, GO-Q2). No unapproved portal updates.
- **Rule R1.7 Separation:** All WoW/MoM calculations, goal discrepancies ($\Delta = \text{Actual} - \text{Goal}$), and alert evaluations MUST be executed via `scripts/compute_weekly_metrics.py` and `scripts/check_alert_rules.py`. Never compute math in prompt text.
- **Pre-Send Sweep:** Any question or required input for Martin must be delivered via an interactive AskUserQuestion card.

## Inputs

- Client identifier (`<client>` slug or name).
- Execution mode: `weekly` (weekly card + Loom), `check` (alert engine), or `quarter` (90-day war room).

## Workflow Checklist

Copy this checklist into your response and tick each step:

```
Tracking Progress <client> (<mode>):
- [ ] P0 Ingest data: run scripts/compute_weekly_metrics.py --client <client>
- [ ] P1 Check early warnings: run scripts/check_alert_rules.py --client <client>
- [ ] P2 Synthesize deliverable (weekly card draft OR quarterly war pack)
- [ ] P3 Emit telemetry: run scripts/write_run.py --client <client> --checkpoint <mode>
- [ ] 🛑 CHECKPOINT: Present draft + Loom points to Martin. Await GO-W / GO-Q1 release.
```

### Step Details

#### P0: Ingest & Compute Metrics
Execute the deterministic computation engine:
```bash
python3 .claude/skills/tracking/scripts/compute_weekly_metrics.py --client <client>
```
Extract current values, WoW % changes, and goal discrepancy delta ($\Delta$).

#### P1: Early Warning Check
Run the alert rule engine:
```bash
python3 .claude/skills/tracking/scripts/check_alert_rules.py --client <client>
```
- **Red Alert (R1–R6):** Output urgent mitigation box for Martin; immediately prepare email alert.
- **Yellow Alert (Y1–Y9):** Log for inclusion in daily standup.

#### P2: Synthesis
- **Mode `weekly`:** Draft the 3-bullet plain-language summary in German (Ich-Form, du) for the client portal "Ergebnisse" tab, plus 3 concise Loom talking points for Martin.
- **Mode `quarter`:** Build the 90-day executive performance vs baseline reconciliation pack, showing total leads, booked jobs, CAC, and 3 strategic renewal options.

#### P3: Telemetry & Checkpoint Gate
Write the standardized telemetry record:
```bash
python3 .claude/skills/tracking/scripts/write_run.py --client <client> --checkpoint <mode> --status passed
```
Present the draft to Martin and await his release click before pushing to the live portal.

## Output Format

```
Tracking: <client> · Mode: <weekly|check|quarter>
Status: <green | yellow | red>
Metrics Summary:
• GBP Calls: <current> (<delta_pct>% WoW)
• Search Impressions: <current> (<delta_pct>% WoW)
• Form Leads: <current> (Pacing vs Goal: <delta>)
Waiting for: <GO-W | GO-Q1>
```
