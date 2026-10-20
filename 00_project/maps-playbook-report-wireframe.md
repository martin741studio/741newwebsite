# Maps growth playbook: report wireframe

Status: design. The rendered prototype is `maps-playbook-skill/maps-playbook/assets/board-prototype.html` (built from the Suriya dry run). Style: 741 CI (yellow `#FAC118`, DM Sans, Anton for big numbers) as in the week-1 report.
Two versions: **internal** (Martin and team, all columns) and **client-safe** (released only at Checkpoint B).

## 1. Internal board, page 1 (30-second read)

```
+--------------------------------------------------------------------------------+
| MAPS-PLAYBOOK  <Client>  ·  Stand <date>  ·  Katalog 0.1.0  ·  Modus kickoff    |
+--------------------------------------------------------------------------------+
| ERLEDIGT  xx %   |  LÜCKEN  nn   |  FRISCHE  yy %   |  GATES OFFEN  g   |  BLOCKIERT b |
+--------------------------------------------------------------------------------+
| PILLAR TABLE                                                                   |
|  P1 Google-Profil    [bar: done | partly | missing | n/a | unknown]  ●ampel      |
|   Profil-Fundament · Kategorien · Bilder · Beiträge · Bewertungen · Abwehr      |
|  P2 Website          [bar] ●                                                    |
|  P3 Off-Page         [bar] ●                                                    |
+--------------------------------------------------------------------------------+
| TOP 5 NÄCHSTE AUFGABEN (by score)                                              |
|  1 G06 Primärkategorie   Prio 4.2   agent+client   S   Gate -   d1-30           |
|  ...                                                                           |
+--------------------------------------------------------------------------------+
| KONFLIKTE & LÜCKEN IM BEWEIS (conflicts between sources, stale, missing access) |
+--------------------------------------------------------------------------------+
| CHECKPOINT A: Korrekturen [ 0 ]   [ Freigabe für Aufgaben-Plan ]                |
+--------------------------------------------------------------------------------+
```

Rules:
- Five tiles on top. One number each. No chart junk.
- Pillar bars show the five statuses in the colours of the Sheet design. Traffic light uses done share: green 75 percent or more, yellow 40 to 74, red below 40.
- Top 5 tasks come from `tasks.json`. A blocked task never shows here.
- The conflict box lists source conflicts and stale cells with the first fix step.
- Every number links to its detail (anchor to the pillar view).

## 2. Pillar view (one per pillar)

- Group sections in board order. Each section is a table: ID, measure, status chip, finding, evidence chip, date, age, class, gate, next task.
- Evidence chip opens the evidence panel: type, reference, date, note. This is the drill from cell to raw evidence.
- Filter chips: status, class (DO, GATE, OUT), phase, blocked.
- Gate measures show an orange gate badge. The badge text is the gate rule in one line.
- Stale cells show a clock icon and `Unbekannt (alt)` with the old status in grey.

## 3. Task view

Ranked table with score parts (impact, confidence, effort, risk), owner type, phase, dependency, state. Blocked tasks sit in a separate band with the blocker. Batch builder: tick tasks, see the batch cost and gate list, copy the batch summary for Checkpoint C.

## 4. Client-safe bundle (draft until Checkpoint B)

Page order: Was wir gefunden haben (plain-language status per group, traffic light) · Was wir als Nächstes vorschlagen (tasks in client words, with the effort in days) · Was wir von dir brauchen (photos, review asks, decisions, access) · Freigabe (checkbox per task group and "Alles freigeben", feedback to the report feedback table as in the week-1 report) · So messen wir (monitoring rhythm, no tool names).
Rules: no tool names, no team names, no internal score, no fit verdict, no price. "du" for du clients. HWG check on every text for health clients. Gate measures appear only as a plain sentence ("Das klären wir zuerst mit dir").

## 5. Prototype checks

- Render in Chrome at 1440 px. Screenshot of page 1, one pillar view, and the task view.
- Check: five tiles, three pillar bars, top 5 list, conflict box, evidence chip opens.
- Check: no horizontal scroll, text readable, status colours match the Sheet design.
- Mobile is not required (desktop-first for internal views).
