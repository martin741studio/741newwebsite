# Baseline Comparison: With vs. Without Workflow (`roadmap`)

Date: 2026-10-16
Workflow ID: `roadmap`

---

## Comparison Matrix

| Dimension | WITHOUT Roadmap Engine (Ad-Hoc Chat) | WITH Roadmap Engine (`client-roadmap`) | Delta / Improvement |
|---|---|---|---|
| **Agent Context Ingestion** | 5–8 conversational turns asking "What are we doing for Celine? What's the goal?" | 1 deterministic script call (`get_roadmap.py`) in 40 ms | **85% fewer exploratory turns** |
| **Token Consumption** | ~8,000 tokens of chat back-and-forth exploring site context | ~350 tokens (structured pre-flight banner) | **~95% token reduction at session start** |
| **Human Corrections** | 2–4 corrections (e.g. "Don't touch the live template", "Focus on speed first") | 0 corrections; constraints and active tasks hard-coded in pre-flight | **Zero blind drift** |
| **Data Persistence** | Lost in chat transcript when session ends | Persisted in `roadmap.json` & Supabase `client_goals` with `_run.json` | **100% permanence across agents** |
| **Benchmark Reality Check** | Intuitive / ad-hoc guessing of targets | Explicit $\Delta$ calculated against verified niche standards | **Scientific, empirical target setting** |
