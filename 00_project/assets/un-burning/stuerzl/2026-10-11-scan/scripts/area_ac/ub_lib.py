"""Helpers for scan agent S1 (areas A and C). Read-only. No secrets are stored."""
import hashlib, json, os, datetime, zoneinfo
HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(os.path.dirname(HERE))          # run folder
PART = os.path.join(RUN, "part-AC")
MANIFEST = os.path.join(PART, "manifest.json")
TZ = zoneinfo.ZoneInfo("Europe/Berlin")
RUN_ID = "stuerzl-2026-10-11-scan"

def now():
    return datetime.datetime.now(TZ).replace(microsecond=0).isoformat()

def sha256(b):
    return hashlib.sha256(b).hexdigest()

def load_manifest():
    if os.path.exists(MANIFEST):
        return json.load(open(MANIFEST))
    return {"run_id": RUN_ID, "part": "AC", "path_base": "run folder", "evidence": []}

def save_evidence(eid, data, ext, tool, request, subdir, cost_eur=0, note=""):
    if isinstance(data, str):
        data = data.encode("utf-8")
    d = os.path.join(RUN, "evidence", subdir)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, f"{eid}.{ext}")
    open(path, "wb").write(data)
    m = load_manifest()
    m["evidence"] = [e for e in m["evidence"] if e["id"] != eid]
    m["evidence"].append({"id": eid, "file": os.path.relpath(path, RUN), "sha256": sha256(data),
        "bytes": len(data), "tool": tool, "request": request, "cost_eur": cost_eur,
        "collected_at": now(), "note": note})
    os.makedirs(PART, exist_ok=True)
    json.dump(m, open(MANIFEST, "w"), indent=1, ensure_ascii=False)
    return eid
