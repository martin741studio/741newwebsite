# 3.1–3.7 Build Note: P6 Proof Tracking (`tracking`)

Date: 2026-10-16
Skill Location: `.claude/skills/tracking/`

---

## 1. Directory Structure (Step 3.1)
```
.claude/skills/tracking/
  SKILL.md                       # Checklist body (88 lines, < 500 lines limit)
  scripts/
    compute_weekly_metrics.py    # Deterministic WoW delta, discrepancy, CAC math
    check_alert_rules.py         # Boolean engine for Red (R1-R6) & Yellow (Y1-Y9)
    write_run.py                 # Telemetry writer for _run.json
  references/
    metric-catalog.md            # Invariant metric definitions
  assets/
```

## 2. Frontmatter Contract (Step 3.2)
- Strict WHAT + WHEN defined.
- Negative trigger explicit: `Do NOT use for one-off Local Falcon ranking scans (use ranking-tracking-master-prompt), and NOT for writing website copy.`
- `disable-model-invocation: true` enforced.
- Tools restricted: `Read, Grep, Glob, Write, Edit, Bash(python3:*)`.

## 3. Checklist & Gates (Step 3.3)
- Sequential P0–P3 checklist with explicit tickable items.
- Top 5 critical rules codified under `## Critical`.

## 4. Modularity & Brevity (Step 3.4)
- Metric catalog moved to `references/metric-catalog.md`.
- `SKILL.md` is 88 lines long (well below the 500-line ceiling).

## 5. Verification & House Rules (Step 3.5 & 3.6)
- Automated verification script tests computation and alert logic.
- ASD-STE100 technical English for agent instructions, clean German for client deliverables.
- Pre-send sweep enforced for open decisions.

## 6. Unattended Rules (Step 3.7)
- Skipped with valid reason: tracking is triggered via `/tracking` command with interactive Martin release checkpoints (GO-W / GO-Q1).
