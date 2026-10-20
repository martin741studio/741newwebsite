# Visual Check in Chrome — Startseite me&you, Prototyp v1 (2026-10-12)

Setup: Prototyp über `python3 -m http.server 8812`, geöffnet in Claude in Chrome (externer Chrome, Martins Profil). Fenster auf 1440 × 900 gesetzt; der Bildschirm erlaubt nur **1386 × 773** innen (echte Messung, `innerWidth`). Seite geladen ohne `?shot=1`, von oben nach unten in Schritten von 700 px gescrollt, Screenshot an jeder Stelle, danach Klicks und Hover.

## Gemessene Checks (measure.js)
| # | Ergebnis | Wert |
|---|---|---|
| M1 | ok (Abweichung notiert) | 1386 × 773 (Bildschirmgrenze) |
| M2 | ok | keine horizontale Scrollleiste |
| M3 | ok | keine Konsolen-Fehler; alle Links auf Vorschau-Seiten antworten 200 (curl) |
| M4 | ok | 0 kaputte, 0 hochskalierte Bilder |
| M4b | ok | 0 verzerrte Bilder |
| M5 | ok | Inter und Libre Baskerville geladen |
| M6 | ok mit Ausnahmen | Buchung → `clients.741.studio/meandyou/v2/termin.html?utm_…` (10 Stellen, eigener `utm_content`); `tel:+4915888367664`; Anker `#termine` vorhanden; offen: Unteranker `seminare.html#frei-sprechen` usw. existieren auf der Seminarseite noch nicht |
| M7 | ok | 0 Elemente bleiben unsichtbar |
| M8 | ok | Hero-Button-Unterkante 649 px |
| M9 | fixed | vorher 50 Textstellen unter 16 px; jetzt nur Labels 14 px und FEHLT-Marken 15 px |
| M10 | ok | genau 2 atmende Buttons (Hero, Abschluss) |
| M11 | ok mit Liste | 256 Textsegmente, 0 Abweichungen mit erlaubter Liste: Footer-Einträge (Rechtliches, Impressum, Datenschutz, Kontakt, E-Mail, Instagram, LinkedIn), Video-Längen 1:00/1:12/1:23, Labels „Kommt dir das bekannt vor?“ (Copy Deck), „Dein erster Schritt“, „Orte und Termine“, Prototyp-Schild, FEHLT-Marke, zwei Sätze mit Platzhalter-Kommentar in der Copy-Datei |

## Globale Punkte
| # | Ergebnis | Notiz |
|---|---|---|
| G1 Raster | ok | eine Wrap-Breite 1240 px, Kanten bündig |
| G2 Abstände | ok | 120 px je Sektion, Band und Abschluss voll |
| G3 Text | fixed | Hero-H1, Band-H2, Abschluss-H2 und Michael-H2 brachen in 3 Zeilen; jetzt je 2 Zeilen (gemessen). Telefonnummer brach um, jetzt `nowrap` |
| G4 Bilder | ok mit 1 offen | alle Bilder scharf, gleicher warmer Stil; Video-Poster zeigen eingebrannte Untertitel-Wörter (echte Wistia-Standbilder) → offen |
| G5 Farbe / Blur | ok | `screenshots/blur-test-first-viewport.png` |
| G6 Typo | ok | zwei Schriften, Body-Zeilen < 75 Zeichen |
| G7 Buttons/Links | ok | gleiche Pille in allen Sektionen, auf Navy die helle Variante |
| G8 Mockup-Vergleich | ok mit Abweichungen | Reihenfolge und Layouts wie Mockup. Absichtlich anders: Situationen ohne vierte Spalte (Mockup erfand dort Text), Für-wen-Liste unter den Karten; Video-Kacheln hochkant (echte Videos sind 9:16); Ortskarten mit Datum statt Monat (Flag F3) |
| G9 Hover | ok | Button hebt sich 2 px, Schatten tiefer; Format-Bild zoomt 1,03 |
| G10 Header/Anker | fixed | „Termine ansehen“ landete unter dem Header; jetzt `scroll-margin-top`, Abschnitt beginnt bei 96 px |

## Sektionen
| Sektion | Ergebnis | Notiz |
|---|---|---|
| Header | ok | echtes Logo (zugeschnitten aus 2052-px-Datei), 5 Menüpunkte, Button |
| S01 Hero | fixed | H1 2 Zeilen, Beweiszeile, Kicker, Buttons gleich hoch, Rückversicherung lesbar; Prototyp-Schild verdeckte die Zeile → nach rechts verschoben |
| S02 Beweis-Leiste | ok | Sterne füllen sich einmal, Zitat mit Name, Medienlogos grau |
| S03 Situationen | ok | gleiche Kartenhöhen; neues Meeting-Bild ohne Michael-Doppelgänger |
| S04 Warum Michael | ok | Portrait scharf, Zahlen in einer Zeile |
| S05 Methode | ok | drei Spalten wie Mockup |
| S06 Seminare | ok | Band-Text lesbar über Verlauf, Faktenkacheln überlappen das Band, 3 Karten mit FEHLT-Marke für Seminarnamen |
| S07 Gespräch | fixed | Linie lief durch die Überschriften → Kreise oben, Linie zwischen den Kreisen, zeichnet sich einmal |
| S08 Stimmen | ok | 6 offene Karten, kein Karussell, 3 Videos |
| S09 Orte | ok | 6 Karten mit Pexels-Fotos, Daten lesbar, heller Button auf Navy |
| S10 FAQ | ok | 12 Fragen zweispaltig, nur eine offen (getestet), Preis zuerst offen mit FEHLT-Marke |
| S11 Abschluss + Footer | fixed | H2 2 Zeilen; Firmenadresse Hallstadt, Rechtliches, Kontakt |

## Interaktion
- Buchungs-Buttons in Hero, Seminare und Abschluss: Ziel ist die Terminseite mit Calendly (Vorschau, nicht abgesendet).
- `tel:`-Link korrekt.
- Menü: Seminare, Michael, Was ist Rhetorik → Vorschau-Seiten (200); Stimmen, FAQ → Anker auf der Seite.

## Offen
1. Video-Poster mit eingebrannten Untertitel-Wörtern (andere Standbilder aus Wistia nötig).
2. Unteranker auf der Seminarseite (`#frei-sprechen`, `#ruhig-bleiben`, `#mit-sprache-fuehren`) fehlen dort noch.
3. Kundendaten: Seminarnamen, Person im Gespräch, Freigabe Übernachtung (gelb markiert).

**Visual check done in Chrome, 30 items checked, 7 fixed, 3 open.**
