# SEO and GEO rules for copy

Sources: `startseite-money-page-standard.md` (A0, B, D, D2, E, I, J, K), `page-content-qa-checklist.md`, skill `seo-page-optimizer` and its rubric, pool data. Full "why" text: Google Doc playbook `1b_TsRsUUf3s4cIXV-Kop7qu4Y5gqmpI4KFciqKqC_0E`.

**Contents** · 9 Gate G6 (v2) · 1 Gate A0 (full and light) · 2 On-page rules · 3 GEO layer · 4 Word count · 5 Local texture · 6 Internal links · 7 Schema · 8 Data points table

## 1. Gate A0

Page types for the gate: A money page (keyword volume 50 or more per month), B spoke page, C brand or mission page (no ranking goal), D cost page (short is normal). Blog posts use the light gate.

**Full A0 (types A and D):** source of truth loaded, Bestand fetched and counted, autocomplete tree (15 or more variants), keyword and volume, SERP top 10, real PAA, competitor word benchmark with at least 2 successful counts (try all 10 URLs before you say "no benchmark"), one verified local fact if the city is part of the positioning.

**Light A0 (blog posts and type B):** keyword and volume from the pool, SERP top 5 read, 2 successful word counts, real PAA, all facts verified, internal link targets from the sitetree. The floor is 70 % of the median. No Bestand check unless the post replaces an old one.

**Type C:** every client text on the topic (also neighbouring pages), Bestand comparison. No competitor benchmark.

Every row of the gate table carries a source and a date. A row that cannot be filled after the retry rules stops the run with the escalation line from the QA gate. Do not write with a gap.

## 2. On-page rules

- S1 Exactly one H1. It holds the primary keyword. Local pages add the city.
- S2 Title up to 60 characters, keyword first, then city or qualifier, then brand. Meta description up to 155 characters, benefit, keyword, soft CTA.
- S3 H2 and H3 map to search intent, competitor subtopics and PAA questions. Cover what the top results cover, plus a real edge from the client's facts.
- S4 URL slug: lowercase, hyphens. Keep an existing URL that already ranks. Rewrites never edit a live page in place (page-swap rule).
- S5 Alt texts name the service and the city, no stuffing. Images are real, never invented faces.
- S6 One keyword per page. If two pages share the main keyword the run stops and asks Martin (cannibalisation check).

## 3. GEO layer (AI answer engines)

- G1 A direct-answer block of 2 to 4 sentences directly under the H1. It stands alone and can be quoted. Element `answer`.
- G2 A definition box for the core term when the page explains one.
- G3 FAQ from real PAA questions, 2 to 3 sentences each, as `### Frage?` headings. The technical block holds the FAQPage schema.
- G4 Extractable facts as short statements: who, where, how long, what it costs if public. Engines cite specifics, not adjectives.
- G5 Name the entities: method, city, nearby areas, institutions, law or standard.
- G6 Author and date visible on blog posts. Credentials proven.

## 4. Word count

- W1 Count with `wordcount.py` on the visible text (H1 to before the TECH block). Same method for Bestand, draft and competitors.
- W2 Never thinner than the Bestand (hard stop). Money pages: at least 70 % of the competitor median.
- W3 Fix the target before writing. Put the sentence "X Wörter eigene Seite, Y Bestand, Z Median, Quelle, Datum, Urteil" in the gate report.
- W4 Quality first: do not pad. If the benchmark is far above what the client can truthfully say, say so to Martin and propose elements (FAQ, steps, table) that add real information.

## 5. Local texture

- L1 City and catchment appear in the H1, title and meta (local pages) and in the body.
- L2 One verified, specific local fact goes into its own paragraph (an institution, a rule, a number with source). Never name-dropping.
- L3 Place pages need demand, catchment signal and unique local facts. All three. Otherwise name the place in text only. (pool rule 6)
- L4 NAP identical to the locked record.

## 6. Internal links

- I1 Link up to the pillar page, across to sibling pages, to the author page and to the contact path. The targets come from the sitetree.
- I2 The links stand in the visible body as Markdown links. The script counts them in the visible text, not in the technical block.
- I3 Anchor text names the target topic. No "hier klicken".
- I4 A blog post links to its money page in the first third and again at the end.

## 7. Schema (technical block)

LocalBusiness or MedicalBusiness or LegalService with locked NAP, Service, FAQPage, Person (for practitioner pages and blog authors, `sameAs` only for verified profiles), Article for blog posts with author, datePublished, dateModified. Valid JSON-LD. Written for 741 and the developer, not part of the visible text.

## 8. Data points per page (what the brief must hold)

| Field | Source |
| --- | --- |
| Primary keyword, cluster, volume (national or local label) | pool `keywords[]` |
| Intent and reader question | pool `question`, `audience` |
| PAA questions | pool `demand.paa_samples`, SERP |
| Competitor words, headings, schema | pool `competitor`, A0 reads |
| Bestand text and words | live page |
| Locked NAP | source of truth |
| Proof assets | pool `evidence[]`, authority pillar |

## 9. Gate G6 (v2, 2026-10-11): what it checks, and why

Checked against the 741 SEO library (90 sources, files 027, 052, 059, 067, 071, 079, 083, 088), the Drive playbook and strategy matrix, and 2025/2026 research. Nobody can guarantee a ranking. G6 guarantees the parts we control and avoids the known traps.

| Check | Type | Evidence and source |
| --- | --- | --- |
| PAA answered, or dropped with a code (off-offer, nicht rechtssicher, Duplikat) | HARD | QA checklist 1.3; library 088. |
| Answer block early (by word 200 and 40 % of the page), 2 to 4 sentences, about 50 words | HARD (position), warn (length) | Library 071, 083, 027; tripledart study (answer in the first 40 % mattered, one niche only). |
| Every Vertiefung block holds a source, a number or a client fact (information gain) | HARD | Library 088, 071, 090; Google helpful-content guide. |
| At least 2 own headings, not 50 % or more copied from the benchmark | HARD | Library 088, 067 ("add what they lack"). |
| Exact primary phrase in at most one third of the H2/H3 | HARD | Library 088, 079 (stuffing hurts). |
| Visible date line on pages that cite statutes (Rechtsstand) | HARD | Library matrix sheet, 088; Google (do not fake dates). |
| A proven credential is visible (E-E-A-T) | HARD | Library 052, 016, 027; Google guidance on author information. |
| JSON-LD matches visible text, no placeholders, absolute URLs; types: WebPage, BreadcrumbList, LegalService/Organization, Person (person pages), Article (blog) | HARD | Library 027; Google AI-features doc (no special schema needed). FAQPage only with `schema_faq: true`: FAQ rich results ended in 2026. |
| Same primary keyword on two pages, links to targets outside the sitemap, own pages more than 25 % similar | HARD (cross-page, `link_network.py`) | Library 042, 052 (cannibalisation = same entity and intent); Google scaled-content policy. |
| Topic stems, entities, statutes that most benchmark pages have | ADVISORY (log, with a reason if omitted) | Ahrefs 2025: content-score tools correlate weakly; no source gives percentages. Needs at least 5 benchmark pages. |
| 3 to 8 contextual internal links, hubs link down to children, 2 incoming links | warn | Library 059 (3 to 8); Zyppy study (more helps, no fixed number). |
| 30/60/90 day Search Console review, 6 and 12 month review, AI-answer prompt set | after launch (`measure_plan.py`) | Matrix sheet (citation assets 60 to 90 days, authority 3 to 12 months); Ahrefs 2025. |

**Never copy from the library:** keyword stuffing in business names, exact-match or "wasteful" domains and behaviour steering (library 011, 012, 023, 044, 068, 078), `llms.txt` (no effect proven), vendor claims such as "34 % of AI citations" or "3.7 positions" as thresholds, "E-E-A-T is a ranking factor" (Google calls it a quality framework).

**Not in G6 (own workflows):** Google Business Profile, off-site mentions and backlinks (they correlate most with AI visibility), Core Web Vitals and indexing (developer handoff; targets are in the measure plan), content refresh (KICK review in the measure plan).
