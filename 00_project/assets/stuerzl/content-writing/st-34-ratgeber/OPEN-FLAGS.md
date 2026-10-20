# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Ratgeber-Hub, ST-34)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand 2026-10-11, nach der Korrekturrunde (REVIEW-G).

## A. Rechtsgrauzonen und Seitenspezifisches

| # | Stelle | Frage | Stand |
| --- | --- | --- | --- |
| A1 | Keyword | Der Sitetree nennt für ST-34 "steuerhinterziehung strafe", das schon ST-35 trägt (Regel S6, Kannibalisierung). Der Hub nimmt "steuerstrafrecht ratgeber" (keine Volumendaten). "steuerstrafrecht" (590) gehört zur Säulenseite ST-11. Der Hub verlinkt jetzt nach oben auf ST-11 und ST-12. | Martin entscheidet |
| A2 | Hub live erst mit Kindseiten | Die Karten verlinken auf ST-35 bis ST-37 (Vorschläge ohne Freigabe) und ST-18 (Batch A). Ohne Ziele gäbe es tote Links. | Reihenfolge der Veröffentlichung beachten |
| A3 | FAQ "Darf die Steuerfahndung meine Wohnung durchsuchen?" | Antwort aus § 102, § 105 StPO und § 404 AO. Der Inhalt muss zu ST-18 passen. Wer ST-18 ändert, prüft diese Antwort. | Hinweis |
| A4 | Karte "Wie läuft ein Steuerstrafverfahren ab?" | Beschreibung nach den Überschriften der Live-FAQ (Ablauf, Behörden, Zwangsmaßnahmen). ST-32 (FAQ) bleibt inhaltlich. | Hinweis |
| A5 | Rechtsstand | Der Satz "Die Beiträge geben den Rechtsstand vom 11. Oktober 2026 wieder" ist gestrichen, weil er für ST-35 (BGH 2008 und 2015) und ST-37 (BMF 2025) nicht galt. Der Hub sagt jetzt: jeder Beitrag nennt seine gelesenen Quellen und sein Prüfdatum. | erledigt (Review A2) |
| A6 | Autorenzeile | Neu auf dem Hub: Platzhalter für Autor und Veröffentlichungsdatum (Auftrag der Korrekturrunde), siehe `05-final/placeholders.md`. | Dr. Stürzl |
| A7 | Verjährungs-FAQ | Wortlaut jetzt mit "in den in § 370 Abs. 3 Satz 2 Nummer 1 bis 6 AO genannten Fällen" und "die Frist kann länger laufen". Gleicher Stand wie ST-36. Wer ST-36 ändert, prüft diese Antwort. | Hinweis |
| A8 | Adressblock | Der Hub hat einen Abschluss-CTA und ist kein Beitrag. Darum steht der Adressblock (drei Zeilen, Entscheidung 5) im Abschluss. Die Beiträge ST-35 bis ST-37 haben ihn nicht (Ausnahme für Ratgeber-Beiträge). | Martin bestätigt die Einordnung |
| A9 | Titel von Dr. Stürzl | siehe B2. | Hinweis |
| A10 | G2-Skript | siehe Bericht zu den Skript-Regeln (Gesetzesformeln). | Vorschlag an Skill |

## B. Offene Punkte für alle Ratgeber-Seiten

| # | Punkt | Quelle | Stand |
| --- | --- | --- | --- |
| B1 | Autorin oder Autor und Freigabe: offen. Pool und Sitetree führen `needs_client`. Berufsrecht-Check (BRAO, UWG) vor Veröffentlichung. Ohne Prüfung bleibt der Status "Vorschlag, wartet auf Abstimmung mit der Kanzlei". | pool.json, sitetree.json | Platzhalter in `05-final/placeholders.md` |
| B2 | Titel von Dr. Stürzl stammen aus ihrem Lebenslauf, nicht aus einem Kammernachweis. | approved-copy.md | Kanzlei bestätigt |
| B3 | Die Live-Seite benutzt Wörter, die dieser Text bewusst nicht übernimmt: "Spezialisierung", "Expertise", "exzellent", "Festpreis", "hart in der Sache". Die Live-FAQ schreibt außerdem "Worst Case Szenario" und "Ihre Freiheit steht auf dem Spiel". Das ist Angst-Wortschatz (Regel LR16) und steht hier nicht. | Live-FAQ, voice.md | Nur Hinweis |
| B4 | Das Stimmprofil `voice.md` ist ein Entwurf. Blog-Beiträge sprechen als "wir" mit Anrede Sie. Die Blog-Regel B4 sieht Ich-Form der Autorin vor. Das hängt an Punkt B1. | blog-rules.md, voice.md | Offen |
| B5 | Rechtsgrenze: Die Beiträge geben allgemeine Information und keine Einschätzung des Einzelfalls (Regel B7). Der Hinweis steht am Ende. | blog-rules.md | erledigt im Text |
| B6 | `schema.jsonld` liegt als Entwurf in `05-final/`. Autorenname und Veröffentlichungsdatum sind darin leer, weil Platzhalter nicht ins Markup dürfen (G6b). Nach der Freigabe Name in `brief.json` (byline) und Datum im Frontmatter eintragen und `schema_tool.py make` neu starten. Das Entwurf-Markup darf vorher nicht live gehen. | schema_tool.py | Offen bis B1 |
| B7 | Adressblock und Telefonnummern im Abschluss stammen aus nap.json (Source of Truth Tab 00). Keine Öffnungszeiten im Schema. | nap.json | bestätigt |

## C. Korrekturrunde 2026-10-11 (REVIEW-G, FIX-G-report.md)

- Sicherung vor der Änderung: `05-final/page-vorreview.md`. Neuer Entwurf: `03-draft/draft-v3.md`, Endfassung `05-final/page.md`.
- Rivalen-Cleanse: nicht gelaufen. Der codex-Aufruf endete mit "usage limit" (Exit 1, Neustart frühestens 17:20 laut Meldung). G5 besteht nur im Lint (5/5). Ein Cleanse-Aufruf ist offen und darf einmal nachgeholt werden (danach `diff_claims.py diff`).
- Die FAQ-Antworten sind Kurzfassungen mit Link auf den Beitrag (Review: Wiederholung der Beitrags-FAQ).
