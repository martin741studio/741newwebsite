#!/usr/bin/env python3
import json, os

pfile = '00_project/prospects/gabriele-heckel/prospect.json'
with open(pfile, 'r', encoding='utf-8') as f:
    p = json.load(f)

p['business_ref'] = 'deine Praxis'
p['branch'] = 'health'
p['first_name'] = 'Gabriele'
p['display_name'] = 'Gabriele Heckel'
p['company'] = 'Gabriele Heckel Psychotherapeutische Praxis'

p['hero']['sub'] = 'Dein Google-Profil hat 0 Bewertungen. Bei der regionalen Suche „heilpraktiker amberg“ ist deine Praxis an keinem der 49 Punkte sichtbar – während Amberger Kollegen bis zu 73 % der Karte belegen.'
p['hero']['cards'][0]['sub'] = 'Psychotherapie (HPG) · Coaching · Hirschau & Amberg'
p['hero']['cards'][0]['badge'] = '0 Bewertungen'
p['hero']['cards'][1]['badge'] = 'An allen 49 Punkten nicht unter den Top 20'
p['hero']['cards'][2]['sub'] = 'Du: 0 Bewertungen · energy in balance: 9 Bewertungen'
p['hero']['cards'][2]['badge'] = 'Keine Antworten'
p['hero']['cards'][3]['sub'] = 'Erster Bildschirm: „Herzlich willkommen!“, Telefonnummer nicht anklickbar'
p['hero']['cards'][3]['badge'] = 'Startseite heute: ausbaufähig'

p['grid']['h2'] = 'Unter den ersten drei an 0 von 49 Punkten. Im Raum Amberg nicht sichtbar.'
p['grid']['caption_today'] = '<b>Unter den ersten drei an 0 von 49 Punkten (0,00 % Sichtbarkeit).</b> Bei der Suche nach „heilpraktiker amberg“ taucht deine Praxis an keinem der 49 Messpunkte unter den Top 20 auf. Kollegen wie „energy in balance“ erreichen bis zu 73,47 % Sichtbarkeit.'
p['grid']['caption_goal'] = '<b>Ziel: Gezielte Präsenz im regionalen Zentrum Amberg und Hirschau.</b> Die führenden Praxen vorn haben lediglich 2 bis 19 Bewertungen.'
p['grid']['chips'] = [
    '📞 Direkte Terminanfragen aus Amberg und dem Landkreis',
    '🧭 Klienten aus Hirschau und Amberg finden dich sofort',
    '🤝 Mehr Anfragen für Psychotherapie (HPG) und Coaching'
]

p['system']['intro'] = 'Für deine Praxis haben wir drei Hebel geprüft: wonach Hilfesuchende in der Region Amberg suchen, warum Mitbewerber in der Karte vorn stehen und wie deine Website Besucher zu Erstterminen macht.'
p['system']['steps'][0]['kpi'] = '210 Suchen/Monat'
p['system']['steps'][1]['kpi'] = '0 von 49 Punkten'
p['system']['steps'][2]['kpi'] = 'Telefon nicht klickbar'

p['system']['step1']['h2'] = 'Nach „heilpraktiker amberg“ wird 210-mal im Monat gesucht. Deine Website taucht dafür nicht auf.'
p['system']['step1']['lead'] = 'Wir haben heilpraxis-heckel.de mit den Websites verglichen, die bei „heilpraktiker amberg“ oben stehen, und mit den Begriffen, die Menschen in der Oberpfalz wirklich suchen.'
p['system']['step1']['demand_note'] = 'Im regionalen Zentrum Amberg suchen jeden Monat 210 Menschen nach einem Heilpraktiker. Deine Praxis in Hirschau liegt nur 13 Kilometer entfernt – ein kurzer Weg für qualifizierte Hilfe.'

p['system']['step1']['depth']['title'] = 'Die Hauptüberschrift lautet „Herzlich willkommen!“ ohne Leistung und Ort.'
p['system']['step1']['depth']['sub'] = 'Google und neue Besucher erfassen in den ersten 5 Sekunden nicht, welche psychotherapeutische Unterstützung du in Hirschau und Amberg anbietest.'
p['system']['step1']['depth']['note'] = 'Weder auf der Startseite noch auf der Psychotherapie-Seite wird der regionale Bezug zu Hirschau und Amberg in den Hauptüberschriften verknüpft.'

p['system']['step1']['items'] = [
    {
        'title': 'Startseite auf Psychotherapie & Coaching Hirschau / Amberg ausrichten',
        'tag': 'Ort',
        'why': 'Heute lautet die Hauptüberschrift „Herzlich willkommen!“ ohne jeden Hinweis auf dein Angebot oder die Region.'
    },
    {
        'title': 'Eigene Leistungsseite für Heilpraktikerin für Psychotherapie Amberg',
        'tag': 'Leistung',
        'why': '„heilpraktiker amberg“ hat 210 Suchen pro Monat. Eine gezielte Landingpage holt Klienten aus dem Einzugsgebiet ab.'
    },
    {
        'title': 'Eigene Leistungsseite für Coaching & Lebensenergie',
        'tag': 'Leistung',
        'why': 'Coaching für mehr Lebensenergie ist dein Herzstück. Eine klare Seite erklärt Methode, Ablauf und Termine.'
    },
    {
        'title': 'Eigene Leistungsseite für Heilsame Berührungen & Entspannung',
        'tag': 'Leistung',
        'why': 'Körperorientierte Methoden brauchen Vertrauen und einen klaren Einblick in die Praxisatmosphäre.'
    },
    {
        'title': 'Anfahrtsbeschreibung aus Amberg, Hirschau & Weiden',
        'tag': 'Ort',
        'why': 'Hilfesuchende aus Amberg wollen sehen, dass die Praxis in Hirschau in nur 15 Minuten bequem erreichbar ist.'
    },
    {
        'title': 'Transparenter Ablauf für das Erstgespräch',
        'tag': 'Profil',
        'why': 'Viele Menschen zögern vor dem ersten Schritt: Eine klare Erklärung der ersten 45 Minuten nimmt Hemmschwellen.'
    }
]

p['system']['step2']['h2'] = 'energy in balance führt mit 73 % der Karte. Dein Profil hat noch 0 Bewertungen.'
p['system']['step2']['meaning'] = 'Die führenden Praxen in der Region Amberg haben zwischen 2 und 19 Bewertungen. Mit 0 Bewertungen und ohne hinterlegte Leistungsattribute wird deine Praxis im Amberger Raum aktuell gar nicht gelistet.'

for row in p['system']['step2']['table']:
    if 'Alternative medicine practitioner' in row.get('cats', ''):
        row['cats'] = row['cats'].replace('Alternative medicine practitioner', 'Alternativmediziner')
    if 'Acupuncturist' in row.get('cats', ''):
        row['cats'] = row['cats'].replace('Acupuncturist', 'Akupunkteur')

p['system']['step2']['changes'] = [
    {
        'title': 'Kategorien im Google-Profil schärfen',
        'text': 'Aktuell ist nur „Psychologischer Berater“ eingetragen. Heilpraktiker für Psychotherapie und ergänzende Kategorien stärken die Relevanz.'
    },
    {
        'title': 'Einzugsgebiet Amberg im Profil hinterlegen',
        'text': 'Amberg und den Landkreis Amberg-Sulzbach als festes Einzugsgebiet in Google Maps definieren.'
    },
    {
        'title': 'Erste 3–5 Bewertungen von zufriedenen Klienten einholen',
        'text': 'Mitbewerber wie Martina Braun-Zweck führen bereits mit nur 2 Bewertungen. Mit wenigen Rezensionen ziehst du gleich.'
    },
    {
        'title': 'Telefonnummer als klickbaren Link hinterlegen',
        'text': 'Die Festnetznummer 09622 70 31 90 sowohl im Profil als auch auf der Website für Mobilnutzer direkt antippbar machen.'
    },
    {
        'title': 'Praxisfotos in Hirschau hochladen',
        'text': 'Ruhige, helle Aufnahmen des Behandlungsraums schaffen sofortige Sicherheit vor der ersten Kontaktaufnahme.'
    },
    {
        'title': 'Unseriöse Backlinks bereinigen',
        'text': '21 verlinkende Spam-Websites per Disavow-Meldung neutralisieren, um dein Google-Vertrauen zu schützen.'
    }
]

p['system']['step2']['cleanup'] = [
    {
        'n': '21 / 51',
        'text': 'Websites, die auf dich verlinken, haben bedenkliche Spam-Werte und sollten neutralisiert werden.'
    },
    {
        'n': '0 / 0',
        'text': 'Bewertungen im Google-Profil vorhanden.'
    }
]

p['system']['step2']['good'] = 'Dein Fundament ist sympathisch und warmherzig: Langjährige Praxiserfahrung, fundierte Vita und ein klarer Coaching-Ansatz. Mit regionaler Ausrichtung auf Amberg kannst du schnell viele neue Klienten erreichen.'

p['system']['step3']['score_draft_label'] = 'Ziel: 36 / 44'
p['system']['step3']['note_today'] = 'Heute: Die Startseite begrüßt mit „Herzlich willkommen!“. Die Telefonnummer ist nur als normaler Text hinterlegt und nicht mit einem Klick wählbar.'
p['system']['step3']['note_draft'] = 'Der Entwurf: Klares Porträt, Überschrift „Ihre Heilpraktikerin für Psychotherapie in Hirschau & Amberg“, Schwerpunkte und direkter Ersttermin-Button.'

p['system']['step3']['five'] = [
    {
        'q': 'Was?',
        'a': 'Heute steht dort „Herzlich willkommen!“. Der Entwurf zeigt sofort: Psychotherapie nach Heilpraktikergesetz, Coaching und Heilsame Berührungen.'
    },
    {
        'q': 'Wo?',
        'a': 'Im ersten Bildschirm wird heute kein Ort genannt. Der Entwurf nennt prominent Hirschau, Amberg und die Oberpfalz.'
    },
    {
        'q': 'Warum du?',
        'a': 'Aktuell keine Auszeichnungen oder Praxisvorteile im ersten Blick. Der Entwurf hebt deine ruhige Einzelpraxis und persönliche Begleitung hervor.'
    },
    {
        'q': 'Wie zum Termin?',
        'a': 'Heute muss man ins Menü auf /kontakt/ navigieren. Der Entwurf bietet klare Terminknöpfe und eine antippbare Telefonnummer.'
    },
    {
        'q': 'Wer?',
        'a': 'Das Porträt von Gabriele Heckel ist heute erst nach Scrollen sichtbar. Der Entwurf stellt dich sofort persönlich vor.'
    }
]

p['system']['step3']['strip'] = [
    {
        'photo': '/review-assets/gabriele-heckel/foto-1.webp',
        'title': 'Gabriele Heckel persönlich',
        'why': 'Klienten fassen Vertrauen, wenn sie die Therapeutin vor der ersten Kontaktaufnahme sympathisch sehen.'
    },
    {
        'photo': '/review-assets/gabriele-heckel/foto-2.webp',
        'title': 'Ruhige Praxisatmosphäre',
        'why': 'Ein geschützter Raum in Hirschau für vertrauliche Therapie- und Coaching-Gespräche.'
    },
    {
        'photo': '/review-assets/gabriele-heckel/foto-3.webp',
        'title': 'Ganzheitliche Begleitung',
        'why': 'Verbindung von psychotherapeutischer Gesprächsführung, Energiecoaching und heilsamen Berührungen.'
    }
]

p['system']['step3']['good'] = 'Deine Website strahlt viel Ruhe und Empathie aus. Mit einem klareren Einstieg und regionalem Fokus auf Amberg trauen sich deutlich mehr Ratsuchende zum ersten Schritt.'

p['calc']['val'] = 100
p['calc']['val_label'] = 'Umsatz pro Behandlung / Sitzung (Startwert 100 €)'
p['calc']['volumes_line'] = 'Google-Suchen pro Monat (Region Amberg / Oberpfalz): <b>heilpraktiker amberg 210</b> · heilpraktiker weiden 140 · psychologische beratung 90. Startwert Sitzung: 100 € (orientiert an deinen Stundensätzen von 70 € für Psychotherapie und 60 € für Energiecoaching). Budget, Anfrage- und Buchungsanteil sind Annahmen.'

p['check'][0]['rows'][0]['text'] = 'Auf der Website ist deine Telefonnummer 09622 70 31 90 als Text gesetzt, aber auf Smartphones nicht direkt mit einem Fingertipp anrufbar.'
p['check'][0]['rows'][1]['text'] = 'Deine Website ist vollständig mit SSL-Verschlüsselung abgesichert.'
p['check'][0]['rows'][2]['text'] = 'Die Ladezeit liegt bei rund 1,1 Sekunden; für Mobilgeräte empfehlen sich noch kleinere Bildgrößen.'
p['check'][0]['rows'][3]['text'] = 'Ein Kontaktformular ist auf der Seite /kontakt/ vorhanden.'

p['check'][1]['rows'][0]['text'] = 'Die Hauptüberschrift lautet heute „Herzlich willkommen!“ ohne Nennung von Psychotherapie, Heilpraxis oder der Region Amberg.'
p['check'][1]['rows'][1]['text'] = '1 von 30 Unterseiten (/elpi-freebie/) hat keine Hauptüberschrift.'
p['check'][1]['rows'][2]['text'] = 'Eine Meta-Beschreibung für Google fehlt auf allen 30 gemessenen Unterseiten.'

p['check'][2]['rows'][0]['text'] = 'Auf der Website ist keine Web-Statistik zur Messung von Besucherströmen aktiv.'
p['check'][2]['rows'][1]['text'] = 'Strukturierte Standort- und Therapeuten-Daten für Google fehlen derzeit.'

p['check'][3]['rows'][0]['text'] = 'Mit 0 Bewertungen im Google-Profil liegst du hinter Amberger Kollegen wie Ostermann (19) oder Scheibl (23).'
p['check'][3]['rows'][1]['text'] = 'Aktuell sind noch keine Antworten im Google-Profil hinterlegt.'
p['check'][3]['rows'][2]['text'] = '21 von 51 Websites, die auf dich verlinken, haben bedenkliche Spam-Werte (Verzeichnis-Spam).'
p['check'][3]['rows'][3]['text'] = 'Gesundheitsaussagen im Web unterliegen dem Heilmittelwerbegesetz (HWG) und sollten sachlich formuliert sein.'

p['quick_wins'] = [
    {
        'title': 'Telefonnummer auf der Website verlinken',
        'text': 'Die Rufnummer 09622 70 31 90 als anklickbaren tel:-Link formatieren, damit Smartphone-Besucher sofort anrufen können.'
    },
    {
        'title': 'Einzugsgebiet Amberg im Google-Profil ergänzen',
        'text': 'Amberg und Nachbargemeinden als Servicegebiet im Google-Unternehmensprofil eintragen.'
    },
    {
        'title': 'Hauptüberschrift auf der Startseite schärfen',
        'text': '„Heilpraktikerin für Psychotherapie & Coaching in Hirschau & Amberg“ statt „Herzlich willkommen!“.'
    },
    {
        'title': 'Erste 3 Klientenbewertungen einholen',
        'text': 'Zufriedene Klienten nach abgeschlossener Begleitung um eine ehrliche Google-Rezension bitten.'
    },
    {
        'title': 'Meta-Beschreibungen für Google hinterlegen',
        'text': 'Auf den wichtigsten Seiten kurze, ansprechende Vorschautexte für die Google-Suchtreffer einpflegen.'
    },
    {
        'title': 'Spam-Backlinks per Disavow bereinigen',
        'text': 'Die 21 minderwertigen Backlink-Quellen über die Google Search Console entwerten lassen.'
    }
]

p['roadmap'] = [
    {
        'step': 'Woche 1–2 · Schnelle Korrekturen',
        'what': 'Telefonnummer antippbar machen, Hauptüberschrift anpassen und Amberg als Einzugsgebiet im Google-Profil eintragen',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Verhindert, dass Smartphone-Besucher sofort wieder abspringen'
    },
    {
        'step': 'Woche 1–3 · Bewertungen aufbauen',
        'what': '3 bis 5 positive Google-Bewertungen von Klienten einholen',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Mitbewerber in Amberg haben 2 bis 19 Bewertungen – mit 3 Rezensionen spielst du direkt mit'
    },
    {
        'step': 'Woche 2–4 · Startseite optimieren',
        'what': 'Erster Bildschirm mit Porträt, Schwerpunkten und direktem Button zum 45-minütigen Kennenlerngespräch',
        'prio': 'Hoch',
        'effort': 'Mittel',
        'why': 'Macht aus Suchenden verbindliche Terminanfragen'
    },
    {
        'step': 'Woche 3–8 · Amberg-Landingpage',
        'what': 'Gezielte Unterseite für Psychotherapie & Coaching für Klienten aus Amberg und dem Landkreis',
        'prio': 'Hoch',
        'effort': 'Mittel',
        'why': 'Erschließt die 210 monatlichen Suchen im direkten Nachbarort'
    },
    {
        'step': 'Laufend · Messen',
        'what': 'Monatliche Kartenmessung und Überprüfung der Terminanfragen',
        'prio': 'Mittel',
        'effort': 'Gering',
        'why': 'Jeder Schritt muss zu messbar mehr Praxisgesprächen führen'
    }
]

p['proof'] = {
    'h2': 'Andere Praxen und Berater hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'lead': 'Ausgewählt nach deiner Praxisgröße: Therapeutische Praxen, die in ihrer Region zur führenden Anlaufstelle wurden.',
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
    'h2': 'Lass uns in 30 Minuten anschauen, wie deine Praxis im Raum Amberg sichtbar wird.',
    'p': '30 Minuten, kostenlos: Ich zeige dir live, wie du die 210 monatlichen Suchen in Amberg erschließt und planbar neue Klienten gewinnst. Unverbindlich.',
    'subject': 'Gabriele%20Heckel%20Sichtbarkeits-Analyse'
}

p['guide'] = {
    'hello': 'Ich habe mir deine Website und deinen Google-Eintrag für deine Praxis in Hirschau genau angesehen. Hier zeige ich dir, was ich gemessen habe.',
    'point': 'Im Amberger Raum suchen jeden Monat 210 Menschen nach einem Heilpraktiker. Deine Praxis taucht an keinem der 49 Messpunkte auf.',
    'think': 'Hirschau liegt nur 13 Kilometer von Amberg entfernt. Wer im Umland sucht, sollte dich als sympathische Therapeutin sofort finden.',
    'insight': 'Der größte Hebel: Telefonnummer klickbar machen, Einzugsgebiet Amberg hinterlegen und die ersten 3 Bewertungen einholen.',
    'celebrate': 'Mit deiner langjährigen Erfahrung kannst du in der gesamten Region Hirschau-Amberg zur festen Adresse werden.'
}

p['headlines'] = {
    'hero_h1': 'Gabriele, so finden Klienten <span style="color:var(--brand--lemon);">im Raum Amberg</span> deine Praxis.<span style="display:block;font-size:.42em;line-height:1.35;font-weight:600;letter-spacing:0;color:#5c5c5c;margin-top:16px;">Bei „heilpraktiker amberg“ ist deine Praxis an keinem von 49 Punkten unter den Top 3. Hier ist dein Fahrplan.</span>',
    'hero_sub': 'Dein Google-Profil hat 0 Bewertungen. Bei der regionalen Suche „heilpraktiker amberg“ ist deine Praxis an keinem der 49 Punkte sichtbar – während Amberger Kollegen bis zu 73 % der Karte belegen.',
    'grid_h2': 'Unter den ersten drei an 0 von 49 Punkten. Im Raum Amberg nicht sichtbar.',
    'proof_h2': 'Andere Praxen und Berater hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'system_h2': 'Drei Hebel für mehr Klienten, und bei jedem fehlt heute ein Schritt',
    'step1_h2': 'Nach „heilpraktiker amberg“ wird 210-mal im Monat gesucht. Deine Website taucht dafür nicht auf.',
    'step2_h2': 'energy in balance führt mit 73 % der Karte. Dein Profil hat noch 0 Bewertungen.',
    'step3_h2': 'Besucher entscheiden in 5 Sekunden. Deine Startseite begrüßt mit „Herzlich willkommen!“ statt klarer Orientierung.',
    'calc_h2': 'Was neue Klienten für deine Praxis bedeuten',
    'check_h2': 'Was deine Website heute richtig macht und wo du Interessenten verlierst',
    'quickwins_h2': 'Sechs Schritte, die du schon nächste Woche umsetzen kannst, ohne neue Website',
    'roadmap_h2': 'Dein Plan für die nächsten 8 Wochen, Schritt für Schritt',
    'final_h2': 'Lass uns in 30 Minuten anschauen, wie deine Praxis im Raum Amberg sichtbar wird.'
}

p['sources']['grid'] = 'evidence/falcon-report-fad24349417e181.json (keyword heilpraktiker amberg, 7x7, 15.0 km, centre 49.444/11.858, 16.10.2026; solv 0.00 = 0/49, found_in 0) + review-assets/gabriele-heckel/scan-grid.webp'
p['sources']['calc'] = 'evidence/dfs-volumes-ads.json (volume heilpraktiker amberg 210); val 100 aus Praxis-Stundensätzen (70 € Psychotherapie, 60 € Energiecoaching); budget/conv/deal = assumptions, labelled'

with open(pfile, 'w', encoding='utf-8') as f:
    json.dump(p, f, indent=2, ensure_ascii=False)

print('Updated Gabriele Heckel prospect.json successfully!')
