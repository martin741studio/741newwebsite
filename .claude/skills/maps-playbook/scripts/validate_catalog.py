#!/usr/bin/env python3
"""Validate maps-playbook-measure-catalog.json. Exit 1 on any error.
Usage: python3 -I validate_catalog.py <catalog.json>"""
import json, sys, re

REQ = ["id","pillar","group","label_de","source","risk_class","gates","gate_text","alternative","dach_adaptation",
       "niche_rules","audit_feed","linked_asset","coverage","evidence_sources","age_class","automation","effort",
       "owner_type","dependencies","cadence","status_rules","impact_base","impact_from_driver","phase","runbook","unburn_overlap","unburn_checks"]

def main(path):
    import os
    c = json.load(open(path, encoding="utf-8"))
    rb = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'references', 'runbooks.md'), encoding='utf-8').read()
    ms = c["measures"]; errs = []
    ids = [m["id"] for m in ms]
    if len(ids) != len(set(ids)): errs.append("duplicate ids")
    gates = set(c["gates"]); ages = set(c["age_rules_days"]); codes = set(c["automation_codes"])
    phases = set(c["phases"]); eff = set(c["effort_scale"])
    for m in ms:
        i = m.get("id", "?")
        for k in REQ:
            if k not in m: errs.append(f"{i}: missing field {k}")
        if m.get("risk_class") not in ("DO","GATE","OUT"): errs.append(f"{i}: bad risk_class")
        if m.get("risk_class") in ("GATE","OUT"):
            if not m.get("gates"): errs.append(f"{i}: gate class without gate number")
            if not m.get("gate_text"): errs.append(f"{i}: gate class without gate_text")
            if not m.get("alternative") and m.get("risk_class") == "OUT": errs.append(f"{i}: OUT without alternative")
        for g in m.get("gates", []):
            if g.strip() not in gates: errs.append(f"{i}: unknown gate {g}")
        if m.get("age_class") not in ages: errs.append(f"{i}: bad age_class")
        for a in m.get("automation", []):
            if a not in codes: errs.append(f"{i}: bad automation code {a}")
        if m.get("effort") not in eff: errs.append(f"{i}: bad effort")
        if m.get("phase") not in phases: errs.append(f"{i}: bad phase")
        for d in m.get("dependencies", []):
            if d not in ids: errs.append(f"{i}: dependency {d} not in catalogue")
            if d == i: errs.append(f"{i}: depends on itself")
        if not (1 <= m.get("impact_base", 0) <= 5): errs.append(f"{i}: impact out of range")
        for k in ("health","trades_local","law_tax"):
            if k not in m.get("niche_rules", {}): errs.append(f"{i}: niche_rules missing {k}")
        if not m.get("evidence_sources"): errs.append(f"{i}: no evidence source")
        if not re.match(r"^[GWO]\d\d$", i): errs.append(f"{i}: bad id pattern")
        if f"## {m.get('runbook')} " not in rb: errs.append(f"{i}: runbook {m.get('runbook')} not found in runbooks.md")
    # dependency cycles
    graph = {m["id"]: m.get("dependencies", []) for m in ms}
    def cyc(n, stack):
        if n in stack: return True
        return any(cyc(x, stack | {n}) for x in graph.get(n, []))
    for n in graph:
        if cyc(n, frozenset()): errs.append(f"{n}: dependency cycle")
    stats = {k: sum(1 for m in ms if m["risk_class"] == k) for k in ("DO","GATE","OUT")}
    print(f"measures={len(ms)} classes={stats} errors={len(errs)}")
    for e in errs: print("ERROR", e)
    return 1 if errs else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
