"""Read-only crawler helpers. GET only. Polite delay. No auth."""
import re, time, json, hashlib, urllib.parse, requests
from bs4 import BeautifulSoup
from ub_lib import save_evidence, now

UA = {"User-Agent": "Mozilla/5.0 (compatible; 741-unburning-dryrun/1.0; read-only)"}
SESS = requests.Session()
SESS.headers.update(UA)
HOSTS = {"suriya-praxis.de", "www.suriya-praxis.de"}
DELAY = 0.3

def slug_of(url):
    p = urllib.parse.urlparse(url)
    s = (p.netloc + p.path + ("?" + p.query if p.query else "")).strip("/")
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", s)
    return s[:120] or "root"

def norm_url(href, base):
    if not href: return None
    href = href.strip()
    if href.startswith(("mailto:", "tel:", "javascript:", "#", "data:", "whatsapp:", "sms:")): return None
    u = urllib.parse.urljoin(base, href)
    u, _ = urllib.parse.urldefrag(u)
    return u

def is_internal(u):
    try: return urllib.parse.urlparse(u).netloc.lower() in HOSTS
    except Exception: return False

def canon_key(u):
    """Key used to compare internal URLs: host-less, no trailing-slash differences."""
    p = urllib.parse.urlparse(u)
    path = p.path or "/"
    if not path.endswith("/") and "." not in path.rsplit("/",1)[-1]: path += "/"
    return path + (("?" + p.query) if p.query else "")

def fetch_chain(url, max_hops=10):
    chain = []
    cur = url
    last = None
    err = None
    for _ in range(max_hops + 1):
        try:
            r = SESS.get(cur, allow_redirects=False, timeout=40)
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
            chain.append({"url": cur, "status": None, "error": err})
            return chain, None, err
        time.sleep(DELAY)
        chain.append({"url": cur, "status": r.status_code, "location": r.headers.get("Location")})
        last = r
        if r.status_code in (301, 302, 303, 307, 308) and r.headers.get("Location"):
            cur = urllib.parse.urljoin(cur, r.headers["Location"])
            continue
        return chain, r, None
    return chain, last, "redirect loop or too many hops"

HWG = [
 ("heilt", r"\bheilt\b"), ("geheilt", r"\bgeheilt\b|\bgeheilte"), ("heilung", r"heilung"), ("heilbar", r"\bheilbar|\bunheilbar"),
 ("heilversprechen", r"heilversprechen"), ("heilerfolg", r"heilerfolg"),
 ("garantiert", r"garantier"), ("100%", r"100\s?%"), ("wundermittel", r"wundermittel|wunderheil|wunderwaffe|\bwunder\b"),
 ("schmerzfrei", r"schmerzfrei"), ("beseitigt", r"\bbeseitigt|\bbeseitigen"),
 ("bewiesen", r"wissenschaftlich bewiesen|nachweislich|erwiesenerma"),
 ("erfolgsquote", r"erfolgsquote|erfolgsgarantie|erfolgsversprechen"),
 ("verschwinden", r"verschwind\w+ (?:dauerhaft|für immer|garantiert)|dauerhaft(?:e)? (?:befreit|schmerzfrei|weg)"),
]
HWG_RE = [(k, re.compile(p, re.I)) for k, p in HWG]
SLOP = [r"in der heutigen (?:schnelllebigen|hektischen) welt", r"tauche(?:n)? (?:sie |du )?(?:ein|tief)", r"es ist wichtig zu (?:beachten|verstehen)",
        r"zusammenfassend (?:lässt sich|kann man)", r"in der welt von", r"eine reise (?:zu|der|in)", r"entfessel", r"nahtlos", r"ganzheitliche[nrs]? ansatz", r"zögern sie nicht", r"fazit",
        r"kraft der natur", r"harmonie von körper, geist und seele", r"tiefgreifend", r"entdecken sie die", r"entdecke die"]
SLOP_RE = [re.compile(p, re.I) for p in SLOP]

def visible_text(node):
    for t in node.find_all(["script", "style", "noscript", "template"]):
        t.decompose()
    txt = node.get_text(" ", strip=True)
    return re.sub(r"\s+", " ", txt)

def parse_page(url, final_url, html, headers):
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
    # JSON-LD
    ld = []
    for s in soup.find_all("script", type="application/ld+json"):
        try: ld.append(json.loads(s.string or s.get_text()))
        except Exception: ld.append({"_unparsed": (s.string or "")[:300]})
    rec["jsonld"] = ld
    # all internal links (full page) for 404 inventory
    all_links = []
    for a in soup.find_all("a", href=True):
        u = norm_url(a["href"], final_url)
        if u: all_links.append({"href": u, "text": a.get_text(" ", strip=True)[:120]})
    rec["all_links"] = all_links
    # NAP regions
    foot = soup.find(id="footer")
    sock = soup.find(id="socket")
    rec["footer_text"] = re.sub(r"\s+", " ", foot.get_text(" ", strip=True))[:1500] if foot else None
    rec["socket_text"] = re.sub(r"\s+", " ", sock.get_text(" ", strip=True))[:600] if sock else None
    # content region
    main = soup.find(id="main") or soup.body
    for sel in main.select("aside, .sidebar, nav, .av-related, .comment-entry, #comments, #footer, #socket, footer, header"):
        sel.decompose()
    h1s = [h.get_text(" ", strip=True) for h in main.find_all("h1")]
    rec["h1_count"] = len(h1s); rec["h1_texts"] = h1s[:3]
    content_links = []
    for a in main.find_all("a", href=True):
        u = norm_url(a["href"], final_url)
        if u: content_links.append({"href": u, "text": a.get_text(" ", strip=True)[:120]})
    rec["content_links"] = content_links
    text = visible_text(main)
    rec["text"] = text
    rec["word_count"] = len(text.split())
    # HWG + slop
    hwg = []
    check = " ".join(filter(None, [rec["title"], rec["meta_description"], text]))
    for k, rx in HWG_RE:
        for m in rx.finditer(check):
            s = max(0, m.start() - 70); e = min(len(check), m.end() + 70)
            hwg.append({"term": k, "match": m.group(0), "context": check[s:e]})
    rec["hwg_matches"] = hwg
    rec["slop_hits"] = sum(len(rx.findall(text)) for rx in SLOP_RE)
    # NAP markers over the whole html
    full = html if isinstance(html, str) else html.decode("utf8", "replace")
    nap = {}
    nap["binger"] = bool(re.search(r"Binger\s?-?\s?(?:str|straße|strasse)", full, re.I))
    nap["schuetzenpfad"] = bool(re.search(r"Sch(?:ü|u|&uuml;|&#252;)tzenpfad", full, re.I))
    nap["old_name_ayurveda_naturheilkunde"] = bool(re.search(r"Praxis Suriya\s*[-–—|]\s*Ayurveda\s*(?:&|&amp;|und)\s*Naturheilkunde", full, re.I))
    nap["old_name_heilpraktiker_I"] = bool(re.search(r"Heilpraktiker Ingelheim\s*[I|]\s*Praxis Suriya", full, re.I))
    phones = set(re.findall(r"(?:\+49|0049|0)[\s./-]?\(?\d{2,5}\)?[\s./-]?\d{3,}[\s./-]?\d{0,}", re.sub(r"<[^>]+>", " ", full)))
    nap["phones_raw"] = sorted({re.sub(r"\s+", " ", p).strip() for p in phones if len(re.sub(r"\D", "", p)) >= 9})[:20]
    rec["nap_markers"] = nap
    rec["text_hash"] = hashlib.sha256(re.sub(r"\W+", " ", text.lower()).encode()).hexdigest()
    return rec

def crawl_url(url, save=True, subdir="area_d/pages", tag="D"):
    chain, r, err = fetch_chain(url)
    out = {"url": url, "collected_at": now(), "chain": chain, "redirect_hops": max(0, len(chain) - 1),
           "final_url": chain[-1]["url"] if chain else url, "error": err}
    if r is None:
        out["final_status"] = None
        return out
    out["final_status"] = r.status_code
    out["content_type"] = r.headers.get("Content-Type")
    out["x_robots_tag"] = r.headers.get("X-Robots-Tag")
    ct = (r.headers.get("Content-Type") or "").lower()
    if "html" in ct and r.status_code < 500:
        html = r.text
        if save:
            out["evidence_id"] = save_evidence(f"EV-{tag}-page-{slug_of(out['final_url'])}", r.content, "html", "requests GET",
                                              f"GET {url} (manual redirect follow, UA 741-unburning-dryrun)", subdir=subdir,
                                              note=f"final_status={r.status_code} hops={out['redirect_hops']}")
        out.update(parse_page(url, out["final_url"], html, r.headers))
    return out
