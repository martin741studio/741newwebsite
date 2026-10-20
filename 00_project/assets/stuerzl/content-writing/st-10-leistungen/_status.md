# Status: ST-10 Leistungen (Hub)

- [x] Step 0 Readiness: Pool-Item CP-SVC-001, Typ C, BRAO, Stimme. Keine Blocker.
- [x] Step 1 Stimme: voice.md wiederverwendet (Sie, wir).
- [x] Step 2 Brief und Gate A0 (Typ C): `01-brief/`
- [x] Step 3 Outline: `02-outline/outline.md` (Go für den Batch von Martin, 2026-10-11)
- [x] Step 4 Entwurf: `03-draft/draft-v1.md`, `draft-v2.md`
- [x] Step 5 Gates G1 bis G6: PASS (`04-gates/gates.md`)
- [x] Slop-Schleife (erste Runde): Lint 5/5, 1 Cleanse-Aufruf, Diff bestanden
- [ ] Step 6 Reviewer: nicht von diesem Agenten (Hauptagent nach dem Batch)
- [x] Step 7 Paket: `05-final/`
- [ ] Checkpoint 2: Martins Freigabe offen. Nichts live, kein Upload.

## Korrekturrunde nach REVIEW-B (2026-10-11)

- [x] Sicherung: `05-final/page-vorreview.md`
- [x] Entwurf: `03-draft/draft-v3.md`, Paket neu gebaut (page.md, cms-blocks.txt, placeholders.md, schema.jsonld, measure-plan.md)
- [x] Gates G1 bis G6: PASS (`04-gates/gates.md`)
- [ ] Cleanse: nicht möglich. Zwei Versuche (ST-11, ST-13) scheiterten am codex-Limit ("usage limit"). G5 gilt als Lint 5/5, ohne Rivalen-Modell. Nach dem Limit: ein Cleanse-Aufruf je Seite und `diff_claims.py diff`.
- [x] Bericht: `FIX-B-report.md`
- [ ] Checkpoint 2: Martins Freigabe offen. Nichts live, kein Upload.
