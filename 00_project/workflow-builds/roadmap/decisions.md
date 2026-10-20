# Decision Record: Checkpoint 1 Design Approval (`roadmap`)

Date: 2026-10-16
Workflow ID: `roadmap`
Gate: Checkpoint 1 (Design Approval)
Decision: **APPROVED (GO)**
Approver: Martin Drendel (via Interactive Decision Card)

---

## Summary of Approved Design:
1. **The Job:** Ingests client audits and competitor scrapes, executes a reality gap check against niche benchmarks, and synthesizes an actionable, sequential client roadmap (North Star Goal + 3–4 Milestones $M_1 \to M_4$).
2. **Runtime Surface:** Agent Skill for Antigravity IDE and Claude Code (`/client-roadmap <client>`) backed by dual-storage persistence (Supabase `public.client_goals` + local `00_project/assets/<client>/roadmap.json`).
3. **Pre-Flight Hook:** Every agent chat session touching client assets performs a mandatory pre-flight check to ingest the active milestone and prevent blind drift.
4. **Hard Limits:** Zero unapproved strategic direction changes, zero hallucinated numbers (immutable sources only), zero uncontrolled API burns, strict read-only isolation during roadmap generation.
5. **Next Step:** Implement Layer 3 (Skill folder, scripts, telemetry, and templates).
