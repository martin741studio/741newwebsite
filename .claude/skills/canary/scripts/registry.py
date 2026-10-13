#!/usr/bin/env python3
"""Canary registry: one row per check. add | validate | list | set-status.

Registry file: 00_project/canary/canaries.json
Schema is documented in the file's own "_schema" key — read it, don't guess fields.

Usage:
  python3 registry.py validate
  python3 registry.py list [--client "<name>"] [--status live|interim|planned]
  python3 registry.py add --file <row.json>          # row must match _schema; id must be new
  python3 registry.py set-status --id <id> --status live|interim|planned [--note "..."]
"""
import argparse, json, sys, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REG = ROOT / "00_project" / "canary" / "canaries.json"

REQUIRED = ["id", "client", "system", "type", "threshold", "severity",
            "escalation", "owner", "status", "runner", "created"]
VALID_TYPES = {"L", "S", "E", "R", "A"}
VALID_SEVERITY = {"SEV1", "SEV2", "SEV3"}
VALID_STATUS = {"live", "interim", "planned"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$")


def load():
    if not REG.exists():
        print(f"FAIL registry not found: {REG}")
        sys.exit(2)
    return json.loads(REG.read_text())


def save(data):
    REG.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def validate(data=None, quiet=False):
    data = data or load()
    errors = []
    ids = set()
    for i, row in enumerate(data.get("checks", [])):
        where = f"checks[{i}] (id={row.get('id','?')})"
        for field in REQUIRED:
            if not row.get(field) and row.get(field) != 0:
                if field == "note":
                    continue
                errors.append(f"{where}: missing '{field}'")
        rid = row.get("id", "")
        if rid and not ID_RE.match(rid):
            errors.append(f"{where}: id must be kebab-case")
        if rid in ids:
            errors.append(f"{where}: duplicate id")
        ids.add(rid)
        if row.get("type") not in VALID_TYPES:
            errors.append(f"{where}: type must be one of {sorted(VALID_TYPES)}")
        if row.get("severity") not in VALID_SEVERITY:
            errors.append(f"{where}: severity must be one of {sorted(VALID_SEVERITY)}")
        if row.get("status") not in VALID_STATUS:
            errors.append(f"{where}: status must be one of {sorted(VALID_STATUS)}")
        if row.get("type") == "E" and row.get("interval_minutes") not in (None,):
            errors.append(f"{where}: type E (push) must have interval_minutes = null")
        sh = row.get("self_heal")
        if sh:
            allow = (Path(__file__).parent.parent / "references" / "allowlist.md").read_text()
            if sh not in allow:
                errors.append(f"{where}: self_heal '{sh}' not found in references/allowlist.md")
    if errors:
        if not quiet:
            for e in errors:
                print("FAIL", e)
            print(f"FAIL {len(errors)} error(s)")
        return False
    if not quiet:
        print(f"OK {len(data.get('checks', []))} check(s) valid")
    return True


def list_checks(client=None, status=None):
    data = load()
    rows = data.get("checks", [])
    if client:
        rows = [r for r in rows if r.get("client", "").lower() == client.lower()]
    if status:
        rows = [r for r in rows if r.get("status") == status]
    if not rows:
        print("(no matching checks)")
        return
    for r in rows:
        print(f"{r['id']:<40} {r['client']:<20} {r['type']} {r['severity']:<4} "
              f"{r['status']:<8} {r['runner']:<14} -> {r.get('system','')[:50]}")


def add(file_path):
    data = load()
    row = json.loads(Path(file_path).read_text())
    ids = {r["id"] for r in data["checks"]}
    if row.get("id") in ids:
        print(f"FAIL id already exists: {row.get('id')}")
        sys.exit(1)
    data["checks"].append(row)
    if not validate(data):
        print("FAIL new row did not validate, not saved")
        sys.exit(1)
    save(data)
    print(f"OK added {row['id']}")


def set_status(check_id, status, note=None):
    data = load()
    for r in data["checks"]:
        if r["id"] == check_id:
            r["status"] = status
            if note:
                r["note"] = note
            save(data)
            print(f"OK {check_id} -> {status}")
            return
    print(f"FAIL id not found: {check_id}")
    sys.exit(1)


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    lp = sub.add_parser("list")
    lp.add_argument("--client")
    lp.add_argument("--status")
    ap = sub.add_parser("add")
    ap.add_argument("--file", required=True)
    sp = sub.add_parser("set-status")
    sp.add_argument("--id", required=True)
    sp.add_argument("--status", required=True, choices=sorted(VALID_STATUS))
    sp.add_argument("--note")
    args = p.parse_args()

    if args.cmd == "validate":
        sys.exit(0 if validate() else 1)
    elif args.cmd == "list":
        list_checks(args.client, args.status)
    elif args.cmd == "add":
        add(args.file)
    elif args.cmd == "set-status":
        set_status(args.id, args.status, args.note)


if __name__ == "__main__":
    main()
