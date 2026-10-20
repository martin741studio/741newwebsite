"""Derive Area D/E metrics from the crawl evidence. Pure local computation."""
import sys, json, re, itertools, collections, urllib.parse
sys.path.insert(0, __file__.rsplit('/',1)[0])
from crawl_lib import canon_key, is_internal
from ub_lib import ROOT, now
sm = json.load(open(ROOT + "/evidence/area_d/crawl-sitemap.json"))
ex = json.load(open(ROOT + "/evidence/area_d/crawl-extra.json"))
gsc = json.load(open(ROOT + "/../baseline/2026-10-01-gsc-export-90d.json"))
sitemap_meta = json.load(open(ROOT + "/evidence/area_d/sitemap-urls.json"))
smap_of = collections.defaultdict(list)
for u in sitemap_meta["urls"]: smap_of[u["url"]].append(u["sitemap"].rsplit("/",1)[-1])
gsc_by = {canon_key(p["keys"][0]): p for p in gsc["pages"]}
def path(u): return urllib.parse.urlparse(u).path
pages = {}
for u, r in sm.items():
    pages[canon_key(u)] = r
# inbound content links
inb = collections.defaultdict(set); outl = {}
for k, r in pages.items():
    out = set()
    for l in r.get("content_links", []):
        if is_internal(l["href"]):
            t = canon_key(l["href"])
            if t != k: out.add(t)
    outl[k] = out
    for t in out: inb[t].add(k)
# all-links inbound (incl. nav/sidebar/footer)
inb_all = collections.defaultdict(set)
for k, r in pages.items():
    for l in r.get("all_links", []):
        if is_internal(l["href"]):
            t = canon_key(l["href"])
            if t != k: inb_all[t].add(k)
# shingles
def shingles(text, n=5):
    w = re.sub(r"[^\wäöüß ]", " ", text.lower()).split()
    return {" ".join(w[i:i+n]) for i in range(max(0, len(w)-n+1))}
sh = {k: shingles(r.get("text", "")) for k, r in pages.items()}
near = []
keys = list(pages)
for a, b in itertools.combinations(keys, 2):
    A, B = sh[a], sh[b]
    if len(A) < 30 or len(B) < 30: continue
    inter = len(A & B)
    if not inter: continue
    j = inter / len(A | B); c = inter / min(len(A), len(B))
    if j >= 0.35 or c >= 0.6:
        near.append({"a": a, "b": b, "jaccard": round(j, 3), "containment_of_smaller": round(c, 3)})
near.sort(key=lambda x: -x["jaccard"])
exact = collections.defaultdict(list)
for k, r in pages.items():
    if r.get("word_count", 0) > 20: exact[r["text_hash"]].append(k)
exact = [v for v in exact.values() if len(v) > 1]
titles = collections.defaultdict(list)
for k, r in pages.items(): titles[(r.get("title") or "").strip()].append(k)
dup_titles = {t: v for t, v in titles.items() if len(v) > 1}
descs = collections.defaultdict(list)
for k, r in pages.items(): descs[(r.get("meta_description") or "").strip()].append(k)
dup_desc = {t: v for t, v in descs.items() if len(v) > 1 and t}
res = {"collected_at": now(), "n_sitemap_urls_unique": len(pages), "n_sitemap_entries": len(sitemap_meta["urls"]),
       "sitemap_duplicate_entries": [u for u, s in smap_of.items() if len(s) > 1],
       "near_duplicates": near, "exact_duplicates": exact, "duplicate_titles": dup_titles, "duplicate_meta_descriptions": dup_desc}
rows = []
for k, r in pages.items():
    g = gsc_by.get(k)
    rows.append({"key": k, "url": r["url"], "final_url": r["final_url"], "status": r["final_status"], "hops": r["redirect_hops"],
                 "canonical": r.get("canonical"), "meta_robots": r.get("meta_robots"), "title": r.get("title"),
                 "h1_count": r.get("h1_count"), "word_count": r.get("word_count"), "inbound_content": sorted(inb.get(k, [])),
                 "inbound_all_count": len(inb_all.get(k, [])), "outbound_content": sorted(outl.get(k, [])),
                 "hwg": len(r.get("hwg_matches", [])), "slop": r.get("slop_hits"), "gsc_clicks_90d": g["keys"] and g["clicks"] if g else 0,
                 "gsc_impr_90d": g["impressions"] if g else 0, "sitemap": smap_of[r["url"]]})
res["rows"] = rows
json.dump(res, open(ROOT + "/evidence/area_d/analysis.json", "w"), ensure_ascii=False, indent=1)
print("near", len(near), "exact", exact, "dup titles", {t: [path(x) for x in v] for t, v in dup_titles.items()})
print("dup desc", {t[:50]: [path(x) for x in v] for t, v in dup_desc.items()})
for n in near[:25]: print(n["jaccard"], n["containment_of_smaller"], n["a"], n["b"])
