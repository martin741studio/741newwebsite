# Visual Check in Chrome — Landingpage „The Undersold“, Prototyp v1 (2026-10-12)
Setup: `python3 -m http.server 8836` (Port 8833 war vom Lauf lp-replayers belegt, dort ein Hilfsserver; nicht beendet). Claude in Chrome, eigener Tab, Fenster 1440 × 900, Viewport 1440 × 757 (gemessen). Seite frisch geladen ohne `?shot=1`, von oben nach unten in Schritten von etwa 700 px gescrollt und zurück. Headless-Screenshots 1440 px in `screenshots/`. Vergleich mit `../06-gpt-assets/full-page-v1-final.png`.

| # | Ergebnis | Wert / was behoben |
|---|---|---|
| M1 | ok (Abweichung notiert) | 1440 × 757 |
| M2 | ok | keine horizontale Scrollleiste |
| M3 | ok | Konsole ohne Fehler; 14 Anfragen, alle 200 oder 304 |
| M4/M4b | ok | 12 Bilder, keins kaputt, hochskaliert oder verzerrt |
| M5 | ok | Inter und Libre Baskerville geladen |
| M6 | ok | Buttons auf `termin.html?utm_source=lp-undersold` (header, abschluss, footer-Textlink); tel +4915888367664; 0 fehlende Anker; 0 „#“ |
| M7 | ok | 0 Elemente unsichtbar nach dem Scrollen |
| M8 | ok (Persona) | kein Button im Hero-Inhalt (Persona-Regel, Auftrag); Header-Button sichtbar, Unterkante 74 px |
| M9 | fixed | Kicker 15 → 16 px, Format-Labels 15 → 16 px. Unter 16 px nur gelbe Marken (15 px, wie Geschwisterseiten), Versal-Labels „Enthalten“ und Footer-Überschriften (14 px, wie Startseite), Prototyp-Schild |
| M10 | ok (Persona) | 1 atmender Button (Abschluss); im Hero gibt es keinen Button |
| M11 | fixed | `check_text.py`: Faktenzeilen mit falschem Doppelpunkt und eine erfundene Bildunterschrift entfernt; jetzt 0 Abweichungen außer Footer, Pfeil und Prototyp-Schild |
| Hero | fixed | Beweiszeile brach um → einzeilig; H1 auf zwei Zeilen wie Mockup; Bild goldene Stunde, kein Trainer, Text links auf ruhigem Bildteil, gut lesbar |
| S02 Kurz-Antwort | fixed | Faktenspalte zu schmal („10 bis 14“ stieß an das Label) → Spalte breiter, Zahlen in Gold wie Mockup |
| S03 Lage | ok | dunkles Band, zwei Spalten wie Mockup, Abschluss kursiv zentriert |
| S04 Methode | ok | drei Schritte mit Goldnummern und Linie |
| S05 Orte | fixed | Hintergrund gleich wie S04 (zwei Cremebänder) → Papierweiß wie Mockup; sechs Karten, Daten als Liste mit Goldpunkt |
| Sprungziel „Orte und Termine“ | ok | Klick: H2 bei 216 px, Header endet bei 86 px, nichts verdeckt |
| S06 Format | fixed | Satzpunkt nach gelber Marke stand allein in einer Zeile → Marken in S06 und S11 fließen im Text |
| S07 Für wen | ok | großes Zitat rechts wie Mockup, Zitat Christin R. darunter |
| S08 Michael | fixed | „Universität St. Gallen:“ brach im Zeilenlayout → Fließzeile |
| S09 Stimmen | ok | drei offene Karten, kein Laufband |
| S10 FAQ | ok | Überschrift oben, Akkordeon zweispaltig, erste Frage offen, eine offen zur Zeit |
| S11 Abschluss | fixed | Schritte lagen auf hellen Lichtern des Fotos → Abdunklung rechts stärker; H2 von drei auf zwei Zeilen |
| Hover | fixed | Button (heller, Schatten), Textlink, Menüpunkt (CTA-Farbe) ok. Ortskarten: Parallaxe überschrieb den Zoom → Parallaxe an den Karten entfernt, Zoom 3 % geprüft |
| Blur-Test | ok | `screenshots/blur-test-first-viewport.png`: der blaue Header-Button ist das einzige gesättigte Element |
| Vergleich Mockup | ok | Reihenfolge, Layout, Farben gleich. Absichtlich anders: S07 Zitat Christin als Zeile unter dem Raster (Mockup gleich), S02 Porträt ohne Bildunterschrift (Text nicht in der Copy), Footer wie Geschwisterseiten |
| Rückweg nach oben | ok | nichts animiert neu, nichts verschwindet |

Visual check done in Chrome, 24 items checked, 10 fixed, 0 open.
