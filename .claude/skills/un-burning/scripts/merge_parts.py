#!/usr/bin/env python3
"""Merge area part folders into one run folder. Standard library only.

Usage: python3 -I merge_parts.py <run-folder> --client-slug <slug> --domain <domain> [--mode scan]
                                 [--scanned A,C,D,E] [--sources-unreadable <json-file>]
Reads <run-folder>/part-*/harm-register.json and part-*/manifest.json.
Writes <run-folder>/harm-register.json, manifest.json and run.json.
Rules: item ids must be unique across parts; evidence ids must be unique across manifests;
an item area must match its id; no item is changed. Errors stop the merge (exit 1).
Run validate_run.py afterwards.
"""
import json, sys, pathlib, datetime, argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder"); ap.add_argument("--client-slug", required=True); ap.add_argument("--domain", required=True)
    ap.add_argument("--mode", default="scan"); ap.add_argument("--scanned", default="A,C,D,E")
    ap.add_argument("--sources-unreadable", default=None); ap.add_argument("--notes", default="")
    a = ap.parse_args()
    folder = pathlib.Path(a.folder)
    items, evidence, errors = [], {}, []
    seen = set()
    for part in sorted(folder.glob("part-*")):
        reg = json.loads((part / "harm-register.json").read_text(encoding="utf-8"))
        for it in reg["items"]:
            if it["id"] in seen:
                errors.append(f"duplicate item id {it['id']} (part {part.name})")
            seen.add(it["id"])
            if it["id"].split("-")[1] != it["area"]:
                errors.append(f"{it['id']}: id area differs from area {it['area']}")
            items.append(it)
        mp = part / "manifest.json"
        if mp.exists():
            m = json.loads(mp.read_text(encoding="utf-8"))
            ents = m.get("evidence", m) if isinstance(m, dict) else m
            if isinstance(ents, dict):
                ents = [{"id": k, **v} for k, v in ents.items()]
            for e in ents:
                if e["id"] in evidence:
                    errors.append(f"duplicate evidence id {e['id']} (part {part.name})")
                evidence[e["id"]] = e
    if errors:
        print("\n".join(errors)); print(f"MERGE FAILED: {len(errors)} errors"); return 1
    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    day = now[:10]
    run = {"run_id": f"{a.client_slug}-{day}-{a.mode}", "client_slug": a.client_slug, "client_id": None,
           "domain": a.domain, "mode": a.mode, "from_audit_run": None, "previous_run_id": None,
           "started_at": now, "timezone": "Europe/Berlin", "catalog_version": "ub-1",
           "params": {"scanned_areas": a.scanned.split(","), "parts": sorted(p.name for p in folder.glob("part-*")), "notes": a.notes},
           "cost": {"eur": 0}}
    nm = folder / "nap-master.json"
    if nm.exists():
        run["client_id"] = json.loads(nm.read_text(encoding="utf-8")).get("client_id")
    items.sort(key=lambda i: i["id"])
    (folder / "harm-register.json").write_text(json.dumps({"run": run, "items": items}, indent=2, ensure_ascii=False), encoding="utf-8")
    (folder / "manifest.json").write_text(json.dumps({"evidence": sorted(evidence.values(), key=lambda e: e["id"])}, indent=2, ensure_ascii=False), encoding="utf-8")
    runjson = {**run}
    if a.sources_unreadable:
        runjson["sources_unreadable"] = json.loads(pathlib.Path(a.sources_unreadable).read_text(encoding="utf-8"))
    (folder / "run.json").write_text(json.dumps(runjson, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"merged {len(items)} items, {len(evidence)} evidence rows from {len(run['params']['parts'])} parts")
    return 0

if __name__ == "__main__":
    sys.exit(main())
