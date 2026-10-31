# Scan-Suche: Kanzlei Schmidt, Troisdorf (Agent D, Teil 1)

Stand 2026-10-31. Quelle: Local Falcon `searchForLocalFalconBusinessLocation` (Proximity Troisdorf) und `find_scan.py` (0 Credits).

## Ergebnis

**Kein eigener Google-Eintrag: JA.** Kein Treffer in sechs Local-Falcon-Suchen zeigt die Website `kanzlei-schmidt.online` oder die Telefonnummer `02241 2407450`. Auch die Maps-Prüfung von Agent O (`evidence/maps-match.md`) findet keinen Eintrag per Name, Telefon oder Adresse.

**Brauchbarer Scan: NEIN.** `find_scan.py "Kanzlei Schmidt"` und `find_scan.py "Thorsten Schmidt"` melden je `total: 0`. Es gibt keinen Eintrag, also gibt es nichts zu scannen. Es wurde kein Scan gestartet und kein Standort im Konto gespeichert.

## Beweis: find_scan.py

| Suchbegriff | Treffer |
| --- | --- |
| Kanzlei Schmidt | 0 |
| Thorsten Schmidt | 0 |

## Beweis: Place-Suchen (zusätzlich zu den vier Suchen des Orchestrators)

Abgleich-Regel: gleiche Website `kanzlei-schmidt.online` ODER gleiche Telefonnummer `02241 2407450`.

### Suche "Rechtsanwalt Troisdorf" (20 Ergebnisse, kein Treffer)

| # | Name | Adresse | Telefon | Website | Treffer? |
| --- | --- | --- | --- | --- | --- |
| 1 | Erbrecht und Arbeitsrecht Fachanwälte Goossens / Brieger | Poststraße 111-113, 53840 Troisdorf | 02241254550 | goossens-brieger.de | nein |
| 2 | Notar Dr. Christoph Huhn | Sieglarer Str. 2c, 53840 Troisdorf | 02241252050 | notar-huhn.de | nein |
| 3 | Rechtsanwalt Zechlin, Gekündigt? Sicher im Recht. | ÄrztehausPlus, Poststraße 111/113, 53840 Troisdorf | 022412545511 | andreas-zechlin.de | nein |
| 4 | Fachanwälte Grey & Grundhoff | Poststraße 101, 53840 Troisdorf | 022419790900 | grey-grundhoff.de | nein |
| 5 | Rechtsanwalt Sebastian Thalmann | Poststraße 111-113, 53840 Troisdorf | 02241254550 | rechtsanwalt-thalmann.de | nein |
| 6 | Rechtsanwälte Bernhardt, Ziemer und Kollegen GbR | Römerstraße 32, 53840 Troisdorf | 0224175001 | bernhardt-ziemer.de | nein |
| 7 | Rechtsanwältin Marion Grundhoff | Poststraße 101, 53840 Troisdorf | 02241407057 | grey-grundhoff.de | nein |
| 8 | Rechtsanwalt Stephan Rössler | Cecilienstraße 3, 53840 Troisdorf | 0224177028 | roessler-ra.de | nein |
| 9 | Rechtsanwalt Fritz | Hospitalstraße 2, 53840 Troisdorf | 02241978490 | rechtsanwalt-fritz.info | nein |
| 10 | Michael Zschacke | Mülheimer Str. 48, 53840 Troisdorf-Spich | 022418816299 | rbsz.de | nein |
| 11 | megra Steuerberatung | Sieglarer Str. 2c, 53840 Troisdorf | 02241944810 | megra-beratung.de | nein |
| 12 | Rechtsanwalt Achim Wald | Kölner Str. 33b, 53840 Troisdorf | 0224183386 | rechtsanwalt-wald.de | nein |
| 13 | Cem Sariyalim | Kölner Str. 144, 53840 Troisdorf | 022411497246 | - | nein |
| 14 | Offermanns & Wiede Steuerberater Partnerschaft mbB | Sieglarer Str. 6, 53840 Troisdorf | 02241979940 | ows-partner.de | nein |
| 15 | DiGiTAXperts Consulting GmbH | Sieglarer Str. 2C, 53840 Troisdorf | 022413226210 | digitaxperts.de | nein |
| 16 | Solmecke Rechtsanwälte PartGmbB | Klevstraße 13, 53840 Troisdorf | 022418817550 | solmecke.eu | nein |
| 17 | Rechtsanwalt Michael Hoffmann | Kochenholzstraße 37, 53842 Troisdorf-Spich | 022419228120 | ra-michael-hoffmann.de | nein |
| 18 | Nöbel Markus | Kerpstraße 11, 53844 Troisdorf-Sieglar | 022412520880 | - | nein |
| 19 | Rechtsanwalt Dr. jur. Peter-René Gülpen | Kirchstraße 11, 53840 Troisdorf | 022419739780 | strafverteidiger-guelpen.de | nein |
| 20 | Rechtsanwälte Marenbach & Kamp | Hauptstraße 135, 53842 Troisdorf | 02241944240 | - | nein |

Kein Ergebnis hat die Website `kanzlei-schmidt.online` oder die Nummer `02241 2407450`.

### Suche "Schmidt Troisdorf" (1 Ergebnis, kein Treffer)

| # | Name | Adresse | Telefon | Website | Treffer? |
| --- | --- | --- | --- | --- | --- |
| 1 | Zahnarzt Timo Schmidt | Schloßstraße 6, 53840 Troisdorf | 022419950709 | zahnarztteam-schmidt.de | nein |

Das einzige Ergebnis ist eine Zahnarztpraxis. Andere Website, andere Nummer, andere Branche.

### Suche "Steuerberater Troisdorf" (20 Ergebnisse, kein Treffer; zur Kontrolle erneut abgerufen)

Kein Ergebnis hat die Website `kanzlei-schmidt.online` oder die Nummer `02241 2407450`. Unter Sieglarer Str. 2c stehen in Local Falcon drei fremde Einträge: megra Steuerberatung, Notar Dr. Christoph Huhn und DiGiTAXperts Consulting GmbH. Keiner gehört zur Kanzlei Schmidt.

## Folgerung für die Seite

- Variante **ohne Google-Eintrag** (`hide_grid`, `hide_step2`, Modell korinna-heintze).
- Es gibt kein Raster. Die Kernaussage lautet: Die Kanzlei erscheint in keiner dieser Suchen. Die Konkurrenz steht in `competitors.md`.
- Keine Aussage "nicht beansprucht" und keine Aussage über Bewertungen der Kanzlei: Es gibt keinen Eintrag, den man prüfen kann.

## Kosten

Nur Suchen (Local-Falcon-Place-Suche, 0 Scan-Credits). Kein `runLocalFalconScan`, kein `saveLocalFalconBusinessLocationToAccount`.
