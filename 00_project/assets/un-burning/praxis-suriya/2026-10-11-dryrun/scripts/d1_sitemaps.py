import sys, re, json, urllib.request
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import save_evidence, ROOT
UA = {"User-Agent":"Mozilla/5.0 (compatible; 741-unburning-dryrun/1.0; read-only)"}
def get(u):
    req = urllib.request.Request(u, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read(), r.status
idx, st = get("https://suriya-praxis.de/sitemap_index.xml")
save_evidence("EV-D-sitemap-index", idx, "xml", "urllib GET", "GET https://suriya-praxis.de/sitemap_index.xml", subdir="area_d/sitemaps", note=f"status={st}")
locs = re.findall(r"<loc>(.*?)</loc>", idx.decode())
print(locs)
urls = []
children = {}
for i, c in enumerate(locs):
    b, st = get(c)
    save_evidence(f"EV-D-sitemap-child-{i+1}", b, "xml", "urllib GET", f"GET {c}", subdir="area_d/sitemaps", note=f"status={st}")
    us = re.findall(r"<loc>(.*?)</loc>", b.decode())
    lm = re.findall(r"<url>.*?<loc>(.*?)</loc>(?:.*?<lastmod>(.*?)</lastmod>)?.*?</url>", b.decode(), re.S)
    children[c] = us
    for u in us: urls.append({"url": u, "sitemap": c})
    print(c, len(us))
json.dump({"children": {k: len(v) for k,v in children.items()}, "urls": urls}, open(ROOT+"/evidence/area_d/sitemap-urls.json","w"), indent=1)
print(len(urls))
