# V05 — Getting started with Claude Managed Agents

- Channel: CJ Avilla (cjav_dev)
- URL: https://www.youtube.com/watch?v=g1QfVjyrWzg
- Type: console walkthrough, 6m 55s
- Upload date: 2026-10-07
- Views: 24,105 (at fetch)
- Fetch date: 2026-10-13 (Apify discovery + `johnvc/YoutubeTranscripts`, dataset `jkrUikamYc0lfnl76`. Raw transcript not stored here.)
- Related, not filed separately: Anthropic workshop "Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4)", AI Engineer channel, 2026-10-12, 7,889 views, https://www.youtube.com/watch?v=Uv0nAf_7tyU. Points from it are marked [AE].

## Extract (own words)

1. Managed Agents run on Anthropic's servers through platform.claude.com. He says Max and Team plans can now use their credits for platform features. (Check this against the live billing docs.)
2. An agent is a saved, versioned config: name, description, model, effort, system prompt, tools, metadata (YAML). Each save makes a new version, and you can roll back.
3. An environment sets the sandbox network: unrestricted, or an allowlist of domains.
4. A session is one unit of work. Sessions can start from the console, an API call, a webhook or a cron schedule.
5. Built-in tools: bash, read, write, edit, file search, web search, web fetch. MCP servers (example: Google Drive) and skills (example: a brand-voice skill) can be added.
6. Vault: credentials sit in a vault and are swapped in at the network exit. The agent never sees the key. [AE] The Anthropic engineers say a proxy injects tokens so a prompt injection cannot make Claude print them.
7. Budget per session: he sets a spend cap ("no more than $5").
8. Deployments schedule runs on a cron basis (example: a daily social-media brief).
9. Memory stores let sessions write notes and later sessions mount them.
10. The dashboard shows every event: tool calls, files read and written, threads. Sub-agents can be added for multi-agent work.
11. [AE] Each session keeps an append-only event log. If the harness or the sandbox dies, a new one resumes from the last event. Each task runs in its own container to limit the blast radius.

Short quote: "your agent never actually has access to your keys"

## Setup details

- Host: Anthropic cloud (Claude Console). No server to run.
- Cost: API credits (or plan credits, per his claim). Per-session budget cap in the UI.
- Tools: Console quick start, agent YAML, environments, vaults, MCP servers, skills, deployments (cron), memory stores. API objects [AE]: environments, agents, sessions, events.

## IF/THEN rules for 741

1. IF a night job must run with no Mac and needs an API key (DataForSEO, Local Falcon, Supabase), THEN Managed Agents with a vault is safer than a routine or a VPS, because the key never enters the agent context.
2. IF a night agent runs on Managed Agents, THEN set a per-session budget cap and a domain allowlist in the environment.
3. IF the same night job runs for many clients, THEN use one session per client so one bad run cannot touch another client's data.
4. IF a night agent must remember yesterday's state, THEN use a memory store or the portal database, not a long chat.

## Caveats

- Short demo with a toy task (Paris travel research). No production numbers.
- The Max/Team credit claim is the creator's statement. Not checked against billing docs here.
- Platform features are new and may change. Re-check before building.
