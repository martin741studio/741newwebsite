#!/usr/bin/env python3
"""Prospect mini workflow: shared readers for the evidence files (used by draft_prospect.py, factcheck.py, draft_home.py).

Every function reads one evidence file and returns plain values. Missing files return None or {}.
facts(pdir) collects all derived numbers (counts, means, distances) in one dict; factcheck.py treats it as evidence
because every value in it is computed from an evidence file. Read only. Standard library only.
"""
import glob, json, math, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
MINI = os.path.join(ROOT, '00_project', 'prospect-mini')
# Local Falcon category keys -> the German words Google shows in the panel
CAT_DE = {'alternative_medicine_practitioner': 'Alternativmediziner', 'naturopathic_practitioner': 'Naturheilpraktiker',
          'heilpraktiker': 'Heilpraktiker', 'physical_therapist': 'Physiotherapeut', 'physiotherapy_center': 'Physiotherapiezentrum',
          'osteopath': 'Osteopath', 'occupational_therapist': 'Ergotherapeut', 'massage_therapist': 'Massagetherapeut',
          'psychotherapist': 'Psychotherapeut', 'psychologist': 'Psychologe', 'counselor': 'Berater', 'acupuncturist': 'Akupunkteur',
          'homeopath': 'Homöopath', 'lawyer': 'Rechtsanwalt', 'law_firm': 'Anwaltskanzlei', 'tax_consultant': 'Steuerberater',
          'dentist': 'Zahnarzt', 'doctor': 'Arzt', 'medical_clinic': 'Klinik', 'beauty_salon': 'Kosmetikstudio', 'hair_salon': 'Friseursalon',
          'speech_pathologist': 'Logopäde', 'chiropractor': 'Chiropraktiker', 'yoga_studio': 'Yogastudio', 'coach': 'Coach',
          'life_coach': 'Lebensberater', 'business_management_consultant': 'Unternehmensberater', 'consultant': 'Berater'}
COUNTRY = {'de': ('DE', 2276), 'at': ('AT', 2040), 'ch': ('CH', 2756)}


def jload(path):
    try:
        return json.load(open(path, encoding='utf-8'))
    except Exception:
        return None


def ev(pdir, *names):
    """First existing evidence file of the given names (glob patterns allowed), newest first."""
    for n in names:
        hits = sorted(glob.glob(os.path.join(pdir, 'evidence', n)), key=os.path.getmtime, reverse=True)
        if hits: return hits[0]
    return None


def de(n, dec=0):
    """German number: 1900 -> 1.900, 4.08 (dec 1) -> 4,1, 48.98 (dec 1) -> 49 (no trailing ,0)."""
    s = f'{n:,.{dec}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return s[:-2] if dec == 1 and s.endswith(',0') else s


def pct(x):
    return de(float(x), 1) + ' %'


def haversine(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (float(a[0]), float(a[1]), float(b[0]), float(b[1])))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def domain(url):
    return re.sub(r'^https?://(www\.)?', '', (url or '').lower()).split('/')[0]


# ---------------------------------------------------------------- intake
def intake(pdir):
    """intake.json from intake.py, else the "- Key: value" lines of a hand-written intake.md."""
    j = jload(os.path.join(pdir, 'intake.json'))
    if j: return j
    md = os.path.join(pdir, 'intake.md')
    out = {}
    if os.path.exists(md):
        s = open(md, encoding='utf-8').read()
        for k, key in [('Name', 'name'), ('Business', 'business'), ('Website', 'website')]:
            m = re.search(r'^- ' + k + r':\s*(.+)$', s, re.M)
            if m: out[key] = m.group(1).strip()
        if out.get('website'): out['website'] = out['website'].split()[0]
        if out.get('business'): out['business'] = re.sub(r'\s*\(.*\)$', '', out['business'])
        m = re.search(r'location_code (\d+)', s)
        if m: out['location_code'] = int(m.group(1))
        if re.search(r'Form of address on (her|his|the) site: "Sie"', s): out['site_address'] = 'Sie'
        m = re.search(r'Branch class: (\w+)', s)
        if m: out['branch'] = m.group(1)
    return out


# ---------------------------------------------------------------- Local Falcon
def falcon(pdir):
    """The newest falcon-report-*.json as one flat dict (both the MCP wrapper and the flat form)."""
    f = ev(pdir, 'falcon-report-*.json')
    d = jload(f) if f else None
    if not d: return None
    if 'result' in d: d = json.loads(d['result']['content'][0]['text'])
    d = d.get('data', d)
    places = d.get('places') or {}
    d['_places'] = list(places.values()) if isinstance(places, dict) else list(places)
    d['_file'] = os.path.relpath(f, pdir)
    return d


def own_place(fr, place_id=None, website=None, name=None):
    """The prospect's own row in the report: place_id, then website domain, then name words."""
    if not fr: return None
    pid = place_id or fr.get('place_id') or (fr.get('location') or {}).get('place_id')
    for p in fr['_places']:
        if pid and p.get('place_id') == pid: return p
    dom = domain(website)
    for p in fr['_places']:
        if dom and domain(p.get('url') or p.get('display_url')) == dom: return p
    words = [w for w in re.findall(r'\w{4,}', (name or '').lower())]
    for p in fr['_places']:
        if words and all(w in (p.get('name') or '').lower() for w in words[:2]): return p
    return fr.get('location')


def cats_de(p):
    c = p.get('categories') or {}
    keys = list(c.keys()) if isinstance(c, dict) else list(c)
    out = []
    for k in keys:
        v = c[k] if isinstance(c, dict) else k
        de_ = CAT_DE.get(k) or (re.search(r'^(\w+) \(', str(v)) or [None, None])[1] or str(v)
        out.append(de_)
    return ', '.join(out[:2])


# ---------------------------------------------------------------- DataForSEO
def volumes(pdir):
    f = ev(pdir, 'dfs-volumes-ads.json', 'dfs-volumes.json')
    d = jload(f) if f else None
    rows = []
    for t in (d or {}).get('tasks') or []:
        rows += t.get('result') or []
    return rows, (os.path.relpath(f, pdir) if f else None)


def merged_groups(rows):
    """Keyword groups that Google reports with identical volume, cpc, competition and monthly series (one merged variant)."""
    g = {}
    for r in rows:
        if r.get('search_volume') is None: continue
        ms = tuple((m.get('year'), m.get('month'), m.get('search_volume')) for m in r.get('monthly_searches') or [])
        g.setdefault((r['search_volume'], r.get('cpc'), r.get('competition'), ms), []).append(r['keyword'])
    return [{'keywords': v, 'volume': k[0], 'cpc': k[1]} for k, v in g.items() if len(v) > 1]


def serp_items(pdir, name):
    d = jload(os.path.join(pdir, 'evidence', name))
    t = ((d or {}).get('tasks') or [{}])[0]
    r = (t.get('result') or [{}])[0] or {}
    return (t.get('data') or {}).get('keyword'), [i for i in r.get('items') or [] if i.get('type') == 'organic'], t.get('status_code')


def spam(pdir):
    s, b = jload(os.path.join(pdir, 'evidence', 'dfs-refdomains-spam.json')), jload(os.path.join(pdir, 'evidence', 'dfs-backlinks-summary.json'))
    try:
        n = s['tasks'][0]['result'][0]['total_count']; tot = b['tasks'][0]['result'][0]['referring_domains']
        return n, tot
    except Exception:
        return None


# ---------------------------------------------------------------- site, panel, score
def site(pdir):
    return jload(os.path.join(pdir, 'evidence', 'site.json')) or {}


def pages(pdir, name='site-pages.json'):
    d = jload(os.path.join(pdir, 'evidence', name))
    if isinstance(d, dict): d = d.get('pages', list(d.values()))
    return d or []


def panel(pdir):
    """Rating, review count, owner replies, newest review age, category from evidence/google-panel-*.md."""
    f = ev(pdir, 'google-panel-*.md')
    if not f: return {}
    s = open(f, encoding='utf-8').read()
    out = {'_file': os.path.relpath(f, pdir)}
    m = re.search(r'Rating:\s*([\d,\.]+)\s*·\s*(\d+)', s)
    if m: out['rating'], out['reviews'] = float(m.group(1).replace(',', '.')), int(m.group(2))
    m = re.search(r'Owner replies:\s*(\d+)', s)
    if m: out['replies'] = int(m.group(1))
    m = re.search(r'newest review about (\d+) (year|month|week)', s)
    if m: out['newest'] = f'{m.group(1)} {m.group(2)}'
    m = re.search(r'Category shown:\s*([^\(\n]+)', s)
    if m: out['category'] = m.group(1).strip()
    m = re.search(r'Phone:\s*([+\d][\d \-/]+\d)', s)
    if m: out['phone'] = m.group(1).strip()
    m = re.search(r'Address:\s*(.+)', s)
    if m: out['address'] = m.group(1).strip()
    return out


def score_today(pdir):
    f = os.path.join(pdir, 'evidence', 'scorecard-today.md')
    if not os.path.exists(f): return None
    m = re.search(r'Total:\s*\**\s*(\d+)\s*/\s*44', open(f, encoding='utf-8').read())
    return int(m.group(1)) if m else None


def slugify(s):
    import unicodedata
    s = s.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss').strip('"')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def stem(w):
    return w[:max(5, len(w) - 3)]


# ---------------------------------------------------------------- derived facts
def facts(pdir):
    """All derived numbers in one dict. Every value names its source file in "src"."""
    it, fr = intake(pdir), falcon(pdir)
    F = {}
    if fr:
        pts = int(fr.get('points') or int(fr.get('grid_size', 7)) ** 2)
        me = own_place(fr, it.get('place_id'), it.get('website'), it.get('business') or it.get('name')) or {}
        solv = float(me.get('solv', fr.get('solv') or 0))
        found = int(me.get('found_in', fr.get('found_in') or 0))
        top = sorted([p for p in fr['_places'] if p is not me], key=lambda p: -float(p.get('solv') or 0))
        ctr = (fr.get('lat'), fr.get('lng'))
        ahead = [p for p in top if float(p.get('solv') or 0) > solv]
        F['scan'] = {'src': fr['_file'], 'keyword': fr.get('keyword'), 'points': pts, 'grid_size': int(fr.get('grid_size', 7)),
                     'radius_km': float(fr.get('radius') or 0), 'centre': ctr, 'date': fr.get('date'), 'timestamp': fr.get('timestamp'),
                     'top3_points': round(solv * pts / 100), 'top3_pair': f'{round(solv * pts / 100)}/{pts}', 'found_in': found,
                     'found_pair': f'{found}/{pts}', 'not_top20': pts - found, 'solv': solv, 'arp': me.get('arp', fr.get('arp')),
                     'me_name': me.get('name'), 'me_reviews': int(me.get('reviews') or 0), 'me_rating': me.get('rating'),
                     'me_km': round(haversine(ctr, (me['lat'], me['lng'])), 2) if me.get('lat') and ctr[0] else None,
                     'ahead': len(ahead), 'ahead_found_all': sum(1 for p in ahead[:4] if int(p.get('found_in') or 0) == pts),
                     'top4': [{'name': p.get('name'), 'solv': float(p.get('solv') or 0), 'reviews': int(p.get('reviews') or 0),
                               'cats': cats_de(p), 'found_in': int(p.get('found_in') or 0), 'url': p.get('url'),
                               'km': round(haversine(ctr, (p['lat'], p['lng'])), 2) if p.get('lat') and ctr[0] else None} for p in top[:6]]}
        t4 = F['scan']['top4'][:4]
        F['scan']['top4_pair_found_all'] = f"{sum(1 for p in t4 if p['found_in'] == pts)}/{len(t4)}"
        F['scan']['reviews_range'] = [min([p['reviews'] for p in t4] or [0]), max([p['reviews'] for p in t4] or [0])]
        F['scan']['km_range'] = [min([p['km'] for p in t4 if p['km'] is not None] or [0]), max([p['km'] for p in t4 if p['km'] is not None] or [0])]
        kw = (fr.get('keyword') or '').split()
        prov = kw[0] if kw else ''
        words = {w.lower()[:5] for p in t4 for w in re.findall(r'[A-Za-zÄÖÜäöüß]{4,}', p['cats'])}
        F['scan']['top4_category_pairs'] = {w: f"{sum(1 for p in t4 if w in p['cats'].lower())}/{len(t4)}" for w in sorted(words)}  # e.g. coach: 3/4
        F['scan']['top4_pair_provider_cat'] = f"{sum(1 for p in t4 if stem(prov) in p['cats'].lower() or 'heilprakt' in p['cats'].lower())}/{len(t4)}" if prov else None
    rows, vf = volumes(pdir)
    if rows:
        F['volumes'] = {'src': vf, 'merged': merged_groups(rows), 'no_data': [r['keyword'] for r in rows if r.get('search_volume') is None],
                        'newest_month': max([(m['year'], m['month']) for r in rows for m in r.get('monthly_searches') or []] or [None])}
    s = site(pdir)
    if s:
        tt = s.get('ttfb_secs') or []
        F['site'] = {'src': 'evidence/site.json', 'ttfb_mean': round(sum(tt) / len(tt), 2) if tt else None, 'home_words': s.get('home_words'),
                     'pages_measured': s.get('pages_measured'), 'pages_no_h1': s.get('pages_no_h1'),
                     'pages_no_h1_pair': f"{s.get('pages_no_h1')}/{s.get('pages_measured')}", 'duplicates': len(s.get('duplicate_pages') or [])}
    cp = [c for c in pages(pdir, 'comp-pages.json') if c.get('status') == 'ok' and c.get('words')]
    if cp:
        kw = (F.get('scan') or {}).get('keyword') or ''
        w = kw.split()
        hit = [c for c in cp if w and any(stem(w[0]) in h.lower() and (len(w) < 2 or w[-1] in h.lower()) for h in c.get('h1') or [])]
        F['comp'] = {'src': 'evidence/comp-pages.json', 'measured': len(cp), 'words': [c['words'] for c in cp],
                     'mean_words': round(sum(c['words'] for c in cp) / len(cp)), 'h1_keyword': len(hit),
                     'h1_keyword_pair': f'{len(hit)}/{len(cp)}', 'h1_keyword_urls': [c['url'] for c in hit]}
    sp = spam(pdir)
    if sp: F['spam'] = {'src': 'evidence/dfs-refdomains-spam.json + dfs-backlinks-summary.json', 'spam': sp[0], 'total': sp[1], 'pair': f'{sp[0]}/{sp[1]}'}
    pn = panel(pdir)
    if pn:
        F['panel'] = dict(pn, src=pn.get('_file'))
        if 'replies' in pn and 'reviews' in pn: F['panel']['replies_pair'] = f"{pn['replies']}/{pn['reviews']}"
    names = []
    dom = domain(it.get('website') or s.get('home'))
    for f in sorted(glob.glob(os.path.join(pdir, 'evidence', 'dfs-serp-name*.json'))):
        kw, items, code = serp_items(pdir, os.path.basename(f))
        if code != 20000: continue
        pos = next((i.get('rank_group') for i in items if domain(i.get('url') or i.get('domain')) == dom), None)
        names.append({'src': os.path.relpath(f, pdir), 'keyword': kw, 'organic': len(items), 'own_rank': pos})
    if names: F['names'] = names
    sc = score_today(pdir)
    if sc is not None: F['score_today'] = {'src': 'evidence/scorecard-today.md', 'score': sc, 'pair': f'{sc}/44'}
    return F
