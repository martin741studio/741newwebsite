# Report design — wireframe (DRAFT)

Status: wireframe for Martin's checkpoint 1. The rendered HTML prototype comes after his "go". I will check it with a screenshot in Chrome (rule: verify UI in rendered state).
Language: this file is STE. The report itself uses German labels and findings. Field names stay English.

## Contents

1. Low-effort rules
2. Page 1: "Auf einen Blick"
3. Block detail layout
4. Raw data layout
5. Client-safe version
6. Agent layer
7. Visual rules

## 1. Low-effort rules (what "little cognitive energy" means)

1. Page 1 answers three questions in 30 seconds: Where are we? Is it winnable? What do we do first?
2. Status before numbers. Color, icon and word together (never color alone).
3. Maximum 5 items in any list. More items go behind "Alle anzeigen".
4. Every block uses the same layout. The eye learns it once.
5. One sentence per finding. "Warum wichtig" is one more sentence, hidden until opened.
6. Detail is collapsed by default. Raw data is one click further.
7. Every number shows its source and date as a small badge. The badge opens the evidence.
8. No tool names and no jargon without a plain word next to it ("SoLV" shows as "Maps-Sichtbarkeit (Top-3-Fläche)").

## 2. Page 1: "Auf einen Blick" (internal)

```
┌────────────────────────────────────────────────────────────────────────────┐
│ STÜRZL Steuerstrafrecht · Kickoff-Audit · 12.10.2026 · Datenlage 86 %      │
├───────────────────────────┬────────────────────────────────────────────────┤
│  MAPS-READINESS           │  EIGNUNG:  ● NOCH NICHT                        │
│        42 / 100           │  "anwalt steuerstrafrecht": Marktführer hat    │
│  ▲ +6 seit Vorlauf        │  82 Bewertungen, ihr habt 14. Lücke 150        │
│  (Deckel 50: Risiko B13)  │  Bewertungen = 37 Monate bei 4 pro Monat.      │
├───────────────────────────┴────────────────────────────────────────────────┤
│ WO WIR STEHEN (Top-3-Fläche je Suchbegriff)                                │
│  anwalt steuerstrafrecht   ▓░░░░░░░░░  2 %    Leader: Dreyenberg 62 %      │
│  anwalt steuerhinterziehung▓▓▓▓▓▓░░░░ 63 %    Leader: —                    │
│  steuerfahndung anwalt     ▓▓░░░░░░░░ 22 %    Leader: Hepp 57 %            │
├────────────────────────────────────────────────────────────────────────────┤
│ 13 BLÖCKE                                                                  │
│ [B05 ● rot  ] [B10 ● gelb] [B11 ● rot ] [B06 ● gelb] [B07 ● gelb]          │
│ [B13 ● rot  ] [B12 ● gelb] [B04 ● grün] [B01 ○ offen][B02 ○ offen]        │
│ [B03 ○ offen] [B08 ○ offen][B09 ○ offen]                                   │
│  Klick = springt zum Block. Tipp: Block = Ampel + 1 Satz.                  │
├────────────────────────────────────────────────────────────────────────────┤
│ DIE 3 ERSTEN AKTIONEN                       Wirkung  Aufwand  Wer          │
│  1 Neue Adresse in Profil und Website angleichen●●●●●    S      741 (Go)    │
│  2 Bewertungs-Prozess nach Mandat starten     ●●●●○     M      Kunde       │
│  3 Zweite Kategorie ergänzen                  ●●●○○     S      741 (Go)    │
├────────────────────────────────────────────────────────────────────────────┤
│ ROTE FLAGGEN (max. 5)         │ WAS FEHLT (Eingaben offen)                 │
│  ⚑ Adresse umgezogen, GBP     │  ○ Formular: 6 von 9 Blöcken beantwortet   │
│    nicht aktualisiert (B13.02)│  ○ GSC-Zugang fehlt (B06.06)               │
│  ⚑ Anrufzeiten 09:30-14:30    │                                            │
│    (B09.03)                   │                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

Sample values only. Reviews and shares come from Stürzl data of 17.09. and 01.10. Score, trend and flags are invented to show the layout. They are not findings.

Rules for page 1:

| Element | Source | Rule |
| --- | --- | --- |
| Score + coverage | `audit_runs` | Always both numbers. Cap note shows only when the cap applies |
| Trend | `audit_run_deltas` | Shows only when the last run is comparable |
| Verdict | B09.04 | One sentence with keyword, leader, gap and months (section 5.3 of the spec) |
| Top-3-Fläche per keyword | B05.06 | Bar + number + leader. Priority 1 keywords only |
| Block tiles | Block scores | Ampel + one sentence on hover or tap. Grey tile for "offen" |
| 3 first actions | `audit_actions` | Sorted by impact, then effort. Max 3 |
| Red flags | Findings with `critical` and red | Max 5 |
| Missing inputs | `unknown` findings | Max 5, with who must give them |

## 3. Block detail layout (same for all 13)

```
┌─ B05  Google-Profil & lokale Rankings ───────────── ● ROT  (Score 31 / 100) ┐
│ Kernaussage: Das Profil wird zu selten bewertet, der Marktführer ist weit   │
│ voraus.                                                                     │
│ ▸ So kommt Platz 1: Lücke zum Marktführer  [Bewertungen −68] [Kategorien −2]│
├──────┬────────────────────────┬────────┬───────────────┬───────────┬───────┤
│ ● ID │ Feld                   │ Wert   │ Referenz      │ Quelle·Datum│ Mehr │
├──────┼────────────────────────┼────────┼───────────────┼───────────┼───────┤
│ ● .03│ Bewertungstempo        │ 2/90 T │ Leader 9/90 T │ [Maps·11.10]│  ▸   │
│ ● .06│ Maps-Sichtbarkeit      │ 2 %    │ Leader 62 %   │ [Scan·11.10]│  ▸   │
│ …                                                                           │
└──────┴────────────────────────┴────────┴───────────────┴───────────┴───────┘
 ▸ geöffnet: Warum wichtig (1 Satz) · Nächster Schritt · Wer · Aufwand
              · Rohdaten-Link · "Tiefer prüfen" (kopiert Agent-Befehl)
```

Rules:

- The block header shows Ampel, name and score. The score shows only for data blocks. Business-fit blocks show Ampel and "Datenlage".
- "So kommt Platz 1" shows only in B05, B10 and B11. It lists gaps to the leader as numbers.
- A row opens to: why it matters, next step, owner, effort, evidence link, and a copy button "Tiefer prüfen" with the `refetch` call and `drilldown_hint`.
- Grey and unknown rows stay visible with a reason ("Zugang fehlt", "Kunde hat nicht geantwortet").
- B11 shows the competitor table as the first element (one row per competitor, leader highlighted).

## 4. Raw data layout

Last section of the page: "Rohdaten".

| Part | Content |
| --- | --- |
| Evidence index | Table: id, kind, tool, date, cost, hash, file link |
| Keyword table | Keyword, priority, volume, source, per-platform values |
| Competitor table | Full set |
| Cost | Euro and credits, against the caps |
| Run meta | Mode, depth, parameters (grid, radius), catalog version, previous run |

## 5. Client-safe version (`client.html`, draft until Go-C)

| Included | Excluded |
| --- | --- |
| Page 1 without verdict, cost and internal flags | Fit verdict (B09), cost, caps |
| Block tiles for B04-B07, B10-B13 | Business-fit blocks B01-B03, B08, B09 |
| Gaps to the market leader (numbers) | Tool names, team names, offer price |
| Top actions with "Wer" = "741" or "Ihr Team" | Findings with `client_safe = false` |
| Source badges as "Google-Daten, 11.10." | Raw evidence index |

Language: normal German prose. Address form from the client record. Layout reuses the existing portal report style (741 CI, DM Sans, `#fac118`). Release adds a `client_reports` row only after Go-C.

## 6. Agent layer

- Every row has `data-field-id`, `data-status` and `data-evidence`.
- The page embeds `<script type="application/json" id="audit-data">` with all findings, keywords and competitors.
- The button "Tiefer prüfen" copies: field id, refetch call, drilldown hint and the evidence path. An agent starts from there.
- The page shows the run id and the catalog version in the footer.

## 7. Visual rules

- Desktop first. Check mobile width after.
- Four status colors with icon and label: green ●, yellow ●, red ●, grey ○. Contrast at least 4.5:1.
- One highlight per section. No motion except open and close of rows.
- Light and dark theme. Print stylesheet for PDF export (page 1 on one A4 page).
