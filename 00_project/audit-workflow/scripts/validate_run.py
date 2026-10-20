"""Validate a run folder. Exit 1 on any failure. Usage: python3 validate_run.py <run_dir>"""
import json, os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
CAT = json.load(open(os.path.join(HERE, '..', 'catalog.json')))
run = sys.argv[1]; errs = []; warns = []
F = json.load(open(os.path.join(run, 'findings.json')))
man = json.load(open(os.path.join(run, 'manifest.json')))
ev = {e['id']: e for e in man['evidence']}
ids = {f['field_id'] for f in CAT['fields']}
seen = set()
for f in F:
    fid = f.get('field_id'); seen.add(fid)
    if fid not in ids: errs.append(f'{fid}: not in catalog'); continue
    if f.get('status') not in ('green', 'yellow', 'red', 'grey', 'unknown'): errs.append(f'{fid}: bad status {f.get("status")}')
    if f.get('confidence') not in ('verified', 'derived', 'client_stated'): errs.append(f'{fid}: confidence {f.get("confidence")!r} not allowed')
    for k in ('finding_de', 'source_tool', 'collected_at', 'client_safe'):
        if f.get(k) in (None, ''): errs.append(f'{fid}: missing {k}')
    if not re.match(r'\d{4}-\d\d-\d\d', str(f.get('collected_at', ''))): errs.append(f'{fid}: collected_at not ISO')
    st = f.get('status')
    if st not in ('unknown', 'grey') and f.get('confidence') == 'verified' and not f.get('evidence_ids'): errs.append(f'{fid}: verified without evidence_ids')
    for e in f.get('evidence_ids', []):
        if e not in ev: errs.append(f'{fid}: evidence {e} not in manifest')
    if st not in ('unknown', 'grey') and not (f.get('source_ref') or f.get('evidence_ids')): errs.append(f'{fid}: no source_ref and no evidence')
    if st == 'red' and not f.get('action_de') and fid.split('.')[0] not in ('B01', 'B02', 'B03', 'B08', 'B09'): warns.append(f'{fid}: red without action_de')
    if st == 'unknown' and not f.get('why_de') and not f.get('drilldown_hint'): warns.append(f'{fid}: unknown without reason')
for fid in ids - seen: errs.append(f'{fid}: no finding (use status unknown)')
for e in man['evidence']:
    p = os.path.join(run, e['file'])
    if e.get('kind') != 'drive_file' and not os.path.exists(p): errs.append(f"evidence {e['id']}: file missing {e['file']}")
print(f'findings {len(F)} / catalog {len(ids)}; evidence {len(ev)}; errors {len(errs)}; warnings {len(warns)}')
for x in errs: print('ERROR', x)
for x in warns[:20]: print('warn', x)
sys.exit(1 if errs else 0)
