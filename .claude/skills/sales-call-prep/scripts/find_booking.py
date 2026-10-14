#!/usr/bin/env python3
"""sales-call-prep: resolve a prospect name to their booking folder, read only.

Usage: find_booking.py "<name as Martin said it>" [--slug <slug>]

Looks under 00_project/prospects/<slug>/booking/booking.json for a name match
(folded, umlaut-safe). Never writes anything — booking-sequence owns that folder.

Exactly one match: prints a JSON summary (slug, booking_json, review_url, call
times, which of baseline.md / claims.json / m1-m3.txt exist) so the skill body
knows what it can read.

0 or more than 1 match: prints the candidates and exits 2 (ask Martin with a
card — never guess which prospect).
"""
import argparse, glob, json, os, re, sys, unicodedata

ROOT = '/Users/martindrendel/741website'
PROS = os.path.join(ROOT, '00_project', 'prospects')


def fold(s):
    s = (s or '').lower()
    for x, y in (('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss')):
        s = s.replace(x, y)
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def jl(p):
    try:
        return json.load(open(p, encoding='utf-8'))
    except Exception:
        return {}


def candidates(name):
    toks = [t for t in fold(name).split() if len(t) > 2]
    hits = {}
    for bj in glob.glob(os.path.join(PROS, '*', 'booking', 'booking.json')):
        slug = bj.split(os.sep)[-3]
        data = jl(bj)
        hay = fold(data.get('name', '') + ' ' + slug.replace('-', ' '))
        score = sum(1 for t in toks if re.search(r'\b' + re.escape(t) + r'\b', hay))
        if score and (score >= 2 or len(toks) == 1):
            hits[slug] = score
    if not hits:
        return []
    best = max(hits.values())
    return sorted(s for s in hits if hits[s] == best)


def summarize(slug):
    bdir = os.path.join(PROS, slug, 'booking')
    bj = jl(os.path.join(bdir, 'booking.json'))
    exists = lambda f: os.path.isfile(os.path.join(bdir, f))
    return {
        'slug': slug,
        'booking_json': os.path.join(bdir, 'booking.json'),
        'review_url': bj.get('review_url', ''),
        'name': bj.get('name', ''),
        'call_times': bj.get('times', {}).get('call', {}),
        'has_baseline': exists('baseline.md'),
        'has_claims': exists('claims.json'),
        'has_m1': exists('m1.txt'),
        'has_m2': exists('m2.txt'),
        'has_m3': exists('m3.txt'),
        'thin_case': not exists('baseline.md'),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('name')
    ap.add_argument('--slug')
    a = ap.parse_args()

    if a.slug:
        if not os.path.isfile(os.path.join(PROS, a.slug, 'booking', 'booking.json')):
            print(json.dumps({'error': f'no booking.json for slug {a.slug}'}))
            sys.exit(2)
        print(json.dumps(summarize(a.slug), ensure_ascii=False, indent=1))
        return

    cands = candidates(a.name)
    if len(cands) == 1:
        print(json.dumps(summarize(cands[0]), ensure_ascii=False, indent=1))
        return
    print(json.dumps({'query': a.name, 'candidates': cands}, ensure_ascii=False, indent=1))
    sys.exit(2)


if __name__ == '__main__':
    main()
