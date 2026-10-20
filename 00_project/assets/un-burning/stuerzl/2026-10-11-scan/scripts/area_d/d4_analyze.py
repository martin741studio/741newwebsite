"""D01-D07: offline analysis of the crawl data. Writes evidence EV-D-analysis (page table, inlinks, dupes, H1 groups, thin, orphans)."""
import sys, os, json, re, itertools, hashlib, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *

crawl = json.load(open(os.path.join(EVID, "area_d", "EV-D-crawl-data.json"), encoding="utf-8"))["pages"]
HOSTS = {"www.stuerzl-steuerstrafrecht.de", "stuerzl-steuerstrafrecht.de"}


def key(u):
    p = urllib.parse.urlparse(u)
    path = p.path or "/"
    return f"https://www.stuerzl-steuerstrafrecht.de{path}" + (f"?{p.query}" if p.query else "")


def ptype(u):
    p = urllib.parse.urlparse(u).path
    q = urllib.parse.urlparse(u).query
    if p in ("/", ""):
        return "home"
    if "/component/content/article/" in p:
        return "news_article"
    if "/component/content/category/" in p or p.endswith("/aktuelles"):
        return "news_category"
    seg = [s for s in p.split("/") if s and s != "index.php"]
    areas = {"steuerstrafrecht", "selbstanzeigen-steuerliche-korrekturen", "ordnungswidrigkeiten", "zollstrafrecht", "arbeitsstrafrecht",
             "korruptionsstrafrecht", "sonstiges-wirtschaftsstrafrecht", "verteidigung-von-individualpersonen", "unternehmensvertretung"}
    if len(seg) == 1 and seg[0] in areas:
        return "service_area"
    if len(seg) == 2 and seg[0] in areas:
        return "service_sub"
    if len(seg) == 1 and seg[0] in ("kanzlei", "team", "leistungen", "friends", "join-our-team", "faq", "kontakt"):
        return "info"
    if len(seg) == 1 and seg[0] in ("impressum", "datenschutz", "nutzungsbedingungen"):
        return "legal"
    if len(seg) == 1 and seg[0] in ("dr-anja-stuerzl", "lea-wimmer", "dr-monika-glogger", "thorben-hoppe", "florentine-jilg",
                                    "maria-bruckmeier", "lenka-schluetter", "jessica-weyel", "nina-gueldenring", "mary"):
        return "team_bio"
    return "other"


pages = {}
for url, p in crawl.items():
    if p.get("final_status") is None:
        continue
    fk = key(p["final_url"])
    rec = pages.setdefault(fk, {"url": p["final_url"], "key": fk, "requested_as": []})
    rec["requested_as"].append({"url": url, "hops": p["redirect_hops"], "chain": [c["status"] for c in p["chain"]]})
    if "evidence_id" in p and "status" not in rec:
        rec.update({
            "status": p["final_status"], "evidence_id": p["evidence_id"], "title": p.get("title"), "meta_description": p.get("meta_description"),
            "canonical": p.get("canonical"), "meta_robots": p.get("meta_robots"), "x_robots_tag": p.get("x_robots_tag"),
            "h1_count": p.get("h1_count"), "h1_texts": p.get("h1_texts"), "h2_count": p.get("h2_count"), "word_count": p.get("word_count"),
            "depth": p.get("depth"), "text": p.get("text"), "jsonld_types": p.get("jsonld_types"), "imgs_no_alt": p.get("imgs_no_alt"),
            "type": ptype(p["final_url"]), "links": p.get("links", [])})
    elif "status" not in rec:
        rec["status"] = p["final_status"]
        rec["type"] = ptype(p["final_url"])
        rec["links"] = []

# inlinks
for k, rec in pages.items():
    rec["content_in"], rec["menu_in"], rec["content_out"] = set(), set(), 0
for k, rec in pages.items():
    seen_out = set()
    for l in rec.get("links", []):
        u = l["url"]
        if not u or urllib.parse.urlparse(u).netloc.lower() not in HOSTS:
            continue
        tk = key(crawl[u]["final_url"]) if u in crawl and crawl[u].get("final_url") else key(u)
        if tk == k:
            continue
        if tk in pages:
            (pages[tk]["content_in"] if l["region"] == "content" else pages[tk]["menu_in"]).add(k)
        if l["region"] == "content" and tk not in seen_out:
            seen_out.add(tk)
            rec["content_out"] += 1

# dead internal links (target 404) with sources
dead = {}
for k, rec in pages.items():
    for l in rec.get("links", []):
        u = l["url"]
        if u and urllib.parse.urlparse(u).netloc.lower() in HOSTS and u in crawl and crawl[u].get("final_status") == 404:
            d = dead.setdefault(u, {"url": u, "raw_hrefs": set(), "texts": set(), "sources": set()})
            d["raw_hrefs"].add(l["raw"]); d["texts"].add(l["text"]); d["sources"].add(k)

# duplicates by shingle
def shingles(t, n=5):
    w = re.findall(r"\w+", t.lower())
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}

ok = {k: r for k, r in pages.items() if r.get("status") == 200 and r.get("text") is not None}
sh = {k: shingles(r["text"]) for k, r in ok.items()}
dupes = []
for a, b in itertools.combinations(ok, 2):
    sa, sb = sh[a], sh[b]
    if not sa or not sb:
        continue
    j = len(sa & sb) / len(sa | sb)
    contain = len(sa & sb) / min(len(sa), len(sb))
    if j >= 0.5 or contain >= 0.8:
        dupes.append({"a": a, "b": b, "jaccard": round(j, 3), "containment": round(contain, 3), "words_a": ok[a]["word_count"], "words_b": ok[b]["word_count"]})
dupes.sort(key=lambda x: -x["jaccard"])
hashes = {}
for k, r in ok.items():
    hashes.setdefault(hashlib.sha256(re.sub(r"\W+", " ", r["text"].lower()).encode()).hexdigest(), []).append(k)
exact = [v for v in hashes.values() if len(v) > 1]

out = {"collected_at": now(), "pages": {k: {kk: (sorted(vv) if isinstance(vv, set) else vv) for kk, vv in r.items() if kk not in ("text", "links")} for k, r in pages.items()},
       "dead_internal_links": [{**d, "raw_hrefs": sorted(d["raw_hrefs"]), "texts": sorted(d["texts"]), "sources": sorted(d["sources"])} for d in dead.values()],
       "dupes_ge_0_5": dupes, "exact_text_dupes": exact}
for k, r in out["pages"].items():
    r["content_in_n"] = len(r["content_in"]); r["menu_in_n"] = len(r["menu_in"])
save_evidence("EV-D-analysis", json.dumps(out, ensure_ascii=False, indent=1), "json", "python analysis of EV-D-crawl-data", "offline: inlinks, dead links, shingle similarity (5-word), page types", note="derived from EV-D-crawl-data")
# console summary
from collections import Counter
print("pages", len(pages), Counter(r.get("status") for r in pages.values()))
print("types", Counter(r.get("type") for r in pages.values() if r.get("status") == 200))
print("H1 counts (200 pages)", Counter(r.get("h1_count") for r in pages.values() if r.get("status") == 200))
for t in ("service_area", "service_sub", "team_bio", "news_article", "info", "legal", "home", "news_category", "other"):
    ps = [r for r in pages.values() if r.get("status") == 200 and r.get("type") == t]
    if ps:
        print(t, len(ps), "h1:", Counter(r["h1_count"] for r in ps), "words min/max", min(r["word_count"] for r in ps), max(r["word_count"] for r in ps))
print("\nORPHAN-ish (content_in == 0):")
for k, r in sorted(pages.items()):
    if r.get("status") == 200 and not r["content_in"]:
        print(" ", r["type"], "menu_in", len(r["menu_in"]), k)
print("\nDEAD:", json.dumps(out["dead_internal_links"], indent=1)[:1800])
print("\nDUPES:")
for d in dupes[:30]:
    print(" ", d["jaccard"], d["containment"], d["a"][-70:], "|", d["b"][-70:])
print("exact", exact)
