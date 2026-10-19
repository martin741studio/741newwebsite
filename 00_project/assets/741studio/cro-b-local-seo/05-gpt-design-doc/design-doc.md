# GPT Design Doc — 741.Studio Local-SEO-Landingpage (Track B, B5/B6)

Stand 2026-10-19. Nachgeholt nach Martins Hinweis, dass der GPT-Mockup-Schritt nicht übersprungen werden darf. Ein ChatGPT-Chat ("Local SEO Landingpage Strategy"), Martins Session, Claude in Chrome.

## Global Style Block (vor den Prompt kopiert)

```
MARKE: 741.Studio, digitale Wachstumsagentur (SEO, Websites, Performance-Marketing). Diese Seite: Local-SEO-Landingpage, Hauptziel ist eine kostenlose Sichtbarkeits-Analyse (Formular-CTA).

FARBEN: Hintergrund warmes Creme #f7f6f2, Text dunkles Anthrazit #1a1a1a, Karten weiß #ffffff mit sehr hellem Rand #eceadf, EIN Akzent: Zitronengelb #fac118 (nur für Buttons, Linien, kleine Markierungen, NIE als große Textfarbe oder Flächenfarbe).

TYPOGRAFIE: Klare, geometrische serifenlose Schrift (PP-Neue-Montreal-Charakter), sehr große fette Headlines, ruhiger Fließtext.

MOOD: bewiesen, selbstbewusst, aufgeräumt, seriös — NICHT verkäuferisch, NICHT reißerisch, kein Stockfoto-Kitsch, kein Hochglanz-Agentur-Klischee.

LAYOUT: Helle, luftige Sektionen auf Creme-Grund, Karten mit weichem Schatten, großzügige Abstände.

FORMAT: Eine durchgehende Full-Page-Mockup-Ansicht (Hochformat, lange scrollbare Seite, 1 Bild), realistisch wie ein echter Website-Screenshot, kein Text muss lesbar/final sein (Platzhaltertext reicht), es geht um Layout, Rhythmus und Farbwirkung.

SEKTIONEN, von oben nach unten: Hero (Headline+CTA+Video), Prozess (3-Schritte-Zeitleiste), Echtes Beispiel (Heute/Ziel-Karten), Beweis-Wand (horizontale Karten-Reihe), Video-Testimonials (5er-Grid), Wachstums-Potenzial (Vergleichs-Kasten), Gründer-Zitat, Abschluss-CTA.
```

## Ergebnis

`06-gpt-assets/full-page-mockup-v1.png` (1 Bild, Full-Page). Laufzeit 1 Min. 8 Sek.

## Abgleich mit dem bereits gebauten Prototyp

Der Prototyp (`04_site/de/pages/local-seo.html`, `04_site/pages/local-seo.html`) war zum Zeitpunkt des Mockups bereits gebaut (siehe Status-Log — dieser Schritt wurde nachgeholt, nicht vorgezogen). Abgleich:

| Sektion | GPT-Mockup | Bereits gebauter Prototyp | Ergebnis |
|---|---|---|---|
| Hero | Headline links, Video rechts, 3 kleine Vertrauens-Label unter CTA | Headline links, Video rechts, 1 Kennzahlen-Zeile unter CTA | Gleiche Struktur, bestätigt |
| Prozess | Vertikale Zeitleiste, 3 nummerierte Punkte | Vertikale Zeitleiste, 3 nummerierte Punkte, Linie zeichnet sich | Gleiche Struktur, bestätigt |
| Echtes Beispiel | Zwei Karten (Heute/Ziel), darunter 3 Chips | Zwei Karten (echter Scan/Ziel-Simulation), darunter 3 Chips | Gleiche Struktur, bestätigt |
| Beweis-Wand | Horizontale Karten-Reihe mit Avatar + Prozentzahl | Horizontale scrollende Karten-Reihe mit Avatar + echtem Ranking-Ergebnis | Gleiche Struktur. **Wichtig:** GPT-Mockup-Zahlen (312 %, 428 % usw.) sind frei erfunden/illustrativ für den Mockup — im echten Prototyp stehen ausschließlich die 29 echten, verifizierten Ergebnisse aus `02-data/dataset.md`, keine GPT-Zahl wurde übernommen |
| Testimonials | 5er-Grid, Kreis-Avatare | 5er-Grid, Hochformat-Video-Karten (echte YouTube-Embeds) | Gleiche Grundidee, Prototyp nutzt echte Videos statt Platzhalter |
| Wachstums-Potenzial | Vergleichs-Kasten mit Sparklines | Vergleichs-Kasten mit Pfeil + Impact-Chips, Pflicht-Fußnote „illustrativ" | Gleiche Struktur, Prototyp hat die vorgeschriebene Kennzeichnung, die der Mockup naturgemäß nicht zeigt |
| Gründer | Foto + Zitat | Foto (leicht gedreht, Polaroid-Look) + Zitat | Gleiche Struktur, bestätigt |
| Abschluss | Zentrierter gelber Button | Zentrierter gelber, atmender Button | Gleiche Struktur, bestätigt |

**Fazit:** Der unabhängig von GPT erzeugte Mockup bestätigt Aufbau, Reihenfolge und Farbsprache des bereits gebauten Prototyps strukturell. Keine Abweichung, die eine Änderung am Prototyp nötig macht. Einzige Differenz: GPT zeigt erfundene Platzhalter-Zahlen in der Beweis-Wand und im Potenzial-Block — der echte Prototyp verwendet ausschließlich echte, verifizierte Daten, wie von Anfang an vorgesehen.
