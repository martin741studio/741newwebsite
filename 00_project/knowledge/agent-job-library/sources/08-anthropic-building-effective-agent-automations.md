# 08 — Anthropic: "Building effective agent automations" (scheduled agents, preferences vs state)

Type: engineering blog, 2026. Local copy: `00_project/knowledge/workflow-library/blog/building-effective-agent-automations.md` (already in the workflow library, not duplicated here).

## Key content for job design
- An automation is a configuration file (agent.md) plus a deployment (schedule, time zone, budget, input message, vault, memory stores).
- Two memory stores: `preferences` (the owner's, read-only to the agent, re-read every run) and `state` (the agent's own: bookmarks, ledger, run records, proposals, notes on source behaviour). "If it can't read the file, it should stop and say so instead of running on defaults."
- Read sources from a bookmark per source, never a fixed window.
- A failed source is reported as unreadable ("pull requests unavailable this run"), never as "nothing new".
- A post counts as sent only after the destination confirms it; ledger and bookmarks update only after that; unclear result = "maybe posted", change nothing.
- Re-check every item right before posting; assert or drop, never hedge.
- Read-only credentials wherever the agent only reads; spend cap per run (start 3–5× a normal run); a capped run pauses, it does not fail.
- Prompt injection: the agent reads text others wrote; limit what it could do if it obeyed it (read-only token, read-only preferences, host allowlist).
- "Proposals" to the owner's preferences are written to state, never applied by the agent.

## Assessment for 741
New vs. video: the preferences/state split is the mechanism behind "a manager"; Tyler's "remember this" is memory with no owner boundary. The ledger + bookmark pattern is the anti-drift tool Tyler lacks. The "propose changes to preferences, never apply" rule is exactly the job-description change control 741 needs.
Marketing: Managed Agents product; the mechanics transfer to any runner.
Usable for 741: every job description is the agent's `preferences` (owned by Martin, agent may propose edits, never apply); every agent keeps a `state` record per run (what it did, what it could not read, what waits for approval); the weekly review reads the state records, not the agent's memory of itself.
