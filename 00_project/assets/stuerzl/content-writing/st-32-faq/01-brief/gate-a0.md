# Gate A0 (leicht, FAQ-Seite): Stürzl, FAQ (ST-32)

Datum: 2026-10-11. Seitentyp FAQ (Hub, Typ B/C). Prüfung: Bestand, alle Kundentexte zum Thema, Keyword und Volumen, SERP gelesen, echte PAA, 2 Wortzahl-Messungen (Untergrenze 70 % des Medians). Quelle der Pool-Daten: `content-pool/` (Lauf 2026-10-11).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth, Stimme, Nicht-Liste | ja | `client-baseline.md`, `approved-copy.md`, `voice.md`, `nap.json`, `source-of-truth-2026-10-11.md`, 2026-10-11. |
| 2 | Live-Bestand abgerufen und gezählt | ja | `/index.php/faq`: 2555 Wörter, 6×H1, 0×H2. Fünf Abschnitte: I Strafverfahren, II Kosten/Versicherung (748 Wörter), III Selbstanzeige, IV Steuerstrafrecht A-Z, V Mythen. `_work/bestand-metrics.json`, `_work/live/faq.txt`, 2026-10-11. Ohne Kostenteil: **1807 Wörter** (Wunsch der Kanzlei, Mail 09.10.). |
| 3 | Alle Kundentexte zum Thema | ja | Live-FAQ, Live-Seiten Verteidigung im Steuerstrafverfahren und Durchsuchungsbegleitung, `kosten.txt`, `ki-baustein.txt`, `pruefung-2026-10-11.md`. Gelesen 2026-10-11. |
| 4 | Ziel-Keyword und Suchvolumen | ja | steuerstrafverfahren 260 (gehört ST-12), steuerstrafverfahren ablauf 20, steuerstrafverfahren einstellung 20. `03-demand/volume.json`, DataForSEO 2026-10-11. 20 heißt wenig Daten, nicht kaum Nachfrage. |
| 5 | SERP gelesen | ja | `_work/serp-steuerstrafverfahren.json` (neu, 2026-10-11, DataForSEO, 0,0035 USD) und `content-pool/02-competitors/serp-8.json` ('steuerstrafverfahren ablauf'). Treffer: Fachverlage, Kanzlei-Ratgeber, Lexika, ein YouTube-Video. |
| 6 | Echte PAA-Fragen | ja | 8 Fragen aus beiden SERPs (Strafen, Fehler in der Steuererklärung, Knast, § 369/370, Kosten, Verdacht, 3000 Euro, Dauer) plus PAA der Cluster-SERPs (Durchsuchung, Verjährung, Selbstanzeige). Im Brief unter `paa_questions` (11 beantwortet, 4 mit Grund verworfen). |
| 7 | Wettbewerber-Wortzahl, mindestens 2 Messungen | ja | 16 von 16 gelesen, Median **1481** Wörter, 70-%-Untergrenze **1037**. Liste unten. `_work/bench-metrics.json`, 2026-10-11. |
| 8 | Lokaler Fakt | nicht nötig | Themenseite, bundesweit. |

## Messreihe Wettbewerber (SERP 'steuerstrafverfahren', 'steuerstrafverfahren ablauf')

| Wörter | Seite |
| --- | --- |
| 5890 | https://www.hortmannlaw.com/steuerfahndung-strafverfahren-selbstanzeige-anwalt |
| 4515 | https://www.lhp-gruppe.de/themen/steuerstrafverfahren/ |
| 3332 | https://steuerstrafrecht-rechtsanwalt.de/strafmass-bei-steuerhinterziehung.html |
| 2746 | https://www.ra-kotz.de/steuerstrafverfahren.htm |
| 2618 | https://rechtinfo.de/blog/ermittlungsverfahren-steuerstrafrecht/ |
| 1888 | https://www.rudolph-recht.de/rechtsgebiete/steuerstrafrecht/ |
| 1844 | https://www.juhn.com/fachwissen/steuerhinterziehung-selbstanzeige/aufgaben-der-steuerfahndung/ |
| 1516 | https://www.steinbock-partner.de/steuerrecht/steuerstrafverfahren/ |
| 1447 | https://www.die-anwalts-kanzlei.de/steuerstrafrecht/steuerstrafverfahren-nach-betriebspruefung/ |
| 1438 | https://www.anwalt-haxthausen.berlin/steuerstrafrecht.html |
| 999 | https://www.lhp-gruppe.de/themen/strafbefehl-im-steuerstrafverfahren/ |
| 943 | https://kanzlei-wb.com/was-tun-bei-einem-steuerstrafverfahren/ |
| 763 | https://leipzig-steuerstrafverteidiger.de/steuerstrafrecht/steuerstrafverfahren/ |
| 649 | https://www.pmpg.de/recht/steuerstrafverfahren-selbstanzeige/ |
| 370 | https://ra-hoernschemeyer.de/steuerstrafverfahren/ |
| 307 | https://steuerdelikt.de/haeufige-fragen/steuerstrafverfahren/wann-werden-steuerstrafverfahren-eingestellt |

Nicht gemessen (Video, Fachdatenbank, Zeitschrift): youtube.com, datenbank.nwb.de, haufe.de, iww.de, burhoff.de.

## Wortzahl-Urteil (vorab, Ziel)

Bestand 2555 (ohne Kostenteil 1807). Wettbewerber-Median 1481, Untergrenze 1037. Die Seite darf nicht dünner werden als der Bestand ohne Kostenteil. Zielkorridor 2.200 bis 3.000 Wörter, weil die Kurzantworten (40 bis 60 Wörter, CP-SVC-024) zusätzlich zu den Langantworten stehen.

## Konflikte im Bestand und bei Kundentexten

1. Der Kostenteil II (748 Wörter, Stundensätze 380/330/280 bis 450/400/350, Picasso-Geschichte) entfällt auf Wunsch der Kanzlei. Neue Sätze und Beträge stehen im Kundentext `kosten.txt` und auf /kosten/. Die FAQ nennt keine Beträge.
2. Live-FAQ nutzt "Worst Case Szenario", "Wir sorgen dafür, dass Sie nicht über den Tisch gezogen werden", "Wir sorgen dafür, dass Sie doch über Los ziehen können" und einen Monopoly-Vergleich: Ergebnisaussagen und Angstton (BRAO). Nicht übernommen.
3. Uli-Hoeneß-Beispiel in der Live-FAQ (III): keine Quelle gelesen und gespeichert, nicht übernommen.
4. "Einleitungsvermerk" ist in der Live-FAQ ein "behördliches Schreiben". § 397 Abs. 2 AO verlangt einen Vermerk in den Akten, die Mitteilung an den Beschuldigten steht in Abs. 3. Die Seite folgt dem Gesetz.
5. "Als vorbestraft gilt, wer zu mehr als 90 Tagessätzen oder mehr als 3 Monaten verurteilt wurde": vereinfacht. Die Seite folgt dem Wortlaut von § 32 Abs. 2 Nr. 5 und § 53 BZRG.
6. Hauptkeyword 'steuerstrafverfahren' steht im Sitetree bei ST-12 und ST-32 (Regel S6). Entscheidung in OPEN-FLAGS B3.

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Keine Blocker.
