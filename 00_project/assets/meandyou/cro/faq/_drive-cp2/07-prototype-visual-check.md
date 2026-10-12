# Visual Check in Chrome — „FAQ“, Prototyp v1 (2026-10-12)
Setup: `python3 -m http.server 8827` (Port 8817 war von einem anderen Server belegt: Element-Pool 741.studio, nicht beendet). Claude in Chrome, eigener Tab, Fenster 1440 × 900, Viewport 1440 × 757 (gemessen). Seite frisch geladen ohne `?shot=1`, von oben nach unten in Schritten von etwa 700 px gescrollt und zurück. Headless-Screenshots 1440 px in `screenshots/`.

| # | Ergebnis | Wert / was behoben |
|---|---|---|
| M1 | ok (Abweichung notiert) | 1440 × 757 |
| M2 | ok | keine horizontale Scrollleiste |
| M3 | ok | Konsole ohne Fehler; 11 Anfragen, alle 200 oder 304 |
| M4/M4b | ok | 5 Bilder, keins kaputt, hochskaliert oder verzerrt |
| M5 | ok | Inter und Libre Baskerville geladen (Arial nur in Buttons einer Browser-Erweiterung) |
| M6 | ok | Buttons auf termin.html mit utm_source=faq (header, hero, seminar, orte, kosten, gespraech, abschluss, textlink, footer); tel +4915888367664; 0 fehlende Anker; 0 „#“ |
| M7 | ok | 0 Elemente unsichtbar nach dem Scrollen |
| M8 | ok | Hero-Button unten bei 618 px |
| M9 | fixed | Ortsnamen und Leisten-Chips hatten 15 px → 16 px. Unter 16 px nur gelbe Marken (15 px, wie Geschwisterseiten) |
| M10 | ok | 2 atmende Buttons (Hero, Abschluss) |
| M11 | ok mit Liste | Abweichungen nur Footer (Adresse, Rechtliches, Kontakt, Social) und Prototyp-Schild |
| Seitenaufbau | fixed | geerbte Klasse `.grp` (700 px fest, Startseite) ließ Gruppen abschneiden → eigene Klasse `.fgrp` |
| Hero | fixed | Button lag bei 703 px (unter der Grenze) → Hero kompakter, Button 618 px. Foto gerahmt wie im Mockup |
| Themen-Kacheln | ok | 4 Spalten, Nummer + Titel, Hover mit Rand in CTA-Farbe |
| Themen-Leiste (sticky) | fixed | Chips brachen auf 2 Zeilen; Leiste breiter als Header; aktiver Chip weiß auf hell; Leiste lag im Abschluss über dem Text → einzeilig, ohne Nummern, so breit wie Header, aktiver Chip blau, ab Abschluss ausgeblendet |
| Sprungziel | ok | Klick „Kosten und Storno“: Gruppen-Nummer bei 238 px, Leiste endet bei 147 px, nichts verdeckt |
| Kurz-Antwort | fixed | Absatz in großer Serifenschrift zu schwer → 20 px Inter wie im Mockup |
| Akkordeon | ok | weiße Karten, Dreieck + Plus/Minus, erste Frage je Gruppe offen, Klick öffnet eine und schließt die andere derselben Gruppe (getestet in Gruppe 05) |
| Gruppen 03 und 07 | ok | zwei Spalten wie Mockup |
| Gruppe 06 | ok | echtes Porträt neben der Nummer |
| Gelbe Marken | ok | 12 sichtbar, alle aus der freigegebenen Copy |
| Abschluss, Footer | ok | Foto, Häkchen, Beweiszeile, heller Button, Telefon, Link Startseite |
| Vergleich Mockup | ok | Reihenfolge, Layout und Farben gleich. Absichtlich anders: Leiste mit aktiver Gruppe (nur Prototyp), Abschluss im Format der Geschwisterseiten |
| Rückweg nach oben | ok | nichts animiert neu, nichts verschwindet |

## Offen
1. Alle gelben Marken (Übernachtung, Verpflegung, Begleitperson, Get Together, Seminarleitung, Person im Gespräch, Bundle, Video-Training, Seminarname) warten auf den Kunden.
2. Stimmen-Link zeigt auf die v2-Startseite (`index.html#stimmen`), bis die Stimmen-Seite steht.
3. Port 8827 statt 8817 (8817 belegt).

**Visual check done in Chrome, 24 items checked, 7 fixed, 3 open.**
