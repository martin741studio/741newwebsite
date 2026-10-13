#!/usr/bin/env python3
"""Morning grill scan (read only).

Reads the deterministic sources since the bookmark and writes scan.json.
Sources that need MCP tools (session list S1, chat summaries S2, calendar S10)
are passed in as JSON files that the agent writes before this script runs.

Usage:
  python3 scan.py --date 2026-10-13 --bookmark 2026-10-12T06:00+08:00 --out <run dir>
                  [--sessions sessions.json] [--chats s2-chats.json] [--calendar calendar.json]
Every source ends as {"status": "ok"} or {"status": "unreadable", "error": "..."}.
A failed source is never reported as "nothing new".
"""
import argparse, datetime as dt, glob, json, os, re, subprocess, sys

REPO = os.environ.get("MG_REPO", "/Users/martindrendel/741website")  # skill may live in ~/.claude/skills
MEM = os.path.expanduser("~/.claude/projects/-Users-martindrendel-741website/memory")
GOALS = os.path.join(REPO, "00_project", "morning-grill-goals.json")
STATE = os.path.join(REPO, "00_project", "assets", "morning-grill", "state")
WITA = dt.timezone(dt.timedelta(hours=8))


def src(fn, *a):
    try:
        data = fn(*a)
        return {"status": "ok", "data": data}
    except Exception as e:  # report, never hide
        return {"status": "unreadable", "error": f"{type(e).__name__}: {e}"}


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def match_client(text, goals):
    t = (text or "").lower()
    for c in goals["clients"]:
        names = [c["client"].lower()] + [a.lower() for a in c.get("aliases", [])]
        if c.get("registry_name"):
            names.append(c["registry_name"].lower())
        if any(n and n in t for n in names):
            return c["client"]
    return None


def read_registry(bm, today):
    reg = load_json(os.path.join(REPO, "00_project", "workflow-registry", "registry.json"))
    approvals, recent = [], []
    for r in reg["runs"]:
        lr = r.get("last_run") or ""
        age = (today - dt.date.fromisoformat(lr)).days if re.match(r"\d{4}-\d{2}-\d{2}$", lr) else None
        if r.get("status", "").startswith("fertig, Freigabe offen"):
            approvals.append({"client": r["client"], "workflow": r["workflow"], "last_run": lr, "age_days": age,
                              "result": r.get("result", ""), "note": r.get("note", "")[:160]})
        if lr >= bm.date().isoformat():
            recent.append({"client": r["client"], "workflow": r["workflow"], "status": r["status"], "last_run": lr})
    return {"approvals_open": approvals, "runs_since_bookmark": recent}


def read_git(bm):
    out = subprocess.run(["git", "-C", REPO, "worktree", "list", "--porcelain"], capture_output=True, text=True, check=True).stdout
    paths = [l.split(" ", 1)[1] for l in out.splitlines() if l.startswith("worktree ")]
    res = []
    for p in paths:
        log = subprocess.run(["git", "-C", p, "log", f"--since={bm.isoformat()}", "--pretty=%h|%ad|%s", "--date=iso"],
                             capture_output=True, text=True).stdout.strip().splitlines()
        dirty = subprocess.run(["git", "-C", p, "status", "--porcelain"], capture_output=True, text=True).stdout.strip().splitlines()
        res.append({"worktree": os.path.basename(p), "commits": [l.split("|", 2) for l in log][:15],
                    "n_commits": len(log), "uncommitted": len(dirty)})
    return res


def read_standup(day):
    d = os.path.join(REPO, "reporting", "standup")
    path = os.path.join(d, f"{day}.json")
    if not os.path.exists(path):
        files = sorted(glob.glob(os.path.join(d, "20*.json")))
        if not files:
            raise FileNotFoundError("no standup json")
        path = files[-1]
    data = load_json(path)
    if not isinstance(data, list) or not data:
        raise ValueError(f"standup file empty or wrong shape: {path}")
    return {"file": os.path.relpath(path, REPO), "clients": data}


def read_nightshift(today=None):
    """v1: REVIEW.md of the latest run folder. v2 (Night Shift v2 runner, D37): state.json + critic/<id>.json + items/<id>/summary.md
    of the newest run folder of the last 2 days (format given by the Night Shift chat 13.10.)."""
    base = os.path.join(REPO, "reporting", "night-shift")
    dirs = sorted(d for d in glob.glob(os.path.join(base, "20*")) if os.path.isdir(d))
    if not dirs:
        raise FileNotFoundError("no night-shift run folder")
    per, head, rev_rel = {}, "", None
    rev = os.path.join(dirs[-1], "REVIEW.md")
    if os.path.exists(rev):
        txt = open(rev, encoding="utf-8").read()
        cur = None
        for line in txt.splitlines():
            if line.startswith("## "):
                cur = line[3:].strip()
            m = re.match(r"- \[( |x)\] (\S+)\s+\*\*(.+?)\*\*.*— (\w+)", line)
            if m and cur:
                per.setdefault(cur, []).append({"ticked": m.group(1) == "x", "item": m.group(3), "result": m.group(4)})
        head = txt.splitlines()[0] if txt else ""
        rev_rel = os.path.relpath(rev, REPO)
    ledger = load_json(os.path.join(base, "processed-feedback.json")) if os.path.exists(os.path.join(base, "processed-feedback.json")) else []
    v2 = None
    today = today or dt.date.today()
    for d in reversed(dirs):
        name = os.path.basename(d)
        try:
            age = (today - dt.date.fromisoformat(name)).days
        except ValueError:
            continue
        if age > 2:
            break
        sp = os.path.join(d, "state.json")
        if not os.path.exists(sp):
            continue
        st = load_json(sp)
        items = []
        for iid, it in (st.get("items") or {}).items():
            crit = os.path.join(d, "critic", f"{iid}.json")
            summ = os.path.join(d, "items", iid, "summary.md")
            c = load_json(crit) if os.path.exists(crit) else {}
            items.append({"id": iid, "title": it.get("title"), "client": it.get("client"), "status": it.get("status"), "attempts": it.get("attempts"),
                          "why": it.get("why"), "fails": c.get("fails") or [], "one_line": c.get("one_line"),
                          "summary": (open(summ, encoding="utf-8").read().strip().splitlines()[:6] if os.path.exists(summ) else []),
                          "summary_file": os.path.relpath(summ, REPO) if os.path.exists(summ) else None})
        v2 = {"date": st.get("date") or name, "folder": os.path.relpath(d, REPO), "runs": st.get("runs"), "usd": st.get("usd"),
              "stopped_reason": st.get("stopped_reason"), "violations": st.get("violations") or [], "items": items}
        break
    pulse = os.path.join(base, "pulse.log")
    last_pulse = open(pulse, encoding="utf-8").read().strip().splitlines()[-1] if os.path.exists(pulse) and os.path.getsize(pulse) else None
    return {"file": rev_rel, "headline": head, "items": per, "ledger_entries": len(ledger), "v2": v2, "pulse": last_pulse}


def read_memory(bm, goals):
    hits = []
    for f in glob.glob(os.path.join(MEM, "*.md")):
        m = dt.datetime.fromtimestamp(os.path.getmtime(f), WITA)
        if m >= bm:
            name = os.path.basename(f)
            hits.append({"file": name, "modified": m.isoformat(timespec="minutes"),
                         "client": match_client(name.replace("-", " "), goals)})
    return sorted(hits, key=lambda h: h["modified"], reverse=True)


def _supabase_get(paths):
    """Read-only PostgREST GETs with the standup admin login (.secrets/standup.env). Never writes."""
    import urllib.request
    env = {}
    for line in open(os.path.join(REPO, ".secrets", "standup.env"), encoding="utf-8"):
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.strip().split("=", 1)
            env[k] = v.strip().strip('"')
    url, anon = env["SUPABASE_URL"], env["SUPABASE_ANON"]
    body = json.dumps({"email": env["STANDUP_EMAIL"], "password": env["STANDUP_PASSWORD"]}).encode()
    req = urllib.request.Request(f"{url}/auth/v1/token?grant_type=password", data=body,
                                 headers={"apikey": anon, "Content-Type": "application/json"})
    token = json.load(urllib.request.urlopen(req, timeout=30))["access_token"]
    out = {}
    for key, path in paths.items():
        r = urllib.request.Request(f"{url}/rest/v1/{path}", headers={"apikey": anon, "Authorization": f"Bearer {token}"})
        out[key] = json.load(urllib.request.urlopen(r, timeout=30))
    return out


def read_citations(today):
    d = _supabase_get({
        "citations": "client_citations?select=client_id,status,last_checked,updated_at,directory:directories(name)",
        "clients": "clients?select=id,name",
        "emails": "listing_emails?select=client_slug,subject,received_at&handled=eq.false&order=received_at.desc&limit=50"})
    names = {c["id"]: c["name"] for c in d["clients"]}
    per = {}
    for r in d["citations"]:
        n = names.get(r["client_id"], r["client_id"])
        b = per.setdefault(n, {"live": 0, "submitted": 0, "planned": 0, "inconsistent": 0, "missing": 0, "planned_stale_14d": 0})
        st = r.get("status") or "missing"
        b[st] = b.get(st, 0) + 1
        ts = (r.get("updated_at") or r.get("last_checked") or "")[:10]
        if st == "planned" and ts and (today - dt.date.fromisoformat(ts)).days > 14:
            b["planned_stale_14d"] += 1
    unhandled = {}
    for e in d["emails"]:
        unhandled[e.get("client_slug") or "?"] = unhandled.get(e.get("client_slug") or "?", 0) + 1
    return {"per_client": per, "listing_emails_unhandled": unhandled}


DEADLINE_WORDS = re.compile(r"(deadline|\bfrist\b|fristende|fällig|due (?:on|by)|läuft ab|expires?|\bby (?=20\d\d-|\d{1,2}\.)|\bbis (?:zum )?(?=20\d\d-|\d{1,2}\.)|abmahnung|\bmahnung|kündigungsfrist|don't miss)", re.I)
URGENT_WORDS = re.compile(r"(abmahnung|anwalt|lawyer|gericht|unterlassung|mahnung|verification|verifizierung|frist|deadline)", re.I)
DONE_WORDS = re.compile(r"(erledigt|done|resolved|gelöst|bezahlt|paid|✅|abgeschlossen|closed)", re.I)
DATE_RX = re.compile(r"(20\d\d-\d\d-\d\d)|(\b\d{1,2}\.\d{1,2}\.(?:20\d\d)?)")


def _parse_date(m, today):
    if m.group(1):
        return dt.date.fromisoformat(m.group(1))
    d, mo, *y = m.group(2).strip(".").split(".")
    year = int(y[0]) if y and y[0] else today.year
    return dt.date(year, int(mo), int(d))


def read_deadlines(today, goals, back=60, ahead=3):
    """Sweep ALL memory files for dated deadlines in [today-back, today+ahead] without a done word (baseline lesson L7)."""
    hits = []
    for f in sorted(glob.glob(os.path.join(MEM, "*.md"))):
        name = os.path.basename(f)
        if name == "MEMORY.md":
            continue
        for line in open(f, encoding="utf-8"):
            if re.match(r"\s*(name|description|type|metadata|originSessionId|modified):", line):
                continue
            for sent in re.split(r"(?<=[.;!?])\s+(?=[A-Z*])|;", line):
                kw = DEADLINE_WORDS.search(sent)
                if not kw or DONE_WORDS.search(sent):
                    continue
                for m in [m for m in DATE_RX.finditer(sent) if m.start() >= kw.start()][:1]:
                    try:
                        d = _parse_date(m, today)
                    except ValueError:
                        continue
                    if today - dt.timedelta(days=back) <= d <= today + dt.timedelta(days=ahead):
                        hits.append({"file": name, "date": d.isoformat(), "overdue_days": (today - d).days,
                                     "urgent": bool(URGENT_WORDS.search(sent)), "client": match_client(name.replace("-", " "), goals),
                                     "text": sent.strip()[:220]})
                        break
    seen, out = set(), []
    for h in sorted(hits, key=lambda h: (not h["urgent"], h["date"])):
        k = (h["file"], h["date"])
        if k not in seen:
            seen.add(k); out.append(h)
    return out[:40]


def read_prospects(bm):
    res = []
    for f in glob.glob(os.path.join(REPO, "00_project", "prospects", "*", "_run.json")):
        r = load_json(f)
        res.append({"slug": os.path.basename(os.path.dirname(f)), "client": r.get("client"), "status": r.get("status"),
                    "last_run": r.get("last_run")})
    return res


def read_cards():
    p = os.path.join(STATE, "cards.json")
    if not os.path.exists(p):
        return {"cards": [], "note": "no ledger yet (first run)"}
    return load_json(p)


def goal_gaps(goals):
    gaps = []
    for c in goals["clients"]:
        if c.get("status") in ("done",):
            continue
        if not c.get("quarter_goal"):
            gaps.append({"client": c["client"], "field": "quarter_goal"})
        for g in c.get("goal_numbers", []):
            if g.get("status") != "confirmed":
                gaps.append({"client": c["client"], "field": f"goal_numbers:{g['metric']}",
                             "baseline": g.get("baseline"), "target": g.get("target")})
        if not c.get("goal_numbers"):
            gaps.append({"client": c["client"], "field": "goal_numbers (none)"})
    return gaps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--bookmark", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--sessions"); ap.add_argument("--chats"); ap.add_argument("--calendar")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.date)
    bm = dt.datetime.fromisoformat(a.bookmark)
    goals = load_json(GOALS)
    scan = {"date": a.date, "bookmark": a.bookmark, "time_zone": "WITA (UTC+8)",
            "read_at": dt.datetime.now(WITA).isoformat(timespec="minutes"), "sources": {}}
    S = scan["sources"]
    S["S1_sessions"] = src(load_json, a.sessions) if a.sessions else {"status": "unreadable", "error": "no sessions file passed"}
    S["S2_chats"] = src(load_json, a.chats) if a.chats else {"status": "unreadable", "error": "no chat summary passed"}
    S["S3_registry"] = src(read_registry, bm, today)
    S["S4_git"] = src(read_git, bm)
    S["S5_standup"] = src(read_standup, a.date)
    S["S6_nightshift"] = src(read_nightshift, today)
    S["S7_citations"] = src(read_citations, today)
    S["S8_tracking"] = {"status": "unreadable", "error": "tracking workflow not built yet"}
    S["S9_memory"] = src(read_memory, bm, goals)
    S["S10_calendar"] = src(load_json, a.calendar) if a.calendar else {"status": "unreadable", "error": "no calendar file passed"}
    S["S11_cards"] = src(read_cards)
    S["S12_prospects"] = src(read_prospects, bm)
    S["S13_deadlines"] = src(read_deadlines, today, goals)
    scan["goal_gaps"] = goal_gaps(goals)
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "scan.json"), "w", encoding="utf-8") as f:
        json.dump(scan, f, ensure_ascii=False, indent=1)
    bad = [k for k, v in S.items() if v["status"] != "ok"]
    print(f"scan.json written · {len(S) - len(bad)}/{len(S)} sources ok · unreadable: {', '.join(bad) or 'none'}")


if __name__ == "__main__":
    sys.exit(main())
