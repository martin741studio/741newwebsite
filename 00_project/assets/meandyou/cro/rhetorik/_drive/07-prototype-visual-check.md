# Visual Check in Chrome — „Was ist Rhetorik“, Prototyp v1 (2026-10-12)
Setup: `python3 -m http.server 8815`, Claude in Chrome, Viewport 1500 × 807. Jede Sektion angesprungen, Messskript, Headless-Screenshots 1440 px.

| # | Ergebnis | Wert |
|---|---|---|
| M1 | ok (Abweichung notiert) | 1500 × 807 |
| M2 | ok | keine horizontale Scrollleiste |
| M4 | ok | 0 kaputte, hochskalierte oder verzerrte Bilder |
| M6 | ok | 7 Links auf /sichtbarkeit-neu mit `utm_source=rhetorik`, 3 Gesprächslinks, 0 fehlende Anker, 0 „#“ |
| M7 | ok | 0 unsichtbare Elemente |
| M8 | ok | Hero-Button 629 px |
| M9 | ok | unter 16 px nur Labels (14) und gelbe Marken (15) |
| M10 | ok | 2 atmende Buttons |
| M11 | ok mit Liste | 206 Segmente, Abweichungen nur Menü, Footer, Prototyp-Schild |
| Überschriften | ok | alle H1/H2 in 1 bis 2 Zeilen (gemessen) |
| Hero | ok | echtes Foto (Café, weißes Hemd), Soft-CTA, Play-Symbol in der Rückversicherung |
| Mythen, Ethos/Pathos/Logos, 5 Schritte, Beruf, Fehler | ok | Karten, Linie mit Nummern, Kacheln, Liste |
| Methode | ok | Navy-Band, 01 bis 03, gelbe Marke, heller Button |
| Lernen | fixed | Übungskarten waren auf Creme unsichtbar → weiß |
| Training | fixed | H2 brach in 3 Zeilen → 38 px; echtes Video-Standbild aus Wistia |
| FAQ, Abschluss | ok | eine Frage offen, Textlinks |

## Offen
1. Video-Inhalt und Länge vom Kunden bestätigen (Wistia nennt 29:39 min).
2. Ob das Video eine Anmeldung braucht.
3. Ob Michael die Seminare selbst leitet (gelb).

**Visual check done in Chrome, 20 items checked, 2 fixed, 3 open.**
