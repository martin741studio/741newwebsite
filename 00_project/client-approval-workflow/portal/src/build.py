#!/usr/bin/env python3
"""Baut die Portal-Datei mit dem Tab "Entscheidungen".
Usage: python3 build.py <frische-live.html> <out.html>
Die Live-Datei IMMER frisch holen (curl), nie eine alte Kopie. Danach: node --check, Upload nur nach /staging/.
Martin-Figuren werden danach mit 00_project/assets/brand/martin-guide/inline.py eingebettet (macht dieses Skript selbst)."""
import sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
INLINE = os.path.join(HERE, '..', '..', '..', 'assets', 'brand', 'martin-guide', 'inline.py')
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read()
if 'apRenderClient' in h:
    sys.exit('Datei enthält den Tab schon (apRenderClient) – nichts zu tun')
css = open(os.path.join(HERE, 'ap.css'), encoding='utf-8').read()
js = open(os.path.join(HERE, 'ap.js'), encoding='utf-8').read()

def sub(old, new, count=1):
    global h
    n = h.count(old)
    if n != count:
        sys.exit(f'Anker {n}x statt {count}x gefunden: {old[:80]!r}')
    h = h.replace(old, new)

# 1. CSS (Martin-guide-Link wird von inline.py durch <style> ersetzt)
sub('</style>\n</head>', css + '</style>\n<link rel="stylesheet" href="martin-guide/martin-guide.css">\n</head>')
# 2. Daten laden
sub("  bundle = await fetchClientBundle(clientId);\n",
    "  bundle = await fetchClientBundle(clientId);\n  await apLoad(bundle, clientId);\n")
# 3. Kunden-Tab + Deep-Link ?view=decisions
sub("  if (currentView === null) currentView = (mode === 'reports') ? 'reports' : 'overview';\n",
    "  if (currentView === null) currentView = (new URLSearchParams(location.search).get('view') === 'decisions' && apOn(b)) ? 'decisions' : (mode === 'reports') ? 'reports' : 'overview';\n")
sub("    ${tab('overview', C.overview)}\n",
    "    ${tab('overview', C.overview)}\n    ${apOn(b) ? tab('decisions', 'Entscheidungen' + (apOpenCount(b) ? ' <span class=\"pill pill-yellow\" style=\"margin-left:4px;\">' + apOpenCount(b) + '</span>' : '')) : ''}\n")
sub("  let body;\n  if (currentView === 'citations') {",
    "  let body;\n  if (currentView === 'decisions' && apOn(b)) {\n    body = apRenderClient(b, false);\n  } else if (currentView === 'citations') {")
# 4. Admin: Knopf im Kundenkopf + Unteransicht
sub("      <button class=\"btn btn-small btn-ghost\" onclick=\"promptActivity()\">+ Feed-Eintrag</button>\n    </div>` : '';",
    "      <button class=\"btn btn-small btn-ghost\" onclick=\"promptActivity()\">+ Feed-Eintrag</button>\n      ${apAdminButton(b)}\n    </div>` : '';")
sub("  if (isAdmin && adminSub === 'leads' && ldOn(b)) {",
    "  if (isAdmin && adminSub === 'approvals') {\n    $(target).innerHTML = adminHead + apRenderAdmin(b);\n    return;\n  }\n  if (isAdmin && adminSub === 'leads' && ldOn(b)) {")
# 5. JS-Modul vor dem Ende des Haupt-Skripts
i = h.rfind('</script>')
h = h[:i] + js + '\n' + h[i:]

tmp = dst + '.tmp.html'
open(tmp, 'w', encoding='utf-8').write(h)
subprocess.run(['python3', INLINE, tmp, dst], check=True)
os.remove(tmp)
out = open(dst, encoding='utf-8').read()
assert 'martin-guide/martin-' not in out, 'Pose nicht eingebettet'
assert 'martin-guide.css' not in out, 'CSS nicht eingebettet'
print('ok', dst, len(out) // 1024, 'KB')
