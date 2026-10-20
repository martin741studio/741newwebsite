# Gate A0 (voll): Stürzl, Standort Frankfurt (ST-41)

Datum: 2026-10-11. Seitentyp A (Ortsseite, Geldseite mit lokaler Absicht). Neue Seite, kein Bestand.

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste, NAP) | ja | `cro/04-copy/approved-copy.md`, `client-baseline.md`, `assets/stuerzl/nap.json` und `source-of-truth-2026-10-11.md` (Frankfurt Untermainkai 26 bestätigt), 2026-10-11 |
| 2 | Live-Bestand abgerufen und gezählt | ja | Es gibt keine Frankfurt-Seite. Pool: `live_status: weak`, `live_url` = Kontaktseite (255 Wörter, nur Teilbestand, 2026-10-11). Bestand der eigenen Ortsseite: 0 Wörter. |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 15 Treffer mit Frankfurt-Bezug (Pool CP-LOC-004 `autocomplete_hits: 15`), unter anderem 'steuerfahndung frankfurt', 'steuerfahndung frankfurt am main', 'steuerhinterziehung frankfurt', 'wirtschaftsstrafrecht frankfurt', 'anwalt steuerstrafrecht frankfurt'. `03-demand/autocomplete.json`, 2026-10-11 |
| 4 | Ziel-Keyword und Suchvolumen | ja | 'anwalt steuerstrafrecht frankfurt': kein Datensatz (heißt wenig Daten, nicht keine Nachfrage). Cluster: 'steuerfahndung hessen' 140, 'steuerfahndung frankfurt' 50, 'anwalt steuerhinterziehung frankfurt' 10, 'wirtschaftsstrafrecht frankfurt' 70 (nicht Ziel dieser Seite). Summe der Ortsbegriffe 200 (Pool). DataForSEO google_ads/search_volume/live, 2026-10-11 |
| 5 | SERP Top 10 für das Ziel-Keyword | ja | `02-competitors/serp-13.json` ('anwalt steuerstrafrecht frankfurt', Frankfurt), 2026-10-11. Verzeichnisse (gelbeseiten, focus, anwalt.org, anwaltssuche) aus dem Wettbewerberset genommen. |
| 6 | Echte PAA-Fragen | ja | serp-13 und serp-16: 'Was kostet eine Beratung beim Fachanwalt für Steuerrecht?', 'Welchen Anwalt bei Finanzamt?' (beantwortet); 'Wie finde ich heraus, ob ein Anwalt gut ist?', 'Wo finde ich kostenlose Rechtsberatung in Frankfurt am Main?', 'Wer kann mir bei Kryptobetrug helfen?', 'Wo bekommst du eine kostenlose Rechtsberatung?' (verworfen mit Code in `brief.json`) |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 13 von 14 Seiten gelesen, Median **656** Wörter, 70-%-Untergrenze **459**. Liste unten. `_work/bench-metrics.json`, 2026-10-11 (page_metrics.py) |
| 8 | Lokaler Fakt (Stadt ist Teil der Positionierung) | ja | Die hessische Finanzverwaltung nennt sechs Finanzämter mit Steuerfahndungsstellen und Bußgeld- und Strafsachenstellen (Darmstadt, Frankfurt am Main I, Kassel, Offenbach am Main II, Wetzlar, Wiesbaden): `_work/hessen-steuerfahndung-quelle.txt`, finanzamt.hessen.de, gelesen 2026-10-11. Dazu § 386, § 388, § 399 AO (gelesen 2026-10-11). |

## Messreihe Wettbewerber (Seiten zu 'anwalt steuerstrafrecht frankfurt', SERP 13)

| Wörter | Seite |
| --- | --- |
| 3181 | https://rechtsanwaltskanzlei-frankfurt.jurebus.de/rechtsgebiete/steuerrecht/ |
| 2205 | https://www.rgra.de/anwalt-strafrecht-frankfurt/ |
| 2171 | https://www.mtrlegal.com/offices/frankfurt/steuerstrafrecht/ |
| 2065 | https://spies-rechtsanwaelte.com/rechtsanwaelte/ |
| 1462 | https://strafrechtanwalt.org/ |
| 1231 | https://ht-strafrecht.de/standorte/hessen/frankfurt-am-main/ |
| 656 | https://grub-brugger.de/wirtschaftsstrafrecht.html |
| 630 | https://doerr-ffm.de/ |
| 606 | https://rae-sus.de/kanzlei/ |
| 493 | https://www.ra-steinbacher.de/ |
| 323 | https://kanzlei-velke.de/ |
| 228 | https://www.richter.law/ |
| 67 | https://www.schmidt-taxlaw.de/ |
| unlesbar | https://www.lsv-legal.com/de/Anwalt-Frankfurt-Steuerstrafrecht (SSL-Zertifikat abgelaufen, 3 Versuche) |

Nicht gemessen (Verzeichnisse und Portale, kein Kanzleitext): gelbeseiten.de, focus.de, anwalt.org, anwaltssuche.de, unternehmen.focus.de.

## Wortzahl-Urteil (Ziel)

0 Wörter eigene Seite (neu), Bestand 0, Median 656, Untergrenze 459. Zielkorridor 650 bis 1.300 Wörter. Die Streuung der Wettbewerber ist groß (67 bis 3.181). Die Tiefe kommt aus belegten lokalen Fakten (AO, hessische Finanzverwaltung), nicht aus Füllsätzen.

## Konflikte und Lücken

1. Frankfurter Anschrift: bestätigt (Source of Truth Tab 00, `nap.json`, Hinweis Hauptagent 2026-10-11): Untermainkai 26, 60329 Frankfurt am Main, Post und Empfang Wilhelm-Leuschner-Straße 23, Tiefgarage Wilhelm-Leuschner-Straße 27 bis 29 (Plätze 148 und 146). Alte Anschrift Wiesenhüttenstraße 17 nie nennen. Die Umstellung von Google-Profil und Live-Website wartet auf Martins Go.
2. Zeiten: Telefon Montag bis Freitag durchgehend 9:30 bis 14:30 Uhr (Live, Source of Truth). Google nennt 9:00 bis 18:00 Uhr. Keine Zeit im Schema.
3. ÖPNV-Anfahrt zur neuen Anschrift ist nicht belegt (die Live-Anfahrt galt für die alte Anschrift). Sie steht nicht im Text.
4. Welche Leistungen das Frankfurter Büro anbietet und welche Fachgebiete einen Frankfurter Bezug haben: offen (CP-LOC-004 `needs_client`). Platzhalter, die Seite zeigt bis dahin alle sechs Bereiche der Kanzlei.
5. Personen im Frankfurter Büro: nur Dr. Stürzl (Live-Kontaktseite) und Thorben Hoppe (Profil: Frankfurt und München) sind belegt. Platzhalter für weitere Personen.
6. Bewertungen (Google Frankfurt 5,0 mit 14, anwalt.de 5,0 mit 79) nicht freigegeben: Beweisabschnitt entfällt.
7. Kostenmodell: 'Erstberatung gegen Pauschale', keine Beträge. Die freigegebene Startseite sagt noch 'RVG' (siehe Flags).

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden, der lokale Fakt ist belegt. Keine Blocker. Die Seite darf als Entwurf mit Platzhaltern entstehen.
