# FIX-B-report: Korrekturrunde Batch B (ST-11, ST-13, ST-10, ST-32)

Stand 2026-10-11. Grundlage: `REVIEW-B.md`, `content-writing-stuerzl-fixes.md`, `content-writing-stuerzl-batch.md`. Vorversionen: `<ordner>/05-final/page-vorreview.md`. Neue Entwürfe: `<ordner>/03-draft/draft-v3.md`. Nichts live, kein Upload.

## Zusammenfassung

| Seite | Wörter vorher | Wörter jetzt | Seller-Layer (höchstens 550) | Gates G1 bis G6 | Cleanse-Aufrufe | Platzhalter |
| --- | --- | --- | --- | --- | --- | --- |
| ST-11 Steuerstrafrecht | 1.752 | 1.584 | 543 | PASS | 1 Versuch, gescheitert (codex-Limit) | 0 (vorher 1) |
| ST-13 Gutachten und Risikobewertung | 1.216 | 1.423 | 521 | PASS | 1 Versuch, gescheitert (codex-Limit) | 2 (Kanzlei-Fragen zu Tax Compliance) |
| ST-10 Leistungen | 512 | 552 | 435 | PASS | 0 | 0 |
| ST-32 FAQ | 2.616 | 3.596 | 272 | PASS | 0 | 0 |

G5 ist nur das Lint (5/5). Das Rivalen-Modell lief nicht: `cleanse_de.sh` meldet "usage limit" (codex, wieder frei ab 17:20 Uhr). Die Seiten bleiben ohne Cleanse. Nach dem Limit: ein Aufruf je Seite, dann `diff_claims.py diff`.

Text-Überschneidung (5-Wort-Folgen, Maß: gemeinsame Folgen geteilt durch die kleinere Seite, Grenze 25 %):

| Paar | vorher | jetzt |
| --- | --- | --- |
| ST-10 / ST-11 | 31 % | 15 % |
| ST-10 / ST-13 | 27 % | 15 % |
| ST-11 / ST-32 | 30 % | 14 % |

`link_network.py --json` für das ganze Verzeichnis: pass = true, keine Fehler. Hinweise (nur Warnungen) zu meinen Seiten: ST-10 17 Textlinks (Hub), ST-11 9 (Säulenseite), ST-32 11 (Hub). Alle Link-Ziele stehen in `slugs.json`. ST-10 hat 3 eingehende Links; mehr entstehen nur auf anderen Seiten.

Ungültige Ziele: keine. ST-11 und ST-10 verlinken /ratgeber/steuerhinterziehung-strafe/ und /ratgeber/verjaehrung/ (ST-11) sowie /compliance/ (ST-10, ST-13). Alle vier Ziele sind geschrieben und stehen in `slugs.json`.

Für alle vier Seiten neu: Adressblock (3 Zeilen) am Ende des Abschluss-Abschnitts; Kostensätze nach Fix-Punkt 3 (ohne Beträge); Hero-Zeile, Telefonzeile, Abschluss-Überschrift und Vertraulichkeits-Antwort je Seite mit eigenen Wörtern; Zitat-Quelle "Startseite" statt "Kanzleiseite".

## ST-11 Steuerstrafrecht

| Punkt des Reviews | Ergebnis |
| --- | --- |
| 1 Verjährung "das Doppelte" gilt auch für 15 Jahre | behoben: Liste "Fristen auf einen Blick" in S07 Block 3: Grundfall das Doppelte (§ 78c Abs. 3 Satz 2 StGB), Fälle des § 376 Abs. 1 AO das Zweieinhalbfache (§ 376 Abs. 3 AO). Wie ST-36. |
| 2 "besonders schwere Fälle 15 Jahre" ohne "Nr. 1 bis 6" | behoben in S07 und FAQ: "Fälle des § 370 Abs. 3 Satz 2 Nr. 1 bis 6 AO". Dazu § 78 Abs. 4 StGB für den Grundfall. |
| 3 § 153 AO ohne "Steuerpflichtiger" und "vor Ablauf der Festsetzungsfrist" | behoben (S07 Block 4, nahe am Gesetzestext). |
| 4 Zitat: Quelle "Kanzleiseite", Auslassung ohne Zeichen | behoben: "Auf der Startseite der Kanzlei", zwei getrennte Zitate. (Das Prüfskript erlaubt keine Klammer "[...]".) |
| 5 H1 und Title "Anwalt für Steuerstrafrecht" | bewusst offen: von Martin freigegeben (Fix-Punkt 13), Flag A1 bleibt. Entscheidung Martin und Kanzlei. |
| 6 "schildern Sie sie uns kurz" | behoben: "Nennen Sie uns Ihr Thema". |
| 7 "wichtigste Tatbestand" | behoben: "Zentral ist" (S02 und S07). |
| 8 Platzhalter für den Betrag der Erstberatung | behoben: gestrichen, "üblicherweise gegen Pauschale" bleibt. `placeholders.md` ohne Eintrag. |
| 9 TECH-Zeile "Frankfurt ohne Straße" | behoben. |
| 10 "zahlreiche Möglichkeiten, auf die Ermittlungen einzuwirken" | behoben: Satz gestrichen, neutral neu gefasst. "konfrontativ" bleibt (Wortlaut der Kanzlei, Flag A6, Querpunkt 9 des Reviews). |
| Überschneidung mit ST-10 und ST-32 | behoben: S08 sind jetzt kurze Antworten in eigenen Wörtern mit Link auf /faq/; S07 Block 2 und 5 in eigenen Wörtern; Hero-, Telefon- und Abschlusszeilen geändert. |
| Lücke (a) NAP-Block | behoben (Adressblock). |
| Lücke (b) Fristen-Übersicht | behoben als Liste in S07 Block 3 (nur aus gespeicherten Gesetzen). |
| Lücke (c) Prüfzeile und Person-Schema | bewusst offen: Prüfzeile braucht das OK der Kanzlei; `schema_tool.py` erzeugt Person nur auf Personenseiten. Flag B7. |

## ST-13 Gutachten und Risikobewertung

| Punkt des Reviews | Ergebnis |
| --- | --- |
| 1 "Tax Compliance" in Title, H1, Meta; Definition in S02 | behoben: Title "Gutachten und Risikobewertung im Steuerstrafrecht", H1 gleich, Meta ohne "Tax Compliance". S02 ohne Definition. Brief: `keyword_primary` jetzt "gutachten und risikobewertung" (vorher "tax compliance"), `own_phrases` ohne "selbstanzeigesicher", `keyword_note` angepasst. Definition in der FAQ als Platzhalter 2, Angebot Tax-CMS als Platzhalter 1. Messplan neu erzeugt. |
| 2 § 30 OWiG "Unternehmen" | behoben: "juristische Person oder Personenvereinigung", Gruppen der leitenden Personen, Bereicherung genannt. |
| 3 § 130 OWiG ohne "vorsätzlich oder fahrlässig" und ohne Pflicht "mit Strafe oder Geldbuße bedroht"; H3 "Leitung" | behoben: beide Elemente stehen im Text und in der FAQ. H3 lautet "Aufsichtspflicht des Inhabers und Geldbuße gegen das Unternehmen" (kein § 9 OWiG). |
| 4 "kein unnötiges Risiko", "selbstanzeigesicher" | behoben: "die Folgen einer Korrektur kennen", "mit Blick auf die Anforderungen des § 371 AO", FAQ "damit die steuerliche und die strafrechtliche Seite einer Korrektur zusammenpassen". |
| 5 § 370-Satz nach § 153 wirkt als Drohung; "sinnvoll"-Satz | behoben: zwei Blöcke (Fehler ohne Vorsatz, Vorsatz oder Leichtfertigkeit); Strafrahmen "sieht das Gesetz vor"; "kann auch dann geprüft werden". |
| 6 § 153 ohne Bedingungen (S07, FAQ) | behoben. Dazu Gesamtrechtsnachfolger (Abs. 1 Satz 2) und Außenprüfung (Abs. 4) aus dem gespeicherten Text. |
| 7 "hängt davon ab, wie sie entstanden sind" | behoben: Wendung der Kanzlei "hängt von einer ganzen Reihe an Faktoren ab". |
| 8 "immer höhere Anforderungen" ohne Quelle | behoben: "Unserer Erfahrung nach". |
| 9 Zitat-Quelle | behoben: "Auf der Startseite der Kanzlei". |
| 10 Platzhalter Erstberatung | behoben: gestrichen. |
| Überschneidung mit ST-10 | behoben (siehe Tabelle oben). |
| Lücken (a) Block "Was eine Risikoprüfung umfasst", (b) Tabelle, (c) Prüfzeile und Person-Schema | bewusst offen: (a) und (c) brauchen die Kanzlei (Angebot unbestätigt); (b) nicht gebaut, § 153 und § 371 stehen in zwei getrennten Blöcken. Flag B6. |

## ST-10 Leistungen

| Punkt des Reviews | Ergebnis |
| --- | --- |
| 1 "Fokus" | behoben: "Wir beraten und verteidigen im Steuerstrafrecht und in angrenzenden Gebieten des Wirtschaftsstrafrechts." |
| 2 Karte 1 verlinkt ST-12 nicht | behoben: Karte 1 verlinkt /steuerstrafrecht/verteidigung-im-steuerstrafverfahren/. |
| 3 "schildern Sie sie uns kurz" | behoben: "Nennen Sie uns Ihr Thema". |
| 4 Überschneidung 31 % und 27 % | behoben (15 % und 15 %): Vertraulichkeits-FAQ gestrichen, Kosten-FAQ auf einen Satz plus Link, neue FAQ "Welcher Bereich passt zu meiner Lage?", eigener Abschluss. |
| Lücke (a) Anlass je Bereich | behoben: S04 deckt jetzt alle sechs Bereiche ab (vorher vier), jede Zeile nennt den Anlass und den Link. Die Karten bleiben im freigegebenen Wortlaut. |
| Lücke (b) Hub-FAQ | behoben (siehe oben). |
| Lücke (c) NAP | behoben. ItemList-Schema bewusst offen: `schema_tool.py` erzeugt keines (Wunsch an den Skill). Flag B8. |

## ST-32 FAQ

| Punkt des Reviews | Ergebnis |
| --- | --- |
| 1 Aussagen ohne Quelle | belegt: Vorsatz (BGH 1 StR 525/20, gespeichert); Schweigerecht (BGH 3 StR 531/99, gespeichert); Einstellung ohne Schuldspruch (§ 153a Abs. 1, § 260 Abs. 4 StPO); Waffen-, Jagd-, Beamten- und Passfolgen (§ 5 WaffG, § 17 BJagdG, § 24 BeamtStG, § 7 PassG, gespeichert); "Beschuldigter" über § 397 Abs. 1 AO statt der falschen Zuordnung. |
| 2 § 152 AO "muss mit Zuschlag rechnen" | behoben: Abs. 1 "kann", Abs. 2 "in bestimmten Fällen festzusetzen". |
| 3 "15 Jahre" ohne "Nr. 1 bis 6" | behoben. |
| 4 § 378 ohne Bedingung | behoben: "als Steuerpflichtiger oder bei Wahrnehmung der Angelegenheiten eines Steuerpflichtigen". |
| 5 Unterschied § 153 / § 371 als Lehre der Kanzlei; § 153 ohne Bedingungen | behoben: "nach Auffassung der Kanzlei", Bedingungen ergänzt. |
| 6 Freiheitsstrafe / Bewährung | behoben: Frage "Wann kommt ... eine Freiheitsstrafe in Betracht?" antwortet jetzt zur Strafe (keine feste Grenze in § 370 AO); neue Frage "Kann eine Freiheitsstrafe zur Bewährung ausgesetzt werden?" nennt den Prognose-Maßstab aus § 56 Abs. 1 StGB. |
| 7 Durchsuchung durch das Finanzamt | behoben: § 404 Abs. 1 AO und § 105 Abs. 1 StPO verknüpft. |
| 8 Kurzantwort 40 bis 60 Wörter | behoben: alle 45 Antworten geprüft, 0 außerhalb des Bandes (vorher 19 von 40). |
| 9 Mythen-Format "Falsch." / "Nein." | bewusst offen (Review: behalten, Kanzlei bestätigt): "Doch, das kann es." Der Rat "unbedingt vorher Fristverlängerung" steht als allgemeine Information mit § 109 AO und "im Einzelfall" (Fix-Punkt 7). Flag A4. |
| Verlinkung (b): ST-12, /unternehmensvertretung/, /dr-anja-stuerzl/ | behoben (zusätzlich /ordnungswidrigkeiten/). |
| Lücke (a) Prüfzeile | bewusst offen (Kanzlei-OK). Flag B9. |
| Überschneidung ST-11 / ST-32 | behoben (14 %). |

### Live-FAQ: was zurückgeholt wurde und was nicht

| Eintrag der Live-FAQ | Ergebnis |
| --- | --- |
| I.1 "In beiden Fällen nicht vorbestraft", "offengelassen, ob der Vorwurf zutrifft" | zurück, als "nach Darstellung der Kanzlei" markiert, mit § 3 Nr. 1 BZRG; Mythos-Antwort wieder mit "nicht vorbestraft" |
| I.1 Strafbefehl: Einspruch führt zur Hauptverhandlung | zurück mit § 411 Abs. 1 StPO (neuer Gesetzestext gespeichert) |
| I.1 "oder ein Haftbefehl erlassen wird" | zurück |
| I.2 Steuerfahndung "im Auftrag der BuStra oder Staatsanwaltschaft" | zurück |
| I.2 BuStra "(kleineren) Steuerdelikten" | in sicherer Fassung zurück: "etwa bei kleineren Steuerdelikten". Grund: § 386 Abs. 2 AO nennt keine Größe. In der Liste für die Kanzlei. |
| I.2 Hauptzollamt: Sozialabgaben | in sicherer Fassung zurück ("nach Darstellung der Kanzlei", § 266a StGB) |
| I.2 Rentenversicherung: "(vorsätzlich)", Schwarzarbeit, Scheinselbständigkeit | zurück |
| I.4 "Passentzug" | in sicherer Fassung: Passversagung nach § 7 Abs. 1 Nr. 2 und 4 PassG. Das Gesetz kennt keinen "Passentzug" als Folge der Verurteilung. In der Liste für die Kanzlei. |
| III zweite Frage ("nur Selbstanzeige, wenn absichtlich?"), "innere Tatsache", "grundlegend unterschiedlich", "regelmäßig notwendig" | zurück, als Darstellung der Kanzlei markiert; neue Frage in S07 |
| IV Bußgeldbescheid, Einleitungsverfügung, Einstellung gegen Geldauflage | zurück als kurze Einträge (Bußgeldbescheid mit § 65 und § 67 OWiG) |
| IV Vollmacht | zurück mit § 145a Abs. 1 StPO und § 137 Abs. 1 StPO |
| IV Belehrung "oder Zeugen", "Aussagen können gegen ihn verwendet werden" | zurück (Zeugen: § 55 Abs. 2 StPO; Aussagen: Darstellung der Kanzlei, kein Gesetzestext) |
| IV Anschlusserklärung: Grund "Sperrgrund der Tatentdeckung" | zurück, mit Verweis auf § 371 Abs. 2 AO ohne Umformulierung und auf /selbstanzeige/ |
| IV Strafanzeige "von jeder Person" | zurück als Darstellung der Kanzlei |
| V Schweigerecht: "Sie sollten zunächst immer ... Gebrauch machen" | in sicherer Fassung (Fix-Punkt 7): "Ob und wie man sich im Einzelfall äußert, lässt sich vorab mit einem Verteidiger klären." Der Satz "Schweigen verhindert unbedachte Selbstbelastung" ist nicht zurück (Ergebniswort). |
| V Steuerberater: "ggf. (mit) strafbar" | zurück |
| Kosten/Versicherung (Rechtsschutz) | bewusst offen: kein Text der Kanzlei; Flag B1 |
| "Worst Case", "Strafe muss sein", "über den Tisch gezogen", Monopoly, Hoeneß, "exzellenter Ruf", "24/7" | nicht zurück (BRAO, wie im Review bestätigt) |

## Änderungen an Dateien außerhalb der Seitentexte

- `01-brief/brief.json` ST-13: `keyword_primary`, `own_phrases`, `keyword_note`. ST-32: `word_range` 1.900 bis 3.700 (Grund: zurückgeholte Einträge, Flag B8).
- `01-brief/claims.json` aller vier Seiten fortgeschrieben (neue Paragrafen, BGH, Telefonzeiten, Kostenmodell).
- `_work/law/` ST-32: neue Gesetzestexte (`bzrg__3`, `stpo__411`, `stpo__145a`, `stgb__16`, `owig_1968__65`, `beamtstg__24`, `waffg__5`, `bjagdg__17`, `passg__7`) und zwei Auszüge: `bgh_1StR_525-20_auszug.txt`, `bgh_3StR_531-99_auszug.txt`.
- `OPEN-FLAGS.md`, `placeholders.md`, `_status.md`, `_run.json`, `cms-blocks.txt`, `schema.jsonld`, `measure-plan.md` aller vier Seiten neu.

## Wünsche an den Skill und offene Punkte für Martin

1. `schema_tool.py`: Person-Schema auch auf Service-Seiten mit Personenblock und ItemList für Hubs. Heute nicht möglich.
2. `validate_page.py` und `check_style.py` lassen kein Auslassungszeichen "[...]" in Zitaten zu. Zitate müssen getrennt stehen.
3. Martin entscheidet: "Anwalt für Steuerstrafrecht" (H1 ST-11), "konfrontativ", "selbstanzeigesicher" (jetzt in keinem Text), Prüfzeile mit Dr. Stürzl, Kürzung von ST-32, Hauptkeyword von ST-13, sobald die Kanzlei das Tax-CMS-Angebot beantwortet hat.
4. Cleanse nach dem Ende des codex-Limits nachholen.
