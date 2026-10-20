# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Ratgeber Strafe, ST-35)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand 2026-10-11, nach der Korrekturrunde (REVIEW-G).

## A. Rechtsgrauzonen und Seitenspezifisches

| # | Stelle | Frage | Stand |
| --- | --- | --- | --- |
| A1 | S04, S05, FAQ "Gefängnis": BGH-Rechtsprechung | Die Grenze für das große Ausmaß steht nach BGH 27.10.2015, 1 StR 373/15 (Primärtext gespeichert: `_work/bgh-1-StR-373-15.txt`, Leitsatz 1 und Rn. 29 bis 32) bei 50.000 Euro für jede Steuerhinterziehung. Die Grenze von 100.000 Euro steht nicht mehr im Text. Das Landgericht Bonn wendet die 50.000 Euro im Urteil vom 03.06.2025 an (`_work/lg-bonn-62-KLs-1-24-auszug.txt`). Nicht geprüft: ob nach 2015 ein weiteres BGH-Urteil die Wertgrenze oder die Maßstäbe von 2008 ändert (sechsstelliger Betrag und Geldstrafe; Millionenhöhe und Bewährung). Der sichtbare Text sagt das offen. | Kanzlei bestätigt oder ergänzt |
| A2 | S06: frühere Aussage "berufs- oder beamtenrechtliche Folgen, Waffen- oder Jagdverbot, Passentzug" | Keine Norm gelesen. Der Satz ist gestrichen. | erledigt (Review A4) |
| A3 | S08: "Das Schweigen darf nicht als Schuldeingeständnis gewertet werden" | Kanzleiaussage aus der Live-FAQ, ohne Norm. Bleibt als Kanzleiaussage (Claim L17). Die Aussage "in beiden Fällen gelten Sie nicht als vorbestraft" ist gestrichen. | Kanzlei prüft |
| A4 | S06 Führungszeugnis | Jetzt mit § 32 Abs. 2 Nummer 5 und Abs. 4 BZRG nach gespeichertem Text. Das Wort "vorbestraft" kommt nicht mehr vor. | erledigt (Review A2 und A3) |
| A5 | S03: "Steuerhinterziehung ist kein Kavaliersdelikt, sondern eine Straftat." | Wendung der Kanzlei (Kanzleiseite). Bleibt wegen der Stimme. | Kanzlei prüft |
| A6 | FAQ "Wie lange dauert ein Strafverfahren" | Jetzt beantwortet ohne Zahl: keine feste Dauer, lange Verfahrensdauer als Strafzumessungsfaktor (BGH 1 StR 373/15, Leitsatz 6). Eine belegte Dauer gibt es nicht. | Kanzlei kann eine Aussage liefern |
| A7 | FAQ 1: "Steuerstraftaten sind Taten, die nach den Steuergesetzen strafbar sind" | Wortlaut von § 369 Abs. 1 Nummer 1 AO. Dass die Steuerhinterziehung dazugehört, ist ein Schluss. | Kanzlei prüft |
| A8 | Das Wort "straffrei" und "Straffreiheit" kommt nicht vor. Die Selbstanzeige-Wirkung steht als "nicht nach § 370 bestraft". | LR10 | Hinweis |
| A9 | G2-Skript: Die Regel "Nr. 1" (Superlativ) trifft Gesetzeszitate und Zitate wie "nach bestem Wissen". Im Text steht darum "Nummer". | check_legal.py | Vorschlag an Skill |
| A10 | FAQ "leichte Steuerhinterziehung": Vorsatz | Der Satz stützt sich auf § 15 StGB und BGH 1 StR 416/08 Rn. 41 (weder direkter Vorsatz noch Bereicherungsabsicht nötig). Die Kanzleidefinition "wissentlich oder billigend in Kauf nehmen" steht nicht mehr im Text, weil keine Quelle dafür gelesen wurde. Der Satz "Vorsatz ist nicht dasselbe wie Absicht" ist eine Schlussfolgerung aus dem BGH-Satz. | Kanzlei prüft |
| A11 | FAQ "Kann eine Selbstanzeige etwas ändern?" | Neu: "grundsätzlich", 25.000 Euro nach § 371 Abs. 2 Satz 1 Nummer 3, Abs. 2a abweichend, § 398a. Wortlaut aus dem gespeicherten § 371. Die Erstberatung wird nicht mehr erwähnt (Source of Truth: Erstberatung gegen Pauschale; Beträge nur auf /kosten/). | erledigt (Review A6, B) |
| A12 | S07 Strafbefehl und § 153a | Neu: Wortlaut nach § 407 Abs. 1, § 410 Abs. 1 und 3 StPO und § 153a Abs. 1 StPO (alle gespeichert in `_work/gesetze/`). "Angeklagter" folgt dem Wortlaut von § 410. | erledigt (Review A5, A7) |
| A13 | Tabelle "Der Strafrahmen auf einen Blick" (S03) | Nur Wortlaut der Normen. Keine Prognose. | Hinweis |

## B. Offene Punkte für alle Ratgeber-Seiten

| # | Punkt | Quelle | Stand |
| --- | --- | --- | --- |
| B1 | Autorin oder Autor und Freigabe: offen. Pool und Sitetree führen `needs_client`. Berufsrecht-Check (BRAO, UWG) vor Veröffentlichung. Ohne Prüfung bleibt der Status "Vorschlag, wartet auf Abstimmung mit der Kanzlei". | pool.json, sitetree.json | Platzhalter in `05-final/placeholders.md` |
| B2 | Titel von Dr. Stürzl stammen aus ihrem Lebenslauf, nicht aus einem Kammernachweis. | approved-copy.md | Kanzlei bestätigt |
| B3 | Die Live-Seite benutzt Wörter, die dieser Text bewusst nicht übernimmt: "Spezialisierung", "Expertise", "exzellent", "Festpreis", "hart in der Sache". Die Live-FAQ schreibt außerdem "Worst Case Szenario" und "Ihre Freiheit steht auf dem Spiel". Das ist Angst-Wortschatz (Regel LR16) und steht hier nicht. | Live-FAQ, voice.md | Nur Hinweis |
| B4 | Das Stimmprofil `voice.md` ist ein Entwurf. Blog-Beiträge sprechen als "wir" mit Anrede Sie. Die Blog-Regel B4 sieht Ich-Form der Autorin vor. Das hängt an Punkt B1. | blog-rules.md, voice.md | Offen |
| B5 | Rechtsgrenze: Die Beiträge geben allgemeine Information und keine Einschätzung des Einzelfalls (Regel B7). Der Hinweis steht am Ende. | blog-rules.md | erledigt im Text |
| B6 | `schema.jsonld` liegt als Entwurf in `05-final/`. Autorenname und Veröffentlichungsdatum sind darin leer, weil Platzhalter nicht ins Markup dürfen (G6b). Nach der Freigabe Name in `brief.json` (byline) und Datum im Frontmatter eintragen und `schema_tool.py make` neu starten. Das Entwurf-Markup darf vorher nicht live gehen. | schema_tool.py | Offen bis B1 |
| B7 | Telefonnummern im Abschluss stammen aus nap.json (Source of Truth Tab 00). Keine Adresse, keine Öffnungszeiten im Text. | nap.json | bestätigt |

## C. Korrekturrunde 2026-10-11 (REVIEW-G, FIX-G-report.md)

- Sicherung vor der Änderung: `05-final/page-vorreview.md`. Neuer Entwurf: `03-draft/draft-v3.md`, Endfassung `05-final/page.md`.
- Rivalen-Cleanse: nicht gelaufen. Der codex-Aufruf endete mit "usage limit" (Exit 1, Neustart frühestens 17:20 laut Meldung). G5 besteht nur im Lint (5/5). Ein Cleanse-Aufruf ist offen und darf einmal nachgeholt werden (danach `diff_claims.py diff`).
- Wortzahl 1848 (Zielbereich bis 1800). Grund: Tabelle, BGH 2015, § 32 Abs. 4 BZRG, § 153a, Strafbefehl, Frage zur Dauer. Kürzen möglich bei der Quellenliste.
- Ein CTA am Ende (Blog-Regel B9). Link zur Geldseite im ersten Drittel (S03) und am Ende (S11).
