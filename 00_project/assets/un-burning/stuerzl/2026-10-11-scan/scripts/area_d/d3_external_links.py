"""D01: check every external link found in the crawl (GET, stream, no body read). 0.3 s delay."""
import sys, os, json, urllib.parse, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *

crawl = json.load(open(os.path.join(EVID, "area_d", "EV-D-crawl-data.json"), encoding="utf-8"))["pages"]
HOSTS = {"www.stuerzl-steuerstrafrecht.de", "stuerzl-steuerstrafrecht.de"}
ext = {}
for url, p in crawl.items():
    for l in p.get("links", []) or []:
        u = l["url"]
        if not u:
            continue
        if urllib.parse.urlparse(u).netloc.lower() in HOSTS:
            continue
        ext.setdefault(u, set()).add(url)
print(len(ext), "external urls")
res = []
for u in sorted(ext):
    row = {"url": u, "found_on": sorted(ext[u])[:5], "found_on_count": len(ext[u])}
    try:
        r = SESS.get(u, allow_redirects=True, timeout=25, stream=True)
        row["status"] = r.status_code
        row["final_url"] = r.url
        row["hops"] = len(r.history)
        r.close()
    except Exception as e:
        row["status"] = None
        row["error"] = f"{type(e).__name__}: {str(e)[:160]}"
    res.append(row)
    time.sleep(DELAY)
    print(row.get("status"), u[:110], row.get("error", ""))
save_evidence("EV-D-external-links", json.dumps({"collected_at": now(), "count": len(res), "rows": res}, ensure_ascii=False, indent=1), "json",
              "requests GET (stream, follow redirects)", f"GET each external link found in crawl, UA {UA}, delay {DELAY}s",
              note="LinkedIn/Xing and similar often answer 999/403 to bots: such codes are NOT proof of a dead link")
