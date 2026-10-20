#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sprechzettel-Generator fuer 90-Sekunden-Videos.

Liest eine Review-Page und erzeugt einen kurzen Sprechzettel:
Anrede, EIN staerkster Fund mit Zahl, Ueberleitung zur Seite.

Nutzung:
    python3 scripts/sprechzettel.py joshua-alsen
    python3 scripts/sprechzettel.py --alle
"""
import re, json, sys, os, html, glob

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
REVIEW = os.path.join(ROOT, '04_site', 'review')


def clean(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return ' '.join(html.unescape(s).split())


def load(slug):
    p = os.path.join(REVIEW, slug, 'index.html')
    if not os.path.exists(p):
        return None
    return open(p, encoding='utf-8').read()


def parse_local(t):
    """LOCAL-Page: window.PROSPECT_DATA auslesen."""
    i = t.find('window.PROSPECT_DATA')
    if i < 0:
        return None
    j = t.index('\n};', i) + 2
    raw = t[t.index('{', i):j]
    try:
        d = json.loads(raw)
    except Exception:
        return None
    crit = [clean(x) for x in d.get('criticalIssues', [])]
    opp = [clean(x) for x in d.get('opportunities', [])]
    return {
        'typ': 'LOCAL',
        'name': d.get('contactName', ''),
        'firma': d.get('companyName', ''),
        'stadt': d.get('city', ''),
        'keyword': d.get('focusKeyword', ''),
        'rang': d.get('mapsRankDesktop', ''),
        'bewertungen': d.get('currentReviewsCount', ''),
        'rating': d.get('currentRating', ''),
        'funde': (crit + opp)[:4],
        'wettbewerber': [
            f"{c.get('name','')} – {c.get('rank','')}, {c.get('reviews','')} Bew."
            for c in d.get('competitors', [])[:2]
        ],
    }


def parse_organic(t):
    """ORGANIC-Page: Anrede + rote Befunde aus dem Brief/Summary ziehen."""
    m = re.search(r'<p[^>]*>\s*(Hallo|Hi|Hello|Dear)\s+([^,<]+),', t)
    name = m.group(2).strip() if m else ''
    ti = re.search(r'<title>(.*?)</title>', t, re.S)
    firma = ''
    if ti:
        parts = clean(ti.group(1)).split('|')
        if len(parts) > 1:
            firma = parts[1].strip()
    funde = []
    # 1. Wahl: rote Box (Kritische Luecken), 2. Wahl: amber (Groesste Chance)
    for cls in ('red', 'amber'):
        box = re.search(r'summary-box ' + cls + r'"(.*?)</ul>', t, re.S)
        if box:
            funde += [clean(x) for x in re.findall(r'<li>(.*?)</li>', box.group(1), re.S)]
        if len(funde) >= 3:
            break
    if not funde:
        funde = [clean(x) for x in re.findall(
            r'pill-critical[^<]*</span>\s*<strong[^>]*>(.*?)</strong>', t, re.S)]
    return {
        'typ': 'ORGANIC', 'name': name, 'firma': firma, 'stadt': '',
        'keyword': '', 'rang': '', 'bewertungen': '', 'rating': '',
        'funde': funde[:4], 'wettbewerber': [],
        'gruen': [clean(x) for x in re.findall(
            r'<li>(.*?)</li>',
            (re.search(r'summary-box green"(.*?)</ul>', t, re.S) or
             re.match(r'(?!)', '') or type('', (), {'group': lambda s, i: ''})()).group(1), re.S)]
        if re.search(r'summary-box green"(.*?)</ul>', t, re.S) else [],
    }


def anker(t, d):
    """Detail-Kandidaten fuer den persoenlichen Anker (0-25 Sek.)."""
    kand = []
    pool = ' '.join(d['funde']) + ' ' + ' '.join(d.get('gruen', []))
    pats = [
        (r'zwei (Standorte?|Profile?|Adressen|Domains)', 'Zwei von etwas — Standorte/Profile/Domains'),
        (r'(seit|Seit) (19|20)\d\d', 'Gruendungsjahr / Jahre am Markt'),
        (r'(\d+) Jahre[n]? (Markt|Erfahrung|als)', 'Jahre im Beruf'),
        (r'(ausgezeichnet|Preis(traeger|)|Award|Duftstars|praemiert)', 'Auszeichnung'),
        (r'(Vizepraesidentin|Praesident|Obfrau|Vorstand|Mitglied)', 'Amt oder Mitgliedschaft'),
        (r'(zertifiziert|B\.Sc\.|Dr\.|Prof\.|LL\.M\.)', 'Qualifikation'),
        (r'(\d{3,}) (Bankpartner|Kunden|Betriebe|Mitglieder)', 'Auffaellige Zahl'),
    ]
    for pat, label in pats:
        m = re.search(pat, pool)
        if m:
            kand.append(f'{label}: "{clean(m.group(0))}"')
    if d.get('stadt'):
        kand.append(f'Ort konkret nennen: "{d["stadt"]}"')
    return kand[:4]


def zettel(slug, d, t=''):
    """Sprechzettel bauen."""
    L = []
    A = '=' * 68
    L.append(A)
    L.append(f'  90-SEKUNDEN-ZETTEL — {d["firma"] or slug}   [{d["typ"]}]')
    L.append(f'  https://741.studio/review/{slug}/')
    L.append(A)
    L.append('')

    L.append('  0-10 SEK · NAME + DER EINE FUND ' + '-' * 34)
    if d['typ'] == 'LOCAL':
        L.append(f'    "Hallo {d["name"] or "[Name]"}. {d["bewertungen"]} Bewertungen bei {d["rating"]} —')
        L.append(f'     und trotzdem {d["rang"]}.')
    else:
        L.append(f'    "Hallo {d["name"] or "[Name]"}. [ZAHL aus Fund 1 nennen] —')
    L.append('     Ich weiss nicht, ob du das wusstest, aber genau das wollte ich dir zeigen."')
    L.append('')

    L.append('  10-25 SEK · DER ANKER (Beweis, dass du hingesehen hast) ' + '-' * 10)
    L.append('    Ein Detail nennen, das NICHTS mit dem Audit zu tun hat.')
    ak = anker(t, d)
    if ak:
        L.append('    Kandidaten von der Seite:')
        for a in ak:
            L.append(f'      - {a}')
    else:
        L.append('      (nichts automatisch gefunden — kurz auf der Seite nachsehen)')
    L.append('')

    L.append('  25-50 SEK · ZEIGEN, NICHT ERKLAEREN ' + '-' * 29)
    if d['typ'] == 'LOCAL':
        L.append(f'    Grid zeigen. Keyword: {d["keyword"]}')
        L.append('    "Gruen waere Top 3. Du bist an X von 49 Punkten ueberhaupt sichtbar."')
    else:
        L.append('    Website / Suchergebnis zeigen. Zwei Saetze, mehr nicht.')
    L.append('')

    L.append('  50-70 SEK · DIE UMDEUTUNG (wichtigster Teil) ' + '-' * 21)
    if d['wettbewerber']:
        for w in d['wettbewerber']:
            L.append(f'    Gegner: {w}')
        L.append('    -> "X und Y stehen vor dir. Du hast mehr Bewertungen als beide."')
    L.append('    -> "Dir fehlt nicht [die Substanz]. Dir fehlen ein paar Einstellungen."')
    L.append('')

    L.append('  70-90 SEK · UEBERGEBEN ' + '-' * 42)
    L.append('    "Was genau zu tun ist, hab ich dir auf einer Seite aufgeschrieben —')
    L.append('     Link ist in der Nachricht. Kostet dich nichts, ich freu mich einfach')
    L.append('     ueber deine Einschaetzung."')
    L.append('')

    L.append('  DIE UEBRIGEN FUNDE (NICHT ins Video — die stehen auf der Seite) ' + '-' * 2)
    for i, f in enumerate(d['funde'], 1):
        L.append(f'    {i}. {f[:120]}')
    L.append('')

    L.append('  NICHT SAGEN ' + '-' * 53)
    L.append('    Raster-Erklaerung · Buch/Inhaltsverzeichnis · Buchautor · Visitenkarten ·')
    L.append('    Retargeting · 10 Jahre / 200 Betriebe · Liste mit 60 Verzeichnissen')
    L.append('    "Ich hoffe ich bin nicht zu schnell" · "Ich geh nicht auf alles ein"')
    L.append('')
    return '\n'.join(L)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    slugs = args
    if args[0] in ('--alle', '--all'):
        slugs = sorted(os.path.basename(os.path.dirname(p))
                       for p in glob.glob(os.path.join(REVIEW, '*', 'index.html')))
    for slug in slugs:
        t = load(slug)
        if t is None:
            print(f'  !! Keine Seite fuer "{slug}"')
            continue
        d = parse_local(t) or parse_organic(t)
        if not d or not d['funde']:
            print(f'  !! Keine Befunde in "{slug}"')
            continue
        print(zettel(slug, d, t))


if __name__ == '__main__':
    main()
