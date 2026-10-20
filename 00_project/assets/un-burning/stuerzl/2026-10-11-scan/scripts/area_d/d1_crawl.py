"""D01/D02: crawl stuerzl-steuerstrafrecht.de from the home page. GET only, 0.3 s delay, depth <= 4.
Saves every HTML page as evidence and one crawl-data JSON."""
import sys, os, json, re, urllib.parse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *
from bs4 import BeautifulSoup

HOSTS = {"www.stuerzl-steuerstrafrecht.de", "stuerzl-steuerstrafrecht.de"}
START = "https://www.stuerzl-steuerstrafrecht.de/"
MAXDEPTH = 4
ASSET_EXT = re.compile(r"\.(pdf|jpe?g|png|gif|webp|svg|ico|css|js|zip|docx?|xlsx?|mp4|mp3|woff2?|ttf|xml|txt)(\?.*)?$", re.I)


def norm(href, base):
    if href is None:
        return None
    h = href.strip()
    if not h or h.startswith(("mailto:", "tel:", "javascript:", "#", "data:", "whatsapp:", "sms:", "callto:")):
        return None
    u = urllib.parse.urljoin(base, h)
    u, _ = urllib.parse.urldefrag(u)
    if not u.startswith(("http://", "https://")):
        return None
    return u


def is_internal(u):
    return urllib.parse.urlparse(u).netloc.lower() in HOSTS


def region_of(a):
    for p in a.parents:
        if p.name == "header" and p.get("id") == "sp-header":
            return "header_menu"
        if p.name == "footer" or p.get("id") in ("sp-footer", "sp-footer1", "sp-footer2"):
            return "footer"
        if p.get("class") and "offcanvas-menu" in p.get("class"):
            return "offcanvas_menu"
        if p.get("id") == "sp-main-body":
            return "content"
        if p.get("id") == "sp-title":
            return "title_bar"
    return "other"


def visible_text(node):
    n = BeautifulSoup(str(node), "html.parser")
    for t in n.find_all(["script", "style", "noscript", "template"]):
        t.decompose()
    return re.sub(r"\s+", " ", n.get_text(" ", strip=True))


def parse_page(final_url, html, headers):
    soup = BeautifulSoup(html, "html.parser")
    rec = {}
    t = soup.find("title")
    rec["title"] = t.get_text(strip=True) if t else None
    md = soup.find("meta", attrs={"name": re.compile("^description$", re.I)})
    rec["meta_description"] = md.get("content") if md else None
    mr = soup.find("meta", attrs={"name": re.compile("^robots$", re.I)})
    rec["meta_robots"] = mr.get("content") if mr else None
    rec["x_robots_tag"] = headers.get("X-Robots-Tag")
    can = soup.find("link", rel=lambda v: v and "canonical" in v)
    rec["canonical"] = can.get("href") if can else None
    rec["hreflang"] = [l.get("href") for l in soup.find_all("link", rel="alternate") if l.get("hreflang")]
    ld = []
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            ld.append(json.loads(s.string or s.get_text()))
        except Exception:
            ld.append({"_unparsed": (s.string or "")[:300]})
    rec["jsonld_types"] = [x.get("@type") if isinstance(x, dict) else None for x in ld]
    rec["jsonld"] = ld
    body = soup.body or soup
    h1s = [re.sub(r"\s+", " ", h.get_text(" ", strip=True)) for h in body.find_all("h1")]
    rec["h1_count"] = len(h1s)
    rec["h1_texts"] = h1s[:5]
    rec["h2_count"] = len(body.find_all("h2"))
    main = soup.find(id="sp-main-body")
    rec["has_main_body"] = main is not None
    text = visible_text(main if main else body)
    rec["text"] = text
    rec["word_count"] = len(text.split())
    links = []
    for a in body.find_all("a", href=True):
        raw = a["href"]
        u = norm(raw, final_url)
        links.append({"raw": raw, "url": u, "text": a.get_text(" ", strip=True)[:120], "region": region_of(a),
                      "rel": " ".join(a.get("rel") or []), "target": a.get("target")})
    rec["links"] = links
    rec["imgs_no_alt"] = sum(1 for i in body.find_all("img") if not (i.get("alt") or "").strip())
    rec["lang"] = (soup.html.get("lang") if soup.html else None)
    return rec


def main():
    m = load_manifest()
    m["evidence"] = [e for e in m["evidence"] if not e["id"].startswith("EV-D-page-")]
    seen, order = {}, []
    queue = collections.deque([(START, 0, None)])
    queued = {START}
    while queue:
        url, depth, via = queue.popleft()
        chain, r, err = fetch_chain(url)
        rec = {"url": url, "depth": depth, "discovered_via": via, "collected_at": now(), "chain": chain,
               "redirect_hops": max(0, len(chain) - 1), "final_url": chain[-1]["url"], "error": err}
        if r is None:
            rec["final_status"] = None
        else:
            rec["final_status"] = r.status_code
            ct = (r.headers.get("Content-Type") or "").lower()
            rec["content_type"] = ct
            rec["set_cookie_present"] = "Set-Cookie" in r.headers
            if "html" in ct:
                rec["evidence_id"] = save_evidence(
                    "EV-D-page-" + slug_of(rec["final_url"]) + ("" if r.status_code == 200 else f"-{r.status_code}"),
                    r.content, "html", "requests GET", f"GET {url} (manual redirect follow, UA {UA})",
                    note=f"final_status={r.status_code} hops={rec['redirect_hops']}", m=m)
                rec.update(parse_page(rec["final_url"], r.text, r.headers))
        seen[url] = rec
        order.append(url)
        print(len(order), rec.get("final_status"), rec["redirect_hops"], depth, url, rec.get("word_count"), flush=True)
        # follow internal links (also from redirect target pages and 404 pages: Joomla 404 page has menu)
        if depth < MAXDEPTH and rec.get("links") is not None and is_internal(rec["final_url"]) and rec.get("final_status") == 200:
            for l in rec["links"]:
                u = l["url"]
                if not u or not is_internal(u) or u in queued:
                    continue
                if ASSET_EXT.search(urllib.parse.urlparse(u).path):
                    continue
                queued.add(u)
                queue.append((u, depth + 1, url))
        # redirect chains: the final URL of an internal redirect is crawled as its own record
        fu = rec["final_url"]
        if fu != url and is_internal(fu) and fu not in queued and depth <= MAXDEPTH:
            queued.add(fu)
            queue.appendleft((fu, depth, url))
    save_manifest(m)
    save_evidence("EV-D-crawl-data", json.dumps({"start": START, "max_depth": MAXDEPTH, "pages": seen}, ensure_ascii=False, indent=1),
                  "json", "requests GET + BeautifulSoup", f"BFS crawl from {START}, depth<={MAXDEPTH}, delay {DELAY}s, UA {UA}",
                  note=f"{len(seen)} URLs fetched")
    print("done", len(seen))


if __name__ == "__main__":
    main()
