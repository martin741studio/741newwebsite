# Gate report 2026-10-11
Page: `page.md`. Result: **PASS**

| Gate | Result | Findings |
| --- | --- | --- |
| G1 facts | PASS | none |
| G2 legal | PASS | none |
| G3 seo | PASS | none |
| G4 style | PASS | none |
| G5 slop (lint) | PASS | none |
| G6 seo/geo coverage + schema | PASS | none |

## Warnings

- G4 style: 1 Sätze über 28 Wörter (zum Beispiel: „Besonders beeindruckt hat mich der Praxisteil, in dem wir freie Reden...)
- G4 style: Sprecher gemischt: ich 17, wir 6
- G6 seo/geo coverage + schema: [Hinweis] Begriffs-Abdeckung 72 % (40 Begriffe aus mindestens 50 % der Seiten). Fehlen: präsenz, zuhörer, stimme, coaching, übungen, umgang, grundlagen, inhouse, workshops, sicherheit, mitarbeiter. Pflicht nur, wenn die Suchabsicht den Begriff braucht.
- G6 seo/geo coverage + schema: Direkt-Antwort hat 6 Sätze (Regel: 2 bis 4, etwa 50 Wörter). Kürzen für KI-Zitate.

## Wortzahl-Urteil
Wortzahl 1.827 (wordcount.py, `05-final/page.md`): über dem Bestand (1.787 Wörter ohne Dubletten, `_work/bestand-dedup.txt`) und über 70 % des Wettbewerber-Medians (1.747 Wörter aus 12 Seiten, `_work/bench-metrics.json`), Stand 2026-10-11. Urteil: ausreichend.

## Antworten auf die Hinweise
- Satz über 28 Wörter: Bewertungszitat (Michael B.), Wortlaut bleibt.
- Sprecher gemischt: „ich“ kommt aus Zitaten von Teilnehmern und Michael, der Seitentext selbst ist dritte Person + „wir“.
- Begriffs-Abdeckung 72 %: Inhouse, Workshops, Coaching, Mitarbeiter sind kein Angebot der Startseite oder nicht belegt (OPEN-FLAGS F11). Präsenz, Stimme fehlen bewusst (keine Quelle für eine Aussage).
- Direkt-Antwort 6 Sätze: der Block selbst hat 4 Sätze (44 Wörter); das Skript zählt die Beweis-Punkte und das Zitat der Beweis-Leiste mit.

## Slop-Schleife und Review
- Rival-Modell-Cleanse (GPT über codex), Runde 1: `cleanse-decision.md` (2 Änderungen übernommen, 6 abgelehnt wegen freigegebener Kunden-Zeilen). diff_claims PASS.
- Frischer Reviewer + SEO-Audit: Runde 1 73,5/100 (26 Lücken), Runde 2 92,5/100, keine BLOCK-Fehler, Entscheidung „liefern“. Alle Runde-2-Punkte N1 bis N9 behoben (draft-v5 = page.md). `review-1.md`.
- Offene Schema-Punkte: JSON-LD wird im Prototyp von Hand gebaut (Person, EducationalOrganization mit Adresse, EducationEvent je Termin, ohne Preis).
