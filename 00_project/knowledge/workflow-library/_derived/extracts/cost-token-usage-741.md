# Token cost: what the docs say, and where 741's own spend actually goes

Checked 2026-10-15. Source docs fetched fresh: `official-docs/claude-code/costs.md`, `model-config.md`, `statusline.md` (all living pages, current as of fetch). Also `sub-agents.md`, `agent-teams.md` (already in the library, re-read for this check).

## What drives cost, per the official docs

1. **Context size, not model tier, is the main driver.** Claude Code resends the whole conversation on every turn. A cheap model with a big context still costs real money.
2. **Scheduled tasks and cross-session messages both resend full context on every fire**, even while the session is idle. This is named explicitly as a top cause of climbing usage.
3. **Subagents and dynamic workflows each carry their own request stream** on top of the main conversation. Attribution is visible in `/usage`.
4. **Model choice**: Sonnet for most tasks, Haiku for simple/mechanical subagent tasks (`model: haiku` in a subagent definition, or `CLAUDE_CODE_SUBAGENT_MODEL=haiku` to force it fleet-wide), Opus only for hard reasoning.
5. **Prompt caching** already runs automatically; a cache miss (session idle past the TTL, or CLAUDE.md/hooks changed) reprocesses full context at full price.

## Where 741's spend is actually going (checked directly, not guessed)

- **`reporting/night-shift-v2/server/health_check.py:74`** calls `claude -p "Reply with exactly: OK" --model claude-sonnet-5` every 10 minutes via a systemd timer. The prompt is trivial, but every `claude -p` call still loads the full project context (CLAUDE.md, skills, MCP servers) from cold — this is the exact "every 10 minutes" cost Martin flagged. Fix: `--model claude-haiku-5-5` (or whatever Haiku alias is current) for a liveness ping; it needs zero reasoning.
- **No `crossSessionInbound` setting anywhere in `.claude/settings*.json` or `~/.claude/settings.json`.** Every cross-session message and task-notification delivered to an idle session starts a new full-context turn at full price. This chat alone processed dozens of these in one day. Default is to deliver immediately; `hold` queues them instead.
- **No `CLAUDE_CODE_SUBAGENT_MODEL` or per-agent `model:` override set.** Every subagent this session spawned ran on whatever the parent session's model was (Sonnet 5, confirmed not a frontier/Opus model — matches "not even using frontier models"), but several ran 150k-340k tokens each doing heavy multi-step research/build work. Sonnet is the right call for building; Haiku would be enough for the `Explore`-type read-only steps inside those builds.
- **No `modelPricing` set.** Not a cost lever, just means `/usage` and the status line show list price, not Martin's real contracted rate if one exists.

## What "other providers, way cheaper" usually means elsewhere (industry pattern, grounded)

Teams outside Anthropic's own docs commonly run a **cascade/router**: a cheap, fast model (Haiku, or a non-Anthropic small model behind a gateway like LiteLLM — unaffiliated with Anthropic, open source, mentioned in `costs.md` as a third-party option) handles the trivial 90% of calls (liveness pings, classification, simple reads), and only escalates to a frontier model when the cheap pass flags something that needs real reasoning. This is exactly the shape `health_check.py` should already follow (Haiku ping, escalate to Sonnet/Opus only on a real failure) but currently doesn't.

## Recommendation (not yet applied — Martin's go per workflow)

1. Switch `health_check.py`'s liveness ping to Haiku. Cuts that specific 10-minute cost without losing the check (a dead server fails the call regardless of model).
2. Set `crossSessionInbound: hold` (or review per-session) so idle sessions don't eat a full-context turn per notification — batches them instead.
3. Set `CLAUDE_CODE_SUBAGENT_MODEL` default to Haiku, with explicit `model: sonnet` only where a build genuinely needs it (matches the official guidance: "Use Sonnet for teammates… for simple subagent tasks, specify model: haiku").
4. Turn on `/usage` tracking as a standing habit (or a status line) so this doesn't need a cold investigation next time.
