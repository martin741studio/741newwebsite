# Visuelle Prüfung: Über-mich-Seite (Chrome, von oben nach unten)

Stand 2026-10-11. Geprüft in Claude in Chrome (extern), Fenster 1440×813, Seite über lokalen Server. Checkliste: `00_project/cro-homepage-visual-check.md` (inklusive M4b). Zwei Durchläufe nach unten (Rohstand und nach Behebung), ein Durchlauf nach oben, dazu Interaktionen.

**Ergebnis: 63 Punkte geprüft, 9 behoben, 0 offen.**

## Gemessene Punkte

| # | Prüfung | Ergebnis |
| --- | --- | --- |
| M1 | Fensterbreite | 1440 px |
| M2 | Kein horizontales Scrollen | ok (1425 von 1440) |
| M3 | Konsole und Netzwerk | ok, keine Fehler |
| M4 | Bilder geladen, Auflösung | ok, kein Bild kleiner als seine Anzeige. Kleinster Faktor 1,24 beim Kräutergarten-Foto (ChatGPT liefert höchstens 1536 px), Hinweis für die Shoot-Liste |
| M4b | Verzerrung | 0 verzerrte Bilder |
| M5 | Schriften | ok |
| M6 | Links | ok: Buchungs-URL 6×, neuer Tab; Telefon korrekt; alle Anker existieren; 10 Platzhalter `#` (Startseite, Ablauf im Menü, 5 Schwerpunkt-Links, Kurse und Seminare, Impressum, Datenschutz) wie gelistet |
| M7 | Reveals | 35 von 35 sichtbar nach Scrollen, 0 versteckt nach Zurückscrollen |
| M8 | CTA im ersten Bildschirm | ok, Unterkante y=534 |
| M9 | Textgröße | behoben (Jahreszahl-Pillen 15 auf 16 px), danach keine Texte unter 16 px |
| M10 | Atmende Animation | genau 2 (Hero, Abschluss) |
| M11 | Text gegen freigegebene Copy | ok, 223 Segmente, Abweichungen nur Adresszeile (Zusammenfügung), Fußzeile, E-Mail, „Datenschutz" |

## Behoben

1. Kräutergarten-Foto war nicht zugeschnitten (fest gesetzte Bildhöhe), jetzt `height:auto` mit Seitenverhältnis und Bildausschnitt auf das Gesicht.
2. Trust-Leiste: Beleg „Vizepräsidentin …" brach in 5 Zeilen. Spaltenbreiten angepasst, 4 Zeilen.
3. Zeitleiste: Jahreszahlen als Pillen wie im Mockup statt Punkte.
4. Logo Viriditas: leerer Rand zugeschnitten (Logo selbst unverändert), Anzeige 112 px, lesbar.
5. Warum-Portrait: harte linke Kante, jetzt weich auslaufend.
6. Abstand der Überschrift „So finden Sie zu mir" nach oben zu klein.
7. Akkordeon im Screenshot-Modus: nur eine Frage blieb offen (Skript-Fehler im Prüfmodus), Prüfmodus korrigiert.
8. Jahreszahl-Pillen unter 16 px.
9. CTA-Lücke von 3 Sektionen (Schwerpunkte, Lehre, Bewertungen): oliver Button im Bewertungsabschnitt ergänzt, Copy angepasst.

## Offen

Keine technischen oder visuellen Punkte. Offen bleiben Kundendaten und Entscheidungen (siehe Handoff).

## Abschnitt für Abschnitt

| Abschnitt | Ergebnis |
| --- | --- |
| Kopfzeile | ok: echte Wortmarke, „Über mich" aktiv unterstrichen, Hover, Anker landen unter der Kopfzeile (Abstand 76 px) |
| 1 Hero | ok: H1 drei Zeilen, CTA-Paar, Portrait scharf, Haarrand sauber, Hintergrund lesbar |
| 2 Trust-Leiste | ok: vier Belege mit Icons, Bewertung rechts |
| 3 Ansatz | ok: 4 Karten gleich hoch (231 px), Icons ohne Kasten, Foto mit Unterschrift |
| 4 Weg | ok: 10 Stationen, Qualifikationen-Karte mit 7 Häkchen und Mitgliedschaften |
| 5 Schwerpunkte | ok: 5 Karten gleich hoch (309 px) |
| 6 Lehre | ok: breites Foto zeigt das Gesicht, 4 Karten gleich hoch (466 px), Logo lesbar |
| 7 Bewertungen | ok: 3 offene Karten, zwei Buttons |
| 8 Warum | ok: Portrait weich, Text lesbar, Linienzeichnung berührt den Text nicht |
| 9 FAQ | ok: öffnet und schließt, immer nur eine offen |
| 10 Hinweisbox | ok |
| 11 Standort | ok: Karte, Pin an der Nithackstraße, Symbole |
| 12 Abschluss und Fuß | ok |
| Hover und Interaktionen | ok: CTA hebt sich, Menü-Anker, Buchungslink in neuem Tab, Telefonlink |

Screenshots des Endstands: `screenshots/desktop-1440-first-viewport.png`, `screenshots/desktop-1440-full.png`.
