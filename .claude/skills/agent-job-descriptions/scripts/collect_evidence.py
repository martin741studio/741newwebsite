#!/usr/bin/env python3
"""Collect review evidence for one agent since a date. Writes 00_project/agent-jobs/reviews/<week>/<id>-evidence.md.
Sources: outbox files, _run.json under 00_project/assets/*/<id>/ and the workflow folder, git log on the roster paths,
grill ledger entries naming the agent, night-shift REVIEW.md (runner). A source that cannot be read is listed as UNREADABLE.

usage: collect_evidence.py --id ID [--since YYYY-MM-DD] [--week YYYY-Www]
"""
import argparse, json, datetime, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "00_project" / "agent-jobs"

def main():
    p = argparse.ArgumentParser(); p.add_argument("--id", required=True); p.add_argument("--since"); p.add_argument("--week")
    a = p.parse_args()
    today = datetime.date.today()
    roster = json.loads((DATA / "roster.json").read_text())
    ag = next((x for x in roster["agents"] if x["id"] == a.id), None) or exit(f"{a.id} not in roster")
    since = a.since or ag.get("last_review") or (today - datetime.timedelta(days=7)).isoformat()
    week = a.week or f"{today.isocalendar()[0]}-W{today.isocalendar()[1]:02d}"
    since_dt = datetime.datetime.fromisoformat(since)
    out = [f"# Evidence — {ag['title']} ({a.id}), week {week}, since {since}", ""]
    unreadable = []
    def newer(f):
        try: return datetime.datetime.fromtimestamp(f.stat().st_mtime) >= since_dt
        except OSError: unreadable.append(str(f)); return False
    # 1 outbox
    ob = DATA / a.id / "outbox"
    files = sorted(f for f in ob.glob("*.md") if newer(f)) if ob.exists() else []
    out += ["## Outbox (tasks reported)"] + ([f"- {f.relative_to(ROOT)}" for f in files] or ["- none"]) + [""]
    if not ob.exists(): unreadable.append(str(ob))
    # 2 _run.json
    runs = [f for f in ROOT.glob(f"00_project/assets/*/{a.id}/*/_run.json") if newer(f)]
    runs += [f for f in ROOT.glob("00_project/assets/741studio/agent-job-descriptions/*/_run.json") if newer(f)]
    out += ["## Run records"]
    for f in runs:
        try: d = json.loads(f.read_text()); out.append(f"- {f.relative_to(ROOT)}: {d.get('status')} · {d.get('result')} · {d.get('note','')}")
        except Exception: unreadable.append(str(f))
    if not runs: out.append("- none")
    out.append("")
    # 3 git log
    out += ["## Git log on the agent's paths"]
    paths = [x.replace("/**", "").replace("**", "") for x in ag.get("paths", [])] or [f"00_project/agent-jobs/{a.id}"]
    try:
        g = subprocess.run(["git", "log", f"--since={since}", "--pretty=format:- %ad %h %s", "--date=short", "--", *paths], cwd=ROOT, capture_output=True, text=True, timeout=30)
        out += (g.stdout.strip().splitlines() or ["- no commits"]) if g.returncode == 0 else ["- UNREADABLE git"]
    except Exception as e: unreadable.append(f"git ({e})")
    out.append("")
    # 4 grill ledger
    led = ROOT / "00_project" / "assets" / "morning-grill" / "state" / "cards.json"
    out += ["## Grill ledger entries naming the agent"]
    try:
        cards = json.loads(led.read_text()); hits = []
        for c in (cards if isinstance(cards, list) else cards.get("cards", [])):
            s = json.dumps(c, ensure_ascii=False)
            if a.id in s or ag["title"] in s: hits.append(f"- {str(c.get('id') or c.get('title') or '')[:80]} · {c.get('answer') or c.get('decision') or ''}")
        out += hits or ["- none"]
    except Exception: unreadable.append(str(led)); out.append("- UNREADABLE ledger")
    out.append("")
    # 5 runner-specific
    if ag["type"] == "runner":
        out += ["## Night-shift reviews since the date"]
        rv = sorted(f for f in (ROOT / "reporting" / "night-shift").glob("**/REVIEW.md") if newer(f))
        out += [f"- {f.relative_to(ROOT)}" for f in rv] or ["- none"]; out.append("")
    out += ["## Unreadable sources"] + ([f"- {u}" for u in unreadable] or ["- none"])
    dest = DATA / "reviews" / week / f"{a.id}-evidence.md"; dest.mkdir(parents=True, exist_ok=True) if False else dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(out) + "\n"); print(dest.relative_to(ROOT)); print("\n".join(out))

if __name__ == "__main__":
    main()
