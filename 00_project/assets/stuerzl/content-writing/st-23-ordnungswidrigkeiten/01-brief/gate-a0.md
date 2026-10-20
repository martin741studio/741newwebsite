# Gate A0 (voll): Stürzl, Ordnungswidrigkeiten (ST-23)

Datum: 2026-10-11. Seitentyp A (Geldseite, Pool-Priorität B). Modus: Überarbeitung.

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth | ja | `client-baseline.md`, `approved-copy.md`, `source-of-truth-2026-10-11.md`, Live-Profil Dr. Stürzl, 2026-10-11. |
| 2 | Live-Bestand abgerufen und gezählt | ja | Hauptseite 229 Wörter, 2×H1, 0×H2. Unterseiten Unternehmensgeldbußen 228 und Geldbußen wegen Organisationsverschulden 245 (alle mit demselben Einleitungstext). `_work/bestand-metrics.json`, page_metrics.py, 2026-10-11. |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 4 Seeds, 141 Treffer: steuerordnungswidrigkeit 9, leichtfertige steuerverkürzung 45, organisationsverschulden 86, unternehmensgeldbuße 1. Pool-Baum: 4 Treffer. `_work/autocomplete.json`, 2026-10-11. |
| 4 | Ziel-Keyword und Suchvolumen | ja | steuerordnungswidrigkeit 30 (Sitetree). Wenig Daten heißt nicht keine Nachfrage: leichtfertige steuerverkürzung 390, organisationsverschulden 480, aufsichtspflichtverletzung 320, steuerverkürzung 320, leichtfertige steuerverkürzung strafe 50, verbandsgeldbuße 40, anwalt ordnungswidrigkeitenrecht 30. `_work/vol.json` (25 Begriffe) und `content-pool/03-demand/volume.json`, DataForSEO, 2026-10-11, 0,09 USD. |
| 5 | SERP Top 10 für das Ziel-Keyword | ja | `_work/serp-steuerordnungswidrigkeit.json` und `serp-leichtfertige-steuerverkuerzung.json`, DataForSEO, 2026-10-11, je 0,0035 USD. Die SERP ist gemischt: Gesetzestext, Lexika, Steuerberater, Kanzlei-Ratgeber. |
| 6 | Echte PAA-Fragen | ja | 8 Fragen aus beiden SERPs. 3 beantwortet (leichtfertige Steuerverkürzung, Beispiele, Unterschied zur Hinterziehung), 5 verworfen mit Code (3 Duplikat, 2 nicht rechtssicher). Liste in brief.json. |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 15 von 15 gelesen. Referenzmenge: 12 Kanzlei-Seiten zu Steuer-OWi und Unternehmensgeldbuße. `_work/bench-metrics.json`, 2026-10-11. |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Themenseite. |

## Messreihe Wettbewerber (Referenzmenge)

| Wörter | Seite |
| --- | --- |
| 3295 | https://gloeckle.law/leichtfertige-steuerverkuerzung/ |
| 2314 | https://www.dr-buchert.de/rechtslexikon/ordnungswidrigkeiten/ |
| 2049 | https://www.kanzleimauss.de/leichtertige-steuerverkuerzung/ |
| 1748 | https://www.anwalt-strafrecht-steuerstreit-berlin.de/leichtfertige-steuerverkuerzung/ |
| 1183 | https://rechtsanwaelte-gsp.de/rechtsberatung/steuerstrafrecht/steuerordnungswidrigkeiten/ |
| 1129 | https://www.dr-buchert.de/rechtslexikon/unternehmenssanktionierung-%c2%a7-30-ivm-%c2%a7-130-owig/ |
| 1037 | https://spies-rechtsanwaelte.com/rechtsgebiete/anwalt-ordnungswidrigkeitsrecht-frankfurt/ |
| 998 | https://steuerdelikt.de/steuerstrafrecht/steuerowi/leichtfertige-steuerverkuerzung-378-ao |
| 974 | https://kanzlei-wb.com/steuerverkuerzung/ |
| 875 | https://www.fachanwalt-steuerrecht-strafrecht.de/2024/12/06/leichtfertige-steuerverkuerzung-was-sie-wissen-sollten/ |
| 872 | https://www.kanzlei-steinwachs.de/glossar/steuerrecht/leichtfertige-steuerverkuerzung/ |
| 425 | https://hp-w.de/steuerhinterziehung-und-leichtfertige-steuerverkuerzung-auch-ohne-vorsatz-koennen-bussgelder-faellig-werden/ |

Messwerte: 12, Median 1083.0, 70 % = 758

Nicht in der Referenzmenge: steuerdelikt.de Straftaten-Übersicht 506, kineke-gottschalk.de 987 (Steuerstrafrecht allgemein), steuerstreit-berlin.de Steuerhinterziehung 1294.

## Wortzahl-Urteil (vorab, Ziel)

Bestand 229 Wörter. Wettbewerber-Median 1083 (12 Seiten). Untergrenze 758. Zielkorridor 900 bis 1600 Wörter. Die Bestandsseite sagt, auch "unbeabsichtigte Fehler" könnten als Ordnungswidrigkeit geahndet werden. Das Gesetz verlangt Leichtfertigkeit (§ 378 AO). Die Seite folgt dem Gesetz.

## Konflikte im Bestand und bei Kundentexten

1. Bestand "unbeabsichtigte Fehler" gegen § 378 AO ("leichtfertig"): Seite folgt dem Gesetz (OPEN-FLAGS A5).
2. Bestand "Effektive Compliance-Maßnahmen ... schützen die Leitungspersonen": als "können helfen" abgeschwächt (BRAO).
3. Bestand nutzt "bestmöglich" und "essenziell": nicht übernommen.
4. Kostenmodell: neuer Kundentext gegen freigegebene Startseite ("RVG").

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Kein Blocker.
