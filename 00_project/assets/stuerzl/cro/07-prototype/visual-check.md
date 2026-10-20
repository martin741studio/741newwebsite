# Visual Check — Startseite STÜRZL Steuerstrafrecht (Prototyp v1)

Datum 2026-10-11 · geprüft in Claude in Chrome (externes Chrome, nicht das Browser-Panel) · Server `python3 -m http.server 8821` · echter Viewport 1512 × 801 (das Chrome-Fenster ließ sich nicht auf 1440 schmaler stellen; `resize_window` ändert den Viewport hier nicht), ohne `?shot=1` · Seitenhöhe 8.757 bis 9.010 px je nach geöffneter FAQ-Frage. Zusätzlich headless Screenshots bei 1440 px (`screenshots/`).

## Gemessene Prüfungen (scripts/measure.js, Chrome)
| # | Prüfung | Ergebnis | Wert |
| --- | --- | --- | --- |
| M1 | Breite | Hinweis | 1512 × 801 statt 1440 (Fensterbreite des Macs). Layout trägt bei 1440 (headless geprüft) |
| M2 | kein horizontaler Scroll | ok | scrollWidth ≤ innerWidth |
| M3 | Konsole und Netz | ok | 0 Konsolenfehler; 13 Requests, alle Status 200 (Seite, 5 Bilder, Google Fonts) |
| M4 | Bilder geladen, nicht hochskaliert | ok | hero 2112×900 → 898×624, office 1400×933 → 330×264, about 1280×853 → 480×492, Logo SVG |
| M4b | keine Verzerrung | ok | alle `object-fit: cover` oder SVG, `height:auto` |
| M5 | Schriften | ok | Manrope und Newsreader geladen |
| M6 | Links | ok mit Liste | Anker alle vorhanden; `tel:` Frankfurt +4969298028870, München +498972444170, Notfall +491603396513 und +4916095945730 (zwei Fehler behoben: erste Fassung hatte je eine Ziffer zu wenig; der Hero-Button wählte für beide Nummern Frankfurt, jetzt zwei getrennte Links); 12 Links mit `#` (siehe Offen) |
| M7 | Reveals | ok | 0 versteckt nach Abwärts- und Aufwärts-Scroll |
| M8 | Hero-CTA im ersten Bildschirm | ok | Unterkante 636 px (Höhe 801) |
| M9 | Textgröße | ok | Body, Menü, Buttons, Karten, Fuß ≥ 16 px. Unter 16: Eyebrow 15 px und die Prototyp-Hinweise `[FEHLT]` 14 px (Beschriftung, kein Seitentext) |
| M10 | Atmen | ok | genau 2 (Hero und Abschluss) |
| M11 | Text = approved copy | ok mit Liste | `check_text.py`: 203 Segmente, 0 Abweichungen (erlaubt: `[FEHLT]`-Hinweise und Prototyp-Zeile im Fuß). Absichtlich nicht auf der Seite, obwohl im Copy-Dokument: Parkgarage Frankfurt (unbestätigt für die neue Adresse) und der Satz "Karte laden (Platzhalter, Einwilligung nötig)" (statt dessen Kartenkachel mit Hinweis) |

## Globale Punkte
| # | Punkt | Ergebnis | Beleg |
| --- | --- | --- | --- |
| G1 | Raster | ok | linke Kante 172 px bei 1512 für alle Sektionen |
| G2 | Rhythmus | ok | Wechsel Weiß, Creme, Weiß, Creme, Weiß, Creme, Weiß, Creme, Weiß, Creme, dunkel |
| G3 | Text | fixed | FAQ in zwei Spalten ergab falsche Lesereihenfolge: auf eine Spalte umgestellt. Keine Einzelwörter, keine Umbrüche mitten im Wort |
| G4 | Bilder | ok | alle drei echt, scharf, kein Halo; Hero-Foto blendet links weich aus |
| G5 | Farbe | ok | eine CTA-Farbe #4E6F55; Blur-Test (7 px): der Hero-Button bleibt der einzige dunkle, gesättigte Block neben dem Kopf-Button |
| G6 | Typografie | ok | Newsreader und Manrope; H1 54 px, Fließtext 18 px (3,0 ×); Zeilenlänge unter 75 Zeichen |
| G7 | Buttons | ok | gleicher Stil in allen Sektionen |
| G8 | gegen Mockup | ok, Abweichungen unten | Reihenfolge, Farben, Proportionen gleich |
| G9 | Hover | ok | Button dunkler (rgb 63,92,70) und Atmen pausiert; Karte hebt sich 3 px, Pfeil 4 px |
| G10 | Sticky Header | ok | alle sechs Menüpunkte landen bei 96 px Abstand, Überschrift nicht verdeckt |

Abweichungen zum Mockup (bewusst): FAQ einspaltig statt zweispaltig (Lesereihenfolge); Hero-Foto ist das echte Foto über die ganze rechte Fläche; Kartenkacheln als CSS-Platzhalter ohne Straßennamen; Schrittbild ist das echte Büro-Foto.

## Sektionen
| Sektion | Ergebnis | Beleg |
| --- | --- | --- |
| Notfall-Streifen | ok | Zwei Nummern als `tel:`-Links, Hinweis `[FEHLT]` sichtbar |
| Kopf | fixed | Logo war durch das SVG-Rand-Weiß zu klein (50 px Höhe, 25 px Schrift): viewBox auf die Logoform beschnitten, jetzt 124×44 |
| 1 Hero | ok | H1 drei Zeilen, Wellenlinie unter "Frankfurt und München.", Sub, Bewertungszeile über den Buttons, beide Buttons gleich hoch, Namensschild |
| 2 Beweis-Leiste | ok | fünf Belege, ein Zitat mit Vorname |
| 3 Mandanten | ok | zwei Karten, gleiche Höhe, Symbole scharf |
| 4 Leistungen | fixed | Kartentitel ein- und zweizeilig: Mindesthöhe gesetzt, Texte fluchten |
| 5 Ablauf | fixed | Linie ragte über Schritt 4 hinaus: endet jetzt an Nummer 4 |
| 6 Über Dr. Stürzl | ok | Foto links, Zeitleiste aus dem Lebenslauf, zwei Buttons |
| 7 Bewertungen | ok | drei offene Karten, Sterne, Google-G, Namen |
| 8 Vertraulich | ok | zwei Spalten mit Haken |
| 9 FAQ | fixed | nur eine Frage offen (getestet: Frage 3 öffnen schließt Frage 1); Spaltenreihenfolge korrigiert; Platzhalter-Hinweis sichtbar |
| 10 Standorte | ok | zwei Karten, Nadel fällt ein; München ohne Parken (`[FEHLT]`) |
| 11 Abschluss | fixed | weißer Streifen über der Wellenkante entfernt; Telefonzeile umbricht jetzt sauber vor "München" |
| Fuß | ok | Logo weiß, Telefon, E-Mail, Adressen, Prototyp-Hinweis |

## Interaktion
Menü: 6 von 6 landen korrekt. Hero-Telefon: zwei getrennte Links (Frankfurt, München), Abschluss und Fuß ebenfalls. FAQ: Öffnen und Schließen ok, nur eine offen. Hero-Button: Hover ok. `tel:` und `mailto:` korrekt. Formular: Felder ok, Absenden bewusst ohne Funktion (Prototyp). Booking-Link entfällt (Kanal ist Formular, Telefon, E-Mail).

## Ergebnis
Fixed: 6 (Logo-Größe, Schrittlinie, Kartentitel, FAQ-Reihenfolge, Wellenkante, Telefon-Umbruch) plus 1 Fehler aus M6 (`tel:`-Ziffern). Offen (nur Daten, alle als `[FEHLT]` im Prototyp markiert): Frankfurter Adresse, Notfallnummern-Freigabe, Einwilligungstext, Preis und Dauer der Erstberatung, Reaktionszeit, Ablauf und Vertraulichkeitszusage, Parken, Karte mit Einwilligung, Google-Profil-Link, Kostenseite, anwalt.de-Freigabe, FAQ-Antworten (kommen später), 12 `#`-Platzhalter (Leistungs- und Profilseiten, Impressum, Datenschutz, Cookie-Einstellungen gibt es im Prototyp nicht).

## Prüfer (frischer Agent, 2026-10-11)
12 Lücken gemeldet, alle behoben: (1) Hero-Telefon wählte Frankfurt für beide Nummern, jetzt zwei Links, Abschluss und Fuß mit `tel:`; (2) F5 und F3 enthielten Ergebnis- und Schnelligkeitsaussagen, gestrichen; (3) "eine Ansprechpartnerin" ersetzt durch "Wobei wir Sie begleiten"; (4) anwalt.de-Flag ergänzt; (5) Flag und Handoff für Ablauf und "zuerst per E-Mail"; (6) Handoff: Bewertungs-Wortlaut gegen Google prüfen; (7) Handoff: Notfall-Event nur im Streifen; (8) Item 20 auf 1, Summe 37; (9) Titel "Dr." als Prüfpunkt ins Dataset und Handoff; (10) M11-Abweichungen gelistet; (11) Schema-Adresse im Handoff; (12) Impressum, Datenschutz, Cookie-Einstellungen als Links.

**Visual check done in Chrome, 55 items checked, 8 fixed, 0 open**
