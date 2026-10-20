---
name: client-roadmap
description: Creates, decomposes, and maintains 741 client roadmaps and goal milestones based on audits, market benchmarks, and empirical gap analysis. Use when Martin types /client-roadmap <client>, or asks for client roadmaps, milestone planning, or goal alignment ("Roadmap für <Kunde>", "Zwischenschritte für Celine", "Meilensteine für Suriya"). Do NOT use for one-off bugfixes without roadmap context, and NOT for writing website copy.
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3:*)
---

# Client Roadmap & Goal Engine (`client-roadmap`)

Full specification: `/Users/martindrendel/741website/00_project/client-roadmap-workflow.md`.
Template: `assets/roadmap-template.json`. Scripts: `scripts/`.

## Critical

- **Zero Unapproved Strategic Drift:** Core client promises, budgets, and North Star Goals must never be altered without Martin's explicit Go via an interactive Decision Card (`ask_question`).
- **Zero Hallucinated Numbers:** Every metric (TTFB, media size, keyword ranking, review count) must cite an authentic evidence file or verified API scan. No estimated baselines.
- **Rule R1.7 Separation:** Gap mathematics ($\Delta = \text{Baseline} - \text{Benchmark}$) and file serialization MUST be executed via deterministic scripts. Strategic milestone sequencing is guided by 741 Phase rules ($P_0 \to P_6$).
- **Strict Read-Only During Synthesis:** This skill plans and structures data; it never directly modifies live client websites, production DNS, or ad campaigns.

## Inputs

- Client identifier (`<client>` slug or name).
- Execution mode:
  - `show` (default: display active roadmap and pre-flight status).
  - `create` (initial synthesis from audit + competitor benchmarks).
  - `update` (mark milestone task complete and advance state).

## Workflow Checklist

Copy this checklist into your response and tick each step:

```
Client Roadmap Progress <client> (<mode>):
- [ ] P0 Ingest data: run scripts/get_roadmap.py <client> OR parse audit baseline
- [ ] P1 Reality check: compute gap delta against market benchmarks
- [ ] P2 Synthesize milestones: decompose North Star Goal into M1-M4
- [ ] 🛑 CHECKPOINT 1: Present roadmap draft to Martin via Decision Card
- [ ] P3 Persist state: write 00_project/assets/<client>/roadmap.json
- [ ] P4 Telemetry: run scripts/write_run.py --client <client> --status passed
```

### Step Details

#### P0: Ingest Client Baseline
If `show` or `update`:
```bash
python3 .claude/skills/client-roadmap/scripts/get_roadmap.py <client>
```
If `create`: Parse audit reports in `00_project/assets/<client>/audit/` and review competitor baseline references.

#### P1: Gap Analysis (Reality Check)
Compute the delta $\Delta = \text{Client Baseline} - \text{Market Benchmark}$:
- Ladezeiten / TTFB (z. B. 2.1s vs. < 200ms Benchmark).
- Medien-Gewicht (z. B. 10.5 MB vs. < 1.5 MB Benchmark).
- Mobile UX / Conversion (z. B. unübersichtliches Dropdown vs. 3-Karten-Hub).

#### P2: Milestone Decomposition
Structure into strictly 3–4 sequential milestones:
- $M_1$: Diagnosis & Audit ($P_2$)
- $M_2$: Harm Repair & Quick-Wins ($P_3$)
- $M_3$: Growth Build-Up & CRO ($P_4/P_5$)
- $M_4$: Proof, Tracking & Telemetry ($P_6$)

#### 🛑 Checkpoint 1: Martin Approval Gate
Always present the proposed roadmap to Martin using an interactive Decision Card (`ask_question`). Never persist a new roadmap without explicit Go.

#### P3: Persist Dual-Storage State
Write the approved roadmap to:
`00_project/assets/<client>/roadmap.json`
and update Supabase `public.client_goals`.

#### P4: Telemetry Output
Emit the standardized run record:
```bash
python3 .claude/skills/client-roadmap/scripts/write_run.py --client <client> --checkpoint cp1 --status passed
```

## Agent Pre-Flight Banner Format

When any chat agent starts a task for `<client>`, it must output:
```
[741 ROADMAP ACTIVE] <Client> · Phase: <Phase> · Active Milestone: M<x> (<Title>)
Goal: <North Star Goal> | Top Constraint: <Client Rule>
Active Tasks:
  ○ [T<x.y>] <Task Description>
```
