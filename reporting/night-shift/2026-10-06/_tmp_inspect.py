import json
d = json.load(open('reporting/night-shift/2026-10-06/context.json'))
print(list(d.keys()))
fo = d.get('feedback_open', [])
print(len(fo))
for item in fo:
    s = json.dumps(item, ensure_ascii=False)
    if '7fd15e89' in s:
        print(s)
nl = d.get('nap_locked', [])
print(len(nl))
for item in nl:
    s = json.dumps(item, ensure_ascii=False)
    if 'Suriya' in s or 'suriya' in s:
        print(s)
