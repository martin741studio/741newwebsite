#!/usr/bin/env python3
"""Validate pool.json. Exit 0 = pass, 1 = fail. Prints every problem. Fix until it passes.

Usage: validate_pool.py --run-dir <content-pool dir> [--schema content-pool-item.schema.json]
Checks: JSON schema (stdlib subset), unique ids, evidence files exist, volumes match raw data,
fit/priority/status rules, four pillars present, HWG notes, needs_client lists, spend cap, benchmark.
"""
import argparse, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def find_schema(arg):
    for c in [arg, os.path.join(HERE, "..", "assets", "content-pool-item.schema.json"), os.path.join(HERE, "..", "..", "content-pool-item.schema.json")]:
        if c and os.path.exists(c):
            return c
    sys.exit("schema not found")


def check(val, sch, path, errs):
    t = sch.get("type")
    if t:
        ts = t if isinstance(t, list) else [t]
        ok = any((x == "string" and isinstance(val, str)) or (x == "integer" and isinstance(val, int) and not isinstance(val, bool)) or (x == "number" and isinstance(val, (int, float)) and not isinstance(val, bool))
                 or (x == "boolean" and isinstance(val, bool)) or (x == "array" and isinstance(val, list)) or (x == "object" and isinstance(val, dict)) or (x == "null" and val is None) for x in ts)
        if not ok:
            errs.append(f"{path}: type {t}, got {type(val).__name__}")
            return
    if "enum" in sch and val not in sch["enum"]:
        errs.append(f"{path}: {val!r} not in {sch['enum']}")
    if isinstance(val, str) and "pattern" in sch and not re.search(sch["pattern"], val):
        errs.append(f"{path}: {val!r} does not match {sch['pattern']}")
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        if "minimum" in sch and val < sch["minimum"]: errs.append(f"{path}: {val} < {sch['minimum']}")
        if "maximum" in sch and val > sch["maximum"]: errs.append(f"{path}: {val} > {sch['maximum']}")
    if isinstance(val, dict):
        for r in sch.get("required", []):
            if r not in val: errs.append(f"{path}: missing '{r}'")
        props = sch.get("properties", {})
        if sch.get("additionalProperties") is False:
            for k in val:
                if k not in props: errs.append(f"{path}: unknown field '{k}'")
        for k, v in val.items():
            if k in props: check(v, props[k], f"{path}.{k}", errs)
    if isinstance(val, list):
        if "minItems" in sch and len(val) < sch["minItems"]: errs.append(f"{path}: fewer than {sch['minItems']} items")
        if "items" in sch:
            for n, v in enumerate(val): check(v, sch["items"], f"{path}[{n}]", errs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--schema")
    a = ap.parse_args()
    run = a.run_dir.rstrip("/")
    pool = json.load(open(f"{run}/04-pool/pool.json"))
    schema = json.load(open(find_schema(a.schema)))
    errs, warns = [], []
    ids = set()
    vols = {}
    for f in glob.glob(f"{run}/03-demand/volume*.json"):
        if "payload" in f: continue
        for r in json.load(open(f))["tasks"][0].get("result") or []:
            vols[r["keyword"].lower()] = r.get("search_volume")
    for it in pool["items"]:
        e0 = len(errs)
        check(it, schema, it.get("id", "?"), errs)
        i = it.get("id", "?")
        if i in ids: errs.append(f"{i}: duplicate id")
        ids.add(i)
        for ev in it.get("evidence", []):
            if not glob.glob(os.path.join(run, ev["file"])) and ev["type"] not in ("manual",):
                errs.append(f"{i}: evidence file missing: {ev['file']}")
            if ev["type"] == "manual" and not glob.glob(os.path.join(run, ev["file"])):
                warns.append(f"{i}: manual evidence file missing: {ev['file']}")
        for k in it.get("keywords", []):
            raw = vols.get(k["kw"].lower(), "absent")
            if raw != "absent" and raw != k["volume"]:
                errs.append(f"{i}: volume for '{k['kw']}' is {k['volume']} but raw data says {raw}")
            if raw == "absent" and k["volume"] is not None:
                errs.append(f"{i}: volume for '{k['kw']}' has no raw record")
        if it["fit"] == 0 and it["priority"] != "cut": errs.append(f"{i}: fit 0 must be cut")
        if it["fit"] == 1 and (it["status"] != "adjacent_review" or it["priority"] == "A"): errs.append(f"{i}: fit 1 must be adjacent_review and not A")
        if it["compliance"]["flag"] == "block" and it["priority"] != "cut": errs.append(f"{i}: compliance block must be cut")
        if it["compliance"]["flag"] == "review" and not it["compliance"].get("note"): errs.append(f"{i}: compliance review needs a note")
        if it["status"] == "needs_client" and not it.get("needs_client"): errs.append(f"{i}: status needs_client but list is empty")
        if it["priority"] == "A" and it["demand"]["basis"] == "none": errs.append(f"{i}: priority A without any demand basis")
        if it["priority"] == "cut" and not it.get("decision_note"): errs.append(f"{i}: cut item needs decision_note")
        if it["page_tag"] == "homepage" and it["item_type"] in ("block", "faq", "proof") and not it.get("section_hint"):
            warns.append(f"{i}: homepage item without section_hint")
        if it["competitor"]["denominator"] < 3 and it["competitor"]["set"] and it["competitor"]["covering"] == 0 and it["competitor"].get("note") is None:
            warns.append(f"{i}: competitor denominator under 3")
    live = [x for x in pool["items"] if x["priority"] != "cut"]
    for pl in ("location", "service", "brand", "authority"):
        n = sum(1 for x in live if x["pillar"] == pl)
        if n < 3: errs.append(f"pillar {pl}: only {n} live items (need 3)")
    meta = pool["meta"]
    if meta["spend_usd"] > meta["cap_usd"]: errs.append(f"spend {meta['spend_usd']} over cap {meta['cap_usd']}")
    if not meta.get("benchmark"): errs.append("meta.benchmark missing (gate A0)")
    for u in meta.get("unreadable_competitors", []): warns.append(f"competitor unreadable, report it: {u}")
    print(f"{len(pool['items'])} items, {len(errs)} errors, {len(warns)} warnings")
    for w in warns: print("WARN ", w)
    for e in errs: print("ERROR", e)
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
