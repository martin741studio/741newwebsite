#!/usr/bin/env python3
"""Publish <run>/tasks.json into the client-work model (work_items) in Supabase 741-portal (D36).

Rules (from 00_project/client-work-visibility/data-model.md and the live triggers work_items_guard / done_proof_check):
- Upsert on (source='grill', source_id='<run date>/<task id>'); a rerun changes nothing.
- accountable is ALWAYS Martin. doer = the owner's work_actor.
- status: open->planned, drafted->planned (+status_reason 'draft'), in_progress, waiting (+waiting_on required),
  agent 'done' -> needs_check. A task becomes 'done' ONLY when Martin's own click 'Done' on its card exists in the ledger
  (source portal); then evidence (relation proves) is written first and Martin is the verifier.
- Never touch rows that are already done or dropped. Never delete.
- Evidence: link -> kind file, session -> kind chat (relation produced for agent tasks, else used).
- One decision event per task with a source card (idempotent key).
Usage: python3 publish_tasks.py --run <run dir> [--dry]
"""
import argparse, json, os, sys, re, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sb

REPO = sb.REPO
GOALS = os.path.join(REPO, "00_project", "morning-grill-goals.json")
LEDGER = os.path.join(REPO, "00_project", "assets", "morning-grill", "state", "cards.json")
OWNER_ACTOR = {"Martin": "Martin", "agent": "Agent (Chat)", "Dinakar": "Dinakar", "Tantri": "Tantri", "Gayo": "Gayo", "external": "Extern"}
STATUS = {"open": "planned", "drafted": "planned", "in_progress": "in_progress", "waiting": "waiting", "done": "needs_check"}


def load(p, d=None):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def q(path):
    return sb.request("GET", path)


def match_client(name, db_clients, goals):
    n = (name or "").lower()
    if n.startswith("741"):
        return None
    keys = [n]
    for g in goals["clients"]:
        if g["client"].lower() == n or n.startswith(g["client"].lower()[:8]):
            keys += [a.lower() for a in g.get("aliases", [])] + [(g.get("registry_name") or "").lower()]
    for c in db_clients:
        cn = c["name"].lower()
        if any(k and (k in cn or cn in k) for k in keys):
            return c["id"]
    return None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--run", required=True); ap.add_argument("--dry", action="store_true"); a = ap.parse_args()
    tasks = load(os.path.join(a.run, "tasks.json"), [])
    snap = load(os.path.join(a.run, "snapshot.json"), {})
    day = snap.get("date") or os.path.basename(a.run.rstrip("/"))[:10]
    goals = load(GOALS, {"clients": []}); ledger = {c["id"]: c for c in load(LEDGER, {"cards": []})["cards"]}
    actors = {x["name"]: x for x in q("work_actors?select=id,kind,name")}
    db_clients = q("clients?select=id,name")
    existing = {x["source_id"]: x for x in q("work_items?source=eq.grill&select=id,source_id,status,title")}
    martin = actors["Martin"]["id"]; grill = actors["Morning Grill"]["id"]
    ops = {"insert": 0, "update": 0, "skip_done": 0, "done_set": 0, "evidence": 0, "events": 0}
    for t in tasks:
        sid = f"{day}/{t['id']}"
        owner_name = OWNER_ACTOR.get(t["owner"], "Extern")
        if t["owner"] == "external" and "google" in (t["title"] + " " + (t.get("next") or "")).lower():
            owner_name = "Google"
        doer = actors[owner_name]["id"]
        client_id = match_client(t.get("client"), db_clients, goals)
        title = t["title"] if client_id or (t.get("client") or "").startswith("741") or not t.get("client") else f"{t['client']}: {t['title']}"
        status = STATUS.get(t["status"], "planned")
        card = ledger.get(t.get("card") or "")
        martin_done = bool(card and card.get("status") == "decided" and card.get("source_of_answer") == "portal"
                           and (card.get("options", {}).get(card.get("answer")) == "Done"))
        row_old = existing.get(sid)
        if row_old and row_old["status"] in ("done", "dropped"):
            ops["skip_done"] += 1; continue
        waiting_on = None
        if status == "waiting":
            waiting_on = t.get("waiting_on") or ("google" if owner_name == "Google" else "external" if owner_name == "Extern" else "martin")
        payload = {"source": "grill", "source_id": sid, "type": "task", "title": title, "client_id": client_id, "status": status if not martin_done else "needs_check",
                   "waiting_on": waiting_on, "accountable_id": martin, "doer_id": doer, "due_on": t.get("due"), "next_action": t.get("next"),
                   "status_reason": "draft" if t["status"] == "drafted" else None, "visibility": "internal", "since": day}
        ops["update" if row_old else "insert"] += 1
        if a.dry:
            print(("UPDATE " if row_old else "INSERT ") + sid, "|", payload["status"], "|", owner_name, "|", title[:60], "| done-by-Martin" if martin_done else ""); continue
        res = sb.request("POST", "work_items?on_conflict=source,source_id", payload, prefer="resolution=merge-duplicates,return=representation")
        item_id = res[0]["id"]
        # evidence from link / session
        rel = "produced" if t["owner"] == "agent" else "used"
        evs = []
        if t.get("link"):
            path = re.split(r"\s+\(", t["link"])[0].strip()
            local = os.path.join(a.run, path)
            url = os.path.relpath(local, REPO) if os.path.exists(local) else path
            evs.append({"kind": "file", "relation": rel, "label": t["link"][:120], "url": url})
        if t.get("session"):
            evs.append({"kind": "chat", "relation": rel, "label": "chat " + t["session"][-12:], "url": t["session"]})
        for e in evs:
            sb.request("POST", "work_evidence?on_conflict=work_item_id,label,relation", {"work_item_id": item_id, "client_id": client_id, **e, "created_by": grill, "visibility": "internal"}, prefer="resolution=ignore-duplicates")
            ops["evidence"] += 1
        if t.get("card") or t.get("source_card"):
            sb.request("POST", "work_events?on_conflict=idempotency_key", {"work_item_id": item_id, "client_id": client_id, "actor_id": grill, "type": "decision",
                       "note": f"source card {t.get('card') or t.get('source_card')}", "idempotency_key": f"grill:{sid}:card", "visibility": "internal"}, prefer="resolution=ignore-duplicates")
            ops["events"] += 1
        if martin_done:   # Martin's own click is the proof; he verifies
            sb.request("POST", "work_evidence?on_conflict=work_item_id,label,relation", {"work_item_id": item_id, "client_id": client_id, "kind": "portal", "relation": "proves",
                       "label": f"Martin answered 'Done' in the Command Center (card {t['card']})", "url": f"grill_answers:{t['card']}", "created_by": martin, "visibility": "internal"},
                       prefer="resolution=ignore-duplicates")
            sb.request("PATCH", f"work_items?id=eq.{item_id}", {"status": "done", "verified_by": martin})
            ops["done_set"] += 1
    print(("DRY " if a.dry else "") + "tasks:", len(tasks), ops)
    return 0


if __name__ == "__main__":
    sys.exit(main())
