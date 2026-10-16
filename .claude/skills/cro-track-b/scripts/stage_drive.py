#!/usr/bin/env python3
"""Stage the finished run for the Drive upload (workflow section 2.2): flat names, step number first, prototype zip, manifest.
Usage: stage_drive.py <cro-dir> [--proto 07-prototype] [--version v1]
Output: <cro-dir>/_drive/ with all files and MANIFEST.json. Upload that folder with the browser method (about 10 MB per call), then run check_drive.py."""
import sys, os, json, shutil, zipfile, glob
a = sys.argv[1:]
cro = a[0]; proto = '07-prototype'; ver = 'v1'
if '--proto' in a: proto = a[a.index('--proto')+1]
if '--version' in a: ver = a[a.index('--version')+1]
out = os.path.join(cro,'_drive'); shutil.rmtree(out, ignore_errors=True); os.makedirs(out)
def put(src, name):
    if os.path.exists(src): shutil.copy(src, os.path.join(out,name)); return name
    print('  missing source:', src); return None
names = []
for f in ['00-lead-info.md','_status.md']: names.append(put(os.path.join(cro,f), f))
names.append(put(os.path.join(cro,'01-input','INVENTORY.md'),'01-input-INVENTORY.md'))
for f in sorted(glob.glob(os.path.join(cro,'02-data','*.md'))): names.append(put(f,'02-data-'+os.path.basename(f)))
names.append(put(os.path.join(cro,'03-diagnosis','diagnosis.md'),'03-diagnosis.md'))
names.append(put(os.path.join(cro,'04-copy','approved-copy.md'),'04-copy-approved.md'))
names.append(put(os.path.join(cro,'05-gpt-design-doc','design-doc.md'),'05-gpt-design-doc.md'))
names.append(put(os.path.join(cro,'06-gpt-assets','images','SLOTS.md'),'06-gpt-assets-SLOTS.md'))
for f in sorted(glob.glob(os.path.join(cro,'06-gpt-assets','*.png'))): names.append(put(f,'06-gpt-assets-'+os.path.basename(f)))
for f in sorted(glob.glob(os.path.join(cro,'06-gpt-assets','images','*.png'))): names.append(put(f,'06-gpt-assets-'+os.path.basename(f)))
pd = os.path.join(cro,proto)
for f,n in [('self-check.md','self-check'),('visual-check.md','visual-check'),('motion.md','motion')]:
    names.append(put(os.path.join(pd,f),f'07-prototype-{n}.md'))
for f in sorted(glob.glob(os.path.join(pd,'screenshots','*.png'))):
    b = os.path.basename(f).replace('prototype-','')
    names.append(put(f,f'07-prototype-{ver}-screenshot-{b}'))
zn = f'07-prototype-{ver}.zip'
with zipfile.ZipFile(os.path.join(out,zn),'w',zipfile.ZIP_DEFLATED) as z:
    for root,_,files in os.walk(pd):
        if 'screenshots' in root.split(os.sep) or '/v' in root[len(pd):]: continue
        for fn in files:
            if fn in ('self-check.md','visual-check.md') or fn.startswith('.'): continue
            p = os.path.join(root,fn); z.write(p, os.path.relpath(p,pd))
names.append(zn)
names.append(put(os.path.join(cro,'08-handoff','handoff.md'),'08-handoff.md'))
names = [n for n in names if n]
man = {n: os.path.getsize(os.path.join(out,n)) for n in names}
json.dump(man, open(os.path.join(out,'MANIFEST.json'),'w'), indent=1)
tot = sum(man.values())
print(f'{len(man)} files, {tot/1e6:.1f} MB staged in {out}')
big = sorted(man.items(), key=lambda x:-x[1])[:3]; print('largest:', big)
print('Split the browser upload so each call stays under about 10 MB.')
