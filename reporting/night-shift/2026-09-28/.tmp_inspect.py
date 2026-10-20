import json
d = json.load(open('/Users/martindrendel/741website/reporting/night-shift/2026-09-28/context.json'))
print(list(d.keys()))
cid = 'fbcc70d1-4c56-437c-b5fb-8056e48d3f62'
for k in ['programs','tasks','feedback_open','nap_locked']:
    v = d.get(k)
    if isinstance(v, list):
        items = [x for x in v if x.get('client_id')==cid]
        print(k, len(v), 'matching', len(items))
        for it in items:
            print('  -', json.dumps(it, ensure_ascii=False)[:300])
