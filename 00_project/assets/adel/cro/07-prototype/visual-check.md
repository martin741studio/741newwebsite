# Visual Check — Startseite Rechtsanwältin Aydan Adel (Prototyp v1)

Datum 2026-10-10. Geprüft in Claude in Chrome (externes Chrome), Seite über `python3 -m http.server 8801`. Fenster 1440×900 gesetzt, **echter Viewport 1440×757** (innerWidth 1440, innerHeight 757; im ersten Durchgang 1421×701, Scrollleiste). Seite einmal von oben nach unten in Schritten von 600 bis 700 px gescrollt, danach Zusatzprüfungen per JavaScript. Ohne `?shot=1`, echtes Reveal-Verhalten.

## Gemessene Prüfungen

| # | Prüfung | Ergebnis | Wert |
| --- | --- | --- | --- |
| M1 | innerWidth | ok | 1440 (Zwischenstand 1421 mit Scrollleiste) |
| M2 | Kein horizontales Scrollen | ok | scrollWidth 1406 bei innerWidth 1421, später 1440 |
| M3 | Konsolenfehler und Netzwerkfehler | ok | keine Fehler, 12 Requests alle 200 (Fonts, 2 Bilder) |
| M4 | Bilder geladen, nicht hochskaliert | ok | hero-portrait 1024 px natürlich bei 406 px Anzeige, about-portrait 1024 bei 484 px |
| M4b | Keine Verzerrung | ok | beide Bilder `object-fit: cover`, Anzeige 406×527 und 484×605 |
| M5 | Schriften geladen | ok | Newsreader 500 und 600 (auch Kursiv 500), Manrope 400 bis 800 |
| M6 | Links | ok mit Ausnahmen | Anker alle vorhanden. WhatsApp 11 Links mit Vorbelegung, `tel:+4917643523159` einheitlich. 16 Platzhalter `#`: 12 mal "Mehr erfahren" (Leistungsseiten), Google-Bewertungen, "Karte laden", Datenschutz, Cookie-Einstellungen |
| M7 | Reveal vollständig | ok | 0 versteckte Elemente nach einem Durchlauf, alle 25 Wörter des Statements hell |
| M8 | Hero-CTA im ersten Bildschirm | ok | CTA-Unterkante bei 620 px (Viewport 701), Bewertungszeile bei 540 px |
| M9 | Schriftgrößen | ok mit Ausnahme | Alles mindestens 14 px. Menü, Buttons, Fließtext, Fußzeile mindestens 16 px. Ausnahme: Wortmarken-Zusatz "RECHTSANWÄLTIN" 10,5 px (Teil der Wortmarke, bewusst) |
| M10 | Breathing nur Hero und Abschluss | ok | genau 2 Elemente mit Animation `breathe`, pausiert bei Hover |
| M11 | Text gleich Freigabetext | ok | 211 Textsegmente, 1 Abweichung: Prototyp-Hinweis im Fuß (bewusst) |

## Globale Punkte

| # | Prüfung | Ergebnis |
| --- | --- | --- |
| G1 | Raster, Ausrichtung | ok. Container 1216 px, alle Sektionen am gleichen linken Rand 144 px |
| G2 | Abstände | ok. Sektionen 120 px, Standort 140 px |
| G3 | Text | fixed: H1 brach "Bonn." in eigene Zeile (Schrift 72 zu 64 px, `white-space:nowrap`); Überschrift "5,0 Sterne bei 18 Google-Bewertungen" brach unglücklich (Breite 820 zu 1000 px); Abschluss-Überschrift hatte Waise "Anliegen." (`text-wrap:balance`) |
| G4 | Bilder | ok. Beide Personenbilder scharf, gleiche Frau, keine Textreste, Gesicht nicht verzerrt. Beide sind KI-Entwürfe, Shoot-Liste im Handoff |
| G5 | Farbe | ok. Nur Bronze als Button-Farbe. Blur-Test: der Bronze-Button gewinnt im Hero und im Abschluss |
| G6 | Schrift | ok. Nur Newsreader und Manrope. Zeilenlänge Fließtext unter 75 Zeichen |
| G7 | Buttons, Links | ok. Bronze-Pille, Umriss-Pille, Textlink mit Pfeil, überall gleich |
| G8 | Vergleich mit dem Mockup | ok mit bewussten Abweichungen: (1) Leistungen als nummerierte Zeilen statt Kästen (Ronas-Muster, intended); (2) Sub-Headline in Tinte statt Bronze (Kontrast, intended); (3) Bewertungszeile steht über den Buttons, damit Beweis und CTA zusammen im ersten Bildschirm sind (intended); (4) Pfeil im Hero-Button entfällt, sonst bricht der Telefon-Button um (fixed) |
| G9 | Hover | ok. CTA hebt sich, Pfeil rückt, Breathing stoppt. Menü und Wortmarke reagieren |
| G10 | Sticky Header | ok. Alle sechs Menüpunkte landen mit Sektionsrand bei 96 px, Überschrift bei 216 px, nicht verdeckt |

## Sektionen

| Sektion | Prüfung | Ergebnis |
| --- | --- | --- |
| Kopf | Wortmarke, Menü einzeilig, Header bleibt | ok. fixed: Menü auf 16 px |
| 1 Hero | H1 vollständig, drei Zeilen mit Wellen, Kreis-Badge, Namensschild | ok. fixed: Telefon-Button brach um (Spalte 1,55/0,9, Padding), Rating und CTA im ersten Bildschirm |
| 1 Hero | Wellenlinien zeichnen einmal | ok |
| 2 Beweis-Leiste | fünf Belege auf einer Linie, Zitat mit Namen | ok |
| 3 Wann Sie mich brauchen | Statement hellt beim Scrollen auf, 6 Zeilen, 2 Spalten gleich hoch | ok. fixed: Statement blieb am Ende grau (Fortschrittsformel) |
| 4 Leistungen | drei Blöcke 01 bis 03, je vier Teilleistungen, Links auf einer Linie | fixed: "Mehr erfahren" saß je nach Textlänge verschieden hoch |
| 5 Weg zur Beratung | Linie zeichnet einmal, Kreise füllen sich nacheinander, Schritte gleich hoch | ok. Dauer und Preis mit [FEHLT]-Marke |
| 6 Über mich | Porträt, Zeitleiste, zwei Buttons | ok |
| 7 Bewertungen | drei offene Karten, Google-Logo, Vorname | ok. fixed: Überschriftenumbruch |
| 8 Sicher und transparent | zwei Spalten mit Haken | ok |
| 9 FAQ | öffnet und schließt, nur eine offen, Plus wird Minus | ok (geprüft per Klick: Frage 2 offen, Frage 1 zu) |
| 10 Standort | Karten-Platzhalter, Pin, vier Zeilen mit Symbolen, zwei Buttons | ok. [FEHLT: Karte] sichtbar |
| 11 Abschluss | Wellenkante, Überschrift, drei Haken, Sterne, drei Wege | ok. fixed: Waise in Überschrift, Seitenleiste unsichtbar auf dunklem Band (weißer Ring) |
| Fuß | Adresse, Telefon, Mail, Rechtliches | ok. Datenschutz mit [FEHLT]. Sprachleiste bricht in zweite Zeile (akzeptiert) |
| Rail links | feste Symbolleiste LinkedIn, Instagram, WhatsApp | ok |

## Interaktion

- WhatsApp-CTA im Hero: `https://wa.me/4917643523159?text=Guten Tag Frau Adel, ich möchte eine Erstberatung anfragen. Mein Thema: ` (nicht gesendet).
- Telefon: `tel:+4917643523159`.
- Menü: sechs Anker geprüft.
- Zurückscrollen: nichts animiert erneut (Beobachter entfernt nach erstem Reveal).

## Ergebnis

Fixed (9): H1-Umbruch, Telefon-Button-Umbruch, Beweis im ersten Bildschirm, Rail-Sichtbarkeit auf Dunkel, Waise in der Abschluss-Überschrift, Bewertungs-Überschrift, Schriftgrößen unter 16 px, Link-Ausrichtung in den Leistungen, Statement-Reveal.
Offen (Daten, nicht lösbar ohne Kundin): [FEHLT] Dauer und Preis der Erstberatung, Karte mit Einwilligung, Datenschutz, Google-Link, Leistungsseiten (Platzhalter `#`).

**Visual check done in Chrome, 41 items checked, 9 fixed, 0 open** (die offenen Daten stehen als [FEHLT] in `self-check.md` und im Handoff).

## Nachtrag nach unabhängiger Prüfung (2026-10-11)

Ein frischer Prüf-Agent fand 12 Lücken. Behoben: M7-Zahl der Statement-Wörter (25, nicht 56), sichtbare [FEHLT]-Marke am Google-Link, Bild-Alt-Texte als KI-Platzhalter, Fuß-Telefon als `tel:`-Link, Schema ohne Köln und ohne Bild-Feld. Die Änderungen an Link, Alt-Texten und Schema wurden per Skript (`verify.py`) geprüft. Die [FEHLT]-Marke am Google-Link wurde im Screenshot neu geprüft.
