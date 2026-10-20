"""Phase 1: free Local Falcon reads for the Stürzl kickoff run. Reads only. Costs 0 credits."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lf_client import session, call
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EV = os.path.join(RUN, 'evidence'); os.makedirs(EV, exist_ok=True)
PLACE = 'ChIJyVGAdikEaW8RUOWpEJs-2XA'
sid = session()
def t(name, args):
    r = call(name, args, sid)
    try: return json.loads(r['result']['content'][0]['text'])
    except Exception: return r
def save(fn, obj):
    p = os.path.join(EV, fn); open(p, 'w').write(json.dumps(obj, ensure_ascii=False, indent=1)); return p
fm = "reports.*.report_key,reports.*.date,reports.*.keyword,reports.*.arp,reports.*.solv,reports.*.grid_size,reports.*.radius,reports.*.platform,reports.*.measurement"
allr, tok = [], None
for _ in range(6):
    a = {"placeId": PLACE, "fieldmask": fm}
    if tok: a["next_token"] = tok
    d = t('listLocalFalconScanReports', a)
    allr += d.get('reports', [])
    tok = d.get('next_token')
    if not tok or not d.get('reports'): break
save('falcon-report-index.json', allr)
print('reports listed:', len(allr))
fields = "report_key,date,keyword,arp,atrp,solv,found_in,grid_size,radius,measurement,platform,lat,lng,unique_competitors,places.*.name,places.*.place_id,places.*.solv,places.*.arp,places.*.rating,places.*.reviews,places.*.url,places.*.categories,places.*.claimed"
got = 0
for r in allr:
    if r.get('platform') != 'google': continue
    d = t('getLocalFalconReport', {"reportKey": r['report_key'], "fieldmask": fields})
    save(f"falcon-report-{r['report_key']}.json", d); got += 1
print('google reports saved:', got)
for k in ['eb2f136efd0fe1e','004b590aed4b96c','6b59ef96d3bcf75','60605f4fb872bea','e5f5803382f47ee','cd13432c3276856','07d0917bde1b164','c4e888e0b4b1829','684d4e2f03135a5']:
    if os.path.exists(os.path.join(EV, f'falcon-report-{k}.json')): continue
    d = t('getLocalFalconReport', {"reportKey": k, "fieldmask": fields})
    save(f"falcon-report-{k}.json", d)
print('baseline reports saved')
