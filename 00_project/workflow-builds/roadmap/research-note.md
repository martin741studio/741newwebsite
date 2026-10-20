# Research Note: Client Roadmap & Goal Engine (`roadmap`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `roadmap`

---

## 1.1 Building Block Selection (Patterns §3)
- **Primary Block:** Skill (`.claude/skills/client-roadmap/` and Antigravity IDE agent skill integration).
- **Secondary Pattern:** Multi-MCP Coordination (Supabase for relational truth, Google Drive for operational sheets, local filesystem for fast agent reading) + Pre-Flight Check Hook.
- **Rationale:** The workflow is an interactive, repeatable procedure triggered on demand per client or automatically at the beginning of an agent session. It needs structured data schemas (Postgres/JSON) for idempotence, coupled with an interactive LLM reasoning core for market gap synthesis and milestone breakdown (R1.7 separation).

## 1.2 Library Search Results
- Searched `00_project/knowledge/workflow-library/` for `goal`, `roadmap`, `benchmark`, `eval`.
- Key Patterns identified:
  - `official-docs/claude-code/goal.md`: Harness design for long-running goal tracking with strict termination conditions and checkpoint validation.
  - `blog/projects-redesigned.md`: Persistent state decoupled from transient conversation memory.
  - `_derived/patterns.md` §4.1: Sequential workflow with strict gates (Collect -> Research -> Draft -> Validate -> Checkpoint -> Deliver).

## 1.3 Library Freshness Check
- Library indexed on: 2026-10-11.
- Freshness status: Active (< 1 week old, well within the 6-week freshness ceiling).
- Next scheduled refresh: 2026-11-22.

## 1.4 Existing 741 Asset Coverage & Reuse
- `00_project/workflow-architecture.md` (v1.0 approved 2026-10-16): Establishes the 8-phase client journey ($P_0 \to P_7$), universal `_run.json` telemetry, and invariant `public.client_goals` error sensor.
- `00_project/morning-grill-goals.json`: Contains top-level `quarter_goal`, `goal_numbers`, `leading` metrics, and `next_milestone`. The new `roadmap` workflow extends this by decomposing high-level quarter targets into operational intermediate milestones ($M_1 \to M_4$) grounded in technical audits and market benchmarks.
- `00_project/assets/<client>/`: Dedicated directory structure where client audits and local `roadmap.json` live.

## 1.5 Synthesis & Architecture Direction
The missing cybernetic link in 741 is not goal definition (which `client_goals` already holds), but **operational milestone decomposition grounded in empirical benchmarks**. When an agent begins work, it must never ask "what code should I fix?", but must ingest the active milestone $M_x$, verify the reality gap against the benchmark, execute within hard constraints, and emit updated telemetry.
