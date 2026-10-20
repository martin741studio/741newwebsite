import sys, json, collections, urllib.parse
sys.path.insert(0, __file__.rsplit('/',1)[0])
from crawl_lib import *
from ub_lib import ROOT
d = json.load(open(ROOT + "/evidence/area_d/crawl-sitemap.json"))
sm = {canon_key(u) for u in d}
gsc = json.load(open(ROOT + "/../baseline/2026-10-01-gsc-export-90d.json"))
extra = {}
for u, r in d.items():
    for l in r.get("all_links", []):
        h = l["href"]
        if is_internal(h) and canon_key(h) not in sm and not urllib.parse.urlparse(h).path.startswith(("/wp-content", "/wp-includes")):
            extra.setdefault(h, "internal_link_not_in_sitemap")
for p in gsc["pages"]:
    u = p["keys"][0]
    if canon_key(u) not in sm and u not in extra:
        extra[u] = "gsc_page_not_in_sitemap"
# canonical/host variants: www + http
for v in ["https://www.suriya-praxis.de/", "http://suriya-praxis.de/", "https://suriya-praxis.de/index.php", "https://suriya-praxis.de/sitemap.xml", "https://suriya-praxis.de/wp-sitemap.xml", "https://suriya-praxis.de/feed/", "https://suriya-praxis.de/?s=test", "https://suriya-praxis.de/author/admin/", "https://suriya-praxis.de/wp-login.php"]:
    extra.setdefault(v, "probe")
out = {}
for i, (u, why) in enumerate(extra.items(), 1):
    rec = crawl_url(u, subdir="area_d/pages_extra", tag="Dx")
    rec["source"] = why
    out[u] = rec
    print(i, rec.get("final_status"), rec["redirect_hops"], u, "->", rec["final_url"] if rec["redirect_hops"] else "", why, flush=True)
json.dump(out, open(ROOT + "/evidence/area_d/crawl-extra.json", "w"), ensure_ascii=False)
