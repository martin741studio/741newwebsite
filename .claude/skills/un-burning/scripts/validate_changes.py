#!/usr/bin/env python3
"""Validate the plan file of one wave (changes.json) before execution. Standard library only.

Usage: python3 -I validate_changes.py <changes.json> <harm-register.json>
changes.json = {"wave": 1, "approved_go2_at": "<iso>|null", "changes": [{"item_id": "H-C-001", "target": "...",
  "snapshot_id": "...", "rollback": "...", "verify_check": "...", "before": ..., "after_expected": ...}]}
Blocks the wave if: an item is not approved in the register, a row lacks snapshot/rollback/verify,
a destructive item has no per-item approval, GO-2 time is missing, or the item belongs to another wave.
Exit 0 = wave may run.
"""
import json, sys, pathlib

def main(argv):
    plan = json.loads(pathlib.Path(argv[1]).read_text(encoding="utf-8"))
    reg = json.loads(pathlib.Path(argv[2]).read_text(encoding="utf-8"))
    by_id = {i["id"]: i for i in reg["items"]}
    errors = []
    if not plan.get("approved_go2_at"):
        errors.append("GO-2 timestamp missing (approved_go2_at)")
    for ch in plan.get("changes", []):
        iid = ch.get("item_id")
        it = by_id.get(iid)
        if not it:
            errors.append(f"{iid}: not in register"); continue
        if it.get("approval") != "approved":
            errors.append(f"{iid}: register approval is {it.get('approval')!r}, needs 'approved'")
        if it.get("wave") not in (None, plan.get("wave")):
            errors.append(f"{iid}: belongs to wave {it.get('wave')}")
        for k in ["snapshot_id", "rollback", "verify_check", "target"]:
            if not ch.get(k):
                errors.append(f"{iid}: missing {k}")
        if it.get("destructive") and not (it.get("approved_by") and it.get("approved_at")):
            errors.append(f"{iid}: destructive item needs per-item approval")
        if it.get("action") in {"delete", "merge", "redirect"} and it.get("evidence_ids") == []:
            errors.append(f"{iid}: no evidence")
    if errors:
        print("\n".join(errors)); print(f"WAVE BLOCKED: {len(errors)} errors"); return 1
    print(f"WAVE OK: {len(plan.get('changes', []))} changes"); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
