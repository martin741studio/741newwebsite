# Self-Check — Prototyp Naturheilpraxis Daniela Dumann

Stand 2026-10-11. Prototyp: `07-prototype/index.html` (eine Datei, Assets in `assets/`). Screenshots in `screenshots/`. Bewertung nach `scorecard.md` (741 CRO-Raster), Ist-Zustand vorher: 7 von 44.

Geprüft in: Headless Chrome mit echtem 390-px- und 1440-px-Viewport (iframe, weil Headless unter ca. 500 px Fenster nicht erlaubt), Live-Scroll-Check in Martins Chrome (Claude in Chrome): Reveals, Sticky-Leiste, FAQ, Karte.

## Scorecard

| # | Item | Prio | Score | Beleg |
| --- | --- | --- | --- | --- |
| 1 | Hero in 5 s: was, für wen, nächster Schritt | A | 2 | Screenshot `mobile-390-first-viewport.png`: H1, Buchen-Button, Telefon, Erstgespräch-Zeile, Bewertung |
| 2 | Headline Ergebnis + Stadt | A | 2 | „… Wohlbefinden … Berlin-Charlottenburg seit 2002" |
| 3 | Sub-Headline: Situation zuerst, dann 3–4 Hilfen | A | 1 | Lead nennt die Themen (Verdauung, Erschöpfung, Schilddrüse, Hormone) und die Methoden, aber nicht „Situation zuerst". Bewusst: HWG-Modus, Beschwerde-Formulierung im Hero würde Heil-/Angstsprache nahekommen. Die Situationen stehen in Sektion 3. **Entscheidung Martin** |
| 4 | Primärer CTA auf 390 px ohne Scrollen | A | 2 | Button bei y≈510–560 von 844 |
| 5 | CTA-Text nennt Schritt + Nutzen | A | 1 | „Termin buchen" nennt den Schritt, keinen Nutzen. So in `approved-copy.md` freigegeben. **Entscheidung Martin** |
| 6 | Rückversicherung direkt unter dem CTA | A | 2 | Zeile „Erstgespräch: 60 Minuten, 220 €" unter den Buttons (Fakt aus dataset 1.9, in der Copy schon in Sektion 5 und 10), darunter Bewertung. Neu in dieser Fassung, nicht im freigegebenen Hero-Text |
| 7 | Zwei Beweisformen above the fold | A | 2 | Google-Bewertung 5,0 ★ + „seit 2002" in der H1 |
| 8 | Gesicht + Qualifikation Hero/Sektion 2 | A | 2 | Echtes Portrait im Hero, „Heilpraktikerin seit 2002" in H1 |
| 9 | „Erster Termin": Schritte, Dauer, Preis | A | 2 | Sektion 5: 4 Schritte, 60 Min, 220 €, 150 € |
| 10 | Eine CTA-Farbe, Blur-Test | A | 2 | Nur Oliv gefüllt; Telefon/Zweit-Buttons nur Kontur |
| 11 | CTA alle 2 Sektionen + Sticky mobil | A | 2 | CTA in Header, 1, 3, 5, 6, 9, 10 + Sticky-Leiste; Live-Check: Leiste aus am Anfang, an in der Mitte, aus im Closer |
| 12 | Bewertungen offen, Vorname, Google-Logo | B | 2 | 3 offene Karten, kein Karussell |
| 13 | Beweis-Überschrift | B | 2 | „5,0 Sterne bei 9 Google Bewertungen" (Zahl statt „Bewertungen") |
| 14 | 3–4 Beweisblöcke verteilt | B | 2 | Hero, Beweis-Leiste, Über mich (Qualifikationen), Bewertungen, Closer |
| 15 | Situationen HWG-sauber | B | 2 | „Begleitung bei …", keine Diagnosen, keine Heilversprechen |
| 16 | Leistungen als Karten mit Link | B | 2 | 6 Karten; Links sind `#`-Platzhalter bis zum Rebuild |
| 17 | FAQ mit echten Einwänden | B | 1 | Absage-Antwort ist Platzhalter und im Prototyp sichtbar markiert `[FEHLT]` |
| 18 | Standort: Karte, Adresse, Parken, ÖPNV, Zeiten | B | 1 | Karte, Adresse, ÖPNV, „nach Vereinbarung" da; **Parken fehlt** `[FEHLT]` |
| 19 | Abschluss = Mini-Hero | B | 2 | Headline, 3 Punkte, Buchen + Telefon |
| 20 | Überschriften mit Aussage | C | 1 | „So arbeite ich mit Ihnen", „Häufige Fragen", „So finden Sie zu mir" sind Labels (so freigegeben) |
| 21 | Typografie, Tap-Ziele | C | 2 | Body 18 px mobil / 17 px Desktop, Buttons 52 px, FAQ-Zeilen 56 px, Telefon-Button 48 px |
| 22 | HWG | A | 2 | Nur freigegebene Copy plus Erstgespräch-Zeile; keine Heilversprechen, keine Krankheitsliste |

Summe: 38 von 44. Priority A: 10 von 12 mit 2. Zwei A-Items (3, 5) stehen auf 1 mit schriftlicher Begründung oben; sie sind die Entscheidungen für Checkpoint 2.

## „Done"-Bedingungen (Workflow Abschnitt 0)

1. Scorecard 2 oder Begründung: ja, siehe Tabelle.
2. Primärer CTA auf 390 px ohne Scrollen sichtbar: ja (Kanal Buchungsformular, nicht WhatsApp).
3. CTA alle 2 Sektionen + Sticky mobil: ja.
4. Erste Sektionen beantworten wer/was/erster Termin/wo/Vertrauen: wer + was + Vertrauen im Hero und Beweis-Leiste, erster Termin in Sektion 5, wo in Sektion 9. Nicht in den ersten 3 Sektionen: erster Termin und Standort (liegen weiter unten, wie im P0-Blueprint).
5. Jeder Anspruch zurückführbar: ja; zwei Stellen mit `[FEHLT]` (Absage, Parken), Bewertungs-Zitate sind Google-Übersetzung `[FEHLT: deutsche Originale]`.
6. Keine Heilversprechen: ja.
7. Martin-Freigaben: Copy ja, Prototyp offen (Checkpoint 2).

## Bewegung (motion spec)

Geprüft gegen `00_project/cro-homepage-motion-spec.md`:
- 1 Highlight je Sektion vorhanden: Hero-CTA atmet, Sterne füllen (Beweis-Leiste, Bewertungen), Icons skalieren (Themen), Bild-Zoom und Pfeil (Leistungen), Schritt-Linie zeichnet (Schritte), Credential-Unterstreichung (Über mich), offene FAQ-Frage färbt sich, Karten-Pin fällt, Closer-CTA atmet.
- Dauerbewegung nur an Hero- und Closer-CTA.
- Nicht vorhanden: Parallax, Karussell, Dauer-Deko, Bounce, Re-Animation beim Zurückscrollen.
- Reduced motion per CSS umgesetzt (Medienabfrage `prefers-reduced-motion`), im Live-Test nur per Code geprüft, nicht per Systemeinstellung umgeschaltet.
- Live-Check: 32 von 32 Reveal-Elemente werden einmalig beim Scrollen sichtbar.

## Offene Punkte (für Handoff)

- `[FEHLT]` Absage-/Stornobedingungen (Platzhaltertext im FAQ sichtbar markiert).
- `[FEHLT]` Parken am Standort.
- `[FEHLT]` Deutsche Originaltexte der Bewertungen.
- Bilder: Hero und Über-mich sind echte Fotos. Die 6 Leistungs-Bilder sind verkleinerte GPT-Ausschnitte (weich); zwei zeigen die Behandlerin in GPT-erzeugten Szenen. Shoot-List: echte Fotos für Aderlass, Darmsanierung, Ernährung, Homöopathie, Oligoscan, Massage.
- Karte lädt OpenStreetMap beim Seitenaufruf. Für den Live-Gang Einwilligung/Zwei-Klick-Lösung nötig (DSGVO).
- Impressum/Datenschutz-Links sind Platzhalter; Header hat auf Mobil nur Telefon-Button statt Menü (bewusst, Sticky-CTA übernimmt).
- Logo: echte Wortmarken-Datei. Das Logo-Icon (Hildegard-Zeichnung) ist noch nicht eingebaut.
