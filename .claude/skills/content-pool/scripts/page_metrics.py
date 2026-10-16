#!/usr/bin/env python3
"""Measure one or more web pages for the content pool (competitor and own pages).

Usage:
  page_metrics.py --out metrics.json [--places "Charlottenburg,Wilmersdorf,..."] URL [URL ...]
  page_metrics.py --out metrics.json --urls-file urls.txt

Per page it writes: status, final url, title, meta description, h1/h2/h3 lists,
visible word count (script/style/nav/footer/header removed), JSON-LD @types, dateModified,
FAQ signal, tel link, form, booking link hint, rating mention, price mention,
credential words, internal link count, places mentioned, image count.

Failed fetches are retried 3 times (gate A0), then reported with status "unreadable". Never skipped silently.
Uses only the standard library. Browser-like User-Agent.
"""
import argparse, json, re, sys, time, urllib.request, urllib.error
from html.parser import HTMLParser
from urllib.parse import urlparse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
SKIP = {"script", "style", "noscript", "nav", "footer", "header", "svg", "form", "iframe"}
CRED_EN = ["doctor", "dr.", "licensed", "certified", "registered", "mbbs", "years of experience", "years' experience", "accredited", "board", "specialist", "graduate"]
EN = {
    "faq": r"frequently asked|faq|questions and answers",
    "booking": r"book (now|an appointment|a session|online)|make an appointment|whatsapp us|book via whatsapp",
    "rating": r"\b[45][,.]\d\s*(stars|/ ?5)|reviews|testimonials",
    "price": r"(idr|rp\.?|usd|\$|€)\s?\d|\d[\d.,]*\s*(idr|k\b|usd|€|million)",
}
LANG = "de"
CRED = ["heilpraktiker", "diplom", "zertifi", "ausbildung", "mitglied", "verband", "approbation", "seit 19", "seit 20", "jahre erfahrung", "jahren erfahrung"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.stack = []
        self.title = ""
        self.meta = ""
        self.h = {"h1": [], "h2": [], "h3": []}
        self.text = []
        self.jsonld = []
        self.in_ld = False
        self.ld_buf = []
        self.links = []
        self.imgs = 0
        self.has_form = False
        self.cur_h = None
        self.cur_h_buf = []
        self.in_title = False
        self.details = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "meta" and (a.get("name", "").lower() == "description"):
            self.meta = a.get("content", "")
        if tag == "script" and a.get("type", "").lower() == "application/ld+json":
            self.in_ld = True
            self.ld_buf = []
        if tag in SKIP and tag != "script":
            self.skip += 1
        elif tag == "script":
            self.skip += 1
        if tag == "form":
            self.has_form = True
        if tag == "details":
            self.details += 1
        if tag == "img":
            self.imgs += 1
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag in ("h1", "h2", "h3"):
            self.cur_h = tag
            self.cur_h_buf = []

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script" and self.in_ld:
            self.in_ld = False
            self.jsonld.append("".join(self.ld_buf))
        if tag in SKIP or tag == "script":
            self.skip = max(0, self.skip - 1)
        if tag == self.cur_h:
            t = re.sub(r"\s+", " ", "".join(self.cur_h_buf)).strip()
            if t:
                self.h[tag].append(t)
            self.cur_h = None

    def handle_data(self, d):
        if self.in_title:
            self.title += d
        if self.in_ld:
            self.ld_buf.append(d)
            return
        if self.cur_h:
            self.cur_h_buf.append(d)
        if self.skip == 0:
            self.text.append(d)


def fetch(url):
    last = None
    for i in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "de-DE,de;q=0.9"})
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
                ct = r.headers.get_content_charset() or "utf-8"
                return r.status, r.geturl(), raw.decode(ct, errors="replace"), r.headers.get("Last-Modified")
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code in (403, 404, 410):
                break
        except Exception as e:  # noqa
            last = str(e)[:120]
        time.sleep(1.5)
    return None, url, None, last


CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def render(url):
    """Fallback: render in headless Chrome and return the DOM (for JS sites and 403 blocks)."""
    import subprocess, os
    if not os.path.exists(CHROME):
        return None
    try:
        out = subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=8000", f"--user-agent={UA}", "--dump-dom", url],
            capture_output=True, timeout=60,
        )
        html = out.stdout.decode("utf-8", errors="replace")
        return html if len(html) > 500 else None
    except Exception:
        return None


def ld_types(blobs):
    types, dm = set(), None

    def walk(o):
        nonlocal dm
        if isinstance(o, dict):
            t = o.get("@type")
            if t:
                for x in (t if isinstance(t, list) else [t]):
                    types.add(str(x))
            if o.get("dateModified") and not dm:
                dm = o["dateModified"]
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    for b in blobs:
        try:
            walk(json.loads(b))
        except Exception:
            pass
    return sorted(types), dm


def parse(html):
    p = P()
    p.feed(html)
    return p


def measure(url, places):
    status, final, html, extra = fetch(url)
    method = "http"
    p = None
    if html is not None:
        try:
            p = parse(html)
        except Exception:
            p = None
    # Fallback to headless Chrome when the fetch failed or the page has almost no text (JS site).
    if p is None or len(" ".join(p.text).split()) < 120:
        rendered = render(url)
        if rendered:
            try:
                p2 = parse(rendered)
                if p is None or len(" ".join(p2.text).split()) > len(" ".join(p.text).split()):
                    p, html, method = p2, rendered, "chrome-rendered"
                    status = status or 200
            except Exception:
                pass
    if p is None:
        return {"url": url, "status": "unreadable", "reason": extra}
    text = re.sub(r"\s+", " ", " ".join(p.text)).strip()
    low = text.lower()
    words = len(text.split())
    types, dm = ld_types(p.jsonld)
    host = urlparse(final).netloc
    internal = sum(1 for l in p.links if l.startswith("/") or host in l)
    return {
        "url": url,
        "final_url": final,
        "status": "ok",
        "http": status,
        "fetch_method": method,
        "title": re.sub(r"\s+", " ", p.title).strip(),
        "meta_description": p.meta,
        "h1": p.h["h1"],
        "h2": p.h["h2"],
        "h3": p.h["h3"],
        "words": words,
        "jsonld_types": types,
        "date_modified": dm or extra if (dm or (extra and "GMT" in str(extra))) else None,
        "faq_signal": bool(re.search(EN["faq"] if LANG == "en" else r"häufige fragen|faq|fragen und antworten", low)) or p.details > 2 or "FAQPage" in types,
        "tel_link": any(l.startswith("tel:") for l in p.links),
        "has_form": p.has_form,
        "booking_hint": bool(re.search(EN["booking"] if LANG == "en" else r"termin (buchen|vereinbaren)|online-?termin|jetzt buchen", low)),
        "rating_mention": bool(re.search(EN["rating"] if LANG == "en" else r"bewertung|\b[45][,.]\d\s*(sterne|/ ?5)|erfahrungen", low)),
        "price_mention": bool(re.search(EN["price"] if LANG == "en" else r"\d+\s*(€|euro)", low)),
        "credential_hits": [c for c in (CRED_EN if LANG == "en" else CRED) if c in low],
        "internal_links": internal,
        "images": p.imgs,
        "places": {pl: n for pl in places for n in [len(re.findall(r"(?<![a-zäöüß])" + re.escape(pl.lower()) + r"(?![a-zäöüß])", low))] if n},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="*")
    ap.add_argument("--urls-file")
    ap.add_argument("--out", required=True)
    ap.add_argument("--places", default="")
    ap.add_argument("--lang", default="de", choices=["de", "en"], help="pattern set for FAQ, booking, rating, price, credentials")
    a = ap.parse_args()
    globals()["LANG"] = a.lang
    urls = list(a.urls)
    if a.urls_file:
        urls += [l.strip() for l in open(a.urls_file) if l.strip() and not l.startswith("#")]
    places = [x.strip() for x in a.places.split(",") if x.strip()]
    res = [measure(u, places) for u in urls]
    json.dump(res, open(a.out, "w"), ensure_ascii=False, indent=1)
    ok = sum(1 for r in res if r["status"] == "ok")
    print(f"{ok}/{len(res)} readable -> {a.out}")
    for r in res:
        if r["status"] != "ok":
            print("UNREADABLE:", r["url"], r.get("reason"))


if __name__ == "__main__":
    main()
