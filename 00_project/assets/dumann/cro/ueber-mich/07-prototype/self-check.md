# Self-Check: Prototyp Über-mich-Seite (Desktop 1440 px)

Stand 2026-10-11. Prototyp: `07-prototype/index.html` (eine Datei, Assets in `assets/`, Schema in `person-schema.json`). Bewertung nach `scorecard.md` (Behandlerinnen-Seite, 21 Items), Ist-Zustand vorher: 11 von 42 (`03-diagnosis/diagnosis.md`).

## Scorecard

| # | Item | Prio | Score | Beleg |
| --- | --- | --- | --- | --- |
| 1 | Hero in 5 s: wer, was, wo, nächster Schritt | A | 2 | Name, Rolle, Stadt in der H1, CTA und Telefon im ersten Bildschirm |
| 2 | Headline Rolle plus Stadt | A | 2 | „Ich bin Daniela Dumann, Heilpraktikerin in Berlin-Charlottenburg seit 2002" |
| 4 | Primärer CTA im ersten Bildschirm | A | 2 | Button endet bei y=534 von 813 |
| 5 | CTA-Text nennt Schritt und Nutzen | A | 1 | „Termin buchen" nennt den Schritt, keinen Nutzen. So in der Copy gesetzt, gleiche offene Entscheidung wie auf der Startseite |
| 6 | Rückversicherung unter dem CTA | A | 2 | „Erstgespräch: 60 Minuten, 220 €" und Bewertungszeile |
| 7 | Zwei Beweisformen above the fold | A | 2 | Bewertung 5,0 und „seit 2002" im Hero, Trust-Leiste direkt darunter |
| 8 | Gesicht und Qualifikation im ersten Bildschirm | A | 2 | großes Portrait, „Heilpraktikerin seit 2002" in H1 |
| 10 | Eine CTA-Farbe, Blur-Test | A | 2 | nur Oliv gefüllt |
| 11 | CTA mindestens alle 2 Sektionen | A | 2 | Hero, Ansatz, Weg, Bewertungen (nach der visuellen Prüfung ergänzt), Warum, Standort, Abschluss |
| 12 | Bewertungen offen mit Vorname und Logo | B | 2 | 3 offene Karten |
| 13 | Beweis-Überschrift mit Zahl | B | 2 | „5,0 Sterne bei 9 Google Bewertungen" |
| 14 | Beweisblöcke verteilt | B | 2 | Hero, Trust-Leiste, Weg, Lehre, Bewertungen, Abschluss |
| 17 | FAQ mit echten Einwänden | B | 2 | 4 Fragen zur Person, Preis im Erstgespräch-Antwort |
| 18 | Standort: Karte, Adresse, ÖPNV, Zeiten | B | 1 | Parken fehlt `[FEHLT]` |
| 19 | Abschluss = Mini-Hero | B | 2 | Überschrift, drei Punkte, Buchen und Telefon |
| 20 | Überschriften mit Aussage | C | 1 | 4 von 7 tragen eine Aussage, „Meine Schwerpunkte", „Häufige Fragen", „So finden Sie zu mir" sind Labels |
| 21 | Typografie | C | 2 | Body 16 bis 18 px, alle Texte mindestens 16 px |
| 22 | HWG | A | 2 | Hinweisbox, keine Wirkaussagen, Motivation umformuliert (Freigabe offen) |
| A1 | Name, Rolle, Stadt in Title, H1, Meta | A | 2 | Title 57 Z., Meta 155 Z., H1 mit allen drei |
| A2 | Person-Schema | A | 2 | gültiges JSON-LD im Kopf: 6 Qualifikationen, worksFor, workLocation, knowsAbout, memberOf. `sameAs` bewusst leer, bis das Citation-Audit geprüfte Profile liefert |
| A3 | Werdegang belegt und lesbar | B | 2 | Zeitleiste mit 10 Stationen plus Qualifikationen-Karte mit Lehrernamen |

Summe: 39 von 42. Alle Priority-A-Items mit 2, außer Item 5 mit 1 (begründet, Entscheidung offen).

## „Done"-Bedingungen (Workflow Abschnitt 0)

1. Scorecard 2 oder Begründung: ja.
2. Primärer CTA im ersten Bildschirm bei 1440 px: ja.
3. CTA alle 2 Sektionen: ja.
4. Erste Sektionen beantworten wer, was, wo, Vertrauen: ja (Hero und Trust-Leiste). Erster Termin in FAQ und Hero-Zeile, Standort in Sektion 11.
5. Jeder Anspruch zurückführbar: ja (alle Texte aus `dataset.md`, 98 von 98 Prompt-Texten und 223 Seitentexte gegen die Copy geprüft, Abweichungen nur Adresszeile, Fußzeile, E-Mail).
6. Keine Heilversprechen: ja.
7. Martin-Freigaben: Sonderregel, ohne Stopp durchgelaufen. Freigabe der Seite durch Martin und Kundin steht aus.

## Abweichungen vom Mockup (bewusst)

- Logo: echte Wortmarke, das Mockup hat „Heilpraktikerin" und ein Icon ergänzt (erfunden, nicht übernommen).
- FAQ als Akkordeon mit einer offenen Antwort.
- Karte live (OpenStreetMap), Pin als Overlay.
- Zusätzlicher oliver Button „Termin buchen" im Bewertungsabschnitt (CTA-Regel).
- Trust-Icons als SVG statt gemalt.

## Bewegung

Nach `00_project/cro-homepage-motion-spec.md`: ein Highlight je Abschnitt, Breathing-CTA nur Hero und Abschluss, Reveal einmal, nichts re-animiert beim Zurückscrollen, Reduced-Motion per CSS.

## Offene Punkte (für Handoff)

Siehe `08-handoff/handoff.md`, Abschnitt „[FEHLT] vor dem Livegang".
