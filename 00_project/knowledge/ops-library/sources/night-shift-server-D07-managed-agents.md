# D07 — Claude Managed Agents: overview, pricing, budgets, approvals, schedules

- Author/org: Anthropic (Claude Platform docs)
- Type: official docs (living pages; Managed Agents is in beta, header `managed-agents-2026-04-01`)
- Publish date: living docs, counted as current on fetch date
- URLs: https://platform.claude.com/docs/en/managed-agents/overview , https://platform.claude.com/docs/en/about-claude/pricing (section "Claude Managed Agents pricing") , https://platform.claude.com/docs/en/managed-agents/budgets , https://platform.claude.com/docs/en/managed-agents/permission-policies , https://platform.claude.com/docs/en/managed-agents/scheduled-deployments , https://platform.claude.com/docs/en/managed-agents/reference
- Fetch date: 2026-10-13

## Extract (own words)

- Managed Agents is a hosted agent harness. You define an agent (model, system prompt, tools, MCP servers, skills), an environment (Anthropic cloud sandbox or self-hosted sandbox), then start sessions and exchange events over the API. Needs a Claude API key; on by default for all API accounts.
- Built-in tools: bash, file ops, web search and fetch (with domain allow/block lists), MCP servers. Sessions keep files and history server-side and resume after pauses.
- **Pricing:** tokens at normal API rates plus **$0.08 per session-hour**, metered only while status is `running`. Idle time (waiting for a message or a tool confirmation), rescheduling and terminated time are free. Web search $10 per 1,000. No batch discount. US-only inference multiplier 1.1x applies.
- Doc example: 1 hour on Opus 5 with 50k input / 15k output tokens = $0.705; with 40k cached input = $0.525.
- **Budgets:** optional hard dollar cap per session at list rates. At the cap no new model requests start; the in-flight one finishes, so cost can land slightly over. The session then goes idle, not terminated.
- **Permission policies:** `always_allow`, `always_ask` (session pauses and waits indefinitely for your approval), `auto` (server evaluates each call: run, deny, or pause). Built-in tools default to `always_allow`; MCP toolsets default to `always_ask`.
- **Scheduled deployments:** cron expression + IANA timezone, minute granularity. Each firing starts a fresh session with at least one initial event. Jitter up to 15% of the interval (min 5 s, max 9 min). Max 1,000 deployments per organization. Each run writes a platform-side run record (session id or typed error).
- API rate limits: 300 create requests and 1,200 read requests per minute per org.
- Not eligible for Zero Data Retention or HIPAA BAA.
- Max 5x/20x monthly API credits ($100/$200) can pay for Managed Agents (see D06).

## IF/THEN rules for 741

1. IF a night task needs a server but not Martin's Mac files, THEN Managed Agents is the "no server to run" option: cron deployment + budget per session + `always_ask` on write tools.
2. IF a tool call needs Martin's go, THEN set that MCP tool to `always_ask`. The session waits for free (idle is not billed) until his phone app or bot sends the confirmation.
3. IF a deployment runs nightly, THEN set a session budget (e.g. a few dollars, 741 value) and read the platform run record, not the agent's own summary, in the morning check.
4. IF client data is health-related, THEN note that Managed Agents is not ZDR/HIPAA eligible and keep patient data out.

## Limits / caveats

- It is an API product: Martin needs a small app or script (or a bot) to receive events and send approvals. There is no ready phone UI in the docs.
- Beta. Behavior may change between releases.
