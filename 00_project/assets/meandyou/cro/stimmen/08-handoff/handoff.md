# Handoff-Teil — Seite „Stimmen“ (für die Gesamtübergabe der Hauptsession)
Stand 2026-10-12. Prototyp: `07-prototype/index.html` (Port 8816). Copy: `04-copy/approved-copy.md` (freigegeben). Mockup: `06-gpt-assets/full-page-v1-final.png`.

## Neue URL und Links
- Neue Seite `/stimmen`. Menüpunkt „Stimmen“ zeigt heute auf `index.html#stimmen` → auf `/stimmen` umstellen. Keine Weiterleitung nötig (keine alte URL).
- Eingehende Links fehlen: Startseite (Bewertungsabschnitt), Michael (S07 Stimmen), Seminare (Stimmen) sollen auf `/stimmen` verlinken (Link-Netz: nur 1 eingehender Link).
- Korrektur auf anderen Seiten: Seminarseite nennt „Steile Lernkurve mit Soforteffekt …“ als Justus S. Laut ProvenExpert ist es Katharina R. (14.05.2023). Startseiten-Prototyp zeigt noch „4,8 bei Google“.

## Schema
WebPage + BreadcrumbList + EducationalOrganization im Head. Kein AggregateRating, kein Review-Markup (eigene Bewertungen, kein Sternwert). `noindex,nofollow` solange Vorschau.

## [FEHLT] / gelbe Marken
1. [FEHLT: Vorname und Rolle der drei Videopersonen, Einwilligung zur Nennung]
2. [FEHLT: vollständiger Wortlaut Zitat Neven Subotic]
3. [FEHLT: Name und Rolle der Person im Gespräch]
4. [FEHLT: Wortlaut Video 2 zur Abschlussquote, Zahl im Bild]
5. Einwilligung Gruppenfoto (Teilnehmergesichter)

## Videos
Wistia-MP4 neu kodiert in `07-prototype/assets/v-stimme-1..3.mp4` (crf 30). Standbilder `vp-*-tall.webp` (9:16) sind Einzelbilder aus den Videos; das eingebrannte Untertitel-Wort ist retuschiert. Hero-Collage verlinkt mit weichem Scrollen auf `#videos` (Martin, 12.10.). Live: Wistia-Einbettung statt MP4.

## Fotos (Shoot-List)
Keine generierten Personenbilder. Abschlussbild `closer-terrace.webp` ist das GPT-Bild der Startseite.
