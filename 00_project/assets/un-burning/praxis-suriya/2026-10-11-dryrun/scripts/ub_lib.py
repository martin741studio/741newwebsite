"""Shared helpers for the Un-Burning dry run. Read-only. No secrets are stored."""
import hashlib, json, os, datetime, zoneinfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVID = os.path.join(ROOT, "evidence")
MANIFEST = os.path.join(ROOT, "manifest.json")
TZ = zoneinfo.ZoneInfo("Europe/Berlin")

def now():
    return datetime.datetime.now(TZ).replace(microsecond=0).isoformat()

def sha256(b):
    return hashlib.sha256(b).hexdigest()

def load_manifest():
    if os.path.exists(MANIFEST):
        return json.load(open(MANIFEST))
    return {"run_id": "praxis-suriya-2026-10-11-dryrun", "evidence": []}

def save_manifest(m):
    json.dump(m, open(MANIFEST, "w"), indent=1, ensure_ascii=False)

def save_evidence(eid, data, ext, tool, request, subdir="", cost_eur=0, note=""):
    """Save raw bytes (or str) as evidence file, add manifest row. Returns eid."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    d = os.path.join(EVID, subdir) if subdir else EVID
    os.makedirs(d, exist_ok=True)
    fn = f"{eid}.{ext}"
    path = os.path.join(d, fn)
    open(path, "wb").write(data)
    m = load_manifest()
    m["evidence"] = [e for e in m["evidence"] if e["id"] != eid]
    m["evidence"].append({
        "id": eid,
        "file": os.path.relpath(path, ROOT),
        "sha256": sha256(data),
        "bytes": len(data),
        "tool": tool,
        "request": request,
        "cost_eur": cost_eur,
        "collected_at": now(),
        "note": note,
    })
    save_manifest(m)
    return eid
