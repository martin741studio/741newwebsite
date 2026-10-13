# D01 — Routines, cloud environments, self-hosted environments (current state)

- Author/org: Anthropic (Claude Code docs)
- Type: official docs (living pages; routines are in research preview)
- Publish date: living docs, no fixed date. Counted as current on fetch date.
- URLs: https://code.claude.com/docs/en/routines , https://code.claude.com/docs/en/cloud-environments , https://code.claude.com/docs/en/self-hosted-environments
- Fetch date: 2026-10-13 (raw markdown via `.md` URL)
- Relation to existing library: updates O1. Only new or changed facts are listed here.

## Extract (own words)

- A routine runs on Anthropic cloud or, when routed there, on an organization's self-hosted environment. It keeps running with the laptop closed.
- Self-hosted environments (runners on your own server) are public beta for **Team and Enterprise only**, off by default. Pro and Max users are pointed to Remote Control on an always-on machine instead.
- Minimum schedule interval is still one hour. Cron expressions that fire more often are rejected.
- Current hourly limits: 100 scheduled runs per hour per account (over the limit the run waits). Run now + API fires + re-runs: 30 per hour per routine, 100 per hour per account. API fires: 100 per hour per account. GitHub events have per-routine and per-account hourly caps; extra events are dropped. No daily run cap appears in the current doc.
- Subscription limit hit: with usage credits on, routines continue on metered overage. Without usage credits, further runs are rejected until the window resets. A paused subscription puts routines on hold.
- No permission picker. The run uses every tool of every included connector, writes included, without asking (some artifact actions excepted).
- Local MCP servers from `claude mcp add` are not available. Use claude.ai connectors or a committed `.mcp.json` (single-repo routines). Your local files are not available; each run clones GitHub repos fresh.
- Default network is "Trusted": an allowlist of package registries and dev domains. Other hosts get 403 `host_not_allowed`. Connector traffic goes through Anthropic and needs no allowlist entry.
- On Pro and Max, API keys belong in "network secrets": they stay outside the sandbox and are attached to matching requests. Plain environment variables are visible to anyone who uses the environment.
- `/schedule why did my nightly review do nothing` lets Claude read a routine's run log (needs v2.1.227+). A green status still only means "no infrastructure error".

## IF/THEN rules for 741

1. IF a night task needs local files, local scripts or a local MCP server (Novamira, Control_Chrome, local Python), THEN it cannot run as a routine. Move the inputs to a GitHub repo or a claude.ai connector first, or run it on a machine you control.
2. IF a routine must call an outside API (DataForSEO, Supabase, WordPress REST), THEN add the host to a Custom network allowlist and store the key as a network secret, not as a plain variable.
3. IF Martin plans a "self-hosted runner" on a VPS, THEN note that this needs a Team or Enterprise plan. On Max, the server path is Remote Control or headless `claude -p`.
4. IF routines are the night engine, THEN decide in advance if usage credits may run at night. Without them, runs are rejected once the plan limit is hit.

## Limits / caveats

- Research preview. Limits and API may change. Re-check before building.
- Older launch reports (April 2026) mention daily caps of 5/15/25 runs by plan. The current doc shows only hourly caps. Treat the daily caps as superseded unless the doc shows them again.
