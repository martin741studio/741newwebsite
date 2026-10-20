import json
d = json.load(open('context.json'))
fb = d['feedback_open']
print(len(fb), 'feedback items')
fb_sorted = sorted(fb, key=lambda x: x['created_at'])
for i,f in enumerate(fb_sorted):
    print(i, f['created_at'], f['client_id'][:8], f['report_slug'], '|', f['section_key'][:40], '|', f['id'][:8])
