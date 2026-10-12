import re, json
s = open('../04-copy/approved-copy.md', encoding='utf-8').read()
s = s.split('<!-- TECH -->')[0]
U = {}
for m in re.finditer(r'<!-- (S\d\d) [^>]*-->(.*?)<!-- /\1 -->', s, re.S):
    sid, body = m.group(1), m.group(2)
    body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
    units = []
    for ln in body.split('\n'):
        ln = ln.strip()
        if not ln or re.match(r'^\|[-| ]+\|$', ln): continue
        if ln.startswith('|'):
            cells = [c.strip() for c in ln.strip('|').split('|')]
            units.append(' | '.join(c if c else '·' for c in cells)); continue
        ln = re.sub(r'^#+\s*', '', ln); ln = re.sub(r'^[-*]\s+', '', ln); ln = re.sub(r'^\d+\.\s+', '', ln)
        ln = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', ln).replace('**', '')
        units.append(ln)
    U[sid] = units
json.dump(U, open('units.json', 'w'), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in U.items()})
