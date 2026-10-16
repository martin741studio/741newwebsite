# 4.3 Baseline Comparison: P6 Proof Tracking (`tracking`)

Date: 2026-10-16
Workflow: Proof Tracking + Quarterly War Room (`tracking`)

---

| Metric / Dimension | Without Tracking Skill (Ad-Hoc) | With Tracking Skill & Scripts | Improvement |
|---|---|---|---|
| **Operator Time per Client** | 45–60 minutes per week (manual login to Falcon, GSC, Stripe, spreadsheet) | 3–5 minutes (run script, inspect draft, record Loom) | **~90% reduction in operator time** |
| **Math Accuracy** | Occasional manual calculation errors in WoW deltas and CPA math | 100% deterministic calculation in `compute_weekly_metrics.py` | **Zero math errors** |
| **Early Warning Latency** | Days or weeks (issues noticed only during monthly reviews) | Automated daily rule check (R1–R6, Y1–Y9); same-day alerts | **Zero silent breakages** |
| **Tokens Consumed per Run** | ~14,000 tokens (feeding raw HTML/JSON dumps to LLM to parse numbers) | ~4,200 tokens (clean structured JSON piped to prompt heuristics) | **~70% token savings** |
| **Client Confidence** | Delayed, unstructured text messages | Clear, consistent 3-bullet proof card + 60s Loom video | **High client retention and clarity** |
