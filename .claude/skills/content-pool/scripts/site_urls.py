#!/usr/bin/env python3
"""List the page URLs of competitor sites from their sitemaps (for 'does a page on topic X exist').

Usage: site_urls.py --out site_urls.json domain1 domain2 ...
Tries /sitemap.xml, /sitemap_index.xml, /wp-sitemap.xml and robots.txt Sitemap lines.
Follows one level of sitemap index (max 15 child sitemaps). Without a sitemap it crawls internal links from the home page (depth 3, 200 pages, field \"sitemap\" says crawl). A domain that cannot be read at all is
reported as {\"status\": \"unreadable\"}; the caller must not treat that as 'no pages'.
"""
import argparse, json, re, urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"


def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=25) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception:
        return None


def locs(xml):
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml or "")


def crawl(domain):
    base = f"https://{domain}"
    cands = [f"{base}/sitemap.xml", f"{base}/sitemap_index.xml", f"{base}/wp-sitemap.xml", f"https://www.{domain}/sitemap.xml"]
    robots = get(f"{base}/robots.txt") or ""
    cands += re.findall(r"(?im)^sitemap:\s*(\S+)", robots)
    for c in cands:
        xml = get(c)
        if not xml or "<loc>" not in xml:
            continue
        urls = locs(xml)
        if "<sitemapindex" in xml:
            allu = []
            for child in urls[:15]:
                allu += locs(get(child))
            urls = allu
        urls = [u for u in urls if not re.search(r"\.(jpg|jpeg|png|webp|gif|pdf)(\?|$)", u, re.I)]
        return {"status": "ok", "sitemap": c, "count": len(urls), "urls": urls[:5000]}
    return bfs(domain)


def bfs(domain, limit=200, depth=3):
    """Fallback when the site has no sitemap: follow internal links from the home page (HTML only, same host)."""
    from collections import deque
    from urllib.parse import urljoin, urlparse, urldefrag
    host = domain.replace("www.", "")
    start = None
    for cand in (f"https://{domain}/", f"https://www.{domain}/"):
        if get(cand):
            start = cand
            break
    if not start:
        return {"status": "unreadable", "reason": "no sitemap and home page not readable"}
    start_host = urlparse(start).netloc
    seen, q = {start}, deque([(start, 0)])
    while q and len(seen) < limit:
        u, d = q.popleft()
        if d >= depth:
            continue
        html_ = get(u) or ""
        for href in re.findall(r'href=["\']([^"\'#]+)', html_):
            full = urldefrag(urljoin(u, href))[0]
            pu = urlparse(full)
            if pu.scheme not in ("http", "https") or pu.netloc != start_host or "\\" in full:
                continue
            if re.search(r"\.(jpg|jpeg|png|webp|gif|pdf|zip|css|js|svg|ico)(\?|$)", full, re.I) or "?" in full:
                continue
            if full not in seen:
                seen.add(full)
                q.append((full, d + 1))
    return {"status": "ok", "sitemap": "crawl (no sitemap found)", "count": len(seen), "urls": sorted(seen)[:5000]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("domains", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = {d: crawl(d) for d in a.domains}
    json.dump(out, open(a.out, "w"), ensure_ascii=False, indent=1)
    for d, r in out.items():
        print(d, r["status"], r.get("count", r.get("reason")))


if __name__ == "__main__":
    main()
