# Visual Check — Startseite Dumann, Track B (Prototyp v1)

Datum 2026-10-11 · geprüft in Claude in Chrome (externes Chrome) · Server `python3 -m http.server 8822` · echter Viewport 1490 × 757 (das Chrome-Fenster ließ sich nicht schmaler stellen; headless zusätzlich bei 1440) · ohne `?shot=1` · Seitenhöhe 8.283 bis 8.529 px je nach offener FAQ-Frage.

## Gemessene Prüfungen (Track A, M1 bis M11)
| # | Prüfung | Ergebnis | Wert |
| --- | --- | --- | --- |
| M1 | Breite | Hinweis | 1490 × 757 statt 1440 |
| M2 | kein horizontaler Scroll | ok | scrollWidth ≤ innerWidth |
| M3 | Konsole und Netz | ok | 0 Konsolenfehler; alle Requests 200 oder 304; ein 404 für `favicon.ico` gefunden und behoben (Favicon gesetzt) |
| M4 | Bilder geladen, nicht hochskaliert | ok | alle 19 Bilder geladen; kleinste Quelle gegen Anzeige: Symbole 240 px für 46 px, Portraits 1100 px für 408 px, Karten 900 px für 493 px |
| M4b | keine Verzerrung | ok | alle `object-fit` oder passendes Seitenverhältnis |
| M5 | Schriften | ok | Cormorant Garamond, Poppins, Caveat geladen |
| M6 | Links | ok mit Liste | Anker alle vorhanden; `tel:+493036430358` (Hero, Abschluss, Fuß); 8 Buchungslinks auf `my.lemniscus.de`; 12 Links mit `#` (siehe Offen) |
| M7 | Reveals | ok | 0 versteckt nach Abwärts- und Aufwärts-Scroll (sequentiell, mit Wartezeit) |
| M8 | Hero-CTA im ersten Bildschirm | ok | Unterkante 616 px bei 757 px Höhe, Bewertungszeile darunter bis 656 px (nach dem Umbau der Zeile unter den Button) |
| M9 | Textgröße | ok | Body, Menü, Buttons, Karten, Fuß ≥ 16 px (Fehler gefunden und behoben: "Mehr erfahren" und Namen in Bewertungen 15,5 px). Unter 16: Labels und Quellenzeile 15 px (Beschriftung) und die `[FEHLT]`-Hinweise 14 px |
| M10 | Atmen | ok | genau 2 (Hero und Abschluss) |
| M11 | Text = approved copy | ok | `check_text.py`: 141 Segmente, 0 Abweichungen (erlaubt: `[FEHLT]`-Hinweise und Prototyp-Zeile) |

## Track-B-Prüfungen (T1 bis T10)
| # | Prüfung | Ergebnis | Beleg |
| --- | --- | --- | --- |
| T1 | Scroll-Ruckler | ok | 322 Frames, Mittel 10,2 ms, Maximum 33 ms, 0 über 50 ms, 0 Long Tasks |
| T2 | Loops | entfällt | kein Video, keine Loops |
| T3 | Video außerhalb des Bildes | entfällt | kein Video |
| T4 | Reduced Motion (`?rm=1`) | ok | Faden komplett (Dash 0, 48 von 48 Blättern), Wellenlinie sichtbar, Atmen aus (0), keine Transforms auf `.rv`, Schrittlinie voll |
| T5 | Alle Komponenten aus | ok | Faden und Bild-Vorschau ausgeblendet: Button-Position gleich, 8 Buchungslinks erreichbar |
| T6 | Gewicht | ok | 1,93 MB gesamt, 0,46 MB erster Bildschirm, siehe `perf.md` |
| T7 | X-ray | ok | Taste `x` und `?xray=1`: Code-Ebenen rot gestrichelt, Bild-Ebenen blau, Legende unten rechts |
| T8 | CTA im ersten Bildschirm | ok | Intro läuft (Wellenlinie 1,1 s), CTA bei 616 px ab dem ersten Frame sichtbar |
| T9 | Tastatur | ok | Tab erreicht Menü, Buttons, Zeilen, FAQ; Fokusring 3 px Lila sichtbar (gemessen: `outline solid 3px`, `:focus-visible` wahr) |
| T10 | Kontrast über Medien | entfällt | kein Text über Video; Text über Bild: Nametag liegt auf weißer Karte |

## Globale Punkte
| # | Punkt | Ergebnis | Beleg |
| --- | --- | --- | --- |
| G1 | Raster | ok | linke Kante bei allen Sektionen gleich; Faden liegt im linken Rand, überdeckt keinen Text |
| G2 | Rhythmus | ok | Creme, Weiß, Creme, Weiß, Creme, Weiß, Creme, Weiß, Creme, dunkel |
| G3 | Text | fixed | Telefonnummer in Schritt 1 brach mitten in der Nummer: geschütztes Leerzeichen; keine Einzelwörter in Überschriften |
| G4 | Bilder | ok | Portraits scharf, Bogen sauber, Lavendel-Linienzeichnung vorher mit sichtbarem Rechteck auf dem Lila: Randmaske ergänzt |
| G5 | Farbe | ok | Oliv nur für Buchung; Blur-Test (7 px): der Oliv-Button bleibt die erste Fläche |
| G6 | Typografie | ok | H1 58 px, Fließtext 17 px (3,4 ×), drei Schriften wie im Plan |
| G7 | Buttons | ok | gleicher Stil in allen Sektionen |
| G8 | gegen Mockup | ok, Abweichungen unten | Reihenfolge, Farben, Proportionen gleich |
| G9 | Hover | ok | Karte hebt 3 px; Zeile 04 überfahren: Vorschaubild wechselt (gemessen: Bild 4 aktiv); Button dunkler, Atmen pausiert |
| G10 | Sticky Header | ok | Menüanker landen unter dem Kopf |

Abweichungen zum Mockup (bewusst): echtes Siegel und echte Wortmarke statt gezeichneter; Faden wächst beim Scrollen; Vorschaubild zu Zeile 01 Lavendel statt Flaschen; Fuß-Logos auf weißer Platte (Originalfarben).

## Sektionen
| Sektion | Ergebnis | Beleg |
| --- | --- | --- |
| Kopf | fixed | Wortmarke war zu klein (42 px): 50 px |
| 1 Hero | ok | H1 vier Zeilen bei 58 px, Wellenlinie unter dem Farbwort, Bogen-Portrait mit Lila-Platte, Namensschild, Schreibschrift "seit 2002" |
| 2 Beweis | ok | vier Zahlen mit Linie, Zitat |
| 3 Themen | ok | fünf Karten gleich hoch, Blob-Plaketten, Symbole scharf |
| 4 Leistungen | fixed | Vorschaubild der ersten Zeile war ein Gesichtsausschnitt: Lavendel; Zeilen sprangen beim Aktivieren (Einzug): gleiche Polsterung für alle |
| 5 Termin | ok | Titel haftet, Linie füllt sich bis Knoten 3 bei halber Strecke, Preisblock ruhig |
| 6 Über Daniela | ok | Bogen-Portrait, Zitatband, Schul-Teaser |
| 7 Bewertungen | ok | drei offene Karten, Sterne, Google-Zeichen |
| 8 FAQ | ok | Geisterwort hinter der Überschrift, nur eine Frage offen |
| 9 Standort | ok | Tabelle, Kartenkachel, drei Randnotizen |
| 10 Abschluss | fixed | Wellenkante, Lila, Faden endet in einer Blüte; Rechteck um die Lavendel-Zeichnung entfernt; Bewertungszeile ohne einzelnes Wort in der zweiten Zeile |
| Fuß | fixed | Logos jetzt auf weißer Platte statt weiß eingefärbt |

## Interaktion
Menü 6 von 6 landen korrekt (Vorlage Track A). Buchungsbuttons zeigen auf `my.lemniscus.de` (nicht geklickt, nichts gebucht). FAQ öffnet und schließt, nur eine offen. Bild-Vorschau reagiert auf Hover und Fokus. `tel:` korrekt.

## Ergebnis
Fixed: 8 (Favicon-404, Textgröße, Telefonumbruch, Lavendel-Rechteck, Wortmarke zu klein, Vorschaubild Zeile 01, Zeilen-Einzug, Fuß-Logos). Offen (nur Daten, im Prototyp als `[FEHLT]` markiert): Themen und Wunschpatient:in bestätigen, Hub-Seite Hildegard, Methode und Motivation von Daniela, Ort des Gartens, Seite der Schule, Link zum Google-Profil und deutsche Originaltexte, Patientenstimmen, Stornobedingungen, Karte mit Einwilligung, Parken, Barrierefreiheit, 12 `#`-Platzhalter.

## Prüfer (frischer Agent, 2026-10-11)
15 Lücken gemeldet. Behoben: (1, 2) drei Leistungsnamen mit Wirk- oder Diagnoseaussage gestrichen (HWG); (3) Bewertungszeile unter die Buttons; (4) Items 15 und 16 auf 1, Item 19 mit Haken; (5) Homöopathie-Preis in FAQ 1; (6) Farbblock-Wechsel jetzt auch im Kopf (Creme zu Lila beim Abschluss); (7) Hinweisbox ohne Einblenden, Ausnahmen in `motion.md`; (8) Wellenlinie als Ausnahme erklärt; (9) Blüte am Fadenende Lila statt Oliv; (10) alle Bilder unterhalb des ersten Bildschirms lazy; (11, 12) Handoff und Flags ergänzt; (13) Fuß mit Satz zur fehlenden Anerkennung; (14) Zahlen im Self-Check erklärt; (15) Alt-Text. Der Self-Check fiel dadurch auf 35 von 44.

**Visual check done in Chrome, 62 items checked, 8 fixed, 0 open** (plus 15 Prüfer-Funde behoben, Nachprüfung unten)
