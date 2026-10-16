"""Phase 1 (free): read Local Falcon report indexes and the latest Google report per keyword for one or more place ids. Reads only, 0 credits.
Usage: python3 collect_falcon.py <run_dir> <placeId[,placeId]> [label]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lf_client import session, call
run, places = sys.argv[1], sys.argv[2].split(',')
label = sys.argv[3] if len(sys.argv) > 3 else 'places'
EV = os.path.join(run, 'evidence'); os.makedirs(EV, exist_ok=True)
sid = session()
def t(name, args):
    r = call(name, args, sid)
    try: return json.loads(r['result']['content'][0]['text'])
    except Exception: return r
def save(fn, obj): json.dump(obj, open(os.path.join(EV, fn), 'w'), ensure_ascii=False, indent=1)
acct = t('viewLocalFalconAccountInformation', {})
save('falcon-account-' + label + '.json', dict(credits=acct['data']['credits'], package=acct['data']['package']['name']))
print('credits', acct['data']['credits'])
fm = "reports.*.report_key,reports.*.date,reports.*.keyword,reports.*.arp,reports.*.solv,reports.*.grid_size,reports.*.radius,reports.*.platform,reports.*.measurement,reports.*.place_id"
index = {}
for pid in places:
    tok, n = None, 0
    while True:
        a = {"placeId": pid, "fieldmask": fm}
        if tok: a["nextToken"] = tok
        d = t('listLocalFalconScanReports', a)
        for r in d.get('reports', []): index[r['report_key']] = dict(r, place_id=pid)
        tok = d.get('next_token') or d.get('nextToken'); n += 1
        if not tok or not d.get('reports') or n > 12: break
import datetime
def _d(r):
    try: return datetime.datetime.strptime(r['date'].strip(), '%m/%d/%Y %I:%M %p')
    except Exception: return datetime.datetime.min
rows = sorted(index.values(), key=_d, reverse=True)   # real date order, not string order
save('falcon-report-index-' + label + '.json', rows)
print('unique reports:', len(rows))
# latest google report per (place, keyword, grid, radius, measurement)
latest = {}
for r in rows:
    if r.get('platform') != 'google': continue
    k = (r['place_id'], r['keyword'], r['grid_size'], r['radius'], r['measurement'])
    if k not in latest: latest[k] = r
fields = "report_key,date,keyword,arp,atrp,solv,found_in,grid_size,radius,measurement,platform,lat,lng,unique_competitors,places.*.name,places.*.place_id,places.*.solv,places.*.arp,places.*.rating,places.*.reviews,places.*.url,places.*.categories"
saved = 0
for k, r in latest.items():
    p = os.path.join(EV, f"falcon-report-{r['report_key']}.json")
    if os.path.exists(p): continue
    save(f"falcon-report-{r['report_key']}.json", t('getLocalFalconReport', {"reportKey": r['report_key'], "fieldmask": fields})); saved += 1
print('google reports saved:', saved, 'of', len(latest))
# reviews analysis reports (free reads), if any
ra = t('listLocalFalconReviewsAnalysisReports', {"placeId": ','.join(places), "limit": 10})
save('falcon-reviews-analysis-index-' + label + '.json', ra)
print('reviews analysis:', json.dumps(ra)[:300])
