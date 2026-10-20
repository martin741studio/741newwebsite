import sys, json, os
sys.path.insert(0, __file__.rsplit('/',1)[0])
from crawl_lib import *
from ub_lib import ROOT, save_evidence
urls = [u["url"] for u in json.load(open(ROOT + "/evidence/area_d/sitemap-urls.json"))["urls"]]
recs = {}
for i, u in enumerate(urls, 1):
    rec = crawl_url(u)
    recs[u] = rec
    print(i, rec.get("final_status"), rec["redirect_hops"], u, rec.get("word_count"), flush=True)
json.dump(recs, open(ROOT + "/evidence/area_d/crawl-sitemap.json", "w"), ensure_ascii=False)
# robots.txt
r = SESS.get("https://suriya-praxis.de/robots.txt", timeout=30)
save_evidence("EV-D-robots", r.content, "txt", "requests GET", "GET https://suriya-praxis.de/robots.txt", subdir="area_d", note=f"status={r.status_code}")
print("robots", r.status_code)
