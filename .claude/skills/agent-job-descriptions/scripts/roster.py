#!/usr/bin/env python3
"""741 agent roster. Data: 00_project/agent-jobs/roster.json. Platform-neutral (python3 stdlib only).

usage:
  roster.py list
  roster.py ids
  roster.py add --id ID --title T --type chat|scheduled|runner|backlog [--runs-at WHERE] [--paths P1,P2] [--task TASK_ID]
  roster.py set --id ID key=value [key=value ...]
  roster.py render            # writes roster.md
"""
import argparse, json, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "00_project" / "agent-jobs"
FILE = DATA / "roster.json"
TYPES = {"chat", "scheduled", "runner", "backlog"}
FIELDS = ["id", "title", "type", "runs_at", "manager", "review_day", "description", "paths", "task",
          "placed_at", "status", "last_review", "last_grade", "added"]

def load():
    if not FILE.exists():
        return {"review_day": "Friday", "manager": "Martin", "agents": []}
    return json.loads(FILE.read_text())

def save(d):
    DATA.mkdir(parents=True, exist_ok=True)
    FILE.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")

def find(d, aid):
    for a in d["agents"]:
        if a["id"] == aid:
            return a
    return None

def cmd_list(d):
    for a in d["agents"]:
        print(f"{a['id']:<28} {a['type']:<10} {a.get('status','draft'):<8} grade={a.get('last_grade') or '-':<2} {a['title']}")
    print(f"{len(d['agents'])} agents · review day {d.get('review_day')} · manager {d.get('manager')}")

def cmd_add(d, a):
    if a.type not in TYPES:
        sys.exit(f"type must be one of {sorted(TYPES)}")
    if find(d, a.id):
        sys.exit(f"id exists: {a.id}")
    if not all(c.isalnum() or c == "-" for c in a.id) or a.id != a.id.lower():
        sys.exit("id must be kebab-case")
    d["agents"].append({
        "id": a.id, "title": a.title, "type": a.type, "runs_at": a.runs_at or "",
        "manager": d.get("manager", "Martin"), "review_day": d.get("review_day", "Friday"),
        "description": f"00_project/agent-jobs/{a.id}.md",
        "paths": [p for p in (a.paths or "").split(",") if p], "task": a.task or "",
        "placed_at": [], "status": "backlog" if a.type == "backlog" else "draft",
        "last_review": None, "last_grade": None, "added": datetime.date.today().isoformat()})
    save(d); print(f"added {a.id}")

def cmd_set(d, a):
    ag = find(d, a.id) or sys.exit(f"unknown id {a.id}")
    for kv in a.kv:
        k, _, v = kv.partition("=")
        if k not in FIELDS:
            sys.exit(f"unknown field {k}; allowed: {FIELDS}")
        if k in ("paths", "placed_at"):
            v = [p for p in v.split(",") if p]
        ag[k] = v
    save(d); print(f"set {a.id}: {' '.join(a.kv)}")

def cmd_render(d):
    lines = [f"# 741 agent roster — rendered {datetime.date.today().isoformat()}", "",
             f"Manager: {d.get('manager')} · review day: {d.get('review_day')} · source: `roster.json` (edit with `roster.py`)", "",
             "| id | title | type | runs at | status | description | placed at | last review | grade |",
             "|---|---|---|---|---|---|---|---|---|"]
    for a in d["agents"]:
        lines.append(f"| {a['id']} | {a['title']} | {a['type']} | {a.get('runs_at','')} | {a.get('status','')} | "
                     f"`{a.get('description','')}` | {', '.join(a.get('placed_at', [])) or '—'} | {a.get('last_review') or '—'} | {a.get('last_grade') or '—'} |")
    (DATA / "roster.md").write_text("\n".join(lines) + "\n")
    print(f"rendered {DATA / 'roster.md'} ({len(d['agents'])} agents)")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["list", "ids", "add", "set", "render"])
    p.add_argument("--id"); p.add_argument("--title"); p.add_argument("--type")
    p.add_argument("--runs-at", dest="runs_at"); p.add_argument("--paths"); p.add_argument("--task")
    p.add_argument("kv", nargs="*")
    a = p.parse_args()
    d = load()
    if a.cmd == "list": cmd_list(d)
    elif a.cmd == "ids": print("\n".join(x["id"] for x in d["agents"]))
    elif a.cmd == "add":
        if not (a.id and a.title and a.type): sys.exit("add needs --id --title --type")
        cmd_add(d, a)
    elif a.cmd == "set":
        if not a.id or not a.kv: sys.exit("set needs --id and key=value")
        cmd_set(d, a)
    elif a.cmd == "render": cmd_render(d)

if __name__ == "__main__":
    main()
