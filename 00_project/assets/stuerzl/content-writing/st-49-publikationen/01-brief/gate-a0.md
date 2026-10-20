# Gate A0 (Typ C, Presse- und Publikationsseite): Stürzl, Veröffentlichungen, Vorträge und Presse (ST-49)

Datum: 2026-10-11. Seitentyp C, Modus Neu (kein Bestand für diese Seite). Regel: alle Kundentexte zum Thema, kein Wort-Benchmark. Die Vergleichsmessung ist Information (Gate G6).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth | ja | `source-of-truth-2026-10-11.md` Tab 12 (Expertise und Erwähnungen, 27 Zeilen mit URL und Linkstatus), Tab 00, `nap.json`, 2026-10-11. |
| 2 | Live-Bestand | kein Bestand | Die Seite /publikationen/ gibt es nicht. Verwandter Bestand: Profil Dr. Stürzl (Reiter Publikationen, Vorträge, 520 Wörter Liste) und Aktuelles (338 Wörter, 8 Beiträge). `_work/live/`. |
| 3 | Alle Kundentexte zum Thema | ja | Live-Profil Dr. Stürzl, Lea Wimmer, Dr. Glogger, Aktuelles (8 Beiträge einzeln gelesen: `_work/live/art-*.txt`), `client-baseline.md` Abschnitt 4 (Presse: 15 Erwähnungen ohne Link). Pool CP-AUT-004 und CP-AUT-003. |
| 4 | Quellen geprüft | ja | Mehr als 20 externe Quellen abgerufen (`_work/ext/`): HTTP 200 und Erwähnung bestätigt: JUVE (2), LTO (3), ZRI, RWS, azur, Private Banking Magazin, C.F. Müller Newsletter 34, Fürstenberg, Peter Lang, IWW-Kongress. Nicht prüfbar: capital.de und anwalt.de (HTTP 403), R&W (Seite lädt Inhalt per Skript, nur Titel lesbar), Spotify (kein Text), Otto Schmidt (HTTP 404), BMF-PDF (HTTP 503), LinkedIn (HTTP 999). |
| 5 | Keyword und Volumen | keins | Kein Rankingziel. Der Pool nennt 11 von 19 Wettbewerbern mit Presse- oder Publikationsbereich (58 %, Tischvorlage, `pool.json` CP-AUT-003). |
| 6 | PAA | nicht nötig (Typ C) | Brief: `paa_questions: []`. |
| 7 | Vergleichsmessung (nur Info) | ja | 10 von 10 Seiten gelesen, Median **756** Wörter (Ausreißer: hortmannlaw.com/articles mit Artikelliste). `_work/bench-metrics.json`. |
| 8 | Lokaler Fakt | nicht nötig | Keine Ortsseite. |

## Vergleichsmessung (Info)

| Wörter | Seite |
| --- | --- |
| 10585 | https://www.hortmannlaw.com/articles |
| 1384 | https://wild.legal/news/ |
| 1101 | https://www.dr-buchert.de/aktuelles/ |
| 871 | https://www.drburkhard.de/vortraege-von-dr-joerg-burkhard-im-2-halbjahr-2016/ |
| 826 | https://www.mtrlegal.com/news/ |
| 686 | https://rae-sus.de/ausgewaehlte-publikationen-und-vortraege/ |
| 489 | https://www.drburkhard.de/aufsaetze-dr-burkhard-2016/ |
| 312 | https://steuerdelikt.de/medien |
| 248 | https://www.anwalt-steuerrecht-frankfurt.de/presse/ |
| 95 | https://www.dnk-rechtsanwaelte.de/de/veroeffentlichungen/ |

## Wortzahl-Urteil

Kein Bestand. Wettbewerber-Median 756 (Info). Zielkorridor 400 bis 1.800. Die Seite besteht aus belegten Listeneinträgen (Titel, Jahr, Quelle), kein Füllmaterial.

## Konflikte

1. Live-Profil: „erscheint 2024“ bei Heidelberger Kommentar und Steuerstrafrecht A-Z. Status offen, Platzhalter.
2. Aktuelles-Beitrag zum Webinar (Otto Schmidt): Link liefert 404, Rolle von Dr. Stürzl steht nicht im Beitrag. Platzhalter.
3. Vortragstitel im IWW-Beitrag und Titel von Veröffentlichungen enthalten Gedankenstriche oder „Spezialisierung“: im Text ersetzt oder umschrieben (OPEN-FLAGS.md).
4. Gate G2 liest „Nr. 1“ in einem Gesetzeszitat als Superlativ: ein Titel (OWiG-Anmerkung) bleibt deshalb draußen (OPEN-FLAGS.md, Vorschlag für den Skill).

## Gate-Ergebnis

Alle Pflichtzeilen für Typ C vorhanden. Keine Blocker. Fallbeispiele (ST-50) nicht geschrieben (keine Daten).
