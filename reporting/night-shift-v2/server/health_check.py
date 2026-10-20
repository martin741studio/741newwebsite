#!/usr/bin/env python3
"""741-agents-01 health check (v3 autonomy build, item 2+3).

Proves the server is actually USEFUL, not just that systemd says "active":
runs one real claude -p call with an external wall-clock timeout (research
rule 23: --max-turns/--max-budget-usd alone are not provable), and also
smoke-tests after every Claude Code version bump (rule 6/N02) since a real
point release has silently broken unattended permission handling before.

On success: writes a heartbeat file (consumed by the canary integration,
once wired) and resets the failure counter.
On failure: increments a rolling failure counter. Below the respawn budget,
restarts claude-remote-control.service with backoff. At/above the budget,
PARKS: stops trying, writes a clear marker with the last error, and does
NOT loop forever (research rule 3/N08). A parked state needs a human to
clear it (see unpark()) — this script will not un-park itself.

Run via systemd timer, every 10 minutes: see health-check.timer/.service.
"""
import json, os, subprocess, sys, time, datetime, pathlib

HOME = pathlib.Path.home()
STATE_DIR = HOME / ".browser-display" / "health"
STATE_DIR.mkdir(parents=True, exist_ok=True)
STATE_FILE = STATE_DIR / "state.json"
PARKED_FILE = STATE_DIR / "PARKED"
LOG_FILE = STATE_DIR / "health.log"
HEARTBEAT_FILE = STATE_DIR / "heartbeat.json"

RESPAWN_BUDGET = 3       # consecutive failures allowed before parking
BACKOFF_BASE_SEC = 30    # backoff = BACKOFF_BASE_SEC * attempt, capped below
BACKOFF_CAP_SEC = 300
WALL_CLOCK_TIMEOUT = 60  # external timeout; never trust --max-turns alone (rule 23)
LAST_GOOD_VERSION_FILE = STATE_DIR / "last-good-claude-version.txt"


def log(msg):
    line = f"[{datetime.datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {"consecutive_failures": 0, "last_restart_at": None, "attempt": 0}


def save_state(s):
    STATE_FILE.write_text(json.dumps(s, indent=2))


def claude_version():
    try:
        out = subprocess.run(["/home/nightshift/.local/bin/claude", "--version"], capture_output=True, text=True, timeout=15)
        return out.stdout.strip() or out.stderr.strip()
    except Exception as e:
        return f"unknown ({e})"


def run_real_task():
    """One real, cheap task. Returns (ok, detail). Enforces an EXTERNAL
    wall-clock timeout — rule 23: --max-turns/--max-budget-usd are not
    airtight on their own (a documented bug let a self-resubmitting mod
    blow past both as late as v2.1.299)."""
    env = dict(os.environ)
    env.pop("CLAUDE_CODE_OAUTH_TOKEN", None)  # health check uses no special auth path
    try:
        p = subprocess.run(
            ["/home/nightshift/.local/bin/claude", "-p", "Reply with exactly: OK", "--model", "claude-haiku-5-5",
             "--max-turns", "2", "--output-format", "json", "--permission-mode", "dontAsk",
             "--strict-mcp-config"],
            capture_output=True, text=True, timeout=WALL_CLOCK_TIMEOUT, env=env,
        )
    except subprocess.TimeoutExpired:
        return False, f"wall-clock timeout after {WALL_CLOCK_TIMEOUT}s (external, not --max-turns)"
    if p.returncode != 0:
        return False, f"exit {p.returncode}: {p.stderr[-300:]}"
    try:
        d = json.loads(p.stdout)
    except Exception:
        return False, f"non-JSON output: {p.stdout[-300:]}"
    # rule 26: don't trust a sign-out/exit code alone as proof of token death;
    # check the actual structured result, not just "it exited".
    if d.get("is_error") or d.get("subtype") != "success":
        return False, f"subtype={d.get('subtype')} is_error={d.get('is_error')} result={str(d.get('result'))[:200]}"
    if "OK" not in str(d.get("result", "")):
        return False, f"unexpected result: {str(d.get('result'))[:200]}"
    return True, f"cost=${d.get('total_cost_usd')} version_checked=yes"


def restart_remote_control(attempt):
    backoff = min(BACKOFF_BASE_SEC * attempt, BACKOFF_CAP_SEC)
    log(f"restarting claude-remote-control.service, attempt {attempt}, backoff {backoff}s first")
    time.sleep(backoff)
    subprocess.run(["systemctl", "--user", "restart", "claude-remote-control.service"])


def park(reason):
    PARKED_FILE.write_text(json.dumps({
        "parked_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "reason": reason,
        "unpark": "rm this file after fixing the cause, then re-run health_check.py by hand once to confirm, before re-enabling the timer",
    }, indent=2))
    subprocess.run(["systemctl", "--user", "stop", "claude-remote-control.service"])
    log(f"PARKED: {reason} — claude-remote-control.service stopped, timer will not retry until this file is removed")


def write_heartbeat(ok, detail, version):
    HEARTBEAT_FILE.write_text(json.dumps({
        "ts": datetime.datetime.now().isoformat(timespec="seconds"),
        "ok": ok,
        "detail": detail,
        "claude_version": version,
        "host": "741-agents-01",
    }, indent=2))


def main():
    if PARKED_FILE.exists():
        log("skipped: currently PARKED, remove the marker file to resume")
        return 1

    version = claude_version()
    last_good = LAST_GOOD_VERSION_FILE.read_text().strip() if LAST_GOOD_VERSION_FILE.exists() else None
    version_bumped = last_good is not None and last_good != version
    if version_bumped:
        log(f"Claude Code version changed {last_good} -> {version} — running mandatory smoke test (research rule 6/N02)")

    s = load_state()
    ok, detail = run_real_task()
    write_heartbeat(ok, detail, version)

    if ok:
        if s["consecutive_failures"] > 0:
            log(f"recovered after {s['consecutive_failures']} failure(s): {detail}")
        else:
            log(f"ok: {detail}")
        LAST_GOOD_VERSION_FILE.write_text(version)
        save_state({"consecutive_failures": 0, "last_restart_at": None, "attempt": 0})
        return 0

    s["consecutive_failures"] += 1
    s["attempt"] += 1
    log(f"FAIL ({s['consecutive_failures']}/{RESPAWN_BUDGET}): {detail}")

    if s["consecutive_failures"] >= RESPAWN_BUDGET:
        park(f"{RESPAWN_BUDGET} consecutive health-check failures, last: {detail}")
        save_state(s)
        return 2

    restart_remote_control(s["attempt"])
    save_state(s)
    return 1


if __name__ == "__main__":
    sys.exit(main())
