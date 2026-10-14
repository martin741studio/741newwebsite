# N05 — systemd watchdog pattern (WatchdogSec), via Kubernetes' own use of it

- Org/author: Kubernetes project (official docs)
- Type: official docs, living page
- Publish date: living/evergreen reference; no dated claim made, counted as current on fetch date (consistent with how O1–O6 in the base ops-library treat Anthropic's own living docs).
- URL: https://kubernetes.io/docs/reference/node/systemd-watchdog/
- Fetch date: 2026-10-15

## Extract (own words)

- systemd's watchdog is a different mechanism from `Restart=on-failure`: it catches a process that is still running but has stopped making progress (hung, deadlocked), which a plain process-alive check cannot see.
- Mechanism: the unit file sets `WatchdogSec=<N>`; the running process must call `sd_notify(WATCHDOG=1)` at roughly half that interval or systemd kills and restarts it. `WatchdogSec=0` (or omitted) disables the watchdog entirely for that unit.
- Kubernetes' own kubelet implementation sends its watchdog ping from inside the kubelet's own healthy-loop logic (not a free-running timer), at `WatchdogSec` ÷ 2, and the project's own guidance suggests `WatchdogSec` ≈ 15s for the kubelet.
- Restart behaviour is a separate setting: `Restart=always|on-failure|on-watchdog|on-abnormal` all cause systemd to restart the service; `on-watchdog` specifically restarts on a watchdog timeout (as distinct from an exit-code failure).
- `Type=notify` lets systemd wait for the process's own `READY=1` signal before starting the watchdog clock — relevant for a process with a slow startup (e.g. a headless Chrome + Playwright stack) that shouldn't be killed as "hung" before it has finished booting.
- Pairing matters: a watchdog without `RestartSec` + a start-limit (`StartLimitBurst`) can crash-loop tightly on a permanently broken process; the restart delay and burst limit exist specifically to stop that.

## IF/THEN rules for 741

1. IF a 741-agents-01 systemd unit only has `Restart=on-failure` (current state per decisions.md: proven via a real reboot test), THEN it will restart a crashed process but will NOT catch a hung-but-still-running one (e.g. a `claude -p` run or the persistent `claude remote-control` session stuck waiting on something that never resolves) — that needs a separate `WatchdogSec` + `sd_notify` heartbeat sent from inside the process's own work loop, not a free-running timer thread.
2. IF 741 adds a watchdog to the persistent `claude-remote-control.service` or the batch runner, THEN send the heartbeat after each unit of real work completes (e.g. after each queue item, not on a fixed timer) — a timer-based ping can keep firing while the actual work loop is stuck, defeating the whole point.
3. IF 741 sets a watchdog timeout, THEN pair it with `Restart=on-watchdog` (or `on-failure`) plus an explicit `RestartSec` and `StartLimitBurst`, so a permanently broken agent process parks instead of restart-looping forever and burning run budget.
4. IF a unit (Chrome/Xvfb/noVNC stack, per decisions.md's browser layer) has a slow, variable startup time, THEN use `Type=notify` with its own `READY=1` signal so the watchdog clock doesn't start — and potentially kill it as "hung" — before startup has actually finished.

## Caveats

- No source found specific to AI-agent processes using this pattern; this is the general systemd mechanism applied by inference. 741's own `claude -p` and `claude remote-control` processes would need custom `sd_notify` wiring (e.g. via Python's `sdnotify` package or a wrapper script) since neither tool is documented to emit watchdog pings natively.
