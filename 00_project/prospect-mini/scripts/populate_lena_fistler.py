#!/usr/bin/env python3
import json, os

pfile = '00_project/prospects/lena-fistler/prospect.json'
with open(pfile, 'r', encoding='utf-8') as f:
    p = json.load(f)

p['business_ref'] = 'deine Praxis'
p['branch'] = 'health'

p['hero']['sub'] = 'Du hast 5,0 Sterne bei Google. Bei der Suche „körpertherapie münchen“ ist deine Praxis an 5 von 49 Punkten unter den ersten drei, an 14 Punkten aber nicht unter den ersten 20.'
p['hero']['cards'][0]['sub'] = 'Heilpraktikerin · Ganzheitliche Körpertherapie & Craniosacral · München'
p['hero']['cards'][1]['badge'] = 'Außerhalb von Neuhausen oft nicht unter den Top 3'
p['hero']['cards'][2]['sub'] = 'Du: 2 Bewertungen · Martin Rosenauer: 35 Bewertungen'
p['hero']['cards'][3]['sub'] = 'Erster Bildschirm: Kein Gesicht, kein Ort München sichtbar, kein Sterne-Siegel'
p['hero']['cards'][3]['badge'] = 'Startseite heute: 13 von 44 Punkten'

p['grid']['h2'] = 'Unter den ersten drei an 5 von 49 Punkten. Außerhalb von Neuhausen kaum sichtbar.'
p['grid']['caption_today'] = '<b>Unter den ersten drei an 5 von 49 Punkten.</b> Rund um deine Praxis in Neuhausen-Nymphenburg bist du gut platziert. Im Zentrum und Osten stehst du auf Platz 20+. Martin Rosenauer führt die Karte mit 8,2 % Sichtbarkeit an.'
p['grid']['caption_goal'] = '<b>Ziel: Sichtbarkeit in ganz München für Klienten, die nach Körpertherapie suchen.</b> Die Praxen vorn haben 1 bis 49 Bewertungen.'
p['grid']['chips'] = [
    '📞 Direkte Terminanfragen aus der Google-Karte',
    '🧭 Klienten aus ganz München finden deine Praxis',
    '🤝 Mehr Buchungen für Craniosacral- & Körpertherapie'
]

p['system']['intro'] = 'Für deine Praxis haben wir drei Hebel geprüft: wonach Menschen in München suchen, warum andere Praxen in der Karte vorn stehen und ob deine Website Besucher zu Terminen macht. Jede Zahl stammt aus echten Messungen.'
p['system']['steps'][2]['kpi'] = 'heute 13 von 44 Punkten'

p['system']['step1']['h2'] = 'Nach „körpertherapie münchen“ wird 110-mal im Monat gesucht. Deine Website steht dafür nicht unter den ersten 20 Treffern.'
p['system']['step1']['lead'] = 'Wir haben lenafistler.de mit den Websites verglichen, die bei „körpertherapie münchen“ oben stehen, und mit den Begriffen, die Patienten in München wirklich suchen.'
p['system']['step1']['demand_note'] = '„körpertherapie münchen“ hat 110 Suchen pro Monat. Für Schwerpunkte wie „craniosacral therapie münchen“ (90 Suchen) gibt es weitere Nachfrage, die deine Seite gezielt abholen kann.'

p['system']['step1']['depth']['title'] = 'Wenig Text auf der Startseite und München fehlt in den wichtigsten Überschriften.'
p['system']['step1']['depth']['sub'] = 'Deine Startseite hat 253 Wörter. Der Begriff „Körpertherapie“ oder „München“ taucht in deiner Hauptüberschrift gar nicht auf.'
p['system']['step1']['depth']['note'] = 'In deiner Hauptüberschrift steht „Hin zu Balance und Aufrichtung“, aber weder dein Therapieschwerpunkt noch der Standort München.'

p['system']['step1']['items'] = [
    {
        'title': 'Startseite auf Körpertherapie in München ausrichten',
        'tag': 'Ort',
        'why': 'Deine Startseite nennt heute weder Körpertherapie noch München im sichtbaren Kopfbereich.'
    },
    {
        'title': 'Eigene Seite zu Craniosacraler Therapie München',
        'tag': 'Leistung',
        'why': '„craniosacral therapie münchen“ hat 90 Suchen pro Monat. Eine fokussierte Leistungsseite holt gezielt Klienten ab.'
    },
    {
        'title': 'Eigene Seite zu Kinesiologischem Taping München',
        'tag': 'Leistung',
        'why': 'Taping ist ein Schwerpunkt deiner Praxis, für den eine eigene Seite mit lokalem Bezug neue Anfragen bringt.'
    },
    {
        'title': 'Eigene Seite zu Skoliosebehandlung München',
        'tag': 'Leistung',
        'why': '„skoliosebehandlung münchen“ hat 10 Suchen pro Monat. Ein wichtiges Spezialgebiet deiner therapeutischen Arbeit.'
    },
    {
        'title': 'Eigene Seite zu Kiefer R.E.S.E.T. München',
        'tag': 'Leistung',
        'why': 'Kieferentspannung bei Zähneknirschen und Stress ist ein konkreter Anlass, nach dem Betroffene suchen.'
    },
    {
        'title': 'Klares Therapeutenprofil mit Praxis-Einblick',
        'tag': 'Profil',
        'why': 'Patienten wollen sofort sehen, wer sie behandelt, welche Ausbildung du mitbringst und wie die Praxisräume wirken.'
    }
]

p['system']['step2']['h2'] = 'Der Markt in München ist offen. Selbst die führende Praxis erreicht nur 8,2 % der Karte.'
p['system']['step2']['meaning'] = 'Die Praxen an der Spitze haben zwischen 1 und 49 Bewertungen. Dein Profil steht mit 5,0 Sternen und 2 Bewertungen bereits gut da, ist bei Google aber noch nicht als Unternehmen bestätigt.'

for row in p['system']['step2']['table']:
    if 'Hypnotherapy service' in row.get('cats', ''):
        row['cats'] = row['cats'].replace('Hypnotherapy service', 'Hypnosetherapie')
    if 'Physiatrist' in row.get('cats', ''):
        row['cats'] = row['cats'].replace('Physiatrist', 'Physikalische Therapie')

p['system']['step2']['changes'] = [
    {
        'title': 'Google-Unternehmensprofil bestätigen (Claiming)',
        'text': 'Dein Eintrag ist bei Google noch nicht als Inhaber bestätigt. Die Bestätigung schützt dein Profil und schaltet alle Funktionen frei.'
    },
    {
        'title': 'Kategorien und Leistungen vollständig hinterlegen',
        'text': 'Neben „Naturheilpraktiker“ und „Craniosacral therapy“ auch Körpertherapie und manuelle Verfahren eintragen.'
    },
    {
        'title': 'Systematisch Patientenstimmen aufbauen',
        'text': 'Zufriedene Klienten nach erfolgreicher Begleitung um eine Google-Bewertung bitten, um von 2 auf 10+ Bewertungen aufzuschließen.'
    },
    {
        'title': 'Auf jede Bewertung persönlich antworten',
        'text': 'Jede Rezension freundlich und professionell beantworten. Das signalisiert Google Aktivität und schafft Vertrauen.'
    },
    {
        'title': 'Praxisfotos und Porträt hochladen',
        'text': 'Fotos deiner Behandlungsräume in der Nymphenburger Straße und dein Porträt machen die Praxis sofort greifbar.'
    },
    {
        'title': 'Google-Beiträge zu Behandlungsmethoden',
        'text': 'Regelmäßige kurze Praxiseinblicke zu Craniosacraler Therapie oder Haltungskorrektur direkt im Google-Eintrag teilen.'
    }
]

p['system']['step2']['cleanup'] = [
    {
        'n': '0 / 1',
        'text': 'Websites, die auf deine Seite verlinken, sind unauffällig. Es liegen keine schädlichen Spam-Verlinkungen vor.'
    },
    {
        'n': '0 / 2',
        'text': 'Bewertungen mit einer Antwort von dir.'
    }
]

p['system']['step2']['good'] = 'Die Ausgangslage ist hervorragend: Niemand dominiert den Münchner Markt, und du hast bereits 5,0 Sterne. Mit einem bestätigten Profil und ein paar Bewertungen kannst du schnell ganz nach vorn kommen.'

p['system']['step3']['score_draft_label'] = 'Ziel: 36 / 44'
p['system']['step3']['note_today'] = 'Im ersten Bildschirm sieht man den Text „Hin zu Balance und Aufrichtung“, aber kein Foto von dir, keinen Ort München und keine Sterne-Bewertung.'
p['system']['step3']['note_draft'] = 'Klarer Fokus: Dein Porträt, „Ganzheitliche Körpertherapie in München“, 5 Google-Sterne, Verbands-Siegel und ein direkter Button zur Terminbuchung.'

p['system']['step3']['five'] = [
    {
        'q': 'Was?',
        'a': '„Hin zu Balance und Aufrichtung“. Der Begriff Körpertherapie steht nur klein im Logo-Schriftzug.'
    },
    {
        'q': 'Wo?',
        'a': 'München wird im ersten Bildschirm nirgends genannt; die Praxis-Adresse steht erst im Footer.'
    },
    {
        'q': 'Warum du?',
        'a': 'Keine Sterne, Bewertungen oder Ausbildungs-Zertifikate im sichtbaren ersten Bildschirm.'
    },
    {
        'q': 'Wie zum Termin?',
        'a': 'Ein Button „Termin buchen“ ist vorhanden, führt zu Zeeg, hat aber keine beruhigenden Hinweise.'
    },
    {
        'q': 'Wer?',
        'a': 'Kein Porträtfoto von Lena Fistler im sichtbaren Bereich; Patienten sehen nicht, wer sie behandelt.'
    }
]

p['system']['step3']['strip'] = [
    {
        'photo': '/review-assets/lena-fistler/foto-1.webp',
        'title': 'Lena Fistler persönlich',
        'why': 'Patienten fassen Vertrauen, wenn sie die Therapeutin vor dem ersten Termin sehen.'
    },
    {
        'photo': '/review-assets/lena-fistler/foto-2.webp',
        'title': 'Achtsame Behandlung',
        'why': 'Echte Einblicke in die Körpertherapie und Craniosacral-Behandlung zeigen die Praxisatmosphäre.'
    },
    {
        'photo': '/review-assets/lena-fistler/foto-3.webp',
        'title': 'Praxis in der Nymphenburger Straße',
        'why': 'Ein ansprechender Behandlungsraum in Neuhausen schafft Ruhe und Sicherheit.'
    }
]

p['system']['step3']['good'] = 'Deine Website wirkt warm und einladend. Mit einem klareren ersten Bildschirm und einer eindeutigen Orientierung werden deutlich mehr Besucher direkt einen Termin buchen.'

p['calc']['val'] = 100
p['calc']['val_label'] = 'Umsatz pro Behandlungstermin (Startwert 100 €)'
p['calc']['volumes_line'] = 'Echte Google-Suchen pro Monat (ganz Deutschland, Mittel der letzten 12 Monate): <b>körpertherapie münchen 110</b> · craniosacral therapie münchen 90. Ein Anzeigen-Klick auf „körpertherapie münchen“ kostet bei Google rund <b>1,52 US-Dollar</b> (Google-Angabe in Dollar; der Regler startet ohne Umrechnung bei 1,50 €) (Abruf 15.10.2026). Startwert Behandlung: 100 € (orientiert an den 99 € auf deiner Website). Budget, Anfrage- und Buchungsanteil sind Annahmen.'

# Check card 0 (Deine Website)
p['check'][0]['rows'][0]['text'] = 'Auf der Startseite ist deine Handynummer direkt verlinkt. Auf der Kontaktseite steht sie als Text ohne Link.'

# Check card 1 (Was Google liest)
p['check'][1]['rows'][0]['text'] = 'Die Hauptüberschrift lautet heute „Hin zu Balance und Aufrichtung“ ohne die Suchbegriffe Körpertherapie oder München.'
p['check'][1]['rows'][1]['text'] = '15 von 17 Unterseiten haben keine Hauptüberschrift (nur Datenschutz und Impressum nutzen ein H1-Tag).'
p['check'][1]['rows'][2]['text'] = 'Die heutige Google-Beschreibung („Begleitung bei Rückenschmerzen und Stress...“) ist gut, lässt sich aber noch präziser auf Suchbegriffe schärfen.'

# Check card 2 (Was du messen kannst)
p['check'][2]['rows'][1]['text'] = 'Im Datenblock für Google steht auf 14 Seiten noch die Augustenstraße statt deiner Praxisadresse Nymphenburger Straße 166.'

# Check card 3 (Dein Ruf im Netz)
p['check'][3]['rows'][1]['text'] = 'Mit 2 Bewertungen stehst du am Anfang. Martin Rosenauer hat 35 Bewertungen, Spiritual Touch hat 49.'
p['check'][3]['rows'][3]['text'] = 'Aktuell gibt es 1 verlinkende Website ohne bedenkliche Spam-Werte.'
p['check'][3]['rows'][4]['text'] = 'Auf deiner Website werden gesundheitliche Themen sachlich beschrieben. Hinweise zur wissenschaftlichen Anerkennung sind vorhanden.'

p['quick_wins'] = [
    {
        'title': 'Praxisadresse im Code korrigieren',
        'text': 'Auf 14 Seiten steht im Google-Code noch die Augustenstraße. Schnell auf Nymphenburger Straße 166 aktualisieren.'
    },
    {
        'title': 'Google-Unternehmensprofil bestätigen',
        'text': 'Das Google-Profil als Inhaberin beanspruchen, um volle Kontrolle und Sichtbarkeit zu erhalten.'
    },
    {
        'title': 'München und Körpertherapie in die Startzeile',
        'text': '„Ganzheitliche Körpertherapie München – Lena Fistler“ als Hauptüberschrift und Seitentitel hinterlegen.'
    },
    {
        'title': 'Foto und 5 Google-Sterne nach oben holen',
        'text': 'Dein Porträtfoto und die 5,0 Sterne direkt im ersten Bildschirm platzieren, damit Besucher sofort Vertrauen fassen.'
    },
    {
        'title': 'Telefonnummer auf der Kontaktseite verlinken',
        'text': 'Die Telefonnummer auf der Kontaktseite als anklickbaren Link anlegen, damit mobile Besucher direkt anrufen können.'
    },
    {
        'title': 'Zufriedene Klienten um Bewertungen bitten',
        'text': 'Bestehende Klienten gezielt um eine kurze Rezension bitten, um bei Google von 2 auf 10+ Bewertungen zu wachsen.'
    }
]

p['roadmap'] = [
    {
        'step': 'Woche 1–2 · Aufräumen',
        'what': 'Adresse im Website-Code korrigieren, Google-Profil beanspruchen und Telefon-Link auf der Kontaktseite reparieren',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Erst aufräumen, dann ausbauen'
    },
    {
        'step': 'Woche 1–3 · Telefon klingeln',
        'what': 'Google-Eintrag vervollständigen: Leistungen eintragen, Praxisfotos ergänzen und erste neue Bewertungen einholen',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Aktuell bist du im Zentrum Münchens auf Platz 20+ und verschenkst Anfragen an Mitbewerber'
    },
    {
        'step': 'Woche 2–4 · Startseite',
        'what': 'Erster Bildschirm mit Porträt, Standort München, 5 Sternen und klarem Termin-Button',
        'prio': 'Hoch',
        'effort': 'Mittel',
        'why': 'Aus Besuchern werden gebuchte Behandlungstermine'
    },
    {
        'step': 'Woche 3–8 · Neue Inhalte',
        'what': 'Fokussierte Seiten für Craniosacrale Therapie München, Taping und Skoliosebehandlung',
        'prio': 'Hoch',
        'effort': 'Mittel',
        'why': 'Seiten für die Themen, die Patienten wirklich googeln'
    },
    {
        'step': 'Laufend · Messen',
        'what': 'Besucher, Anrufe und Anfragen plus monatliche Kartenmessung',
        'prio': 'Mittel',
        'effort': 'Gering',
        'why': 'Jede Maßnahme muss sich in Zahlen zeigen'
    }
]

p['proof'] = {
    'h2': 'Andere Praxen und Berater hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'lead': 'Ausgewählt nach deiner Praxisgröße und Fachrichtung: Ganzheitliche Praxen und Therapeuten, die lokal zur führenden Adresse wurden.',
    'featured': [
        'schlirf',
        'laserstein',
        'abel',
        'lengauer'
    ],
    'labels': {},
    'more': [
        'menge',
        'irmscher',
        'everitt',
        'kuch',
        'kraft'
    ]
}

p['final'] = {
    'h2': 'Lass uns in 30 Minuten anschauen, wer in München oben steht und wie deine Praxis dorthin kommt.',
    'p': '30 Minuten, kostenlos: Ich zeige dir live, wer in München vorn steht und welche Hebel für deine Praxis am schnellsten Termine bringen. Unverbindlich.',
    'subject': 'Praxis%20f%C3%BCr%20ganzheitliche%20K%C3%B6rpertherapie%20Sichtbarkeits-Analyse'
}

p['guide'] = {
    'hello': 'Ich habe mir lenafistler.de und deinen Google-Eintrag genau angesehen. Hier zeige ich dir, was ich gefunden habe.',
    'point': 'Der Münchner Markt ist komplett offen: Selbst der Spitzenreiter hat nur 8,2 % Sichtbarkeit. Deine Praxis steht an 5 von 49 Punkten unter den Top 3.',
    'think': 'In der Körpertherapie zählen Vertrauen und Nähe. Wer in München nach Begleitung sucht, sollte deine Praxis sofort finden.',
    'insight': 'Der größte Hebel: Dein Google-Profil offiziell bestätigen, die veraltete Adresse im Code korrigieren und deine 5 Sterne oben zeigen.',
    'celebrate': 'Mit wenigen gezielten Schritten kannst du in ganz München zur ersten Anlaufstelle für Körpertherapie werden.'
}

p['headlines'] = {
    'hero_h1': 'Lena, so finden Patienten <span style="color:var(--brand--lemon);">in München</span> deine Praxis.<span style="display:block;font-size:.42em;line-height:1.35;font-weight:600;letter-spacing:0;color:#5c5c5c;margin-top:16px;">Bei „körpertherapie münchen“ steht deine Praxis an 5 von 49 Punkten unter den Top 3. Hier ist dein Fahrplan.</span>',
    'hero_sub': 'Du hast 5,0 Sterne bei Google. Bei der Suche „körpertherapie münchen“ ist deine Praxis an 5 von 49 Punkten unter den ersten drei, an 14 Punkten aber nicht unter den ersten 20.',
    'grid_h2': 'Unter den ersten drei an 5 von 49 Punkten. Außerhalb von Neuhausen kaum sichtbar.',
    'proof_h2': 'Andere Praxen und Berater hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'system_h2': 'Drei Hebel für mehr Patienten, und bei jedem fehlt heute ein Schritt',
    'step1_h2': 'Nach „körpertherapie münchen“ wird 110-mal im Monat gesucht. Deine Website steht dafür nicht unter den Top 20.',
    'step2_h2': 'Der Markt in München ist offen. Selbst die führende Praxis erreicht nur 8,2 % der Karte.',
    'step3_h2': 'Besucher entscheiden in 5 Sekunden. Deine Startseite zeigt heute kein Gesicht und keinen Standort.',
    'calc_h2': 'Was neue Patienten für deine Praxis bedeuten',
    'check_h2': 'Was deine Website heute richtig macht und wo du Termine verlierst',
    'quickwins_h2': 'Sechs Schritte, die du schon nächste Woche umsetzen kannst, ohne neue Website',
    'roadmap_h2': 'Dein Plan für die nächsten 8 Wochen, Schritt für Schritt',
    'final_h2': 'Lass uns in 30 Minuten anschauen, wer in München oben steht und wie deine Praxis dorthin kommt.'
}

p['sources']['grid'] = 'evidence/falcon-report-4fe389eb4e0685a.json (keyword körpertherapie münchen, 7x7, 5.0 km, centre 48.1536149/11.5312987, 16.10.2026; solv 10.2 = 5/49, found_in 35) + review-assets/lena-fistler/scan-grid.webp'
p['sources']['calc'] = 'evidence/dfs-volumes-ads.json (volume körpertherapie münchen 110, cpc 1.52 -> slider 1.5); val: 100 aus Preis-Seite (Termin 99 €); budget/conv/deal = assumptions, labelled'

with open(pfile, 'w', encoding='utf-8') as f:
    json.dump(p, f, indent=2, ensure_ascii=False)

print('Updated Lena Fistler prospect.json successfully!')
