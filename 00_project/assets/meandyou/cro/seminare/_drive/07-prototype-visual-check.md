# Visual Check in Chrome — Seminarseite me&you, Prototyp v1 (2026-10-12)

Setup: Prototyp über `python3 -m http.server 8813`, geöffnet in Claude in Chrome (externer Chrome). Viewport **1500 × 807** (Bildschirmgrenze dieses Geräts, gemessen über `innerWidth`). Seite ohne `?shot=1` geladen, jede Sektion per Sprung und Scroll angesehen, danach Messskript (measure.js) und Headless-Screenshots 1440 px.

## Gemessene Checks
| # | Ergebnis | Wert |
|---|---|---|
| M1 | ok (Abweichung notiert) | 1500 × 807 |
| M2 | ok | keine horizontale Scrollleiste |
| M3 | ok | keine Konsolen-Fehler |
| M4 / M4b | ok | 0 kaputte, 0 hochskalierte, 0 verzerrte Bilder |
| M5 | ok | Inter und Libre Baskerville geladen |
| M6 | ok | 11 Buchungslinks auf `termin.html?utm_source=seminare&utm_content=…`; `tel:+4915888367664`; 0 fehlende Anker, 0 „#“-Links; Anker `#frei-sprechen`, `#ruhig-bleiben`, `#mit-sprache-fuehren`, `#termine` vorhanden |
| M7 | ok | 0 Elemente bleiben unsichtbar |
| M8 | ok | Hero-Button-Unterkante 643 px |
| M9 | ok | unter 16 px nur Overlines und Tabellenköpfe (14 px), Ortslabels (14 px), gelbe Marken (15 px) |
| M10 | ok | genau 2 atmende Buttons (Hero, Abschluss) |
| M11 | ok mit Liste | 264 Textsegmente; Abweichungen nur Footer (Adresse, Rechtliches, Kontakt, E-Mail, Social), Videolängen 1:00/1:12/1:23, Prototyp-Schild |

## Globale Punkte
| # | Ergebnis | Notiz |
|---|---|---|
| G1 Raster | ok | eine Wrap-Breite 1240 px wie Startseite |
| G2 Abstände | ok | 120 px je Sektion, Bänder voll |
| G3 Text | fixed | Hero-H1 brach in 3 Zeilen, Bewertungszeile in 2 → Textspalte 740 px, H1 jetzt 2 Zeilen; FAQ-H2 auf 34 px |
| G4 Bilder | fixed | VR-Band schnitt den Kopf mit der VR-Brille ab → Bildausschnitt oben; Einstieg-Bild auf die Sprecherin zentriert. Offen: Video-Poster mit eingebrannten Untertiteln (wie Startseite) |
| G5 Farbe / Blur | ok | `screenshots/blur-test-first-viewport.png` |
| G6 Typo | ok | zwei Schriften, Body-Zeilen < 75 Zeichen |
| G7 Buttons | fixed | Button unter den drei Gesprächsschritten stand links → zentriert |
| G8 Mockup-Vergleich | ok mit Abweichungen | Reihenfolge und Layouts wie Mockup. Absichtlich anders: Hero mit echtem Foto (Mockup zeigte ein neu gerechnetes Gesicht), H1 klein + Copy-Deck-Zeile groß (Mockup vertauschte Headline und Body), Stimmen-Videos rechts neben den Karten wie Mockup |
| G9 Hover | ok | Buttons heben sich, Format-Bilder zoomen 1,03 (Startseiten-CSS) |
| G10 Header/Anker | ok | „Seminare“ aktiv; Sprünge landen unter dem Header (`scroll-margin-top`) |

## Sektionen
| Sektion | Ergebnis | Notiz |
|---|---|---|
| S01 Hero | fixed | echtes Foto Michael (braunes Sakko), H1 2 Zeilen |
| S02 Antwort + Beweis | fixed | Kacheln waren zu schmal (3 Spalten) → 2 Spalten, Bewertungen oben über volle Breite |
| S03 Einstieg | ok | Feature-Bild links (sticky), 7 Themen zweispaltig, Termin-Box, Button |
| S04 Formate | ok | 3 gleiche Karten, gelbe Marken, Button je Karte |
| S05 Vergleich | ok | Tabelle 5 Spalten, gelbe Marken in der Bundle-Zeile |
| S06 Im Raum | fixed | VR-Band (siehe G4), drei Spalten mit Icons, Enthalten-Box |
| S07 Stimmen | ok | 4 offene Karten 2 × 2, 3 Videos rechts |
| S08 Orte | ok | 6 Ortskarten mit Seminar und Daten, heller Button |
| S09 Michael | ok | echtes Foto (olivgrüne Jacke), ERFOLG-Cover |
| S10 Gespräch | fixed | Button zentriert (siehe G7) |
| S11 FAQ | ok | 9 Fragen zweispaltig, nur eine offen (Startseiten-JS) |
| S12 Abschluss + Footer | ok | Mini-Hero, Link zurück zur Startseite |

## Offen
1. Video-Poster mit eingebrannten Untertiteln (andere Standbilder aus Wistia nötig, gleich wie Startseite).
2. Die Startseiten-Links zeigen auf die alte v2-Seminarseite. Nach Freigabe müssen sie auf diese Seite zeigen (Handoff).
3. Kundendaten gelb markiert: Seminarnamen, Bundle (Termine, Ort, Plätze), Übernachtung, Verpflegung, Person im Gespräch.

**Visual check done in Chrome, 34 items checked, 7 fixed, 3 open.**
