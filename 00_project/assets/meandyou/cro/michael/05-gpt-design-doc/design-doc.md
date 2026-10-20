# GPT Design Doc — me&you / Michael Ehlers, Michael-Seite

Stand 2026-10-12. Quellen: `../../02-data/brand.md`, `03-diagnosis/diagnosis.md` (P1 Personen-Seite), `04-copy/approved-copy.md` (freigegeben 12.10.).
Verfahren wie Seminarseite: ein Bild der ganzen Seite, eine Nachricht, neuer Chat, Startseiten-Mockup als Stil-Referenz. Prompt `prompt.txt` (13.716 Zeichen, 94 Zitate, check_prompt 0 fehlend), Generator `build_prompt.py`.

## Sektionen
1 Hero: echtes Foto Stuhl (2026), Text links · 2 Antwort + Fakten + Medienlogos · 3 Zeitleiste 1990/2008/2014/2018/Heute · 4 Motto + Methode, echtes Foto weißes Hemd · 5 Bücher als typografische Karten (keine erfundenen Cover) + Podcast · 6 Navy-Band St. Gallen + Medien · 7 Stimmen 2×2 · 8 echtes Gruppenfoto + Seminare · 9 Gespräch · 10 FAQ · 11 Abschluss.

## Referenzen (`refs/`)
ref-homepage-mockup.jpg, ref-logo.png, ref-michael-chair.jpg, ref-michael-white.jpg, ref-group.jpg (alle echt, Quelle institut-ehlers.de bzw. Startseiten-Lauf).

## Bildregel
Keine neuen GPT-Bilder nötig: alle Bildplätze mit echten Fotos (Michael, Gruppe) oder Startseiten-Assets (Abschluss-Terrasse). Buchcover nur typografisch, keine erfundenen Cover.
