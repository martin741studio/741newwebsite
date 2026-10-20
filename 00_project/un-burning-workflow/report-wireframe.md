# Report wireframe — Un-Burning

Status: DRAFT. Rendered prototype: `report-prototype.html`. Language: STE here. Report text in German.
Readers: Martin first, then agents. The client reads only the released client-safe tab.
Low-load rule: Martin must grasp the state in 5 seconds from page 1. Each screen has one question it answers.

## Internal report — structure

1. Page 1: damage map (one screen)
2. Area tables B to E (one table per area)
3. Keep / fix / kill list (the GO-1 view)
4. Companion views: NAP corrections, redirect map, indexed vs intended, link plan
5. Before/after tracker and bedrock check
6. Evidence index (raw data, hashes, refetch calls)

## Page 1: damage map

```
+--------------------------------------------------------------------------------+
| Un-Burning · Praxis Suriya · Lauf 2026-10-11 · Modus scan · Stand: Entwurf     |
+--------------------------------------------------------------------------------+
| FUNDAMENT-CHECK      [B grau] [C rot] [D gelb] [E rot]     0 von 3 bereit |
|                      Wachstums-SEO startet erst, wenn C, D, E grün sind.       |
+---------------------------------------+----------------------------------------+
| SCHADENSBILANZ                        | DIE 5 GRÖSSTEN LECKS                   |
|  offen: 42 Einträge                   |  1 [Umsatz] ...        Bereich C  S    |
|  blockiert Umsatz: 6                  |  2 [Umsatz] ...        Bereich E  M    |
|  kostet Linkkraft: 28                 |  3 [Linkkraft] ...     Bereich D  S    |
|  kosmetisch: 8                        |  4 [Linkkraft] ...     Bereich D  M    |
|                                       |  5 [Linkkraft] ...     Bereich E  M    |
+---------------------------------------+----------------------------------------+
| NÄCHSTE 3 AKTIONEN                    | DEINE FREIGABEN (GO-1)                 |
|  1 ...  wer: 741   Aufwand S          |  12 Einträge warten auf Entscheidung   |
|  2 ...  wer: Kundin Aufwand S         |  [Zur Liste]                           |
|  3 ...  wer: Google Aufwand M         |  3 davon destruktiv (Einzel-Go)        |
+---------------------------------------+----------------------------------------+
| WIRKUNG (Vorher / Nachher)            | DATENLAGE                              |
|  GBP Anrufe · Routen · Klicks         |  Quellen gelesen: 11 von 13            |
|  Indexierte Seiten · 404 · NAP %      |  Nicht lesbar: ...                     |
|  Anfragen pro Woche                   |  Vertrauen: verified 80 % · derived 20 %|
+---------------------------------------+----------------------------------------+
```

Rules for page 1:
- Four lights (B, C, D, E). Ownership and access are no light (onboarding). Grey means "not scanned" or "not applicable". Grey is never green.
- The five leaks are sorted by severity first (`blocks_revenue`), then by effort (S first).
- "Deine Freigaben" shows only what waits for a go. It links to the GO-1 list.
- No score between 0 and 100. The bedrock check is a state, not a number. A number invites false precision.
- Every number on the page links to its table row or evidence.

## Area table (one per area B to E)

Columns: `ID` | Eintrag | Ziel (URL or asset) | Schwere (colour chip) | Aktion | Wer | Aufwand | Status | Vorher → Nachher | Beleg

- Sorted: `blocks_revenue` first, then `leaks_link_power`, then `cosmetic`.
- Row click opens a drawer: why it harms, evidence list, refetch call, rollback step, approval history.
- Status chips: vorgeschlagen, freigegeben, erledigt, abgelehnt, blockiert.
- Filter chips: Schwere, Aktion, Wer, Status.

## Keep / fix / kill list (GO-1 view)

One row per item. Three buttons per row: Behalten, Reparieren, Entfernen, plus Zurückstellen. A destructive row shows a red lock icon: "Einzel-Go nötig".
Header actions: "Alle umkehrbaren Einträge dieses Bereichs freigeben" (reversible class only).
The page stores nothing. It exports `approvals.json`, which Martin hands to the agent. Writing to the register needs Martin's explicit step.

## Companion views

| View | Columns |
| --- | --- |
| NAP corrections | Verzeichnis, URL, Feld, Alt, Neu, Methode, Status, zuletzt geprüft. Footer: NAP-Konsistenz in Prozent |
| Redirect map | Alte URL, Status jetzt, Backlinks, Klicks 90 Tage, Ziel, Grund, Freigabe |
| Indexed vs intended | URL, Klasse, indexiert, gewollt, Urteil, Aktion |
| Link plan | Seite, Elternseite, Content-Links nach oben, fehlende Links (Anker, Ziel) |

## Before/after tracker

Table: Kennzahl | Basis (Datum) | Jetzt (Datum) | Pfeil | Hinweis. Rows: GBP Anrufe, Routen, Website-Klicks (per Woche, 4-Wochen-Fenster); indexierte Seiten; 404-Anzahl; NAP-Prozent; Anfragen pro Woche.
Footer line: "Bewegung kann auch andere Ursachen haben. Verglichen wird nur mit gleichen Zeiträumen."

## Evidence index

Table: Beleg-ID | Typ | Tool | Datum | Hash | Datei | Neu laden (refetch). The page embeds the register as `<script type="application/json" id="un-burning-data">`. An agent reads one page and finds every item.

## Client-safe tab (draft until GO-3)

- Plain German, "du". No tool names, no team names, no cost, no internal severity words.
- Shows: what was found (counts in words), what was fixed (before and after), what is next, what the client does (if anything).
- Hides: items marked `client_safe: false`, evidence hashes, refetch calls, destructive rows before they are done.
- Health clients: no promise of success. HWG check on every sentence.
- Title idea: "Dein Fundament: Was wir bereinigt haben".

## Visual rules

- Colour for state only: green, yellow, red, grey. One accent colour for actions. Never two accent colours.
- One highlight per section. Calm. No animation except a single reveal.
- Desktop first (1440 px). Mobile stacks the cards.
- Light and dark mode via tokens. Text contrast at least 4.5:1.
- Verify in rendered state with a screenshot before delivery.
