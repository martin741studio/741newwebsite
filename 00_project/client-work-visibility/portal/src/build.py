#!/usr/bin/env python3
"""Adds or updates the "Kundenarbeit" module (client work view, step 1 = admin) in the portal index.html.
Usage: python3 build.py <fresh-live.html> <out.html>
Always run on a FRESH pull. Several chats patch this file with marker blocks:
  'Entscheidungen (Kunden-Freigabe)' (client-approval-workflow/portal/src/build.py),
  'Command Center (Morning Grill)' (morning-grill-portal/patch_portal.py),
  outreach accounts (portal-outreach-accounts/patch_portal.py).
This script only touches its own blocks between 'Kundenarbeit (Client work view)' and 'Ende Kundenarbeit', plus 6 small anchors.
Stops if an anchor is missing or ambiguous."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read()
css = open(os.path.join(HERE, 'kw.css'), encoding='utf-8').read()
js = open(os.path.join(HERE, 'kw.js'), encoding='utf-8').read()
CSS_START = '  /* ---------- Kundenarbeit (Client work view)'
CSS_END = '  /* ---------- Ende Kundenarbeit ---------- */\n'
JS_START = '/* ---------- Kundenarbeit (Client work view) · 2026-10-13 ----------\n'
JS_END = '/* ---------- Ende Kundenarbeit ---------- */\n'

def finish(h):
    for need in ['function kwRenderClient', 'id="workview"', "'workview'", 'kwAdminButton(b)', "adminSub === 'work'", 'loadWorkview()']:
        assert need in h, 'missing after build: ' + need
    assert h.count('function kwRenderClient') == 1, 'module twice'
    open(dst, 'w', encoding='utf-8').write(h)
    print('ok', dst, len(h) // 1024, 'KB')
    sys.exit(0)

def sub(old, new):
    global h
    n = h.count(old)
    if n != 1: sys.exit(f'STOP: anchor found {n}x: {old[:90]!r}')
    h = h.replace(old, new)

if 'function kwRenderClient' in h:   # update mode: swap own blocks only
    c0 = h.find(CSS_START); c1 = h.find(CSS_END, c0)
    assert c0 > 0 and c1 > 0, 'CSS block markers missing'
    h = h[:c0] + css + h[c1 + len(CSS_END):]
    j0 = h.find(JS_START); j1 = h.find(JS_END, j0)
    assert j0 > 0 and j1 > 0, 'JS block markers missing'
    h = h[:j0] + js + h[j1 + len(JS_END):]
    print('update mode: module swapped')
    finish(h)

sub('</head>', '<style>\n' + css + '</style>\n</head>')
sub("""onclick="window.open('/team/whiteboard.html','_blank')">→ Whiteboard</button></div>""",
    """onclick="window.open('/team/whiteboard.html','_blank')">→ Whiteboard</button>
      <button class="btn btn-small btn-yellow" style="margin-left:8px;" onclick="loadWorkview()">→ Kundenarbeit (Heute)</button></div>""")
sub('<div id="admin-client" class="container hidden"></div>', '<div id="admin-client" class="container hidden"></div>\n  <div id="workview" class="container hidden"></div>')
sub("'newsletter','grill'].forEach", "'newsletter','grill','workview'].forEach")
sub('      ${apAdminButton(b)}\n', '      ${apAdminButton(b)}\n      ${kwAdminButton(b)}\n')
sub("  if (isAdmin && adminSub === 'approvals') {", "  if (isAdmin && adminSub === 'work') {\n    $(target).innerHTML = adminHead + kwRenderClient(b);\n    return;\n  }\n  if (isAdmin && adminSub === 'approvals') {")
i = h.rfind('</script>')
h = h[:i] + js + '\n' + h[i:]
finish(h)
