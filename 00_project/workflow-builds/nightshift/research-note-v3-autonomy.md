# 1.5 (v3 addendum) — Autonomous-operation research, 2026-10-15

Trigger: Martin's morning-grill ask — the server "noch nicht so wirklich eingerichtet ist, dass es wirklich autonom laufen kann." Full pass: `00_project/knowledge/ops-library/_derived/nightshift-v3-autonomy-facts.md` (11 new sources N01–N11, 26 IF/THEN rules, 6 gap areas). Library freshness checked: workflow-library built 2026-10-11, no refresh due until 2026-11-22.

## The honest finding

741-agents-01 "runs now" but has 3 real production gaps, not cosmetic ones:

1. **No proof of life beyond "systemd says active."** A hung-but-running process passes every check we have today. The reboot test (N43–N47) proved ports came back, not that a real task completes.
2. **No watchdog/respawn discipline.** `Restart=on-failure` catches crashes, not hangs. Nothing caps a crash-loop or parks a dead process with its error attached — it would just loop forever.
3. **No heartbeat into the one alerting system we already have.** Canary already does outage-watch + Telegram escalation for clients. The server itself reports to nobody.

Plus two lower-urgency but real items: a documented history of Claude Code point releases silently breaking unattended permission modes (one did exactly this in July), and Node 22 hits its own maintenance window with Node 24 going Active LTS this week.

## What does NOT need building

- Vault/systemd-creds/secret rotation — current threat model (single operator, Tailscale-only, 600-mode files) doesn't call for it yet; the research explicitly says don't pre-build this.
- A second monitoring stack — canary already exists; bolt onto it, don't duplicate it.
- Any OAuth-retry-loop automation — the evidence says back off and retry the original call, never loop `/login` unattended.

## 4 build items, cheapest first (→ checkpoint 1 options)

1. Dead-man's-switch heartbeat per unit of real work (night-shift batch run, remote-control liveness) → canary's existing Telegram path.
2. `WatchdogSec`/`sd_notify` + bounded respawn-budget/backoff/park on the two processes that matter (batch runner, `claude-remote-control.service`).
3. Mandatory one-task smoke test after every Claude Code version bump (already have a cheap one: `claude -p "OK"` + check exit).
4. A scheduled (not one-off) kill/reboot drill with written failure-mode/abort criteria, pass/pass-with-finding/fail rating.

Plus 2 small hygiene fixes, low effort, do regardless of the above scope decision:
- Switch `--permission-prompts none` in for `dontAsk` in night-shift-v2 (denies instead of hangs); re-run the N28 permission test after.
- Note Node 24 migration on the roadmap (not urgent — EOL for 22.x is 2027-04-30).
