# Seiten-Scorecard (Kopie je Lauf nach `04-gates/scorecard.md`)

Punkte 0 bis 100. Bestanden ab 85, wenn kein Block-Fehler vorliegt. Block-Fehler = keine Lieferung, egal wie die Summe aussieht. Die Gate-Skripte liefern die Fakten. Der Prüfer-Subagent und Martin vergeben die weichen Punkte.

| Block | Punkte | Prüfpunkt | Wer prüft | Punkte erreicht |
| --- | --- | --- | --- | --- |
| **Textqualität (25)** | 5 | Hook folgt der Regelseite (Ergebnis oder Situation zuerst, kein Wortspiel, kein „Wer wir sind") | Prüfer | |
| | 5 | Schmerz vor Lösung, Weg aus der Lage im selben Abschnitt | Prüfer | |
| | 5 | Ein Haupt-CTA, klarer Text, Beruhigungszeile, Wiederholung alle 2 Abschnitte | Skript + Prüfer | |
| | 5 | Einwände beantwortet (Preis, Vertraulichkeit, Ablauf, Dauer) | Prüfer | |
| | 5 | Scan-Format (kurze Sätze, kurze Absätze) und Elemente statt Textspalte | Skript + Prüfer | |
| **SEO und GEO (20)** | 4 | Eine H1, Title ≤ 60, Meta ≤ 155, Keyword in Title und H1 | G3 | |
| | 4 | Direkt-Antwort-Block, Definition, Entitäten genannt | G3 + Prüfer | |
| | 4 | FAQ aus echten PAA, bestehende FAQ des Kunden erhalten | G3 + Prüfer | |
| | 4 | G6: PAA beantwortet, Direkt-Antwort früh, Informationsgewinn je Vertiefungs-Block, eigene Überschriften, sichtbares Datum, Schema passt zum Text | G6 | |
| | 4 | Interne Links im sichtbaren Text, Anker nennen das Thema (3 bis 8), Link-Netz ohne Keyword-Konflikt | G3 + G6c | |
| | 4 | Wortzahl: nicht unter Bestand, ≥ 70 % Median (Geldseite, Martins Regel nach dem Brasse-Vorfall), Urteil-Satz mit Quelle und Datum | G3 | |
| **Fakten (20) BLOCK** | 10 | Jede Zahl und jeder Claim steht in der Claim-Liste (G1 grün) | G1 | |
| | 5 | Lokaler Fakt echt und mit Quelle (wo Ort Pflicht ist) | Prüfer | |
| | 5 | Offene Kundenfakten sind gelbe Platzhalter, alle in `placeholders.md` | G3 | |
| **Recht (15) BLOCK** | 10 | G2 ohne Block-Treffer, Pflichthinweis da | G2 | |
| | 5 | Graue Zonen aufgelistet und von Martin entschieden | Prüfer + Martin | |
| **Slop und Stil (10) BLOCK unter 5/5** | 5 | G5: 5/5 nach Cleanse, Claim-Diff sauber | G5 | |
| | 5 | G4: keine Gedankenstriche, eine Anrede, keine verbotenen Wörter | G4 | |
| **Lesegefühl (10)** | 4 | Passt zum Stimmprofil (Anrede, Ton, eigene Wendungen) | Prüfer + Martin | |
| | 3 | Pro Abschnitt ein konkretes Detail vom Kunden | Prüfer | |
| | 3 | Satzlänge wechselt, kein gleichförmiger Rhythmus | Prüfer + G5 | |

## Entscheidung

- Summe ≥ 85 und kein Block-Fehler: **liefern** (Checkpoint 2).
- Summe 70 bis 84 oder ein Block-Fehler: **nachbessern**, nur die genannten Abschnitte, Gates neu.
- Summe < 70: **neu schreiben** ab Outline.

## Erfassung pro Lauf

`_run.json` bekommt: `score`, `rounds` (Änderungswünsche von Martin an den Checkpoints), `slop_rounds`, `minutes` (Zeit bis zum geprüften Entwurf), `cost_usd`.
