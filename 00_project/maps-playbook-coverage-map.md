# Maps growth playbook: coverage map (version 2, final after design go)

Date: 2026-10-11. Status: final for this session. Version 1 (before the grilling) is replaced by this file. Design approved by Martin at checkpoint 1.
Language: STE. Measure names are German, as on Martin's board. Nothing here changes a client asset. Machine-readable twin: `maps-playbook-measure-catalog.json`.

## 1. Result in one view

- The board has **74 measure cards** (not about 60). Martin's text adds **3** that are not on the board: Local Schema, on-page basics and `llms.txt`. Total: **77 measures** in 21 groups and 3 pillars.
- Coverage: **32 covered**, **28 partly**, **17 missing**.
- Risk sorting (approved): **56 DO**, **20 DO WITH GATE**, **1 OUT OF SCOPE** (G16 bonus per 5-star).
- Phase: **16 measures** start in days 1 to 30, **43** from month 2, **18** later or on demand.
- 69 of 77 measures have an audit field. For these the playbook only reads the field. The new work is the **execution layer**: runbooks, tasks, owners, cadence, evidence per client.
- Truly new (no asset at all): DBA name rule, tracking number, post and photo cadence, review-request process and cards, spam and suggest-edit reports, canary and uptime checks, tool pages, decision pages, abandoned-form follow-up, best-of lists, landmark references, `llms.txt`.

## 2. Legend

| Code | Meaning |
| --- | --- |
| C | Covered: an asset exists and handles the measure |
| P | Partly: an asset exists, a part is missing |
| M | Missing: no asset |
| DO / GATE / OUT | Risk class: do, do only after a gate, out of scope (alternative given) |
| Phase | `d1-30` days 1 to 30, `m2+` from month 2, `later` on demand |
| Un-burning checks | IDs of the `un-burning` checks that cover the harm side of this measure (`UB.A01` to `UB.E05`). The measure waits while a matching harm item is open |
| RB | Runbook in `maps-playbook-skill/maps-playbook/references/runbooks.md` |

Asset codes: `AUD` = `00_project/audit-workflow-spec.md` (fields B01 to B13). `WK1` = `00_project/local-seo-program-week1-playbook.md`. `BP` = `00_project/gbp-visibility-blueprint.md`. `LOOP` = `00_project/loop-signals-playbook.md`. `SMP` = `00_project/startseite-money-page-standard.md`. `QA` = `00_project/page-content-qa-checklist.md`. `PSEO` = `00_project/programmatic-pages-playbook.md`. `CRO` = `00_project/cro-homepage-workflow.md`. `STR` = `website-struktur-master-prompt.md` (worktree only). `SEC` = `website-security-checklist.md` (worktree only). `ILP` = `00_project/internal-linking-plan.md`.

## 3. Coverage map


### P1 Google-Profil


**Profil-Fundament** (runbook RB01)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G01 | Keyword im Profilnamen (DBA) | AUD B13.03 flags extra words as risk. No build asset | ✗ M | No rule for a legal DBA. Audit rule B13.03 says red for extra words: needs an exception when legal-name proof exists | B13.03 | GATE | 1 | d1-30 | UB.C03 |
| G02 | Physische Adresse | NAP master (huewel-nap, maria-brasse-nap), `client_locations`, AUD B05.02, B13.02 | ✅ C | Check exists. Nothing to build: only a real eligible address counts | B05.02, B13.02 | GATE | 8 | d1-30 | UB.C03, UB.B01 |
| G03 | Einzugsgebiete | STR step 5 (catchment levels, worktree), AUD B04.01 | ◐ P | Catchment is analysed. The GBP service-area setting itself is not a task type | B04.01 | DO | 8 | d1-30 | - |
| G04 | Rufnummern-Attribution (Tracking-Nummer) | AUD B06.07 (call tracking tag), B09.03 (phone hours) | ✗ M | No process: tracking number as secondary, main number stays primary NAP, consent text. DE tool choice open | B06.07, B09.03 | GATE | 9 | m2+ | UB.C07 |
| G05 | Unternehmensbeschreibung | WK1 step 6 (max 750 characters, counted), AUD B10.05 | ✅ C | Texts exist per client. Execution needs GBP access and a per-change go | B10.05 | DO | 5 | d1-30 | - |

**Kategorien & Leistungen** (runbook RB02)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G06 | Primärkategorie | BP section 1, AUD B10.01, B11.05, B11.09 (driver analysis) | ✅ C | Use the audit driver result to rank this lever. Execution = task | B10.01, B11.05, B11.09 | DO | - | d1-30 | - |
| G07 | Sekundärkategorien | BP section 1 (1 + 9), AUD B10.01 | ✅ C | As G06 | B10.01 | DO | - | d1-30 | - |
| G08 | Service-Ausbau (20 bis 50) | BP section 2 (each service needs its own page), AUD B10.02, WK1 step 6 | ✅ C | Small-practice rule exists: coverage beats volume. Page dependency links to W09 | B10.02, B06.08 | DO | 5 | d1-30 | - |

**Bilder & Fotos** (runbook RB03)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G09 | Kontinuierlicher Foto-Upload | LOOP section 1 (file name, EXIF, caption loop), AUD B10.06 | ◐ P | Rules exist. Missing: a monthly upload routine and a client photo intake | B10.06 | DO | - | m2+ | - |
| G10 | Vorher/Nachher-Bilder | HWG guideline (memory hwg-fallstudien-guideline) | ◐ P | Health: HWG limits apply. Trades: no process yet | - | GATE | 5 | m2+ | - |
| G11 | Team- und Fahrzeugfotos (beschriftet) | LOOP section 1 (real signage photos) | ◐ P | Vehicle-photo trick is new. Needs client photos | B10.06 | DO | - | m2+ | - |

**Beiträge** (runbook RB04)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G12 | Regelmäßige Google Posts | AUD B10.07 (check). WK1 rule: own texts, no Falcon Agent auto-posts | ◐ P | No post calendar, no text pipeline, no owner | B10.07 | DO | 5 | m2+ | - |
| G13 | Saisonale Angebote und Promos | - | ✗ M | New. Health: price offers and gifts are restricted (HWG). Law and tax: own advertising law | B10.07 | GATE | 5 | later | - |

**Bewertungs-System** (runbook RB05)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G14 | CRM-Automatisierung (Bewertungsanfrage) | AUD B05.03 asks how reviews are requested, B13.07 flags gating | ✗ M | No build asset. Gated SMS is review gating. Alternative: ask every customer, no filter | B05.03, B13.07 | GATE | 2 | d1-30 | - |
| G15 | RFID / QR-Tapping-Karten | WK1 step 6 (patient guide with QR, spec only) | ◐ P | QR guide exists as spec. NFC or QR card for the review link: new, low risk | B05.03 | DO | - | d1-30 | - |
| G16 | Mitarbeiter-Incentives (Bonus je 5-Sterne) | - | ✗ M | Per-star cash bonus is OUT. Alternative: team goal on asks per job, not on stars | B13.07 | OUT | 2 | later | - |
| G17 | Review Velocity | AUD B05.03, B11.03 (gap to leader). WK1 rule 6 (target 2x leader) | ✅ C | Target and check exist. Build = G14 and G15 | B05.03, B11.03 | DO | - | d1-30 | - |
| G18 | Antwort-Disziplin | AUD B05.04, WK1 step 6 (reply templates). Memory no-review-answering | ✅ C | Client answers. 741 gives templates and tracks the reply rate | B05.04 | DO | 5 | d1-30 | - |

**Konkurrenz-Abwehr** (runbook RB06)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G19 | Bearbeitungsvorschläge (Suggest edits) | - | ✗ M | No process. Only genuine documented violations | B13.01, B11.07 | GATE | 6 | later | - |
| G20 | Meldung von Spam-Einträgen | AUD B13.01 (own duplicates only) | ✗ M | Reporting of competitors is new. Needs evidence log | B13.01, B11.07 | GATE | 6 | later | UB.C05 |
| G21 | Mehrfach-Profile (Standort-Expansion) | AUD B13.01 (duplicate = red), B04.03 (expansion intent) | ✗ M | Only real own locations. Audit treats duplicates as risk: need a clear line between duplicate and real location | B13.01, B04.03 | GATE | 7 | later | UB.C05, UB.B02 |
| G22 | Google-Profil-Übernahme durch Dritte / Capturing | WK1 section 11 (Falcon Guard), AUD B13.06 | ◐ P | Decided by Martin 11.10.2026: only reclaim own old or dormant profiles. No takeover-defence task. Falcon Guard stays a monitoring item in WK1 | B13.06 | GATE | 7 | later | UB.B02 |

### P2 Website


**Fundament & Gesundheit** (runbook RB07)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W01 | Ladezeit (Site Speed) | AUD B06.07 (PageSpeed API, to be tested) | ◐ P | Check only. No fix routine | B06.07 | DO | - | m2+ | - |
| W02 | Mobile Bedienbarkeit | AUD B06.02, memory mobile-fluid-root-and-header | ◐ P | Check exists. Fix = per client site | B06.02 | DO | - | m2+ | - |
| W03 | Modernes Website-Design | CRO workflow and skill `cro-homepage`, skill `imagery-audit` | ✅ C | Homepage only. Other pages not covered | B06.02 | DO | - | m2+ | - |
| W04 | Automatisierte Frühwarn-Checks (Canary) | SEC section 9 (monitoring, worktree only) | ✗ M | No agent that crawls forms, plugins and layout daily. Needs a scheduled task | B06.07 | DO | - | m2+ | - |
| W05 | Hosting-Erreichbarkeits-Check (Uptime) | SEC section 2, AUD B06.01 (ownership only) | ✗ M | No uptime check | B06.01 | DO | - | m2+ | - |

**Startseite** (runbook RB08)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W06 | Wichtigste Seite der Website | SMP, CRO workflow and skill | ✅ C | Covered | B06.02 | DO | 5 | m2+ | - |
| W07 | Lokale Relevanzsignale | SMP section E (local minimum), CRO | ✅ C | Covered | B06.02, B06.05 | DO | - | m2+ | - |
| W08 | Verlinkungsfokus | SMP, PSEO section 6 | ◐ P | Rule exists, no client check | B06.03 | DO | - | m2+ | - |

**Haupt- und Unterseiten** (runbook RB09)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W09 | Dedizierte Service-Seiten | SMP, skill `seo-page-optimizer`, STR (keyword to page), AUD B06.08 | ✅ C | Covered. Content pool will rank what to write | B06.08 | DO | 5 | m2+ | - |
| W10 | H1- und H2-Optimierung | Skill `seo-page-optimizer`, SMP section D, AUD B06.03 | ✅ C | Covered | B06.03 | DO | - | m2+ | - |
| W11 | Spezifischer Content und echte Jobs | QA gate, content pool (design), HWG guideline | ◐ P | Real-job proof has no intake process for trades | B06.08 | DO | 5 | m2+ | - |
| W12 | Unter-Dienstleistungsseiten | STR sitetree, skill `seo-page-optimizer`, PSEO | ◐ P | Covered as page spec. Content pool picks them | B06.08 | DO | - | m2+ | - |

**Standortseiten** (runbook RB10)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W13 | Regionale Abdeckung | STR step 5, PSEO, content pool rule 11 | ✅ C | Covered. Place page only with demand and unique facts | B04.01, B06.04 | DO | - | m2+ | UB.D05 |
| W14 | Kein KI-Slop | PSEO section 1 (uniqueness), skill `slopmonster`, QA gate | ✅ C | Covered | B06.04 | DO | - | m2+ | UB.D04 |
| W15 | Tiefe Funnel-Struktur | PSEO section 3 (page anatomy) | ◐ P | No funnel-depth check per client | B06.04 | DO | - | later | - |

**Interaktive Tools** (runbook RB11)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W16 | Nützliche Tools und Rechner | Review-page ROI calculator, taxi price calculator (client case) | ◐ P | No catalogue of tool types per niche, no process | - | DO | 5 | later | - |
| W17 | SEO-Hebel der Tools | Content pool (demand data) | ✗ M | Rule that picks tools from search demand is missing | - | DO | - | later | - |

**Interne Verlinkung** (runbook RB12)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W18 | Fluss nach oben | PSEO section 6, SMP, ILP (741.studio only) | ◐ P | Board diagram is a rule. No client check script | B06.03 | DO | - | m2+ | UB.E04, UB.D06 |
| W19 | Regelmäßige Anpassungen | - | ✗ M | No cadence, no crawl diff (Ahrefs not usable) | - | DO | - | later | UB.E04 |

**Conversion-Ebene** (runbook RB13)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W20 | Lead-Formular oben | CRO workflow, PSEO section 3, AUD B06.02 | ✅ C | Covered for homepage | B06.02 | DO | 5 | m2+ | - |
| W21 | Mobile Navigation, immer sichtbar (sticky CTA) | SMP, STR, AUD B06.02 (tap-to-call) | ✅ C | Covered | B06.02 | DO | - | m2+ | - |
| W22 | Kontrastreiche CTAs und Click-to-Call im Fließtext | CRO, AUD B06.02 | ◐ P | Homepage only. Body-text CTAs on other pages not checked | B06.02 | DO | - | m2+ | - |
| W23 | Vertrauenssignale (inkl. Google-Icon bei Zitaten) | CRO, SMP, skill `behandler-seite` | ✅ C | Covered | B06.02 | DO | 5 | m2+ | - |
| W24 | Abgebrochene Formulare nachfassen | - | ✗ M | New. Needs prior consent (GDPR). Health data is sensitive | B06.07 | GATE | 10 | later | - |
| W25 | CRM-Anbindung | AUD B08.01, memory leadgen-funnel-infra, portal leads CRM (staging) | ◐ P | Check exists. No standard connector per client | B08.01 | DO | - | m2+ | - |

**Kaufentscheidende Inhalte** (runbook RB14)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W26 | Kosten- und Preisseiten | QA gate (cost question), WK1 (cost FAQ mandatory) | ◐ P | No cost-page standard per niche. Prices: only verified | - | GATE | 5 | m2+ | - |
| W27 | Entscheidungshilfen (Vergleich, Finanzierung, Garantie) | - | ✗ M | New page types. Content pool can rank them | - | DO | 5 | later | - |
| W28 | Lokale FAQs | SMP section D, PSEO, skill `seo-page-optimizer` | ✅ C | Covered | B06.08 | DO | 5 | m2+ | - |
| W29 | Eigene "Best-of"-Verzeichnisse | - | ✗ M | New. Own ranking lists need neutral rules (fair-trade law) | - | GATE | 11 | later | - |

**Lokale Texturen** (runbook RB15)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W30 | Echte Projektberichte | HWG guideline (health), case-study pages on 741.studio | ◐ P | Health covered. Trades: no intake and consent process | - | GATE | 5 | m2+ | - |
| W31 | Verweis auf Google-Maps-Landmarks | SMP section E (districts) in part | ✗ M | Landmark rule and source check missing | B06.04 | DO | - | m2+ | - |
| W32 | Eingebettete Rezensionen mit Ortsbezug | LOOP section 3 (on-click shield, grey zone) | ◐ P | Method exists but is grey zone. Health: third-party praise limits (HWG) | B10.10 | GATE | 5 | m2+ | - |

**Technik (nur Text)** (runbook RB16)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W33 | Local Schema (JSON-LD) | SMP, PSEO section 5, AUD B06.03 | ✅ C | Covered | B06.03 | DO | - | m2+ | - |
| W34 | Basics: Alt, Canonical, Breadcrumbs, Meta | Skill `seo-page-optimizer`, AUD B06.03, PSEO | ✅ C | Covered | B06.03 | DO | - | m2+ | UB.D07 |
| W35 | llms.txt | - | ✗ M | New. Low cost, low proof of effect: set as low priority | B12.02 | DO | - | later | - |

### P3 Off-Page


**Branchenverzeichnisse** (runbook RB17)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O01 | Spezielle Nischen-Verzeichnisse | Skill `backlink-dach` (pillar A niche), Citations module | ✅ C | Covered. Health manual (jameda, Doctolib) | B07.02 | DO | - | d1-30 | - |
| O02 | Lokale Verzeichniseinträge | Citations module (44 DACH directories), `coralie-submission-runbook.md` | ✅ C | Covered | B07.02 | DO | - | d1-30 | UB.C04 |
| O03 | Kern-Verzeichniseinträge | Citations module, BrightLocal | ✅ C | Covered | B07.02, B06.05 | DO | - | d1-30 | UB.C04 |
| O04 | Datenaggregatoren und Verteilung | `coralie-aggregator-pack.md`, `portal-aggregator-selfservice-spec.md` | ✅ C | Covered. DACH aggregator list to verify | B06.05 | DO | - | d1-30 | UB.C04 |
| O05 | Indexierung der Verzeichniseinträge | `reporting/citation-monitor.mjs` (DataForSEO) | ◐ P | Monitor checks live status. Index check not confirmed | B07.02 | DO | - | d1-30 | - |

**Lokales Ökosystem** (runbook RB18)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O06 | Lokale Sponsoring-Partnerschaften | `backlink-workflow-dach.md` pillar B, LOOP section 4 | ◐ P | Process exists. Pilot (Hüwel) has no live link yet | B07.01 | DO | 4 | m2+ | - |
| O07 | IHK und Handwerkskammern | Backlink workflow (fixed priority, only if Gewerbe) | ✅ C | Covered | B07.01 | DO | - | m2+ | - |
| O08 | Berufs- und Branchenverbände | Backlink workflow | ✅ C | Covered | B07.01 | DO | - | m2+ | - |
| O09 | Lokale Presse und Blogger | Backlink workflow pillar D | ✅ C | Covered | B07.01 | DO | 4 | m2+ | - |
| O10 | Gemeinnützige Organisationen (.org-Links) | Backlink workflow (in part) | ◐ P | Donation for a link is a paid link: label rule needed | B07.01 | GATE | 4 | later | - |
| O11 | Hersteller und Lieferanten | Backlink workflow | ✅ C | Covered | B07.01 | DO | - | m2+ | - |
| O12 | Sponsoring lokaler Veranstaltungen | Backlink workflow (merge with O06) | ◐ P | Merge with O06. Same process | B07.01 | DO | 4 | later | - |

**Backlink-Kauf** (runbook RB19)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O13 | Strategischer Backlink-Kauf | Skill `backlink-dach` pillar C (strict path, label) | ✅ C | Covered. Pilot not run | B07.01 | GATE | 4 | later | - |
| O14 | Domain-Rating-Überwachung und Indexierung | Backlink workflow step 5 (monthly report, not scheduled) | ◐ P | Use DataForSEO rank, not DR. No schedule exists | B07.01 | DO | - | m2+ | - |
| O15 | Auswahl der Linktexte | Backlink workflow section 3.1 (anchor mix 60 / 30 / 10, no repeat of exact anchor) | ✅ C | Covered. Needs a check on paid placements only | B07.01 | GATE | 4 | m2+ | - |
| O16 | Auswahl der Quell-Domains | `local-backlink-classifier-prompt.md`, `gap-analysis.mjs` (spam flag) | ✅ C | Covered | B07.01 | GATE | 4 | m2+ | UB.D10 |

**Digitale PR** (runbook RB20)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O17 | HARO / Connectively | Backlink workflow section 3.3 (DACH journalist channels, marked "to verify") | ◐ P | Tool status checked 11.10.2026: Connectively closed Dec 2024. HARO runs again under Featured (free email, since Apr 2025). English market. DACH channels still to verify | B07.01 | DO | - | later | - |
| O18 | Unverlinkte Erwähnungen aufspüren | Backlink workflow section 3.3 (DataForSEO Content Analysis, Google quotes, Firecrawl), AUD B07.04 | ◐ P | Method exists in text. No script, no reclaim mail template, no schedule | B07.04 | DO | - | m2+ | - |
| O19 | Reputations-Management und Reddit-Beobachtung | Backlink workflow section 3.3 (reddit watch), AUD B07.04, B13.07. Sibling chat un-burning | ◐ P | Watch with real help = DO. Reddit burying = OUT. Clean-up of harm belongs to un-burning | B07.04, B13.07 | GATE | 3 | m2+ | UB.D08, UB.D09 |

**KI-Zitierung** (runbook RB21)

| ID | Maßnahme | Existing 741 asset | Cov | Gap (what is new) | Audit feed | Class | Gate | Phase | Un-burning checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O20 | LLM-Strukturierung und Zitate | AUD B12.01 to B12.04, BP section 4 (money prompts), WK1 section 11 (AI scans), backlink pillar E | ✅ C | Check and scans exist. Page structure rules in SMP (GEO) | B12.01, B12.04 | DO | - | m2+ | - |

## 4. Findings

1. **Board is bigger than the brief.** 74 cards plus 3 text-only measures. O06 and O12 (sponsoring) share one process. G06 and G07 (categories) share one runbook.
2. **The audit already checks most of the board** (69 of 77 measures have an audit field). The playbook reads these fields. It never recomputes them.
3. **Conflict with the audit spec, resolved.** Field `B13.03` marks extra words in the profile name as red. The board treats the same item as a lever. Decision: red stays red unless legal proof exists (legal name, signage, website, imprint). Then the cell shows "documented". Real case: Praxis Suriya removed its name suffix on 02.09.2026 because it was SEO-only.
4. **Driver lesson from the Stürzl run.** In that market, reviews did not explain visibility. Categories did (audit change D1, field `B11.09`). The playbook ranks G06, G07, G08, G14, G15 and G17 by the audit driver result, not by the board order.
5. **G22 decided by Martin.** Only reclaim the client's own old or dormant profiles. No takeover-defence task. Falcon Guard stays a monitoring item.
6. **Two more gates** beyond Martin's nine: gate 10 (abandoned forms, GDPR consent) and gate 11 (own best-of lists, fair-trade law). Donation-for-link (O10) falls under gate 4.
7. **Tool status checked 11.10.2026.** HARO: Connectively closed Dec 2024. HARO runs again under Featured (free email, since Apr 2025), English market. DACH directories Gelbe Seiten, Das Örtliche, 11880 and Cylex exist. Dynamic call-tracking numbers need consent before they show. A BGH ruling treats an unrequested review mail as unlawful advertising. HWG: before-after images are tightly limited. All from secondary web sources. Not legal advice.
8. **Four source files exist only in worktrees**, not on `main`: `backlink-workflow-dach.md` (worktree `great-easley-4f6970`), `website-struktur-master-prompt.md` and `seo-converting-page-prompt.md` (worktree `admiring-nightingale-f0f882`), `website-security-checklist.md` (worktree `dazzling-bhabha-2ba7cf`). Martin merges them or confirms the paths.
9. **The 90-day program file is missing.** `~/Downloads/741-studio-portal-90-tage-programm.md` does not exist on this machine.
10. **Un-burning spec now exists** (`00_project/un-burning-workflow.md`, first client also Praxis Suriya). Boundary: harm (exists and damages) = un-burning. Gap (missing, adds growth) = playbook. 16 measures carry `unburn_checks` (G01, G02, G04, G20 to G22, W13, W14, W18, W19, W34, O02 to O04, O16, O19). The playbook reads the harm register and the bedrock light. Growth starts when areas A to E are green or grey and C, D, E are green. W18 (flow upwards) is the ongoing side of `UB.E04`.
11. **Stale pack found.** `coralie-aggregator-pack.md` still shows the old Suriya business name with a suffix. The master record says "Praxis Suriya". The playbook reports such conflicts and uses the master record.

## 5. Interfaces (short)

| Sibling | Role | What this playbook takes or gives |
| --- | --- | --- |
| `audit-workflow` (diagnosis) | Finds what is wrong, with evidence | Takes: field status, evidence ID, date. Gives: a re-audit request |
| `un-burning-workflow` (clean-up) | Removes harm | Takes: harm register and bedrock light. Measures with un-burning checks wait while a matching harm item is open |
| `content-pool-workflow` (page content) | Ranks page content items | Takes: pool items for W09 to W15 and W26 to W31. Gives: page tasks with status |
| 90-day program | Client timeline | Open: file missing |
| Portal and night shift | Task list and overnight content specs | Gives: approved tasks. Night shift never publishes |

