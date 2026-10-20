"""Phase 1: free live-site check (homepage + robots + sitemap + selected URLs). Read only."""
import json, re, ssl, sys, time, urllib.request, urllib.parse, os, datetime
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = sys.argv[1] if len(sys.argv) > 1 else 'https://www.stuerzl-steuerstrafrecht.de'
UA = {'User-Agent': 'Mozilla/5.0 (maps-audit; read-only)'}
def get(url):
    t0 = time.time()
    try:
        req = urllib.request.Request(url, headers=UA)
        r = urllib.request.urlopen(req, timeout=30)
        body = r.read().decode('utf-8', 'replace')
        return dict(url=url, final=r.geturl(), status=r.status, ttfb_total_s=round(time.time()-t0, 2), body=body, headers=dict(r.headers))
    except urllib.error.HTTPError as e:
        return dict(url=url, status=e.code, final=url, body=e.read().decode('utf-8', 'replace')[:2000], headers=dict(e.headers), ttfb_total_s=round(time.time()-t0, 2))
    except Exception as e:
        return dict(url=url, status=None, error=str(e), body='', headers={})
def parse(b):
    g = lambda p: (re.findall(p, b, re.S | re.I) or [''])
    jl = re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', b, re.S | re.I)
    types = []
    for j in jl:
        try:
            o = json.loads(j); o = o if isinstance(o, list) else [o]
            for x in o:
                if isinstance(x, dict) and '@graph' in x: o += x['@graph']
            types += [str(x.get('@type')) for x in o if isinstance(x, dict)]
        except Exception: types.append('unparseable')
    return dict(title=re.sub(r'\s+', ' ', g(r'<title[^>]*>(.*?)</title>')[0]).strip(),
        meta_description=(re.findall(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', b, re.S | re.I) or [''])[0].strip(),
        h1=[re.sub(r'<[^>]+>|\s+', ' ', x).strip() for x in re.findall(r'<h1[^>]*>(.*?)</h1>', b, re.S | re.I)],
        canonical=(re.findall(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']', b, re.I) or [''])[0],
        og_image=bool(re.search(r'property=["\']og:image', b, re.I)), robots_meta=(re.findall(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']', b, re.I) or [''])[0],
        jsonld_types=types, ga4=sorted(set(re.findall(r'G-[A-Z0-9]{8,12}', b))), gtm=sorted(set(re.findall(r'GTM-[A-Z0-9]{6,8}', b))),
        aw=sorted(set(re.findall(r'AW-\d{8,12}', b))), imgs=len(re.findall(r'<img\b', b, re.I)), imgs_no_alt=len(re.findall(r'<img\b(?![^>]*\balt=)[^>]*>', b, re.I)),
        tel_links=sorted(set(re.findall(r'href=["\']tel:([^"\']+)', b, re.I))), mailto=sorted(set(re.findall(r'href=["\']mailto:([^"\']+)', b, re.I))),
        has_form=bool(re.search(r'<form\b', b, re.I)), words=len(re.sub(r'<script.*?</script>|<style.*?</style>|<[^>]+>', ' ', b, flags=re.S | re.I).split()))
out = dict(base=BASE, collected_at=datetime.datetime.now().astimezone().isoformat(timespec='seconds'), pages={})
for path in ['/', '/robots.txt', '/sitemap.xml', '/index.php/schwerpunkte', '/index.php/kontakt', '/index.php/impressum', '/index.php/steuerstrafrecht']:
    r = get(BASE + path); b = r.pop('body'); r.pop('headers', None)
    r['parsed'] = parse(b) if path != '/robots.txt' and r.get('status') == 200 else None
    if path == '/robots.txt': r['robots_txt'] = b[:1500]
    if path == '/' : r['text_sample'] = re.sub(r'\s+', ' ', re.sub(r'<script.*?</script>|<style.*?</style>|<[^>]+>', ' ', b, flags=re.S | re.I))[:1500]
    if path == '/index.php/impressum': r['text_sample'] = re.sub(r'\s+', ' ', re.sub(r'<script.*?</script>|<style.*?</style>|<[^>]+>', ' ', b, flags=re.S | re.I))[:2500]
    out['pages'][path] = r
    print(path, r.get('status'), r.get('final'), (r.get('parsed') or {}).get('title'))
json.dump(out, open(os.path.join(RUN, 'evidence', 'site-check-2026-10-11.json'), 'w'), ensure_ascii=False, indent=1)
