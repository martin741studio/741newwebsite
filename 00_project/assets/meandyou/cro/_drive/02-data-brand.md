# Brand — me&you Communication / Michael Ehlers

Quelle: Ehlers.pdf V1.1 (Source of Truth Design), `quellen/meandyou-design-richtlinien.html`, Copy Deck Round 3, Tokens von Entwurf A (`prototype/page.html` :root). Logo vorhanden (echt, Vektor und 2052 px).

Vorrang: Look and Feel aus der PDF, Hierarchie aus dem Sales-Feedback. Entwurf A ist die freigegebene Richtung (Phil).

## Farben (Hex)
| Rolle | Hex | Hinweis |
|---|---|---|
| Text | #2A2622 (ink) | Kontrast auf Papier 14,2 : 1 |
| Text gedämpft | #5E5650 | statt #7B736B (4,4 : 1, zu schwach für 16-px-Text) |
| Hintergrund | #FAF8F4 (paper) | warmes Off-White, Grundfläche |
| Zweiter Hintergrund | #F2EDE4 (cream) | Wechselbänder, Karten |
| Sand | #D8CCB7 | warme Akzentflächen, Linien |
| Taubenblau | #7E99B6 (dove) | Overlines, Zahlen, Icons. **Nicht** für Text auf Weiß (2,95 : 1) |
| Taubenblau hell | #DFE6EE | Karte Situation 1 |
| Dunkelnavy | #2B3C52 (navy) | dunkle Bänder, Karte Situation 2, Footer |
| Anthrazit warm | #47403A (char) | Karte Situation 3 |
| **CTA (einzige Akzentfarbe)** | **#4F6D90** | Taubenblau vertieft. Weiße Schrift 5,35 : 1 (AA). Copy Deck fordert „ein gesättigtes Element“: der Button ist das einzige Element in dieser Farbe. Auf dunklen Bändern: Button hell (#FAF8F4) mit Navy-Schrift |
| CTA hover | #3F5E8C | 6,6 : 1 |
| Linie | rgba(71,64,58,.16) | |
| Sterne | #C9A24A (gedämpftes Gold) | nur Bewertungssterne |

Entwurf A nutzte #7E99B6 für den Button (weiße Schrift 2,95 : 1). Das ist ein Grund für „bessere Umsetzung“.

## Schrift (Google Fonts)
- Überschriften: Libre Baskerville 400 (selten 700), ruhig, erwachsen.
- Fließtext, Overline, UI: Inter 400/500/600.
- Wortmarke: echtes Logo, nie gesetzt.
- Größen bei 1440 px: H1 sichtbar 60 bis 68 px; H2 42 bis 46 px; H3 22 bis 26 px; Body 18 px; klein mindestens 16 px; Overline 13 px Versalien mit 0,2 em Sperrung (einzige Ausnahme unter 16 px, reines Label).
- Verhältnis Headline zu Body etwa 3,5 : 1.

## Bildstil
- Echte Fotos von Michael: Tageslicht, warm, Café, Holz, Leinen, nie Bühne als Hauptmotiv.
- Persona-Bilder: Replayers warm, privat, Innenraum, Abend. Overlooked kühles Tageslicht, Architektur, Glas. Undersold goldene Stunde, Ort und Gruppe vor Personen.
- Immer Menschen im Bild. Reportage, niemand schaut in die Kamera (außer Michael-Portrait). Leichtes Korn, nie glatt.
- Nie: Bühne mit Menge, Hotel-Ballsaal, Lanyards, Stock-Look, Konferenz.

## Formen
- Weiche Ecken: Radius 22 px für Karten und Bilder, Buttons als Pille (Copy Deck und Entwurf A). Pille bleibt, weil die Marke sie so führt (Ausnahme zu Regel R9.5, begründet).
- Keine harten Trennlinien, viel Weißraum, eine Idee pro Bildschirm.
- Zahlen 01, 02, 03 in Taubenblau, Serif.

## Stimmung (5 Wörter)
ruhig · souverän · warm · erwachsen · selten

## Layout-Muster (aus Entwurf A, beibehalten)
- Header offen am Seitenanfang, wird nach 60 px zur schwebenden Kapsel (Logo, 5 Menüpunkte, Button).
- Hero: Text links, großes Foto rechts als Vollbild-Hintergrund mit weichem Verlauf.
- Situationen: 3 gleich hohe Karten, Foto oben, farbiger Textteil unten (hell, navy, anthrazit).
- Raster: Titel links, Inhalt rechts (Methode).
- Ein Vollbild-Band mit Foto (Seminare) und ein dunkler Abschluss mit Foto.
- Parallaxe: von Martin für me&you ausdrücklich gewollt (08.10.), ein Faktor für alle Bilder. Abweichung von der Motion-Spec, dokumentiert in `07-prototype/motion.md`.

## Fotoinventar → `01-input/INVENTORY.md`
