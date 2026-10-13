#!/usr/bin/env python3
"""Publish <run>/snapshot.json as ONE row into Supabase grill_snapshots (admin-only table, D29).
This is the only write the scheduled run may do. It never touches another table.
Usage: python3 publish_snapshot.py --run <run dir> --mode morning|evening [--dry]
"""
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sb


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--run", required=True); ap.add_argument("--mode", default="morning"); ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    snap = json.load(open(os.path.join(a.run, "snapshot.json"), encoding="utf-8"))
    row = {"run_date": snap["date"], "mode": a.mode, "data": snap}
    size = len(json.dumps(row))
    if a.dry:
        print(f"DRY: would insert 1 row, {size} bytes, {len(snap['cards'])} cards, {len(snap['clients'])} clients"); return 0
    res = sb.request("POST", "grill_snapshots", row, prefer="return=representation")
    print(f"published snapshot id={res[0]['id']} · {a.mode} · {snap['date']} · {size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
