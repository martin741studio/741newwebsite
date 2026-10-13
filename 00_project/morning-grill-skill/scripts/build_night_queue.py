#!/usr/bin/env python3
"""Night queue for the Night Shift v2 runner (D37). Martin's go 13.10.: only items he ticked are written; no answer = no file.

Modes
  --candidates <run dir>   print the open agent tasks of tasks.json as candidates (JSON). The agent turns the night-suitable ones into
                           items (id, client, class, lang, title, brief, inputs, done) and shows them to Martin as the card 'Night queue <date>'.
  --write <items.json> --date YYYY-MM-DD --confirmed-by "<Martin's card answer>" [--replace] [--dry]
                           validate the ticked items and write reporting/night-shift/queue/<date>.json

Limits come from 00_project/night-shift-server-workflow.md sections 2, 3 and 13: classes draft | research | public_audit | build only; at most 8 items;
never send, message, publish, deploy, FTP, live site or portal writes, ads, money, credit-spending scans, login/Chrome work, deletes.
The runner has its own gates; this script is the first gate and rejects before the file exists.
"""
import argparse, json, os, re, sys

REPO = os.environ.get("MG_REPO", "/Users/martindrendel/741website")
QUEUE_DIR = os.path.join(REPO, "reporting", "night-shift", "queue")
CLASSES = {"draft", "research", "public_audit", "build"}
LANGS = {"German", "English"}
MAX_ITEMS = 8
# title / done / inputs: strict (an item whose TITLE is a forbidden action is not a night item)
BAD_TITLE = re.compile(r"\b(send|sende[nt]?|message|whatsapp|e-?mail|publish|publiziere[nt]?|deploy|ftp|upload|go live|live[- ]schalten|login|log in|post|delete|lösche[nt]?|pay|bezahl\w*|buy|kauf\w*|run[_ ]scan|ads?)\b", re.I)
# brief: only hard stops (a brief may say 'no live edit' or 'never publish')
BAD_BRIEF = re.compile(r"\b(run_scan|lastpass|password|passwort|ftp[ _]?(upload|put)|git push|rm -rf|sudo|drop table|credit card|kreditkarte|api[_ ]?key\s*[:=])", re.I)
BAD_INPUT = re.compile(r"(\.env|\.secrets|id_rsa|credentials|password|token)", re.I)


def load(p, d=None):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def candidates(run):
    tasks = load(os.path.join(run, "tasks.json"), [])
    out = [{"task_id": t["id"], "client": t.get("client"), "title": t["title"], "status": t["status"], "next": t.get("next"), "link": t.get("link")}
           for t in tasks if t.get("owner") == "agent" and t.get("status") in ("open", "waiting", "in_progress", "drafted")]
    print(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"# {len(out)} open agent tasks. Night-suitable only: research / draft / public audit / local build. Never: send, publish, deploy, login, money, credit scans.", file=sys.stderr)


def validate(items):
    errs, ids = [], set()
    if not items:
        errs.append("no items")
    if len(items) > MAX_ITEMS:
        errs.append(f"{len(items)} items > max {MAX_ITEMS}")
    for i, it in enumerate(items, 1):
        p = f"item {i} ({it.get('id')})"
        for f in ("id", "client", "class", "lang", "title", "brief", "inputs", "done"):
            if not it.get(f):
                errs.append(f"{p}: missing {f}")
        if not it.get("id"):
            continue
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", it["id"]):
            errs.append(f"{p}: id must be kebab-case")
        if it["id"] in ids:
            errs.append(f"{p}: duplicate id")
        ids.add(it["id"])
        if it.get("class") not in CLASSES:
            errs.append(f"{p}: class '{it.get('class')}' not allowed (night classes: {', '.join(sorted(CLASSES))})")
        if it.get("lang") not in LANGS:
            errs.append(f"{p}: lang must be German or English")
        if BAD_TITLE.search(it.get("title", "")):
            errs.append(f"{p}: title names a forbidden night action: '{BAD_TITLE.search(it['title']).group(0)}'")
        if BAD_BRIEF.search(it.get("brief", "")):
            errs.append(f"{p}: brief contains a hard stop: '{BAD_BRIEF.search(it['brief']).group(0)}'")
        if not str(it.get("done", "")).startswith(f"items/{it['id']}/"):
            errs.append(f"{p}: done must start with 'items/{it['id']}/'")
        for inp in it.get("inputs", []) or []:
            if BAD_INPUT.search(inp):
                errs.append(f"{p}: input looks like a secret: {inp}")
            elif not inp.startswith(("http://", "https://")):
                path = inp.split(" (")[0].strip()
                if not os.path.exists(os.path.join(REPO, path)):
                    errs.append(f"{p}: input path not found: {path}")
    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates"); ap.add_argument("--write"); ap.add_argument("--date"); ap.add_argument("--confirmed-by")
    ap.add_argument("--replace", action="store_true"); ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    if a.candidates:
        candidates(a.candidates); return 0
    if not a.write:
        ap.error("use --candidates or --write")
    if not a.date or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.date):
        ap.error("--date YYYY-MM-DD required")
    if not a.confirmed_by or len(a.confirmed_by.strip()) < 10 or "martin" not in a.confirmed_by.lower():
        print("REFUSED: --confirmed-by must quote Martin's card answer (no answer = no queue file)"); return 2
    items = load(a.write)
    items = items["items"] if isinstance(items, dict) else items
    errs = validate(items or [])
    if errs:
        print("REFUSED:\n" + "\n".join(" - " + e for e in errs)); return 1
    path = os.path.join(QUEUE_DIR, f"{a.date}.json")
    if os.path.exists(path) and not a.replace:
        print(f"REFUSED: {path} exists (hand-made or earlier). Use --replace after Martin said so."); return 1
    doc = {"date": a.date, "confirmed_by": a.confirmed_by.strip(), "items": items}
    if a.dry:
        print(f"DRY OK: {len(items)} items would be written to {path}"); return 0
    os.makedirs(QUEUE_DIR, exist_ok=True)
    json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"written {path} · {len(items)} items · confirmed_by recorded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
