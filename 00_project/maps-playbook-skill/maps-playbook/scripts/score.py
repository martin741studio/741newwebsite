#!/usr/bin/env python3
"""Turn gaps in matrix.json into ranked tasks.json.
Usage: python3 -I score.py <catalog.json> <matrix.json> <out tasks.json> [driver.json]
driver.json (optional): {"impact_override": {"G14": 3, ...}} from the audit driver result."""
import json, sys

CONF_W = {"verified": 1.0, "derived": 0.75, "client_stated": 0.5, "none": 0.5}

def main(cat_path, mat_path, out_path, driver_path=None):
    cat = json.load(open(cat_path, encoding="utf-8"))
    mat = json.load(open(mat_path, encoding="utf-8"))
    over = json.load(open(driver_path))["impact_override"] if driver_path else {}
    cm = {m["id"]: m for m in cat["measures"]}
    rows = {r["id"]: r for r in mat["rows"]}
    eff = cat["effort_scale"]; high = set(cat["risk_points"]["high_gates"])
    tasks = []
    for i, r in rows.items():
        m = cm[i]
        if r["status"] in ("done", "n/a"): continue
        if m["risk_class"] == "OUT": continue
        check_only = r["status"] == "unknown"
        impact = over.get(i, m["impact_base"])
        conf = CONF_W.get(r.get("confidence", "none"), 0.5)
        effort = eff["S"] if check_only else eff[m["effort"]]
        if m["risk_class"] == "GATE" and not check_only:
            risk = 3 if set(m["gates"]) & high else 2
        else:
            risk = 0
        score = round(impact * conf / (effort + risk), 2)
        deps = [d for d in m["dependencies"] if rows[d]["status"] != "done"]
        blocked = list(r.get("blocked_by") or [])
        blocked = [b for b in blocked if b != "none"]
        if m.get("unburn_overlap") and any(b == "un-burning" for b in blocked): pass
        state = "blocked" if (deps or blocked) and not check_only else "proposed"
        tasks.append(dict(
            measure_id=i, label_de=m["label_de"], pillar=m["pillar"],
            kind="check" if check_only else "change",
            action_text=("Re-check evidence: " + ", ".join(m["evidence_sources"][:2])) if check_only else (r.get("task_hint") or "TODO: agent writes action"),
            owner_type=["agent"] if check_only else m["owner_type"],
            gate=[] if check_only else m["gates"], impact=impact, confidence=conf,
            effort=effort, risk=risk, score=score, phase=m["phase"],
            depends_on=deps, blocked_by=blocked, state=state))
    def key(t):
        ph = {"d1-30": 0, "m2+": 1, "later": 2}[t["phase"]]
        return (t["state"] == "blocked", ph, -t["score"])
    tasks.sort(key=key)
    for n, t in enumerate(tasks, 1): t["rank"] = n
    quick = [t["measure_id"] for t in tasks
             if t["pillar"].startswith("P1") and t["state"] != "blocked" and cm[t["measure_id"]]["impact_from_driver"]][:5]
    out = dict(client=mat["client"], as_of=mat["as_of"], catalog_version=cat["catalog_version"],
               quick_wins=quick, tasks=tasks)
    json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    blocked_n = sum(1 for t in tasks if t["state"] == "blocked")
    print(f"tasks={len(tasks)} blocked={blocked_n} quick_wins={quick}")
    return 0

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:5]))
