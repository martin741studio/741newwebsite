#!/usr/bin/env python3
"""Compute the bedrock check per area from harm-register.json. Standard library only.

Usage: python3 -I bedrock.py <run-folder> [--write]
Area A is retired (ownership and access are onboarding preconditions, not harm). Areas are B, C, D, E.
Rules (spec section 12):
  red    = at least one open blocks_revenue item
  yellow = no open blocks_revenue, but more than 10 percent of leaks_link_power items open
  green  = no open blocks_revenue and at most 10 percent of leaks_link_power items open
  grey   = area not scanned (no scanned_areas entry and no items)
"Open" = approval not in {done, rejected-with-reason} and action != keep.
ready_for_growth = areas C, D, E green and no area red.
--write stores the result in run.bedrock of harm-register.json.
"""
import json, sys, pathlib

def is_open(it):
    if it.get("action") == "keep":
        return False
    if it.get("approval") == "done":
        return False
    if it.get("approval") == "rejected" and it.get("action_detail"):
        return False
    return True

def main(argv):
    folder = pathlib.Path(argv[1])
    path = folder / "harm-register.json"
    reg = json.loads(path.read_text(encoding="utf-8"))
    scanned = set(reg.get("run", {}).get("params", {}).get("scanned_areas", list("BCDE")))
    areas = {}
    counts = {}
    for a in "BCDE":
        items = [i for i in reg["items"] if i["area"] == a]
        if a not in scanned:
            areas[a] = "grey"; counts[a] = {}
            continue
        op = [i for i in items if is_open(i)]
        blocks = [i for i in op if i["severity"] == "blocks_revenue"]
        leaks_all = [i for i in items if i["severity"] == "leaks_link_power" and i.get("action") != "keep"]
        leaks_open = [i for i in op if i["severity"] == "leaks_link_power"]
        share = (len(leaks_open) / len(leaks_all)) if leaks_all else 0.0
        if blocks:
            areas[a] = "red"
        elif share > 0.10:
            areas[a] = "yellow"
        else:
            areas[a] = "green"
        counts[a] = {"open": len(op), "blocks_revenue": len(blocks), "leaks_open": len(leaks_open),
                     "leaks_total": len(leaks_all), "leaks_open_share": round(share, 3)}
    ready = all(areas[a] == "green" for a in "CDE") and "red" not in areas.values()
    result = {"areas": areas, "ready_for_growth": ready}
    print(json.dumps({"bedrock": result, "counts": counts}, indent=2, ensure_ascii=False))
    if "--write" in argv:
        reg["run"]["bedrock"] = result
        path.write_text(json.dumps(reg, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
