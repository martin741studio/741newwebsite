#!/usr/bin/env python3 -I
"""Area E crawl. READ ONLY. GET only, manual redirects, 0.3 s delay, UA 741-unburning-scan/1.0.
Seeds: apex + www home, OSMap sitemap URLs. BFS depth <= 4 over all internal links.
Then probes for known Joomla variants. Writes crawl.json (+ raw html tar.gz) into evidence/area_e/ via e_lib."""
import re, sys, os, json, time, io, tarfile, urllib.parse, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import requests
from bs4 import BeautifulSoup
from e_lib import save_evidence, now

UA = {"User-Agent": "741-unburning-scan/1.0"}
S = requests.Session(); S.headers.update(UA)
HOSTS = {"stuerzl-steuerstrafrecht.de", "www.stuerzl-steuerstrafrecht.de"}
BASE = "https://www.stuerzl-steuerstrafrecht.de"
DELAY = 0.3
MAXDEPTH = 4
ASSET_EXT = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".pdf", ".zip", ".doc", ".docx", ".xls", ".xlsx", ".mp4", ".css", ".js", ".ico", ".woff", ".woff2", ".txt", ".xml")
RAW = {}  # url -> html bytes

def is_internal(u):
    try: return urllib.parse.urlparse(u).netloc.lower() in HOSTS
    except Exception: return False

def norm(href, base):
    if not href: return None
    href = href.strip()
    if href.startswith(("mailto:", "tel:", "javascript:", "#", "data:", "whatsapp:", "sms:")): return None
    u = urllib.parse.urljoin(base, href)
    u, _ = urllib.parse.urldefrag(u)
    return u

def fetch(url, max_hops=8):
    chain = []; cur = url; r = None
    for _ in range(max_hops + 1):
        try:
            asset = urllib.parse.urlparse(cur).path.lower().endswith(ASSET_EXT)
            r = S.get(cur, allow_redirects=False, timeout=40, stream=asset)
        except Exception as e:
            chain.append({"url": cur, "status": None, "error": f"{type(e).__name__}: {e}"}); return chain, None
        time.sleep(DELAY)
        chain.append({"url": cur, "status": r.status_code, "location": r.headers.get("Location")})
        if r.status_code in (301, 302, 303, 307, 308) and r.headers.get("Location"):
            cur = urllib.parse.urljoin(cur, r.headers["Location"]); continue
        return chain, r
    return chain, r

REGION_SELECTORS = [("header", "#sp-header"), ("offcanvas", ".offcanvas-menu"), ("footer", "#sp-footer"),
                    ("title", "#sp-section-2"), ("component", "#sp-component"), ("main_other", "#sp-main-body")]

def parse(final_url, r):
    html = r.content.decode("utf-8", "replace")
    soup = BeautifulSoup(html, "html.parser")
    rec = {}
    t = soup.find("title"); rec["title"] = t.get_text(strip=True) if t else None
    md = soup.find("meta", attrs={"name": re.compile("^description$", re.I)}); rec["meta_description"] = md.get("content") if md else None
    mr = soup.find("meta", attrs={"name": re.compile("^robots$", re.I)}); rec["meta_robots"] = mr.get("content") if mr else None
    rec["x_robots_tag"] = r.headers.get("X-Robots-Tag")
    can = soup.find("link", rel=lambda v: v and "canonical" in v); rec["canonical"] = can.get("href") if can else None
    rec["link_header"] = r.headers.get("Link")
    rec["alternates"] = [{"rel": " ".join(l.get("rel") or []), "type": l.get("type"), "href": l.get("href"), "hreflang": l.get("hreflang")}
                         for l in soup.find_all("link", rel=lambda v: v and ("alternate" in v or "next" in v or "prev" in v))]
    rec["og_url"] = (soup.find("meta", property="og:url") or {}).get("content") if soup.find("meta", property="og:url") else None
    rec["h1_all"] = [h.get_text(" ", strip=True) for h in soup.find_all("h1")]
    rec["jsonld_types"] = []
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            j = json.loads(s.string or s.get_text())
            def types(x):
                if isinstance(x, dict):
                    if "@type" in x: yield x["@type"]
                    for v in x.values(): yield from types(v)
                elif isinstance(x, list):
                    for v in x: yield from types(v)
            rec["jsonld_types"] += [str(a) for a in types(j)]
        except Exception: rec["jsonld_types"].append("_unparsed")
    # links by region
    links = []
    seen_a = set()
    comp = soup.select_one("#sp-component")
    for region, sel in REGION_SELECTORS:
        for node in soup.select(sel):
            for a in node.find_all("a", href=True):
                if id(a) in seen_a: continue
                seen_a.add(id(a))
                u = norm(a["href"], final_url)
                if not u: continue
                links.append({"region": region, "href": u, "raw": a["href"], "text": a.get_text(" ", strip=True)[:120]})
    for a in soup.find_all("a", href=True):
        if id(a) in seen_a: continue
        u = norm(a["href"], final_url)
        if u: links.append({"region": "other", "href": u, "raw": a["href"], "text": a.get_text(" ", strip=True)[:120]})
    rec["links"] = links
    rec["h1_component"] = [h.get_text(" ", strip=True) for h in comp.find_all("h1")] if comp else []
    rec["h1_title_bar"] = [h.get_text(" ", strip=True) for h in soup.select("#sp-section-2 h1")]
    rec["h2_component"] = [h.get_text(" ", strip=True) for h in comp.find_all("h2")][:30] if comp else []
    if comp:
        c2 = BeautifulSoup(str(comp), "html.parser")
        for tg in c2.find_all(["script", "style", "noscript"]): tg.decompose()
        txt = re.sub(r"\s+", " ", c2.get_text(" ", strip=True)); rec["words_component"] = len(txt.split())
        rec["text_hash"] = hashlib.sha256(re.sub(r"\W+", " ", txt.lower()).encode()).hexdigest()
    else:
        rec["words_component"] = None; rec["text_hash"] = None
    # resource URLs under paths blocked by robots.txt
    res = set()
    for tg in soup.find_all(["link", "script", "img"]):
        for k in ("href", "src"):
            v = tg.get(k)
            if v and not tg.name == "a":
                u = norm(v, final_url)
                if u and is_internal(u):
                    p = urllib.parse.urlparse(u).path
                    if re.match(r"^/(components|modules|plugins|layouts|libraries|includes|cache|language)/", p): res.add(p)
    rec["resources_under_robots_disallow"] = sorted(res)
    rec["html_bytes"] = len(r.content)
    return rec

PAGES = {}   # first-seen URL (as requested) -> record
def crawl_one(url, depth, source):
    if url in PAGES: return PAGES[url]
    chain, r = fetch(url)
    rec = {"url": url, "depth": depth, "discovered_via": source, "collected_at": now(), "chain": chain,
           "redirect_hops": max(0, len(chain) - 1), "final_url": chain[-1]["url"] if chain else url}
    if r is None:
        rec["final_status"] = None; rec["error"] = chain[-1].get("error") if chain else "no response"
    else:
        rec["final_status"] = r.status_code
        ct = r.headers.get("Content-Type", ""); rec["content_type"] = ct
        rec["x_robots_tag"] = r.headers.get("X-Robots-Tag")
        if "html" in ct.lower() and not urllib.parse.urlparse(rec["final_url"]).path.lower().endswith(ASSET_EXT):
            try:
                rec.update(parse(rec["final_url"], r)); RAW[url] = r.content
            except Exception as e:
                rec["parse_error"] = f"{type(e).__name__}: {e}"
        elif "xml" in ct.lower() or "text" in ct.lower():
            RAW[url] = r.content
            rec["body_head"] = r.content[:300].decode("utf-8", "replace")
        r.close()
    PAGES[url] = rec
    return rec

def main():
    t0 = time.time()
    # robots + sitemap probes first (raw)
    probes = {}
    for p in ["/robots.txt", "/sitemap.xml", "/sitemap.xml.gz", "/sitemap_index.xml", "/index.php/sitemap",
              "/index.php?option=com_osmap&view=xml&id=1&format=xml", "/index.php/component/osmap/?view=xml&id=1&format=xml",
              "/index.php?option=com_osmap&view=html&id=1", "/index.php?option=com_xmap&view=xml&tmpl=component&id=1",
              "/index.php?option=com_jmap&view=sitemap&format=xml", "/llms.txt"]:
        probes[p] = crawl_one(BASE + p, 0, "sitemap_probe")
    # sitemap urls
    sm_urls = []
    sm = probes["/index.php?option=com_osmap&view=xml&id=1&format=xml"]
    body = RAW.get(BASE + "/index.php?option=com_osmap&view=xml&id=1&format=xml", b"").decode("utf-8", "replace")
    sm_urls = re.findall(r"<loc><!\[CDATA\[(.*?)\]\]></loc>", body)
    # seeds
    crawl_one("https://stuerzl-steuerstrafrecht.de/", 0, "seed_apex")
    queue = [(BASE + "/", 0, "seed")]
    seen_norm = set()
    def key(u):
        p = urllib.parse.urlparse(u)
        return p.netloc.replace("www.", "") + p.path + ("?" + p.query if p.query else "")
    while queue:
        url, d, src = queue.pop(0)
        k = key(url)
        if k in seen_norm and url in PAGES: continue
        seen_norm.add(k)
        rec = crawl_one(url, d, src)
        if d >= MAXDEPTH or rec.get("final_status") != 200 or "links" not in rec: continue
        if not is_internal(rec["final_url"]): continue
        for l in rec["links"]:
            u = l["href"]
            if not is_internal(u): continue
            if key(u) in seen_norm: continue
            queue.append((u, d + 1, url))
    # sitemap URLs not reached
    for u in sm_urls:
        if key(u) not in seen_norm:
            seen_norm.add(key(u)); crawl_one(u, 99, "sitemap_only")
    print("crawl done", len(PAGES), "urls", round(time.time() - t0), "s")
    out = {"collected_at": now(), "ua": "741-unburning-scan/1.0", "delay_s": DELAY, "max_depth": MAXDEPTH,
           "sitemap_urls_osmap": sm_urls, "pages": list(PAGES.values())}
    save_evidence("EV-E-crawl", json.dumps(out, indent=1, ensure_ascii=False), "json", "python requests + bs4 (GET only)",
                  "BFS crawl from https://www.stuerzl-steuerstrafrecht.de/ depth<=4, UA 741-unburning-scan/1.0, delay 0.3 s; script scripts/E/e2_crawl.py",
                  note=f"{len(PAGES)} URLs fetched")
    bio = io.BytesIO()
    with tarfile.open(fileobj=bio, mode="w:gz") as tf:
        for i, (u, b) in enumerate(RAW.items()):
            ti = tarfile.TarInfo(f"{i:03d}_" + re.sub(r"[^A-Za-z0-9._-]+", "_", u.replace('https://', ''))[:100]); ti.size = len(b)
            tf.addfile(ti, io.BytesIO(b))
    save_evidence("EV-E-crawl-html", bio.getvalue(), "tar.gz", "python requests (GET only)", "raw response bodies of the crawl EV-E-crawl", note=f"{len(RAW)} bodies")

if __name__ == "__main__":
    main()
