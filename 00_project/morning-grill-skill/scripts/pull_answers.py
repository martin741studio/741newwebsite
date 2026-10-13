#!/usr/bin/env python3
"""Pull Martin's portal answers (grill_answers) since the last cursor into the local ledger state/cards.json.
Latest answer per card wins. 'done' answers on walk items go to state/walk-done.json.
Usage: python3 pull_answers.py [--dry]
"""
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sb

MG = os.path.join(sb.REPO, "00_project", "assets", "morning-grill", "state")


def load(p, d):
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else d


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dry", action="store_true"); a = ap.parse_args()
    cur = load(os.path.join(MG, "answers-cursor.json"), {"last_id": 0})
    rows = sb.request("GET", f"grill_answers?id=gt.{cur['last_id']}&order=id.asc&select=id,card_id,run_date,option,note,answered_at")
    print(f"{len(rows)} new answers since id {cur['last_id']}")
    if a.dry or not rows:
        for r in rows: print(" ", r)
        return 0
    led = load(os.path.join(MG, "cards.json"), {"cards": []})
    byid = {c["id"]: c for c in led["cards"]}
    # enrich new ledger entries (client, headline, option texts) from the latest published snapshot
    snap_cards = {}
    try:
        latest = sb.request("GET", "grill_snapshots?order=id.desc&limit=1&select=data")
        snap_cards = {c["id"]: c for c in (latest[0]["data"].get("cards", []) if latest else [])}
    except Exception as e:
        print("note: could not read the latest snapshot for enrichment:", e)
    for r in rows:
        c = byid.get(r["card_id"])
        if not c:
            sc = snap_cards.get(r["card_id"], {})
            c = {"id": r["card_id"], "client": sc.get("client", "?"), "headline": sc.get("headline"), "created": r["run_date"],
                 "options": sc.get("options", {}), "kind": "click" if r["card_id"].startswith("walk-") else "decision"}
            led["cards"].append(c); byid[c["id"]] = c
        c["status"] = "parked" if r["option"] == "park" else "decided"
        c["answer"] = r["option"]
        c["decided_at"] = r["answered_at"]
        c["source_of_answer"] = "portal"
        if r["option"] == "park":
            c["park_reason"] = r["note"]
        elif r["option"] == "own":   # Martin's own words in the portal (13.10.): the note IS the decision
            c["answer_text"] = r["note"]
        else:
            c["answer_text"] = (c.get("options", {}).get(r["option"]) or r["option"]) + (f" ({r['note']})" if r.get("note") else "")
    json.dump(led, open(os.path.join(MG, "cards.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump({"last_id": rows[-1]["id"]}, open(os.path.join(MG, "answers-cursor.json"), "w"))
    print("ledger updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
