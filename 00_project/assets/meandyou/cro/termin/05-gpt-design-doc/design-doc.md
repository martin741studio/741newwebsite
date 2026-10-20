# GPT Design Doc — me&you, Seite „Gespräch buchen“
Stand 2026-10-12. Quelle Text: `04-copy/approved-copy.md` (freigegeben). Verfahren wie Seminar-, Michael- und Rhetorik-Seite: ein Bild, Startseiten-Mockup als Stil-Referenz. Prompt `prompt.txt`, Generator `build_prompt.py`, Text-Einheiten `units.json` (aus `approved-copy.md`, `check_prompt.py`: 65 Zitate, 0 fehlen).

Seitentyp: Buchungsseite, ablenkungsfrei. Header nur Logo und Telefon, keine Navigation. Footer nur Rechtliches und Kontakt.

| # | Abschnitt | Layout |
|---|---|---|
| S01 | Hero + Kalender | links 40 % Text (Kicker, H1, 3 Häkchen, Gesprächspartner), rechts 60 % Calendly-Karte, Oberkante auf Höhe H1, ganz im ersten Bildschirm. Unter der Karte: ProvenExpert-Zeile, Telefon, Datenschutz-Zeile |
| S02 | Ablauf | Creme-Band, 3 Schritte mit Linie, Kasten „Im Gespräch klärst du“, Button |
| S03 | Mit wem du sprichst | 2 Karten: Gesprächspartner (Platzhalter), Michael als Kopf dahinter (echtes Foto Holzrahmen) |
| S04 | Stimmen | ProvenExpert-Zeile, 3 offene Zitatkarten, Button |
| S05 | Vorbereitung | Creme-Band, 3 Kärtchen, Absatz WhatsApp und Umbuchen |
| S06 | FAQ | 6 Fragen offen in 2 Spalten, Button |
| S07 | Abschluss | Navy-Band, Copy-Deck-Zeile, heller Button, Telefon |
| S08 | Zustand nach Buchung | gleiche Hero-Fläche: links „Dein Termin steht.“ + 3 Schritte + Video-Platz, rechts Calendly-Bestätigung |

Buttons „Termin wählen“ springen zu `#kalender` (kein neuer Seitenaufruf). Eine CTA-Farbe #4F6D90. Calendly-Farben: primary `4F6D90` (statt v2 `64809e`), Text `2a2622`, Hintergrund weiß.
Refs: `refs/ref-homepage-mockup.jpg` (Startseiten-Mockup, aus `../06-gpt-assets/full-page-v1-final.png`), `refs/ref-logo.png`, `refs/ref-michael-door.jpg` (echtes Foto). Keine neuen GPT-Bilder: Michael-Foto ist echt, Gesprächspartner bleibt Platzhalter bis zum Kundenfoto.
