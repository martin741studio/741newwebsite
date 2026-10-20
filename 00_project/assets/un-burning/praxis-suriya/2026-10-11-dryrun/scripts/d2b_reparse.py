"""Re-parse saved HTML evidence with the current parse_page (no new requests)."""
import sys, json, os
sys.path.insert(0, __file__.rsplit('/',1)[0])
from crawl_lib import parse_page
from ub_lib import ROOT
for name in ["crawl-sitemap.json", "crawl-extra.json"]:
    p = ROOT + "/evidence/area_d/" + name
    d = json.load(open(p))
    n = 0
    for u, r in d.items():
        f = None
        if r.get("evidence_id"):
            m = json.load(open(ROOT + "/manifest.json"))
            f = next((e["file"] for e in m["evidence"] if e["id"] == r["evidence_id"]), None)
        if not f: continue
        html = open(os.path.join(ROOT, f), encoding="utf8", errors="replace").read()
        r.update(parse_page(u, r["final_url"], html, {"X-Robots-Tag": r.get("x_robots_tag")} if r.get("x_robots_tag") else {}))
        n += 1
    json.dump(d, open(p, "w"), ensure_ascii=False)
    print(name, n)
