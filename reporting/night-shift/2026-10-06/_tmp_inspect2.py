import json
d = json.load(open('/Users/martindrendel/741website/reporting/night-shift/2026-10-06/context.json'))
print(list(d.keys()))
fo = d.get('feedback_open', [])
print('feedback_open count', len(fo))
for f in fo:
    print('---')
    print(json.dumps(f, indent=2, ensure_ascii=False)[:1500])
