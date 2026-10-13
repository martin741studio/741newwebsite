# 1.1 Building block (patterns.md section 3)

Question 1 of the tree: "Does it run on a schedule with nobody present?" Yes.
Candidates: Routine (cloud, repo clone + connectors), Cowork scheduled task (connectors only), Managed Agent (production, vault secrets, budget), plus the existing 741 pattern: skill `night-shift` + bash runner with fresh `claude -p` per item.

Provisional choice (2026-10-13): keep the existing pattern, a skill (`night-shift` v2) driven by a runner script with hook guards (`automation_guard.py`), on a self-hosted Linux box.
Reason: the night work needs `.secrets/` read keys, local scripts (seo-page-optimizer, deslop, DataForSEO wrappers) and the local repo state. Routines and Cowork cannot read `.secrets/` or local MCP servers. A Managed Agent fits the "budget + vault" need, but it means a rebuild on the API and per-token billing.
Final host choice is open: Martin decides it at checkpoint 1 (grill round "Hosting"). If Martin picks Anthropic cloud, the block becomes a Routine with a committed skill.

Final (2026-10-13, decision N1): self-hosted Hetzner VPS Nuremberg. Block = skill `night-shift` v2 + runner + hook guards (not a Routine).
