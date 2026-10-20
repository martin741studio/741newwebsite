"""Derived analysis: which profile factors explain Maps visibility inside one Falcon report.
Input: evidence/falcon-report-<key>.json. Output: evidence/drivers.json. Free. Pure computation."""
import json, glob, os, statistics as st
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rank(xs):
    o = sorted(range(len(xs)), key=lambda i: xs[i]); r = [0]*len(xs); i = 0
    while i < len(o):
        j = i
        while j+1 < len(o) and xs[o[j+1]] == xs[o[i]]: j += 1
        for k in range(i, j+1): r[o[k]] = (i+j)/2+1
        i = j+1
    return r
def spearman(a, b):
    if len(a) < 5: return None
    ra, rb = rank(a), rank(b); ma, mb = st.mean(ra), st.mean(rb)
    num = sum((x-ma)*(y-mb) for x, y in zip(ra, rb))
    den = (sum((x-ma)**2 for x in ra)*sum((y-mb)**2 for y in rb))**0.5
    return round(num/den, 2) if den else None
KEYCATS = {'tax': ('tax attorney','tax_attorney','tax law attorney'), 'crim': ('criminal justice attorney','criminal_justice_attorney')}
def cats(p):
    c = p.get('categories') or {}
    return [str(v).lower() for v in (c.values() if isinstance(c, dict) else c)]
out = {}
BEST = {}   # place key -> highest review count seen in any report (Falcon shows 0 when it has no data)
for f in sorted(glob.glob(os.path.join(RUN, 'evidence', 'falcon-report-*.json'))):
    if f.endswith('index.json'): continue
    d0 = json.load(open(f)); d0 = d0.get('data', d0)
    pl0 = d0.get('places') or []
    pl0 = list(pl0.values()) if isinstance(pl0, dict) else pl0
    for p0 in pl0:
        k = p0.get('place_id') or p0.get('name')
        try: r0 = int(float(p0.get('reviews') or 0))
        except Exception: r0 = 0
        BEST[k] = max(BEST.get(k, 0), r0)
for f in sorted(glob.glob(os.path.join(RUN, 'evidence', 'falcon-report-*.json'))):
    if f.endswith('index.json'): continue
    d = json.load(open(f)); d = d.get('data', d)
    if d.get('platform') != 'google': continue
    pl = d.get('places') or []
    if isinstance(pl, dict): pl = list(pl.values())
    rows = []
    for p in pl:
        try: s = float(p.get('solv') or 0)
        except Exception: s = 0.0
        try: rv = int(float(p.get('reviews') or 0))
        except Exception: rv = 0
        rv = max(rv, BEST.get(p.get('place_id') or p.get('name'), 0))
        rows.append(dict(name=p.get('name'), solv=s, reviews=rv, cats=cats(p), url=p.get('url')))
    n = len(rows)
    if n < 8: out[d['report_key']] = dict(keyword=d['keyword'], date=d['date'], grid=d['grid_size'], radius=f"{d['radius']} {d.get('measurement')}", n=n, note='too few places'); continue
    rho_rev = spearman([r['reviews'] for r in rows], [r['solv'] for r in rows]) if sum(r['reviews'] > 0 for r in rows)/n >= 0.5 else None
    rho_ncat = spearman([len(r['cats']) for r in rows], [r['solv'] for r in rows])
    rev_cov = round(sum(r['reviews'] > 0 for r in rows)/n, 2)   # review data is incomplete in some reports
    srt = sorted(rows, key=lambda r: -r['solv']); top10 = [r for r in srt[:10] if r['solv'] > 0]
    from collections import Counter
    cnt = Counter(c for r in rows for c in set(r['cats']))
    grp = {}
    for c, k_n in cnt.items():
        if k_n < 5 or not top10: continue
        base = k_n/n; in_top = sum(c in r['cats'] for r in top10)/len(top10)
        grp[c] = dict(share_all=round(base, 2), share_top10=round(in_top, 2), lift=round(in_top/base, 2))
    drivers = sorted([c for c, v in grp.items() if v['lift'] >= 2.0 and v['share_top10'] >= 0.3], key=lambda c: -grp[c]['lift'])
    top = sorted(rows, key=lambda r: -r['solv'])[:5]
    sz = [r for r in rows if r['name'] and 'stürzl' in r['name'].lower() or r['name'] and 'sturzl' in r['name'].lower()]
    out[d['report_key']] = dict(keyword=d['keyword'], date=d['date'], grid=d['grid_size'], radius=f"{d['radius']} {d.get('measurement')}", n=n, review_data_coverage=rev_cov,
        spearman_reviews_vs_solv=rho_rev, spearman_catcount_vs_solv=rho_ncat, category_groups=grp, driver_categories=drivers,
        zero_review_with_solv_over_10=[r['name'] for r in rows if r['reviews'] == 0 and r['solv'] > 10][:8],
        top5=[dict(name=r['name'], solv=r['solv'], reviews=r['reviews'], cats=r['cats'][:4]) for r in top],
        client=[dict(name=r['name'], solv=r['solv'], reviews=r['reviews'], cats=r['cats']) for r in sz])
json.dump(out, open(os.path.join(RUN, 'evidence', 'drivers.json'), 'w'), ensure_ascii=False, indent=1)
for k, v in out.items():
    print(k, v['keyword'], v['date'], v['grid'], v['radius'], 'n=', v['n'])
    if 'note' in v: continue
    print('  review coverage', v['review_data_coverage'], ' rho reviews:', v['spearman_reviews_vs_solv'], ' drivers:', v['driver_categories'])
