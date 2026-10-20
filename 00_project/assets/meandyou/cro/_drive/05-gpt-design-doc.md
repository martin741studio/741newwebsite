# GPT Design Doc — me&you / Michael Ehlers, Startseite

Stand 2026-10-11. Quellen: `02-data/brand.md`, `03-diagnosis/diagnosis.md` (Muster P0 + P1-Stimmung + P9-Hierarchie, Struktur von Entwurf A), `04-copy/approved-copy.md` (exakte Texte).

Verfahren (Martin, 2026-10-11): ein Bild der ganzen Seite, eine Nachricht, neuer Chat. Der vollständige Prompt steht in `prompt.txt` (19.951 Zeichen, 139 wörtliche Zitate, `check_prompt.py` gegen `approved-copy-plain.txt` = sichtbarer Text der freigegebenen Copy: 0 fehlend).

## Global Style Block
Desktop 1440 px, eine hohe Mockup-Seite, 11 Sektionen. Look und Struktur von Entwurf A (angehängter Screenshot), ruhiger, klarer, hochwertiger. Farben: Grund #FAF8F4, Creme #F2EDE4, Sand #D8CCB7, Taubenblau #7E99B6 (Akzente, Zahlen), Navy #2B3C52 (ein dunkles Band, Footer), Anthrazit #47403A, Text #2A2622. Einzige starke Buttonfarbe: #4F6D90 mit weißer Schrift, Pille; auf dunklen Bändern Creme mit Navy-Schrift. Libre Baskerville für Headlines und Zitate, Inter für Body und UI. Overlines Versalien gesperrt. Radius 22 px, keine harten Linien, viel Weißraum. Fotos: Reportage, Tageslicht, leichtes Korn, kleine Gruppen, keiner schaut in die Kamera außer Michaels Portrait, nie Bühne, Konferenz, Ballsaal, Lanyards, Stock. Michael aus den Referenzfotos exakt (Glatze, kurzer grau-weißer Bart, dunkle rechteckige Brille, Alter). Echtes Logo aus der angehängten Datei.

## Sektionen (Layout-Kurzform, volle Texte im Prompt)
1 Hero: Foto Michael (Magazin, beiges Sakko) rechts, Text links, Beweiszeile mit Sternen, kleines H1, große Headline, Subline, Body, zwei Pillen, Rückversicherung.
2 Beweis-Leiste: Creme-Band, Direkt-Antwort links, 4 Beweise + Zitat rechts, Medienlogos.
3 Situationen: drei Karten (hell, Navy, Anthrazit), darunter Weg hinaus, Für-wen-Liste, Button.
4 Warum Michael: Text + Zahlenreihe links, Portrait (weißes Hemd, Holztür) rechts, Zitat, Button.
5 Methode: Titel links, Schritte 01–03 rechts.
6 Seminare: Foto-Band (Finca-Terrasse, goldene Stunde, Gruppe), Faktenreihe, drei Format-Karten, Button.
7 Erstes Gespräch: drei Schritte mit Linie, Notiz, Checkliste, Button + Telefon.
8 Stimmen: sechs offene Karten 3×2 mit Quelle und Sternen, drei Video-Kacheln, Button.
9 Orte und Termine: Navy-Band, sechs Ortskarten mit Foto und Daten, heller Button.
10 FAQ: Akkordeon zweispaltig.
11 Abschluss: dunkles Foto-Band, Häkchen, Beweis, Button, Telefon; Navy-Footer.

## Referenzbilder (`refs/`)
ref-michael-magazine.jpg (Hero), ref-michael-door.jpg (Warum Michael), ref-michael-cafe.jpg (Gesicht), ref-logo.png (echtes Logo), ref-entwurfA.jpg (aktuelles Design, Struktur und Stil).

## Bildregel
Echte Fotos sind die Referenz. GPT erzeugt die idealen Bilder für den Prototyp (Gruppe, Orte, Szenen) im Look der Marke. Michaels Gesicht kommt aus echten Fotos; erzeugte Bilder mit Michael gehen auf die Shoot-Liste.
