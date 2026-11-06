#!/usr/bin/env python3
"""Acceptance-criteria contract tool (741).

    python3 contract.py new <slug> "<Title>"            create 00_project/contracts/<slug>/contract-v001.json
    python3 contract.py validate <contract.json>        errors (exit 1) and warnings
    python3 contract.py md <contract.json>              write the human summary next to the json
    python3 contract.py approve <contract.json> "<Martin's words>"   freeze the version
    python3 contract.py bump <contract.json>            copy to the next version as a draft
    python3 contract.py tasks <contract.json>           print the task split for the shared task list
    python3 contract.py verdict <contract.json> <results.json>       acceptance table, exit 0 only when done

The contract is the source of truth for a team build. See ../SKILL.md.
"""
import copy
import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[4])
CONTRACTS = ROOT / "00_project" / "contracts"
TEMPLATE = Path(__file__).resolve().parent.parent / "references" / "contract-template.json"

CATEGORIES = {"functional", "security", "privacy", "performance", "accessibility", "legal", "seo", "ops"}
PRIORITIES = {"must", "should", "could"}
METHODS = {"unit", "e2e", "command", "review", "manual"}
SOURCE_TYPES = {"standard", "law", "vendor", "guide"}
AUTOMATABLE = {"functional", "security", "performance", "accessibility"}
NEEDS_SECURITY = {"auth", "form", "api", "payment", "upload", "data", "ai-feature", "wordpress", "infra"}
NEEDS_PRIVACY = {"auth", "form", "tracking", "data", "email", "ai-feature"}
NEEDS_LEGAL = {"health-content", "email", "tracking", "ai-feature"}
VAGUE = re.compile(
    r"\b(schnell|zügig|gut|besser|benutzerfreundlich|nutzerfreundlich|intuitiv|einfach|sauber|modern|robust|"
    r"performant|sicher|stabil|ordentlich|angemessen|fast|quick|good|better|user[- ]friendly|intuitive|easy|"
    r"simple|clean|robust|secure|stable|proper|appropriate|nice|seamless)\b",
    re.IGNORECASE,
)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def criteria_hash(c):
    core = {k: c.get(k) for k in ("context", "module_types", "sources", "milestones", "criteria", "limits")}
    return hashlib.sha256(json.dumps(core, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


def overlaps(a, b):
    a, b = a.rstrip("*").rstrip("/"), b.rstrip("*").rstrip("/")
    return a == b or a.startswith(b + "/") or b.startswith(a + "/")


def validate(c):
    err, warn = [], []
    for k in ("id", "version", "status", "title", "context", "module_types", "sources", "milestones", "criteria"):
        if k not in c or c[k] in (None, "", [], {}):
            err.append(f"missing field: {k}")
    if err:
        return err, warn
    ctx = c["context"]
    for k in ("who_uses", "goal", "access"):
        if not str(ctx.get(k, "")).strip():
            err.append(f"context.{k} is empty (intake grill not done)")
    if not ctx.get("out_of_scope"):
        warn.append("context.out_of_scope is empty: say what we do NOT build")

    # sources
    src_ids = set()
    for s in c["sources"]:
        sid = s.get("id")
        if sid in src_ids:
            err.append(f"duplicate source id {sid}")
        src_ids.add(sid)
        if not str(s.get("url", "")).startswith("http"):
            err.append(f"source {sid}: url missing")
        if s.get("type") not in SOURCE_TYPES:
            err.append(f"source {sid}: type must be one of {sorted(SOURCE_TYPES)}")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(s.get("checked", ""))):
            err.append(f"source {sid}: checked date YYYY-MM-DD missing")
    if len(c["sources"]) < 3:
        err.append(f"only {len(c['sources'])} sources: research needs at least 3")
    if not any(s.get("type") in ("standard", "law") for s in c["sources"]):
        err.append("no primary source (type standard or law)")

    # milestones
    ms_ids = [m.get("id") for m in c["milestones"]]
    if len(ms_ids) != len(set(ms_ids)):
        err.append("duplicate milestone id")
    for m in c["milestones"]:
        if not str(m.get("exit", "")).strip():
            err.append(f"milestone {m.get('id')}: exit condition missing")

    # criteria
    ids, used_src, cats = set(), set(), set()
    must_per_ms = {m: 0 for m in ms_ids}
    max_must = (c.get("limits") or {}).get("max_must_per_milestone", 15)
    for cr in c["criteria"]:
        cid = cr.get("id", "?")
        if cid in ids:
            err.append(f"duplicate criterion id {cid}")
        ids.add(cid)
        if cr.get("milestone") not in ms_ids:
            err.append(f"{cid}: milestone {cr.get('milestone')} does not exist")
        if cr.get("category") not in CATEGORIES:
            err.append(f"{cid}: category must be one of {sorted(CATEGORIES)}")
        cats.add(cr.get("category"))
        if cr.get("priority") not in PRIORITIES:
            err.append(f"{cid}: priority must be must, should or could")
        text, measure = str(cr.get("text", "")).strip(), str(cr.get("measure", "")).strip()
        if not text:
            err.append(f"{cid}: text missing")
        if not measure:
            err.append(f"{cid}: measure missing (number or observable result)")
        for field, val in (("text", text), ("measure", measure)):
            m = VAGUE.search(val)
            if m and not re.search(r"\d", val):
                err.append(f"{cid}: vague word '{m.group(0)}' in {field} without a number")
        v = cr.get("verify") or {}
        if v.get("method") not in METHODS:
            err.append(f"{cid}: verify.method must be one of {sorted(METHODS)}")
        if not str(v.get("how", "")).strip():
            err.append(f"{cid}: verify.how missing (exact test, command or check)")
        if cr.get("priority") == "must" and v.get("method") == "manual" and cr.get("category") in AUTOMATABLE:
            warn.append(f"{cid}: must + {cr.get('category')} with a manual check; an automated test is better")
        srcs = cr.get("sources") or []
        if not srcs:
            err.append(f"{cid}: no source")
        for s in srcs:
            if s not in src_ids:
                err.append(f"{cid}: source {s} does not exist")
            used_src.add(s)
        if cr.get("priority") == "must" and cr.get("milestone") in must_per_ms:
            must_per_ms[cr["milestone"]] += 1
    for m, n in must_per_ms.items():
        if n == 0:
            warn.append(f"milestone {m} has no must criterion")
        if n > max_must:
            warn.append(f"milestone {m} has {n} must criteria (Pareto limit {max_must}): lower some to should")
    for s in src_ids - used_src:
        warn.append(f"source {s} is not used by any criterion")

    types = set(c["module_types"])
    if types & NEEDS_SECURITY and "security" not in cats:
        err.append(f"module types {sorted(types & NEEDS_SECURITY)} need at least one security criterion")
    if types & NEEDS_PRIVACY and "privacy" not in cats:
        err.append(f"module types {sorted(types & NEEDS_PRIVACY)} need at least one privacy criterion")
    if types & NEEDS_LEGAL and "legal" not in cats and "privacy" not in cats:
        err.append(f"module types {sorted(types & NEEDS_LEGAL)} need at least one legal criterion")

    # tasks
    tasks = c.get("tasks") or []
    if tasks:
        tids = set()
        covered = set()
        owned = []
        for t in tasks:
            tid = t.get("id", "?")
            if tid in tids:
                err.append(f"duplicate task id {tid}")
            tids.add(tid)
            if not t.get("owner"):
                err.append(f"{tid}: owner missing")
            if not t.get("files"):
                err.append(f"{tid}: files missing (file ownership prevents overwrites)")
            for cid in t.get("criteria") or []:
                if cid not in ids:
                    err.append(f"{tid}: criterion {cid} does not exist")
                covered.add(cid)
            for f in t.get("files") or []:
                owned.append((f, t.get("owner"), tid))
        for t in tasks:
            for d in t.get("depends_on") or []:
                if d not in tids:
                    err.append(f"{t.get('id')}: depends_on {d} does not exist")
        for i, (f1, o1, t1) in enumerate(owned):
            for f2, o2, t2 in owned[i + 1:]:
                if o1 != o2 and overlaps(f1, f2):
                    err.append(f"file conflict: {f1} ({o1}, {t1}) overlaps {f2} ({o2}, {t2})")
        for cr in c["criteria"]:
            if cr.get("priority") == "must" and cr.get("id") not in covered:
                err.append(f"{cr.get('id')}: must criterion has no task")
    elif c.get("status") == "approved":
        warn.append("no tasks yet: split the work before the team starts")

    if c.get("status") in ("approved", "done"):
        h = (c.get("approved") or {}).get("hash")
        if h and h != criteria_hash(c):
            err.append("approved contract changed after the go: revert or run bump for a new version")
    return err, warn


def cmd_new(slug, title):
    if not re.match(r"^[a-z0-9][a-z0-9-]{1,60}$", slug):
        sys.exit("slug: lowercase letters, digits and hyphens")
    d = CONTRACTS / slug
    p = d / "contract-v001.json"
    if p.exists():
        sys.exit(f"exists: {p}")
    t = load(TEMPLATE)
    c = {
        "id": slug, "version": "001", "status": "draft", "title": title,
        "created": dt.date.today().isoformat(),
        "approved": {"by": "", "date": "", "words": "", "hash": ""},
        "context": {"who_uses": "", "goal": "", "access": "", "limits": [], "out_of_scope": []},
        "module_types": ["base"], "sources": [], "milestones": [], "criteria": [], "tasks": [],
        "limits": copy.deepcopy(t["limits"]),
    }
    d.mkdir(parents=True, exist_ok=True)
    save(p, c)
    print(p)


def cmd_validate(path):
    c = load(path)
    err, warn = validate(c)
    for e in err:
        print("ERROR  " + e)
    for w in warn:
        print("WARN   " + w)
    n = len(c.get("criteria") or [])
    must = sum(1 for x in c.get("criteria") or [] if x.get("priority") == "must")
    print(f"== {len(err)} errors, {len(warn)} warnings · {n} criteria ({must} must) · {len(c.get('tasks') or [])} tasks")
    return 1 if err else 0


def cmd_md(path):
    c = load(path)
    out = [f"# {c['title']} · Vertrag v{c['version']} ({c['status']})", ""]
    ctx = c.get("context", {})
    out += [f"- **Wer nutzt es:** {ctx.get('who_uses','')}", f"- **Ziel:** {ctx.get('goal','')}",
            f"- **Zugang:** {ctx.get('access','')}"]
    if ctx.get("limits"):
        out.append("- **Grenzen:** " + "; ".join(ctx["limits"]))
    if ctx.get("out_of_scope"):
        out.append("- **Nicht Teil davon:** " + "; ".join(ctx["out_of_scope"]))
    out += ["", f"Modultypen: {', '.join(c.get('module_types', []))}", ""]
    src = {s["id"]: s for s in c.get("sources", [])}
    for m in c.get("milestones", []):
        out += [f"## {m['id']} {m.get('title','')}", f"Abschluss: {m.get('exit','')}", "",
                "| ID | Prio | Kategorie | Kriterium | Messung | Prüfung | Quelle |", "|---|---|---|---|---|---|---|"]
        for cr in c.get("criteria", []):
            if cr.get("milestone") != m["id"]:
                continue
            v = cr.get("verify", {})
            s = ", ".join(cr.get("sources", []))
            out.append(f"| {cr['id']} | {cr.get('priority')} | {cr.get('category')} | {cr.get('text','')} | "
                       f"{cr.get('measure','')} | {v.get('method','')}: {v.get('how','')} | {s} |")
        out.append("")
    if c.get("tasks"):
        out += ["## Aufgaben", "", "| Task | Owner | Kriterien | Dateien | Abhängig von |", "|---|---|---|---|---|"]
        for t in c["tasks"]:
            out.append(f"| {t['id']} {t.get('title','')} | {t.get('owner','')} | {', '.join(t.get('criteria', []))} | "
                       f"{', '.join(t.get('files', []))} | {', '.join(t.get('depends_on', [])) or '-'} |")
        out.append("")
    out += ["## Quellen", ""]
    for s in src.values():
        out.append(f"- {s['id']} {s['title']} ({s['type']}, geprüft {s['checked']}): {s['url']}")
    p = Path(path).with_suffix(".md")
    p.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(p)


def cmd_approve(path, words):
    c = load(path)
    err, _ = validate(c)
    if err:
        print("\n".join("ERROR  " + e for e in err))
        sys.exit("not approved: fix the errors first")
    if not words.strip():
        sys.exit("Martin's words are required")
    c["status"] = "approved"
    c["approved"] = {"by": "Martin", "date": dt.date.today().isoformat(), "words": words.strip(), "hash": criteria_hash(c)}
    save(path, c)
    print(f"approved v{c['version']} hash {c['approved']['hash']}")


def cmd_bump(path):
    c = load(path)
    nv = f"{int(c['version']) + 1:03d}"
    c["version"], c["status"] = nv, "draft"
    c["approved"] = {"by": "", "date": "", "words": "", "hash": ""}
    p = Path(path).parent / f"contract-v{nv}.json"
    if p.exists():
        sys.exit(f"exists: {p}")
    save(p, c)
    print(p)


def cmd_tasks(path):
    c = load(path)
    crit = {x["id"]: x for x in c.get("criteria", [])}
    for t in c.get("tasks", []):
        musts = [i for i in t.get("criteria", []) if crit.get(i, {}).get("priority") == "must"]
        dep = ", ".join(t.get("depends_on", [])) or "-"
        print(f"{t['id']} [{t.get('owner')}] {t.get('title')}")
        print(f"    criteria: {', '.join(t.get('criteria', []))} (must: {', '.join(musts) or '-'})")
        print(f"    files (only this owner): {', '.join(t.get('files', []))}")
        print(f"    depends on: {dep}")
        for i in t.get("criteria", []):
            v = crit.get(i, {}).get("verify", {})
            print(f"    {i} done when: {crit.get(i, {}).get('measure','')} · check: {v.get('how','')}")
    return 0


def cmd_verdict(path, results_path):
    c = load(path)
    r = load(results_path)
    mx = (c.get("limits") or {}).get("max_fix_rounds", 2)
    done, rows, escalate = True, [], []
    for cr in c.get("criteria", []):
        res = r.get(cr["id"], {})
        state = res.get("result", "open")
        ev = str(res.get("evidence", "")).strip()
        if state == "pass" and not ev:
            state = "pass?"
        if cr.get("priority") == "must" and state != "pass":
            done = False
        if state == "fail" and int(res.get("rounds", 0)) >= mx:
            escalate.append(cr["id"])
        rows.append((cr["id"], cr.get("milestone"), cr.get("priority"), state, ev[:60]))
    print(f"{'ID':8} {'MS':4} {'PRIO':6} {'RESULT':7} EVIDENCE")
    for row in rows:
        print(f"{row[0]:8} {row[1]:4} {row[2]:6} {row[3]:7} {row[4]}")
    for m in c.get("milestones", []):
        ok = all(r.get(x["id"], {}).get("result") == "pass" and r.get(x["id"], {}).get("evidence")
                 for x in c["criteria"] if x.get("milestone") == m["id"] and x.get("priority") == "must")
        print(f"{m['id']}: {'passed' if ok else 'open'}")
    if escalate:
        print(f"ESCALATE to Martin (failed after {mx} fix rounds): {', '.join(escalate)}")
    print("== DONE: every must criterion passed with evidence" if done else "== NOT DONE")
    return 0 if done else 1


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd, args = argv[1], argv[2:]
    if cmd == "new" and len(args) == 2:
        return cmd_new(*args)
    if cmd == "validate" and len(args) == 1:
        return cmd_validate(args[0])
    if cmd == "md" and len(args) == 1:
        return cmd_md(args[0])
    if cmd == "approve" and len(args) == 2:
        return cmd_approve(*args)
    if cmd == "bump" and len(args) == 1:
        return cmd_bump(args[0])
    if cmd == "tasks" and len(args) == 1:
        return cmd_tasks(args[0])
    if cmd == "verdict" and len(args) == 2:
        return cmd_verdict(*args)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
