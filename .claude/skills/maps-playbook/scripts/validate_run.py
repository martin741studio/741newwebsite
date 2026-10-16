#!/usr/bin/env python3
"""Validate a maps-playbook run. Exit 1 on any error.
Usage: python3 -I validate_run.py <catalog.json> <matrix.json> [tasks.json]
Checks: 77 rows match the catalogue, every non-unknown status has dated evidence,
age rules, confidence rules, n/a reasons, gate flags, task rules."""
import json, sys, datetime

STATUS = {"done", "partly", "missing", "n/a", "unknown"}
CONF = {"verified", "derived", "client_stated", "none"}
ETYPE = {"live", "scan", "document"}

def d(s):
    return datetime.date.fromisoformat(s[:10])

def main(cat_path, mat_path, task_path=None):
    cat = json.load(open(cat_path, encoding="utf-8"))
    mat = json.load(open(mat_path, encoding="utf-8"))
    cm = {m["id"]: m for m in cat["measures"]}
    ages = cat["age_rules_days"]
    as_of = d(mat["as_of"])
    errs, warns = [], []
    rows = {r["id"]: r for r in mat["rows"]}
    if set(rows) != set(cm):
        errs.append(f"row ids differ from catalogue: missing={sorted(set(cm)-set(rows))} extra={sorted(set(rows)-set(cm))}")
    if len(mat["rows"]) != len(rows):
        errs.append("duplicate row ids")
    for i, r in rows.items():
        m = cm.get(i)
        if not m: continue
        st = r.get("status")
        if st not in STATUS: errs.append(f"{i}: bad status {st}"); continue
        if r.get("confidence") not in CONF: errs.append(f"{i}: bad confidence")
        ev = r.get("evidence", [])
        for e in ev:
            if e.get("type") not in ETYPE: errs.append(f"{i}: bad evidence type")
            if not e.get("ref"): errs.append(f"{i}: evidence without ref")
            if not e.get("date"): errs.append(f"{i}: evidence without date")
        if st != "unknown":
            if not ev: errs.append(f"{i}: status {st} without evidence")
            if r.get("confidence") in (None, "none"): errs.append(f"{i}: status {st} without confidence")
        if st == "done" and r.get("confidence") == "client_stated":
            errs.append(f"{i}: client_stated cannot set done")
        if not (r.get("finding_de") or "").strip(): errs.append(f"{i}: empty finding")
        if st == "n/a" and len(r.get("finding_de", "")) < 8: errs.append(f"{i}: n/a without reason")
        # age rule
        src = [e for e in ev if e.get("role", "rule_source") == "rule_source"]
        if st != "unknown" and ev and not src:
            errs.append(f"{i}: only secondary_claim evidence cannot set status {st}")
        if src:
            newest = max(d(e["date"]) for e in src)
            age = (as_of - newest).days
            rule = ages[m["age_class"]]
            if r.get("age_days") is not None and r["age_days"] != age:
                warns.append(f"{i}: age_days {r['age_days']} differs from computed {age}")
            if age > rule and st != "unknown":
                errs.append(f"{i}: evidence {age} days old (rule {rule}) but status {st}; must be unknown/stale")
            if age > rule and not r.get("stale"):
                errs.append(f"{i}: evidence older than rule but stale flag not set")
            if age <= rule and r.get("stale"):
                warns.append(f"{i}: stale flag set but evidence is fresh")
        elif st == "unknown" and not r.get("task_hint"):
            warns.append(f"{i}: unknown without task hint")
        if m["risk_class"] == "OUT" and st not in ("n/a", "unknown"):
            errs.append(f"{i}: OUT measure must be n/a")
        for b in r.get("blocked_by", []) or []:
            if b not in cm and b not in ("un-burning", "client", "none", "audit"):
                errs.append(f"{i}: unknown blocker {b}")
    out_ids = [i for i, m in cm.items() if m["risk_class"] == "OUT"]
    counts = {s: sum(1 for r in rows.values() if r.get("status") == s) for s in STATUS}
    stale = sum(1 for r in rows.values() if r.get("stale"))
    # tasks
    if task_path:
        tk = json.load(open(task_path, encoding="utf-8"))
        for t in tk["tasks"]:
            r = rows.get(t["measure_id"])
            if not r: errs.append(f"task {t['measure_id']}: no matrix row"); continue
            if r["status"] in ("done", "n/a"): errs.append(f"task {t['measure_id']}: task for status {r['status']}")
            m = cm[t["measure_id"]]
            if m["risk_class"] == "GATE" and t.get("kind") != "check" and not t.get("gate"):
                errs.append(f"task {t['measure_id']}: gate measure without gate")
            if t["state"] not in cat["task_states"]: errs.append(f"task {t['measure_id']}: bad state")
            for dep in t.get("depends_on", []):
                if dep not in cm: errs.append(f"task {t['measure_id']}: bad dependency {dep}")
            exp = t["impact"] * t["confidence"] / (t["effort"] + t["risk"])
            if abs(exp - t["score"]) > 0.02: errs.append(f"task {t['measure_id']}: score mismatch")
    print(f"rows={len(rows)} counts={counts} stale={stale} errors={len(errs)} warnings={len(warns)}")
    for e in errs: print("ERROR", e)
    for w in warns: print("WARN", w)
    return 1 if errs else 0

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:4]))
