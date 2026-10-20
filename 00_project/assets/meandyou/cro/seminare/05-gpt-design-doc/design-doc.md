# GPT Design Doc — me&you / Michael Ehlers, Seminarseite

Stand 2026-10-12. Quellen: `../../02-data/brand.md`, `03-diagnosis/diagnosis.md` (P0 für Angebotsseite), `04-copy/approved-copy.md` (exakte Texte, freigegeben 12.10.).

Verfahren: ein Bild der ganzen Seite, eine Nachricht, neuer Chat. Das freigegebene Startseiten-Mockup ist als Stil-Referenz angehängt (Workflow 4b Punkt 5), damit beide Seiten wie eine Website aussehen. Prompt: `prompt.txt` (19.077 Zeichen, 138 wörtliche Zitate, `check_prompt.py` gegen `04-copy/approved-copy-plain.txt`: 0 fehlend). Generator: `build_prompt.py` aus `units.json` (`plain.py`).

## Global Style
Wie Startseite: Grund #FAF8F4, Creme #F2EDE4, Sand #D8CCB7, Taubenblau #7E99B6, Navy #2B3C52, Anthrazit #47403A, Text #2A2622; einzige Buttonfarbe #4F6D90 (weiß), auf dunklen Bändern Creme. Libre Baskerville + Inter. Radius 22 px. Reportage-Fotos, keine Bühne, kein Michael-Doppelgänger (andere Personen ohne Glatze und Brille).

## Sektionen
1 Hero split: Text links, echtes Foto Michael (braunes Sakko) rechts.
2 Antwort + Beweis: Creme-Band, 5 Fakten-Kacheln, Zitat, Medienlogos.
3 Der Einstieg (`#frei-sprechen`): großes Feature, Gruppenfoto, 7 Themen zweispaltig, Info-Streifen Plätze + Termine, Button.
4 Die Formate (`#ruhig-bleiben`, `#mit-sprache-fuehren`, Bundle): drei gleiche Karten mit Foto, Streifen, Button.
5 Vergleich: Tabelle 5 Spalten.
6 Im Raum: Foto-Band VR, drei Spalten mit Icons, Enthalten-Box, Button.
7 Stimmen: 4 offene Karten 2×2, 3 Video-Kacheln.
8 Orte und Termine (`#termine`): Navy-Band, 6 Ortskarten, heller Button.
9 Für wen + Michael: echtes Foto (olivgrüne Jacke), Text, ERFOLG-Cover.
10 Erst ein Gespräch: 3 Schritte mit Linie, Button, Telefon.
11 FAQ: Akkordeon zweispaltig, 9 Fragen.
12 Abschluss: dunkles Foto-Band, Häkchen, Beweis, Button; Navy-Footer.

## Referenzbilder (`refs/`)
ref-homepage-mockup.jpg (Stil), ref-logo.png (echtes Logo), ref-michael-jacket.jpg (Hero), ref-michael-olive.jpg (S09).

## Bildregel
Neue Bilder nach dem Mockup in eigenen Chats (Step 5b): S03 Einstieg-Gruppe, S04 Kartenbilder (wo die Startseiten-Bilder nicht passen), S06 VR-Band. Wiederverwendbar aus der Startseite: Ortsfotos, Abschluss-Terrasse, Video-Standbilder, Format-Bilder.
