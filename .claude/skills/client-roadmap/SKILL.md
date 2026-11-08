---
name: client-roadmap
description: Creates, decomposes and maintains 741 client roadmaps and goal milestones from audits, market benchmarks and gap analysis. Use when Martin types /client-roadmap <client>, or says "Roadmap für <Kunde>", "Zwischenschritte für Celine", "Meilensteine für Suriya", or asks for milestone planning or goal alignment. Not for one-off bugfixes without roadmap context.
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3:*)
---

# Client Roadmap & Goal Engine (`client-roadmap`)

Full specification: `/Users/martindrendel/741website/00_project/client-roadmap-workflow.md`. Template: `assets/roadmap-template.json`. Schema: `references/roadmap-schema.md`.

## Critical

- **No strategic drift.** Client promises, budgets and North Star Goals change only with Martin's Go via an AskUserQuestion decision card.
- **No invented numbers.** Every metric (TTFB, media size, keyword ranking, review count) cites an evidence file or a verified API scan. No estimated baselines.
- **Math and serialization in scripts.** Gap delta (baseline minus benchmark) and file writing run through the scripts. Milestone order follows the 741 phase rules (P0 to P6).
- **Read-only.** This skill plans. It never changes live client sites, production DNS or ad campaigns.

## Inputs

Client slug or name, and mode: `show` (default: active roadmap and pre-flight status), `create` (first synthesis from audit and competitor benchmarks), `update` (mark a milestone task complete, advance state).

## Steps

1. Ingest. `show` or `update`: `python3 .claude/skills/client-roadmap/scripts/get_roadmap.py <client>`. `create`: read the audit reports in `00_project/assets/<client>/audit/` and the competitor baselines.
2. Reality check: gap against market benchmarks, for example TTFB 2.1 s vs under 200 ms, media weight 10.5 MB vs under 1.5 MB, mobile UX (unclear dropdown vs 3-card hub).
3. Decompose the North Star Goal into 3 to 4 sequential milestones:
   - M1 Diagnosis & Audit (P2)
   - M2 Harm Repair & Quick-Wins (P3)
   - M3 Growth Build-Up & CRO (P4/P5)
   - M4 Proof, Tracking & Telemetry (P6)
4. CHECKPOINT: present the draft roadmap via AskUserQuestion. Persist nothing without an explicit Go.
5. Persist: write the approved roadmap to `00_project/assets/<client>/roadmap.json` and update Supabase `public.client_goals`.
6. Telemetry: `python3 .claude/skills/client-roadmap/scripts/write_run.py --client <client> --checkpoint cp1 --status passed`

## Pre-flight banner

When any chat agent starts a task for `<client>`, it prints:
```
[741 ROADMAP ACTIVE] <Client> · Phase: <Phase> · Active Milestone: M<x> (<Title>)
Goal: <North Star Goal> | Top Constraint: <Client Rule>
Active Tasks:
  ○ [T<x.y>] <Task Description>
```
