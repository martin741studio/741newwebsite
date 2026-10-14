#!/usr/bin/env python3
"""Booking sequence: free quick check of the prospect's homepage, compared with the review-page evidence.

Usage: quick_check.py <slug> [<homepage_url>]
       quick_check.py <slug> --recheck     (for the m1 reminder: compares today with booking/site-check.json,
                                            writes booking/site-recheck.json, prints CHANGED lines or NO CHANGE)

Reads the URL from booking/baseline.md (find_prospect.py) when not given. Writes
00_project/prospects/<slug>/booking/site-check.json, booking/evidence/home.html (for claim quotes) and prints a short report:
facts today + "CHANGED since the review page" lines (when evidence/site.json from the review run exists).
Facts: status, final URL, https redirect, server time, title, meta description, H1, canonical, robots noindex,
visible words in the raw HTML (what Google sees before scripts), schema types, phone links, form, GA4/GTM,
viewport, sitemap URL count, page last-modified header. Read only. Standard library only.
"""
import html, json, os, re, sys, time, urllib.request, datetime

ROOT = '/Users/martindrendel/741website'
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36'


def get(url, timeout=25):
    t = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=timeout) as r:
            return {'status': r.status, 'url': r.geturl(), 'secs': round(time.time() - t, 2), 'headers': dict(r.headers),
                    'body': r.read().decode('utf-8', 'replace')}
    except urllib.error.HTTPError as e:
        return {'status': e.code, 'url': url, 'secs': round(time.time() - t, 2), 'headers': {}, 'body': ''}
    except Exception as e:
        return {'status': None, 'url': url, 'secs': round(time.time() - t, 2), 'headers': {}, 'body': '', 'error': str(e)[:200]}


def one(rx, s, flags=re.I | re.S):
    m = re.search(rx, s, flags); return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', m.group(1)))).strip() if m else ''


def facts(url, bdir=None):
    r = get(url); s = r['body']
    if bdir and s:
        os.makedirs(os.path.join(bdir, 'evidence'), exist_ok=True)
        open(os.path.join(bdir, 'evidence', 'home.html'), 'w', encoding='utf-8').write(s)
    vis = re.sub(r'<(script|style|noscript|template)\b.*?</\1>', ' ', s, flags=re.S | re.I)
    words = len(re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', vis))).split())
    types = sorted(set(re.findall(r'"@type"\s*:\s*"([^"]+)"', s)))
    http = get(re.sub(r'^https://', 'http://', url), timeout=15) if url.startswith('https://') else None
    root = re.match(r'(https?://[^/]+)', r['url'] or url).group(1)
    sm = get(root + '/sitemap.xml', timeout=15); sm_urls = len(re.findall(r'<loc>', sm['body'])) if sm['status'] == 200 else None
    if sm_urls is not None and '<sitemapindex' in sm['body']:
        sm_urls = sum(len(re.findall(r'<loc>', get(u, 15)['body'])) for u in re.findall(r'<loc>\s*([^<\s]+)', sm['body'])[:10])
    return {'url': url, 'checked_at': datetime.datetime.now().astimezone().isoformat(timespec='minutes'),
            'status': r['status'], 'final_url': r['url'], 'error': r.get('error'), 'secs': r['secs'],
            'http_redirects_to_https': (http['url'].startswith('https://') if http and http['status'] else None),
            'title': one(r'<title[^>]*>(.*?)</title>', s), 'meta_description': (re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', s, re.I) or [None, ''])[1],
            'h1': [one(r'(.*)', h) for h in re.findall(r'<h1[^>]*>(.*?)</h1>', s, re.I | re.S)][:3],
            'h2_count': len(re.findall(r'<h2\b', s, re.I)),
            'canonical': (re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', s, re.I) or [None, ''])[1],
            'noindex': bool(re.search(r'<meta[^>]+robots[^>]+noindex', s, re.I)),
            'visible_words_raw_html': words, 'schema_types': types,
            'tel_links': sorted(set(re.findall(r'href=["\']tel:([^"\']+)', s, re.I)))[:5], 'form': bool(re.search(r'<form\b', s, re.I)),
            'ga4': sorted(set(re.findall(r'G-[A-Z0-9]{6,}', s)))[:3], 'gtm': sorted(set(re.findall(r'GTM-[A-Z0-9]{4,}', s)))[:3],
            'viewport': bool(re.search(r'<meta[^>]+name=["\']viewport', s, re.I)), 'sitemap_urls': sm_urls,
            'last_modified': r['headers'].get('Last-Modified') or r['headers'].get('last-modified') or ''}


def recheck(slug):
    bdir = os.path.join(ROOT, '00_project', 'prospects', slug, 'booking')
    old = json.load(open(os.path.join(bdir, 'site-check.json'), encoding='utf-8'))
    f = facts(old['url']); json.dump(f, open(os.path.join(bdir, 'site-recheck.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    out = []
    for k in ('status', 'title', 'meta_description', 'h1', 'noindex', 'visible_words_raw_html', 'canonical'):
        a, b = old.get(k), f.get(k)
        if k == 'visible_words_raw_html' and isinstance(a, int) and isinstance(b, int) and abs(a - b) <= 0.2 * max(a, 1): continue
        if a != b: out.append(f'CHANGED {k}: {a!r} -> {b!r}')
    print('\n'.join(out) if out else f"NO CHANGE since {old.get('checked_at', '')[:10]}")


def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    if '--recheck' in sys.argv: return recheck(sys.argv[1])
    slug = sys.argv[1]; pdir = os.path.join(ROOT, '00_project', 'prospects', slug); bdir = os.path.join(pdir, 'booking')
    url = sys.argv[2] if len(sys.argv) > 2 else ''
    if not url and os.path.exists(os.path.join(bdir, 'baseline.md')):
        m = re.search(r'"website":\s*"([^"]+)"', open(os.path.join(bdir, 'baseline.md'), encoding='utf-8').read()); url = m.group(1) if m else ''
    if not url: sys.exit('No website URL. Pass it as the 2nd argument.')
    os.makedirs(bdir, exist_ok=True); f = facts(url, bdir)
    old = {}
    sp = os.path.join(pdir, 'evidence', 'site.json')
    if os.path.exists(sp):
        o = json.load(open(sp, encoding='utf-8'))
        old = {'title': o.get('home_title'), 'meta_description': o.get('home_meta'), 'h1': o.get('home_h1'),
               'visible_words_raw_html': o.get('home_words'), 'http_redirects_to_https': o.get('http_redirects_to_https'),
               'sitemap_urls': o.get('sitemap_urls') if isinstance(o.get('sitemap_urls'), int) else None,
               'secs': o.get('ttfb_secs'), 'evidence_date': datetime.date.fromtimestamp(os.path.getmtime(sp)).isoformat()}
    changed = []
    for k in ('title', 'meta_description', 'h1', 'visible_words_raw_html', 'http_redirects_to_https', 'sitemap_urls'):
        a, b = old.get(k), f.get(k)
        if isinstance(a, list) and a and isinstance(a[0], str): a = a[:3]
        if k == 'visible_words_raw_html' and isinstance(a, int) and isinstance(b, int) and abs(a - b) <= 0.2 * max(a, 1): continue
        if isinstance(a, str) and isinstance(b, str):
            na, nb = re.sub(r'\s+', ' ', a).strip().lower(), re.sub(r'\s+', ' ', b).strip().lower()
            if na == nb or (nb and nb in na) or (na and na in nb): continue   # scrape noise like "Chevron up"
        if a not in (None, '', []) and a != b: changed.append({'field': k, 'review_page': a, 'today': b})
    f['compared_with'] = 'evidence/site.json ' + old.get('evidence_date', '') if old else 'no site.json (old page): compare with baseline.md text by hand'
    f['changed_since_review'] = changed
    json.dump(f, open(os.path.join(bdir, 'site-check.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in f.items()}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
