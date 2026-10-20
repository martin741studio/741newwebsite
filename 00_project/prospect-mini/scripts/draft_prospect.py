#!/usr/bin/env python3
"""Prospect mini workflow, step 7a: skeleton prospect.json from the evidence and findings files (proposal 28, 2026-10-12).

Usage: draft_prospect.py <slug|prospect_dir> [--out <file>] [--force]
Fills every number, table, card, cleanup number, calculator value (on its slider step) and the full sources block.
Text that needs a writer gets a short "TODO: ..." placeholder, often with the fact it must use. validate.py rejects
every TODO, so a skeleton never reaches a deploy. Writes prospect.json (only if it does not exist; else use --out or --force)
and evidence/draft-facts.json (all derived counts, for the writer and factcheck.py).
Slider steps are read from calc() in build_page.py, so the two files cannot drift apart.
Reads: intake.json|intake.md, evidence/falcon-report-*.json, dfs-volumes-ads.json, dfs-serp-name*.json, dfs-refdomains-spam.json,
dfs-backlinks-summary.json, site.json, site-pages.json, comp-pages.json, google-panel-*.md, scorecard-today.md.
Read only except the two output files. Standard library only.
"""
import datetime, json, os, re, sys, time
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_lib as L
from evidence_lib import de, pct

NUM = ['null', 'eine', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn', 'elf', 'zwölf']
LAND = {'DE': 'Deutschland', 'AT': 'Österreich', 'CH': 'der Schweiz'}
WHO = {'health': ('Patienten', 'neuem Patienten', 'Praxis', 'einer Praxis'), 'legal': ('Mandanten', 'neuem Mandanten', 'Kanzlei', 'einer Kanzlei'),
       'service': ('Kunden', 'neuem Kunden', 'Betrieb', 'einem Anbieter')}


def T(hint=''):
    return 'TODO' + (f': {hint}' if hint else '')


def word(n):
    return NUM[n] if 0 <= n < len(NUM) else str(n)


def steps():
    """Slider origin and step per calc key, parsed from calc() in build_page.py."""
    src = open(os.path.join(HERE, 'build_page.py'), encoding='utf-8').read()
    out = {}
    for k, mn, step in re.findall(r"dict\(id='(\w+)'.*?min=([^,]+(?:\([^)]*\))?), max=.*?step=([\d.]+)", src):
        m = re.match(r"c\.get\('(\w+)', ([\d.]+)\)", mn)
        out[k] = (float(step), (m.group(1), float(m.group(2))) if m else float(mn))
    return out


def snap(v, step, origin):
    n = round((v - origin) / step)
    x = round(origin + max(n, 0) * step, 2)
    return int(x) if x == int(x) else x


def scan_date(fr):
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.fromtimestamp(int(fr['timestamp']), ZoneInfo('Europe/Berlin')).strftime('%d.%m.%Y')
    except Exception:
        m = re.match(r'(\d+)/(\d+)/(\d{4})', fr.get('date') or '')
        return f'{int(m.group(2)):02d}.{int(m.group(1)):02d}.{m.group(3)} (US-Zeit, prüfen)' if m else T('Messdatum')


def pull_date(pdir, out_name):
    f = os.path.join(pdir, 'cost_ledger.jsonl')
    if os.path.exists(f):
        for l in open(f, encoding='utf-8'):
            j = json.loads(l) if l.strip() else {}
            if j.get('out') == out_name: return datetime.date.fromisoformat(j['at'][:10]).strftime('%d.%m.%Y')
    p = os.path.join(pdir, 'evidence', f'dfs-{out_name}.json')
    return datetime.date.fromtimestamp(os.path.getmtime(p)).strftime('%d.%m.%Y') if os.path.exists(p) else T('Abrufdatum')


def proof_pick(branch, kw):
    lib = json.load(open(os.path.join(L.MINI, 'case-library.json'), encoding='utf-8'))
    want = {'health': ['gesundheit'], 'legal': ['recht'], 'service': ['dienstleistung']}.get(branch, [])
    for k, tags in [('heilprakt', ['heilpraktiker']), ('physio', ['physio']), ('psycho', ['psychotherapie']), ('ergo', ['ergo'])]:
        if k in kw: want = tags + want
    score = lambda c: sum(3 - min(i, 2) for i, t in enumerate(want) if t in (c.get('branch') or []))
    ok = lambda c: branch == 'legal' or 'recht' not in (c.get('branch') or [])  # never a law firm case on a non-legal page
    feat = sorted([c for c in lib['cases'] if ok(c)], key=lambda c: -score(c))[:4]
    more = sorted([c for c in lib['more'] if ok(c)], key=lambda c: -score(c))[:5]
    return [c['id'] for c in feat], [c['id'] for c in more]


def build(pdir):
    it, fr, F = L.intake(pdir), L.falcon(pdir), L.facts(pdir)
    sc, s = F.get('scan') or {}, L.site(pdir)
    pn, comp, sp = L.panel(pdir), F.get('comp') or {}, F.get('spam')
    rows, vfile = L.volumes(pdir)
    vm = {r['keyword'].lower(): r for r in rows}
    branch = it.get('branch') or 'health'
    who, per, col, prov_word = WHO.get(branch, WHO['service'])
    cols = {'Praxis': 'Praxen', 'Kanzlei': 'Kanzleien'}.get(col, col + 'e')
    slug = it.get('slug') or os.path.basename(os.path.normpath(pdir))
    kw = sc.get('keyword') or T('Suchbegriff')
    kws = kw.split()
    city = it.get('city') or (kws[-1].title() if len(kws) > 1 else T('Ort'))
    provider = kws[0].title() if kws else T('Beruf')
    land = LAND.get(it.get('country', 'DE'), 'Deutschland')
    company = it.get('business') or pn.get('name') or sc.get('me_name') or T('Firmenname')
    website = it.get('website') or s.get('home_final_url') or s.get('home') or T('Website')
    dom = L.domain(website)
    first = it.get('first_name') or (it.get('name') or T('Vorname')).split()[0]
    pts, top3, found = sc.get('points', 49), sc.get('top3_points', 0), sc.get('found_in', 0)
    top = sc.get('top4') or []
    rating = pn.get('rating') or float(sc.get('me_rating') or 0)
    reviews = pn.get('reviews') if pn.get('reviews') is not None else sc.get('me_reviews', 0)
    replies, newest = pn.get('replies'), pn.get('newest')
    age = {'year': 'Jahr', 'month': 'Monat', 'week': 'Woche'}
    newest_de = (lambda n, u: f'rund {n} {age[u]}{"en" if u == "week" and n != "1" else "e" if n != "1" else ""}')(*newest.split()) if newest else None
    score = (F.get('score_today') or {}).get('score')
    sdate = scan_date(fr) if fr else T('Messdatum')
    vdate = pull_date(pdir, 'volumes-ads')
    me_kw = vm.get(kw.lower()) or {}

    # demand: rows with a volume, one row per merged Google variant, provider rows marked
    merged = {k for g in L.merged_groups(rows) for k in g['keywords'][1:]}
    dem = sorted([r for r in rows if r.get('search_volume') and r['keyword'] not in merged], key=lambda r: -r['search_volume'])[:10]
    ptype = lambda k: 'provider' if kws and (L.stem(kws[0]) in k or (len(kws) > 1 and k.endswith(' ' + kws[-1]) and len(k.split()) == 2 and L.stem(kws[0])[:5] in k)) else 'question'
    demand = [{'keyword': r['keyword'], 'volume': r['search_volume'], 'type': ptype(r['keyword'])} for r in dem]
    topics = [d for d in demand if d['type'] == 'question']
    merged_note = ' '.join(f'Google zählt „{b}“ bei „{g["keywords"][0]}“ mit.' for g in L.merged_groups(rows) for b in g['keywords'][1:])

    # depth: own homepage vs. competitors
    hw = s.get('home_words') or 0
    h1 = ' '.join(s.get('home_h1') or []).lower()
    h1_hits = sum(1 for w in ([L.stem(kws[0])] if kws else []) + ([kws[-1]] if len(kws) > 1 else []) if w in h1)
    longer = bool(comp) and hw >= comp.get('mean_words', 0)

    # calculator on its slider steps
    st = steps()
    vol = me_kw.get('search_volume') or max([d['volume'] for d in demand if d['type'] == 'provider'] or [50])
    vol_min = min(50, max(10, int(vol) // 10 * 10))
    cpc_raw = me_kw.get('cpc') or 1.0
    calc = {'vol': snap(vol, st['vol'][0], vol_min), 'vol_min': vol_min, 'vol_max': max(2000, int(vol) * 10),
            'budget': snap(150, st['budget'][0], st['budget'][1]), 'cpc': snap(max(cpc_raw, 0.5), st['cpc'][0], st['cpc'][1]),
            'conv': snap(4, st['conv'][0], st['conv'][1]), 'deal': snap(40, st['deal'][0], st['deal'][1]),
            'deal_label': 'Anteil der Anfragen, die einen Termin buchen', 'val': snap(250, st['val'][0], 100), 'val_min': 100, 'val_max': 2000,
            'val_label': T(f'Umsatz pro {per} (Startwert aus der Preis-Seite, Vielfaches von 50 ab 100)'),
            'group_c': f'Aus Besuchern werden {who}', 'deals_label': f'neue {who} / Monat', 'per_label': per}
    calc['volumes_line'] = (f'Echte Google-Suchen pro Monat (ganz {land}, Mittel der letzten 12 Monate): <b>{kw} {de(vol)}</b>'
                            + (f' · {topics[0]["keyword"]} {de(topics[0]["volume"])}' if topics else '')
                            + (f'. Ein Anzeigen-Klick auf „{kw}“ kostet bei Google rund <b>{de(cpc_raw, 2)} US-Dollar</b> (Google-Angabe in Dollar; der Regler startet ohne Umrechnung bei {de(calc["cpc"], 2)} €)' if me_kw.get('cpc') else '')
                            + f' (Abruf {vdate}). {T("Startwert Umsatz pro " + per + " aus der Preis-Seite")}. Budget, Anfrage- und Buchungsanteil sind Annahmen.')

    # hero cards
    t1 = top[0] if top else {}
    cards = [
        {'icon': {'health': '🌿', 'legal': '⚖️'}.get(branch, '🏢'), 'title': company, 'sub': T(f'Beruf · Leistungen · Ort ({city})'),
         'badge': f'{de(rating, 1)} ★ bei {reviews} Bewertungen' if rating else T('Sterne + Bewertungen'), 'tone': 'green' if rating >= 4.5 else 'amber'},
        {'icon': '📍', 'title': 'Dein Google-Eintrag', 'sub': f'„{kw}“: unter den ersten drei an {top3} von {pts} Punkten',
         'badge': T('Platz in der Stadtmitte (aus dem Kartenbild)'), 'tone': 'red' if top3 < pts / 4 else 'amber'},
        {'icon': '⭐', 'title': 'Google-Bewertungen', 'sub': f'Du: {reviews}' + (f', die neueste vor {newest_de}' if newest_de else '') + (f' · {T("Kurzname")} ({t1.get("name")}): {t1.get("reviews")}' if t1 else ''),
         'badge': ('Keine Antworten der Praxis' if replies == 0 else f'{replies} von {reviews} beantwortet') if replies is not None else T('Antworten der Praxis (Panel)'),
         'tone': 'red' if replies == 0 else 'amber'},
        {'icon': '🔍', 'title': dom, 'sub': T('erster Bildschirm heute (aus home-today-1440.jpg)'),
         'badge': f'Startseite heute: {score} von 44 Punkten' if score is not None else T('Punkte heute (scorecard-today.md)'), 'tone': 'amber', 'href': website}]

    # check strips (facts as plain sentences)
    tel = bool(s.get('tel_links_home')) and not s.get('pages_with_broken_tel')
    ttfb = (F.get('site') or {}).get('ttfb_mean')
    photo = lambda i: f'/review-assets/{slug}/foto-{i}.webp'
    r_site = [{'status': 'ok' if tel else 'crit', 'title': 'Telefonnummer antippbar' if tel else 'Telefonnummer nicht antippbar',
               'text': 'Auf jeder Seite ist deine Nummer ein Link. Ein Tipp am Handy, und es klingelt.' if tel else T('welche Seiten (site.json pages_with_broken_tel)')},
              {'status': 'ok' if s.get('http_redirects_to_https') else 'crit', 'title': 'Immer verschlüsselt' if s.get('http_redirects_to_https') else 'Nicht immer verschlüsselt',
               'text': 'Deine Seite öffnet sich immer mit dem Schloss-Symbol im Browser.' if s.get('http_redirects_to_https') else 'Die Adresse ohne „https“ leitet nicht auf die sichere Seite weiter.'}]
    if ttfb is not None:
        r_site.append({'status': 'ok' if ttfb < 0.8 else 'warn', 'title': 'Ladezeit gut' if ttfb < 0.8 else 'Ladezeit knapp',
                       'text': f'Deine Seite beginnt nach rund {de(ttfb, 1)} Sekunden zu laden.' + ('' if ttfb < 0.8 else ' Schneller ist besser, vor allem am Handy.')})
    form = s.get('form_on_contact') or s.get('form_on_home')
    r_site.append({'status': 'ok' if form else 'warn', 'title': 'Anfrage-Formular' if form else 'Kein Anfrage-Formular',
                   'text': 'Auf der Kontakt-Seite gibt es ein Formular.' if s.get('form_on_contact') else 'Auf der Startseite gibt es ein Formular.' if form
                   else 'Es gibt keine Kontakt-Seite und kein Formular.' if not s.get('contact_url') else 'Weder Startseite noch Kontakt-Seite haben ein Formular.'})
    r_read = [{'status': 'ok' if h1_hits == 2 else 'crit', 'title': 'Hauptüberschrift',
               'text': f'Nennt „{provider}“ und „{city}“.' if h1_hits == 2 else T(f'Hauptüberschrift heute: „{" / ".join(s.get("home_h1") or ["keine"])[:120]}“; ohne „{provider}“ oder „{city}“')}]
    for d in s.get('duplicate_pages') or []:
        r_read.append({'status': 'warn', 'title': 'Seite doppelt', 'text': f'{dom}{d["pages"][1]} zeigt denselben Titel und gleich viele Wörter ({d["words"]}) wie {dom}{d["pages"][0]}.'})
    if s.get('pages_no_h1'):
        r_read.append({'status': 'warn', 'title': 'Seiten ohne Hauptüberschrift', 'text': f'{s["pages_no_h1"]} von {s.get("pages_measured")} Seiten haben keine. ' + T('Beispielseite')})
    r_read.append({'status': 'warn', 'title': 'Beschreibung bei Google', 'text': T(f'heutige Beschreibung: „{(s.get("home_meta") or "keine")[:120]}“')})
    if comp:
        r_read.append({'status': 'ok' if longer else 'warn', 'title': 'Ausführliche Texte' if longer else 'Kurze Texte',
                       'text': f'Deine Startseite hat {de(hw)} Wörter, die gemessenen Seiten vor dir im Mittel {de(comp["mean_words"])}. ' + T('Startseiten oder Leistungsseiten? (comp-pages.json)')})
    r_meas = [{'status': 'ok' if s.get('ga4') or s.get('gtm') else 'crit', 'title': 'Besucher-Statistik eingebaut' if s.get('ga4') or s.get('gtm') else 'Keine Besucher-Statistik',
               'text': 'Auf der Website ist eine Besuchermessung eingebaut.' if s.get('ga4') or s.get('gtm') else 'Auf der Website ist keine Besuchermessung zu finden.'},
              {'status': 'ok' if s.get('jsonld_blocks') else 'warn', 'title': 'Daten für Google' if s.get('jsonld_blocks') else 'Daten für Google fehlen',
               'text': T(f'{s.get("jsonld_blocks")} Datenblock/-blöcke für Google: prüfen, ob Adresse und Leistungen darin stehen') if s.get('jsonld_blocks') else 'Adresse, Zeiten und Leistungen stehen nicht in der Form auf der Seite, die Google direkt auslesen kann.'}]
    r_rep = []
    if rating: r_rep.append({'status': 'ok' if rating >= 4.5 else 'warn', 'title': f'{de(rating, 1)} Sterne', 'text': f'{de(rating, 1)} Sterne bei {reviews} Bewertungen.'})
    if reviews is not None and t1:
        r_rep.append({'status': 'warn' if reviews < (t1.get('reviews') or 0) else 'ok', 'title': 'Wenige Bewertungen' if reviews < (t1.get('reviews') or 0) else 'Genug Bewertungen',
                      'text': f'{reviews} Bewertungen' + (f', die neueste ist {newest_de} alt' if newest_de else '') + f'. {T("Kurzname")} ({t1.get("name")}) hat {t1.get("reviews")}.'})
    if replies is not None: r_rep.append({'status': 'warn' if replies == 0 else 'ok', 'title': 'Keine Antworten' if replies == 0 else 'Antworten auf Bewertungen',
                                          'text': f'Auf keine deiner {reviews} Bewertungen gibt es eine Antwort.' if replies == 0 else f'{replies} von {reviews} Bewertungen haben eine Antwort.'})
    if sp: r_rep.append({'status': 'crit' if sp['spam'] / max(sp['total'], 1) >= 0.3 else 'warn', 'title': 'Unseriöse Links',
                         'text': f'{sp["spam"]} von {sp["total"]} Websites, die auf dich verlinken, sind unseriös. ' + T('Beispiel aus dfs-refdomains-spam.json')})
    if branch == 'health': r_rep.append({'status': 'warn', 'title': 'Werberecht', 'text': T('neutral, nur wenn site-findings.md Sätze mit Krankheiten oder Heilversprechen zitiert')})

    # cleanup numbers
    cleanup = []
    if sp: cleanup.append({'n': f'{sp["spam"]} / {sp["total"]}', 'text': 'Websites, die auf deine Seite verlinken, sind unseriös. ' + T('Beispiel, und was wir tun')})
    person = L.slugify(it.get('name') or '')
    for n in F.get('names') or []:
        if n['own_rank'] is None and n['organic'] and L.slugify(n['keyword'] or '') != person:  # the person's own name is not the business name
            cleanup.append({'n': f'{n["organic"]} Treffer', 'text': f'Wer „{n["keyword"].strip(chr(34))}“ sucht, findet deine Website nicht unter den ersten {n["organic"]} Treffern. ' + T('was davor steht')})
    if s.get('duplicate_pages'): cleanup.append({'n': f'{len(s["duplicate_pages"]) + 1} Startseiten' if any(d['pages'][0] == '/' for d in s['duplicate_pages']) else f'{len(s["duplicate_pages"])} doppelt',
                                                 'text': T('welche Adressen (site.json duplicate_pages)')})
    if replies is not None and reviews: cleanup.append({'n': f'{replies} / {reviews}', 'text': 'Bewertungen mit einer Antwort von dir.'})

    me_cats = pn.get('category') or (L.cats_de(L.own_place(fr, it.get('place_id'), website, company) or {}) if fr else '')
    table = [{'name': company, 'cats': me_cats or T('Kategorie'), 'reviews': reviews, 'share': pct(sc.get('solv', 0)), 'me': True}]
    for i, p in enumerate(top[:4]):
        table.append(dict({'name': p['name'], 'cats': p['cats'], 'reviews': p['reviews'], 'share': pct(p['solv'])}, **({'bold': True} if i == 0 else {})))
    rr, kr = sc.get('reviews_range', [0, 0]), sc.get('km_range', [0, 0])
    feat, more = proof_pick(branch, kw.lower())

    items = [{'title': f'Startseite „{provider} in {city}“', 'tag': 'Ort',
              'why': (f'{word(comp["h1_keyword"]).capitalize()} der {word(comp["measured"])} gemessenen Seiten vor dir nennen Beruf und Ort in der Hauptüberschrift. ' if comp else '') + T('was deine Startseite heute sagt')}]
    for d in topics[:4]:
        items.append({'title': T(f'Seite zu „{d["keyword"]}“'), 'tag': 'Leistung', 'why': f'„{d["keyword"]}“: {de(d["volume"])} Suchen pro Monat in {land}. ' + T('was deine Seite heute dazu sagt')})
    while len(items) < 6: items.append({'title': T('Inhalt'), 'tag': 'Profil', 'why': T('Grund mit Beleg')})

    p = {
        'slug': slug, 'first_name': first, 'display_name': it.get('name') or T('Name'), 'company': company,
        'business_ref': T(f'deine {col} {company}'), 'website': website, 'loom_url': '',
        'meta': {'title': f'Private Website- & Sichtbarkeits-Analyse | {company}, {city} | 741.Studio',
                 'desc': f'Persönliche Website- und Sichtbarkeits-Analyse für {company} in {city}, von 741.Studio.'},
        'hero': {'accent': 'Google-Sichtbarkeit', 'sub': T(f'Lage in 3 Sätzen: {de(rating, 1)} Sterne, „{kw}“ unter den ersten drei an {top3} von {pts} Punkten'), 'cards': cards},
        'grid': {'grid_size': sc.get('grid_size', 7), 'h2': T('Überschrift Kartenmessung'),
                 'intro': f'Wir haben gemessen, wo deine {col} bei der Suche <b>„{kw}“</b> in der Google-Karte erscheint: an {pts} Punkten im {de(sc.get("radius_km", 5), 0)}-km-Umkreis um die Stadtmitte von {city} (Messung vom {sdate}). Jede Zahl ist dein Platz an genau diesem Ort.',
                 'alt': f'Google-Karten-Messung für {company}, Suchbegriff {kw}',
                 'caption_today': f'<b>Unter den ersten drei an {top3} von {pts} Punkten.</b> {T("wo genau (aus dem Kartenbild), Platz in der Stadtmitte")}. An {sc.get("not_top20", 0)} Punkten nicht unter den ersten 20.'
                                  + (f' {T("Kurzname")} ({t1["name"]}) steht auf rund {pct(t1["solv"])} der Karte unter den ersten drei.' if t1 else ''),
                 'caption_goal': f'<b>{T("Ziel in einem Satz")}</b> Die {cols} vorn haben {rr[0]} bis {rr[1]} Bewertungen.',
                 'chips': [T('Chip 1'), T('Chip 2'), T('Chip 3')]},
        'system': {
            'intro': T('Für deine Praxis haben wir drei Dinge geprüft ... (Zahlen = Messungen, Rechner = Annahmen)'),
            'steps': [{'title': f'Wonach deine {who} suchen', 'text': 'Welche Leistungen sie bei Google eingeben und welche Fragen deine Seite noch nicht beantwortet.',
                       'kpi': f'{de(topics[0]["volume"])} Suchen/Monat: {topics[0]["keyword"]}' if topics else T('größte Suchzahl')},
                      {'title': 'Damit das Telefon klingelt', 'text': f'Warum andere {cols} in der Google-Karte vor dir stehen.',
                       'kpi': f'unter den ersten 20 an {found} von {pts} Punkten'},
                      {'title': 'Startseite, die Termine bringt', 'text': 'Ob ein Besucher in 5 Sekunden versteht, was du anbietest und wie er einen Termin bekommt.',
                       'kpi': f'heute {score} von 44 Punkten' if score is not None else T('Punkte heute')}],
            'step1': {'h2': T('Überschrift Suchthemen'), 'lead': T('ein Satz: womit wir verglichen haben'),
                      'demand_sub': f'Suchen pro Monat in ganz {land} (Mittel der letzten 12 Monate, Abruf {vdate})', 'provider_word': prov_word,
                      'demand': demand, 'demand_note': T('was die Zahlen heißen') + (' ' + merged_note if merged_note else ''),
                      'no_data': (F.get('volumes') or {}).get('no_data', []),
                      'depth': {'title': T('Titel Tiefe'), 'sub': T('ein Satz'),
                                'big': [{'n': de(hw), 'label': 'Wörter auf deiner Startseite', 'tone': 'good' if longer else 'bad'},
                                        {'n': str(h1_hits), 'label': f'Mal „{provider}“ oder „{city}“ in deiner Hauptüberschrift', 'tone': 'good' if h1_hits == 2 else 'bad'}],
                                'bars': ([{'label': 'Deine Startseite', 'val': hw, 'tone': 'good' if longer else 'bad'},
                                          {'label': f'Seiten vor dir (Mittel aus {comp["measured"]})', 'val': comp['mean_words'], 'tone': 'bad' if longer else 'good'}] if comp else []),
                                'note': ((f'{word(comp["h1_keyword"]).capitalize()} der {word(comp["measured"])} gemessenen Seiten vor dir nennen „{provider}“ und „{city}“ in der Hauptüberschrift. ') if comp else '') + T('ein Satz zu deiner Hauptüberschrift')},
                      'items': items},
            'step2': {'h2': T('Überschrift Karte'),
                      'lead': f'Wir haben die Google-Einträge der {cols} verglichen, die bei „{kw}“ oben stehen. '
                              + f'{word(int(sc.get("top4_pair_found_all", "0/4").split("/")[0])).capitalize()} der {word(len(top[:4]))} ersten sind an allen {pts} Messpunkten unter den ersten 20 zu sehen. Deine {col} an {found}.',
                      'keyword': kw, 'col_name': col, 'table': table,
                      'fine': f'Prozent = an wie vielen von {pts} Messpunkten im {de(sc.get("radius_km", 5), 0)}-km-Umkreis um die Stadtmitte die {col} unter den ersten drei der Google-Karte steht. Gemessen am {sdate}.',
                      'meaning': T(f'was das heißt; Fakten: Bewertungen vorn {rr[0]} bis {rr[1]}, Entfernung vorn {de(kr[0], 1)} bis {de(kr[1], 1)} km, deine {col} {de(sc.get("me_km") or 0, 1)} km'),
                      'changes': [{'title': T(f'Einordnung (Google heute: {me_cats or "?"})'), 'text': T(f'Fakt: {sc.get("top4_pair_provider_cat")} der vier vorn mit Kategorie wie „{provider}“')},
                                  {'title': 'Alle Leistungen eintragen', 'text': T('Liste aus dem Menü der Website')},
                                  {'title': 'Neue Bewertungen', 'text': (f'Deine neueste Bewertung ist {newest_de} alt. ' if newest_de else '') + T('wie bitten')},
                                  {'title': 'Auf jede Bewertung antworten', 'text': (f'Heute hat keine deiner {reviews} Bewertungen eine Antwort. ' if replies == 0 else '') + T('warum')},
                                  {'title': T('Fotos'), 'text': T('Satz')}, {'title': T('Beiträge'), 'text': T('Satz')}],
                      'cleanup': cleanup, 'good': T('die gute Nachricht')},
            'step3': {'lead': 'Wir prüfen jede Startseite an 22 Punkten, die darüber entscheiden, ob jemand einen Termin anfragt'
                              + (', bei Gesundheitsberufen inklusive Werberecht' if branch == 'health' else '') + '. Im zweiten Bild siehst du einen Entwurf des ersten Bildschirms mit deinem Logo und deinen Fotos.',
                      'score_today': score or 0, 'score_draft': score or 0, 'score_draft_label': T('Zielwert für den Entwurf (nur mit Beleg)'),
                      'alt_today': f'Heutige Startseite von {company}, erster Bildschirm', 'alt_draft': f'Entwurf des ersten Bildschirms für {company}',
                      'note_today': T('was heute gut ist, was fehlt'), 'note_draft': T('was der Entwurf zeigt'),
                      'five': [{'q': q, 'a': T('Antwort aus home-today-1440.jpg')} for q in ['Was?', 'Wo?', 'Warum du?', 'Wie zum Termin?', 'Wer?']]}},
        'calc': calc,
        'check': [{'title': 'Deine Website', 'photo': photo(1), 'pos': '50% 50%', 'rows': r_site},
                  {'title': 'Was Google liest', 'photo': photo(2), 'pos': '50% 30%', 'rows': r_read},
                  {'title': 'Was du messen kannst', 'photo': photo(3), 'pos': '50% 50%', 'rows': r_meas},
                  {'title': 'Dein Ruf im Netz', 'photo': photo(1), 'pos': '80% 70%', 'rows': r_rep}],
        'quick_wins': [{'title': T(f'Sofort-Schritt {i}'), 'text': T('Satz')} for i in range(1, 7)],
        'roadmap': [{'step': 'Woche 1–2 · Aufräumen', 'what': T('was'), 'prio': 'Hoch', 'effort': 'Gering', 'why': 'Erst aufräumen, dann ausbauen'},
                    {'step': 'Woche 1–3 · Telefon klingeln', 'what': T('Google-Eintrag: was'), 'prio': 'Hoch', 'effort': 'Gering', 'why': T('warum')},
                    {'step': 'Woche 2–4 · Startseite', 'what': f'Erster Bildschirm mit „{provider} in {city}“, Bewertungen, Telefon und Termin-Button', 'prio': 'Hoch', 'effort': 'Mittel', 'why': 'Aus Besuchern werden Termine'},
                    {'step': 'Woche 3–8 · Neue Inhalte', 'what': ', '.join(d['keyword'] for d in topics[:4]) or T('Themen'), 'prio': 'Hoch', 'effort': 'Mittel', 'why': f'Seiten für die Themen, die {who} wirklich googeln'},
                    {'step': 'Laufend · Messen', 'what': 'Besucher, Anrufe und Anfragen plus monatliche Kartenmessung', 'prio': 'Mittel', 'effort': 'Gering', 'why': 'Jede Maßnahme muss sich in Zahlen zeigen'}],
        'proof': {'h2': T('Überschrift Fälle'), 'lead': T('warum diese Fälle (Branche + Engpass)'), 'featured': feat, 'labels': {}, 'more': more},
        'final': {'h2': T('Schluss-Überschrift'), 'p': '30 Minuten, kostenlos: Ich zeige dir live, wer in deinem Markt oben steht, und wie aus diesen Punkten mehr Anfragen werden. Unverbindlich.',
                  'subject': quote(f'{company} Sichtbarkeits-Analyse')},
        'sources': {k: v for k, v in {
            'grid': f'{sc.get("src")} (keyword {kw}, {sc.get("grid_size")}x{sc.get("grid_size")}, {sc.get("radius_km")} km, centre {"/".join(map(str, sc.get("centre") or []))}, {sdate}; solv {sc.get("solv")} = {top3}/{pts}, found_in {found}) + review-assets/{slug}/scan-grid.webp' if sc else None,
            'step1.demand': f'{vfile} (Google Ads, {it.get("country", "DE")} {it.get("location_code", 2276)}, 12-month mean, newest month {"-".join(map(str, (F.get("volumes") or {}).get("newest_month") or []))}; merged variants shown once: {"; ".join(" = ".join(g["keywords"]) for g in L.merged_groups(rows)) or "none"})' if vfile else None,
            'step1.depth': f'evidence/site-pages.json (home {hw} words) + evidence/comp-pages.json ({comp.get("measured")} readable competitor homepages: {", ".join(map(str, comp.get("words", [])))}; mean {comp.get("mean_words")}; H1 with provider + city: {comp.get("h1_keyword_pair")})' if comp else None,
            'step2.table': f'{sc.get("src")} (places: solv, reviews, categories, found_in, lat/lng)' if sc else None,
            'step2.cleanup.spam': f'evidence/dfs-refdomains-spam.json (total_count {sp["spam"]}) + evidence/dfs-backlinks-summary.json (referring_domains {sp["total"]})' if sp else None,
            'step2.cleanup.name': '; '.join(f'{n["src"]} ({n["keyword"]}: {n["organic"]} organic, own rank {n["own_rank"]})' for n in F.get('names') or []) or None,
            'check.site': f'evidence/site.json (https {s.get("http_redirects_to_https")}, ttfb {s.get("ttfb_secs")}, ga4 {s.get("ga4")}, tel links, jsonld {s.get("jsonld_blocks")}, pages_no_h1 {s.get("pages_no_h1")}, form on contact {s.get("form_on_contact")})' if s else None,
            'reviews': f'{pn.get("_file")} ({de(rating, 1)} / {reviews}; newest {newest}; {replies} owner replies)' if pn else f'{sc.get("src")} (rating {sc.get("me_rating")}, reviews {sc.get("me_reviews")}); panel missing' if sc else None,
            'step3.today': f'evidence/home-today-1440.jpg + evidence/scorecard-today.md ({score}/44)' if score is not None else None,
            'step3.draft': 'draft/index.html + evidence/home-draft-1440.jpg',
            'calc': f'{vfile} (volume {kw} {vol}, cpc {cpc_raw} -> slider {calc["cpc"]}); val: ' + T('Preis-Seite') + '; budget/conv/deal = assumptions, labelled',
            'proof': 'prospect-mini/case-library.json (' + ', '.join(feat) + '; more: ' + ', '.join(more) + ')',
            'derived': 'evidence/draft-facts.json (counts computed by draft_prospect.py from the files above)'}.items() if v},
        'guide': {k: T(f'max. 2 Sätze ({k})') for k in ['hello', 'point', 'think', 'insight', 'celebrate']},
    }
    return p, F


def main():
    t0 = time.time()
    args = sys.argv[1:]
    out = None
    if '--out' in args: i = args.index('--out'); out = args[i + 1]; del args[i:i + 2]
    force = '--force' in args
    if force: args.remove('--force')
    a = args[0]
    pdir = a if os.path.isdir(a) else os.path.join(L.ROOT, '00_project', 'prospects', a)
    p, F = build(pdir)
    out = out or os.path.join(pdir, 'prospect.json')
    if os.path.exists(out) and not force and not out.endswith('.draft.json'):
        raise SystemExit(f'{out} exists: use --out <file> or --force')
    json.dump(p, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(F, open(os.path.join(pdir, 'evidence', 'draft-facts.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
    todo = len(re.findall(r'TODO', json.dumps(p, ensure_ascii=False)))
    print(json.dumps({'out': out, 'todo_fields': todo, 'secs': round(time.time() - t0, 2)}))


if __name__ == '__main__':
    main()
