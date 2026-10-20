# me&you: Referenz remedyeditorial.com (Bausteine und Scroll-Verhalten)

Quelle: https://remedyeditorial.com/ (WordPress, eigenes Theme "remedy"). Gezogen am 05.10.2026.
Rohdaten: `00_project/assets/meandyou/referenz-remedy/` (index.html, app.css, app.js, featured-work.js, smooth-scroll, shared).
Zweck: Grundstock für Aufbau und Scroll-Gefühl. Wir übernehmen die Muster, nicht den Code und nicht die Marke (Farben, Schrift, Logo bleiben me&you).

## Warum sich die Seite gut anfühlt

| Baustein | Was die Seite tut | Technik (gemessen) |
|---|---|---|
| Weiches Scrollen | Die Seite gleitet nach, sie stoppt nicht hart | Lenis: `duration: 1.1`, Ease `1.001 - 2^(-10t)`, `smoothWheel: true`, `smoothTouch: false`. Aus bei `prefers-reduced-motion`. |
| Parallax im Raster | Karten im 2-Spalten-Raster bewegen sich verschieden schnell | Eigener Code auf Lenis-Scroll: ungerade Karten Faktor `0.06`, gerade Karten `0.18`, `translate3d`. Nur ab 1024 px. IntersectionObserver schaltet nur sichtbare Karten. |
| Stehende Titelspalte | Links bleibt der Sektionstitel stehen, rechts läuft der Inhalt | `position: sticky; top: 138px; align-self: flex-start` (Klasse `os-sticky-col`). Raster: Titel links schmal, Inhalt rechts breit. |
| Header als Kapsel | Oben groß und offen, beim Scrollen eine kleine schwebende Kapsel mit Logo und Menü | `position: fixed`, transparent, Kapsel mit Rahmen und Blur, Höhe 50 px. |
| Farbwechsel | Eine Sektion schaltet auf Schwarz, danach zurück auf Weiß | Klasse `js-bg-switch`, Wechsel beim Eintritt in den Viewport. |
| Großes Medium im Hero | Unter Wortmarke und Claim folgt ein großes Video mit runden Ecken | Sektion `m-leadspace`, Medium volle Containerbreite, großer Radius. |
| Zahlen als Kontur | Kennzahlen stehen groß in Outline-Schrift, darunter ein kurzer Satz | Sektion `m-stats-block`, Liste untereinander neben stehendem Titel. |

## Maße

- Container: max. 1440 px, Seitenrand 60 px (Desktop).
- Abstand je Sektion: 90 px oben und unten (Desktop), 45 px (Mobil). Kleine Stufe: 45 px.
- Letzte Sektion vor dem Footer: ca. 200 px Luft unten.
- Hintergrund: Weiß `#FFFFFF`, Nebenfläche `#FBF9F6`, Linie `#DBDAD7`.
- Text: Fließtext 20 px bei 1024 px Breite, Titel fett und klein (24 px), Hero-Claim 34 px. Wenig Größen, viel Raum.
- Aufbau der Startseite: nur 6 Sektionen (Hero, Arbeiten, Leistung, Feed, Zahlen, Kontakt).

## Übertragung auf me&you

| me&you-Block | Muster von Remedy |
|---|---|
| Hero | Claim oben, darunter großes Bild oder Video von Michael mit runden Ecken |
| Trust-Zahlen + Auszeichnung | Stehender Titel links, Zahlen in großer Serif rechts untereinander |
| Story + Problem | Stehender Titel links, Text läuft rechts |
| Orte | 2-Spalten-Raster mit Parallax (Karten verschieden schnell) |
| Termine | Stehender Titel "Termine 2026" links, Terminliste rechts, Daten wie Überschriften |
| Nutzen (9 Punkte) | Stehender Titel links, nummerierte Liste rechts |
| Zitat / Versprechen | Farbwechsel auf Dunkelnavy für genau eine Sektion |
| Stimmen | Horizontale Reihe wie der Feed, im dunklen Band |
| FAQ | Stehender Titel links, Akkordeon rechts |
| Abschluss + Kontakt | Titel links, kurzer Text, zwei Kontaktwege, ein Button |
| Header | Navigation oben offen, beim Scrollen Kapsel mit Logo und "Jetzt Gespräch buchen" |

## Regeln für den Bau

- Lenis mit denselben Werten. Auf Touch-Geräten natives Scrollen.
- Parallax nur ab 1024 px und nur mit kleinen Faktoren (0.06 bis 0.18).
- `prefers-reduced-motion` schaltet Lenis und Parallax aus.
- Sticky-Spalte nur ab Tablet-Breite. Mobil steht der Titel normal über dem Inhalt.
- Das Muster geht in Framer (Sticky, Scroll-Effekte) und in eigenem HTML. Die Plattform ist noch offen.
