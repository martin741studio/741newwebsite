# Gate A0 (voll, Typ D Kostenseite): Stürzl, Kosten und Honorar (ST-31)

Datum: 2026-10-11. Seitentyp D (Kostenseite, kurz ist normal). Neue Seite, die URL /kosten gibt es heute nicht (404). Pool-Items CP-SVC-003 und CP-BRD-006 (KI-Baustein).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste, Adressen) | ja | `source-of-truth-2026-10-11.md`, `nap.json`, `content-pool/01-client/client-baseline.md`, `cro/04-copy/approved-copy.md`, 2026-10-11. Kostentext: `client-texte/kosten.txt`, `ki-baustein.txt`, `pruefung-2026-10-11.md`. |
| 2 | Live-Bestand abgerufen und gezählt | nein, Seite neu | Der Kostenteil steht heute als Abschnitt II "Kosten/Versicherung" in der Live-FAQ (rund 750 Wörter laut Prüfnotiz). Er wird übernommen und gekürzt; die FAQ soll danach auf /kosten/ verweisen (Kanzlei-Wunsch). `_work/live/faq.txt`, 2026-10-11. |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 25 Treffer für 'anwaltskosten selbstanzeige', 'steuerstrafverfahren kosten', 'strafverteidiger kosten'. `_work/autocomplete.json`, 2026-10-11. |
| 4 | Ziel-Keyword und Suchvolumen | ja | anwaltskosten selbstanzeige 10; selbstanzeige kosten 10; strafverteidiger kosten 210; strafverteidiger stundensatz 10; weitere Anfragen ohne Daten (steuerstrafverfahren kosten, anwalt steuerstrafrecht kosten). `_work/volume.json`, DataForSEO, de, 2276, 2026-10-11. Null heißt wenig Daten, nicht keine Nachfrage: Autocomplete zeigt 'kosten steuerstrafverfahren steuerlich absetzbar', 'strafverteidiger kosten rechner'. |
| 5 | SERP Top 10 für das Ziel-Keyword | ja | 'anwaltskosten selbstanzeige' (`_work/serp.json`) und 'anwalt steuerstrafrecht kosten' (`_work/serp2.json`), 2026-10-11. Kostenseiten von Kanzleien im Benchmark; Verzeichnisse, Versicherer (verivox), Wikipedia und Fachverlage nicht. |
| 6 | Echte PAA-Fragen | ja | 7 Fragen aus beiden SERPs. 4 beantwortet, 3 verworfen mit Grund (Strafanzeige nicht im Angebot; steuerliche Absetzbarkeit nicht rechtssicher ohne gelesene Rechtsprechung, doppelt gezählt). Siehe `brief.paa_questions`. |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 17 von 17 Seiten gelesen, Median **744** Wörter, 70-%-Untergrenze **520**. Liste unten. `_work/bench-metrics.json`, 2026-10-11 |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Seite. |

## Messreihe Wettbewerber (Kostenseiten)

| Wörter | Seite |
| --- | --- |
| 3174 | https://kanzlei-keiser.de/anwaltskosten-im-strafverfahren/kosten-und-faq/ |
| 2189 | https://www.bildt-law.de/selbstanzeige-kosten |
| 1824 | https://www.drburkhard.de/honorare-und-mandatsbedingungen/ |
| 1633 | https://www.strafrecht-bundesweit.de/anwaltskosten/anwaltskosten-bei-strafverteidigung/ |
| 1128 | https://www.dnk-rechtsanwaelte.de/de/kompetenzen/kosten_der_strafverteidigung/ |
| 1000 | https://www.ketzer-hermann.de/ratgeber-recht/anwaltskosten-im-strafverfahren/ |
| 979 | https://www.ochsmann.net/honorar.html |
| 857 | https://steuerdelikt.de/selbstanzeige/kosten-selbstanzeige |
| 744 | https://www.hortmannlaw.com/honorar |
| 709 | https://rabriel.de/Strafrecht/Kosten-im-Strafverfahren/ |
| 673 | https://steuerdelikt.de/fachanwaltskanzlei-steuerrecht/honorar |
| 672 | https://www.anwalt-strafverteidigung.de/strafrecht-abc/gebuhren-strafverteidiger-65 |
| 656 | https://alphalex.de/honorar/ |
| 631 | https://www.dnk-rechtsanwaelte.de/de/kanzlei/honorar_kosten/ |
| 586 | https://ht-strafrecht.de/strafverfahren/kosten-strafverteidigung/transparente-kosten/ |
| 472 | https://www.strafrecht-berlin-mitte.de/service/kosten-und-gebuehren.html |
| 447 | https://ht-strafrecht.de/strafverfahren/kosten-strafverteidigung/erste-instanz/ |

## Wortzahl-Urteil (vorab, Ziel)

Kein Bestand zu zählen (neue Seite). Wettbewerber-Median 744. Richtboden 520. Typ D: kurz ist normal (400 bis 700 Wörter). Zielkorridor 520 bis 1.500 Wörter. Die Seite wird länger als der Standard, weil der Kunde zwei Bausteine liefert (Kostentext 758 Wörter, KI-Baustein 219 Wörter) und der Kostenteil der FAQ hier aufgehen soll.

## Konflikte im Bestand und bei Kundentexten

1. Stundensätze: Kundentext EUR 350 bis 500 für alle nach Seniorität, Live-FAQ 380 bis 450 / 330 bis 400 / 280 bis 350 nach Funktion, Source of Truth früher 350 bis 450. Beide Fassungen dürfen nicht gleichzeitig live sein. Die Seite nennt keinen Betrag (Platzhalter).
2. Erstberatung: Kundentext Pauschale EUR 250 bis 350; Live-Kanzleiseite "zum Festpreis"; Source of Truth früher "350 € fest". Platzhalter.
3. Vorschuss: Kundentext EUR 1.000 bis 5.000 "üblicherweise". Platzhalter.
4. Rechtsschutz und Versicherung: der Kostentext schweigt, die FAQ-Überschrift heißt "Kosten/Versicherung". Platzhalter.
5. Der Kundentext enthält "besonders hohe Spezialisierung", "ausgezeichneter Ruf bei Kollegen und Behörden", "hochqualifiziert", "unbedingte Leidenschaft", "starkes Netzwerk", "umfassende fachliche Aus- und Weiterbildung": nicht übernommen (BRAO/UWG).
6. Interne Anmerkungen im Kundentext ("Ziel: Wir sprechen über's Geld ...", "Zusätzlich sollte auf der Website ...") gehören nicht auf die Seite und fehlen.
7. Redaktionelle Fehler im Kundentext ("geht es hier wirtschaftlich oder persönlich existenzielle Angelegenheiten", Preisformat "EUR 350, --") sind nicht übernommen.

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden (Zeile 2 durch FAQ-Abschnitt II ersetzt). Keine Blocker.
