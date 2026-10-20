#!/usr/bin/env python3
"""Prospect mini workflow, step 0: intake in one command (proposal 27, 2026-10-12).

Usage: intake.py <name> <website> [maps-link] [--business "<name on Google>"] [--city <city>] [--linkedin <url>]
                 [--country DE|AT|CH] [--no-place] [--slug <slug>] [--out <prospect_dir>]
--slug sets the folder and page name (e.g. <name>-v2 when an old page must stay online until a go).
Does: site reachable (status + final URL), Sie/du count on the homepage, country from the domain (DE 2276 / AT 2040 / CH 2756),
old review page (grep 04_site/review/ and prospects/), place_id (from the Maps link, else ONE place search),
existing Local Falcon scans for that place (free list).
Writes <prospect_dir>/intake.md, intake.json, run-state.json and the first browser-queue.jsonl jobs
(maps_search if no place, linkedin_chat, maps_panel, home_shot) in the format of workflow section 1b.
COST: the place search costs 2 Local Falcon credits per hit. It runs at most once, and never with --no-place or
when the Maps link has a place_id. The scan list is free. No DataForSEO calls.
"""
import datetime, html, json, os, re, subprocess, sys, time, unicodedata, urllib.request
from urllib.parse import unquote, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
COUNTRY = {'de': ('DE', 2276), 'at': ('AT', 2040), 'ch': ('CH', 2756)}
BRANCH = [('health', r'heilprakt|naturheil|physio|osteopath|ergothera|psychothera|logopäd|praxis für|therapie|massage|hebamme|zahnarzt|arzt|ärztin'),
          ('legal', r'rechtsanw|kanzlei|anwält|notar|steuerber'), ('service', r'.')]
SIE = r'\b(Sie|Ihnen|Ihr|Ihre|Ihren|Ihrem|Ihrer)\b'
DU = r'\b(du|dich|dir|dein|deine|deinen|deinem|deiner|euch|euer|eure|euren)\b'


def slugify(s):
    s = s.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def get(url, timeout=20):
    t = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=timeout) as r:
            return dict(status=r.status, url=r.geturl(), secs=round(time.time() - t, 2), body=r.read().decode('utf-8', 'replace'))
    except urllib.error.HTTPError as e:
        return dict(status=e.code, url=url, secs=round(time.time() - t, 2), body='')
    except Exception as e:
        return dict(status=None, url=url, secs=None, body='', error=str(e)[:160])


def visible(h):
    h = re.sub(r'<(script|style|noscript|svg)\b.*?</\1>|<!--.*?-->', ' ', h, flags=re.S | re.I)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()


def maps_link(link):
    """place_id, CID and coordinates from a Google Maps link (any part may be missing)."""
    out = {}
    if not link: return out
    u = unquote(link)
    m = re.search(r'(?:place_id[:=]|query_place_id=)(ChI[\w-]+)', u) or re.search(r'!1s(ChI[\w-]+)', u)
    if m: out['place_id'] = m.group(1)
    m = re.search(r'(0x[0-9a-f]+:0x[0-9a-f]+)', u)
    if m: out['cid'] = m.group(1)
    m = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', u) or re.search(r'!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)', u)
    if m: out['lat'], out['lng'] = float(m.group(1)), float(m.group(2))
    m = re.search(r'/place/([^/@]+)', u)
    if m: out['maps_name'] = m.group(1).replace('+', ' ')
    return out


def country(dom, text, place_addr, forced):
    if forced: return forced.upper(), dict(COUNTRY.values())[forced.upper()], 'argument'
    tld = dom.rsplit('.', 1)[-1]
    if tld in COUNTRY: return COUNTRY[tld] + ('domain .' + tld,)
    a = (place_addr or '') + ' '
    for k, words in [('at', r'Österreich|Austria|\b\d{4} Wien\b'), ('ch', r'Schweiz|Switzerland'), ('de', r'Deutschland|Germany|\b\d{5}\b')]:
        if re.search(words, a): return COUNTRY[k] + ('place address',)
    for k, pre in [('at', r'\+43|0043'), ('ch', r'\+41|0041'), ('de', r'\+49|0049')]:
        if re.search(pre, text): return COUNTRY[k] + (f'phone prefix {pre.split("|")[0]} on the site',)
    return COUNTRY['de'] + ('default (no hint found: CHECK)',)


def old_pages(slug, dom, name):
    """Old review pages or prospect folders: folder names with the last name, files that contain the domain."""
    hits = []
    last = slugify(name).split('-')[-1]
    first_ = slugify(name).split('-')[0] if '-' in slugify(name) else ''
    for base in ('04_site/review', '00_project/prospects'):
        d = os.path.join(ROOT, base)
        if not os.path.isdir(d): continue
        for f in os.listdir(d):
            if not (f == slug or f.startswith(slug + '-') or (last and first_ and last in f and first_ in f)): continue  # same person, not only the same last name
            if base.endswith('prospects') and f == slug and set(os.listdir(os.path.join(d, f))) <= {'evidence', 'intake.md', 'intake.json', 'run-state.json', 'browser-queue.jsonl'}:
                continue  # the folder this intake just made
            hits.append(f'{base}/{f}')
    r = subprocess.run(['grep', '-rlis', '--include=*.html', '--include=*.json', dom.replace('www.', ''), os.path.join(ROOT, '04_site', 'review')],
                       capture_output=True, text=True, timeout=60)
    hits += [os.path.relpath(x, ROOT) for x in r.stdout.split()]
    return sorted(set(hits))


def lf_lookup(pid, business, city, allow_place):
    """(place rows, matching scans). One place search at most (2 credits per hit); the report list is free."""
    import find_scan as fs
    sid = fs.lf['session']()
    found, note = [], ''
    if not pid and allow_place:
        found = fs.places(sid, business, city)
        note = f'place search "{business}"' + (f' near "{city}"' if city else '') + f': {len(found)} hit(s), 2 credits per hit'
    pid = pid or (found[0]['place_id'] if found else None)
    words = [w.lower() for w in re.findall(r'\w{4,}', business)][:2]
    scans = []
    for r in fs.reports(sid):
        loc = r.get('location') or {}
        hay = ' '.join(str(loc.get(k, '')) for k in ('name', 'address', 'place_id')).lower()
        if (pid and pid.lower() in hay) or (not pid and words and all(w in hay for w in words)):
            scans.append({'report_key': r.get('report_key'), 'date': r.get('date'), 'keyword': r.get('keyword'), 'grid_size': r.get('grid_size'), 'name': loc.get('name')})
    return pid, found, scans, note


def opt(args, flag, has_value=True):
    if flag not in args: return None
    i = args.index(flag)
    if not has_value: del args[i]; return True
    v = args[i + 1]; del args[i:i + 2]; return v


def main():
    t0 = time.time()
    args = sys.argv[1:]
    business, city, linkedin, forced, out = opt(args, '--business'), opt(args, '--city'), opt(args, '--linkedin'), opt(args, '--country'), opt(args, '--out')
    no_place = bool(opt(args, '--no-place', False))
    slug_arg = opt(args, '--slug')
    name, website = args[0], args[1]
    link = args[2] if len(args) > 2 else None
    if not website.startswith('http'): website = 'https://' + website
    slug = slug_arg or slugify(name)
    pdir = out or os.path.join(ROOT, '00_project', 'prospects', slug)
    os.makedirs(os.path.join(pdir, 'evidence'), exist_ok=True)
    now = datetime.datetime.now().isoformat(timespec='minutes')
    dom = urlparse(website).netloc.lower()

    h = get(website)
    text = visible(h['body'])
    title = (re.search(r'<title[^>]*>(.*?)</title>', h['body'], re.S | re.I) or [None, ''])[1].strip()
    sie, du = len(re.findall(SIE, text)), len(re.findall(DU, text, re.I))
    addr = 'Sie' if sie > du else 'du' if du > sie else 'unklar'
    blob = (title + ' ' + text[:4000]).lower()
    branch = next(b for b, rx in BRANCH if re.search(rx, blob))

    ml = maps_link(link)
    business = business or ml.get('maps_name') or name
    pid, places, scans, lf_note, lf_err = ml.get('place_id'), [], [], '', None
    try:
        pid, places, scans, lf_note = lf_lookup(pid, business, city, not no_place)
    except Exception as e:
        lf_err = str(e)[:200]
    place = places[0] if places else {}
    cc, loc_code, cc_why = country(dom, text, place.get('address'), forced)
    old = old_pages(slug, dom, name)

    it = {'slug': slug, 'name': name, 'first_name': name.split()[0], 'business': business, 'website': h['url'] or website,
          'website_status': h['status'], 'website_secs': h['secs'], 'website_error': h.get('error'), 'home_title': title,
          'site_address': addr, 'sie_count': sie, 'du_count': du, 'branch': branch, 'country': cc, 'location_code': loc_code,
          'country_source': cc_why, 'city': city, 'maps_link': link, 'place_id': pid, 'cid': ml.get('cid'),
          'lat': ml.get('lat'), 'lng': ml.get('lng'), 'place_search': places, 'place_note': lf_note, 'lf_error': lf_err,
          'scans': scans, 'old_pages': old, 'linkedin': linkedin, 'at': now}
    json.dump(it, open(os.path.join(pdir, 'intake.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    L = [f'# Intake: {name} (step 0, {now[:10]}, intake.py)', '',
         f'- Name: {name}', f'- Business: {business}', f'- Website: {it["website"]} ({h["status"]}' + (f', {h["error"]}' if h.get('error') else '') + f', {h["secs"]} s)',
         f'- Home title: {title or "(none)"}',
         f'- Form of address on the site: "{addr}" (Sie-forms {sie}, du-forms {du}). Page = "du"; homepage draft = "{addr if addr != "unklar" else "Sie"}".',
         f'- Branch class: {branch}' + (' (HWG: no healing or success promise, no protected titles)' if branch == 'health' else ''),
         f'- Country: {cc}, location_code {loc_code} (from {cc_why}).',
         f'- City: {city or "(not given: take it from the place address)"}',
         f'- Google profile: place_id {pid or "NOT FOUND"}' + (f' · CID {ml["cid"]}' if ml.get('cid') else '') + (f' · {lf_note}' if lf_note else '') + (f' · Local Falcon error: {lf_err}' if lf_err else '')]
    for p in places: L.append(f'  - {p.get("name")} · {p.get("address")} · {p.get("place_id")}')
    if places and len(places) > 1: L.append('  - More than one hit: the operator job maps_panel must confirm website AND phone.')
    L.append(f'- Existing scans (0 credits): {len(scans)}')
    for s in scans: L.append(f'  - {s["report_key"]} · {s["date"]} · "{s["keyword"]}" · {s["grid_size"]}x{s["grid_size"]}')
    L.append(f'- Old review page / folder: {", ".join(old) if old else "none (grep 04_site/review/ and prospects/)"}' + (' → gate G4' if old else ''))
    L.append(f'- Channel: {"LinkedIn " + linkedin if linkedin else "(no LinkedIn URL given)"}; chat = operator job linkedin_chat.')
    L.append(f'- Loom: none yet (placeholder)')
    L += ['', f'Run time intake.py: {time.time() - t0:.1f} s']
    open(os.path.join(pdir, 'intake.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

    rs_path = os.path.join(pdir, 'run-state.json')
    rs = json.load(open(rs_path, encoding='utf-8')) if os.path.exists(rs_path) else {'slug': slug, 'steps': {}}
    blockers = ([] if pid else ['no place_id: operator job maps_search']) + ([f'site status {h["status"]}'] if h['status'] != 200 else []) + (['old page: gate G4'] if old else [])
    rs['steps']['intake'] = {'agent': 'orchestrator', 'status': 'done', 'at': now, 'outputs': ['intake.md', 'intake.json', 'browser-queue.jsonl'], 'blockers': blockers}
    for k, a in [('demand', 'A'), ('site', 'B'), ('homepage', 'C'), ('scan', 'D')]:
        rs['steps'].setdefault(k, {'agent': a, 'status': 'waiting'})
    json.dump(rs, open(rs_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    q_path = os.path.join(pdir, 'browser-queue.jsonl')
    have = set()
    if os.path.exists(q_path):
        have = {json.loads(l).get('id') for l in open(q_path, encoding='utf-8') if l.strip()}
    day = now[:10]
    jobs = []
    if not pid and not link:
        jobs.append({'id': 'maps-search', 'type': 'maps_search', 'url': f'https://www.google.com/maps/search/{business} {city or ""}'.strip(), 'out': 'evidence/maps-match.md',
                     'match': {'website': dom, 'phone': 'from the site'}})
    if linkedin:
        jobs.append({'id': 'chat', 'type': 'linkedin_chat', 'url': linkedin if linkedin.startswith('http') else 'https://' + linkedin, 'out': f'evidence/chat-{day}.md'})
    if pid or link:
        jobs.append({'id': 'panel', 'type': 'maps_panel', 'url': f'https://www.google.com/maps/place/?q=place_id:{pid}&hl=de' if pid else link, 'out': f'evidence/google-panel-{day}.md'})
    jobs.append({'id': 'home-shot', 'type': 'home_shot', 'url': it['website'], 'out': 'evidence/home-today-1440.jpg', 'also': 'evidence/home-images.txt'})
    with open(q_path, 'a', encoding='utf-8') as f:
        for j in jobs:
            if j['id'] in have: continue
            f.write(json.dumps(dict({'id': j['id'], 'slug': slug}, **{k: v for k, v in j.items() if k != 'id'}, by='orchestrator', at=now, status='queued'), ensure_ascii=False) + '\n')
    print(json.dumps({'dir': pdir, 'slug': slug, 'status': h['status'], 'address': addr, 'country': cc, 'place_id': pid, 'scans': len(scans),
                      'old': old, 'jobs': [j['id'] for j in jobs if j['id'] not in have], 'secs': round(time.time() - t0, 1)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
