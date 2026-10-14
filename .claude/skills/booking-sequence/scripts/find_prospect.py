#!/usr/bin/env python3
"""Booking sequence: find the prospect's review page and write the baseline (what the prospect already saw).

Usage: find_prospect.py "<name as in the booking>" [--email x@y.de] [--phone +49...] [--slug <slug>]

Searches 04_site/review/<slug>/ and 00_project/prospects/<slug>/ by name tokens, email and phone.
Exactly one match (or --slug): writes 00_project/prospects/<slug>/booking/baseline.md and prints a JSON summary
(slug, review_url, website, branch, health, city, first_name, data files). 0 or >1 matches: prints the
candidates and exits 2 (ask Martin with a card).
Read only except the booking/ folder. Standard library only.
"""
import argparse, glob, html, json, os, re, sys, unicodedata

ROOT = '/Users/martindrendel/741website'
REVIEW, PROS = os.path.join(ROOT, '04_site', 'review'), os.path.join(ROOT, '00_project', 'prospects')
HEALTH = re.compile(r'heilprakt|therap|physio|psycho|praxis|arzt|ärzt|zahn|osteo|naturheil|hypno|ayurved|massage|heb(amme)?|klinik|gesundheit|health|coach.*gesund', re.I)


def fold(s):
    s = (s or '').lower()
    for x, y in (('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss')): s = s.replace(x, y)
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def page_text(p):
    s = open(p, encoding='utf-8', errors='ignore').read()
    s = re.sub(r'<(script|style|noscript)\b.*?</\1>', ' ', s, flags=re.S | re.I)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip(), s


def jl(p):
    try: return json.load(open(p, encoding='utf-8'))
    except Exception: return {}


def candidates(name, email, phone):
    toks = [t for t in fold(name).split() if len(t) > 2]
    slugs = set(os.listdir(REVIEW)) | set(d for d in os.listdir(PROS) if os.path.isdir(os.path.join(PROS, d)))
    score = {}
    for s in slugs:
        if s.startswith(('_', '.')): continue
        st = s.replace('-', ' ')
        hit = sum(1 for t in toks if re.search(r'\b' + re.escape(t) + r'\b', st))
        if hit and (hit >= 2 or len(toks) == 1): score[s] = hit * 10
    needles = [n for n in (email, (phone or '').replace(' ', '')[-8:]) if n and len(n) > 5]
    if needles:
        for f in glob.glob(os.path.join(PROS, '*', 'intake.*')) + glob.glob(os.path.join(PROS, '*', 'evidence', 'chat-*.md')):
            t = open(f, encoding='utf-8', errors='ignore').read()
            if any(n in t for n in needles):
                s = f.split(os.sep)[len(PROS.split(os.sep))]; score[s] = score.get(s, 0) + 50
    if score:
        # prefer the newest version (-v2) of the same person when both exist
        best = max(score.values()); top = [s for s in score if score[s] == best]
        return sorted(top, key=lambda s: (os.path.exists(os.path.join(REVIEW, s, 'index.html')), s), reverse=True), score
    return [], score


def main():
    a = argparse.ArgumentParser(); a.add_argument('name'); a.add_argument('--email'); a.add_argument('--phone'); a.add_argument('--slug')
    o = a.parse_args()
    if o.slug: top, score = [o.slug], {o.slug: 100}
    else: top, score = candidates(o.name, o.email, o.phone)
    live = [s for s in top if os.path.exists(os.path.join(REVIEW, s, 'index.html'))]
    if not o.slug and len(live) > 1:
        # several versions of one person: newest page file wins only if the slugs share the base name
        bases = {re.sub(r'-v\d+.*$', '', s) for s in live}
        if len(bases) == 1: live = [max(live, key=lambda s: os.path.getmtime(os.path.join(REVIEW, s, 'index.html')))]
    pick = live if live else top
    if len(pick) != 1:
        print(json.dumps({'status': 'ASK MARTIN', 'reason': 'no match' if not pick else 'several matches',
                          'candidates': {s: score.get(s) for s in sorted(score, key=score.get, reverse=True)[:8]}}, ensure_ascii=False, indent=1))
        sys.exit(2)
    slug = pick[0]; pdir = os.path.join(PROS, slug); os.makedirs(os.path.join(pdir, 'booking'), exist_ok=True)
    pj, ij = jl(os.path.join(pdir, 'prospect.json')), jl(os.path.join(pdir, 'intake.json'))
    page = os.path.join(REVIEW, slug, 'index.html'); text, raw = page_text(page) if os.path.exists(page) else ('', '')
    website = pj.get('website') or ij.get('website') or ''
    if not website and raw:
        ext = [u for u in re.findall(r'https?://[A-Za-z0-9.-]+\.[a-z]{2,}[A-Za-z0-9/._~%?=&#-]*', raw) if not re.search(r'741\.studio|google|loom|youtube|calendly|cal\.com|gstatic|fonts|cdn|wa\.me|linkedin|schema\.org|w3\.org', u)]
        website = ext[0] if ext else ''
    branch = ij.get('branch') or ''
    title = re.search(r'<title>(.*?)</title>', raw, re.S | re.I)
    blob = ' '.join([pj.get('company', ''), ij.get('business', ''), title.group(1) if title else ''])
    hm = HEALTH.search(blob)
    files = [f for f in ('prospect.json', 'intake.json', 'demand.md', 'site-findings.md', 'homepage.md', 'competitors.md',
                         'scan-search.md', 'evidence/site.json', 'evidence/loom-transcript.md', 'evidence/dfs-volumes-ads.json')
             if os.path.exists(os.path.join(pdir, f))]
    info = {'status': 'OK', 'slug': slug, 'review_url': f'https://741.studio/review/{slug}/' if text else '',
            'page_date': __import__('datetime').date.fromtimestamp(os.path.getmtime(page)).isoformat() if text else '',
            'website': website, 'first_name': pj.get('first_name') or ij.get('first_name') or o.name.split()[0],
            'company': pj.get('company') or ij.get('business') or '', 'city': ij.get('city') or '',
            'country': ij.get('country') or '', 'branch': branch, 'health': branch == 'health' if branch else bool(hm),
            'health_reason': f'branch={branch}' if branch else (f'guess from title/company: "{hm.group(0)}"' if hm else 'no health word in title/company'),
            'data_files': files, 'version': 'v2.1 (prospect.json)' if pj else 'old page (text only)'}
    with open(os.path.join(pdir, 'booking', 'baseline.md'), 'w', encoding='utf-8') as f:
        f.write(f"# Baseline: what {info['first_name']} already saw ({info['review_url'] or 'no review page'}, page file {info['page_date']})\n\n")
        f.write('```json\n' + json.dumps(info, ensure_ascii=False, indent=1) + '\n```\n\n')
        for fn in ('demand.md', 'site-findings.md', 'homepage.md'):
            p = os.path.join(pdir, fn)
            if os.path.exists(p): f.write(f'## {fn} (first 60 lines)\n\n' + ''.join(open(p, encoding='utf-8').readlines()[:60]) + '\n\n')
        f.write('## Visible review-page text\n\n' + (text[:60000] or '(no page)') + '\n')
    print(json.dumps(info, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
