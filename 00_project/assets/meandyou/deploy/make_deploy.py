"""Build the deploy bundle (deploy/meandyou) and the Figma capture copy from prototype-v2 and prototype-v3.

- HTML: "assets/ -> "../assets/, noindex meta, Lenis always on (no ?still gate).
- Assets: copy every file from prototype/assets that is new or changed; list them in new_assets.txt for the FTP upload.
- figma-capture/: same HTML plus the Figma capture script.
"""
import os, shutil, filecmp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'v2': os.path.join(ROOT, 'prototype-v2'), 'v3': os.path.join(ROOT, 'prototype-v3')}
ASSETS = os.path.join(ROOT, 'prototype', 'assets')
DEP = os.path.join(ROOT, 'deploy', 'meandyou')
FIG = os.path.join(ROOT, 'figma-capture')
NOINDEX = '<meta name="robots" content="noindex, nofollow">'
CAPTURE = '<script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>'

def convert(html):
    html = html.replace('"assets/', '"../assets/')
    html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + NOINDEX, 1)
    html = html.replace("location.search.indexOf('still') < 0", 'true')
    return html

pages = 0
for ver, src in SRC.items():
    for d in (os.path.join(DEP, ver), os.path.join(FIG, ver)):
        os.makedirs(d, exist_ok=True)
    for name in sorted(os.listdir(src)):
        if not name.endswith('.html') or name == 'page.html':
            continue
        html = convert(open(os.path.join(src, name), encoding='utf-8').read())
        open(os.path.join(DEP, ver, name), 'w', encoding='utf-8').write(html)
        open(os.path.join(FIG, ver, name), 'w', encoding='utf-8').write(html.replace('</body>', CAPTURE + '</body>'))
        pages += 1

new = []
dst_assets = os.path.join(DEP, 'assets')
os.makedirs(dst_assets, exist_ok=True)
for name in sorted(os.listdir(ASSETS)):
    s, d = os.path.join(ASSETS, name), os.path.join(dst_assets, name)
    if os.path.isfile(s) and (not os.path.exists(d) or not filecmp.cmp(s, d, shallow=False)):
        shutil.copy2(s, d); new.append(name)
open(os.path.join(ROOT, 'deploy', 'new_assets.txt'), 'w').write('\n'.join(new) + ('\n' if new else ''))
print('pages', pages, '| new assets', len(new), new)
