# Bewegung — 741.studio Startseite (Track B)

Stand 2026-10-11. Grundlage: Element-Pool-Abstimmung (`../00-element-pool/votes-summary.md`), Konzept (`../05-gpt-design-doc/concept/concept.md`). Alle Bewegungen laufen einmal, nicht als Dauerschleife außer dem sehr langsamen Drift im dunklen Band.

## Eingebaute Bewegungen
- **Punkt-Formation (Hero, Signature Idea):** graue/rote Punkte ziehen sichtbar zum Rand, bilden das echte Vorher/Nachher-Bild, eine Zahl zählt dabei hoch (+278 %). Läuft einmal beim Erscheinen im Bild (IntersectionObserver).
- **Kopf schrumpft** beim Scrollen (Höhe und Logo-Größe).
- **Gelbe Linie wächst** unter dem aktiven Menüpunkt beim Hover.
- **Hauptbutton atmet** sehr langsam (4,5 s) im Hero und im Abschluss.
- **Kennzahlen-Karten gleiten gestaffelt ein** und zählen beim Erscheinen hoch (Outcome-Sektion).
- **Leistungszeile zeigt Kurzzeile** beim Hover, mit wachsender Linie.
- **Glänzendes Objekt driftet** sehr sanft im dunklen Leistungen-Band, abhängig von der Scroll-Position (ersetzt das fremde Stock-Video der Live-Seite).
- **Alle übrigen Blöcke:** einmaliges Einblenden mit leichtem Hochschweben (`.rv`), ausgelöst beim ersten Sichtbarwerden.

## Nicht eingebaut (Pool-Votum: Nein)
Gezeichnetes Anführungszeichen im Gründer-Teil, Zeitleisten-Muster im Gründer-Teil, Punkte lösen sich in den Partner-Logos auf (der Punkt-Faden bleibt auf den Hero begrenzt), Bogenrahmen am Gründer-Foto.

## Schalter
`?rm=1` oder `prefers-reduced-motion: reduce`: alle `.rv`-Elemente stehen fertig da, der Hauptbutton atmet nicht, die Punkt-Formation und die Kennzahlen zeigen sofort den Endzustand, der Drift im dunklen Band bleibt aus.
`x`-Taste: X-ray-Schalter ist in der Klasse vorbereitet (`body.xray`), aber ohne sichtbare Markierung in dieser Variante, da kein Code-gezeichnetes Element existiert, das von einem Medien-Element unterschieden werden müsste (alle Formen sind entweder echte Bilder oder einfache CSS-Flächen).
`?shot=1`: alle Bewegungen zeigen sofort den Endzustand, für Screenshots.

## Keine-Bewegung-Zonen
Garantie-Pille-Text, Sterne-Zeile, Preise (keine auf der Seite), rechtliche/Fuß-Texte, CTA-Buttons selbst (nur Hover ändert sich normal).
