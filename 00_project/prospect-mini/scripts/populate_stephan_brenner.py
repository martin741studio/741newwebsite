#!/usr/bin/env python3
import json, os

pfile = '00_project/prospects/stephan-brenner/prospect.json'
with open(pfile, 'r', encoding='utf-8') as f:
    p = json.load(f)

p['business_ref'] = 'eure Kanzlei'
p['branch'] = 'legal'

p['hero']['sub'] = 'Ihr habt 5,0 Sterne bei Google. Bei der Suche „anwalt gesellschaftsrecht stuttgart“ ist die Kanzlei jedoch an keinem der 49 Messpunkte unter den ersten drei zu sehen.'
p['hero']['cards'][0]['sub'] = 'Boutique-Kanzlei für Gesellschaftsrecht und Prozessführung · Stuttgart'
p['hero']['cards'][1]['badge'] = 'In ganz Stuttgart an keinem Punkt unter den ersten drei'
p['hero']['cards'][2]['sub'] = 'Ihr: 5 Bewertungen · LUTZ Rechtsanwälte: 202 Bewertungen'
p['hero']['cards'][3]['sub'] = 'Erster Bildschirm: Kein Kontakt-Button, keine Sterne, Angebot ohne klaren Handlungsaufruf'
p['hero']['cards'][3]['badge'] = 'Startseite heute: 8 von 42 Punkten'

p['grid']['h2'] = 'Unter den ersten drei an 0 von 49 Punkten. Im gesamten Stadtgebiet nicht unter den Top 3.'
p['grid']['intro'] = 'Wir haben gemessen, wo eure Kanzlei bei der Suche <b>„anwalt gesellschaftsrecht stuttgart“</b> in der Google-Karte erscheint: an 49 Punkten im 5-km-Umkreis um die Kanzlei in Stuttgart (Messung vom 16.10.2026). Jede Zahl ist euer Platz an genau diesem Ort.'
p['grid']['caption_today'] = '<b>Unter den ersten drei an 0 von 49 Punkten.</b> Selbst in der Calwer Straße und im Zentrum reicht es nicht für die Top 3. LUTZ Rechtsanwälte führt die Karte mit 97,96 % Sichtbarkeit an.'
p['grid']['caption_goal'] = '<b>Ziel: Sichtbarkeit in Stuttgart für Unternehmer und Gesellschafter, die nach Gesellschaftsrecht suchen.</b> Die Kanzleien vorn haben 78 bis 202 Bewertungen.'
p['grid']['chips'] = [
    '📞 Direkte Mandatsanfragen aus der Google-Karte',
    '🧭 Unternehmer in Stuttgart finden CONTIQ sofort',
    '🤝 Erstkontakt für gesellschaftsrechtliche Beratung'
]

p['system']['intro'] = 'Für eure Kanzlei haben wir drei Hebel geprüft: wonach Mandanten in Stuttgart suchen, warum andere Kanzleien in der Karte vorn stehen und wie eure Website Mandanten gewinnt.'
p['system']['steps'][2]['kpi'] = 'heute 8 von 42 Punkten'

p['system']['step1']['h2'] = 'Für gesellschaftsrechtliche Beratung suchen Mandanten gezielt nach Fachanwälten in Stuttgart.'
p['system']['step1']['lead'] = 'Wir haben die Website von CONTIQ mit den Kanzleien verglichen, die bei „anwalt gesellschaftsrecht stuttgart“ oben stehen.'
p['system']['step1']['demand_note'] = '„anwalt gesellschaftsrecht stuttgart“ und „rechtsanwalt gesellschaftsrecht stuttgart“ bündeln die gezielte lokale Nachfrage von Unternehmen und Gesellschaftern.'

p['system']['step1']['depth']['title'] = 'Gute Texttiefe, aber Stuttgart fehlt in den wichtigsten Überschriften.'
p['system']['step1']['depth']['sub'] = 'Eure Unterseiten bieten fachliche Tiefe, doch Google fehlt die klare Verknüpfung der Rechtsgebiete mit dem Standort Stuttgart.'
p['system']['step1']['depth']['note'] = 'Die Startseite konzentriert sich auf die Kanzlei-Marke, nennt aber im Kopfbereich keinen Standort.'

p['system']['step1']['items'] = [
    {
        'title': 'Startseite auf Gesellschaftsrecht in Stuttgart ausrichten',
        'tag': 'Ort',
        'why': 'Die Startseite nennt Stuttgart heute nur im Impressum und Footer, nicht im sichtbaren Kopfbereich.'
    },
    {
        'title': 'Eigene Leistungsseite zu Gesellschaftsrecht Stuttgart',
        'tag': 'Leistung',
        'why': 'Eine fokussierte Unterseite für gesellschaftsrechtliche Streitigkeiten und Beratung im Großraum Stuttgart.'
    },
    {
        'title': 'Eigene Leistungsseite zu M&A und Unternehmenstransaktionen',
        'tag': 'Leistung',
        'why': 'Unternehmer suchen gezielt nach Beratern für Unternehmenskauf und Transaktionsbegleitung.'
    },
    {
        'title': 'Eigene Leistungsseite zu Gesellschafterstreit und Beschlussanfechtung',
        'tag': 'Leistung',
        'why': 'Konkrete Mandatsanlässe abfangen, statt nur abstrakte Rechtsgebiete aufzuzählen.'
    },
    {
        'title': 'Eigene Leistungsseite zu Prozessführung und Dispute Resolution',
        'tag': 'Leistung',
        'why': 'Eure Kernkompetenz vor Gerichten und Schiedsgerichten mit Referenzen untermauern.'
    },
    {
        'title': 'Klares Kanzleiprofil für Unternehmer',
        'tag': 'Profil',
        'why': 'Mandanten wollen sofort sehen, welche Partner den Fall führen und warum CONTIQ die richtige Boutique-Kanzlei ist.'
    }
]

p['system']['step2']['h2'] = 'LUTZ Rechtsanwälte hält fast 98 % der Karte. Eure Kanzlei ist in Stuttgart noch nicht vorn platziert.'
p['system']['step2']['meaning'] = 'Die Kanzleien an der Spitze haben zwischen 78 und 202 Bewertungen und sind als Rechtsanwälte fest in Stuttgart verankert. CONTIQ hat 5 Bewertungen und taucht fast nirgends in den Top 20 auf.'

for row in p['system']['step2']['table']:
    if 'Bankruptcy attorney' in row.get('cats', ''):
        row['cats'] = row['cats'].replace('Bankruptcy attorney', 'Insolvenzrecht')
    if 'Employment attorney' in row.get('cats', ''):
        row['cats'] = row['cats'].replace('Employment attorney', 'Arbeitsrecht')

p['system']['step2']['changes'] = [
    {
        'title': 'Kanzlei-Kategorien im Google-Profil prüfen',
        'text': 'Neben „Rechtsanwalt“ auch „Anwaltskanzlei“ und Fachkategorien ergänzen, um das Suchspektrum zu erweitern.'
    },
    {
        'title': 'Alle juristischen Fachbereiche hinterlegen',
        'text': 'Gesellschaftsrecht, M&A, Handelsrecht und Prozessführung als konkrete Leistungen im Google-Profil auflisten.'
    },
    {
        'title': 'Systematischer Aufbau von Mandantenstimmen',
        'text': 'Zufriedene Mandanten und Unternehmensklienten nach Abschluss von Verfahren gezielt um Google-Bewertungen bitten.'
    },
    {
        'title': 'Auf Bewertungen professionell antworten',
        'text': 'Jede Rezension sachlich und mandantengerecht beantworten, um Google und neuen Mandanten Aktivität zu zeigen.'
    },
    {
        'title': 'Hochwertige Kanzlei- und Teambilder',
        'text': 'Einblicke in die Kanzleiräume in der Calwer Straße und Porträts aller Partner schaffen sofortiges Vertrauen.'
    },
    {
        'title': 'Google-Beiträge zu aktuellen Urteilen',
        'text': 'Kurze rechtliche Einordnungen und Kanzlei-News direkt im Google-Eintrag veröffentlichen.'
    }
]

p['system']['step2']['cleanup'] = [
    {
        'n': '94 / 1352',
        'text': 'Verlinkende Websites weisen einen hohen Spam-Wert auf und sollten im Google Disavow-Tool entwertet werden.'
    },
    {
        'n': '0 / 5',
        'text': 'Bewertungen mit einer öffentlichen Antwort der Kanzlei.'
    }
]

p['system']['step2']['good'] = 'Das Fundament steht: Makellose 5,0 Sterne, renommierte Partner und eine klare Ausrichtung auf Gesellschaftsrecht. Mit gezielten Profil-Optimierungen lässt sich dieser Rückstand schnell aufholen.'

p['system']['step3']['score_draft_label'] = 'Ziel: 34+ / 42'
p['system']['step3']['note_today'] = 'Im ersten Bildschirm sieht man die Kanzlei-Marke, aber keinen Button zur Kontaktaufnahme und keine Bewertungen.'
p['system']['step3']['note_draft'] = 'Klarer Fokus: CONTIQ als Boutique-Kanzlei für Gesellschaftsrecht in Stuttgart, Partner-Porträts und ein direkter Button zur Mandatsanfrage.'

p['system']['step3']['five'] = [
    {
        'q': 'Was?',
        'a': '„Die Boutique-Kanzlei für Gesellschaftsrecht und Prozessführung“. Ein klares Profil, aber ohne Handlungsaufforderung.'
    },
    {
        'q': 'Wo?',
        'a': 'Stuttgart wird im ersten Bildschirm nicht genannt; die Kanzlei-Adresse steht nur im Footer.'
    },
    {
        'q': 'Warum ihr?',
        'a': 'Keine Sterne, Bewertungen oder Siegel im sichtbaren Bereich.'
    },
    {
        'q': 'Wie zur Kontaktaufnahme?',
        'a': 'Kein primärer Button. Nur Menü-Icons und Links zu offenen Stellen.'
    },
    {
        'q': 'Wer?',
        'a': 'Die Partner Stephan Brenner und Dr. Dachs werden erst weiter unten im Team-Bereich vorgestellt.'
    }
]

p['system']['step3']['strip'] = [
    {
        'photo': '/review-assets/stephan-brenner/foto-1.webp',
        'title': 'Stephan Brenner und Partner',
        'why': 'Unternehmer wollen sofort sehen, welche Partner ihre Fälle und Transaktionen persönlich führen.'
    },
    {
        'photo': '/review-assets/stephan-brenner/foto-2.webp',
        'title': 'Boutique-Beratung auf Augenhöhe',
        'why': 'Klarer Zuschnitt auf Gesellschaftsrecht statt einer unpersönlichen Großkanzlei.'
    },
    {
        'photo': '/review-assets/stephan-brenner/foto-3.webp',
        'title': 'Kanzlei in der Calwer Straße',
        'why': 'Zentrale Präsenz im Herzen von Stuttgart schafft sofortige lokale Greifbarkeit.'
    }
]

p['system']['step3']['good'] = 'Die Website wirkt hochwertig und seriös. Was fehlt, ist die direkte Führung des Mandanten zur ersten Kontaktaufnahme.'

p['calc']['val'] = 1500
p['calc']['val_label'] = 'Umsatz pro neuem Mandat (Startwert 1.500 €)'
p['calc']['volumes_line'] = 'Echte Google-Suchen pro Monat (Region Stuttgart): <b>anwalt gesellschaftsrecht stuttgart 40</b> · rechtsanwalt gesellschaftsrecht stuttgart 30. Ein Anzeigen-Klick auf diese Fachbegriffe liegt bei rund <b>3,50 US-Dollar</b> (Abruf 15.10.2026). Startwert Umsatz: vorsichtig geschätzte 1.500 € pro Neumandat. Budget, Anfrage- und Mandatsquote sind Annahmen.'

# Check card 0 (Deine Website)
p['check'][0]['rows'][0]['title'] = 'Telefonnummer direkt anrufbar'
p['check'][0]['rows'][0]['text'] = 'Die Kanzleinummer in Stuttgart ist auf Unterseiten verlinkt und direkt antippbar.'

# Check card 1 (Was Google liest)
p['check'][1]['rows'][0]['text'] = 'Die Startseite nutzt als Hauptüberschrift den Kanzleinamen CONTIQ ohne die Suchbegriffe Gesellschaftsrecht oder Stuttgart.'
p['check'][1]['rows'][1]['text'] = 'Unterseiten haben eigene Titel, doch Stuttgart fehlt häufig im Seitentitel.'
p['check'][1]['rows'][2]['text'] = 'Die heutige Meta-Beschreibung beschreibt das Team, formuliert aber kein klares Angebot für suchende Mandanten.'

# Check card 2 (Was du messen kannst)
p['check'][2]['rows'][1]['text'] = 'Strukturierte Kanzleidaten sind teilweise hinterlegt; Fachanwalts- und Standortattribute sollten geschärft werden.'

# Check card 3 (Dein Ruf im Netz)
p['check'][3]['rows'][1]['text'] = 'Mit 5 Bewertungen liegt CONTIQ hinter Stuttgarter Mitbewerbern wie LUTZ (202) oder Streich & Wittke (102).'
p['check'][3]['rows'][3]['text'] = '94 von 1.352 verlinkenden Domains weisen einen hohen Spam-Score auf und sollten entwertet werden.'

p['quick_wins'] = [
    {
        'title': 'Stuttgart und Gesellschaftsrecht in den Startseitentitel',
        'text': '„Kanzlei für Gesellschaftsrecht Stuttgart – CONTIQ Rechtsanwälte“ als klarer Seitentitel.'
    },
    {
        'title': 'Button zur Mandatsanfrage im ersten Bildschirm',
        'text': 'Einen gut sichtbaren Button „Mandat anfragen“ oder „Erstgespräch vereinbaren“ im Hero-Bereich platzieren.'
    },
    {
        'title': 'Eure 5 Sterne bei Google sichtbar machen',
        'text': 'Die makellose 5,0-Sterne-Bewertung mit Google-Logo prominent im sichtbaren Bereich einbinden.'
    },
    {
        'title': 'Google-Unternehmensprofil schärfen',
        'text': 'Alle Schwerpunkte von M&A bis Gesellschafterstreit als konkrete Leistungen im Profil hinterlegen.'
    },
    {
        'title': 'Mandantenstimmen aufbauen',
        'text': 'Bestehende Mandanten gezielt um eine Rezension bitten, um zu den Top-Kanzleien in Stuttgart aufzuschließen.'
    },
    {
        'title': 'Spam-Backlinks bereinigen',
        'text': 'Die 94 auffälligen Backlink-Quellen über die Google Search Console entwerten.'
    }
]

p['roadmap'] = [
    {
        'step': 'Woche 1–2 · Aufräumen',
        'what': 'Seitentitel bei Google schärfen, Spam-Links entwerten und Google-Unternehmensprofil vollständig ausfüllen',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Erst aufräumen, dann ausbauen'
    },
    {
        'step': 'Woche 1–3 · Telefon klingeln',
        'what': 'Kanzleieintrag ausbauen: Leistungen hinterlegen, Fotos der Kanzlei ergänzen und erste neue Bewertungen einsammeln',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Aktuell ist CONTIQ in der Stuttgarter Innenstadt auf Platz 20+ und überlässt Anfragen den Mitbewerbern'
    },
    {
        'step': 'Woche 2–4 · Startseite',
        'what': 'Erster Bildschirm mit Kanzleifokus Stuttgart, 5 Sternen, Partner-Porträts und Button zur Mandatsanfrage',
        'prio': 'Hoch',
        'effort': 'Mittel',
        'why': 'Aus interessierten Unternehmern werden Erstgespräche'
    },
    {
        'step': 'Woche 3–8 · Neue Inhalte',
        'what': 'Gezielte Landingpages für Gesellschaftsrecht, M&A und Gesellschafterstreit im Wirtschaftsraum Stuttgart',
        'prio': 'Hoch',
        'effort': 'Mittel',
        'why': 'Seiten für die konkreten Suchanfragen, die Mandanten bei Google stellen'
    },
    {
        'step': 'Laufend · Messen',
        'what': 'Entwicklung der Mandatsanfragen, Klicks aus der Google-Karte und monatliche Ranking-Messung verfolgen',
        'prio': 'Mittel',
        'effort': 'Gering',
        'why': 'Jede Optimierung muss zu messbaren neuen Mandaten führen'
    }
]

p['proof'] = {
    'h2': 'Andere Kanzleien und Berater hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'lead': 'Ausgewählt nach eurer Kanzleigröße und Ausrichtung: Wirtschaftskanzleien und spezialisierte Berater, die lokal zur führenden Adresse wurden.',
    'featured': [
        'lengauer',
        'schlirf',
        'laserstein',
        'abel'
    ],
    'labels': {
        'lengauer': 'Wirtschaftsberatung, vorher:'
    },
    'more': [
        'mediaberater',
        'menge',
        'irmscher',
        'everitt',
        'kuch'
    ],
    'first_featured': False
}

p['final'] = {
    'h2': 'Lass uns in 30 Minuten anschauen, wer in Stuttgart oben steht und wie CONTIQ dorthin kommt.',
    'p': '30 Minuten, kostenlos: Ich zeige euch live die Stuttgarter Mitbewerber und welche Schritte für eure Kanzlei die meiste Hebelwirkung haben. Unverbindlich.',
    'subject': 'CONTIQ%20Rechtsanw%C3%A4lte%20Sichtbarkeits-Analyse'
}

p['guide'] = {
    'hello': 'Ich habe mir contiq.de und euren Google-Eintrag genau angesehen. Hier zeige ich dir, was ich gefunden habe.',
    'point': 'LUTZ Rechtsanwälte hält fast 98 % der Karte. Eure Kanzlei steht trotz 5,0 Sternen an keinem Messpunkt unter den Top 3.',
    'think': 'Im Gesellschaftsrecht zählt Vertrauen und Spezialisierung. Wer in Stuttgart sucht, sollte CONTIQ direkt ganz oben finden.',
    'insight': 'Der größte Hebel: Die Kanzlei-Startseite klar auf Mandatsanfragen ausrichten und den Google-Eintrag systematisch mit Bewertungen ausbauen.',
    'celebrate': 'Mit einer klaren Struktur und aktiver lokaler Präsenz lässt sich der Vorsprung der Mitbewerber Schritt für Schritt aufholen.'
}

p['headlines'] = {
    'hero_h1': 'Stephan, so finden Mandanten <span style="color:var(--brand--lemon);">in Stuttgart</span> eure Kanzlei.<span style="display:block;font-size:.42em;line-height:1.35;font-weight:600;letter-spacing:0;color:#5c5c5c;margin-top:16px;">Bei „anwalt gesellschaftsrecht stuttgart“ steht CONTIQ an 0 von 49 Punkten unter den Top 3. Hier ist euer Fahrplan.</span>',
    'hero_sub': 'Ihr habt 5,0 Sterne bei Google. Bei der Suche „anwalt gesellschaftsrecht stuttgart“ ist die Kanzlei jedoch an keinem der 49 Messpunkte unter den ersten drei zu sehen.',
    'grid_h2': 'Unter den ersten drei an 0 von 49 Punkten. Im gesamten Stadtgebiet nicht unter den Top 3.',
    'proof_h2': 'Andere Kanzleien und Berater hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'system_h2': 'Drei Hebel für mehr Mandate, und bei jedem fehlt heute ein Schritt',
    'step1_h2': 'Für gesellschaftsrechtliche Beratung suchen Mandanten gezielt nach Fachanwälten in Stuttgart.',
    'step2_h2': 'LUTZ Rechtsanwälte führt mit 98 % Sichtbarkeit. CONTIQ erreicht 0 %.',
    'step3_h2': 'Besucher entscheiden in 5 Sekunden. Eure Startseite bietet heute keinen direkten Kontakt-Button.',
    'calc_h2': 'Was neue gesellschaftsrechtliche Mandate für eure Kanzlei bedeuten',
    'check_h2': 'Was eure Website heute richtig macht und wo ihr potenzielle Mandanten verliert',
    'quickwins_h2': 'Sechs Schritte, die ihr schon nächste Woche umsetzen könnt, ohne neue Website',
    'roadmap_h2': 'Euer Plan für die nächsten 8 Wochen, Schritt für Schritt',
    'final_h2': 'Lass uns in 30 Minuten anschauen, wer in Stuttgart oben steht und wie CONTIQ dorthin kommt.'
}

p['sources']['grid'] = 'evidence/falcon-report-da6ceb86d5e2406.json (keyword anwalt gesellschaftsrecht stuttgart, 7x7, 5.0 km, centre 48.7757/9.1712, 16.10.2026; solv 0.00 = 0/49, found_in 1) + review-assets/stephan-brenner/scan-grid.webp'
p['sources']['calc'] = 'evidence/dfs-volumes-ads.json (volume anwalt gesellschaftsrecht stuttgart 40, cpc 3.50); val 1500 = Wirtschaftsmandat / Erstberatungspaket Annahme; budget/conv/deal = assumptions, labelled'

with open(pfile, 'w', encoding='utf-8') as f:
    json.dump(p, f, indent=2, ensure_ascii=False)

print('Updated Stephan Brenner prospect.json successfully!')
