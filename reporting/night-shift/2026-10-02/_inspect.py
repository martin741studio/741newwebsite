import json
d = json.load(open('context.json'))
print(list(d.keys()))
for k in d:
    v = d[k]
    print(k, type(v), len(v) if hasattr(v, '__len__') else '')
