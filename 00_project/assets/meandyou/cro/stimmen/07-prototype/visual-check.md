# Visual Check in Chrome — „Stimmen“, Prototyp v1, Runde 2 nach Martins Feedback (2026-10-12)
Setup: `python3 -m http.server 8816` in `07-prototype/`, Claude in Chrome (eigener Tab), `innerWidth` 1440, `innerHeight` 757. Jede Sektion angesprungen, Messskript, Headless-Screenshots 1440 px.

| # | Ergebnis | Wert |
|---|---|---|
| M1 | ok | 1440 × 757 |
| M2 | ok | keine horizontale Scrollleiste |
| M3 | ok | 0 Konsolenfehler |
| M4 | ok | 0 kaputte, hochskalierte oder verzerrte Bilder |
| M5 | ok | Inter und Libre Baskerville geladen |
| M6 | ok | 8 Gesprächslinks mit `utm_source=stimmen`, `tel:+4915888367664`, 0 fehlende Anker, 0 „#“ |
| M7 | ok | 0 unsichtbare Elemente nach einem Scroll |
| M8 | ok | Hero-Button unten bei 651 px |
| M9 | ok | unter 16 px nur Quellenzeilen (15), Labels und gelbe Marken (14) |
| M10 | ok | 2 atmende Buttons (Hero, Abschluss) |
| M11 | ok mit Liste | 210 Segmente, Abweichungen nur Menü, Footer, Prototyp-Schild |
| Überschriften | fixed | H2 S02 brach in 3 Zeilen → Spalte breiter, 38 px, jetzt 2 Zeilen |
| Hero | fixed | Wistia-Standbilder hatten eingebrannte Untertitel („Aufgabe“, „reingehen“) → neue Standbilder aus dem Video, oberhalb der Untertitel geschnitten; Collage überlappte den Text → nach rechts versetzt |
| Videos S03 | fixed | MP4 auf der v2-Vorschau gibt 404 → Videos lokal (neu kodiert, 4 bis 7 MB); Abspielen im Hochformat-Fenster, Escape schließt (getestet mit Klick) |
| Themen S04 | ok | 3 + 2 Karten wie Mockup, Hinweiszeile unter dem Raster |
| Öffentliche Stimmen S05 | fixed | Karten waren 100 px schmal (Standard-Rand von `figure`) → `margin:0`; Subotic mit gelber Marke |
| Seminar S06 | ok | echtes Gruppenfoto, 2 × 2 Blöcke mit Linien-Icons |
| Michael S07 | fixed | Kopf im Porträt angeschnitten → Bildausschnitt oben |
| Transparenz S08 | fixed | erfundene Quellenzeile in der Balkenkarte entfernt (nicht in der Copy) |
| Gespräch, FAQ, Abschluss | ok | Linie mit Nummern, FAQ einspaltig wie Mockup, eine Frage offen |
| Hero-Klick (Martin) | fixed | Video-Collage ist jetzt ein Link auf `#videos`: weiches Scrollen (Schritte 0, 107, 684, 1001 … 1234 px), Überschrift landet bei 269 px unter dem Header (86 px), `scroll-margin-top` 110 px, Cursor Zeiger, Hinweis-Pille „Direkt zu den Videos ↓“ (Text aus der freigegebenen Copy). Ohne Animation bei `prefers-reduced-motion`. Textlink im Hero getestet: gleiche Landeposition |
| Videos Hochformat (Martin) | fixed | Kacheln 340 × 604 px, Verhältnis 0,5629 (9:16 = 0,5625); Hero-Karten 0,5632. Standbilder: volle 9:16-Bilder aus den Videos (1: 25,5 s, 2: 1,75 s, 3: 2,75 s), eingebrannte Untertitel-Wörter retuschiert (OpenCV), Gesichter unverändert |
| Mockup-Vergleich | ok mit Liste | Hero-Videokarten jetzt hoch wie im Mockup, H1 groß „Vorher. Nachher.“ (Mockup zeigte die Sub groß, Copy gilt) |

## Offen
1. Vorname, Rolle und Einwilligung der drei Videopersonen (gelb).
2. Vollständiger Wortlaut Subotic (gelb).
3. Name und Rolle der Person im Gespräch (gelb).
4. Video 2 zeigt am Anfang eine Prozentzahl im Bild (zählt hoch, vermutlich „30 %“ Abschlussquote). Die Copy zitiert die Zahl nicht. Kunde bestätigt den Wortlaut (OPEN-FLAGS ST3).

**Visual check done in Chrome, 23 items checked, 9 fixed, 4 open.**
