# Gate A0 (voll): Stürzl, Standort München (ST-42)

Datum: 2026-10-11. Seitentyp A (Ortsseite, Geldseite mit lokaler Absicht). Neue Seite, kein Bestand.

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste, NAP) | ja | `cro/04-copy/approved-copy.md`, `client-baseline.md`, `assets/stuerzl/nap.json`, `source-of-truth-2026-10-11.md` (München Oberanger 32, Telefon, Zugang), 2026-10-11 |
| 2 | Live-Bestand abgerufen und gezählt | ja | Es gibt keine München-Seite. Source of Truth Tab 02: 'München hat noch KEINE eigene Standortseite'. Pool: `live_status: weak`, nur die Kontaktseite trägt München (255 Wörter gesamt). Bestand der eigenen Ortsseite: 0 Wörter. |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 16 Treffer mit München-Bezug (Pool CP-LOC-005 `autocomplete_hits: 16`), unter anderem 'selbstanzeige münchen', 'steuerfahndung münchen', 'wirtschaftsstrafrecht münchen', 'steuerfahndung münchen adresse', 'durchsuchung steuerfahndung münchen'. `03-demand/autocomplete.json`, 2026-10-11 |
| 4 | Ziel-Keyword und Suchvolumen | ja | 'anwalt steuerstrafrecht münchen' 70, 'anwalt wirtschaftsstrafrecht münchen' 40, weitere München-Begriffe ohne Datensatz (wenig Daten, nicht keine Nachfrage). DataForSEO google_ads/search_volume/live, de, 2276, 2026-10-11 |
| 5 | SERP Top 10 für das Ziel-Keyword | ja | `02-competitors/serp-6.json` ('anwalt steuerstrafrecht münchen', München), 2026-10-11. Verzeichnisse (anwalt.de, anwaltssuche.de) aus dem Wettbewerberset genommen. |
| 6 | Echte PAA-Fragen | ja | serp-6: 'Was kostet eine einfache Rechtsberatung?' (beantwortet); 'Was ist eine juristische Beratung?', 'Was macht ein Fachanwalt für Handels- und Gesellschaftsrecht?', 'Wurde ein Münchener Strafverteidiger angeklagt?' (verworfen mit Code in `brief.json`) |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 11 von 11 Kanzleiseiten gelesen, Median **625** Wörter, 70-%-Untergrenze **437**. Liste unten. `_work/bench-metrics.json`, 2026-10-11 (page_metrics.py) |
| 8 | Lokaler Fakt (Stadt ist Teil der Positionierung) | ja | Das Bayerische Landesamt für Steuern nennt neun Steuerfahndungsstellen, eine beim Finanzamt München; das Finanzamt München führt Steuerfahndung und Bußgeld- und Strafsachenstelle (`_work/bayern-steuerfahndung-quelle.txt`, gelesen 2026-10-11). Dazu § 387, § 388, § 370 AO (gelesen 2026-10-11). Zugang Marienplatz und Sendlinger Tor, Tiefgaragen: Live-Kontaktseite, Kanzlei-Angabe. |

## Messreihe Wettbewerber (SERP 6)

| Wörter | Seite |
| --- | --- |
| 2453 | https://www.kanzlei-kunkel.de/ |
| 1975 | https://www.die-anwalts-kanzlei.de/standort/muenchen/ |
| 1677 | https://alphalex.de/rechtsgebiete/strafrecht/steuerstrafrecht/ |
| 826 | https://muenchen-strafrecht.de/ |
| 639 | https://www.michalkerosskopf.de/ |
| 625 | https://www.bietmann.eu/standorte/rechtsanwalt-muenchen |
| 507 | https://www.eckstein-kollegen.de/ |
| 421 | https://dms-strafrecht.de/steuerstrafrecht/ |
| 396 | https://schirach.law/ |
| 381 | https://birkenmaier-obser.de/de/schwerpunkte/steuerstrafrecht |
| 178 | https://www.leisnernet.com/leistungen/steuerstrafrecht |

Nicht gemessen (Verzeichnisse): anwalt.de, anwaltssuche.de.

## Wortzahl-Urteil (Ziel)

0 Wörter eigene Seite (neu), Bestand 0, Median 625, Untergrenze 437. Zielkorridor 600 bis 1.300 Wörter. München-Wettbewerber sind meist kurz. Die Tiefe kommt aus belegten lokalen Fakten (AO, bayerische Finanzverwaltung) und aus den belegten Münchner Personen.

## Konflikte und Lücken

1. Zeiten: Telefon Montag bis Freitag durchgehend 9:30 bis 14:30 Uhr (Live, Source of Truth). Das Google-Profil München nennt Dienstag bis Freitag 9:00 bis 18:00 Uhr, montags geschlossen. Die Seite folgt Live und Source of Truth. Keine Zeit im Schema.
2. Eintrittsdaten: Das Live-Profil von Lea Wimmer nennt '7/2025 Rechtsanwältin und Salary Partnerin bei STÜRZL Steuerstrafrecht (München)'. Dr. Stürzls Lebenslauf nennt '03/2026 Eröffnung einer Zweigstelle in München', Source of Truth 'München seit Anfang 2026'. Die Seite nennt keine Eröffnungs- oder Eintrittsdaten.
3. Titel von Lea Wimmer (Fachanwältin für Steuerrecht seit 2017) und Dr. Glogger (Zertifizierter Compliance Officer) stammen von den Live-Profilen, nicht von der Kanzlei bestätigt.
4. Welche Leistungen das Münchner Büro anbietet: offen (CP-LOC-005 `needs_client`). Platzhalter.
5. Die Live-Profile nennen Auszeichnungen (Handelsblatt, WirtschaftsWoche, 'Beste Anwältin'). Nicht übernommen, nicht freigegeben, BRAO-Risiko.
6. Das Münchner Google-Profil hat 1 Bewertung und 0 Fotos: Beweisabschnitt entfällt, Bild nur mit echtem Foto.
7. Kostenmodell: 'Erstberatung gegen Pauschale', keine Beträge.

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden, der lokale Fakt ist belegt. Keine Blocker. Die Seite darf als Entwurf mit Platzhaltern entstehen.
