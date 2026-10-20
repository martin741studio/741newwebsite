# Visuelle Prüfung v2 (Chrome, von oben nach unten)

Stand 2026-10-11. Geprüft in Claude in Chrome (extern), Fenster 1430 px, im zweiten Durchgang 1440×757, Seite über lokalen Server. Checkliste: `00_project/cro-homepage-visual-check.md`. Zwei Durchgänge nach unten, einer nach oben, danach Interaktionen.

**Ergebnis: 61 Punkte geprüft, 9 behoben, 0 offen. Zweiter Durchgang nach Martins Hinweis, dass die beiden offenen Punkte behoben werden müssen.**

## Gemessene Punkte

| # | Prüfung | Ergebnis |
| --- | --- | --- |
| M1 | Fensterbreite | 1430 px (Chrome-Grenze), kein Layout-Unterschied zu 1440 |
| M2 | Kein horizontales Scrollen | ok (1415 von 1430) |
| M3 | Konsole und Netzwerk | ok, keine Fehler |
| M4 | Bilder geladen, Auflösung | ok, kleinstes Verhältnis 2,26 (Bild-Pixel zu Anzeige-Pixel), nach Scrollen alle geladen (der About-Portrait ist lazy) |
| M4b | Verzerrung | behoben (Punkt 9), danach 0 verzerrte Bilder |
| M5 | Schriften | ok, Playfair Display und Poppins geladen |
| M6 | Links | ok: Buchungs-URL 6×, öffnet in neuem Tab; Telefon korrekt; alle Anker existieren; 8 Platzhalter `#` (6 Leistungslinks, Impressum, Datenschutz) wie gelistet |
| M7 | Reveals | ok, 0 versteckt nach dem Scrollen, 0 versteckt nach dem Zurückscrollen |
| M8 | CTA im ersten Bildschirm | ok, Unterkante y=538 |
| M9 | Textgröße | behoben (siehe unten), übrig nur Quellenzeilen mit 14 px und das `[FEHLT]`-Schild |
| M10 | Atmende Animation | ok, genau 2 (Hero, Abschluss) |
| M11 | Text gegen freigegebene Copy | ok. Abweichungen: Zeile „Erstgespräch: 60 Minuten, 220 €" im Hero (bekannt, Entscheidung offen), Abschnittsüberschrift „Häufige Fragen" (Label, in der Copy nur „FAQ"), Platzhalter-FAQ-Antwort (bekannt), Fußzeile mit Adresse und E-Mail (E-Mail geprüft: steht auf ihrer Website und im Datensatz) |

## Behoben

1. Textgröße: Menü, Hero-Zeilen, Themen-Texte, Bewertungsnamen und Fußzeile von 14,5 bis 15 px auf 16 px.
2. Karte Aderlass: Kopf war oben abgeschnitten. Neuer Ausschnitt mit vollem Haaransatz.
3. Über-mich-Portrait: zu groß und zu nah. Spalte von 480 auf 400 px.
4. Schritt 4: Überschrift brach in zwei Zeilen und verschob den Text. Seitenbreite von 1240 auf 1320 px, alle vier Texte stehen auf gleicher Höhe (gemessen 88 px).
5. Themenkarten: Text zu klein. Größe 16 px, Karten gleich hoch (295 px).
6. Foto Homöopathie: das echte Foto war kalt blau. Neu erzeugt in warmen Tönen wie die anderen Karten (`06-gpt-assets/images/04d-homoeopathie.png`, in Drive). Auf der Shoot-Liste.
7. Silbentrennung in den Themenkarten: keine automatische Trennung mehr, nur eine feste Trennstelle in „Wechseljahres-beschwerden". Kein Text läuft über die Karte.
8. Haarränder der beiden Portraits: heller Rand vom beigen Originalhintergrund. Randpixel entmischt, Haarsträhnen wirken natürlich auf Violett und auf der Hero-Fläche.
9. Über-mich-Portrait war verzerrt (schmal und hoch gezogen, weil die Bildhöhe fest gesetzt war). Jetzt `height:auto`, gemessen: kein Bild weicht mehr als 2 Prozent vom Seitenverhältnis ab. Neuer Messpunkt M4b in der Checkliste.

## Offen

Keine technischen oder visuellen Punkte. Offen bleiben nur Daten vom Kunden und Entscheidungen: Stornobedingungen, Parken, deutsche Bewertungs-Originale, Entscheidung zur Sub-Headline, zum CTA-Text und zur Hero-Zeile „Erstgespräch: 60 Minuten, 220 €".

## Abschnitt für Abschnitt

| Abschnitt | Ergebnis |
| --- | --- |
| Kopfzeile | ok: Logo scharf, sieben Punkte in einer Zeile, Hover-Unterstrich, alle Anker landen unter der Kopfzeile (Abstand 76 px, Überschrift sichtbar) |
| 1 Hero | ok: H1 vier Zeilen, CTA-Paar gleich hoch, Portrait scharf, linke Kante läuft weich aus, kein Heiligenschein, Text auf dem Hintergrund gut lesbar |
| 2 Beweis-Leiste | ok: eine Zeile, zentriert, Sterne füllen sich, ein echtes Zitat mit Vorname |
| 3 Themen | ok nach Behebung: Icons ohne Kasten, gleiche Größe, Karten gleich hoch |
| 4 Leistungen | ok nach Behebung: Bilder zeigen das Motiv, einheitlicher warmer Ton, Zoom beim Hover ohne Überlauf, Kartenhöhen gleich |
| 5 Schritte | ok nach Behebung: Linie zeichnet einmal, Badges füllen sich mit, Hinweiszeile lesbar |
| 6 Über mich | ok nach Behebung: Portrait unverzerrt, Haarrand sauber, sitzt sauber, Dekor berührt den Text nicht, kein sichtbares Rechteck um die Zeichnung, Unterstreichung läuft einmal, Kontrast gut |
| 7 Bewertungen | ok: drei offene Karten, gleich hoch, Stern, Zitat, Vorname, Google-Logo, Link zum Profil |
| 8 FAQ | ok: jede Frage öffnet und schließt, immer nur eine offen, Pfeil dreht, `[FEHLT]`-Schild bei der Absage-Antwort sichtbar |
| 9 Standort | ok: Karte lädt, Pin steht an der Nithackstraße, Symbole passen, Adresse stimmt mit dem NAP |
| 10 Abschluss | ok: Überschrift, drei Punkte, CTA-Paar, Linienzeichnungen berühren den Text nicht |
| Fußzeile | ok: Adresse, Telefon, E-Mail korrekt, Impressum und Datenschutz als Platzhalter gelistet |
| Hover | ok: CTA hebt sich und wird heller, Menüpunkt bekommt Unterstrich |
| Vergleich mit Mockup | Abweichungen wie in `self-check.md` (Leistungen 3×2, Textlink statt Button, FAQ als Akkordeon) |

Screenshots des Endstands: `screenshots/desktop-1440-first-viewport.png`, `screenshots/desktop-1440-full.png`.
