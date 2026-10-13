#!/usr/bin/env python3
"""Validate a morning brief. Exit 1 on any failure; print every failure.

Checks:
  V1 every card has headline, >= 2 options, a recommended option that exists, why, deadline, evidence
  V2 max cards respected (default 7)
  V3 every active client in the goal sheet has a client block
  V4 every unreadable source is listed as unreadable (never dropped)
  V5 no open card in state/cards.json older than 3 days without a decision or park reason
  V6 brief.html exists and contains every card headline
  V7 no secret-looking strings in brief.html
Usage: python3 validate_brief.py --run <run dir> [--max 7]
"""
import argparse, datetime as dt, html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
GOALS = os.path.join(REPO, "00_project", "morning-grill-goals.json")
STATE = os.path.join(REPO, "00_project", "assets", "morning-grill", "state", "cards.json")
SECRET = re.compile(r"(eyJ[a-zA-Z0-9_-]{20,}|sk-[A-Za-z0-9]{20,}|PASSWORD=|apikey[:=]\s*\S{20,})")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--run", required=True); ap.add_argument("--max", type=int, default=7)
    a = ap.parse_args()
    fails = []
    b = json.load(open(os.path.join(a.run, "brief.json"), encoding="utf-8"))
    goals = json.load(open(GOALS, encoding="utf-8"))
    for i, c in enumerate(b["cards"], 1):
        for f in ("headline", "why", "deadline", "evidence"):
            if not c.get(f):
                fails.append(f"V1 card {i} ({c.get('id')}): missing {f}")
        if len(c.get("options", {})) < 2:
            fails.append(f"V1 card {i}: fewer than 2 options")
        if c.get("recommended") not in c.get("options", {}):
            fails.append(f"V1 card {i}: recommended option does not exist")
    if len(b["cards"]) > a.max:
        fails.append(f"V2 {len(b['cards'])} cards > max {a.max}")
    for c in goals["clients"]:
        if c.get("status") != "done" and c["client"] not in b["clients"]:
            fails.append(f"V3 client block missing: {c['client']}")
    for k, v in b["sources"].items():
        if v["status"] != "ok" and not v.get("error"):
            fails.append(f"V4 source {k} unreadable without error text")
    if os.path.exists(STATE):
        today = dt.date.fromisoformat(b["date"])
        for c in json.load(open(STATE, encoding="utf-8")).get("cards", []):
            if c.get("status") == "open" and (today - dt.date.fromisoformat(c["created"])).days > 3:
                fails.append(f"V5 card {c['id']} open for more than 3 days")
    hp = os.path.join(a.run, "brief.html")
    if not os.path.exists(hp):
        fails.append("V6 brief.html missing")
    else:
        h = open(hp, encoding="utf-8").read()
        for c in b["cards"]:
            if html.escape(c["headline"]) not in h:
                fails.append(f"V6 headline not rendered: {c['headline'][:60]}")
        if SECRET.search(h):
            fails.append("V7 secret-looking string in brief.html")
    if fails:
        print("FAIL\n" + "\n".join(fails)); return 1
    print(f"PASS · {len(b['cards'])} cards · {len(b['clients'])} clients · V1–V7 ok"); return 0


if __name__ == "__main__":
    sys.exit(main())
