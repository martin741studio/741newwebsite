#!/usr/bin/env python3
import json, os

pfile = '00_project/prospects/roland-parbs/prospect.json'
with open(pfile, 'r', encoding='utf-8') as f:
    p = json.load(f)

p['business_ref'] = 'deine Praxis'
p['branch'] = 'health'
p['first_name'] = 'Roland'
p['display_name'] = 'Roland Parbs'
p['company'] = 'E. R. Parbs'

p['hero']['sub'] = 'Dein Google-Profil hat 0 Bewertungen und ist unbestätigt. Bei der Suche „heilpraktiker dannenberg“ ist deine Praxis an nur 1 von 49 Punkten unter den ersten drei – und deine hinterlegte Website zeigt einen 404-Fehler.'
p['hero']['cards'][0]['sub'] = 'Naturheilkunde · Schmerztherapie · Gusborn bei Dannenberg'
p['hero']['cards'][0]['badge'] = 'Profil unbestätigt'
p['hero']['cards'][1]['badge'] = 'An 20 Punkten nicht unter den Top 20'
p['hero']['cards'][2]['sub'] = 'Du: 0 Bewertungen · Günther Bentz: 2 Bewertungen'
p['hero']['cards'][2]['badge'] = 'Keine Bewertungen'
p['hero']['cards'][3]['sub'] = 'Hinterlegte Webadresse liefert einen 404-Fehler'
p['hero']['cards'][3]['badge'] = 'Website heute: nicht erreichbar (404)'

p['grid']['h2'] = 'Unter den ersten drei an nur 1 von 49 Punkten. Im Großraum Dannenberg kaum sichtbar.'
p['grid']['caption_today'] = '<b>Unter den ersten drei an nur 1 von 49 Punkten (2,04 % Sichtbarkeit).</b> Direkt an deinem Standort in Klein Gusborn wirst du gelistet, in Dannenberg und im Umland führen Mitbewerber. Herr Günther Bentz erreicht mit nur 2 Bewertungen 32,65 % Sichtbarkeit.'
p['grid']['caption_goal'] = '<b>Ziel: Solide Top-3-Präsenz in Dannenberg und im gesamten Wendland.</b> Die führenden Kollegen haben lediglich 0 bis 11 Bewertungen.'
p['grid']['chips'] = [
    '📞 Direkte Terminanfragen aus der Google-Karte',
    '🌐 Funktionierende Praxisseite statt 404-Fehler',
    '📍 Patienten aus Dannenberg & Wendland finden dich sofort'
]

p['system']['intro'] = 'Für deine Praxis haben wir drei Hebel geprüft: wonach Patienten in Dannenberg und im Wendland suchen, warum Mitbewerber in der Karte vorn stehen und warum deine hinterlegte Website heute Interessenten verliert.'
p['system']['steps'][0]['kpi'] = '20 Suchen/Monat'
p['system']['steps'][1]['kpi'] = '1 von 49 Punkten'
p['system']['steps'][2]['kpi'] = 'heute 404-Fehler'

p['system']['step1']['h2'] = 'Nach „heilpraktiker dannenberg“ wird 20-mal im Monat gesucht. Deine Website ist aktuell nicht erreichbar.'
p['system']['step1']['lead'] = 'Wir haben deinen Webauftritt mit den Praxen verglichen, die bei „heilpraktiker dannenberg“ oben stehen, und mit den Begriffen, die Patienten in der Region wirklich eingeben.'
p['system']['step1']['demand_note'] = 'Im ländlichen Raum zählt jeder Suchende: 20 gezielte Suchen pro Monat nach „heilpraktiker dannenberg“ plus regionale Suchen nach Schmerztherapie und Akupunktur im Wendland.'

p['system']['step1']['depth']['title'] = 'Die hinterlegte Website zeigt einen 404-Fehlerbildschirm.'
p['system']['step1']['depth']['sub'] = 'Wer in Google Maps auf deine Webadresse klickt, landet auf einer Fehlerseite („Oh No! 404 Looks like the page you\'re trying to visit doesn\'t exist“).'
p['system']['step1']['depth']['note'] = 'Patienten brechen an dieser Stelle sofort ab und rufen die nächste Praxis in der Liste an.'

p['system']['step1']['items'] = [
    {
        'title': 'Funktionierende Startseite für Dannenberg & Wendland',
        'tag': 'Ort',
        'why': 'Eine zuverlässig erreichbare Seite, die deine Praxis und deinen Standort sofort vorstellt.'
    },
    {
        'title': 'Eigene Leistungsseite zu Schmerztherapie',
        'tag': 'Leistung',
        'why': 'Schmerzpatienten suchen gezielt nach ganzheitlichen Ansätzen und individueller Begleitung.'
    },
    {
        'title': 'Eigene Leistungsseite zu Akupunktur',
        'tag': 'Leistung',
        'why': 'Akupunktur ist ein stark nachgefragtes Verfahren in der alternativen Schmerz- und Regulationsbehandlung.'
    },
    {
        'title': 'Eigene Seite zu Naturheilkunde & Diagnostik',
        'tag': 'Leistung',
        'why': 'Transparenz über deine Methoden schafft Sicherheit vor dem ersten Praxisbesuch.'
    },
    {
        'title': 'Anfahrtsbeschreibung aus Dannenberg & Lüchow',
        'tag': 'Ort',
        'why': 'Patienten aus dem Umland wollen sehen, wie schnell Gusborn-Klein Gusborn mit dem Auto erreichbar ist.'
    },
    {
        'title': 'Klares Therapeutenprofil & Terminkanal',
        'tag': 'Profil',
        'why': 'Patienten brauchen Vertrauen: Ein Foto von dir, klare Sprechzeiten und eine direkte Telefonnummer.'
    }
]

p['system']['step2']['h2'] = 'Günther Bentz führt mit nur 2 Bewertungen. Dein Google-Profil ist noch unbestätigt.'
p['system']['step2']['meaning'] = 'Im Wendland ist die Wettbewerbshürde extrem niedrig: Die führenden Praxen haben zwischen 0 und 11 Bewertungen. Du hast 0 Bewertungen und dein Profil ist bei Google noch nicht offiziell als Inhaber beansprucht.'

for row in p['system']['step2']['table']:
    if 'Alternative medicine practitioner' in row.get('cats', ''):
        row['cats'] = row['cats'].replace('Alternative medicine practitioner', 'Alternativmediziner')

p['system']['step2']['changes'] = [
    {
        'title': 'Google-Unternehmensprofil beanspruchen (Claiming)',
        'text': 'Dein Profil zeigt bei Google „Als Inhaber eintragen“. Die Bestätigung sichert deinen Eintrag und gibt dir die volle Kontrolle.'
    },
    {
        'title': 'Funktionierende Website verlinken',
        'text': 'Den toten 404-Link in Google Maps durch eine funktionierende Praxis-Webseite ersetzen.'
    },
    {
        'title': 'Telefonnummer und Sprechzeiten hinterlegen',
        'text': 'Aktuell fehlt eine direkt wählbare Telefonnummer im Profil für mobile Patienten.'
    },
    {
        'title': 'Erste 3–5 Google-Bewertungen einholen',
        'text': 'Zufriedene Patienten um eine kurze Rezension bitten. Damit ziehst du bereits mit den Spitzenreitern gleich.'
    },
    {
        'title': 'Praxisfotos in Gusborn hochladen',
        'text': 'Bilder der Praxisräume und des Behandlungszimmers schaffen sofortige Nahbarkeit und Vertrauen.'
    },
    {
        'title': 'Leistungskategorien schärfen',
        'text': 'Neben Alternativmediziner auch Naturheilkunde und Akupunktur als Profil-Leistungen hinterlegen.'
    }
]

p['system']['step2']['cleanup'] = [
    {
        'n': '0 / 0',
        'text': 'Verzeichniseinträge und Branchenportale sind aktuell noch nicht aufgebaut.'
    },
    {
        'n': '0 / 0',
        'text': 'Bewertungen im Google-Profil vorhanden.'
    }
]

p['system']['step2']['good'] = 'Deine Chance ist hervorragend: Weil im Landkreis Lüchow-Dannenberg selbst die Top-Profile nur 0 bis 11 Bewertungen haben, genügen wenige gezielte Optimierungen, um ganz oben zu stehen.'

p['system']['step3']['score_draft_label'] = 'Ziel: 36 / 44'
p['system']['step3']['note_today'] = 'Heute: Die hinterlegte Domain heilpraxis-parbs.now.site liefert einen 404-Fehler. Patienten finden weder Telefonnummer noch Adresse oder Behandlungsschwerpunkte.'
p['system']['step3']['note_draft'] = 'Der Entwurf: Klare Überschrift „Ihre Heilpraxis in Dannenberg & Wendland“, Leistungen (Schmerztherapie, Akupunktur), Praxisadresse in Gusborn und direkter Ersttermin-Button.'

p['system']['step3']['five'] = [
    {
        'q': 'Was?',
        'a': 'Aktuell lädt ein 404-Fehlerbildschirm. Der Entwurf zeigt sofort: Naturheilkunde, Schmerztherapie und Akupunktur.'
    },
    {
        'q': 'Wo?',
        'a': 'Heute kein Ort sichtbar. Der Entwurf nennt prominent Dannenberg, Gusborn und das Wendland.'
    },
    {
        'q': 'Warum du?',
        'a': 'Heute keine Information. Der Entwurf hebt deine ruhige Praxisatmosphäre und individuelle Betreuung hervor.'
    },
    {
        'q': 'Wie zum Termin?',
        'a': 'Heute keine Kontaktmöglichkeit. Der Entwurf bietet klare Terminknöpfe und eine direkte Telefonnummer.'
    },
    {
        'q': 'Wer?',
        'a': 'Heute kein Name sichtbar. Der Entwurf stellt Roland Parbs und seine Praxis in Gusborn klar vor.'
    }
]

p['system']['step3']['strip'] = [
    {
        'photo': '/review-assets/roland-parbs/home-draft.webp',
        'title': 'Klare Praxisvorstellung',
        'why': 'Patienten sehen sofort deine Schwerpunkte: Schmerztherapie, Akupunktur und Naturheilkunde.'
    },
    {
        'photo': '/review-assets/roland-parbs/home-draft.webp',
        'title': 'Fester Standort in Gusborn',
        'why': 'Transparente Adresse und Anfahrtszeiten für Patienten aus Dannenberg und Lüchow.'
    },
    {
        'photo': '/review-assets/roland-parbs/home-draft.webp',
        'title': 'Einfache Terminanfrage',
        'why': 'Klare Handlungsaufforderung nimmt Hemmschwellen und bringt das Telefon zum Klingeln.'
    }
]

p['system']['step3']['good'] = 'Mit einem funktionierenden, ruhigen und vertrauensvollen Auftritt hebst du dich im Wendland sofort von veralteten Praxisseiten ab.'

p['calc']['val'] = 100
p['calc']['val_label'] = 'Umsatz pro Behandlung / Termin (Startwert 100 €)'
p['calc']['volumes_line'] = 'Google-Suchen pro Monat (Region Dannenberg / Wendland): <b>heilpraktiker dannenberg 20</b> · heilpraktiker uelzen 70 · akupunktur uelzen 50. Startwert Behandlung: 100 € (typischer Stundensatz für Heilpraktiker-Leistungen). Budget, Anfrage- und Buchungsanteil sind Annahmen.'

p['check'][0]['rows'][0]['text'] = 'Die hinterlegte Webadresse liefert aktuell einen 404-Fehlerbildschirm, sodass Telefonnummer und Kontakt nicht erreichbar sind.'
p['check'][0]['rows'][1]['text'] = 'Die Now.site-Domain lädt ein Fehler-Template statt deiner Praxis-Website.'
p['check'][0]['rows'][2]['text'] = 'Es gibt aktuell keine funktionierende Kontakt-Seite und kein Terminformular.'

p['check'][1]['rows'][0]['text'] = 'Google findet wegen der Fehlerseite keine Hauptüberschrift mit den Begriffen Heilpraktiker oder Dannenberg.'
p['check'][1]['rows'][1]['text'] = 'Eine Meta-Beschreibung für Google-Suchtreffer fehlt durch den 404-Status vollständig.'

p['check'][2]['rows'][0]['text'] = 'Auf der Website ist keine Besuchermessung oder Webanalyse auffindbar.'
p['check'][2]['rows'][1]['text'] = 'Strukturierte Standort- und Praxisdaten für Google fehlen derzeit.'

p['check'][3]['rows'][0]['text'] = '0 Bewertungen im Google-Profil. Mitbewerber wie Günther Bentz (2) oder Vitalplus (11) liegen vorn.'

p['quick_wins'] = [
    {
        'title': 'Google-Unternehmensprofil beanspruchen',
        'text': 'Den Eintrag bei Google offiziell als Inhaber bestätigen, um alle Profilfunktionen freizuschalten.'
    },
    {
        'title': 'Toten Website-Link reparieren',
        'text': 'Die fehlerhafte Now.site-Adresse durch eine erreichbare Seite oder digitale Praxis-Visitenkarte austauschen.'
    },
    {
        'title': 'Telefonnummer & Zeiten einpflegen',
        'text': 'Eine direkt anklickbare Rufnummer und verlässliche Sprechzeiten im Google-Eintrag hinterlegen.'
    },
    {
        'title': 'Erste 3 Patientenbewertungen sammeln',
        'text': 'Zufriedene Patienten direkt nach der Behandlung ansprechen, um sofort zu den Spitzenreitern aufzuschließen.'
    },
    {
        'title': 'Leistungen im Profil eintragen',
        'text': 'Schmerztherapie, Akupunktur und Naturheilkunde als feste Leistungsbausteine im Profil hinterlegen.'
    },
    {
        'title': 'Praxisschild & Fotos hochladen',
        'text': 'Fotos von Praxisgebäude und Behandlungsraum in Google Maps ergänzen für sofortige Wiedererkennung.'
    }
]

p['roadmap'] = [
    {
        'step': 'Woche 1–2 · Fundament reparieren',
        'what': 'Google-Profil beanspruchen, Telefonnummer eintragen und den 404-Weblink durch eine saubere Seite ersetzen',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Ohne funktionierenden Link und Telefonnummer gehen heute alle Interessenten verloren'
    },
    {
        'step': 'Woche 1–3 · Bewertungen aufbauen',
        'what': 'Gezielt 3 bis 5 zufriedene Patienten um eine Google-Rezension bitten',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Mitbewerber führen mit nur 2 bis 11 Bewertungen – die Lücke ist schnell geschlossen'
    },
    {
        'step': 'Woche 2–4 · Praxisseite aktivieren',
        'what': 'Schlanke Startseite mit Schmerztherapie, Akupunktur und klarer Anfahrt aus Dannenberg und Lüchow',
        'prio': 'Hoch',
        'effort': 'Mittel',
        'why': 'Aus Website-Besuchern werden verbindliche Ersttermine'
    },
    {
        'step': 'Woche 3–8 · Regionale Vernetzung',
        'what': 'Einträge in relevanten Therapeuten-Verzeichnissen und lokale Verlinkungen im Wendland',
        'prio': 'Mittel',
        'effort': 'Gering',
        'why': 'Stärkt die Autorität der Praxis bei Google für das gesamte Einzugsgebiet'
    },
    {
        'step': 'Laufend · Messen',
        'what': 'Monatliche Kartenmessung und Tracking der Neupatienten-Anrufe',
        'prio': 'Mittel',
        'effort': 'Gering',
        'why': 'Jeder Schritt muss zu messbar mehr Behandlungen führen'
    }
]

p['proof'] = {
    'h2': 'Andere Praxen und Therapeuten hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'lead': 'Ausgewählt nach deiner Praxisgröße: Heilpraxen und Therapeuten, die lokal zur festen Adresse wurden.',
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
    'h2': 'Lass uns in 30 Minuten anschauen, wie wir deinen Google-Eintrag reparieren und deine Praxis nach vorn bringen.',
    'p': '30 Minuten, kostenlos: Ich zeige dir live, wie du die 404-Hürde nimmst und mit wenigen Handgriffen zur sichtbaren Praxis im Raum Dannenberg wirst. Unverbindlich.',
    'subject': 'Roland%20Parbs%20Sichtbarkeits-Analyse'
}

p['guide'] = {
    'hello': 'Ich habe mir deine Webadresse und deinen Google-Eintrag genau angesehen. Hier zeige ich dir, was ich gemessen habe.',
    'point': 'Günther Bentz führt mit nur 2 Bewertungen die Karte an. Dein Eintrag steht an 1 von 49 Punkten unter den Top 3, und deine Website liefert einen 404-Fehler.',
    'think': 'Im Wendland ist der Wettbewerb überschaubar. Wer eine funktionierende Seite hat und 3 Bewertungen vorweist, steht ganz vorn.',
    'insight': 'Der größte Hebel: Das Google-Profil beanspruchen, den toten Link reparieren und die ersten 3 Patientenrezensionen sammeln.',
    'celebrate': 'Mit wenigen klaren Handgriffen kannst du im Raum Dannenberg zur ersten Anlaufstelle für Naturheilkunde werden.'
}

p['headlines'] = {
    'hero_h1': 'Roland, so finden Patienten <span style="color:var(--brand--lemon);">in Dannenberg</span> deine Praxis.<span style="display:block;font-size:.42em;line-height:1.35;font-weight:600;letter-spacing:0;color:#5c5c5c;margin-top:16px;">Bei „heilpraktiker dannenberg“ steht deine Praxis an nur 1 von 49 Punkten unter den Top 3. Hier ist dein Fahrplan.</span>',
    'hero_sub': 'Dein Google-Profil hat 0 Bewertungen und ist unbestätigt. Bei der Suche „heilpraktiker dannenberg“ ist deine Praxis an nur 1 von 49 Punkten unter den ersten drei – und deine hinterlegte Website zeigt einen 404-Fehler.',
    'grid_h2': 'Unter den ersten drei an nur 1 von 49 Punkten. Im Großraum Dannenberg kaum sichtbar.',
    'proof_h2': 'Andere Praxen und Therapeuten hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'system_h2': 'Drei Hebel für mehr Patienten, und bei jedem fehlt heute ein Schritt',
    'step1_h2': 'Nach „heilpraktiker dannenberg“ wird 20-mal im Monat gesucht. Deine Website ist aktuell nicht erreichbar.',
    'step2_h2': 'Günther Bentz führt mit nur 2 Bewertungen. Dein Google-Profil ist noch unbestätigt.',
    'step3_h2': 'Besucher entscheiden in 5 Sekunden. Deine Website zeigt heute einen 404-Fehlerbildschirm.',
    'calc_h2': 'Was neue Patienten für deine Praxis bedeuten',
    'check_h2': 'Was deine Website heute richtig macht und wo du Interessenten verlierst',
    'quickwins_h2': 'Sechs Schritte, die du schon nächste Woche umsetzen kannst, ohne neue Website',
    'roadmap_h2': 'Dein Plan für die nächsten 8 Wochen, Schritt für Schritt',
    'final_h2': 'Lass uns in 30 Minuten anschauen, wie wir deinen Google-Eintrag reparieren und deine Praxis nach vorn bringen.'
}

p['sources']['grid'] = 'evidence/falcon-report-65631fcef076bb8.json (keyword heilpraktiker dannenberg, 7x7, 10.0 km, centre 53.0840/11.1955, 16.10.2026; solv 2.04 = 1/49, found_in 29) + review-assets/roland-parbs/scan-grid.webp'
p['sources']['calc'] = 'evidence/dfs-volumes-ads.json (volume heilpraktiker dannenberg 20); val 90 aus typischem Heilpraktiker-Stundensatz; budget/conv/deal = assumptions, labelled'

with open(pfile, 'w', encoding='utf-8') as f:
    json.dump(p, f, indent=2, ensure_ascii=False)

print('Updated Roland Parbs prospect.json successfully!')
