#!/usr/bin/env python3
"""Validate a 741 agent job description (block template) or its placed copies.

usage:
  validate_jd.py 00_project/agent-jobs/<id>.md        # structure check → PASS/FAIL, exit 0/1
  validate_jd.py --copies <id>                          # placed copies match the source
Checks: 15 sections in order; every never-line has a rung; every tool has a rating; goal has a success
criterion; the Go section exists and mentions "Go"; no self-grade; caps contain a number; edge cases name
the missing-source rule; agent id is in roster.json; no raw video/creator names.
"""
import re, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "00_project" / "agent-jobs"
SECTIONS = ["Title", "Goal", "Trigger / cadence", "Duties", "Data it may read", "Tools (risk)",
            "Actions it may take alone", "Actions that need a Go", "Never (rung)", "Caps", "May delegate to",
            "Expected output / report", "Manager", "Review day", "Edge cases"]
RUNGS = {"hook", "runner", "card", "skill", "rule", "advisory"}
RATINGS = re.compile(r"\((low|medium|high)[^)]*\)")
FORBIDDEN = ["Tyler", "Phillips", "Grok Bot", "12-block"]

def hdr(name):
    return re.compile(r"\*\*" + re.escape(name) + r"(?: \([^)]*\))?:\*\*")

def find_hdr(body, name, start=0):
    m = hdr(name).search(body, start)
    return m.start() if m else -1

def section_text(body, name, nxt):
    i = find_hdr(body, name)
    if i < 0: return None
    j = find_hdr(body, nxt, i + 1) if nxt else -1
    return body[i:j if j > 0 else len(body)]

def validate(path):
    errs = []
    body = Path(path).read_text()
    m = re.search(r"^# Job description — .+\(agent id: ([a-z0-9-]+)\)", body, re.M)
    if not m: errs.append("H1 must be '# Job description — <Title> (agent id: <id>)'")
    aid = m.group(1) if m else None
    pos = -1
    for s in SECTIONS:
        i = find_hdr(body, s)
        if i < 0: errs.append(f"missing section **{s}:**")
        elif i < pos: errs.append(f"section out of order: **{s}:**")
        else: pos = i
    for k, s in enumerate(SECTIONS):
        nxt = SECTIONS[k + 1] if k + 1 < len(SECTIONS) else None
        t = section_text(body, s, nxt) or ""
        if s == "Goal" and "success" not in t.lower(): errs.append("Goal: no 'Success =' criterion")
        if s == "Tools (risk)":
            items = [x for x in re.split(r"\s·\s|\n- ", t.split(":**", 1)[-1]) if x.strip()]
            for it in items:
                if not RATINGS.search(it): errs.append(f"Tools: no (low|medium|high) rating in: {it.strip()[:60]}")
        if s == "Actions that need a Go" and not re.search(r"\bGo\b", t.split(":**", 1)[-1]): errs.append("Actions that need a Go: must name the card Go (word 'Go') for the listed actions")
        if s == "Never (rung)":
            lines = [l for l in t.splitlines() if l.strip().startswith("- ")]
            if not lines: errs.append("Never: no bullet lines")
            for l in lines:
                r = re.search(r"rung:\s*([a-z]+)", l)
                if not r: errs.append(f"Never line without rung: {l.strip()[:70]}")
                elif r.group(1) not in RUNGS: errs.append(f"Never line with unknown rung '{r.group(1)}': {l.strip()[:60]}")
        if s == "Caps" and not re.search(r"\d", t): errs.append("Caps: no number")
        if s == "Review day" and not re.search(r"(writes no grade|does not grade|never grades|no self-grade|Martin grades)", t, re.I): errs.append("Review day: must state that the agent writes no grade and Martin grades")
        if s == "Review day" and "Friday" not in t: errs.append("Review day: must be Friday (roster review_day)")
        if s == "Edge cases" and not re.search(r"missing|unreadable|fehlt", t, re.I): errs.append("Edge cases: missing-source rule absent")
        if s == "Expected output / report" and not all(w in t.lower() for w in ["facts", "assumptions", "unresolved", "unreadable"]): errs.append("Report: needs facts · assumptions · done · waiting for Go · unresolved · unreadable")
    for w in FORBIDDEN:
        if w in body: errs.append(f"forbidden source name in description: {w}")
    rf = DATA / "roster.json"
    if aid and rf.exists():
        ids = {a["id"] for a in json.loads(rf.read_text())["agents"]}
        if aid not in ids: errs.append(f"agent id '{aid}' not in roster.json (run roster.py add)")
    return aid, errs

def copies(aid):
    src = (DATA / f"{aid}.md").read_text()
    r = json.loads((DATA / "roster.json").read_text())
    ag = next((a for a in r["agents"] if a["id"] == aid), None)
    if not ag: return [f"unknown id {aid}"]
    errs = []
    if not ag.get("placed_at"): return [f"nothing placed yet for {aid} (placed_at empty) — run place.py first"]
    for p in ag.get("placed_at", []):
        f = ROOT / p
        if not f.exists(): errs.append(f"placed copy missing: {p}"); continue
        t = f.read_text()
        if p.endswith(f"rules/agents/{aid}.md"):
            body = t.split("---", 2)[2] if t.startswith("---") else t
            if src.strip() not in body: errs.append(f"rules copy drifted: {p}")
        else:
            m = re.search(r"<!-- agent-job:start -->(.*?)<!-- agent-job:end -->", t, re.S)
            if not m: errs.append(f"no agent-job markers in {p}")
            else:
                for s in ("Never (rung)", "Actions that need a Go", "Caps"):
                    seg = section_text(src, s, SECTIONS[SECTIONS.index(s) + 1])
                    if seg and seg.strip() not in m.group(1): errs.append(f"task header drifted in section {s}: {p}")
    return errs

def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--copies":
        errs = copies(sys.argv[2]); label = f"copies {sys.argv[2]}"
    elif len(sys.argv) == 2:
        aid, errs = validate(sys.argv[1]); label = sys.argv[1]
    else:
        sys.exit(__doc__)
    for e in errs: print("FAIL", e)
    print(("PASS" if not errs else "FAIL") + f" · {label} · {len(errs)} finding(s)")
    sys.exit(1 if errs else 0)

if __name__ == "__main__":
    main()
