# Gate A0 (voll): Stürzl, Schwarzarbeit, Sozialversicherung und Arbeitnehmerüberlassung (ST-28)

Datum: 2026-10-11. Seitentyp A (Geldseite, hohe Informationsnachfrage). Pool-Item CP-SVC-015. Titel mit den Suchwörtern, nicht "Arbeitsstrafrecht" (Sitetree-Vorgabe).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste, Adressen) | ja | `source-of-truth-2026-10-11.md`, `nap.json` (Adressen bestätigt), `content-pool/01-client/client-baseline.md`, `cro/04-copy/approved-copy.md`, 2026-10-11 |
| 2 | Live-Bestand abgerufen und gezählt | ja | ST-28: 148 Wörter, 2×H1 ("Leistungen", "Arbeitsstrafrecht"), 0×H2. `_work/live/arbeitsstrafrecht.txt`, `_work/metrics.json`, 2026-10-11 |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 98 Treffer für 'schwarzarbeit strafe', 'sozialversicherungsbetrug', 'arbeitnehmerüberlassung'. `_work/autocomplete.json`, 2026-10-11 |
| 4 | Ziel-Keyword und Suchvolumen | ja | schwarzarbeit strafe 2.900; finanzkontrolle schwarzarbeit 2.400; sozialversicherungsbetrug 480; scheinselbständigkeit strafe 480; sozialversicherungsbetrug strafe 90; illegale arbeitnehmerüberlassung 40; arbeitsstrafrecht 40; schwarzarbeit anwalt 30. `_work/volume.json`, DataForSEO, de, 2276, 2026-10-11. "Arbeitsstrafrecht" ist kaum ein Suchbegriff, die Begleitdelikte sind es (Onboarding-Call). |
| 5 | SERP Top 10 für das Ziel-Keyword | ja | 'schwarzarbeit strafe' (`_work/serp.json`) und 'sozialversicherungsbetrug anwalt' (`_work/serp2.json`), 2026-10-11. Behörden (zoll.de, berlin.de, arbeitsagentur.de), Lexika (personio, lexware, wikipedia) und Software-Blogs bleiben außerhalb des Wettbewerberset, soweit nicht von Kanzleien. |
| 6 | Echte PAA-Fragen | ja | 6 Fragen. Beantwortet: 'Was passiert, wenn man wegen Schwarzarbeit angezeigt wird?', 'Wann gilt es als Schwarzarbeit?', 'Wer bekommt Ärger bei Schwarzarbeit?'. Verworfen mit Grund: anonyme Meldung (nicht im Angebot), Sozialbetrug und § 263 StGB (nicht im Angebot). Siehe `brief.paa_questions`. |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 14 von 14 Seiten gelesen, Median **1876** Wörter, 70-%-Untergrenze **1313**. Liste unten. `_work/bench-metrics.json`, 2026-10-11 |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Themenseite. |

## Messreihe Wettbewerber (Seiten zu Schwarzarbeit und Arbeitsstrafrecht)

| Wörter | Seite |
| --- | --- |
| 3243 | https://www.lhp-gruppe.de/wirtschaftsstrafrecht/schwarzarbeit-sozialversicherungsbetrug/ |
| 2579 | https://www.bms-rechtsanwaelte.de/wirtschaftsrecht-blog/schwarzarbeit-strafe-vermeiden-durch-selbstanzeige |
| 2500 | https://www.strafverteidiger-salzgitter.de/schwarzarbeit-strafe/ |
| 2279 | https://www.die-anwalts-kanzlei.de/steuerstrafrecht/strafe-bei-schwarzarbeit/ |
| 2210 | https://gloeckle.law/schwarzarbeit-strafe/ |
| 2169 | https://www.liebert-roeth.de/de/rechtsgebiete/architektenrecht/schwarzarbeit-am-bau-konsequenzen |
| 2106 | https://kanzlei-succu.de/schwarzarbeit/ |
| 1647 | https://ra-araujo-kurth.de/rechtsbeitraege/schwarzarbeit-diese-strafe-droht-arbeitnehmern/ |
| 1445 | https://www.dr-buchert.de/strafverteidigung/arbeitsstrafrecht/ |
| 1420 | https://www.frankfromm.de/sozialversicherungsbetrug-strafe/ |
| 1036 | https://www.prehn-recht.de/arbeitsstrafrecht/ |
| 975 | https://dreyenberg.com/kompetenzen/zollrecht/ermittlungen-zu-schwarzarbeit-2 |
| 697 | https://alphalex.de/arbeitsstrafrecht/ |
| 656 | https://www.hopkins.law/expertise/schwarzarbeit-strafe |

## Wortzahl-Urteil (vorab, Ziel)

Bestand 148 Wörter (ST-28). Wettbewerber-Median 1876. Untergrenze 1313. Zielkorridor 1.300 bis 2.000 Wörter. Der Median ist hoch, weil viele Treffer lange Ratgeber von Kanzleien sind. Die Tiefe kommt aus fünf Vertiefungs-Blöcken mit gespeichertem Gesetzestext. Lange Lehrtexte (Verjährung, Strafzumessung) gehören in die Ratgeber-Beiträge.

## Konflikte im Bestand und bei Kundentexten

1. Der Bestand schreibt "Wir bringen haben die notwendige Expertise und Erfahrung" (Satzfehler) und "Experten aus unserem Netzwerk". Die Wörter "Expertise" und "Experten" stehen nicht auf der neuen Seite (BRAO/UWG). Die Aussage "Netzwerk" steht sinngemäß als "Fachleute aus unserem Netzwerk" (Flag).
2. Tippfehler im Bestand: "Abreitszeitschutzgesetz". Die Seite nennt das Arbeitszeitgesetz nicht eigens, weil kein Gesetzestext gelesen wurde.
3. Kostenmodell: Kundentext vom 2026-10-11 (Zeitaufwand, kein RVG) widerspricht der freigegebenen Startseite ("RVG") und der Live-FAQ.
4. Live-Seite nennt die alte Adresse und die alte Telefonnummer. Die neue Seite nennt nur bestätigte Daten.

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Keine Blocker.
