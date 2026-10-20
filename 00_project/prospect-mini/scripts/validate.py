#!/usr/bin/env python3
"""Prospect mini workflow, step 7: check the built page before anybody sees it.

Usage: validate.py <prospect_dir>
Fails (exit 1) on: jargon in visible text, missing local images, text from another prospect,
empty sections, missing sources block, "0" search volumes, Martin-guide bubbles longer than 2 sentences,
"TODO" placeholders anywhere in prospect.json (draft_prospect.py skeleton),
hero text longer than 14 / 28 / 35 words (headline / subline / paragraph).
Warns on: "Sie" in the reader text (house form is "du"), protected titles, missing loom_url, long guide bubbles,
calc values off their slider step, demand rows that are one merged Google variant (double count).
Writes prospects/<slug>/_run.json for the overview Excel (v2, 2026-10-12).
"""
import json, os, re, sys, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
JARGON = ['Pool', 'H1', 'SoLV', 'Schema', 'Sitemap', 'Citation', 'Backlink', 'NAP', 'Canonical', 'E-E-A-T', 'Local Pack',
          'Lawyer', 'attorney', 'Physical therapist', 'Counselor', 'CRO', 'Un-Burning', 'Falcon', 'DataForSEO', 'SERP', 'Keyword', 'Book a call']
FOREIGN = ['Stürzl', 'STÜRZL', 'Steuerstraf', 'Kanzlei', 'Mandant']
PROTECTED = ['Psychotherapeut', 'Psychotherapeutin', 'Psychologe', 'Psychologin', 'Facharzt', 'Fachärztin', 'Fachanwalt', 'Fachanwältin']
ZERO_VOL = r'(?<![\d.,])0\s*(?:x\s*)?(?:Suchanfragen|Suchen|Anfragen|mal gesucht|Mal gesucht)'
SIE_OK = [r'Sie\s+bringen\s+Anfragen\s+sofort', r'Sie\s+brauchen\s+ein\s+paar\s+Monate']  # template: plural "they", not the reader
# slider steps from calc() in build_page.py: key -> (step, origin key or fixed origin)
STEPS = {'vol': (10, ('vol_min', 50)), 'budget': (50, 0), 'cpc': (0.1, 0.5), 'conv': (0.5, 1), 'deal': (1, 5), 'val': (50, ('val_min', 100))}


def calc_steps(c):
    """Calculator start values that are not on their slider step."""
    out = []
    for k, (step, o) in STEPS.items():
        if not isinstance(c.get(k), (int, float)): continue
        o = c.get(o[0], o[1]) if isinstance(o, tuple) else o
        n = (c[k] - o) / step
        if abs(n - round(n)) > 1e-6: out.append(f'calc.{k}={c[k]} is not on its slider step ({step} from {o})')
    return out


def merged_variants(pdir, demand):
    """Demand rows with the same volume whose keywords Google reports with identical volume, cpc and competition."""
    f = os.path.join(pdir, 'evidence', 'dfs-volumes-ads.json')
    if not demand or not os.path.exists(f): return []
    m = {}
    for t in json.load(open(f, encoding='utf-8')).get('tasks') or []:
        for r in t.get('result') or []:
            m[r.get('keyword', '').lower()] = (r.get('search_volume'), r.get('cpc'), r.get('competition'),
                                               tuple(x.get('search_volume') for x in r.get('monthly_searches') or []))  # same monthly series too
    out = []
    for i, a in enumerate(demand):
        for b in demand[i + 1:]:
            ka, kb = a.get('keyword', '').lower(), b.get('keyword', '').lower()
            if a.get('volume') == b.get('volume') and ka in m and m[ka] == m.get(kb) and m[ka][0] is not None:
                out.append(f'demand: "{ka}" and "{kb}" look like one merged Google variant ({a.get("volume")}); do not add them up')
    return out


HERO_MAX = {'headline': 14, 'subline': 28, 'paragraph': 35}  # words; Martin 2026-10-12: hero text was far too big and too long


def hero_length(p):
    """Hero text longer than HERO_MAX words (headline, the block subline inside the H1, the paragraph)."""
    hl = p.get('headlines') or {}
    h1 = hl.get('hero_h1') or ''
    sub_in = ' '.join(re.findall(r'<span[^>]*display:block[^>]*>(.*?)</span>', h1, re.S))
    main = re.sub(r'<span[^>]*display:block[^>]*>.*?</span>', ' ', h1, flags=re.S)
    para = hl.get('hero_sub') or (p.get('hero') or {}).get('sub') or ''
    out = []
    for name, txt in (('headline', main), ('subline', sub_in), ('paragraph', para)):
        n = len(re.sub(r'<[^>]+>', ' ', txt).split())
        if n > HERO_MAX[name]: out.append(f'hero {name}: {n} words (max {HERO_MAX[name]}); shorten it')
    return out


def todo_paths(x, path=''):
    """Field paths in prospect.json whose text still contains a "TODO" placeholder."""
    if isinstance(x, dict): return [q for k, v in x.items() for q in todo_paths(v, f'{path}.{k}' if path else k)]
    if isinstance(x, list): return [q for i, v in enumerate(x) for q in todo_paths(v, f'{path}[{i}]')]
    return [path] if isinstance(x, str) and 'TODO' in x else []


def live_state(slug):
    """Ask the live site once (4 s timeout). 200 = the page is online; local changes may still wait for a deploy."""
    import urllib.request
    try:
        r = urllib.request.urlopen(urllib.request.Request(f'https://741.studio/review/{slug}/', method='HEAD', headers={'User-Agent': '741-validate'}), timeout=4)
        if r.status == 200: return f'LIVE (Prüfung {datetime.date.today().isoformat()}); neue lokale Änderungen brauchen ein Deploy nach Go.'
    except Exception:
        pass
    return 'Noch nicht live: Deploy nach Go.'


def main():
    pdir = sys.argv[1]
    p = json.load(open(os.path.join(pdir, sys.argv[2] if len(sys.argv) > 2 else 'prospect.json'), encoding='utf-8'))
    page = os.path.join(ROOT, '04_site', 'review', p['slug'], 'index.html')
    s = open(page, encoding='utf-8').read()
    body = s[s.index('<body'):]
    vis = re.sub(r'<style.*?</style>|<script.*?</script>|<svg.*?</svg>|<!--.*?-->', ' ', body, flags=re.S)
    vis = re.sub(r'<[^>]+>', ' ', vis)
    vis = re.sub(r'\{\{>[^}]*\}\}', ' ', vis)
    errs, warns = [], []
    for w in JARGON:
        if re.search(r'(?<![\w-])' + re.escape(w) + r'(?![\w-])', vis):
            errs.append(f'jargon: {w}')
    own = (p.get('company', '') + ' ' + p.get('display_name', '')).lower()
    branch = p.get('branch') or ''
    if not branch and os.path.exists(os.path.join(pdir, 'intake.json')):
        try:
            branch = json.load(open(os.path.join(pdir, 'intake.json'))).get('branch', '')
        except Exception:
            pass
    for w in FOREIGN:
        if branch == 'legal' and w in ('Kanzlei', 'Mandant'):
            continue
        if w in vis and w.lower() not in own:
            errs.append(f'foreign text: {w}')
    for src in set(re.findall(r'(?:src=|url\()"?(/review-assets/[^")\s]+)', s)):
        if not os.path.exists(os.path.join(ROOT, '04_site', 'public', src.lstrip('/'))):
            errs.append(f'missing image: {src}')
    if 'SLOT:' in s or '%%' in s.replace('%%"', ''):
        errs.append('unfilled slot or placeholder')
    if not p.get('sources'):
        errs.append('no sources block in prospect.json')
    todo = todo_paths(p)  # draft_prospect.py skeleton placeholders (2026-10-12)
    if todo:
        errs.append(f'TODO placeholder in {len(todo)} field(s): ' + ', '.join(todo[:8]) + (' ...' if len(todo) > 8 else ''))
    if re.search(ZERO_VOL, vis):
        errs.append('a "0" search volume is shown; write "Google gibt keine Zahl heraus"')
    for w in PROTECTED:
        if re.search(r'\b' + w + r'\b', vis) and w.lower() not in own:
            warns.append(f'protected title on the page: {w} (only if the prospect holds it)')
    for k, v in (p.get('guide') or {}).items():
        txt = v if isinstance(v, str) else ' '.join(str(x) for x in (v.values() if isinstance(v, dict) else v))
        txt = re.sub(r'<[^>]+>', ' ', txt)
        n = len([x for x in re.split(r'(?<=[.!?])\s+', txt.strip()) if x])
        if n > 2: errs.append(f'guide.{k}: {n} sentences (max 2)')
        if len(txt.split()) > 40: warns.append(f'guide.{k}: {len(txt.split())} words (aim for 30 or fewer)')
    sie = len(re.findall(r'\b(Sie|Ihre|Ihren|Ihrer)\b', re.sub('|'.join(SIE_OK), ' ', vis)))
    if sie:
        warns.append(f'"Sie"-forms in visible text: {sie} (header/footer partials are excluded; check draft quotes)')
    errs += hero_length(p)
    warns += calc_steps(p.get('calc') or {})
    warns += merged_variants(pdir, ((p.get('system') or {}).get('step1') or {}).get('demand'))
    if not p.get('loom_url'):
        warns.append('no loom_url: hero shows the video placeholder')
    print(json.dumps({'page': page, 'errors': errs, 'warnings': warns}, ensure_ascii=False, indent=1))
    run_path = os.path.join(pdir, '_run.json')
    old = {}
    if os.path.exists(run_path):
        try: old = json.load(open(run_path, encoding='utf-8'))
        except Exception: old = {}
    run = {'client': p.get('display_name') or p.get('company') or p['slug'], 'workflow': 'prospect',
           'status': old.get('status') if old.get('status') in ('fertig, Freigabe offen',) and not errs else ('fertig, Freigabe offen' if not errs else 'in Arbeit'),
           'mode': 'Echt', 'last_run': datetime.date.today().isoformat(),
           'local': os.path.relpath(os.path.abspath(pdir), ROOT), 'result': f"https://741.studio/review/{p['slug']}/",
           'drive': old.get('drive', ''),
           'note': (f"validate: {len(errs)} Fehler, {len(warns)} Hinweise" + ('' if p.get('loom_url') else ', Loom fehlt') + '. ' + live_state(p['slug']))}
    if len(sys.argv) <= 2:  # a variant file (e.g. prospect-headlines.json) must not overwrite the overview entry
        json.dump(run, open(run_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main()
