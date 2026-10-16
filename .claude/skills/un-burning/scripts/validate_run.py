#!/usr/bin/env python3
"""Validate an Un-Burning run folder. Standard library only.

Usage: python3 -I validate_run.py <run-folder> [--schema <harm-register.schema.json>]
Exit 0 = valid. Exit 1 = errors (printed, one per line).
Checks: required fields, enums, id pattern, evidence exists in manifest.json,
done-rule (snapshot, before, after, done_at, approved_at), destructive rows need
per-item approval before done, confidence and date present. Never guesses.
"""
import json, re, sys, pathlib

ID_RE = re.compile(r"^H-[B-E]-[0-9]{3}$")
CHECK_RE = re.compile(r"^UB\.[B-E][0-9]{2}$")
ENUMS = {
    "entity": {"domain", "hosting", "cms", "website", "gbp", "listing", "social", "backlink", "review", "search_index", "analytics"},
    "severity": {"blocks_revenue", "leaks_link_power", "cosmetic"},
    "action": {"keep", "fix", "merge", "redirect", "delete", "report", "claim"},
    "actor": {"client", "741", "google"},
    "effort": {"S", "M", "L"},
    "approval": {"proposed", "approved", "rejected", "done", "blocked"},
    "confidence": {"verified", "derived", "client_stated"},
}
REQUIRED = ["id", "area", "entity", "item", "check_id", "severity", "action", "actor", "effort",
            "approval", "confidence", "collected_at", "evidence_ids"]
DESTRUCTIVE_ACTIONS = {"delete", "report", "merge"}
ALLOWED = set(REQUIRED) | {"why", "source_field", "target", "action_detail", "destructive", "approved_by",
    "approved_at", "wave", "snapshot_id", "rollback", "before", "after", "verify_check", "done_at",
    "source_tool", "refetch", "depends_on", "drilldown_hint", "client_safe", "client_text"}


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def main(argv):
    if len(argv) < 2:
        print("usage: validate_run.py <run-folder>")
        return 2
    folder = pathlib.Path(argv[1])
    errors = []
    reg_path = folder / "harm-register.json"
    if not reg_path.exists():
        print(f"missing {reg_path}")
        return 1
    reg = load(reg_path)
    manifest = {}
    mpath = folder / "manifest.json"
    if mpath.exists():
        m = load(mpath)
        entries = m.get("evidence", m) if isinstance(m, dict) else m
        if isinstance(entries, dict):
            manifest = entries
        else:
            manifest = {e.get("id"): e for e in entries if isinstance(e, dict)}
    else:
        errors.append("manifest.json missing")

    run = reg.get("run", {})
    for k in ["run_id", "client_slug", "domain", "mode", "started_at", "catalog_version", "params"]:
        if k not in run:
            errors.append(f"run.{k} missing")

    seen = set()
    for it in reg.get("items", []):
        iid = it.get("id", "?")
        if iid in seen:
            errors.append(f"{iid}: duplicate id")
        seen.add(iid)
        for k in REQUIRED:
            if k not in it:
                errors.append(f"{iid}: missing {k}")
        for k in it:
            if k not in ALLOWED:
                errors.append(f"{iid}: unknown field {k}")
        if "id" in it and not ID_RE.match(it["id"]):
            errors.append(f"{iid}: bad id pattern")
        if "check_id" in it and not CHECK_RE.match(it["check_id"]):
            errors.append(f"{iid}: bad check_id")
        if it.get("area") == "A":
            errors.append(f"{iid}: area A is retired. Ownership and access belong to onboarding (preconditions.json), not to the register")
        elif it.get("area") not in set("BCDE"):
            errors.append(f"{iid}: bad area")
        elif iid.startswith("H-") and iid[2:3] != "-" and iid.split("-")[1] != it.get("area"):
            errors.append(f"{iid}: id area differs from area field")
        for k, allowed in ENUMS.items():
            if k in it and it[k] not in allowed:
                errors.append(f"{iid}: {k}={it[k]!r} not allowed")
        ev = it.get("evidence_ids") or []
        if not ev:
            errors.append(f"{iid}: no evidence (unsourced claim)")
        for e in ev:
            if manifest and e not in manifest:
                errors.append(f"{iid}: evidence {e} not in manifest")
        if it.get("action") in DESTRUCTIVE_ACTIONS and it.get("destructive") is not True:
            errors.append(f"{iid}: action {it['action']} must set destructive=true")
        if it.get("approval") in {"approved", "done"}:
            for k in ["approved_at", "approved_by"]:
                if not it.get(k):
                    errors.append(f"{iid}: approval {it['approval']} needs {k}")
        if it.get("approval") == "done":
            for k in ["snapshot_id", "rollback", "before", "after", "done_at", "verify_check"]:
                if it.get(k) in (None, "", {}):
                    errors.append(f"{iid}: done needs {k}")
        if it.get("action") == "delete" and it.get("approval") in {"approved", "done"} and not it.get("snapshot_id"):
            errors.append(f"{iid}: delete without snapshot")

    if errors:
        print("\n".join(errors))
        print(f"INVALID: {len(errors)} errors in {len(reg.get('items', []))} items")
        return 1
    print(f"VALID: {len(reg.get('items', []))} items")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
