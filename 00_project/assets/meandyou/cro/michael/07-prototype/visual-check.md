# Visual Check in Chrome — Michael-Seite me&you, Prototyp v1 (2026-10-12)

Setup: `python3 -m http.server 8814`, Claude in Chrome, Viewport 1500 × 807 (Bildschirmgrenze). Jede Sektion angesprungen und angesehen, Messskript, Headless-Screenshots 1440 px.

## Gemessen
| # | Ergebnis | Wert |
|---|---|---|
| M1 | ok (Abweichung notiert) | 1500 × 807 |
| M2 | ok | keine horizontale Scrollleiste |
| M4 / M4b | ok | 0 kaputte, 0 hochskalierte, 0 verzerrte Bilder |
| M5 | ok | Inter, Libre Baskerville geladen |
| M6 | fixed | Footer-Link „Termine“ zeigte auf `#termine` (gibt es hier nicht) → `seminare.html#termine`; jetzt 0 fehlende Anker, 0 „#“; Buchungslinks mit `utm_source=michael` |
| M7 | ok | 0 unsichtbare Elemente |
| M8 | ok | Hero-Button 637 px |
| M9 | ok | unter 16 px nur Labels (14 px) und gelbe Marken (15 px) |
| M10 | ok | 2 atmende Buttons (Hero, Abschluss) |
| M11 | ok mit Liste | 166 Segmente; Abweichungen nur Menü, Footer, Prototyp-Schild |

## Global und Sektionen
| Punkt | Ergebnis | Notiz |
|---|---|---|
| Hero | ok | echtes Foto (Stuhl, Mai 2026), H1 2 Zeilen, Sub, Buttons |
| Antwort + Fakten | ok | 5 Kacheln, Medienlogos |
| Zeitleiste | fixed | Button ergänzt, damit nie zwei Sektionen ohne Button folgen |
| Methode | ok | Motto mit gelber Marke, echtes Foto weißes Hemd |
| Bücher | ok | 9 typografische Karten (keine erfundenen Cover), Podcast-Karte |
| Lehre + Medien | ok | zwei Spalten, ERFOLG-Cover; ARTE/WELT nur als Text (keine echten Logo-Dateien) |
| Stimmen | ok | 4 Karten 2 × 2 |
| Seminare | fixed | Gruppenfoto schnitt Michael ab → Ausschnitt links unten, Michael sichtbar |
| Gespräch, FAQ, Abschluss | ok | Button zentriert, eine Frage offen, Link Startseite |
| Mockup-Vergleich | ok | Reihenfolge und Layout wie Mockup; Mockup zeigte erfundene ARTE/WELT/n-tv-Logos → nicht übernommen |

## Offen
1. Fotorechte institut-ehlers.de und Einwilligung der Personen auf dem Gruppenfoto.
2. Logos ARTE und WELT TV fehlen als echte Dateien.
3. Kundendaten gelb: Motto-Wortlaut, Seminarleitung, Person im Gespräch.

**Visual check done in Chrome, 24 items checked, 3 fixed, 3 open.**
