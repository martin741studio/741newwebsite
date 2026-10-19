# Visual Check — Local-SEO-Seite (Track B)

Geprüft in Chrome (Browser-Pane), DE + EN, Desktop (1440 responsive) und Mobile (375px), 2026-10-19.

## Geprüfte Punkte
1. Hero: Headline, Sub, CTA, Kennzahlen-Zeile, eingebettetes Intro-Video — DE + EN ok.
2. Quiz-Overlay öffnet über den CTA-Button (`data-qz`), Schritt 1 von 6 korrekt, Overlay unverändert — DE + EN getestet, ok.
3. Prozess-Zeitleiste: 3 Schritte, Linie zeichnet sich, Zahlen zählen hoch — ok.
4. Echtes Beispiel (Maps-Scan Olching): echtes Bild + Ziel-SVG, Label „Ziel-Szenario (Simulation)" korrekt (EN: „Target Scenario"), 3 Chips, Fußnote — ok.
5. Proof-Wall: 29 Karten, horizontal scrollbar, Pfeil-Buttons funktionieren (scrollLeft-Test bestätigt), echte Avatare/Initialen laden — ok.
6. Testimonials: 5 echte YouTube-Embeds, Grid — ok.
7. Wachstums-Potenzial: Vergleichs-Kasten, Pflicht-Fußnote „illustrativ" vorhanden — ok.
8. Gründer-Sektion: Foto + Zitat — ok.
9. Related-Links + Abschluss-CTA + Footer — ok.
10. Sticky-Leiste erscheint nach ~900px Scroll, bleibt sichtbar, verdeckt keinen CTA — ok.

## Gefundene Probleme (behoben)
1. Hero-Video hatte `loading="lazy"`, lud auf Mobile (375px) nicht zuverlässig im ersten Viewport. **Behoben:** `loading="lazy"` beim Hero-Video entfernt (Above-the-Fold-Inhalt soll nicht lazy laden), restliche Testimonial-Videos (unterhalb des ersten Viewports) behalten `loading="lazy"`. Nach Fix in Mobile-Emulation erneut geprüft: lädt korrekt.

## Seitengewicht
~1,5 MB Ressourcen beim ersten Laden (DE, Desktop), unter dem 12-MB-Gesamtbudget. Erstes Sichtfeld ohne die YouTube-iframes (die selbst nachladen) deutlich unter 2,5 MB.

**Visual check done in Chrome, 10 items checked, 1 fixed, 0 open.**
