# Maps growth playbook: Sheet design (client instance)

Status: design only. Nothing is created in Drive without Martin's go. Rules: memory `well-designed-sheets` and `local-seo-sheet-workflow`.
Language: STE here. Sheet labels are German (the client may read the client-safe tabs).

## 1. Build method

- One `.xlsx` file built by `scripts/build_sheet.py` with **XlsxWriter** (never openpyxl, never CSV).
- Upload with Drive `create_file`, mime type xlsx, conversion to a native Google Sheet (leave `disableConversionToGoogleType` unset).
- Location: client folder, subfolder `Maps-Playbook`. Name: `[Maps-Playbook] Matrix <YYYY-MM-DD>`. Old version goes to `_archiv`, never overwritten.
- After upload, open it in Chrome (Claude in Chrome, Martin's session) and take a screenshot of each tab. Check fills, dropdowns, frozen rows, conditional colours, column widths. Report the Drive link and the screenshot as a file.
- Drive MCP cannot write cells. Later edits go through Chrome. The matrix source of truth is `matrix.json`. The Sheet is a view. A hand edit in the Sheet is not evidence.

## 2. Tabs

| Tab | Content | Reader |
| --- | --- | --- |
| `00 Übersicht` | One-page summary (section 4) | Martin, team |
| `01 P1 Google-Profil` | 22 measures | Martin, team |
| `02 P2 Website` | 35 measures | Martin, team |
| `03 P3 Off-Page` | 20 measures | Martin, team |
| `04 Aufgaben` | Ranked task proposals | Martin, team, client after release |
| `05 Evidenz` | Evidence index: every source with date and measure IDs | Team |
| `99 Legende` | Status, colours, age rules, gates, catalogue version | All |

Client-safe release: only tabs `00` (client view without score parts), `04` (approved tasks) and `99`. The internal tabs stay internal. No tool names and no team names in any client-safe cell.

## 3. Pillar tab columns (tabs 01 to 03)

| Col | Header | Width | Content | Validation or format |
| --- | --- | --- | --- | --- |
| A | ID | 7 | `G01` | Bold, frozen |
| B | Gruppe | 20 | Board group | Frozen. Group rows get a light band |
| C | Maßnahme | 34 | German measure name | Frozen, wrap |
| D | Status | 13 | Erledigt, Teilweise, Fehlt, Nicht relevant, Unbekannt | **Dropdown** list. Fill by value (see section 5) |
| E | Befund | 52 | One finding sentence | Wrap, top aligned |
| F | Evidenz | 24 | Short label as link to the evidence | Hyperlink |
| G | Datum | 11 | Newest evidence date | Date `DD.MM.YYYY` |
| H | Alter (Tage) | 9 | Days since evidence | Number. Red font if over the age rule |
| I | Frisch? | 9 | Ja / Nein | Conditional colour |
| J | Konfidenz | 12 | verified, derived, client_stated | Dropdown |
| K | Klasse | 9 | DO, GATE, OUT | Colour: DO green, GATE orange, OUT grey |
| L | Gate | 8 | Gate numbers | Text |
| M | Blocker | 16 | `un-burning`, `client`, measure ID, or `-` | Text |
| N | Nächste Aufgabe | 40 | Task hint | Wrap |
| O | Prio | 8 | Score | Number `0.0`. Heat scale on the column |
| P | Phase | 9 | d1-30, m2+, later | Dropdown |

Frozen panes: header row and columns A to C. Group header rows span all columns (merge). Zebra rows on measure rows.

## 4. Summary tab `00 Übersicht`

Top to bottom:
1. Title row (merged): "Maps-Playbook <Client>, Stand <date>, Katalog <version>".
2. Three tiles: **Erledigt** (share of measures `done`, count), **Lücken** (missing + partly + unknown), **Frische** (share of cells with fresh evidence).
3. Pillar table: for each of P1, P2, P3 and each group: counts per status and a traffic light (green 75 percent done or more, yellow 40 to 74, red below 40).
4. **Top 5 nächste Aufgaben**: rank, measure, action, gate, owner type, effort.
5. **Blockiert**: tasks waiting on un-burning, client or dependency.
6. **Gates offen**: measures with a gate and the proof still missing.
7. Delta (refresh runs): what moved since the last run.
Martin reads sections 1 to 4 in 30 seconds.

## 5. Colours and conditional formats

| Value | Fill | Font |
| --- | --- | --- |
| Erledigt | `#C6EFCE` | `#0B6623` |
| Teilweise | `#FFEB9C` | `#7F6000` |
| Fehlt | `#FFC7CE` | `#9C0006` |
| Nicht relevant | `#E7E6E6` | `#595959` |
| Unbekannt | `#DDEBF7` | `#1F4E79` |
| Header | `#1A1A1A` | white, bold |
| Accent (title, tiles) | `#FAC118` | `#1A1A1A` |

Font: Arial 10. Gridlines off. Thin borders. Header row height 28. Title row merged.

## 6. Task tab columns (tab 04)

Rank | ID | Maßnahme | Aktion | Wer (agent, client, human) | Aufwand (S, M, L) | Risiko | Gate | Prio (score) | Impact | Konfidenz | Phase | Abhängig von | Status (proposed, approved, blocked, in_progress, done, verified) | Batch | Freigabe Kunde (checkbox) | Go Martin (checkbox).
Dropdown on Status. Checkboxes as data validation lists (`Ja`, empty). Sorted by rank. Blocked rows are grey.

## 7. Evidence tab columns (tab 05)

Evidence ID | Typ (live, scan, document) | Referenz (link) | Datum | Alter | Regel (30, 60, 180) | Stützt Maßnahmen (IDs) | Hash | Notiz.
Any cell on tabs 01 to 03 can drill to its row here by the evidence label.

## 8. Checks before delivery

- `validate_run.py` passes (every cell has evidence, date, age).
- Sheet opens as a native Google Sheet. Screenshot of every tab. Colours, dropdowns and frozen panes all work.
- No tool names, no team names, no price in client-safe tabs.
- Drive link and screenshot go to Martin with the message draft.
