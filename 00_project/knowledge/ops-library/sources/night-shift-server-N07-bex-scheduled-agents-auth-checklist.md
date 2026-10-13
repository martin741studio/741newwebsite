# N07 — No Human Typed This Deploy: what cron-triggered Claude agents demand from your auth

- Author/org: bex.co (open-source deploy platform; blog)
- Type: technical article / checklist
- Publish date: 2026-09-07 (from the URL path `/blog/2026/09/07/`; no date in page metadata — flagged)
- URL: https://bex.co/blog/2026/09/07/claude-scheduled-deployments-mcp-auth
- Fetch date: 2026-10-13

## Extract (own words)

- Context: Managed Agents scheduled deployments and vaults (public beta since 9 June 2026). A timer, not a person, starts the agent.
- Chat-based work gets three safety properties for free: intent tied to a person and moment, a live login, and a human witness. A cron run has none of them.
- Rule 1: credentials per run, from a vault, short-lived. The model never sees raw secrets.
- Rule 2: no standing production authority. Read-only tools can be always on; any production change needs a per-run grant or a human approval.
- Rule 3: append-only audit trail keyed on the platform's run record, written by the platform, not by the agent.
- Rule 4: limit the blast radius in advance: allowlisted targets, rate limits, auto-pause after repeated failures.
- Rule 5: fail closed on any missing or expired input. No fallback to a broader credential.
- Rule 6: check success through independent status (health check, rollout state), never through the agent's own report.
- Thesis: a scheduled agent is "untrusted input with a valid credential".

## IF/THEN rules for 741

1. IF a night job can write to a client system (WordPress, GBP, ads), THEN it gets no standing write key. It drafts, and the write happens only after Martin's card answer.
2. IF a night job fails three nights in a row (741 value), THEN it pauses itself and becomes one card, not three.
3. IF the morning check says "done", THEN it must quote an independent check (live URL status, portal row), not the agent's summary.

## Limits / caveats

- Written for deploy pipelines. Publish date not in metadata; taken from the URL.
