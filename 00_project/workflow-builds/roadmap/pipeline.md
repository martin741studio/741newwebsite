# Pipeline & Architecture Specification: Client Roadmap & Goal Engine (`roadmap`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `roadmap`

---

## 1. Architectural Shape (Cybernetic Regulation Loop)

```
[ Ingestion Membrane ]
• Audit crawl: Lighthouse / TTFB / Media size / GSC positions
• Competitor scrape / Niche benchmark baseline
                 │
                 ▼
[ Transformation Core: R1.7 Separation ]
• Deterministic: Gap math (Δ = Baseline - Target), schema validation
• Heuristic: Strategic milestone formulation ($M_1 \to M_4$), task decomposition
                 │
                 ▼
[ Checkpoint 1 (Design Gate) ] ──► Martin Decision Card
                 │ (Approved)
                 ▼
[ Expression & Delivery ]
• Primary: Supabase `public.client_goals`
• Local Mirror: `00_project/assets/<client>/roadmap.json`
• Telemetry: `_run.json` emitted at checkpoint
                 │
                 ▼
[ Sensor Feedback: Pre-Flight Ingestion ]
• Every agent chat session reads active milestone before touching client files
• Discrepancy signals feed Morning Grill & Standup
```

---

## 2. Checkpoints & Gates

| Checkpoint | Gate Requirement | Verification Method | Enforcement |
|---|---|---|---|
| **CP0 (Ingestion)** | Baseline audit and benchmark data verified from authentic source (no estimation). | `inputs-grill.md` & audit log check | Pre-flight validation |
| **CP1 (Design Go)** | Milestone breakdown, North Star Goal, and task sequence approved by Martin. | Interactive Decision Card | Martin explicit Go |
| **CP2 (Telemetry)** | Task completed, verified against acceptance criteria, `_run.json` emitted, `roadmap.json` state updated. | Programmatic check (`check_phase.py`) | Agent verification |

---

## 3. Degrees of Freedom per Step (Rule R1.7)

| Step | Freedom Level | Mechanism | Rationale |
|---|---|---|---|
| **1. Audit Data Ingestion** | Zero (Deterministic) | Python script (`scripts/audit_ingest.py`) | Raw technical metrics (TTFB, bytes, URLs) must be exact and immutable. |
| **2. Gap Calculation** | Zero (Deterministic) | Formula: $\Delta = \text{Client} - \text{Benchmark}$ | Math operations must not hallucinate. |
| **3. Milestone Synthesis** | High (Heuristic) | LLM prompt guided by 741 Phase Rules ($P_0 \to P_6$) | Creative agency judgment required to sequence business priorities cleanly. |
| **4. Martin Approval** | Zero (Human Gate) | Decision Card (`ask_question`) | Strategic agency direction requires Martin's explicit Go. |
| **5. Storage & Persistence** | Zero (Deterministic) | JSON validation & Supabase UPSERT | Schema integrity must be 100% predictable and idempotent. |
| **6. Pre-Flight Reading** | Zero (Deterministic) | Script / Hook reading `roadmap.json` | Agent orientation must be reliable across all chat sessions. |
