# Self-Check v2: Prototyp Desktop 1440 px, Naturheilpraxis Daniela Dumann

Stand 2026-10-11. Prototyp: `07-prototype/v2/index.html` (eine Datei, Assets in `assets/`). Screenshots in `screenshots/`. v1 (mobile-first) bleibt unverändert in `07-prototype/`.

Geprüft in: Headless Chrome mit 1440 px Fensterbreite (`?shot=1` zeigt alle Reveal-Zustände) und Live-Scroll-Check in Martins Chrome: 28 Reveal-Elemente, alle werden einmalig sichtbar, keine kaputten Bilder, keine Konsolenfehler, Karte und Pin laden, CTA im ersten Bildschirm (Button endet bei y≈537 von 800).

Mobile ist nicht Teil dieses Workflows (Martin, 2026-10-11). Die Seite ist ab 1100 px Breite ausgelegt.

## Was neu ist gegenüber v1

- Layout Abschnitt für Abschnitt am finalen Mockup ausgerichtet: Kopfzeile mit sieben Menüpunkten, Hero mit Schmetterlings-Hintergrund und freigestelltem Portrait, Beweis-Leiste, fünf Themenkarten mit gemalten Icons, Leistungskarten, vier Schritte, dunkles Über-mich-Band mit Lavendel-Foto und Linienzeichnung, Bewertungen, FAQ, Standort mit Symbolen, Abschluss mit Linienzeichnungen links und rechts.
- Bilder: echte Portraits in voller Auflösung (freigestellt per rembg), echte Fotos von ihrer Website (Schmetterling, Lavendel, Fläschchen), sechs neu erzeugte Bilder in 1024 px oder mehr. Keine Ausschnitte aus dem Mockup mehr.
- Mobile-Teile entfernt: Sticky-Leiste, Telefon-Symbol im Kopf, Mobil-Breakpoints.

## Scorecard (Desktop)

| # | Item | Prio | Score | Beleg |
| --- | --- | --- | --- | --- |
| 4 | Primärer CTA im ersten Bildschirm (1440×800) | A | 2 | Button bei y≈485–537 im Screenshot `desktop-1440-first-viewport.png` |
| 11 | CTA mindestens alle 2 Sektionen | A | 2 | Hero, Themen, Schritte, Über mich, Standort, Abschluss |
| 21 | Typografie | C | 2 | Body 17 px, Buttons 54 px |
| übrige | wie in `../self-check.md` (v1) | | | Inhalt unverändert, nur Layout und Bilder |

Summe unverändert 38 von 44. Zwei A-Items stehen weiter auf 1 und warten auf Martin: Item 3 (Sub-Headline Situation zuerst) und Item 5 (CTA-Text mit Nutzen). Item 6: die Zeile „Erstgespräch: 60 Minuten, 220 €" im Hero ist weiter nicht im freigegebenen Hero-Text.

## Abweichungen vom Mockup (bewusst)

- Leistungen: 3 × 2 Karten statt 6 in einer Reihe, weil sechs Spalten bei 1440 px zu schmal für die Überschriften sind.
- Karten-Schaltfläche: Textlink „Mehr erfahren" statt oliver Button, damit nur der Haupt-CTA oliv ist (Item 10).
- FAQ als Akkordeon, eine Antwort offen (Mockup zeigt alle offen).
- Kein Kopf-Button im Menü, wie im Mockup.
- Tagline „Naturheilkunde im Einklang mit Mensch und Natur" und die Pflanze im Standort-Abschnitt nicht übernommen.
- Bewegung nach `00_project/cro-homepage-motion-spec.md`: ein Highlight je Sektion, Breathing-CTA nur Hero und Abschluss.

## Offene Punkte (für Handoff)

- `[FEHLT]` Absage-/Stornobedingungen (Platzhalter im FAQ sichtbar markiert).
- `[FEHLT]` Parken am Standort.
- `[FEHLT]` Deutsche Originaltexte der Bewertungen.
- Shoot-Liste (erzeugte Bilder ersetzen durch echte Fotos): Darmsanierung, Ernährung, Homöopathie, Oligoscan, Massage. Das Icon-Set ist gemalt und bleibt.
- Leistungs-Links sind `#`-Platzhalter bis zum Rebuild.
- Karte lädt OpenStreetMap beim Aufruf, für den Live-Gang Einwilligung nötig (DSGVO).
- Impressum und Datenschutz sind Platzhalter. Das Logo-Icon (Hildegard-Zeichnung) ist nicht eingebaut.
- Mobile-Version: eigener späterer Workflow.
