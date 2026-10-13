#!/usr/bin/env python3
"""741 Night Shift v2 runner (laptop phase, queue mode).

One night = Martin's confirmed queue (reporting/night-shift/queue/<DATE>.json).
Per item: one fresh Executor run + one fresh Critic run, max one retry.
Planner and reviewer are scripts (no LLM), so the run counter is exact.

Breakers (any one stops the night): MAX_RUNS runs · MAX_USD estimated cost ·
hard deadline (default 22:45 WITA) · STOP file · plan/usage-limit error.
Never: sends, deploys, live writes. Executor writes only into its item folder;
the runner checks `git status` after every run and logs violations.

Usage:
  python3 reporting/night-shift-v2/run.py                # scheduled (window check)
  NIGHT_ALLOW_ANYTIME=1 python3 reporting/night-shift-v2/run.py --dry-run
"""
import argparse, datetime as dt, json, os, re, signal, subprocess, sys, time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BASE = REPO / "reporting" / "night-shift"
V2 = REPO / "reporting" / "night-shift-v2"
CLAUDE = os.environ.get("NIGHT_CLAUDE", "/opt/homebrew/bin/claude")
MODEL = os.environ.get("NIGHT_MODEL", "claude-sonnet-5")
MAX_RUNS = int(os.environ.get("NIGHT_MAX_RUNS", "14"))
MAX_USD = float(os.environ.get("NIGHT_MAX_USD", "10"))
MAX_TURNS = int(os.environ.get("NIGHT_MAX_TURNS", "40"))
WINDOW_START = os.environ.get("NIGHT_WINDOW_START", "17:30")
DEADLINE_HM = os.environ.get("NIGHT_DEADLINE", "22:45")
STOP_FILE = BASE / "STOP"

ALLOWED = ",".join([
    "Read", "Write(./reporting/night-shift/**)", "Edit(./reporting/night-shift/**)", "Glob", "Grep", "WebFetch", "WebSearch",
    "Bash(python3:*)", "Bash(ls:*)", "Bash(wc:*)", "Bash(head:*)", "Bash(tail:*)",
    "Bash(grep:*)", "Bash(cat:*)", "Bash(mkdir:*)", "Bash(git status:*)", "Bash(git diff:*)",
])
DENIED = ",".join([
    "Bash(curl:*)", "Bash(wget:*)", "Bash(ftp:*)", "Bash(lftp:*)", "Bash(scp:*)", "Bash(sftp:*)",
    "Bash(rsync:*)", "Bash(ssh:*)", "Bash(git push:*)", "Bash(git commit:*)", "Bash(git reset:*)",
    "Bash(git checkout:*)", "Bash(rm:*)", "Bash(mv:*)", "Bash(npx:*)", "Bash(node:*)",
    "Bash(osascript:*)", "Bash(open:*)", "Bash(launchctl:*)", "Bash(sudo:*)",
])
LIMIT_PAT = re.compile(r"(usage limit|rate limit|limit reached|weekly limit|429|credit balance|out of credits)", re.I)

now = lambda: dt.datetime.now()
def hm(s):
    h, m = map(int, s.split(":")); return now().replace(hour=h, minute=m, second=0, microsecond=0)


class Night:
    def __init__(self, day, dry):
        self.day, self.dry = day, dry
        self.out = BASE / day
        self.out.mkdir(parents=True, exist_ok=True)
        (self.out / "items").mkdir(exist_ok=True)
        (self.out / "critic").mkdir(exist_ok=True)
        self.log_file = BASE / "night-shift.log"
        self.state_file = self.out / "state.json"
        self.state = json.loads(self.state_file.read_text()) if self.state_file.exists() else {
            "date": day, "version": "v2", "model": MODEL, "runs": 0, "usd": 0.0,
            "caps": {"runs": MAX_RUNS, "usd": MAX_USD, "turns": MAX_TURNS, "deadline": DEADLINE_HM},
            "items": {}, "stopped_reason": None, "violations": [], "started": now().isoformat(timespec="seconds")}
        self.deadline = hm(DEADLINE_HM)
        self.baseline = self.git_dirty()

    def log(self, msg):
        line = f"[{now():%F %T}] v2 {msg}"
        print(line, flush=True)
        with open(self.log_file, "a") as f: f.write(line + "\n")

    def save(self):
        self.state_file.write_text(json.dumps(self.state, indent=2, ensure_ascii=False))

    def git_dirty(self):
        r = subprocess.run(["git", "status", "--porcelain"], cwd=REPO, capture_output=True, text=True)
        return set(r.stdout.splitlines())

    def breaker(self):
        if STOP_FILE.exists(): return "stopped by Martin (STOP file)"
        if self.state["runs"] >= MAX_RUNS: return f"run cap {MAX_RUNS} reached"
        if self.state["usd"] >= MAX_USD: return f"cost cap USD {MAX_USD} reached"
        if now() >= self.deadline - dt.timedelta(minutes=4): return f"deadline {DEADLINE_HM}"
        return None

    def run(self, role, item_id, prompt):
        """One fresh claude -p invocation. Returns (ok, text). Counter is checked BEFORE the call."""
        why = self.breaker()
        if why: return False, f"BREAKER: {why}"
        self.state["runs"] += 1; self.save()
        n = self.state["runs"]
        remaining = max(0.5, min(3.0, MAX_USD - self.state["usd"]))
        self.log(f"run {n}/{MAX_RUNS} {role} {item_id} (budget left ${MAX_USD - self.state['usd']:.2f})")
        if self.dry:
            self.log(f"  dry-run: prompt {len(prompt)} chars, not executed"); return True, "DRY"
        cmd = [CLAUDE, "-p", prompt, "--model", MODEL, "--max-turns", str(MAX_TURNS),
               "--output-format", "json", "--permission-mode", "dontAsk",
               "--allowedTools", ALLOWED, "--disallowedTools", DENIED,
               "--strict-mcp-config", "--setting-sources", "user", "--max-budget-usd", f"{remaining:.2f}"]
        raw = self.out / f".run{n}.json"
        with open(raw, "w") as fo, open(self.out / f".run{n}.err", "w") as fe:
            p = subprocess.Popen(cmd, cwd=REPO, stdout=fo, stderr=fe, start_new_session=True)
            while p.poll() is None:
                if now() >= self.deadline or STOP_FILE.exists():
                    os.killpg(p.pid, signal.SIGTERM); time.sleep(5)
                    if p.poll() is None: os.killpg(p.pid, signal.SIGKILL)
                    self.log(f"  killed {role} {item_id}: {'STOP file' if STOP_FILE.exists() else 'deadline'}")
                    break
                time.sleep(5)
        try:
            d = json.loads(raw.read_text() or "{}")
        except Exception:
            d = {"is_error": True, "result": raw.read_text()[-500:]}
        cost = float(d.get("total_cost_usd") or 0)
        self.state["usd"] = round(self.state["usd"] + cost, 4)
        text = str(d.get("result") or "")
        err = bool(d.get("is_error")) or d.get("subtype") not in (None, "success")
        self.log(f"  {role} {item_id} exit={p.returncode} cost=${cost:.3f} total=${self.state['usd']:.2f} sub={d.get('subtype')} :: {text[:160]!r}")
        # write-outside-sandbox check
        new = self.git_dirty() - self.baseline
        bad = [l for l in new if f"reporting/night-shift/{self.day}/" not in l and "reporting/night-shift/" + "night-shift.log" not in l
               and "00_project/workflow-registry/" not in l and not l.endswith("reporting/night-shift/")]
        if bad:
            self.state["violations"].append({"run": n, "role": role, "item": item_id, "paths": bad})
            self.log(f"  VIOLATION: wrote outside the night folder: {bad}")
        self.baseline |= new
        if err and LIMIT_PAT.search(text + (self.out / f".run{n}.err").read_text()):
            self.state["stopped_reason"] = "plan/usage limit hit"
            (self.out / "resume.json").write_text(json.dumps({"at": now().isoformat(), "role": role, "item": item_id}))
        self.save()
        return (not err), text


def fill(tpl, **kw):
    for k, v in kw.items(): tpl = tpl.replace("{" + k + "}", str(v))
    return tpl


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--day", default=now().strftime("%F"))
    a = ap.parse_args()

    if os.environ.get("NIGHT_ALLOW_ANYTIME") != "1":
        if not (hm(WINDOW_START) <= now() < hm(DEADLINE_HM) - dt.timedelta(minutes=10)):
            print(f"outside window {WINDOW_START}-{DEADLINE_HM}; not starting"); return 0
    if STOP_FILE.exists():
        print("STOP file present; not starting"); return 0
    qf = BASE / "queue" / f"{a.day}.json"
    if not qf.exists():
        print(f"no confirmed queue {qf}; nothing to do"); return 0
    lock = BASE / ".lock-v2"
    try: lock.mkdir()
    except FileExistsError:
        if time.time() - lock.stat().st_mtime < 6 * 3600: print("another v2 run holds the lock"); return 0
    try:
        night = Night(a.day, a.dry_run)
        queue = json.loads(qf.read_text())
        items = queue["items"] if isinstance(queue, dict) else queue
        night.log(f"=== night v2 {a.day} start · {len(items)} items · caps {MAX_RUNS} runs / ${MAX_USD} / {DEADLINE_HM} · dry={a.dry_run} ===")
        ex_tpl = (V2 / "prompts" / "executor.md").read_text()
        cr_tpl = (V2 / "prompts" / "critic.md").read_text()
        for it in items:
            iid = it["id"]
            st = night.state["items"].setdefault(iid, {"title": it["title"], "client": it["client"], "status": "planned", "attempts": 0})
            if st["status"] in ("pass", "needs_martin"): continue
            if not it.get("confirmed", True):
                st["status"] = "skipped"; st["why"] = "not confirmed by Martin"; continue
            idir = night.out / "items" / iid; idir.mkdir(parents=True, exist_ok=True)
            cfile = night.out / "critic" / f"{iid}.json"; vfile = night.out / "critic" / f".verdict_{iid}"
            common = dict(ID=iid, CLIENT=it["client"], CLASS=it["class"], TITLE=it["title"], BRIEF=it.get("brief", ""),
                          INPUTS="; ".join(it.get("inputs", [])) or "none", DONE=it["done"], LANG=it.get("lang", "German"),
                          ITEM_DIR=idir.relative_to(REPO), CRITIC_FILE=cfile.relative_to(REPO), VERDICT_FILE=vfile.relative_to(REPO))
            while st["attempts"] < 2:
                retry = ""
                if st["attempts"] == 1 and cfile.exists():
                    retry = f"RETRY: attempt 2. Read the critic result {cfile.relative_to(REPO)} first and fix every item in 'fails'."
                if MAX_RUNS - night.state["runs"] < 2:  # never start an Executor without room for its Critic
                    night.state["stopped_reason"] = f"run cap {MAX_RUNS}: no room for Executor + Critic"; break
                ok, txt = night.run("EXECUTOR", iid, fill(ex_tpl, RETRY_NOTE=retry, **common))
                if txt.startswith("BREAKER") or night.state["stopped_reason"]: break
                st["attempts"] += 1; st["status"] = "executed"; night.save()
                if vfile.exists(): vfile.unlink()
                ok, txt = night.run("CRITIC", iid, fill(cr_tpl, **common))
                if txt.startswith("BREAKER") or night.state["stopped_reason"]:
                    st["status"] = "executed_no_critic"; break
                verdict = vfile.read_text().strip() if vfile.exists() else ("pass" if a.dry_run else "retry")
                st["status"] = "pass" if verdict == "pass" else ("needs_martin" if st["attempts"] >= 2 else "retry")
                night.save()
                if verdict == "pass": break
            why = night.breaker() or night.state["stopped_reason"]
            if why:
                night.state["stopped_reason"] = night.state["stopped_reason"] or why
                night.log(f"stop: {why}"); break
        night.state["finished"] = now().isoformat(timespec="seconds"); night.save()
        subprocess.run([sys.executable, str(V2 / "review.py"), str(night.out)], cwd=REPO)
        night.log(f"=== night v2 {a.day} end · runs {night.state['runs']} · ${night.state['usd']:.2f} · stop={night.state['stopped_reason']} ===")
    finally:
        try: lock.rmdir()
        except Exception: pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
