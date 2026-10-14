# N01 — Claude Code official changelog (Oct 2026 entries)

- Org/author: Anthropic
- Type: official docs (living changelog page)
- Publish date: living page; entries read are dated 2026-10-06 through 2026-10-14 (versions 2.1.292–2.1.300). Verified by the dates printed next to each entry.
- URL: https://code.claude.com/docs/en/changelog.md
- Fetch date: 2026-10-15

## Extract (own words)

- 2.1.295 (Oct 8) added `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS` to cap how long unattended retry mode waits out 429/529 errors. 2.1.296 and 2.1.292 added matching backoff-delay env vars for overloaded (529) retries.
- 2.1.300 (Oct 14) fixed `claude remote-control` giving up on reconnecting after a brief sign-in error (example given: a locked keychain); it now retries and tells the user to run `claude /login` instead of just dying.
- 2.1.293 (Oct 7) fixed `claude logs`, `stop`, `kill`, `rm` and the daemon's own stop/status/uninstall commands sometimes signing the user out when the login had merely expired or was about to.
- 2.1.300 fixed Remote Control sessions being wrongly marked "stopped" while still running, on a machine serving several sessions at once.
- 2.1.299 (Oct 14) fixed a bug where a mod that submits a prompt at the end of every turn could keep a headless run going past `--max-turns`, `--max-budget-usd`, an interrupt, or the end of the conversation — i.e. those caps were not airtight before this fix.
- 2.1.299 fixed `claude -p` printing nothing when a settings file fails validation; it now prints the bad file and entry to stderr instead of failing silently.
- 2.1.295 fixed remote MCP servers in headless/SDK sessions staying disconnected after an outage longer than 15 seconds (now backs off and retries up to 30s).
- 2.1.299 fixed scheduled wakeups (`ScheduleWakeup`) not firing while a background task was already running, in Agent SDK, IDE and `claude remote-control` sessions — a silent-skip failure mode for recurring jobs.
- 2.1.295 changed `claude agents` behaviour so that stopping the background service also stops running sessions within about a minute, instead of leaving them orphaned.
- 2.1.299/2.1.293 fixed two separate memory leaks that matter for a server left running for days: unbounded memory growth under heavy `--debug` logging, and an HTTP MCP connection retaining every request it ever sent until the connection closed.
- No entry found for `--permission-prompts none` in the visible (Oct-only) window — it was added earlier (confirmed via N04, a third-party summary of the Sept 2 release).

## IF/THEN rules for 741

1. IF 741-agents-01 runs `claude -p` or Remote Control unattended for multiple days, THEN pin and re-check the Claude Code version regularly — multiple fixes landed in a single week (Oct 6–14, 2026) for exactly the failure modes the night shift depends on (retry backoff, remote-control reconnect, scheduled-wakeup misses, memory leaks).
2. IF the night-shift-v2 runner relies on `--max-turns` / `--max-budget-usd` as a hard ceiling, THEN know that as late as 2.1.299 there was a documented bug where a self-resubmitting mod could blow past both caps — treat them as a strong deterrent, not a provable hard stop, and keep an external wall-clock timeout (`timeout`/systemd `RuntimeMaxSec`) as the real backstop.
3. IF the server runs `claude agents` background sessions or `/loop` across a process restart, THEN expect scheduled wakeups to have silently failed to fire in some 2.1.x versions while a background task was already running — add a heartbeat check (see N07) rather than trusting "it should have run."
4. IF `claude logs/stop/kill/rm` or daemon subcommands are used in health scripts, THEN don't treat an unexpected sign-out from those commands alone as proof the token is dead — 2.1.293 fixed a case where a merely-expiring (not dead) token caused exactly that signal.

## Caveats

- The fetched page is 1,095,374 characters and this extract covers only characters 0–100,000 (the most recent entries); July–September entries were not read from this page directly (see N02–N04 for that window via third-party summaries and bug trackers).
- "Living page" means the content is current as of fetch date, consistent with how O1–O6 in the base ops-library were treated.
