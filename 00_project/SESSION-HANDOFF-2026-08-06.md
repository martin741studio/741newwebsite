# 741.Studio — Session Handoff (Stand 2026-08-06)

> Kurzer Übergabe-Stand, damit ein neuer Chat sofort weiß, wo wir stehen.
> Die wichtigsten Fakten liegen auch im Auto-Memory (`MEMORY.md`) und laden automatisch in jede neue Session.

## ✅ Diese Session erledigt

### Neue Review-Pages (alle live: `741.studio/review/<slug>/`)
| Slug | Prospect | Besonderheit | Video |
|---|---|---|---|
| `eri-trostl-coach` | Eri Trostl – Excellence Transformation Coach (München) | NEUE Marke (eritrostl.de); kein GBP für neue Marke, altes „Personal Trainer"-Profil | ❌ fehlt |
| `silke-riebauer` | Schmerzfrei leben Freiburg | Kliniken dominieren; Kälin-Beweis | ✅ |
| `karin-dinter` | PIROL Druckerei Minden | Notendruck-Nische bundesweit | ❌ fehlt |
| `silvia-richter-kaupp` | Business Coach Karlsruhe | GBP falsch „Personal Trainer" + 0 Bew. | ❌ fehlt |
| `tom-bauer` | GRUPPE93 Architektur (Lauf/Nürnberg) | Growth-Gap „Architekt Nürnberg" 0/81 | ✅ |
| `claudia-bischoff` | Salutogenese Pfullendorf | Blank-slate (kein GBP + keine Website) | ✅ |
| `michael-bolleier` | Osteopath Viernheim | Hat GBP, aber Kategorie „Gesundheitsberater" → „Osteopath" 0/81; Website = PM-Intl | ✅ |
| `agnes-speidel` | Naturheilpraxis Olching | | ✅ |

### Angebot (Offer)
- **Martin Hüwel**: PDF fertig → `~/Downloads/Angebot-741Studio-Martin-Huewel.pdf` (3.699 €, 2 Raten, Rate 2 nach 6 Wochen, Geld-zurück-Garantie). Begleit-E-Mail getextet. Format = Barbara-Brunner-Template. Workflow in Memory `offer-pdf-workflow`.

### Infrastruktur / Fixes
- 🔴→🟢 **Supabase `741-leads` war PAUSED** (Ursache: keine Lead-Mails). Restored + **täglicher Keep-Alive-Cron** (`.github/workflows/supabase-keepalive.yml`) verhindert künftiges Auto-Pause.
- **Bali Google Ads** (741 Acc): Report `00_project/bali-google-ads-report-2026-08-05.md`. Conversion-Tracking **verifiziert funktionierend** (0 Conversions = wenig Traffic, kein Bug).
- **Global `bypassPermissions`** in `~/.claude/settings.json` → keine Allow-Prompts mehr in irgendeiner Session.
- **Astrid-Lengauer Proof-Card** korrigiert → „Innenarchitektur"/„Interior Design" (war „Craniosacral") auf allen Seiten. (anja-kayser echt Craniosacral → unberührt.)
- **About-Seite** (EN+DE): neues Martin-Foto (Bergshot) + Hero-Spacing enger.
- **EN local-seo Hero** auf `{{> hero-slider }}` umgestellt.

## ⬜ Offen / To-do
- **Videos einbetten** sobald Loom-Links da: `silvia-richter-kaupp`, `karin-dinter`, `eri-trostl-coach`.
- **Drive-Analyse-Sheets füllen** (angelegt, aber leer) für die neuen Prospects – Chrome-UI.
- **Growth-plan Pricing: +10 % dann −10 % Kennenlern-Discount** (growth-plan-de.html) – gewünscht, noch offen.
- **EN local-seo: 3 DE-Sektionen** nach Englisch portieren (Analyse-Showcase, Potenzial-Vergleich, Proof-Wall) – nur Hero war gewünscht.
- **Kuhr Security GmbH** (Mike Kuhr, Berlin): Review-Page angeboten, wartet auf OK.
- Optional: Hüwel-Angebot-PDF auf Google Drive ablegen.

## 🔑 Kern-Workflows (Details im Memory)
- **Review-Page**: immer `cp 04_site/review/claudia-hauser/index.html`; PROSPECT_DATA als JSON tauschen; Scan-Grid als WebP; **Lücken-Keyword statt Top-Platzierung**; blank-slate (kein GBP) = graues „not-listed"-Grid + grünes Ziel. Build `npm run build` + `npm run deploy`; 375px-Check.
- **Offer-PDF**: HTML → Chrome-headless `--print-to-pdf`; Header/Footer via `<table><thead><tfoot>` (nicht `position:fixed`). Standard = 3.699 € 90-Tage-Paket.
- **Verkaufs-Haltung**: Rabatt nie herschenken → tauschen (Empfehlungen, Review-Video, Referenz, Monatspaket). „Patientenstrom aus der Google-Suche = wichtigster Hebel einer Praxis."
