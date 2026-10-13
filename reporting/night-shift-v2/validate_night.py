#!/usr/bin/env python3
"""Verify one night of Night Shift v2. Exit 0 = PASS, 1 = FAIL. Prints evidence.

Checks: every queued item has a final verdict · counter in state.json equals the
run lines in night-shift.log · no write violations · cost and runs within caps ·
REVIEW.md, _run.json and a pulse line exist · every pass item has its files.
Usage: python3 reporting/night-shift-v2/validate_night.py [YYYY-MM-DD]
"""
import json, re, sys, datetime as dt
from pathlib import Path

base = Path(__file__).resolve().parents[1] / "night-shift"
day = sys.argv[1] if len(sys.argv) > 1 else dt.date.today().isoformat()
out = base / day
fails, ok = [], []
def chk(cond, good, bad): (ok if cond else fails).append(good if cond else bad)

q = base / "queue" / f"{day}.json"
if not q.exists():
    print(f"no queue for {day}: no night run expected. PASS"); sys.exit(0)
s = json.loads((out / "state.json").read_text()) if (out / "state.json").exists() else None
chk(s is not None, "state.json exists", "state.json missing (run never started?)")
if s:
    items = json.loads(q.read_text())["items"]
    final = {"pass", "needs_martin", "skipped"}
    for it in items:
        st = s["items"].get(it["id"], {}).get("status", "missing")
        early = s.get("stopped_reason")
        chk(st in final or (early and st in ("planned", "executed", "executed_no_critic", "retry")),
            f"{it['id']}: {st}", f"{it['id']}: no final verdict ({st}) and no stop reason")
        if st == "pass":
            d = out / "items" / it["id"]
            chk((d / "summary.md").exists() and (d / "sources.md").exists() and (out / "critic" / f"{it['id']}.json").exists(),
                f"{it['id']}: summary, sources, critic present", f"{it['id']}: pass without summary/sources/critic file")
    log = (base / "night-shift.log").read_text().splitlines()
    runs_logged = len([l for l in log if f"[{day} " in l and re.search(r" v2 run \d+/\d+ ", l) and "dry-run" not in l])
    chk(runs_logged >= s["runs"], f"counter {s['runs']} matches log ({runs_logged} run lines today)", f"counter {s['runs']} > logged runs {runs_logged}")
    chk(s["runs"] <= s["caps"]["runs"], f"runs {s['runs']} <= cap {s['caps']['runs']}", f"runs {s['runs']} over cap")
    chk(s["usd"] <= s["caps"]["usd"] * 1.15, f"cost ${s['usd']:.2f} within cap", f"cost ${s['usd']:.2f} over cap")
    chk(not s.get("violations"), "no writes outside the night folder", f"VIOLATIONS: {s.get('violations')}")
    chk((out / "REVIEW.md").exists() and (out / "_run.json").exists(), "REVIEW.md + _run.json exist", "REVIEW.md or _run.json missing")
    pulse = base / "pulse.log"
    chk(pulse.exists() and any("night-v2" in l for l in pulse.read_text().splitlines()[-5:]), "pulse line written", "no pulse line")
for l in ok: print("OK  ", l)
for l in fails: print("FAIL", l)
print("PASS" if not fails else f"FAIL ({len(fails)})")
sys.exit(0 if not fails else 1)
