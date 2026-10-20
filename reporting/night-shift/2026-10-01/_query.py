import json
d = json.load(open('context.json'))
print(list(d.keys()))
for f in d.get('feedback_open', []):
    if f.get('id') == '61abce05-2b04-49b4-b4ab-420ab4374080':
        print("FEEDBACK:")
        print(json.dumps(f, indent=2, ensure_ascii=False))
for n in d.get('nap_locked', []):
    if n.get('client_id') == '3f71ef33-8c74-4ea1-b2d3-0273c2e99649':
        print("NAP:")
        print(json.dumps(n, indent=2, ensure_ascii=False))
