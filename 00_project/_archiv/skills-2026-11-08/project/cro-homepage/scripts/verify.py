#!/usr/bin/env python3
"""One verification command for a CRO run (workflow Step 6b/7). The agent runs it, fixes every FAIL, runs it again.
Usage: verify.py <cro-dir> [--proto 07-prototype] [--allow "text part" ...]
Checks: required files per step, text equals approved copy (M11), [FEHLT] list, '#' placeholders, method-source names, visual-check line, self-check total.
It does NOT replace the visual check in Chrome. It only covers what a script can measure."""
import sys, os, re, subprocess, glob
a = sys.argv[1:]; cro = a[0]; proto = '07-prototype'
if '--proto' in a: proto = a[a.index('--proto')+1]
allow = []
b = list(a)
while '--allow' in b:
    i = b.index('--allow'); allow += ['--allow', b[i+1]]; del b[i:i+2]
here = os.path.dirname(os.path.abspath(__file__))
res = []
def ok(c, name, info=''): res.append(('PASS' if c else 'FAIL', name, info))
def note(name, info=''): res.append(('INFO', name, info))
def rd(p): return open(os.path.join(cro,p),encoding='utf-8').read() if os.path.exists(os.path.join(cro,p)) else ''
req = ['00-lead-info.md','_status.md','01-input/INVENTORY.md','02-data/dataset.md','02-data/brand.md','03-diagnosis/diagnosis.md','04-copy/approved-copy.md','05-gpt-design-doc/design-doc.md','06-gpt-assets/images/SLOTS.md',proto+'/index.html',proto+'/self-check.md',proto+'/visual-check.md','08-handoff/handoff.md']
for f in req: ok(os.path.exists(os.path.join(cro,f)), 'file '+f)
ok(bool(glob.glob(os.path.join(cro,'06-gpt-assets','full-page*.png'))), 'final mockup full-page*.png')
ok(bool(glob.glob(os.path.join(cro,proto,'screenshots','*.png'))), 'prototype screenshots')
# Content-writing gates (from 2026-10-12 strict, older runs get an INFO line)
gt = rd('04-copy/gates.md'); st0 = rd('_status.md'); dm = re.search(r'(20\d\d-\d\d-\d\d)', st0)
strict = bool(dm and dm.group(1) >= '2026-10-12')
if gt:
    ok('Result: **PASS**' in gt, '04-copy/gates.md shows Result PASS (content-writing gates G1 to G6)')
elif strict:
    ok(False, '04-copy/gates.md missing (content-writing gates, required for runs started on or after 2026-10-12)')
else:
    note('no 04-copy/gates.md (legacy run before 2026-10-12)')
# M11
idx = os.path.join(cro,proto,'index.html'); cp = os.path.join(cro,'04-copy','approved-copy.md')
if os.path.exists(idx) and os.path.exists(cp):
    r = subprocess.run([sys.executable, os.path.join(here,'check_text.py'), idx, cp]+allow, capture_output=True, text=True)
    ok(r.returncode==0, 'M11 text equals approved copy', r.stdout.strip().replace('\n',' | ')[:300])
# placeholders
if os.path.exists(idx):
    h = open(idx,encoding='utf-8').read()
    note("links with '#' placeholder", str(len(re.findall(r'href="#"',h)))+' (each must be listed as open in visual-check.md)')
    ok('noindex' in h, 'robots noindex while preview')
    ok('application/ld+json' in h, 'JSON-LD present')
    note('image distortion (M4b) and the rendered look need the Chrome check, a script cannot see them')
# visual check line
vc = rd(proto+'/visual-check.md')
ok(bool(re.search(r'Visual check done in Chrome, \d+ items checked, \d+ fixed, \d+ open', vc)), 'visual-check.md has the report line')
sc = rd(proto+'/self-check.md')
ok(bool(re.search(r'\d+ von \d+', sc)), 'self-check.md has a total')
ho = rd('08-handoff/handoff.md')
ok('[FEHLT]' in ho or 'FEHLT' in ho, 'handoff lists the [FEHLT] items')
# method sources in client-facing files
bad = ['hormozi','backlinko','gotch','diggity','brian dean']
hit = []
for f in ['04-copy/approved-copy.md','08-handoff/handoff.md',proto+'/index.html']:
    t = rd(f).lower()
    hit += [f'{f}:{w}' for w in bad if w in t]
ok(not hit, 'no method-source names in client-facing files', ', '.join(hit))
# FEHLT inventory
fe = set()
for f in glob.glob(os.path.join(cro,'**','*.md'),recursive=True)+[idx]:
    if os.sep+'_drive' in f or os.sep+'_build' in f: continue
    try: fe |= set(re.findall(r'\[FEHLT[^\]]*\]', open(f,encoding='utf-8').read()))
    except Exception: pass
fails = [r for r in res if r[0]=='FAIL']
res_pass = [r for r in res if r[0]=='PASS']
for r in res: print(f'{r[0]}  {r[1]}' + (f'  -> {r[2]}' if r[2] else ''))
print(f'\n{len(res_pass)} pass, {len(fails)} fail. Distinct [FEHLT] tags: {len(fe)}')
sys.exit(1 if fails else 0)
