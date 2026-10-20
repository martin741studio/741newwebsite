#!/usr/bin/env python3
import json, os

pfile = '00_project/prospects/claudia-fuegel/prospect.json'
with open(pfile, 'r', encoding='utf-8') as f:
    p = json.load(f)

p['business_ref'] = 'deine Praxis'
p['branch'] = 'health'
p['first_name'] = 'Claudia'
p['display_name'] = 'Claudia Fügel'
p['company'] = 'Claudia Fügel'

p['hero']['sub'] = 'Du hast 5,0 Sterne bei Google. Bei der Suche „astrologie stuttgart“ ist deine Praxis an 9 von 49 Punkten unter den ersten drei, an 14 Punkten aber nicht unter den ersten 20.'
p['hero']['cards'][0]['sub'] = 'Traumdeutung · Astrologische Beratung · Stuttgart & Leinfelden'
p['hero']['cards'][1]['badge'] = 'Im Stuttgarter Norden nicht unter den Top 3'
p['hero']['cards'][2]['sub'] = 'Du: 6 Bewertungen · Petra Heinisch-Holzwarth: 9 Bewertungen'
p['hero']['cards'][3]['sub'] = 'Erster Bildschirm: Poesie-Titel, kein direkter Termin-Button, keine Sterne'
p['hero']['cards'][3]['badge'] = 'Startseite heute: 12 von 44 Punkten'

p['grid']['h2'] = 'Unter den ersten drei an 9 von 49 Punkten. Im Stuttgarter Zentrum nicht vorn.'
p['grid']['caption_today'] = '<b>Unter den ersten drei an 9 von 49 Punkten.</b> Rund um deinen Standort in Stuttgart-Plieningen und Leinfelden bist du gut sichtbar. Im Norden und Zentrum führen Mitbewerber. Petra Heinisch-Holzwarth erreicht 100 % Sichtbarkeit.'
p['grid']['caption_goal'] = '<b>Ziel: Sichtbarkeit in ganz Stuttgart für Ratsuchende, die nach Astrologie und Lebensberatung suchen.</b> Die Praxen vorn haben 5 bis 48 Bewertungen.'
p['grid']['chips'] = [
    '📞 Direkte Terminanfragen aus der Google-Karte',
    '🧭 Klienten aus dem ganzen Großraum Stuttgart finden dich',
    '🤝 Mehr Buchungen für Traumdeutung & Astrologie'
]

p['system']['intro'] = 'Für deine Praxis haben wir drei Hebel geprüft: wonach Menschen in Stuttgart suchen, warum andere Astrologen in der Karte vorn stehen und ob deine Website Besucher zu Terminen macht.'
p['system']['steps'][2]['kpi'] = 'heute 12 von 44 Punkten'

p['system']['step1']['h2'] = 'Nach „astrologie stuttgart“ wird 40-mal im Monat gesucht. Deine Website steht dafür nicht unter den Top 20.'
p['system']['step1']['lead'] = 'Wir haben traumdeutung-fuegel.de mit den Websites verglichen, die bei „astrologie stuttgart“ oben stehen, und mit den Begriffen, die Menschen in der Region wirklich suchen.'
p['system']['step1']['demand_note'] = '„astrologie stuttgart“ und „lebensberatung stuttgart“ bündeln die gezielte lokale Nachfrage. Für „traumdeutung online“ gibt es bundesweit weitere 480 Suchen pro Monat.'

p['system']['step1']['depth']['title'] = 'Ausführliche Texte, aber Stuttgart fehlt in der wichtigsten Überschrift.'
p['system']['step1']['depth']['sub'] = 'Deine Startseite hat 1.818 Wörter. Doch in der Hauptüberschrift fehlt die Verknüpfung mit deinem Standort Stuttgart.'
p['system']['step1']['depth']['note'] = 'In deiner Hauptüberschrift steht „Träume, Briefe Deiner Seele“, aber weder dein Angebot noch dein Standort.'

p['system']['step1']['items'] = [
    {
        'title': 'Startseite auf Astrologie & Traumdeutung Stuttgart ausrichten',
        'tag': 'Ort',
        'why': 'Deine Startseite nennt heute weder Astrologie noch Stuttgart in der sichtbaren Hauptüberschrift.'
    },
    {
        'title': 'Eigene Seite zu Astrologischer Beratung Stuttgart',
        'tag': 'Leistung',
        'why': '„astrologie stuttgart“ hat 40 Suchen pro Monat. Eine fokussierte Leistungsseite fängt gezielt lokale Ratsuchende ab.'
    },
    {
        'title': 'Eigene Seite zu Lebensberatung Stuttgart',
        'tag': 'Leistung',
        'why': '„lebensberatung stuttgart“ hat 50 Suchen pro Monat. Viele Klienten suchen genau unter diesem Begriff nach Unterstützung.'
    },
    {
        'title': 'Eigene Seite zu Traumdeutung online buchen',
        'tag': 'Leistung',
        'why': '„traumdeutung online“ hat 480 Suchen pro Monat. Ein idealer Hebel für deine Zoom-Beratungen in ganz Deutschland.'
    },
    {
        'title': 'Eigene Seite zu Seminare & Traumdeutung lernen',
        'tag': 'Leistung',
        'why': 'Interessierte suchen nach Ausbildungen und Kursen, um Träume selbst verstehen und deuten zu lernen.'
    },
    {
        'title': 'Klares Therapeuten- und Beraterprofil',
        'tag': 'Profil',
        'why': 'Klienten wollen sofort sehen, wie eine Sitzung abläuft, was sie kostet und wie das kostenlose 15-Minuten-Erstgespräch gebucht wird.'
    }
]

p['system']['step2']['h2'] = 'Petra Heinisch-Holzwarth hält 100 % der Karte. Dein Profil ist bei Google noch unbestätigt.'
p['system']['step2']['meaning'] = 'Die führenden Praxen in Stuttgart haben zwischen 5 und 48 Bewertungen. Dein Profil steht mit 5,0 Sternen und 6 Bewertungen bereits gut da, ist bei Google aber noch nicht als Inhaberin beansprucht.'

for row in p['system']['step2']['table']:
    if 'Astrologer' in row.get('cats', ''):
        row['cats'] = row['cats'].replace('Astrologer', 'Astrologe')
    if 'Massage spa' in row.get('cats', ''):
        row['cats'] = row['cats'].replace('Massage spa', 'Wellness')

p['system']['step2']['changes'] = [
    {
        'title': 'Google-Unternehmensprofil bestätigen (Claiming)',
        'text': 'Dein Profil zeigt bei Google „Als Inhaber eintragen“. Die offizielle Bestätigung schützt deinen Eintrag und schaltet alle Funktionen frei.'
    },
    {
        'title': 'Kategorien im Google-Profil ergänzen',
        'text': 'Neben „Alternativmediziner“ auch „Astrologe“ und „Lebensberater“ hinterlegen, um in der Karte direkt vorn mitzuspielen.'
    },
    {
        'title': 'Kostenloses Erstgespräch im Profil bewerben',
        'text': 'Dein 15-minütiges Kennenlerngespräch direkt als Terminknopf im Google-Eintrag verlinken.'
    },
    {
        'title': 'Auf jede Google-Bewertung persönlich antworten',
        'text': 'Heute hat keine deiner 6 Bewertungen eine Antwort. Eine persönliche Rückmeldung zeigt Google und neuen Klienten Wertschätzung.'
    },
    {
        'title': 'Praxisfotos und TV-Beiträge einbinden',
        'text': 'Bilder deiner Praxis in Plieningen und Hinweise auf deinen QS24-Gesundheitsfernsehen-Auftritt schaffen sofortiges Vertrauen.'
    },
    {
        'title': 'Regelmäßige Impulse teilen',
        'text': 'Monatsimpulse oder Gedanken zur Astrologie als Google-Beiträge direkt im Eintrag veröffentlichen.'
    }
]

p['system']['step2']['cleanup'] = [
    {
        'n': '0 / 5',
        'text': 'Websites, die auf deine Seite verlinken, sind unauffällig. Es liegen keine bedenklichen Spam-Backlinks vor.'
    },
    {
        'n': '0 / 6',
        'text': 'Bewertungen mit einer Antwort von dir.'
    }
]

p['system']['step2']['good'] = 'Das Fundament ist stark: Makellose 5,0 Sterne, Fachbuch-Autorin und TV-Erfahrung. Mit der Profil-Bestätigung und der richtigen Kategorie kannst du in Stuttgart ganz nach vorn aufrücken.'

p['system']['step3']['score_draft_label'] = 'Ziel: 34 / 44'
p['system']['step3']['note_today'] = 'Im ersten Bildschirm sieht man den poetischen Titel „Träume, Briefe Deiner Seele“, aber keinen Ort Stuttgart, keine Sterne und keinen direkten Erstgesprächs-Button.'
p['system']['step3']['note_draft'] = 'Klarer Fokus: Dein Porträt, „Astrologie & Traumdeutung in Stuttgart“, 5 Google-Sterne, Buch-Hinweis und direkter Button zum kostenfreien 15-Minuten-Erstgespräch.'

p['system']['step3']['five'] = [
    {
        'q': 'Was?',
        'a': '„Träume, Briefe Deiner Seele“. Ein schöner Gedanke, aber das konkrete Beratungsangebot wird erst weiter unten erklärt.'
    },
    {
        'q': 'Wo?',
        'a': 'Stuttgart wird im ersten Bildschirm nicht genannt; die Adresse in Plieningen steht nur im Footer.'
    },
    {
        'q': 'Warum du?',
        'a': 'Keine Sterne, Bewertungen oder Auszeichnungen im sichtbaren ersten Bildschirm.'
    },
    {
        'q': 'Wie zum Termin?',
        'a': 'Zwei Inhaltsknöpfe („Traumdeutung“, „Astrologie“), aber kein direkter Button zum kostenlosen Erstgespräch.'
    },
    {
        'q': 'Wer?',
        'a': 'Ein Foto von Claudia Fügel erscheint erst nach dem Herunterscrollen, nicht im ersten Blick.'
    }
]

p['system']['step3']['strip'] = [
    {
        'photo': '/review-assets/claudia-fuegel/foto-1.webp',
        'title': 'Claudia Fügel persönlich',
        'why': 'Ratsuchende fassen Vertrauen, wenn sie die Beraterin vor der ersten Sitzung sehen.'
    },
    {
        'photo': '/review-assets/claudia-fuegel/foto-2.webp',
        'title': 'Expertin im Gesundheitsfernsehen',
        'why': 'Auftritte bei QS24 unterstreichen deine langjährige Erfahrung und Fachkompetenz.'
    },
    {
        'photo': '/review-assets/claudia-fuegel/foto-3.webp',
        'title': 'Astrologie & Traumdeutung',
        'why': 'Individuelle Deutung und Horoskop-Analysen in ruhiger Atmosphäre in Stuttgart.'
    }
]

p['system']['step3']['good'] = 'Deine Website hat viel Tiefe und persönliche Wärme. Mit einem klareren Einstieg werden deutlich mehr Besucher den Schritt zum ersten Gespräch wagen.'

p['calc']['val'] = 150
p['calc']['val_label'] = 'Umsatz pro Beratungstermin (Startwert 150 €)'
p['calc']['volumes_line'] = 'Echte Google-Suchen pro Monat (Region Stuttgart / Deutschland): <b>astrologie stuttgart 40</b> · lebensberatung stuttgart 50 · traumdeutung online 480. Startwert Beratung: 150 € (orientiert am Stundensatz von 120 € bzw. 180 € für 1,5 Stunden). Budget, Anfrage- und Buchungsanteil sind Annahmen.'

# Check card 0 (Deine Website)
p['check'][0]['rows'][0]['text'] = 'Auf deiner Website ist die Telefonnummer genannt, aber auf der Kontaktseite nicht als anklickbarer Link hinterlegt.'

# Check card 1 (Was Google liest)
p['check'][1]['rows'][0]['text'] = 'Die Hauptüberschrift lautet heute „Träume, Briefe Deiner Seele“ ohne die Suchbegriffe Astrologie oder Stuttgart.'
p['check'][1]['rows'][1]['text'] = '3 von 30 Unterseiten haben keine Hauptüberschrift.'
p['check'][1]['rows'][2]['text'] = 'Die Meta-Beschreibung nennt deinen Namen und Berufe, könnte aber noch gezielter auf Anfragen ausgerichtet werden.'

# Check card 2 (Was du messen kannst)
p['check'][2]['rows'][1]['text'] = 'Ein strukturierter Datenblock für Google ist vorhanden; lokale Standortattribute sollten geschärft werden.'

# Check card 3 (Dein Ruf im Netz)
p['check'][3]['rows'][1]['text'] = 'Mit 6 Bewertungen stehst du gut da, liegst aber hinter Mitbewerbern wie Ernst Albrecht Vöhringer (48) oder Jyotish (33).'
p['check'][3]['rows'][3]['text'] = 'Aktuell gibt es 5 verlinkende Domains ohne bedenkliche Spam-Werte.'
p['check'][3]['rows'][4]['text'] = 'Auf deiner Website werden gesundheitliche und astrologische Themen mit Bedacht formuliert.'

p['quick_wins'] = [
    {
        'title': 'Google-Unternehmensprofil beanspruchen',
        'text': 'Den Eintrag offiziell als Inhaberin bestätigen, um vollen Schutz und Ranking-Vorteile zu sichern.'
    },
    {
        'title': 'Kategorie Astrologe im Profil ergänzen',
        'text': 'Neben „Alternativmediziner“ auch „Astrologe“ und „Lebensberater“ im Google-Profil hinterlegen.'
    },
    {
        'title': 'Stuttgart & Astrologie in die Startzeile',
        'text': '„Astrologische Beratung & Traumdeutung Stuttgart – Claudia Fügel“ als klare Hauptüberschrift nutzen.'
    },
    {
        'title': 'Kostenfreies Erstgespräch nach oben holen',
        'text': 'Einen Button „Kostenloses 15-Minuten-Gespräch vereinbaren“ direkt im ersten Bildschirm platzieren.'
    },
    {
        'title': 'Telefonnummer auf Kontaktseite verlinken',
        'text': 'Die Telefonnummer auf der Kontaktseite als anklickbaren Link anlegen für mobile Besucher.'
    },
    {
        'title': 'Zufriedene Klienten um Rezensionen bitten',
        'text': 'Bestehende Klienten gezielt um Google-Bewertungen bitten, um zu den Top-Profilen in Stuttgart aufzuschließen.'
    }
]

p['roadmap'] = [
    {
        'step': 'Woche 1–2 · Aufräumen',
        'what': 'Google-Profil beanspruchen, Kategorie Astrologe ergänzen und Telefon-Link auf der Kontaktseite aktivieren',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Erst technische Grundlagen aufräumen, dann ausbauen'
    },
    {
        'step': 'Woche 1–3 · Telefon klingeln',
        'what': 'Google-Eintrag ausbauen: Erstgespräch verlinken, Praxisfotos hochladen und erste neue Bewertungen einholen',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Aktuell führt Petra Heinisch-Holzwarth mit 100 % Sichtbarkeit die Karte an'
    },
    {
        'step': 'Woche 2–4 · Startseite',
        'what': 'Erster Bildschirm mit Porträt, Standort Stuttgart, 5 Sternen und Button zum 15-minütigen Kennenlerngespräch',
        'prio': 'Hoch',
        'effort': 'Mittel',
        'why': 'Aus Webseiten-Besuchern werden Erstgespräche'
    },
    {
        'step': 'Woche 3–8 · Neue Inhalte',
        'what': 'Gezielte Seiten für Astrologische Beratung Stuttgart, Lebensberatung Stuttgart und Traumdeutung online',
        'prio': 'Hoch',
        'effort': 'Mittel',
        'why': 'Seiten für die konkreten Suchanfragen, die Ratsuchende bei Google stellen'
    },
    {
        'step': 'Laufend · Messen',
        'what': 'Entwicklung der Anfragen, Erstgespräche und monatliche Kartenmessung verfolgen',
        'prio': 'Mittel',
        'effort': 'Gering',
        'why': 'Jede Optimierung muss zu messbaren neuen Klienten führen'
    }
]

p['proof'] = {
    'h2': 'Andere Berater und Therapeuten hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'lead': 'Ausgewählt nach deiner Praxisgröße: Beratende Praxen und Therapeuten, die lokal zur führenden Adresse wurden.',
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
    'h2': 'Lass uns in 30 Minuten anschauen, wer in Stuttgart oben steht und wie deine Praxis dorthin kommt.',
    'p': '30 Minuten, kostenlos: Ich zeige dir live die Stuttgarter Mitbewerber und welche Schritte für deine Praxis die meiste Hebelwirkung haben. Unverbindlich.',
    'subject': 'Claudia%20F%C3%BCgel%20Sichtbarkeits-Analyse'
}

p['guide'] = {
    'hello': 'Ich habe mir traumdeutung-fuegel.de und deinen Google-Eintrag genau angesehen. Hier zeige ich dir, was ich gemessen habe.',
    'point': 'Petra Heinisch-Holzwarth erreicht 100 % der Karte. Dein Eintrag steht an 9 von 49 Punkten unter den Top 3, ist aber bei Google noch unbestätigt.',
    'think': 'Bei persönlicher Beratung und Astrologie zählen Vertrauen und Sympathie. Wer in Stuttgart sucht, sollte dich direkt finden.',
    'insight': 'Der größte Hebel: Dein Google-Profil beanspruchen, die Kategorie Astrologe ergänzen und das kostenfreie Erstgespräch oben zeigen.',
    'celebrate': 'Mit deiner Erfahrung als Autorin und TV-Expertin kannst du in ganz Stuttgart zur führenden Anlaufstelle werden.'
}

p['headlines'] = {
    'hero_h1': 'Claudia, so finden Klienten <span style="color:var(--brand--lemon);">in Stuttgart</span> deine Praxis.<span style="display:block;font-size:.42em;line-height:1.35;font-weight:600;letter-spacing:0;color:#5c5c5c;margin-top:16px;">Bei „astrologie stuttgart“ steht deine Praxis an 9 von 49 Punkten unter den Top 3. Hier ist dein Fahrplan.</span>',
    'hero_sub': 'Du hast 5,0 Sterne bei Google. Bei der Suche „astrologie stuttgart“ ist deine Praxis an 9 von 49 Punkten unter den ersten drei, an 14 Punkten aber nicht unter den ersten 20.',
    'grid_h2': 'Unter den ersten drei an 9 von 49 Punkten. Im Stuttgarter Zentrum nicht vorn.',
    'proof_h2': 'Andere Berater und Therapeuten hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'system_h2': 'Drei Hebel für mehr Klienten, und bei jedem fehlt heute ein Schritt',
    'step1_h2': 'Nach „astrologie stuttgart“ wird 40-mal im Monat gesucht. Deine Website steht dafür nicht unter den Top 20.',
    'step2_h2': 'Petra Heinisch-Holzwarth hält 100 % der Karte. Dein Profil ist bei Google noch unbestätigt.',
    'step3_h2': 'Besucher entscheiden in 5 Sekunden. Deine Startseite zeigt heute kein klares Angebot im ersten Blick.',
    'calc_h2': 'Was neue Klienten für deine Praxis bedeuten',
    'check_h2': 'Was deine Website heute richtig macht und wo du Interessenten verlierst',
    'quickwins_h2': 'Sechs Schritte, die du schon nächste Woche umsetzen kannst, ohne neue Website',
    'roadmap_h2': 'Dein Plan für die nächsten 8 Wochen, Schritt für Schritt',
    'final_h2': 'Lass uns in 30 Minuten anschauen, wer in Stuttgart oben steht und wie deine Praxis dorthin kommt.'
}

p['sources']['grid'] = 'evidence/falcon-report-6ab0269fea7c8e3.json (keyword astrologie stuttgart, 7x7, 5.0 km, centre 48.7026/9.2073, 16.10.2026; solv 18.37 = 9/49, found_in 35) + review-assets/claudia-fuegel/scan-grid.webp'
p['sources']['calc'] = 'evidence/dfs-volumes-ads.json (volume astrologie stuttgart 40); val 150 aus Preis-Seite (120 €/h bis 180 € für 1,5 h); budget/conv/deal = assumptions, labelled'

with open(pfile, 'w', encoding='utf-8') as f:
    json.dump(p, f, indent=2, ensure_ascii=False)

print('Updated Claudia Fügel prospect.json successfully!')
