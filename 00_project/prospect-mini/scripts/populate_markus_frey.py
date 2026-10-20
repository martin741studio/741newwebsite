#!/usr/bin/env python3
import json, os

pfile = '00_project/prospects/markus-frey/prospect.json'
with open(pfile, 'r', encoding='utf-8') as f:
    p = json.load(f)

p['business_ref'] = 'deine Akademie'

p['hero']['sub'] = 'Du hast 5,0 Sterne bei Google. Bei der Suche „life coach köln“ bist du an 5 von 49 Punkten unter den ersten drei, in weiten Teilen der Stadt aber nicht unter den ersten 20.'
p['hero']['cards'][0]['sub'] = 'Life Coach · Stressmanagement & Burnout-Prävention · Köln-Mülheim'
p['hero']['cards'][1]['badge'] = 'In der Stadtmitte von Köln auf Platz 20+'
p['hero']['cards'][2]['sub'] = 'Du: 1 Bewertung · Wer bist Du Baby: 17 Bewertungen'
p['hero']['cards'][3]['sub'] = 'Erster Bildschirm: Slogan „Spitzenenergie“, E-Book-Button statt Kennenlerngespräch, keine Sterne sichtbar'
p['hero']['cards'][3]['badge'] = 'Startseite heute: 13 von 42 Punkten'

p['grid']['h2'] = 'Unter den ersten drei an 5 von 49 Punkten. Im Kölner Zentrum nicht unter den ersten 20.'
p['grid']['caption_today'] = '<b>Unter den ersten drei an 5 von 49 Punkten.</b> Zu sehen bist du vor allem im Nordosten rund um deinen Standort in Köln-Mülheim. In der Kölner Innenstadt stehst du auf Platz 20+. Der führende Anbieter Wer bist Du Baby erreicht 42,9 % Sichtbarkeit.'
p['grid']['caption_goal'] = '<b>Ziel: Sichtbarkeit in ganz Köln, wo Monat für Monat 210 Menschen nach einem Life Coach suchen.</b> Die Anbieter vorn haben 17 bis 42 Bewertungen.'
p['grid']['chips'] = [
    '📞 Direkte Anrufe aus der Google-Karte',
    '🧭 Klienten aus ganz Köln finden dein Angebot',
    '🤝 Mehr Anfragen für dein Kennenlern-Coaching'
]

p['system']['intro'] = 'Für deine Akademie haben wir drei Hebel geprüft: wonach Menschen in Köln suchen, warum andere Coaches in der Karte vorn stehen und ob deine Website Besucher zu Anfragen macht. Jede Zahl stammt aus echten Messungen.'
p['system']['steps'][2]['kpi'] = 'heute 13 von 42 Punkten'

p['system']['step1']['h2'] = 'Nach „life coach köln“ wird 210-mal im Monat gesucht. Deine Website steht dafür nicht unter den ersten 20 Treffern.'
p['system']['step1']['lead'] = 'Wir haben deine Website mit den Angeboten verglichen, die bei „life coach köln“ oben stehen, und mit den Begriffen, die Menschen in der Region wirklich suchen.'
p['system']['step1']['demand_note'] = '„life coach köln“ hat 210 Suchanfragen pro Monat. Zu speziellen Themen wie „stressmanagement köln“ oder „burnout prävention köln“ gibt es weitere Nachfrage, für die auf deiner Website eigene Unterseiten fehlen.'

p['system']['step1']['depth']['title'] = 'Wenig Text auf der Startseite und Köln fehlt in der Hauptüberschrift.'
p['system']['step1']['depth']['sub'] = 'Deine Startseite hat 324 Wörter. Der Begriff „Life Coach“ oder „Köln“ taucht in deiner Hauptüberschrift gar nicht auf.'
p['system']['step1']['depth']['note'] = 'In deiner Hauptüberschrift steht ein Bildslogan („Spitzenenergie“), aber weder dein Beruf noch dein Standort.'

p['system']['step1']['items'] = [
    {
        'title': 'Startseite auf Life Coach in Köln ausrichten',
        'tag': 'Ort',
        'why': 'Deine Startseite nennt heute weder „Life Coach“ noch „Köln“ im sichtbaren Kopfbereich.'
    },
    {
        'title': 'Eigene Seite zu „stressmanagement köln“',
        'tag': 'Leistung',
        'why': '„stressmanagement köln“ hat 20 Suchen pro Monat. Auf deiner Seite gibt es dafür bisher keine eigene Unterseite mit klarem Ortsbezug.'
    },
    {
        'title': 'Eigene Seite zu „burnout prävention köln“',
        'tag': 'Leistung',
        'why': '„burnout prävention köln“ hat 10 Suchen pro Monat. Bisher fehlt eine fokussierte Seite zu diesem Thema.'
    },
    {
        'title': 'Eigene Seite zu „energiemanagement köln“',
        'tag': 'Leistung',
        'why': '„energiemanagement köln“ wird monatlich gesucht, ist aber auf deiner Website nicht als eigenes Angebot ausgebaut.'
    },
    {
        'title': 'Eigene Seite zu „stressmanagement leverkusen“',
        'tag': 'Leistung',
        'why': 'Auch im benachbarten Leverkusen suchen Menschen nach Stressmanagement.'
    },
    {
        'title': 'Klares Profil als Coach',
        'tag': 'Profil',
        'why': 'Wer nach einem Life Coach oder Stressmanagement in Köln sucht, braucht sofort Klarheit über deinen Ansatz und deinen Standort.'
    }
]

p['system']['step2']['h2'] = 'In der Kölner Innenstadt steht deine Akademie auf Platz 20+. Andere Coaches teilen den Markt unter sich auf.'
p['system']['step2']['meaning'] = 'Die führenden Anbieter in Köln haben 17 bis 42 Bewertungen und teilen die vorderen Plätze unter sich auf. Du hast erst 1 Bewertung und bist im Zentrum noch unsichtbar.'

p['system']['step2']['changes'] = [
    {
        'title': 'Kategorie im Google-Eintrag optimieren',
        'text': 'Prüfe neben „Life Coach“ auch verwandte Kategorien wie Coaching-Zentrum oder Beratung, um dein Profil zu stärken.'
    },
    {
        'title': 'Alle Leistungen eintragen',
        'text': 'Trage deine konkreten Coaching-Formate, Vorträge und Methoden einzeln im Google-Unternehmensprofil ein.'
    },
    {
        'title': 'Aktive Bewertungseinladungen',
        'text': 'Zufriedene Klienten systematisch nach einer Google-Bewertung fragen, um von 1 auf 15+ Bewertungen aufzuschließen.'
    },
    {
        'title': 'Auf Bewertungen antworten',
        'text': 'Beantworte jede Rezension persönlich. Das signalisiert Google und neuen Interessenten Verlässlichkeit.'
    },
    {
        'title': 'Fotos vom Standort und Coaching',
        'text': 'Echte Einblicke in deine Räume in Köln und Porträtfotos schaffen sofortiges Vertrauen.'
    },
    {
        'title': 'Regelmäßige Google-Beiträge',
        'text': 'Kurze Impulse und Praxis-Tipps im Google-Profil zeigen, dass deine Akademie aktiv Klienten betreut.'
    }
]

p['system']['step2']['cleanup'] = [
    {
        'n': '34 / 95',
        'text': 'Websites, die auf deine Seite verlinken, sind unseriös (z. B. Spam-Verzeichnisse). Diese sollten bereinigt werden.'
    },
    {
        'n': '0 / 1',
        'text': 'Bewertungen mit einer Antwort von dir.'
    }
]

p['system']['step3']['score_draft_label'] = 'Ziel: 34+ / 42'
p['system']['step3']['note_today'] = 'Im ersten Bildschirm sieht man den Slogan „Spitzenenergie“ und einen Button zum E-Book. Es wird nicht sofort klar, dass du persönliches Coaching in Köln anbietest.'
p['system']['step3']['note_draft'] = 'Klarer Fokus: Markus Frey als Life Coach in Köln, dein Porträt, Kundenstimmen und ein direkter Button zum kostenlosen Kennenlerngespräch.'

p['system']['step3']['five'] = [
    {
        'q': 'Was?',
        'a': '„Spitzenenergie – auch morgen noch!“. Das Wort Coaching steht erst weiter unten im Fließtext.'
    },
    {
        'q': 'Wo?',
        'a': 'Köln wird im ersten Bildschirm nicht genannt; der Standort Mülheim ist unsichtbar.'
    },
    {
        'q': 'Warum du?',
        'a': 'Keine Bewertungen, Kundenstimmen oder Auszeichnungen im sichtbaren Bereich.'
    },
    {
        'q': 'Wie zum Erstgespräch?',
        'a': 'Der Hauptbutton bietet ein E-Book an, statt direkt zum Kennenlerngespräch zu führen.'
    },
    {
        'q': 'Wer?',
        'a': 'Ein kleines Video-Vorschaubild, aber kein klares Porträt mit Namen direkt in der Überschrift.'
    }
]

p['system']['step3']['strip'] = [
    {
        'photo': '/review-assets/markus-frey/foto-1.webp',
        'title': 'Markus Frey als Life Coach in Köln',
        'why': 'Klienten wollen sofort wissen, wer sie coacht und wo das Coaching stattfindet.'
    },
    {
        'photo': '/review-assets/markus-frey/foto-2.webp',
        'title': 'Direkter Weg zum Kennenlerngespräch',
        'why': 'Statt eines E-Books sollte der direkte Kontakt im Mittelpunkt stehen.'
    },
    {
        'photo': '/review-assets/markus-frey/foto-3.webp',
        'title': 'Vertrauen durch Sterne und Feedback',
        'why': 'Bewertungen und Erfahrungen nehmen die Hürde vor dem ersten Anruf.'
    }
]

p['system']['step3']['good'] = 'Deine Website hat ein klares Farbkonzept und ansprechende Fotos. Mit einer klareren Ausrichtung auf das Erstgespräch und deinen Standort Köln wird daraus ein wirksamer Kundenmagnet.'

p['calc']['val'] = 300
p['calc']['val_label'] = 'Umsatz pro neuem Klienten (Startwert 300 €)'
p['calc']['volumes_line'] = 'Echte Google-Suchen pro Monat (ganz Deutschland, Mittel der letzten 12 Monate): <b>life coach köln 210</b> · stressmanagement köln 20. Ein Anzeigen-Klick auf „life coach köln“ kostet bei Google rund <b>2,53 US-Dollar</b> (Google-Angabe in Dollar; der Regler startet ohne Umrechnung bei 2,50 €) (Abruf 15.10.2026). Startwert Umsatz: geschätzte 300 € pro Klient (z. B. Einstiegscoaching). Budget, Anfrage- und Buchungsanteil sind Annahmen.'

p['system']['step2']['good'] = 'Das Gute: Mit 5,0 Sternen und einem bestehenden Profil hast du bereits ein Fundament. Mit gezielten Leistungen, Fotos und ersten neuen Bewertungen kannst du schnell aufschließen.'

# Fix check card 0 (Deine Website)
p['check'][0]['rows'][0]['title'] = 'Telefonnummer nicht als Anruf-Link hinterlegt'
p['check'][0]['rows'][0]['text'] = 'Auf deiner Website ist keine Telefonnummer als anklickbarer tel:-Link hinterlegt. Am Smartphone können Besucher nicht direkt per Fingertipp anrufen.'

# Fix check card 1 (Was Google liest)
p['check'][1]['rows'][0]['text'] = 'Deine Startseite hat heute keine H1-Hauptüberschrift im HTML-Code, sondern Textgrafiken ohne die Suchbegriffe Life Coach oder Köln.'
p['check'][1]['rows'][1]['text'] = '1 von 30 Seiten (die Startseite) hat keine H1-Hauptüberschrift im HTML.'
p['check'][1]['rows'][2]['text'] = 'Die heutige Meta-Beschreibung ist sehr lang und wird in den Google-Suchergebnissen abgeschnitten.'

# Fix check card 2 (Was du messen kannst)
p['check'][2]['rows'][1]['text'] = 'Ein strukturierter Datenblock ist vorhanden; lokale Adress- und Leistungsdaten sollten noch ergänzt werden.'

# Fix check card 3 (Dein Ruf im Netz)
p['check'][3]['rows'][1]['text'] = 'Mit 1 Bewertung liegst du hinter Anbietern wie Wer bist Du Baby mit 17 Bewertungen.'
p['check'][3]['rows'][3]['text'] = '34 von 95 verlinkenden Websites weisen einen hohen Spam-Wert auf und sollten bereinigt werden.'

p['quick_wins'] = [
    {
        'title': 'Köln und Life Coach in den Seitentitel',
        'text': '„Life Coach in Köln – StressFrey-Akademie Markus Frey“ als prägnanter Titel deiner Startseite.'
    },
    {
        'title': 'Button zum Kennenlerngespräch nach oben',
        'text': 'Im ersten Bildschirm den E-Book-Download durch einen Button „Kostenloses Kennenlerngespräch“ ersetzen.'
    },
    {
        'title': 'Deine 5 Sterne sichtbar machen',
        'text': 'Die 5-Sterne-Bewertung direkt neben deinem Porträt im ersten Bildschirm platzieren.'
    },
    {
        'title': 'Unterseite für Stressmanagement in Köln anlegen',
        'text': 'Eine eigene Money-Page für „Stressmanagement Köln“ erstellen, um die 20 monatlichen Suchanfragen abzufangen.'
    },
    {
        'title': 'Google-Unternehmensprofil vervollständigen',
        'text': 'Alle Coaching-Leistungen und genaue Öffnungszeiten im Profil hinterlegen.'
    },
    {
        'title': 'Aktive Bewertungseinladungen starten',
        'text': 'Bestehende und frühere Klienten gezielt um eine kurze Google-Rezension bitten.'
    }
]

p['roadmap'] = [
    {
        'step': 'Woche 1–2 · Aufräumen',
        'what': 'Seitentitel und Beschreibung bei Google neu ausrichten, Spam-Links entwerten, Google-Profil schärfen',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Erst aufräumen, dann ausbauen'
    },
    {
        'step': 'Woche 1–3 · Telefon klingeln',
        'what': 'Google-Eintrag ausbauen: Kategorien, Leistungen, Fotos und erste neue Bewertungen einsammeln',
        'prio': 'Hoch',
        'effort': 'Gering',
        'why': 'Aktuell bist du in der Kölner Innenstadt auf Platz 20+ und verlierst täglich suchende Klienten'
    },
    {
        'step': 'Woche 2–4 · Startseite',
        'what': 'Erster Bildschirm mit „Life Coach in Köln“, 5 Sternen, Porträt und Button zum Kennenlerngespräch',
        'prio': 'Hoch',
        'effort': 'Mittel',
        'why': 'Aus Besuchern werden Erstgespräche'
    },
    {
        'step': 'Woche 3–8 · Neue Inhalte',
        'what': 'Gezielte Unterseiten für „Stressmanagement Köln“, „Burnout-Prävention“ und Nachbarstädte wie Leverkusen',
        'prio': 'Hoch',
        'effort': 'Mittel',
        'why': 'Seiten für die Themen, die Klienten wirklich bei Google eingeben'
    },
    {
        'step': 'Laufend · Messen',
        'what': 'Besucherzahlen, Anfragen für Kennenlerngespräche und monatliche Kartenmessung verfolgen',
        'prio': 'Mittel',
        'effort': 'Gering',
        'why': 'Jede Maßnahme muss sich in planbaren Zahlen zeigen'
    }
]

p['proof'] = {
    'h2': 'Andere Berater und Coaches hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'lead': 'Ausgewählt nach deiner Ausgangslage: Coaching- und Beratungspraxis mit starker Expertise, die lokal sichtbarer werden wollten.',
    'featured': [
        'lengauer',
        'schlirf',
        'laserstein',
        'abel'
    ],
    'labels': {
        'lengauer': 'Auch Beratung & Coaching, vorher:'
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
    'h2': 'Lass uns in 30 Minuten anschauen, wer in Köln oben steht und wie deine Akademie dorthin kommt.',
    'p': '30 Minuten, kostenlos: Ich zeige dir live deinen Markt in Köln und welche Schritte für dein Coaching die meiste Wirkung haben. Unverbindlich.',
    'subject': 'StressFrey-Akademie%20K%C3%B6ln%20Sichtbarkeits-Analyse'
}

p['guide'] = {
    'hello': 'Ich habe mir stressfrey.de und deinen Google-Eintrag genau angesehen. Hier zeige ich dir, was ich gefunden habe.',
    'point': 'Bei „life coach köln“ bist du an 5 Punkten sichtbar, im Zentrum aber nicht unter den ersten 20. Der Marktführer erreicht 42,9 % Sichtbarkeit.',
    'think': 'Mit 210 monatlichen Suchen nach „life coach köln“ gibt es echte Nachfrage. Die Frage ist, wie viel davon heute bei dir ankommt.',
    'insight': 'Der größte Hebel: deine Startseite direkt auf das Kennenlerngespräch ausrichten und deinen Google-Eintrag gezielt stärken.',
    'celebrate': 'So sieht es aus, wenn das System greift: Aus einer unsichtbaren Position wird eine verlässliche Anlaufstelle in deiner Stadt.'
}

p['headlines'] = {
    'hero_h1': 'Markus, so finden dich Klienten <span style="color:var(--brand--lemon);">in Köln</span> bei Google.<span style="display:block;font-size:.42em;line-height:1.35;font-weight:600;letter-spacing:0;color:#5c5c5c;margin-top:16px;">Bei „life coach köln“ bist du an 5 von 49 Punkten unter den ersten drei. Hier ist dein Fahrplan für ganz Köln.</span>',
    'hero_sub': 'Du hast 5,0 Sterne bei Google. Bei der Suche „life coach köln“ bist du an 5 von 49 Punkten unter den ersten drei, in weiten Teilen der Stadt aber nicht unter den ersten 20.',
    'grid_h2': 'Unter den ersten drei an 5 von 49 Punkten. Im Kölner Zentrum nicht unter den ersten 20.',
    'proof_h2': 'Andere Berater und Coaches hatten ähnliche Lücken. So hat sich ihre Sichtbarkeit verändert.',
    'system_h2': 'Drei Hebel für mehr Klienten, und bei jedem fehlt heute ein Schritt',
    'step1_h2': 'Für „life coach köln“ zählt Google 210 Suchen im Monat. Deine Website steht dafür nicht unter den ersten 20 Treffern.',
    'step2_h2': 'Wer bist Du Baby führt mit 42,9 % Sichtbarkeit. Deine Akademie erreicht 10,2 %.',
    'step3_h2': 'Besucher entscheiden in 5 Sekunden. Deine Startseite bietet heute ein E-Book statt ein Kennenlerngespräch.',
    'calc_h2': 'Was neue Klienten über Google für deine Akademie bedeuten',
    'check_h2': 'Was deine Website heute richtig macht und wo du Interessenten verlierst',
    'quickwins_h2': 'Sechs Schritte, die du schon nächste Woche umsetzen kannst, ohne neue Website',
    'roadmap_h2': 'Dein Plan für die nächsten 8 Wochen, Schritt für Schritt',
    'final_h2': 'Lass uns in 30 Minuten anschauen, wer in Köln oben steht und wie deine Akademie dorthin kommt.'
}

p['sources']['grid'] = 'evidence/falcon-report-5bd7097be1b0e31.json (keyword life coach köln, 7x7, 5.0 km, centre 50.9375/6.9603, 16.10.2026; solv 10.20 = 5/49, found_in 9) + review-assets/markus-frey/scan-grid.webp'
p['sources']['calc'] = 'evidence/dfs-volumes-ads.json (volume life coach köln 210, cpc 2.53 -> slider 2.5); val 300 = Coaching-Erststunde / Paket-Annahme (site-findings.md); budget/conv/deal = assumptions, labelled'

with open(pfile, 'w', encoding='utf-8') as f:
    json.dump(p, f, indent=2, ensure_ascii=False)

print('Updated prospect.json successfully!')
