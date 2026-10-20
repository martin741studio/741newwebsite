"""Build catalog.json (machine table) from spec section 6. Run after any spec edit."""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(HERE, '..', '..', 'audit-workflow-spec.md')
OUT = os.path.join(HERE, '..', 'catalog.json')
txt = open(SPEC, encoding='utf-8').read()
sec = txt.split('## 6. Field catalog')[1].split('## 7. Cost and caps')[0]
blocks = {}
cur = None
fields = []
for line in sec.splitlines():
    m = re.match(r'### (B\d\d) (.+?)(\(|$)', line)
    if m:
        cur = m.group(1); blocks[cur] = m.group(2).strip(); continue
    m = re.match(r'\| (B\d\d\.\d\d)( L)?( !)?( L)? \| (.+?) \| (.+?) \| (.+?) \| (.+?) \|$', line)
    if m and cur:
        fid, l1, crit, l2, label, typ, src, rule = m.groups()
        fields.append(dict(field_id=fid, block=cur, label_de=label.strip(), input_type=typ.strip(), source=src.strip(), rule=rule.strip(), light=bool(l1 or l2), critical=bool(crit)))
BLOCK_WEIGHTS_BY_STRATEGY = {
    'maps': {'B05': 25, 'B10': 15, 'B11': 15, 'B06': 15, 'B07': 10, 'B13': 10, 'B12': 5, 'B04': 5},
    'paid': {'B06': 30, 'B05': 20, 'B03': 10, 'B04': 10, 'B13': 10, 'B10': 5, 'B07': 5, 'B11': 5, 'B12': 5},
}
BLOCK_WEIGHTS = BLOCK_WEIGHTS_BY_STRATEGY['maps']
out = dict(catalog_version='2026-10-11.3', blocks=blocks, block_weights=BLOCK_WEIGHTS, block_weights_by_strategy=BLOCK_WEIGHTS_BY_STRATEGY, fields=fields)
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)
print(len(blocks), 'blocks', len(fields), 'fields ->', os.path.abspath(OUT))
