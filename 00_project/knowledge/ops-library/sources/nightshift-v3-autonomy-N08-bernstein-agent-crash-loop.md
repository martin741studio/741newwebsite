# N08 — Bernstein docs: respawn budget, backoff and "parked" terminal state for a crashing agent process

- Org/author: Bernstein (open-source governance layer for AI agents; per its own page description, no model in the coordination loop, per-task git worktrees, signed lineage, air-gap friendly)
- Type: project/vendor technical documentation
- Publish date: **not shown on the page** — no timestamp, version date, or changelog date visible, only an "edit this page" link. Flagged as an undated exception (same treatment as A13/EOS in the base ops-library): included because it is the single clearest documented formalisation of the exact crash-loop pattern this research was asked to cover, and the project itself (and its docs) appear to be a current, actively maintained one, not an archived artifact.
- URL: https://docs.bernstein.run/en/latest/operations/agent_crash_loop/ (redirected from bernstein.readthedocs.io)
- Fetch date: 2026-10-15

## Extract (own words)

- Default respawn budget: **3 respawns per rolling 60-second window**; the initial spawn does not count against the budget. The window is rolling, so a session that has gone quiet regains budget automatically — no operator action needed for a transient blip.
- Backoff formula: `initial_backoff_ms × attempt`, capped at `max_backoff_ms`. With documented defaults this gives waits of 500ms, 1000ms, 1500ms, and so on up to a 5000ms (5s) ceiling.
- Once the respawn budget in the current window is exhausted, the *next* failure parks the session instead of respawning again:
  - Session is marked parked, with reason `respawn_budget_exhausted`.
  - An `agent.startup_exhausted` event is published (for an operator/monitor to pick up).
  - Any further spawn attempt is refused with `SessionParkedError`.
- Recovery from "parked" is manual and explicit: an operator runs `bernstein agents resume <id>` after fixing the actual root cause — the design deliberately does not auto-resume, on the stated reasoning that a persistent crash loop usually means a real fault (missing binary, bad config, expired token), and the last error should be read before resuming.

## IF/THEN rules for 741

1. IF a 741-agents-01 systemd unit only has `Restart=on-failure` with no burst/backoff limit (the current proven-but-basic state per decisions.md), THEN add the same shape of control: a rolling respawn budget (e.g. systemd's own `StartLimitIntervalSec`/`StartLimitBurst`) plus linear or exponential backoff (`RestartSec`), so a broken agent process degrades to a clearly-flagged stopped state instead of restart-looping silently and burning the night's run budget or API cost.
2. IF a process exhausts its restart budget, THEN don't auto-resume it blind — surface a single, specific, named failure event (mirrors 741's own existing pattern of "needs_martin" cards) with the last error attached, and require an explicit unblock (a Martin go, or a fixed root cause) before it runs again. This matches 741's existing "same blocker 3× → leaves the queue, needs Martin" rule in night-shift-server-workflow.md — the same logic generalised to process-level crashes, not just task-level content blockers.
3. IF 741 wants this exact mechanism rather than hand-rolling it in systemd, THEN Bernstein itself (open-source, AI-agent-specific, git-worktree-based) is a candidate tool to evaluate directly — it already encodes this pattern natively for agent sessions rather than generic services.

## Caveats

- Undated page; treat the specific default numbers (3/60s, 500ms×attempt, 5000ms cap) as illustrative of a sound pattern, not as a verified-current spec — re-check against the live docs before copying numbers into 741's own config.
- Not independently corroborated by a second source; included on the strength of being a precise, concrete, directly-on-topic technical description rather than a vague best-practice claim.
