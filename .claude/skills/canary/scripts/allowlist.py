#!/usr/bin/env python3
"""Check whether a self-heal action id is on the allow-list.

Usage: python3 allowlist.py check <action-id>
Exit 0 + "ALLOWED (no go needed)" | "ALLOWED (needs Martin's go)" | exit 1 + "NOT ALLOWED".
Reads references/allowlist.md — the file is the source of truth, this script only parses it.
"""
import sys, re
from pathlib import Path

REF = Path(__file__).parent.parent / "references" / "allowlist.md"


def sections():
    text = REF.read_text()
    parts = re.split(r"^## ", text, flags=re.MULTILINE)[1:]
    out = {}
    for p in parts:
        title, _, body = p.partition("\n")
        ids = re.findall(r"^- `([a-z0-9-]+)`", body, flags=re.MULTILINE)
        out[title.strip()] = ids
    return out


def check(action_id):
    secs = sections()
    no_go = secs.get("Allowed (no go needed — read-only or reversible-and-logged)", [])
    needs_go = secs.get("Allowed with Martin's go (G2) — writes into a client system", [])
    if action_id in no_go:
        print(f"ALLOWED (no go needed): {action_id}")
        return 0
    if action_id in needs_go:
        print(f"ALLOWED (needs Martin's go, G2): {action_id}")
        return 0
    print(f"NOT ALLOWED: {action_id} — escalate with a decision card instead. "
          f"See {REF.relative_to(Path.cwd()) if REF.is_relative_to(Path.cwd()) else REF}")
    return 1


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "check":
        print(__doc__)
        sys.exit(2)
    sys.exit(check(sys.argv[2]))
