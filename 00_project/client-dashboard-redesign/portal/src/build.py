#!/usr/bin/env python3
"""Adds or updates the "Dashboard (neu)" module (client view, pilot Bali Healing) in the portal index.html.
Usage: python3 build.py <fresh-live.html> <out.html>
Always run on a FRESH pull. Several chats patch this file with marker blocks (Entscheidungen, Command Center, Kundenarbeit, outreach accounts).
This script only touches its own blocks between 'Dashboard (neu)' and 'Ende Dashboard (neu)', plus 4 small anchors.
Stops if an anchor is missing or ambiguous."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read()
css = open(os.path.join(HERE, 'dsh.css'), encoding='utf-8').read()
js = open(os.path.join(HERE, 'dsh.js'), encoding='utf-8').read()
FONT = '<link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">\n'
CSS_START = '/* ---------- Dashboard (neu) '
CSS_END = '/* ---------- Ende Dashboard (neu) ---------- */\n'
JS_START = '/* ---------- Dashboard (neu) '
JS_END = '/* ---------- Ende Dashboard (neu) ---------- */\n'

def finish(h):
    for need in ['function dshRenderClient', 'dshOn(b)', "adminSub === 'dash'", 'dshAdminButton(b)']:
        assert need in h, 'missing after build: ' + need
    assert h.count('function dshRenderClient') == 1, 'module twice'
    open(dst, 'w', encoding='utf-8').write(h)
    print('ok', dst, len(h) // 1024, 'KB')
    sys.exit(0)

def sub(old, new):
    global h
    n = h.count(old)
    if n != 1: sys.exit(f'STOP: anchor found {n}x: {old[:90]!r}')
    h = h.replace(old, new)

if 'function dshRenderClient' in h:   # update mode: swap own blocks only
    c0 = h.find(CSS_START); c1 = h.find(CSS_END, c0)
    assert c0 > 0 and c1 > 0, 'CSS block markers missing'
    h = h[:c0] + css + h[c1 + len(CSS_END):]
    # the JS block is the second occurrence of the start marker
    first = h.find(JS_START); second = h.find(JS_START, first + 10)
    assert second > 0, 'JS block start marker missing'
    j1 = h.find(JS_END, second); assert j1 > 0, 'JS block end marker missing'
    h = h[:second] + js + h[j1 + len(JS_END):]
    print('update mode: module swapped')
    finish(h)

sub('</head>', FONT + '<style>\n' + css + '</style>\n</head>')
sub("function renderClientTabs(b, target, onboardingDone) {\n", "function renderClientTabs(b, target, onboardingDone) {\n  if (dshOn(b)) { dshRenderClient(b, target); return; }\n")
sub('      ${apAdminButton(b)}\n', '      ${apAdminButton(b)}\n      ${dshAdminButton(b)}\n')
sub("  if (isAdmin && adminSub === 'work') {", "  if (isAdmin && adminSub === 'dash' && dshOn(b)) {\n    $(target).innerHTML = adminHead + dshAdminView(b);\n    return;\n  }\n  if (isAdmin && adminSub === 'work') {")
i = h.rfind('</script>')
h = h[:i] + js + '\n' + h[i:]
finish(h)
