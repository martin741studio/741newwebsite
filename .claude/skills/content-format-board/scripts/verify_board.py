#!/usr/bin/env python3
"""Verify a client-facing content board before it is shown to Martin.

Usage: verify_board.py <board.md> [--lang en|de] [--no-slop]

Checks (exit 1 on any failure):
  1. all 7 required sections present
  2. no banned internal term (label_map.py scan)
  3. at least 4 idea blocks, each with all 8 fields; at least one Why-We-Do-It idea
  4. no promise language (guarantee / will go viral / garantiert ...)
  5. no leftover template placeholders (<...>) except OPEN QUESTION markers
  6. readiness and on-camera sections either answered or marked OPEN QUESTION
  7. slop lint at 5/5 (deslop.py for en, deslop_de.py for de) unless --no-slop
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = '/Users/martindrendel/741website'
SECTIONS = {
    'en': ['## 1. What we found', '## 2. Production readiness check', '## 3. Who is on camera',
           '## 4. Real questions your customers ask', '## 5. Format ideas', '## 6. How to run it', '## 7. Next step'],
    'de': ['## 1. Was wir gefunden haben', '## 2. Produktions-Check', '## 3. Wer vor der Kamera steht',
           '## 4. Echte Fragen Ihrer Kunden', '## 5. Format-Ideen', '## 6. So läuft es', '## 7. Nächster Schritt'],
}
FIELDS = {
    'en': ['**Idea:**', '**Opening line', '**Opening image:**', '**Second sentence', '**How to shoot:**',
           '**Length:**', '**Ending:**', '**Quality bar:**'],
    'de': ['**Idee:**', '**Erste Zeile', '**Erstes Bild:**', '**Zweiter Satz', '**So drehen:**',
           '**Länge:**', '**Ende:**', '**Qualitätslatte:**'],
}
WHY = {'en': 'Why-We-Do-It', 'de': 'Warum-wir-es-so-machen'}
PROMISES = ['guarantee', 'guaranteed', 'will go viral', 'will get you', 'will bring you', 'million views',
            'garantiert', 'wird viral', 'bringt ihnen', 'werden sie bekommen']


def fail(msgs, m):
    msgs.append('FAIL ' + m)


def main(argv):
    if not argv:
        sys.exit(__doc__)
    path = argv[0]
    lang = argv[argv.index('--lang') + 1] if '--lang' in argv else 'en'
    text = open(path, encoding='utf-8').read()
    low = text.lower()
    msgs = []

    for s in SECTIONS[lang]:
        if s not in text:
            fail(msgs, f'missing section "{s}"')

    r = subprocess.run([sys.executable, os.path.join(HERE, 'label_map.py'), 'scan', path],
                       capture_output=True, text=True)
    if r.returncode != 0:
        for line in r.stdout.strip().splitlines():
            fail(msgs, line)

    ideas = re.split(r'\n### ', text)[1:]
    if len(ideas) < 4:
        fail(msgs, f'only {len(ideas)} idea blocks, need at least 4')
    for i, block in enumerate(ideas, 1):
        for f in FIELDS[lang]:
            if f not in block:
                fail(msgs, f'idea {i} missing field {f}')
    if not any(WHY[lang].lower() in b.lower() for b in ideas):
        fail(msgs, f'no {WHY[lang]} idea — the public-questions format is mandatory')

    for p in PROMISES:
        if p in low:
            fail(msgs, f'promise language: "{p}"')

    for m in re.finditer(r'<[^>\n]{3,}>', text):
        if 'OPEN QUESTION' not in m.group(0) and 'OFFENE FRAGE' not in m.group(0):
            fail(msgs, f'template placeholder left: {m.group(0)[:50]}')

    for sec in (SECTIONS[lang][1], SECTIONS[lang][2]):
        part = text.split(sec, 1)[1].split('\n## ', 1)[0] if sec in text else ''
        if not part.strip():
            fail(msgs, f'{sec} is empty — answer it or mark OPEN QUESTION')

    long = []
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith(('#', '|', '-', '*')) or not line.strip():
            continue
        for sent in re.split(r'(?<=[.!?])\s+', line):
            if len(sent.split()) > 20:
                long.append(n)
                break
    if long:
        msgs.append(f'WARN STE: sentences over 20 words on lines {long[:8]} — shorten them')
    if '—' in text or '–' in re.sub(r'\d[–-]\d', '', text):
        msgs.append('WARN dashes: em/en dashes found — use commas or full stops (the slop lint flags them)')

    if '--no-slop' not in argv:
        if lang == 'de':
            cmd = [sys.executable, os.path.join(ROOT, '00_project/content-writing-skill/scripts/deslop_de.py'), path]
        else:
            cmd = [sys.executable, os.path.join(ROOT, '.claude/skills/slopmonster/tools/deslop.py'), '--text', text]
        r = subprocess.run(cmd, capture_output=True, text=True)
        out = (r.stdout + r.stderr).strip()
        tail = '\n'.join(out.splitlines()[-6:])
        if '5/5' not in out:
            fail(msgs, 'slop lint below 5/5:\n' + tail)
        else:
            msgs.append('OK slop lint 5/5')

    for m in msgs:
        print(m)
    bad = [m for m in msgs if m.startswith('FAIL')]
    print(f'{"BOARD PASSED" if not bad else "BOARD BLOCKED"} · {path} · {len(ideas)} ideas · {len(bad)} failures')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
