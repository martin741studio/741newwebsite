#!/usr/bin/env python3
"""Prospect mini workflow: find existing Local Falcon scan reports before a new scan (0 credits).

Usage: find_scan.py <name|place_id> [more terms...] [--place "<name>" [--proximity "<city>"]]
Pages listLocalFalconScanReports and prints each report whose name, address or place_id contains
all terms (case-insensitive) as one JSON line, then the total count.
--place also runs searchForLocalFalconBusinessLocation and prints the place_id(s).
NOTE: --place costs 2 Local Falcon credits per successful search (tool description). The scan list is free.
Reuses session()/call() from audit-workflow/scripts/lf_client.py (unchanged). The API key is never printed.
"""
import json, os, sys

LF = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'audit-workflow', 'scripts', 'lf_client.py')
lf = {}
exec(open(LF).read().split("if __name__")[0], lf)
MASK = 'report_key,date,keyword,grid_size,location.name,location.address,location.place_id'


def data(r):
    """JSON payload of a tools/call answer (result.content[0].text, maybe wrapped in "data")."""
    d = json.loads(r['result']['content'][0]['text'])
    return d.get('data', d) if isinstance(d, dict) else d


def reports(sid):
    """All scan reports, page by page; stops when there is no token or no new keys."""
    seen, out, tok = set(), [], None
    while True:
        a = {'fieldmask': MASK}
        if tok: a['nextToken'] = tok
        d = data(lf['call']('listLocalFalconScanReports', a, sid))
        rows = d.get('reports', []) if isinstance(d, dict) else d
        new = [x for x in rows if x.get('report_key') not in seen]
        seen.update(x.get('report_key') for x in new); out += new
        tok = d.get('next_token') if isinstance(d, dict) else None
        if not tok or not new: return out


def places(sid, term, proximity):
    a = {'term': term}
    if proximity: a['proximity'] = proximity
    d = data(lf['call']('searchForLocalFalconBusinessLocation', a, sid))
    rows = d.get('results', d.get('locations', [])) if isinstance(d, dict) else d
    if not rows and isinstance(d, dict): print(f"place search: 0 results (count {d.get('count')}, true_count {d.get('true_count')})", file=sys.stderr)
    return [{'place_id': x.get('place_id'), 'name': x.get('name'), 'address': x.get('address')} for x in rows]


def opt(args, flag):
    if flag not in args: return None
    i = args.index(flag); v = args[i + 1] if i + 1 < len(args) else ''
    del args[i:i + 2]; return v


def main():
    args = sys.argv[1:]
    place, prox = opt(args, '--place'), opt(args, '--proximity')
    terms = [t.lower() for t in args]
    sid = lf['session']()
    if place is not None:
        for x in places(sid, place or ' '.join(args), prox): print(json.dumps({'place': x}, ensure_ascii=False))
    if not terms: return
    n = 0
    for r in reports(sid):
        loc = r.get('location') or {}
        hay = ' '.join(str(loc.get(k, '')) for k in ('name', 'address', 'place_id')).lower()
        if all(t in hay for t in terms):
            n += 1
            print(json.dumps({'report_key': r.get('report_key'), 'date': r.get('date'), 'keyword': r.get('keyword'),
                              'grid_size': r.get('grid_size'), 'name': loc.get('name')}, ensure_ascii=False))
    print(f'total: {n}')


if __name__ == '__main__':
    main()
