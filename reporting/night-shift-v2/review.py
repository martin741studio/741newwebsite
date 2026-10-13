#!/usr/bin/env python3
"""Night Shift v2 reviewer (script, no LLM): REVIEW.md, LOG.md line, _run.json, pulse line."""
import json, sys, datetime as dt
from pathlib import Path

out = Path(sys.argv[1]); repo = out.parents[2]
s = json.loads((out / "state.json").read_text())
items = s.get("items", {})
cnt = {k: sum(1 for v in items.values() if v["status"] == k) for k in ("pass", "needs_martin", "retry", "executed", "executed_no_critic", "skipped", "planned")}
lines = [f"# Night Shift v2 · {s['date']} · {len(items)} items · {cnt['pass']} pass · {cnt['needs_martin']} needs Martin",
         "", f"Runs {s['runs']}/{s['caps']['runs']} · est. ${s['usd']:.2f}/{s['caps']['usd']} · stop: {s.get('stopped_reason') or 'queue done'} · violations: {len(s.get('violations', []))}", ""]
by_client = {}
for iid, v in items.items(): by_client.setdefault(v["client"], []).append((iid, v))
for client, lst in by_client.items():
    lines.append(f"## {client}")
    for iid, v in lst:
        c = out / "critic" / f"{iid}.json"
        one = ""
        if c.exists():
            try: one = json.loads(c.read_text()).get("one_line", "")
            except Exception: one = "(critic file unreadable)"
        summ = out / "items" / iid / "summary.md"
        lines.append(f"- [ ] **{v['title']}** — {v['status']} (attempts {v.get('attempts', 0)})")
        lines.append(f"      → `items/{iid}/` · critic: {one or '—'}")
        if summ.exists(): lines += ["      " + l for l in summ.read_text().strip().splitlines()[:6]]
    lines.append("")
if s.get("violations"):
    lines += ["## Violations (writes outside the night folder)"] + [f"- run {x['run']} {x['role']} {x['item']}: {x['paths']}" for x in s["violations"]]
(out / "REVIEW.md").write_text("\n".join(lines) + "\n")
with open(out.parent / "LOG.md", "a") as f:
    f.write(f"{s['date']} · v2 · {len(items)} queued/{cnt['pass']} pass/{cnt['needs_martin']} needs_martin · runs {s['runs']} · ${s['usd']:.2f} · stop: {s.get('stopped_reason') or 'queue done'} · violations {len(s.get('violations', []))}\n")
(out / "_run.json").write_text(json.dumps({"client": "741", "workflow": "nightshift", "status": "fertig, Freigabe offen" if cnt["pass"] else "in Arbeit",
    "mode": "Echt", "last_run": s["date"], "result": str((out / "REVIEW.md").relative_to(repo)), "drive": "",
    "note": f"{cnt['pass']}/{len(items)} pass, runs {s['runs']}, ${s['usd']:.2f}"}, ensure_ascii=False, indent=1))
with open(out.parent / "pulse.log", "a") as f:
    f.write(f"{dt.datetime.now().isoformat(timespec='seconds')} night-v2 {'ok' if not s.get('violations') else 'violation'} items={len(items)} pass={cnt['pass']} runs={s['runs']} usd={s['usd']:.2f} stop={s.get('stopped_reason') or 'done'}\n")
print(f"REVIEW → {out / 'REVIEW.md'}")
