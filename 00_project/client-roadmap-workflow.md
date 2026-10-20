# 741 Client Roadmap & Goal Engine Specification

Version 1.0 · 2026-10-16 · Owner: Martin Drendel · Approved Cybernetic Architecture.
Language: STE. Registry ID: `roadmap`. Skill: `.claude/skills/client-roadmap/SKILL.md`.

---

## 0. Purpose & Cybernetic Context

The **Client Roadmap & Goal Engine** bridges the gap between high-level client business objectives ($P_1/P_7$) and daily agent execution ($P_3 \to P_5$). It ensures that every compute agent (Antigravity IDE, Claude Code) always has complete visibility into:
1. The **North Star Goal** and empirical benchmark delta ($\Delta$).
2. The current **sequential milestone** ($M_1 \to M_4$) and active task backlog.
3. The **immutable client rules** and operational constraints.

```
[ 1. Sensory Ingestion ]
• Client technical audits (TTFB, media weight, Lighthouse, GSC, Local Falcon)
• Verified niche benchmarks (competitor performance baselines)
                 │
                 ▼
[ 2. Transformation Core (R1.7 Separation) ]
• Deterministic: Gap calculation (Δ = Baseline - Benchmark) via Python script
• Guided Heuristic: Milestone synthesis ($M_1 \to M_4$) based on 741 Phase rules
                 │
                 ▼
[ 3. Governance Gate: Checkpoint 1 ] ──► Martin Decision Card
                 │ (Approved)
                 ▼
[ 4. Dual-Storage Expression ]
• Relational Truth: Supabase `public.client_goals`
• Local Agent Mirror: `00_project/assets/<client>/roadmap.json`
• Telemetry Output: `00_project/assets/<client>/roadmap/_run.json`
                 │
                 ▼
[ 5. Feedback Loop: Mandatory Agent Pre-Flight ]
• Any chat session touching client files reads active milestone before execution
• Completed tasks update milestone state and trigger Morning Grill telemetry
```

---

## 1. The `roadmap.json` Data Contract

Every client has a canonical operational roadmap stored at `00_project/assets/<client>/roadmap.json`:

```json
{
  "client": "Client Name",
  "client_slug": "client-slug",
  "phase": "P4",
  "updated_at": "2026-10-16T12:00:00Z",
  "north_star_goal": {
    "title": "Target description",
    "target_metric": "Primary KPI",
    "deadline": "YYYY-MM-DD",
    "source": "Contract / Audit baseline"
  },
  "benchmark_delta": {
    "baseline": {
      "ttfb_ms": 2100,
      "page_weight_mb": 10.5,
      "mobile_score": 45
    },
    "market_benchmark": {
      "ttfb_ms": 150,
      "page_weight_mb": 1.5,
      "mobile_score": 90
    },
    "gap_summary": "Media weight is 7x higher than market standard; TTFB exceeds budget by 1.9s."
  },
  "milestones": [
    {
      "id": "M1",
      "title": "Diagnosis & Audit",
      "phase": "P2",
      "status": "completed",
      "completed_at": "2026-10-16",
      "evidence": "00_project/assets/<client>/audit/report.md"
    },
    {
      "id": "M2",
      "title": "Speed Quick-Wins & Harm Repair",
      "phase": "P3",
      "status": "in_progress",
      "tasks": [
        {"id": "T2.1", "task": "Convert 3 uncompressed GIFs to WebM/MP4 video loops", "status": "ready"},
        {"id": "T2.2", "task": "Activate WP Fastest Cache static caching", "status": "ready"},
        {"id": "T2.3", "task": "Repoint external Arrow-2.png dependency to local assets", "status": "ready"}
      ]
    },
    {
      "id": "M3",
      "title": "Mobile UX & Conversion Paths",
      "phase": "P4",
      "status": "pending",
      "tasks": [
        {"id": "T3.1", "task": "Streamline navigation menu", "status": "pending"},
        {"id": "T3.2", "task": "Implement sticky mobile booking touchpoint", "status": "pending"}
      ]
    },
    {
      "id": "M4",
      "title": "Telemetry Verification & Reporting",
      "phase": "P6",
      "status": "pending",
      "tasks": [
        {"id": "T4.1", "task": "Lighthouse re-audit verification", "status": "pending"},
        {"id": "T4.2", "task": "GSC baseline logging and client handoff report", "status": "pending"}
      ]
    }
  ],
  "client_rules": [
    "Strict plain text only in client-editable WordPress text boxes",
    "No modifying live templates without backup"
  ]
}
```

---

## 2. Mandatory Agent Pre-Flight Protocol

Whenever an agent (Antigravity IDE, Claude Code) starts a chat session to perform work on a client, it MUST execute the pre-flight routine:

1. **Detection:** Detect client slug from prompt or open files.
2. **Ingestion:** Run `python3 .claude/skills/client-roadmap/scripts/get_roadmap.py <client>`.
3. **Orientation Output:** Output the 2-line pre-flight banner:
   ```
   [741 ROADMAP ACTIVE] <Client> · Phase: <Phase> · Active Milestone: M<x> (<Title>)
   Target: <North Star Goal> | Constraint: <Top Client Rule>
   ```
4. **Scope Enforced:** The agent proceeds only with work directly supporting the active milestone.

---

## 3. Telemetry & Checkpoint Gate

Upon completing any milestone task:
1. Agent runs the deterministic verification script:
   ```bash
   python3 .claude/skills/client-roadmap/scripts/verify_task.py --client <client> --task <task_id>
   ```
2. Writes standardized `_run.json`:
   ```bash
   python3 .claude/skills/client-roadmap/scripts/write_run.py --client <client> --milestone <milestone_id> --status passed
   ```
3. Updates `roadmap.json` and syncs with Supabase `public.client_goals`.
