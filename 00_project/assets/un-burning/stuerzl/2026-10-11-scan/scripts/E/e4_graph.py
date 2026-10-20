#!/usr/bin/env python3 -I
"""Area E link graph. Reads EV-E-crawl.json + EV-E-crawl-html.tar.gz. Writes scripts/E/_graph.json (intermediate, derived)."""
import json, tarfile, re, os, sys, urllib.parse, collections, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bs4 import BeautifulSoup
from e_lib import ROOT
B = "https://www.stuerzl-steuerstrafrecht.de"
crawl = json.load(open(os.path.join(ROOT, "evidence/area_e/EV-E-crawl.json")))
pages = {p["url"]: p for p in crawl["pages"]}
tf = tarfile.open(os.path.join(ROOT, "evidence/area_e/EV-E-crawl-html.tar.gz"))
members = {m.name: m for m in tf.getmembers()}
def tar_name(i, u): return f"{i:03d}_" + re.sub(r"[^A-Za-z0-9._-]+", "_", u.replace('https://', ''))[:100]
# RAW order == insertion order of crawl_one calls that stored bodies -> pages with 'links' or body_head, in crawl order
order = [p["url"] for p in crawl["pages"] if ("links" in p or "body_head" in p)]
html = {}
for i, u in enumerate(order):
    nm = tar_name(i, u)
    if nm in members and "links" in pages[u] and pages[u].get("discovered_via") != "sitemap_probe" and pages[u].get("final_status") == 200:
        html[u] = tf.extractfile(members[nm]).read().decode("utf-8", "replace")
def key(u):
    u = u.replace("https://stuerzl-steuerstrafrecht.de", B)
    if u == B: return "/"
    p = u.replace(B, "")
    return p if p else "/"
def internal(h): return urllib.parse.urlparse(h).netloc in ("www.stuerzl-steuerstrafrecht.de", "stuerzl-steuerstrafrecht.de")
# per page: component links with addon info
graph = {}
fp_count = collections.Counter()
for u, h in html.items():
    s = BeautifulSoup(h, "html.parser")
    comp = s.select_one("#sp-component")
    items = []
    if comp:
        for a in comp.find_all("a", href=True):
            href = a["href"].strip()
            if href.startswith(("mailto:", "tel:", "javascript:", "#")): continue
            full = urllib.parse.urldefrag(urllib.parse.urljoin(pages[u]["final_url"], href))[0]
            addon = a.find_parent(class_="sppb-addon")
            aid = None
            if addon is not None:
                aid = addon.get("id") or id(addon)
            items.append({"href": full, "text": a.get_text(" ", strip=True)[:100], "addon": str(aid) if aid is not None else None, "internal": internal(full)})
    # block detection: addon with >=4 internal link targets
    by_addon = collections.defaultdict(list)
    for it in items:
        if it["addon"] and it["internal"]: by_addon[it["addon"]].append(key(it["href"]))
    blocks = {a: tuple(sorted(set(v))) for a, v in by_addon.items() if len(set(v)) >= 4}
    for fp in blocks.values(): fp_count[fp] += 1
    graph[u] = {"items": items, "blocks": blocks}
# repeated block = fingerprint with >=3 pages, or the addon holds >= 8 internal links to service-tree pages
rep_fps = {fp for fp, c in fp_count.items() if c >= 2}
out = {}
for u, g in graph.items():
    k = key(pages[u]["final_url"]) if pages[u].get("final_url") else key(u)
    blk_addons = {a for a, fp in g["blocks"].items() if fp in rep_fps}
    ctx, blk = [], []
    for it in g["items"]:
        if not it["internal"]: continue
        (blk if it["addon"] in blk_addons else ctx).append({"to": key(it["href"]), "text": it["text"]})
    out[u] = {"key": key(u), "contextual": ctx, "block": blk, "n_block_addons": len(blk_addons),
              "external_component": sum(1 for it in g["items"] if not it["internal"])}
json.dump({"rep_fingerprints": [list(f) for f in rep_fps], "pages": out}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_graph.json"), "w"), indent=1, ensure_ascii=False)
print(len(out), "pages;", len(rep_fps), "repeated block fingerprints")
for fp in rep_fps: print(fp_count[fp], len(fp), fp[:3])
