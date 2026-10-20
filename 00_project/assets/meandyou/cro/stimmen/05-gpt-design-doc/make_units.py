"""Units per section from 04-copy/approved-copy.md (visible text only, markdown removed). Writes units.json and ../04-copy/approved-copy-plain.txt."""
import json, re, os
H = os.path.dirname(os.path.abspath(__file__))
raw = open(os.path.join(H, '..', '04-copy', 'approved-copy.md'), encoding='utf-8').read().split('<!-- TECH -->')[0]
U = {}
for sid, body in re.findall(r'<!--\s*(S\d\d)\b[^>]*-->(.*?)<!--\s*/\1\s*-->', raw, flags=re.S):
    body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
    out = []
    for line in body.splitlines():
        s = line.strip()
        if not s:
            continue
        s = re.sub(r'^#+\s*', '', s)
        s = re.sub(r'^[-*]\s+', '', s)
        s = re.sub(r'^\d+\.\s+', '', s)
        s = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', s)
        s = s.replace('**', '')
        out.append(s)
    U[sid] = out
json.dump(U, open(os.path.join(H, 'units.json'), 'w'), ensure_ascii=False, indent=1)
open(os.path.join(H, '..', '04-copy', 'approved-copy-plain.txt'), 'w').write('\n'.join(l for v in U.values() for l in v) + '\n')
print({k: len(v) for k, v in U.items()})
