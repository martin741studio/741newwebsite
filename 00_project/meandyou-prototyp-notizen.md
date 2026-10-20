# me&you: Notizen zum ChatGPT-Mockup und Regeln für den Live-Prototyp

Stand: 05.10.2026. Grundlage: ChatGPT-Bild v2 (Ganzseiten-Mockup), Ehlers.pdf (Design-Quelle), Remedy-Analyse (`meandyou-referenz-remedy-bausteine.md`), Ist-Texte (`meandyou-sektionen-kontext.md`).

## Regeln von Martin (05.10.)

1. **Eine Sektion = eine Bildschirmhöhe.** Beim Scrollen ist immer nur eine Sektion zu sehen.
2. **Einzige Ausnahme:** "Dein Ergebnis" (Zitat-Band mit Icons) und "Unser Ansatz" stehen zusammen auf einem Bildschirm. "Dein Ergebnis" ist ein schmales Band.
3. **Bilder:** zuerst echte Dateien, dann Bilder aus der Ehlers.pdf, fehlende Bilder selbst über ChatGPT erzeugen.
4. **Design-Entscheidungen** folgen der Ehlers.pdf.
5. **Aufbau und Scroll-Gefühl** folgen der Remedy-Seite.
6. **Texte bleiben Ist-Stand.** Keine Textänderungen.

## Was im ChatGPT-Bild stimmt (übernehmen)

- Reihenfolge der Blöcke und die Overlines als Sektionsnamen: Seminartermine, Dein Ergebnis, Unser Ansatz, Über Michael, Stimmen, Für wen?, FAQ.
- Hero mit drei Sprechblasen-Karten.
- Trust-Zahlen direkt unter dem Hero, mit Auszeichnung rechts.
- Termine als vier Karten mit Umschalter 2026 | 2027.
- "Dein Ergebnis" als Navy-Band: Zitat links, sechs Icon-Punkte rechts.
- "Unser Ansatz" als Vergleich in zwei Karten.
- Stimmen mit Umschalter Video-Stimmen | Kundenstimmen.
- Abschluss-CTA mit Kontaktformular über einem Ortsbild.

## Was im ChatGPT-Bild falsch ist (nicht übernehmen)

| Stelle | Fehler | Lösung im Prototyp |
|---|---|---|
| Alle Fotos von Michael | Gesicht erfunden | Echte Fotos von der Ist-Seite (5 Motive in hoher Auflösung) |
| Auszeichnungs-Siegel | Erfunden | Echtes ERFOLG-Cover "Top 100" von der Ist-Seite |
| Video-Thumbnails | Erfundene Personen, Studio-Look | Neutrale Platzhalter mit Play-Symbol, als Platzhalter markiert |
| FAQ | 7 erfundene Fragen | Die 13 echten Fragen und Antworten |
| Kundenstimmen | Zitate und Titel erfunden | Die 4 echten Zitate mit echten Namen |
| "Dein Ergebnis", "Unser Ansatz", "Für wen", Story, Über Michael | Texte umgeschrieben | Ist-Texte wörtlich |
| Orte-Titel "Besondere Orte für besondere Entwicklung." | Erfunden | Nur Overline "Seminarorte", kein neuer Satz |
| Abstände | Mehrere Sektionen pro Bildschirm, alles gepresst | Eine Sektion pro Bildschirm, Seitenrand 60 px, Luft 90 px |
| Hintergrund | Flächiges Beige | Warmes Off-White als Grund, Creme nur für einzelne Flächen |
| Fehlende Inhalte | Problem-Sektion ("Intelligente haben es schwerer") und die 9 Veränderungen fehlen | Beide als eigene Bildschirme behalten. Leicht zu entfernen, wenn nicht gewünscht |

## Aufbau des Prototyps (12 Bildschirme)

1. Hero + Trust-Zahlen
2. Story "Klügster im Raum"
3. Problem "Intelligente haben es schwerer" (mit den 5 echten Problem-Karten der Ist-Seite)
4. Seminarorte
5. Seminartermine (2026 | 2027)
6. Dein Ergebnis + Unser Ansatz
7. Die 9 Veränderungen
8. Über Michael + Auszeichnung + Medien-Logos
9. Stimmen (Videos | Kundenstimmen)
10. Für wen?
11. FAQ (13 Fragen)
12. Abschluss-CTA + Kontaktformular + Footer

## Übernommen von Remedy

- Weiches Scrollen mit Lenis (Dauer 1,1 s), aus bei "Bewegung reduzieren" und auf Touch.
- Header: oben offen, beim Scrollen eine schwebende Kapsel.
- Zwei-Spalten-Raster: Titel links, Inhalt rechts.
- Parallax in Bildern und Karten, nur am Desktop, kleine Faktoren.
- Genau eine dunkle Sektion als Farbwechsel.

## Bilder

| Bild | Quelle |
|---|---|
| Michael (Hero, Über Michael, Story-Variante) | Echt, Ist-Seite |
| Logo dunkel und hell | Echt, Ist-Seite |
| ERFOLG Top 100, Medien-Logos | Echt, Ist-Seite |
| Dubai, Mallorca, Barcelona | ChatGPT, nach Fotoregeln "Undersold" (goldene Stunde, Ort vor Mensch) |
| Meeting-Raum (Story) | ChatGPT, nach Fotoregeln "Overlooked" (kühles Licht, Architektur) |
| Kleine Gruppe (Für wen) | ChatGPT, nach Fotoregeln "Undersold" (kleine Gruppe, keine Bühne) |
| Abschluss-Landschaft | ChatGPT |

Die Fotos in der Ehlers.pdf sind zu klein für eine Bildschirmhöhe (PDF-Seite 920 × 514 px). Sie dienen als Stil-Vorlage für die ChatGPT-Bilder.

## Nicht im Prototyp

- Keine Seminarpreise (Regel: Preise nur im Gespräch).
- Formular sendet nichts. Buttons führen zur echten Buchungsseite.
- Mobil-Ansicht ist lesbar, aber nicht fein abgestimmt.
