# Fact rules

Sources: memory `claims-need-real-data`, `page-content-qa-checklist.md` (Phase 0, 1, 2), `startseite-money-page-standard.md` B, CRO L10.

- F1 Every fact, number, name, address, phone number, price, credential, year, quote and review count is in the claim list (`claims.json`) with a source and a date. The source is a file path, a URL read on that date, or a statement by Martin or the client.
- F2 A fact the data does not hold becomes a yellow placeholder: `[von Kunde bestätigen: Preis der Erstberatung]`. It also goes into `placeholders.md` with the question and who can answer. Never fill the gap with a likely value.
- F3 IF a volume or ranking shows "0" or no data THEN it means no data, not no demand. Say that. Sense-check with autocomplete, PAA, Trends.
- F4 IF the live page and another page disagree on a fact THEN use the newer and safer statement, write the conflict in the placeholder list and in the delivery note. (CRO 4b)
- F5 NAP comes from the locked record only. Never a second variant.
- F6 A local fact in the text (a statistic, an institution, a rule) comes with a source read on that date. "Berlin" in the meta line is not local texture. (QA gate 1.4)
- F7 Word counts come from `wordcount.py`. Never from memory. (A0 point 2)
- F8 Quote the client's text 1:1 where it is good and proven. Improve around it. Never replace a good Bestand section with a worse one. (money-page standard I)
- F9 Competitor text is never a source. Competitors show what readers expect and where the gap is. (pool rule 5)
- F11 **Source of Truth first (Martin, 2026-10-11).** Before any fact is marked open or `[FEHLT]`, read the client's Source-of-Truth Google Sheet. The Drive MCP shows only tab 00 and the structure. Read all tabs with `node ~/.claude/skills/content-writing/scripts/read_sot.mjs <sheet-id> <out.json>` (service account, read only; sheet IDs are in the client memory) and save a text snapshot next to the client's files. Client NAP (address, phone, hours), team, titles, rates and contact people come from there. Pool items marked `needs_client` can be out of date: the sheet wins. A wrong `[FEHLT]` costs Martin's time and makes agents copy the error.
- F10 Method sources (Hormozi and others) are never named in client text. Call it "741 Content-Raster".

## Claim list format `01-brief/claims.json`

```json
{"claims": [
 {"id": "C01", "type": "fact", "text": "Büro in Frankfurt, Untermainkai 26", "source": "GBP, gelesen 2026-10-09", "numbers": ["26"], "must_appear": ["Untermainkai 26"], "required": true},
 {"id": "C02", "type": "credential", "text": "Fachanwältin für Steuerrecht seit 2021", "source": "Lebenslauf Dr. Stürzl, 2026-10-11", "numbers": ["2021"], "must_appear": ["Fachanwältin für Steuerrecht"], "required": false},
 {"id": "C03", "type": "number", "text": "Google 5,0 bei 14 Bewertungen", "source": "Maps, 2026-10-09", "numbers": ["5,0", "14"], "required": false}
]}
```

`type`: fact, credential, number, legal, placeholder. `required: true` means the text must contain every `must_appear` string. The G1 script fails on any number in the text that no claim backs, and on missing required claims.
