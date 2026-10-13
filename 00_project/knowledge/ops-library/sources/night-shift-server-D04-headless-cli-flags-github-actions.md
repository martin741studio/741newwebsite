# D04 — Headless `claude -p`, CLI flags, GitHub Actions

- Author/org: Anthropic (Claude Code docs)
- Type: official docs (living pages)
- Publish date: living docs, counted as current on fetch date
- URLs: https://code.claude.com/docs/en/headless , https://code.claude.com/docs/en/cli-reference , https://code.claude.com/docs/en/github-actions
- Fetch date: 2026-10-13

## Extract (own words)

- `claude -p` runs one prompt and exits. Exit code 0 means success.
- `--max-turns N`: caps agent turns in print mode and exits with an error at the cap. No limit by default.
- `--max-budget-usd X`: stops the run when the client-side cost estimate reaches X (print mode only). Spend can pass the cap, so leave headroom. Subagent spend counts. At the cap, new subagents fail with "Budget limit reached" (v2.1.217+).
- `--permission-mode` accepts `default` (alias `manual`), `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`. `--permission-prompts none` (v2.1.259+) denies prompts that nobody can answer. Example from the doc: `--permission-mode auto --permission-prompts none`.
- `--allowedTools` pre-approves tools with rule syntax, e.g. `Bash(git diff *)`. `--disallowedTools` removes or denies tools.
- `--output-format json` returns `total_cost_usd`, a per-model breakdown and `session_id`. With stream-json, denials show as `permission_denied` events.
- `--bare` skips CLAUDE.md, hooks, skills, plugins, MCP auto-discovery. Recommended for scripts and planned as the future `-p` default. Bare mode does not read `CLAUDE_CODE_OAUTH_TOKEN`; it needs `ANTHROPIC_API_KEY` or `apiKeyHelper`.
- Without `--bare`, a `-p` run in an untrusted folder runs that repo's hooks and `.mcp.json` servers with no trust prompt.
- `--fallback-model` lists models to try when the main one is overloaded. `CLAUDE_CODE_RETRY_WATCHDOG=1` retries 429/529 capacity errors without end in unattended runs, but a spend-limit or usage-credit 429 still fails at once.
- GitHub Actions: `anthropics/claude-code-action@v1`. Auth with `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`). A `schedule:` cron trigger works in automation mode. Costs = GitHub Actions minutes + tokens (or plan usage with the OAuth token). Doc advice: `--max-turns` in `claude_args`, workflow timeouts, concurrency controls.

## IF/THEN rules for 741

1. IF a night job runs via `claude -p`, THEN always pass `--max-turns`, `--max-budget-usd` (only meaningful with an API key), an explicit `--permission-mode` and `--output-format json`, and write the JSON to a dated log file.
2. IF the job must never ask, THEN use `--permission-mode dontAsk` with an exact `--allowedTools` list, or `auto` with `--permission-prompts none`.
3. IF the job runs in a client repo Martin did not write, THEN use `--bare` with an API key, so foreign hooks and MCP servers do not run.
4. IF a scheduled job lives in GitHub Actions, THEN set `timeout-minutes` and a concurrency group in the workflow, and `--max-turns` in `claude_args`.

## Limits / caveats

- `--max-budget-usd` is an estimate, not billing. On a subscription it caps estimated value, not real money.
- Default permission mode for `-p` is `default` in sessions that fetch feature flags; nobody answers prompts unless you set a mode.
