# GPT Design Doc — me&you, Landingpage „The Undersold“
Stand 2026-10-12. Quelle Text: `04-copy/approved-copy.md` (freigegeben, Martin „confirmed continue“). Verfahren wie Seminar-, Michael-, Rhetorik- und FAQ-Seite: ein Bild, Startseiten-Mockup als Stil-Referenz. Prompt `prompt.txt` (volle Copy, 11 Sektionen), Generator `build_prompt.py`, Text-Einheiten `units.json`. `check_prompt.py` gegen `04-copy/approved-copy-plain.txt`: 105 Zitate, alle gefunden.

## Globaler Stil (Kurzform, voll in `build_prompt.py`)
Sprache der Startseite (Header-Kapsel, Schrift Libre Baskerville + Inter, Footer), Persona-Stimmung: weit, warm, goldenes Licht, wenige Elemente je Bildschirm, breite Bildausschnitte, kleine Schrift vor großem Bild, Orte und Daten als Überschriften. Farben Papier #FAF8F4, Creme #F2EDE4, Sand #D8CCB7, Gold #C9A24A nur für Linien, Datenakzente und Sterne, Anthrazit #47403A für dunkle Bänder, Navy #2B3C52 Footer. Einzige Button-Farbe #4F6D90; ein Button im Inhalt (S11), Header-Button bleibt.

## Sektionen
1 Hero: breites Foto Mallorca-Küste in goldener Stunde, Finca-Terrasse, kleine Gruppe weit im Bild, kein Trainer, Text unten links klein, kein Button · 2 Kurz-Antwort mit vier Faktenzeilen, kleinem echten Porträt Michael (braunes Sakko), Zitat Röser · 3 dunkles Band, vier Situationen im 2 × 2 Raster · 4 Methode, drei Schritte mit Goldnummern · 5 Orte und Termine: sechs breite Ortskarten, Ortsname groß, Daten als Überschriften, Zitat · 6 Format: Foto-Band kleine Gruppe auf Terrasse, vier Spalten, drei Formate als ruhige Zeilen, Bundle, Enthalten-Box · 7 Für wen mit großem Zitat · 8 Michael mit echtem Foto (olive Jacke) und vier Belegen · 9 drei offene Zitat-Karten · 10 FAQ-Akkordeon zweispaltig · 11 dunkles Foto-Band Terrasse am Abend, drei Schritte, einziger Button, Telefon, Beweiszeile, Footer.

## Bilder
- Neu per GPT (Step 5b): `hero-coast.webp` (Hero) und bei Bedarf `format-terrace.webp` (S06 Band), jeweils eigener Chat, ohne erkennbare Gesichter, ohne Trainer.
- Echt oder freigegeben: Ortskarten `city-*.webp` (Pexels, Seminarseite), Abschluss `closer-terrace.webp` (Startseite), Michael `michael-olive`, `michael-jacket`.
- Shoot-Liste (Handoff): echte Fotos je Seminarort in goldener Stunde, kleine Gruppe auf der Terrasse.

## Refs (an ChatGPT)
`refs/ref-homepage-mockup.jpg`, `refs/ref-logo.png`, `refs/ref-michael-jacket.jpg`, `refs/ref-michael-olive.jpg`, `refs/ref-city-mallorca.jpg`.

## Prototyp-Zusatz (nicht im Bild)
Schema JSON-LD aus `content-writing/lp-undersold/05-final/schema.jsonld`, `noindex, nofollow`, Links nach Muster `_site` (`gespraech-buchen.html?utm_source=lp-undersold&utm_content=abschluss|header`).
