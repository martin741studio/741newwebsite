#!/usr/bin/env python3
"""741-agents-01 scheduled recovery drill (v3 autonomy build, item 4).

Research rule 18/N11: don't rely on the one-off reboot test forever, and
don't run a drill with no written abort criteria. This script:
1. States the failure mode and abort condition BEFORE acting (printed + logged).
2. Kills claude-remote-control.service hard (kill -9, not a graceful stop).
3. Waits for systemd to restart it (its own Restart=on-failure + backoff).
4. Runs the real health check (not just "systemd says active" — rule 17/N11).
5. Rates the drill pass / pass-with-finding / fail (rule 19/N11), logs it,
   and writes a tracked finding file if it's anything but a clean pass.

Run monthly via drill.timer. Can also be run by hand: python3 drill.py
"""
import subprocess, sys, time, datetime, pathlib, json

HOME = pathlib.Path.home()
DRILL_DIR = HOME / ".browser-display" / "drills"
DRILL_DIR.mkdir(parents=True, exist_ok=True)
LOG = DRILL_DIR / "drill.log"

FAILURE_MODE = "claude-remote-control.service is killed with SIGKILL (hard, not graceful)"
ABORT_CONDITION = "if the service does not even attempt to restart within 60s, abort and alert immediately rather than waiting longer"
RECOVERY_TARGET_SEC = 90


def log(msg):
    line = f"[{datetime.datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def service_pid():
    r = subprocess.run(["systemctl", "--user", "show", "-p", "MainPID", "claude-remote-control.service"],
                        capture_output=True, text=True)
    return r.stdout.strip().split("=")[-1]


def service_active():
    r = subprocess.run(["systemctl", "--user", "is-active", "claude-remote-control.service"],
                        capture_output=True, text=True)
    return r.stdout.strip() == "active"


def main():
    log(f"=== drill start === failure mode: {FAILURE_MODE} | abort: {ABORT_CONDITION} | recovery target: {RECOVERY_TARGET_SEC}s")

    pid_before = service_pid()
    if pid_before in ("0", ""):
        log("FAIL: service was not running before the drill even started — nothing to test")
        write_finding("fail", "service not running pre-drill")
        return 2

    log(f"killing pid {pid_before} with SIGKILL")
    subprocess.run(["kill", "-9", pid_before])

    t0 = time.time()
    attempted_restart = False
    while time.time() - t0 < 60:
        if service_pid() not in ("0", "", pid_before):
            attempted_restart = True
            break
        time.sleep(3)

    if not attempted_restart:
        log(f"ABORT: {ABORT_CONDITION} — no restart attempt seen within 60s")
        write_finding("fail", "no restart attempt within 60s abort window")
        subprocess.run(["systemctl", "--user", "start", "claude-remote-control.service"])
        return 2

    while time.time() - t0 < RECOVERY_TARGET_SEC:
        if service_active():
            break
        time.sleep(3)

    recovered_in = round(time.time() - t0, 1)
    if not service_active():
        log(f"FAIL: service not active {RECOVERY_TARGET_SEC}s after kill")
        write_finding("fail", f"not active after {RECOVERY_TARGET_SEC}s")
        return 2

    log(f"service active again after {recovered_in}s — now proving it does real work, not just 'active'")
    r = subprocess.run([sys.executable, str(HOME / "health_check.py")])
    if r.returncode == 0:
        log(f"PASS: recovered in {recovered_in}s and completed a real task afterward")
        write_finding("pass", f"recovered in {recovered_in}s, real task confirmed")
        return 0
    else:
        log(f"PASS WITH FINDING: service shows active after {recovered_in}s but the post-recovery real-task check failed")
        write_finding("pass-with-finding", f"active after {recovered_in}s but health check failed afterward — needs a human look")
        return 1


def write_finding(rating, note):
    f = DRILL_DIR / f"{datetime.date.today().isoformat()}-drill.json"
    f.write_text(json.dumps({
        "date": datetime.date.today().isoformat(),
        "rating": rating,
        "note": note,
        "failure_mode": FAILURE_MODE,
        "abort_condition": ABORT_CONDITION,
        "owner": "Martin" if rating != "pass" else None,
        "due": None,
    }, indent=2))


if __name__ == "__main__":
    sys.exit(main())
