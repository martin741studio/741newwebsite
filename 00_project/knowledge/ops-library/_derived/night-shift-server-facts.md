# Night shift with server autonomy: verified tool facts

All facts come from the official docs and help pages as fetched on 2026-10-13. These are living pages. Check them again before you build. Source ids refer to `sources/night-shift-server-*.md`. Earlier facts are in `claude-tooling-facts.md` (O1–O6).

## 1. Where an unattended run can live

| Option | Runs with Mac off | Local 741 files / local MCP | Phone approvals | Auth | Cost driver | Source |
|---|---|---|---|---|---|---|
| Cloud routine | Yes | No. Only a GitHub clone, claude.ai connectors, or a committed `.mcp.json` | No. It has no permission picker and runs fully autonomously | claude.ai plan | Plan usage. Usage credits can cover overage | D01 |
| Cloud session (claude.ai/code, `claude --cloud`) | Yes | No. User `~/.claude` skills, CLAUDE.md and user MCP do not carry over | Yes, in the app while the session lives. Idle VMs are reclaimed | claude.ai plan | Plan usage | D02 |
| Self-hosted cloud environment (runner on own server) | Yes | Runner host tools | As cloud session | Team or Enterprise only | Org usage | D01 |
| Remote Control server on own machine (VPS or Mac mini) | Yes, if the machine is not the MacBook | Yes, on that machine | Yes. App plus push | Full claude.ai login only. No API key, no setup-token | Plan usage + server | D03 |
| Headless `claude -p` on a VPS (cron, systemd, tmux) | Yes | Yes, on that machine | Not by itself. Needs a channel relay or hook push | setup-token (plan) or API key | Plan usage, or API (Max API credits) | D04, D05, D06 |
| Channels session (Telegram) on own machine | Yes | Yes | Yes. Permission relay, first answer wins | claude.ai login or Console API key | Plan or API | D09 |
| Managed Agents (API) | Yes | No. Anthropic or self-hosted sandbox | `always_ask` pauses the session until your app confirms | API key | Tokens + $0.08 per running session-hour | D07 |
| GitHub Actions (`claude-code-action@v1`) | Yes | Repo only | No | API key or `CLAUDE_CODE_OAUTH_TOKEN` | GitHub minutes + tokens or plan | D04 |

## 2. Fact table

| Fact | Value | Source | Fetch date |
|---|---|---|---|
| Routine minimum interval | 1 hour. Faster cron expressions are rejected | D01 | 2026-10-13 |
| Routine scheduled-run cap | 100 per hour per account. Over the cap the run waits | D01 | 2026-10-13 |
| Routine Run now / API / re-run cap | 30 per hour per routine (shared). 100 per hour per account for Run now. 100 per hour per account for API fires | D01 | 2026-10-13 |
| Routine daily run cap | None in the current doc. Launch-era reports of 5/15/25 per day are not in the doc | D01 | 2026-10-13 |
| Routine at plan limit | Continues on metered overage only if usage credits are on. Otherwise runs are rejected until reset | D01 | 2026-10-13 |
| Routines and local MCP / local files | Not available. Use claude.ai connectors or a committed `.mcp.json`. Each run clones the repo fresh | D01 | 2026-10-13 |
| Routine network default | "Trusted" allowlist. Other hosts get 403 `host_not_allowed`. Connectors bypass the allowlist | D01 | 2026-10-13 |
| Secrets in cloud runs (Pro/Max) | "Network secrets" stay outside the sandbox. Plain env vars are visible to anyone who uses the environment | D01, D02 | 2026-10-13 |
| Self-hosted environments | Public beta, Team and Enterprise only, off by default | D01 | 2026-10-13 |
| Cloud session VM | Ubuntu 24.04 x86_64, 4 vCPU, 16 GB RAM, 30 GB disk | D02 | 2026-10-13 |
| Cloud session command timeout | 2 min default, up to 10 min on request. Setup script cached if done in about 5 min | D02 | 2026-10-13 |
| Cloud session idle | Stops after inactivity. Waiting for an MCP approval counts as idle. Conversation restored, background work not restored | D02 | 2026-10-13 |
| Cloud session permission modes | Picked per session. `dontAsk` and `bypassPermissions` set in settings files are ignored | D02, D08 | 2026-10-13 |
| Remote Control: machine on? | Yes. The machine must stay on and the `claude` process must keep running. Use tmux or screen on a remote machine | D03 | 2026-10-13 |
| Remote Control auth | Pro, Max, Team or Enterprise with a full claude.ai login. API keys and setup-token tokens fail | D03, D05 | 2026-10-13 |
| Remote Control server capacity | 32 concurrent sessions by default (`--capacity`). `--spawn worktree` isolates sessions | D03 | 2026-10-13 |
| Remote Control network loss | Server mode exits after about 10 min offline. An interactive session retries without end | D03 | 2026-10-13 |
| Remote Control resume window | About 4 hours after the server stopped (`claude remote-control`, `--continue`, `--session-id`) | D03 | 2026-10-13 |
| Phone push | Only while Remote Control is active. Two `/config` toggles. No per-event setup | D03 | 2026-10-13 |
| Forwarded dialogs | Permission prompts and AskUserQuestion wait until answered. Other dialogs close after 5 min (`dialogExpiry`) | D03 | 2026-10-13 |
| setup-token validity | One year. Not saved by the command. Set it as `CLAUDE_CODE_OAUTH_TOKEN` | D05 | 2026-10-13 |
| setup-token scope | Model requests only. No Remote Control, no claude.ai connectors, no Chrome integration. Local MCP works. `--bare` ignores it | D05, D10 | 2026-10-13 |
| setup-token allowed use | Documented for CI pipelines and scripts. Needs Pro, Max, Team or Enterprise. The OAuth login is for "ordinary use" by the plan purchaser, and logins must not be shared | D05 | 2026-10-13 |
| Auth precedence | Cloud provider > `ANTHROPIC_AUTH_TOKEN` > `ANTHROPIC_API_KEY` > `apiKeyHelper` > `CLAUDE_CODE_OAUTH_TOKEN` > profile > `/login` | D05 | 2026-10-13 |
| `--max-turns` | Exists. Print mode only. Errors out at the cap. No limit by default | D04 | 2026-10-13 |
| `--max-budget-usd` | Exists. Print mode only. Uses the client-side estimate, so spend can pass the cap. Subagents count. At the cap new subagents fail (v2.1.217+) | D04 | 2026-10-13 |
| `--permission-mode` values | `default`/`manual`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions` | D04 | 2026-10-13 |
| `--permission-prompts none` | Denies prompts nobody can answer in `-p` (v2.1.259+) | D04 | 2026-10-13 |
| `--allowedTools` / `--disallowedTools` | Rule syntax, e.g. `Bash(git diff *)`. Deny rules apply in every mode | D04, D08 | 2026-10-13 |
| `--bare` | Skips CLAUDE.md, hooks, skills, plugins, MCP discovery. Needs an API key or `apiKeyHelper` | D04 | 2026-10-13 |
| JSON cost output | `--output-format json` returns `total_cost_usd` and `session_id` | D04 | 2026-10-13 |
| Capacity retry | `CLAUDE_CODE_RETRY_WATCHDOG=1` retries 429/529 without end. A spend-limit 429 still fails at once | D04 | 2026-10-13 |
| Plan limits | 5-hour session limit + weekly limit (Max: plus a weekly Fable limit). One pool for Claude, Claude Code and Desktop. The weekly reset is at a fixed account time | D06 | 2026-10-13 |
| Limit hit mid-run | Requests are blocked until the reset time shown. A model switch does not help for session or weekly limits. An interactive CLI can auto-continue after reset. `-p` runs fail | D06 | 2026-10-13 |
| Usage credits | Pay-as-you-go at API rates past plan limits, up to a monthly spend cap. Prepaid, optional auto-reload | D06 | 2026-10-13 |
| Max monthly API credits (new 7 Oct 2026) | Max 5x $100, Max 20x $200 per month in one linked Console org. Claim after 7 days on the plan. No rollover. Requests stop when the credit is gone and no purchased credits exist | D06 | 2026-10-13 |
| What API credits cover | Claude API, Batches, Managed Agents, Agent SDK, and `claude -p` only when run with that org's API key. Not interactive Claude Code, not GitHub Action runs, not extra usage | D06 | 2026-10-13 |
| `claude -p` on plan login | Still draws from plan limits. The June "Agent SDK credit" was paused and is not available | D06 | 2026-10-13 |
| Managed Agents pricing | Tokens at API rates + $0.08 per session-hour while `running`. Idle time is free. Web search $10 per 1,000 | D07 | 2026-10-13 |
| Managed Agents budget | Optional hard USD cap per session at list rates. Goes idle at the cap. Can land slightly over | D07 | 2026-10-13 |
| Managed Agents approvals | `always_ask` pauses and waits without end. MCP toolsets default to `always_ask`, built-in tools to `always_allow`. `auto` lets the server decide | D07 | 2026-10-13 |
| Managed Agents schedules | Cron + IANA timezone, minute granularity. Jitter up to 15% of the interval (5 s to 9 min). Max 1,000 deployments per org | D07 | 2026-10-13 |
| Managed Agents data | Not eligible for ZDR or HIPAA BAA | D07 | 2026-10-13 |
| Auto mode fallback | 3 blocks in a row or 20 in total pause auto mode (fixed). In `-p` the action is skipped and the run continues | D08 | 2026-10-13 |
| Bypass mode | Refuses root/sudo on Linux and macOS. Only for isolated containers or VMs. No protection against prompt injection | D08 | 2026-10-13 |
| Bash sandbox | Off by default. macOS Seatbelt; Linux bubblewrap + socat. Network allowlist starts empty. File tools, MCP and hooks run outside it | D08 | 2026-10-13 |
| Channels auth | claude.ai login or Console API key. Research preview | D09 | 2026-10-13 |
| Permission relay | Tool approvals (Bash, Write, Edit) go in parallel to the phone. The first answer wins. Reply `yes <id>` / `no <id>`. Trust and MCP consent do not relay | D09 | 2026-10-13 |
| Claude in Chrome on a server | Needs a visible Chrome window and a full `/login`. Off with API key or setup-token. Not in WSL. Pauses at logins and CAPTCHAs | D10 | 2026-10-13 |
| Playwright MCP headless | `--headless`. Persistent profile by default (`--user-data-dir`). `--isolated` / `--storage-state` for parallel or clean runs. Headless idle timeout 1 h | D10 | 2026-10-13 |
| GitHub Actions auth | `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN`. A cron `schedule:` works. Use `--max-turns`, workflow timeout and concurrency | D04 | 2026-10-13 |

## 3. Third-party figures (not official, check before use)

| Figure | Value | Source | Date of source |
|---|---|---|---|
| VPS minimum | 4 GB RAM. About 512 MB free for the installer. Add swap on small boxes | N01 | 2026-10-02 |
| VPS prices (Sept 2026) | Vultr 4 GB $20/mo; DigitalOcean $24/mo; Hetzner CPX22 EUR 19.99/mo; Contabo 8 GB about EUR 5.50/mo (24-month term); MacStadium Mac mini from $109/mo | N03 | 2026-09-06 |
| ntfy / Pushover | ntfy free, the topic name acts as the password. Pushover $4.99 one-time per platform, 10,000 messages a month | N02 | 2026-10-02 |
| Safe default headless line | `claude --bare -p ... --permission-mode dontAsk --allowedTools ... --max-turns 15 --max-budget-usd 3 --output-format json` | N04 | 2026-09-24 |

## 4. Bottom line for Martin (Max plan, Bali, DACH clients)

- **No server at all:** cloud routines, cloud sessions and Managed Agents run with the MacBook closed. None of them can read the local 741 repo or local MCP servers. Inputs must be in GitHub or connectors.
- **Own server with phone cards:** Remote Control in server mode on a VPS or Mac mini, under tmux or a service, with Martin's full login. Push and approvals reach the Claude app. The server must stay online.
- **Own server, scripted jobs:** `claude -p` with an API key from the Console org that gets the Max API credit ($100 or $200 a month). The night shift then does not use Martin's daytime plan limits. Phone approvals then need a Telegram channel with permission relay, or Managed Agents `always_ask`.
- **Browser jobs:** Claude in Chrome needs a machine with a desktop and a full login. Use Playwright MCP headless for everything that does not need Martin's Google sessions.
