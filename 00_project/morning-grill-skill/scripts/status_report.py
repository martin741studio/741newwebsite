#!/usr/bin/env python3
"""Chat status report (Part 1 of the grill, D24-D25): where we are, what moved, what runs, what is stuck and why.

Clients with movement or a blocker get 3-4 lines. Quiet clients get one line.
Reads <run>/brief.json (+ goal sheet). Writes <run>/status-report.md and prints it.
Usage: python3 status_report.py --run <run dir> [--mode morning|evening]
"""
import argparse, json, os, sys

REPO = os.environ.get("MG_REPO", "/Users/martindrendel/741website")
GOALS = os.path.join(REPO, "00_project", "morning-grill-goals.json")
STUCK_KEYS = ("waiting for your approval", "waiting for", "access missing", "blocked", "overdue", "date in memory", "unread", "help request")


def short(t, n=150):
    t = " ".join(str(t).split())
    return t if len(t) <= n else t[: n - 1] + "…"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--run", required=True); ap.add_argument("--mode", default="morning")
    a = ap.parse_args()
    b = json.load(open(os.path.join(a.run, "brief.json"), encoding="utf-8"))
    cards_by = {}
    for i, c in enumerate(b["cards"], 1):
        cards_by.setdefault(c["client"], []).append(i)
    later_by = {}
    for c in b.get("below_the_line", []):
        later_by.setdefault(c["client"], []).append(c)
    walk_by = {}
    for w in b.get("walk_queue", []):
        walk_by.setdefault(w["client"], []).append(w["item"])
    busy, quiet = [], []
    for name, c in b["clients"].items():
        stuck = [w for w in c["watch"] if any(k in w.lower() for k in STUCK_KEYS)]
        moved = c["fixed"]
        if moved or stuck or name in cards_by or name in walk_by or name in later_by:
            busy.append((name, c, moved, stuck))
        else:
            quiet.append((name, c))
    # most pressure first: cards, then stuck lines, then movement
    busy.sort(key=lambda x: (-(len(cards_by.get(x[0], [])) * 10 + len(x[3])), x[0]))
    head = "Status since the last grill" if a.mode == "morning" else "Today per client"
    out = [f"**{head}** ({b['date']}, WITA). {len(busy)} clients with movement or blockers, {len(quiet)} quiet."]
    unread = [k for k, v in b["sources"].items() if v["status"] != "ok"]
    if unread:
        out.append(f"Unreadable sources: {', '.join(unread)}. Facts from them are missing below.")
    out.append("")
    for name, c, moved, stuck in busy:
        goal = short(c.get("goal") or "no quarter goal yet", 90)
        out.append(f"**{name}** ({c.get('phase') or '?'}, {c.get('status')}) — goal: {goal}")
        if moved:
            out.append(f"• Moved: {short('; '.join(moved[:2]), 220)}")
        if c["today"]:
            out.append(f"• Runs / next today: {short('; '.join(c['today'][:2]), 220)}")
        if stuck:
            out.append(f"• Stuck: {short('; '.join(stuck[:2]), 220)}")
        refs = []
        if name in cards_by:
            refs.append("card " + ", ".join(str(n) for n in cards_by[name]))
        if name in walk_by:
            refs.append(f"{len(walk_by[name])} walk item(s)")
        if name in later_by:
            refs.append(f"{len(later_by[name])} item(s) on the later list")
        if refs:
            out.append(f"• Your part: {', '.join(refs)}")
        out.append("")
    if quiet:
        out.append("**Quiet** (no step, no blocker since the last grill):")
        for name, c in quiet:
            nxt = c["next"][0] if c["next"] else "no next step set"
            out.append(f"• {name}: next {short(nxt, 100)}")
    if b.get("line_741"):
        out += ["", "**741**", *[f"• {short(x, 180)}" for x in b["line_741"][:5]]]
    agency = [c for c in b["cards"] if c["client"].startswith("741")]
    if agency:
        out.append(f"• Agency cards: {', '.join(str(b['cards'].index(c) + 1) for c in agency)}")
    if a.mode == "morning":
        out += ["", f"Next: {len(b.get('walk_queue', []))} walk items (1–5 min clicks), then {len(b['cards'])} decision cards."]
    text = "\n".join(out)
    open(os.path.join(a.run, "status-report.md"), "w", encoding="utf-8").write(text)
    print(text)


if __name__ == "__main__":
    sys.exit(main())
