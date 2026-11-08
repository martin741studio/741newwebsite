# Claude-Setup-Audit 08.11.2026: Streichliste

Maßstab: Anthropic, „The new rules of context engineering for Claude 5 generation models" (24.07.2026) und Claude-Code-Docs (memory, skills, costs). Prüfung durch 5 Subagents, read-only. Nichts ist geändert.

## 0. Zusammenfassung

| Baustein | Bestand | Löschen | Zusammenlegen | Kürzen/Aufteilen | Behalten | Unsicher |
|---|---|---|---|---|---|---|
| CLAUDE.md (3 Dateien, 174 Z.) | 174 Zeilen | ~110 Zeilen (ganze ~/CLAUDE.md + Dubletten) | 6 Abschnitte | 4 Abschnitte verschieben | ~40 Zeilen | – |
| Memory | 329 Dateien | 68 | 71 → ~35 Zieldateien | 12 große Dateien kürzen | 177 | 13 |
| Skills | 42 (35 Projekt, 10 User, 3 doppelt) | 6 + 3 Dubletten | – | 15 kürzen, 8 aufteilen | 10 | – |
| Job-Descriptions | 5 Dateien + 4 platzierte Kopien | 1 Draft + 5 Roster-Ghosts | – | 4 auf je 1 Seite | – | – |
| Hooks | 6 aktiv + 3 global | 0 | – | README + Docstrings aktualisieren | 6 | – |

Immer geladener Kontext heute: ~64 KB (CLAUDE.md 11,6 + Skill-Descriptions 31,6 + MEMORY.md 20,4). Nach Umsetzung geschätzt ~30 KB. MEMORY.md liegt heute bei 82 % des 25-KB-Hard-Limits.

Sicherheitsbefund (sofort, unabhängig vom Rest): Klartext-Passwörter, Keys oder Bankdaten in 9 Memory-Dateien. Memory wird in jede Session und in Transkripte geladen. Werte nach `.secrets/` verschieben, in der Memory nur der Pfad.

- `huewel-client.md` (Passwort) · `maria-brasse-client.md` (Passwort) · `dumann-client.md` (Passwort) · `client-portal-infra.md` (Passwort Coralie)
- `741-circle-community.md` (x-lead-secret) · `garmin-741-watchface.md` (Calendar-Key `k=`) · `smartlead-cold-email.md` (API-Key, Plan abgelaufen)
- `coldemail-sending-infra.md` (IBAN) · `gayo-employment-contract.md` (NIK, Bankdaten)

## A. CLAUDE.md

### A1 `~/.claude/CLAUDE.md` (28 Zeilen, global)
- Questions = grill-me → **mit Pre-send-Sweep zu einem Abschnitt zusammenlegen** (gleiche Regel).
- Pre-send-Sweep → **behalten, auf 3 Zeilen**. Hook `presend_sweep_hook.py` fängt Überschriften, Schlussfragen, Schrittlisten. Prosa nur noch für „versprochen, nicht geliefert".
- Login-Vorbereitung → **behalten**. Memory `open-login-tab-first.md` löschen (Dublette).
- Vorab-Bestätigung → **behalten, kürzen**. Widerspruch auflösen: Block endet mit „Go?", Text sagt „ich warte nicht". Vorschlag: „Go?" streichen.
- E-Mails → **behalten**. Memory `email-sending-airmailer.md` löschen (Dublette).

### A2 `~/CLAUDE.md` (69 Zeilen) → **komplett löschen**
Beschreibt `/weekly-checkin` und `/daily-checkin`. Beide existieren als `~/.claude/commands/*.md` und enthalten den Ablauf selbst. Letzter Journal-Eintrag 16.09.2025. Nennt „741 Digital Solutions LLC". Lädt heute in jeder 741website-Session mit.

### A3 `741website/CLAUDE.md` (78 Zeilen)
| Abschnitt | Urteil |
|---|---|
| STE: 7 Regel-Bullets | LÖSCHEN. Modell kennt ASD-STE100. Einzeiler + E-Mail-Ausnahme bleiben. |
| Slop: „jeden Text prüfen" | LÖSCHEN (zu breit; Hook prüft nur ```text-Blöcke). |
| Slop: deslop-Pfade, cleanse-Schleife | VERSCHIEBEN in Skill `slopmonster`. |
| Slop: „Nachrichten in ```text-Block, • und 1." | BEHALTEN (Hook hängt daran). |
| Pre-send-Sweep | LÖSCHEN (Dublette zu ~/.claude/CLAUDE.md + Hook). |
| Supabase-Tabellenliste | LÖSCHEN (per `list_tables` ableitbar). Die 3 Fallstricke (GSC vorhanden, meta_campaigns = Agentur, v_paid_campaigns) BEHALTEN. |
| WP Text-Boxen | BEHALTEN auf 2 Zeilen, Begründung löschen. Memory `no-html-in-client-edit-fields.md` löschen, deren Ausnahmen hier eintragen. |
| Client Roadmap Pre-Flight | VERSCHIEBEN in Skill `client-roadmap` (Description). Liste korrigieren: Kisser hat kein roadmap.json, Hüwel/Dumann/Bali/Kamil fehlen. |
| Body-Copy nur via content-writing | BEHALTEN auf 2 Zeilen. Registry-Verify in Skill `content-writing`. **Tote Referenz:** Skill heißt `content-writing`, nicht `content-writing-workflow`; `/content-write` existiert nicht; „auch mid-session aufrufen" ist unmöglich (`disable-model-invocation: true`). |
| Struktur via /cro-homepage | ZUSAMMENLEGEN mit Memory `pages-always-via-cro-workflow.md` (ein Ort). |

## B. Memory (329 Dateien)

### B1 LÖSCHEN (68)
**Dublette zu CLAUDE.md (8):** ai-slop-check-everything · email-sending-airmailer · message-format-copy-safe · no-html-in-client-edit-fields (Ausnahmen retten) · open-login-tab-first · open-questions-as-grill-cards · questions-as-grill-me · supabase-marketing-data-sources · client-roadmap-workflow

**Dublette zu einem Skill (22):** agent-job-descriptions-workflow · agent-team-setup · automation-build-workflow · backlink-dach-workflow (Suriya-Linkkauf-Regel vorher nach praxis-suriya-client) · booking-sequence-workflow · canary-workflow · captions-workflow · client-access-lockout-workflow · collab-content-reciprocal-link-bug · collab-content-workflow · content-format-board-workflow · content-pool-workflow · cro-desktop-first-assets · cro-drive-home-resume · cro-motion-spec · cro-registry-desktop · cro-track-b-design-intense · cro-visual-check-gate · cro-workflow-tooling · maps-audit-review-numbers-from-google-account · maps-audit-workflow · maps-playbook-workflow · marketing-grill-workflow · outlier-content-needs-real-transcript · personal-posts-workflow · prospect-mini-workflow · sales-call-prep-workflow · sales-pitch-workflow · tracking-workflow · un-burning-workflow · workflow-build-knowledge-base-step

**Veraltet / erledigt (17):** 741studio-cro-track-b-pilot · bali-data-readiness-2026-10-13 · client-approval-workflow · ftp-deploy-stray-public-html (Fix in upload.js) · huewel-banerji-subtitles · internal-linking · linux-repo-clone-transfer · malware-pause-2026-10-15 · night-shift-agent (RETIRED) · only-inside-cms-build (Hüwel auf GitHub Pages) · prospect-batch-2026-08-04 · review-page-anchor-overlap-fixed-sitewide · review-page-fast-workflow · review-page-hero-video-and-risk-reversal · review-page-proof-hover-about · review-page-proof-wall · session-state-2026-08-06 · smartlead-cold-email

**Generisch, macht Claude 5 ohnehin (8):** claims-need-real-data (Preisausnahme nach 741studio-pricing) · feedback-calc-chat-no-messages · findability-fallback-search · morning-grill-read-before-write-shared-files · own-answer-needs-direct-followup · stuerzl-backlog-no-implement · verify-blocks-against-source · verify-workflow-build-status · website-security-checklist

Abweichung von den Prüfern: `always-give-drive-link` bleibt (Martins wiederholte Korrektur, kurz).

### B2 ZUSAMMENLEGEN (71 → Zieldateien)
| Ziel | Quellen, die hineingehen |
|---|---|
| client-reply-first-in-response | always-full-message-draft · deliver-messages-ready · feedback-always-draft-the-message · feedback-draft-complaint-message-first |
| chrome-use-existing-window-with-groups | always-external-chrome-browser · api-access-priority · browser-before-handing-back-to-martin |
| read-source-of-truth-first | check-source-of-truth-before-asking · client-markup-screenshots-are-source · client-questions-verify-first |
| morning-grill-workflow | goals-data-architecture · grill-verify-live-chat-before-carding · morning-grill-automation-disabled · morning-grill-cards-show-content-inline · morning-grill-single-source-of-questions · show-content-before-decision-card |
| review-page-must-haves | review-page-closing-cta · review-page-hero-size |
| review-page-standard-template-only | review-page-site-chrome-required |
| loom-embed-always-with-message | loom-video-no-extra-deploy-step · message-before-deploy (**Widerspruch klären: Nachricht vor oder nach Deploy**) |
| approval-card-preview-url | client-textdraft-delivery · feedback-drafts-link-only |
| client-portal-infra | client-dashboard-redesign · client-work-view · kundenarbeit-admin-card-actions |
| collab-content-partner-rules | collab-content-partner-discovery-not-cold-search · collab-content-relationship-first-phasing |
| huewel-repo-ai-rules | huewel-site-workflow · huewel-website-live-state |
| newsletter-backend | huewel-newsletter-build |
| go-gate-hook-needs-typed-go | no-website-changes-without-go |
| never-use-martin-private-google-account | always-check-741studio-google-account · verify-google-account-first |
| balihealing-local-seo | bali-client-facts-2026-10-13 · balihealing-cleanup-before-website-pitch |
| 741studio-tracking-consent | 741studio-analytics-conversions |
| google-ads-api-access | google-reporting-api-access |
| gayo-employment-contract | gayo-unit-economics |
| link-library-local → neu „libraries-local" | hormozi-library-local · seo-library-local · seo-knowledge-base · workflow-library-local · cro-library-local |
| startseite-money-page-standard | page-content-qa-checklist · seo-page-optimization-playbook-doc |
| pages-always-via-cro-workflow | service-pages-full-cro-workflow-each |
| topic-grill-needs-external-research | post-content-grill-before-drafting · grill-only-when-asked |
| program-deliverable-rules | week1-playbook |
| video-edit-workflow | video-edit-first-real-run |
| video-message-transcript-and-email-ask | review-page-loom-talk-track |
| verify-ui-in-rendered-state | review-page-check-after-reveal |
| seo-tooling-dataforseo | sensecheck-keywords-google |
| review-scan-show-the-gap | keyword-must-match-service |
| drive-socials-martin-folder-ids | personal-posts-drive-folder |
| revenue-model-not-for-stuerzl | revenue-model-100k |
| sidebar-client-group-emojis | sidebar-client-emoji-convention |
| page-swap-never-edit-live | suriya-conversion-paths-must-stay |
| no-tool-names-in-client-messages | no-method-sources-in-deliverables |
| no-unnecessary-client-questions | no-own-questions-in-messages |
| no-booking-link-in-messages | message-links-https |
| meta-lead-attribution-gap | meta-ads-live-tab |
| mymia-woman-society-project | mymia-woman-society-wait-for-mia-design |
| marcel-rosenbach-client | marcel-message-in-martin-voice |
| kamil-physio-client | kamil-novamira-connections |
| dumann-client | dumann-ueber-mich-page |
| body-copy-only-via-content-writing | content-writing-workflow (nur Stimmregel retten) |
| content-writing-worktree-root-bug | content-writing-schema-tool-no-hub-type |
| 741-post-design-standard | content-loop-vidiq-outliers |
| coldemail-sending-infra | smartlead-cold-email (Abmahnung-Lehre) |
| empowering-therapists-benchmark | frontend-offer-examples |

### B3 KÜRZEN (große Kundendateien auf Ist-Stand, Chronologie raus)
praxis-suriya-client (94 KB, 12 tote Pfade) · maria-brasse-client (61 KB) · marcel-rosenbach-client (38 KB) · huewel-client (19 KB) · johnijayamotor-client (12 KB) · anja-stuerzl-client · dumann-client · franziska-rabenmuetter-client · citations-listings-module · pauspapier-michael-ehlers · morning-grill-workflow (Changelog D1–D37) · php2shell-2026-10-server-status

### B4 UNSICHER (13, Martins Entscheidung)
741studio-kicms-landingpage · dev-vps-setup-plan (Plan 23.07., nie umgesetzt) · empowering-therapists-benchmark · huewel-onlyinside-ersatz · hwg-fallstudien-guideline · local-seo-sheet-workflow · marketing-quarter-campaign (endet ~09.11., Owner „Maya" ≠ roster) · night-shift-server-workflow · stipendium-giveaway-page (Ziehung vorbei) · story-automation-system (seit Aug offen) · suriya-elementor-dinakar-set · team-outreach-area · wp-incident-2026-10-20-kisser-physiokraft (Lektionen extrahieren, Log löschen)

### B5 Tote Referenzen in BEHALTEN-Dateien (Pfad korrigieren oder Zeile streichen)
portal-leads-crm · praxis-suriya-client · startseite-money-page-standard · stuerzl-local-falcon-keywords · stuerzl-source-of-truth-sheet · suriya-baseline-tracking · suriya-online-bereich · workflow-create-skill · huewel-repo-ai-rules · joomla-search-and-hosting-lessons · joomla-sppb-page-build-recipe · live-content-audit-before-page-swap · offer-pdf-workflow (Preis 3.699 € veraltet → 4.999 €) · anja-stuerzl-client · client-structure-page-playbook · dumann-client · feedback-german-customer-facing · franziska-rabenmuetter-client

## C. Skills (42)

### C1 LÖSCHEN (6)
archify (Fremdpaket, 16 KB, nirgends referenziert) · claudex-loop · claudex-route (Modellliste Sep 2026 veraltet) · codex-build · codex-review (Alias-Stubs) · night-shift (RETIRED)

### C2 DUBLETTEN auflösen (3)
- backlink-dach: Projektkopie behalten, `~/.claude/skills/backlink-dach` löschen (nur Frontmatter weicht ab).
- cro-homepage: identisch; User-Kopie nutzt `~/.claude`-Pfade → **Projektkopie löschen**, User-Kopie behalten.
- cro-track-b: identisch → Projektkopie löschen.

### C3 AUFTEILEN (>8 KB, Rest nach references/) (8)
personal-posts 19 KB (~55 % raus) · morning-grill 19 KB (~60 %; Quellkopie in 00_project veraltet) · content-format-board 15 KB (Description −60 %) · cro-homepage 14 KB (~40 %) · collab-content 13 KB (~40 %) · booking-sequence 10 KB (~35 %) · maps-playbook 10 KB (~40 %) · un-burning 10 KB (~35 %)

### C4 KÜRZEN (Beispiele, Do-NOT-Listen, Basiswissen raus) (15)
citations-dach 50 % · maps-audit 40 % · seo-page-optimizer 40 % · backlink-dach 35 % · content-pool 35 % · tracking 35 % · client-roadmap 30 % · client-access-lockout 30 % · agent-job-descriptions 25 % · captions 25 % · imagery-audit 25 % · sales-call-prep 25 % · video-edit 25 % · canary 20 % · automation-build 20 % · content-writing 20 %

### C5 BEHALTEN (10)
acceptance-criteria · behandler-seite · local-seo-review-page · marketing-grill · night-shift-v2 · novamira · sales-pitch · slopmonster · team-orchestrator · workflow-create

### C6 Tote Referenzen in Skills
canary → `00_project/morning-grill-skill/scan.py` (real: `scripts/scan.py`) · captions, content-format-board, personal-posts → Skills `social-visuals`, `story-automation-system` (existieren nur als Memory) · client-roadmap → Tool `ask_question` (heißt AskUserQuestion) · content-pool → „structure playbook" · maps-audit → `ranking-tracking` · tracking → `ranking-tracking-master-prompt` · content-writing → `references/scoring-rubric.md` (liegt in seo-page-optimizer) · morning-grill → `00_project/assets/741studio/creative-editor/`

Descriptions: 31.598 Zeichen (~8k Tokens) in jeder Session. Ziel nach Kürzung: unter 15.000.

## D. Job-Descriptions und Agent-Team

- Nutzung: 4 Dateien am 03.11., seither nichts. `reviews/` fehlt, `last_review` überall null. Freitags-Review 07.11. lief nicht. social-media-manager hat keinen inbox/outbox.
- Inhalt: ~20 % Nie-Regeln (wiederholen Hooks, Memory, CLAUDE.md), ~20 % Gates/Tools, ~45 % Rollenwissen.
- Urteil: webdev, project-manager, sales-director, social-media-manager **auf je 1 Seite** (Goal, Duties, Edge Cases). Nie-Regeln durch einen Verweis „Gates: siehe Hooks + CLAUDE.md" ersetzen. `morning-grill-brief.md` (Draft, Task aus) **löschen**. Roster-Ghosts ohne Datei **streichen**: nightshift, evening-log, canary, command-board-sync, chat-base.
- Platzierte Kopie `.claude/rules/agents/webdev.md` (6,4 KB) lädt in jeder Session, sobald eine Datei unter `assets/suriya|huewel|stuerzl|balihealing` gelesen wird. Nach Kürzung neu platzieren oder Pfad-Scope enger ziehen.
- tmux-Team (4 Sessions): nur noch für echte parallele, unabhängige Stränge starten. Für Seite, Nachricht, Kunde: eine Session plus Subagents. Skill `team-orchestrator` bleibt, Memory `agent-team-setup` fällt (Dublette).

## E. Hooks (behalten, Doku nachziehen)
- 6 aktiv: go_marker, go_card, live_change_gate, destructive_guard, slop_gate (Projekt) + presend_sweep_hook (global, absoluter Pfad nach `00_project/`). Plus global automation_guard, automation_done_gate, automation_session.
- `hooks/README.md` sagt „NOT active", Docstring presend „DRAFT, not installed" → beides veraltet, aktualisieren.
- Falsch-Positiv in live_change_gate: lesende Bash-Befehle, die `settings.json` oder `.claude/go` nur erwähnen, werden geblockt (heute 2× passiert).
- Lücke: INSERT/UPDATE mit WHERE geht am destructive_guard vorbei. Darum bleibt Memory `db-write-needs-isolated-confirmation`.

## F. Widersprüche, die eine Entscheidung brauchen
1. Nachricht **vor** oder **nach** Deploy? (`message-before-deploy` vs. `loom-video-no-extra-deploy-step`)
2. HTML in Kunden-Feldern: „Never" (CLAUDE.md) vs. „normalerweise, mit Ausnahmen" (Memory).
3. Vorab-Bestätigung: „Go?" am Ende vs. „ich warte nicht".
4. `minimal-change-website-work` vs. `page-swap-never-edit-live` (bewusst, aber in einer Datei festhalten).

## G. Reihenfolge der Umsetzung
1. Secrets aus 9 Memory-Dateien nach `.secrets/` (Sicherheit).
2. `~/CLAUDE.md` löschen, `741website/CLAUDE.md` auf ~35 Zeilen, `~/.claude/CLAUDE.md` auf ~18 Zeilen, tote Skill-Namen korrigieren.
3. Memory: 68 löschen, 71 zusammenlegen, MEMORY.md neu schreiben (Ziel unter 12 KB).
4. Skills: 6 löschen, 3 Dubletten, 8 aufteilen, 15 kürzen, tote Referenzen fixen.
5. Job-Descriptions auf 1 Seite, Ghosts raus, Kopien neu platzieren.
6. Hooks-Doku, danach `/doctor prompt-audit` als Gegenprobe.

## H. Umsetzungsstand 08.11.2026 (Go von Martin für Blöcke Secrets, CLAUDE.md, Memory, Skills)

| Baustein | vorher | nachher | Archiv |
|---|---|---|---|
| CLAUDE.md | 3 Dateien, 174 Zeilen, 11,6 KB | 2 Dateien, 43 Zeilen, 4,0 KB | `00_project/_archiv/home-CLAUDE.md-2026-11-08` |
| Memory | 329 Dateien, Index 20,4 KB | 191 Dateien, Index 11,8 KB, 0 tote Links | `~/.claude/projects/-Users-martindrendel-741website/memory-archiv-2026-11-08/` (150 Dateien, 11 davon als .ORIGINAL.md) |
| Skills | 42, SKILL.md 366 KB, Descriptions 31,6 K Zeichen | 33, SKILL.md 200 KB, Descriptions 16,5 K Zeichen | `00_project/_archiv/skills-2026-11-08/` |
| Secrets | 13 Werte im Klartext in Memory | 0 (Restscan sauber) | `.secrets/memory-secrets.env` (600, gitignored) |
| Immer geladener Kontext | ~64 KB | ~32 KB | |

Offen (kein Go): Block D Job-Descriptions/Team, Block E Hooks-Doku + Falsch-Positiv in `live_change_gate` (blockt lesende Bash-Befehle mit „FTP"/„deploy"/settings.json im Text; heute 5× bei Prüfern), Widersprüche F1–F4, Kamil-Ads-Konto 992-981-4693 vs 4093 (in `kamil-physio-client` markiert), Behandler-Seite Kunden-CI vs 741-CI (in `startseite-money-page-standard` markiert). 13 UNSICHER-Memories unverändert in M. Commit steht aus.

Nachtrag 08.11. (zweites Go): Block D umgesetzt (4 Job-Descriptions auf je unter 2.500 Zeichen, per place.py neu platziert, Validator PASS; 5 Roster-Geister entfernt; morning-grill-brief archiviert; webdev-Regel nur noch für suriya/stuerzl/talkinfive). Block E umgesetzt (Go-Gate ignoriert Heredoc-Bodies und /dev/null-Redirects, `ftp` nur noch als Befehl; 5 Regressionstests, 32/32 grün; README + presend-Docstring auf "aktiv"). F1 entschieden: Nachricht nach Deploy + Live-Check. Offen: F2–F4 (HTML-Ausnahmen jetzt in CLAUDE.md), Kamil-Ads-Konto-Ziffer, Behandler-Seite CI, 13 UNSICHER-Memories.
