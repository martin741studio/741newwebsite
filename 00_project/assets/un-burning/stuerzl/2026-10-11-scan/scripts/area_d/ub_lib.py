"""Shared helpers for Un-Burning scan, area D (STUERZL). Read-only. No secrets stored."""
import hashlib, json, os, datetime, zoneinfo, re, time, urllib.parse
import requests

RUN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # run folder root
EVID = os.path.join(RUN, "evidence")
PART = os.path.join(RUN, "part-D")
MANIFEST = os.path.join(PART, "manifest.json")
TZ = zoneinfo.ZoneInfo("Europe/Berlin")
UA = "741-unburning-scan/1.0"
DELAY = 0.3
SESS = requests.Session()
SESS.headers.update({"User-Agent": UA})
RUN_ID = "stuerzl-2026-10-11-scan"


def now():
    return datetime.datetime.now(TZ).replace(microsecond=0).isoformat()


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def load_manifest():
    if os.path.exists(MANIFEST):
        return json.load(open(MANIFEST, encoding="utf-8"))
    return {"run_id": RUN_ID, "part": "D", "base_dir": "run folder root (2026-10-11-scan/)", "evidence": []}


def save_manifest(m):
    json.dump(m, open(MANIFEST, "w", encoding="utf-8"), indent=1, ensure_ascii=False)


def save_evidence(eid, data, ext, tool, request, subdir="area_d", cost_eur=0, note="", m=None):
    if isinstance(data, str):
        data = data.encode("utf-8")
    d = os.path.join(EVID, subdir)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, f"{eid}.{ext}")
    open(path, "wb").write(data)
    own = m is None
    if own:
        m = load_manifest()
    m["evidence"] = [e for e in m["evidence"] if e["id"] != eid]
    m["evidence"].append({
        "id": eid, "file": os.path.relpath(path, RUN), "sha256": sha256(data), "bytes": len(data),
        "tool": tool, "request": request, "cost_eur": cost_eur, "collected_at": now(), "note": note})
    if own:
        save_manifest(m)
    return eid


def slug_of(url):
    p = urllib.parse.urlparse(url)
    s = (p.netloc + p.path + ("?" + p.query if p.query else "")).strip("/")
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", s)
    return s[:110] or "root"


def fetch_chain(url, max_hops=8, timeout=40):
    """GET only. Manual redirect follow. Returns (chain, response_or_None, error)."""
    chain, cur, last = [], url, None
    for _ in range(max_hops + 1):
        try:
            r = SESS.get(cur, allow_redirects=False, timeout=timeout)
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
            chain.append({"url": cur, "status": None, "error": err})
            return chain, None, err
        time.sleep(DELAY)
        chain.append({"url": cur, "status": r.status_code, "location": r.headers.get("Location")})
        last = r
        if r.status_code in (301, 302, 303, 307, 308) and r.headers.get("Location"):
            cur = urllib.parse.urljoin(cur, r.headers["Location"])
            continue
        return chain, r, None
    return chain, last, "redirect loop or too many hops"
