#!/usr/bin/env python3
"""Prospect mini workflow, step 2 (free): website facts for the review page.

Usage: collect_site.py <prospect_dir> <homepage_url>

Writes <prospect_dir>/evidence/site.json and site-pages.json.
Reuses content-pool-skill/scripts/site_urls.py (URL list) and page_metrics.py (per-page metrics).
Extra checks: https redirect, server wait time (3 runs), sitemap URL count vs. crawled pages,
broken phone links, dead links on the home page, GA4/GTM ids, form, schema types, image URLs (for strip photos),
form and phone links on the contact page, duplicate pages (same title and same word count).
Read only. Standard library only.
"""
import json, os, re, subprocess, sys, time, urllib.request
from urllib.parse import urljoin, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
CP = os.path.join(HERE, '..', '..', 'content-pool-skill', 'scripts')
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"


def get(url, method='GET', timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method=method)
    t = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read() if method == 'GET' else b''
            return dict(status=r.status, url=r.geturl(), secs=round(time.time() - t, 2), body=body.decode('utf-8', 'replace'))
    except urllib.error.HTTPError as e:
        return dict(status=e.code, url=url, secs=round(time.time() - t, 2), body='')
    except Exception as e:
        return dict(status=None, url=url, secs=None, body='', error=str(e)[:120])


def contact_url(html, base):
    """First link on the home page whose href or text contains "kontakt" or "contact"."""
    for href, txt in re.findall(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.I | re.S):
        if href.lower().startswith(('mailto:', 'tel:', '#', 'javascript:')): continue
        if re.search(r'kontakt|contact', href + ' ' + re.sub(r'<[^>]+>', ' ', txt), re.I): return urljoin(base, href)
    return None


def duplicates(mets):
    """Pairs of measured pages with the same title and the same word count."""
    out = []
    for i, a in enumerate(mets):
        for b in mets[i + 1:]:
            if a.get('title') and a.get('title') == b.get('title') and a.get('words') == b.get('words'):
                out.append({'pages': [urlparse(a.get('url', '')).path or '/', urlparse(b.get('url', '')).path or '/'], 'title': a['title'], 'words': a.get('words')})
    return out


def ttfb(url):
    out = []
    for _ in range(3):
        r = subprocess.run(['curl', '-s', '-o', '/dev/null', '-A', UA, '-w', '%{time_starttransfer}', url], capture_output=True, text=True, timeout=40)
        try: out.append(round(float(r.stdout), 2))
        except ValueError: pass
    return out


def main():
    pdir, home = sys.argv[1], sys.argv[2]
    ev = os.path.join(pdir, 'evidence'); os.makedirs(ev, exist_ok=True)
    dom = urlparse(home).netloc
    site = {'home': home, 'domain': dom}

    h = get(home)
    html = h['body']
    site['home_status'], site['home_final_url'] = h['status'], h['url']
    hp = get('http://' + dom.replace('www.', '') + '/')
    site['http_redirects_to_https'] = (hp.get('url') or '').startswith('https://')
    site['ttfb_secs'] = ttfb(h['url'] or home)

    # tracking, schema, form, phone links
    site['ga4'] = sorted(set(re.findall(r'G-[A-Z0-9]{6,12}', html)))
    site['gtm'] = sorted(set(re.findall(r'GTM-[A-Z0-9]{5,9}', html)))
    site['jsonld_blocks'] = len(re.findall(r'application/ld\+json', html))
    site['form_on_home'] = '<form' in html.lower()
    tels = re.findall(r'href=["\'](tel[^"\']*)["\']', html, re.I)
    site['tel_links_home'] = tels
    site['tel_links_broken_home'] = [t for t in tels if not t.lower().startswith('tel:')]
    cu = contact_url(html, h['url'] or home)
    site['contact_url'], site['form_on_contact'], site['tel_links_contact'] = cu, None, []
    if cu:
        cb = get(cu, timeout=15)['body']
        site['form_on_contact'] = '<form' in cb.lower()
        site['tel_links_contact'] = re.findall(r'href=["\'](tel[^"\']*)["\']', cb, re.I)

    # dead internal links on the home page (max 40)
    links = []
    for a in re.findall(r'href=["\']([^"\'#]+)["\']', html):
        u = urljoin(h['url'] or home, a)
        if urlparse(u).netloc == urlparse(h['url'] or home).netloc and not re.search(r'\.(jpg|jpeg|png|webp|svg|pdf|css|js|ico)(\?|$)', u, re.I):
            if u not in links: links.append(u)
    dead = []
    for u in links[:40]:
        r = get(u, timeout=15)
        if r['status'] is None or r['status'] >= 400: dead.append({'url': u, 'status': r['status']})
    site['home_internal_links'] = len(links)
    site['dead_links_from_home'] = dead

    # images on home (candidates for strip photos and hero mockup)
    imgs = []
    for src in re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html, re.I) + re.findall(r'url\(["\']?([^"\')]+\.(?:jpe?g|png|webp))', html, re.I):
        u = urljoin(h['url'] or home, src)
        if re.search(r'\.(jpe?g|png|webp)(\?|$)', u, re.I) and u not in imgs: imgs.append(u)
    site['images_home'] = imgs[:40]

    # URL list (sitemap or crawl) + per-page metrics
    su = os.path.join(ev, 'site-urls.json')
    subprocess.run([sys.executable, os.path.join(CP, 'site_urls.py'), '--out', su, dom], check=False, capture_output=True, timeout=600)
    try:
        sd = json.load(open(su))
        rec = sd[dom] if isinstance(sd, dict) and dom in sd else (list(sd.values())[0] if isinstance(sd, dict) else sd)
    except Exception:
        rec = {}
    site['url_source'] = rec.get('sitemap') if isinstance(rec, dict) else None
    urls = rec.get('urls', []) if isinstance(rec, dict) else []
    site['sitemap_or_crawl_urls'] = len(urls)

    # real sitemap count (independent of crawl)
    sm_count = None
    for path in ('/sitemap.xml', '/sitemap_index.xml', '/wp-sitemap.xml'):
        r = get('https://' + dom + path, timeout=15)
        if r['status'] == 200 and '<loc>' in r['body']:
            locs = re.findall(r'<loc>\s*([^<\s]+)', r['body'])
            if any(l.endswith('.xml') for l in locs):
                n = 0
                for l in locs[:15]:
                    n += len(re.findall(r'<loc>', get(l, timeout=15)['body']))
                sm_count = n
            else:
                sm_count = len(locs)
            site['sitemap_path'] = path
            break
    site['sitemap_urls'] = sm_count

    pages = [h['url'] or home] + [u for u in urls if u.rstrip('/') != (h['url'] or home).rstrip('/')][:29]
    uf = os.path.join(ev, 'site-page-urls.txt'); open(uf, 'w').write('\n'.join(pages))
    pm = os.path.join(ev, 'site-pages.json')
    subprocess.run([sys.executable, os.path.join(CP, 'page_metrics.py'), '--out', pm, '--urls-file', uf, '--lang', 'de'], check=False, capture_output=True, timeout=900)
    try:
        mets = json.load(open(pm))
        mets = mets if isinstance(mets, list) else mets.get('pages', list(mets.values()))
    except Exception:
        mets = []
    site['pages_measured'] = len(mets)
    site['pages_two_h1'] = sum(1 for m in mets if len(m.get('h1', [])) > 1)
    site['pages_no_h1'] = sum(1 for m in mets if len(m.get('h1', [])) == 0)
    site['duplicate_pages'] = duplicates(mets)
    broken_tel_pages = []
    for u in pages:
        b = get(u, timeout=15)['body'] if u != pages[0] else html
        if re.search(r'href=["\']tel(?!:)[^"\']*["\']', b, re.I): broken_tel_pages.append(u)
    site['pages_with_broken_tel'] = broken_tel_pages
    if mets:
        hm = mets[0]
        site['home_title'] = hm.get('title'); site['home_meta'] = hm.get('meta_description') or hm.get('meta')
        site['home_h1'] = hm.get('h1'); site['home_words'] = hm.get('words') or hm.get('word_count')
    json.dump(site, open(os.path.join(ev, 'site.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in site.items() if k not in ('images_home', 'tel_links_home')}, ensure_ascii=False, indent=1)[:3000])


if __name__ == '__main__':
    main()
