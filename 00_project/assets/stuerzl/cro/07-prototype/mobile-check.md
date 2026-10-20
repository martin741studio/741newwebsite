# Mobile-Check: Variante A (ruhig), Prototyp STÜRZL Steuerstrafrecht

Datum 2026-10-11 · Quelle: `_build/template.html` (nur dort geändert, `build.py` unverändert) · Build: `python3 _build/build.py` · Messung mit Headless-Chrome, Seite in iframe mit echter Breite (Headless-Chrome hat ein Mindestfenster von 500 px) · `?shot=1`.

## Prüftabelle

| # | Prüfung | Ergebnis | Messwert |
| --- | --- | --- | --- |
| 1 | Breiten geprüft | ok | 320, 360, 390, 430, 768, dazu 901, 1024, 1099, 1100, 1440 |
| 2 | `<meta name="viewport">` | ok | `width=device-width, initial-scale=1` vorhanden |
| 3 | Kein horizontaler Überlauf | ok | `scrollWidth` = Viewport bei 320, 360, 390, 430, 768, 1024; 0 Elemente breiter als der Viewport (nach Korrektur, siehe unten) |
| 4 | Tap-Ziele unter 44 × 44 px (ohne Links im Fließtext) | ok bis 768 | 0 bei 320, 360, 390, 430, 768. 1 Link im Fließtext ausgenommen (Datenschutzerklärung im Einwilligungstext). Bei 901 bis 1099 (Tablet quer) nicht erzwungen: 16 Ziele zwischen 13 und 41 px hoch (Telefonlinks, Mehr erfahren, Route planen, Fußlinks) |
| 5 | Texte unter 16 px | ok | nur Eyebrow-Labels 15 px (Aufklären…, Mandanten) und Prototyp-Hinweise `[FEHLT]` 14 px. Fließtext 17 px, Buttons 16 px, Formularfelder 16 px |
| 6 | Erster Bildschirm 390 × 844 | ok | Notfallleiste 0 bis 60, Kopf 60 bis 125, H1 (34,4 px) 199 bis 322, Sub-Text bis 531, grüner Button 633 bis 690. Bei 360 × 780: Button bis 681. Bei 430 × 932: bis 659. Foto folgt darunter (ab 949), kein Überlapp |
| 7 | Kopfzeile | ok | sticky, 64 px (+ 1 px Linie); Logo, grüner Button „Vertraulich anfragen“, Menü-Button 44 × 44 px; bei 360 passt alles (Logo 79 px, Button 186 px) |
| 8 | Menü | ok | Hamburger öffnet ein Panel unter der Kopfzeile mit 6 Links à 56 px; schließt bei Link-Klick, Klick daneben, Esc und beim Wechsel auf Desktop; `aria-expanded` und `aria-label` gesetzt; im geschlossenen Zustand nicht fokussierbar (`visibility:hidden`) |
| 9 | Raster einspaltig | ok | Trust-Chips (2 Spalten ab 601 px, 1 Spalte darunter), Situationen, Leistungen (2 Spalten 601 bis 1099 px, 1 Spalte darunter), Schritte (vertikale Zeitleiste), Über-mich, Zeitleiste, Bewertungen, Vertrauens-Spalten, Standorte, Abschluss-Formular, Fuß |
| 10 | Standort-Karten | ok | Kartenkachel bleibt sichtbar (16 : 8 über dem Text unter 600 px, links 200 px breit darüber) |
| 11 | Formular | ok | Felder 16 px Schrift, 50 bis 52 px hoch; Haken-Felder 22 px, Zeile mindestens 44 px; Buttons 56 und 48 px hoch, volle Breite; Telefonlinks je 44 px hoch |
| 12 | FAQ | ok | Zeile mindestens 56 px (gemessen 56) |
| 13 | Überschriften und Schrift | ok | H1 31,5 px bei 360, 34,4 px bei 390, 38,3 px bei 430, 46 px ab 600; H2 28 bis 38 px (clamp); Body 17 px; Silbentrennung (`hyphens:auto`) greift bei 768 („Wirtschafts-strafrecht“) |
| 14 | Bilder | ok | alle `object-fit: cover` mit festem Seitenverhältnis (Hero 4 : 3,3 bzw. 16 : 8 bzw. 16 : 7, Büro 4 : 3 bzw. 16 : 9, Porträt 4 : 3,4 bzw. 16 : 9); Gesicht im Hero bleibt im Ausschnitt (Position 47 % 26 %) |
| 15 | Nachweis-Elemente | ok | Namensschild unter dem Foto als statischer Block, kein Überlapp |
| 16 | Bewegung | ok | Atmen genau 2 (Hero und Abschluss, wie vorher); Reveal einmal; `prefers-reduced-motion` greift; `?rm=1` neu ergänzt (siehe unten); `?client=1` blendet `.flag` und `.proto` weiter aus (Klasse `cview` gesetzt); `?shot=1` zeigt alle Zustände |
| 17 | Text unverändert | ok | `check_text.py`: 202 Segmente, 0 nicht gefunden |
| 18 | Desktop-Pixel-Vergleich | ok, 0 Pixel Unterschied | Vorher-Build (alte Vorlage mit aktueller Copy) gegen Nachher-Build, mit `--force-prefers-reduced-motion` (sonst rauscht die Atmen-Animation): 1440, 1280, 1100 und 1920 px Breite, volle Seite (9105 bzw. 9446 px Höhe): 0 abweichende Pixel |

## Was geändert wurde

Alle neuen Regeln stehen in Media-Queries (≤ 1099, ≤ 900, 601 bis 1099, ≤ 600, ≤ 480, ≤ 400, ≤ 359). Ab 1100 px gilt unverändert das bisherige Layout.

- Kopfzeile: unter 1100 px Menü-Button und Panel statt der sechs Links. Der grüne Button bleibt im Kopf.
- Notfallleiste: Zeilenhöhe und Telefonlinks mit 44 px Tippfläche, ohne dass die Leiste höher wird (Polster mit negativem Rand).
- Hero unter 1100 px: Text zuerst, Foto darunter mit weichem Übergang oben, Namensschild als Block darunter. Telefon-Pille unter 600 px als Block mit zwei 44-px-Zeilen, darüber 601 bis 1099 px in einer Zeile.
- H1 skaliert über `clamp` so, dass der unterstrichene Teil „Frankfurt und München.“ in einer Zeile bleibt (ohne dies lief er bei 390 px über den Rand; der Hero-Container war 402 px breit).
- Inhalt: alle Mehrspalter einspaltig bzw. 2 Spalten auf dem Tablet; Schritte als vertikale Zeitleiste (Linie wächst von oben); Zeitleiste im Über-mich-Block gestapelt unter 600 px; Buttons in Abschnitten volle Breite; Links mit 44 px Höhe.
- Formular: Einwilligungstext fließt unter 900 px normal (das Label ist ein Flex-Container; der Link „Datenschutzerklärung“ brach als eigene Spalte aus und drückte das Formular über den Rand).
- Fuß: gestapelt, Links 44 px hoch.
- `?rm=1`: im Prototyp gab es das bisher nicht. Ein Zeilen-JS setzt die Klasse `rm` auf `<html>`, CSS spiegelt die `prefers-reduced-motion`-Regeln. Ohne `?rm=1` ändert sich nichts.

Gefundene und behobene Fehler beim Messen: Hero-Container 402 px breit bei 390 (nowrap-Unterstreichung), Formular über den rechten Rand (Einwilligungs-Label), Notfall-Links 43 px hoch.

## Screenshots (`screenshots/mobile/`)

`hero-360.png`, `hero-390.png`, `hero-430.png`, `hero-768.png`, `menu-open-390.png`, `full-390.png` (und in 10 Scheiben `slice-390-01…10.png`), `full-430.png`, `full-768.png`.

## Offen und Hinweise (keine Inhaltsentscheidung getroffen)

1. Desktop-Fehler im Einwilligungstext des Abschluss-Formulars: Der Link „Datenschutzerklärung“ steht rechts neben dem Text statt im Satz (Flex-Zeile). Auf Mobil behoben, auf Desktop absichtlich nicht (Vorgabe: Desktop unverändert). Vorschlag: Text in ein `<span>` fassen. Braucht Go.
2. Die Tablet-Ansicht quer (901 bis 1099 px) hat Telefon- und Textlinks unter 44 px. Bei Bedarf dieselben Tippflächen dort anwenden.
3. Kleine Telefone mit nur 640 px Höhe (z. B. 360 × 640): der grüne Hero-Button liegt bei 681 px und damit unter dem Falz. Ab 740 px Höhe sichtbar.
4. Die Trennpunkte „·“ zwischen den Telefonnummern (Fuß, Formular) sind auf Mobil mit Schriftgröße 0 ausgeblendet, damit sie nicht allein am Zeilenende stehen. Im Copy-Text bleiben sie.
5. Der Copy-Text `04-copy/approved-copy.md` wurde zwischenzeitlich geändert (FAQ-Antworten). Der Rebuild übernimmt das; der Seitenhöhen-Unterschied zum ersten Desktop-Screenshot kommt daher, nicht von den CSS-Änderungen.
6. Keine feste Anruf- oder Anfrage-Leiste am unteren Rand auf Mobil ergänzt (wäre eine Gestaltungsentscheidung). Der grüne Kopf-Button bleibt beim Scrollen sichtbar.
7. Menü ohne abgedunkelten Hintergrund; Menü-Beschriftung nur als `aria-label` („Menü öffnen“ / „Menü schließen“).
8. Eyebrow-Labels haben 15 px (bisherige Größe, Beschriftung); Prototyp-Hinweise `.flag` haben 14 px.
