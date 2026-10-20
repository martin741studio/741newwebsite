# Page templates (section plans with IDs)

Each page type has a fixed list of section IDs. The outline may drop a section only with a written reason (like the CRO coverage check). Elements follow the money-page standard D2: `hero`, `answer`, `text`, `accordion`, `check-list`, `el-grid`, `step-flow`, `stat-badge`, `table`, `timeline`, `faq`, `person`, `proof`, `notice`, `cta`. Status of each template: P = proven pattern, D = draft template, first use.

**Contents** · 1 Homepage (P) · 2 Service page seller + Vertiefung (D) · 3 Location page (D) · 4 Practitioner page (P) · 5 Cost page (D) · 6 FAQ page (D) · 7 Blog post (D) · 8 Section-plan rules

## 1. Homepage (P): CRO P0 blueprint, 10 rows

| ID | Row | Element | Job | CTA |
| --- | --- | --- | --- | --- |
| S00 | Notfall-Streifen (optional) | `cta` | Acute case reaches a number at once. Only with released numbers. | secondary |
| S01 | Hero | `hero` | Who, what, where, next step in 5 seconds. H1 with keyword and city. | primary |
| S02 | Beweis-Leiste | `proof` | Compact proof: rating with count, one credential. | |
| S03 | Ist das etwas für mich? | `check-list` | 3 to 5 recognisable situations, then one line how you help. | primary |
| S04 | Leistungen | `el-grid` | Cards, each links to its service page. | |
| S05 | Der erste Termin | `step-flow` | 3 to 4 steps, duration, price range if known. | primary |
| S06 | Über die Behandlerin / den Anwalt | `person` | Photo, name, proven credentials, one own sentence. | primary |
| S07 | Bewertungen | `proof` | Open layout, experience content only. | primary |
| S08 | FAQ | `faq` | Price first, real objections. | |
| S09 | Standort | `text` | Address, access, hours, map note. | |
| S10 | Abschluss-CTA | `cta` | Mirrors the hero: benefit headline, check marks, proof, reassurance, CTA. | primary |

Source: `cro-homepage-workflow.md` Step 2/3 and `patterns.md` P0. The CRO workflow keeps the layout. This workflow writes the words.

The homepage needs a direct-answer block too (GEO). Put it in the hero block and mark the hero `element: hero+answer`, or add it as the first lines of S03. The CRO Step 3 calls this workflow (Martin, 2026-10-11): see section 16 of the spec.

## 2. Service page: seller layer plus Vertiefung (D, v2 from 2026-10-11)

Martin (2026-10-11): a service page is like a homepage. It sells, it is fast, it has the best UX. Depth is a mix with blog content. So the page has two layers:

1. **Seller layer** (S01 to S06, S08 to S09): short, scannable, one CTA path. Together at most 550 visible words (counted without the FAQ section S08 and the Vertiefung S07).
2. **Vertiefung** (S07): the depth the benchmark pages have, as 3 to 5 accordion blocks. Each block answers one search intent or PAA question in 120 to 220 words. Google reads it, the visitor opens it only if needed.
3. **Ratgeber links:** long teaching (statute walk-throughs, sentencing, limitation periods) belongs in blog posts. The page links to them from the Vertiefung.

The total still reaches the A0 floor (Bestand, 70 % of the competitor median). If it does not, add Vertiefung blocks with real facts. Never pad the seller layer.

| ID | Section | Element | Job | CTA |
| --- | --- | --- | --- | --- |
| S01 | Hero | `hero` | H1 with the service keyword (and city if local). Situation first, then how you help. 1 CTA, reassurance line. | primary |
| S02 | Direkt-Antwort | `answer` | 2 to 4 sentences, quotable. Definition of the core term. | |
| S03 | Wann das Thema für Sie wichtig wird | `check-list` | 3 to 5 situations the reader recognises (from the Bestand and the firm's phrases). | |
| S04 | So läuft es ab | `step-flow` | 3 to 5 steps, taken from the Bestand and the approved homepage. The CTA repeats here. | primary |
| S05 | Wer Sie berät | `person` | Proven titles, one own sentence of the person, link to the person page. | |
| S06 | Kosten kurz | `text` | Cost model in 3 to 5 sentences with link to the Kosten page. No amounts without release. | secondary |
| S07 | Vertiefung | `accordion` | 3 to 5 blocks `### Heading`, each 120 to 220 words, law and facts with sources. | secondary |
| S08 | Häufige Fragen | `faq` | The client's own FAQ first, then real PAA. `### Frage?` | |
| S09 | Abschluss-CTA | `cta` | Mirrors the hero. | primary |

Order on the page: S01, S02, S03, S04, S05, S06, S07, S08, S09. Internal links: pillar, siblings, person page, Kosten page, Ratgeber posts.
**Legal pages:** HWG or BRAO rules apply to every accordion block as to the seller layer.

## 3. Location page (D)

Required before writing: demand signal, catchment signal and one verified local fact (all three, or the place is only named in text).

| ID | Section | Element | Job | CTA |
| --- | --- | --- | --- | --- |
| S01 | Hero | `hero` | H1 service + city. Address and next step visible. | primary |
| S02 | Direkt-Antwort | `answer` | What the client does in this city, for whom. | |
| S03 | Lokaler Bezug | `text` | The verified local fact in its own paragraph, with the client's link to the place. | |
| S04 | Leistungen vor Ort | `el-grid` | Only services really offered at this location. | |
| S05 | Anfahrt und Zeiten | `text` | NAP identical to the locked record, transit, parking, hours. | secondary |
| S06 | Wer Sie vor Ort berät | `person` | The person or team at this location. | |
| S07 | Beweis | `proof` | Reviews from this location only. | primary |
| S08 | Fragen | `faq` | 3 to 5 local questions (arrival, languages, first contact). | |
| S09 | Abschluss-CTA | `cta` | | primary |

Never copy one location page to make another. A swapped city name is scaled content. (pool rule 6)

## 4. Practitioner page (P)

From the skill `behandler-seite`. Address form follows the client's site.

| ID | Section | Element | Job |
| --- | --- | --- | --- |
| S01 | Hero | `hero` | Name, role, city, one trust sentence, portrait, CTA. |
| S02 | Vertrauensleiste | `proof` | 4 chips: years, state licence or approbation, top certificate, clinical or professional background. Only proven. |
| S03 | Mein Ansatz | `el-grid` | One strong H2 in ich-form and 4 cards distilled from the client's own text. |
| S04 | Einblick | `text` | 2 sections with real photos and factual captions. |
| S05 | Werdegang | `timeline` | Chronological, plus a "Qualifikationen im Überblick" check-list. |
| S06 | Warum dieser Weg | `text` | Personal motivation. HWG defensive: motivation, never a treatment result. |
| S07 | Hinweis | `notice` | Mandatory notice box. |
| S08 | Abschluss-CTA | `cta` | |

Person schema in the technical block, `worksFor` pointing to the existing business `@id`, `sameAs` only for verified profiles.

## 5. Cost page (D, type D: short is normal, 400 to 700 words typical)

| ID | Section | Element | Job |
| --- | --- | --- | --- |
| S01 | Hero | `hero` | H1 with the cost keyword. |
| S02 | Direkt-Antwort | `answer` | The cost basis in 2 to 4 sentences. A number only if the client confirms it. |
| S03 | Wovon der Preis abhängt | `el-grid` | 3 to 5 factors. |
| S04 | So wird abgerechnet | `step-flow` or `table` | Model (for example RVG, time, advance). Real terms only. |
| S05 | Wer die Kosten trägt | `text` | Krankenkasse, Rechtsschutz, self-pay. Exact, with source. |
| S06 | Fragen | `faq` | |
| S07 | Abschluss-CTA | `cta` | |

All prices are placeholders until the client confirms them. No "kostenlos" or "Festpreis" unless true and stated with terms.

## 6. FAQ page (D)

| ID | Section | Element | Job |
| --- | --- | --- | --- |
| S01 | Hero | `hero` | H1 "Häufige Fragen zu [Thema]". One intro sentence. |
| S02 | Direkt-Antwort | `answer` | The most asked question first, answered fully. |
| S03 to S0n | Fragegruppen | `faq` | Group by theme (Ablauf, Kosten, Vertraulichkeit, Vorbereitung). Each question is a `###` heading. 2 to 3 sentences, longer where the topic needs it. |
| S0n+1 | Abschluss-CTA | `cta` | |

Keep the client's existing FAQ 1:1 (adjust address form and legal wording). Add real PAA. FAQPage schema in the technical block.

## 7. Blog post (D)

Rules: `blog-rules.md`.

| ID | Section | Element | Job |
| --- | --- | --- | --- |
| S01 | Titel und Autorenzeile | `hero` | H1 with the keyword question or statement. Byline: name, proven title, published date, last checked date. |
| S02 | Kurzantwort | `answer` | 2 to 4 sentences. |
| S03 | Grundlage | `text` | Law, method or guideline, with source. |
| S04 | Was das für Sie bedeutet | `text` | Practical meaning. No case assessment. |
| S05 | Was Sie jetzt tun können | `step-flow` or `check-list` | Next steps. |
| S06 | Häufige Fragen | `faq` | 3 or more real PAA. |
| S07 | Quellen | `text` | Source lines. |
| S08 | Autorenbox und CTA | `person` and `cta` | Author with credentials, link to the person page, soft CTA. |

## 7b. Further page types (D, first use 2026-10-11)

**Hub page** (Leistungen, Ratgeber): S01 hero with H1 · S02 `answer` (what the area covers) · S03 `el-grid` cards, each with benefit heading, one line, link · S04 `step-flow` or `check-list` (how to choose) · S05 `faq` (3 to 5) · S06 `cta`. Words: short, 350 to 600. The Vertiefung lives on the child pages.

**About the firm** (Kanzlei, Über uns): S01 hero · S02 `answer` (who we are, for whom) · S03 `el-grid` (way of working, from the firm's own words) · S04 `text` (positioning, two mandate groups) · S05 `proof` (only released numbers) · S06 `person` (lead person) · S07 `text` (locations) · S08 `cta`.

**Team page:** S01 hero · S02 `answer` · S03 `el-grid` of person cards (name, role, area, link, only proven facts) · S04 `text` (how the team works) · S05 `cta`. A name only appears if the live site names it and the firm confirms it (flag, not invent).

**Person page** (Dr. Stürzl, Dr. Glogger): use section 4 (practitioner page). Facts only from the live profile page. Awards and rankings only with release (flag).

**Contact page and news hub:** no answer block needed: set `require_answer_block: false` in the brief. Brand, person and press pages (type C) use `gate: A0-brand`: G6 then skips the benchmark-based checks and says so.

**Contact page:** S01 hero · S02 `el-grid` two location cards (address, phone, hours, access, parking) · S03 `notice` emergency numbers (only released ones, else placeholder) · S04 `text` how the first contact works (topic only, no case details) · S05 `faq` (3) · S06 `cta`. NAP identical to the locked record.

**Publications and press:** S01 hero · S02 `answer` · S03 `timeline` or list of publications and talks from the live profile pages with year and source · S04 `proof` awards and rankings (placeholder until released) · S05 `cta`.

**News hub** (Aktuelles): S01 hero with one intro paragraph and the list of posts is generated by the CMS. No copy beyond the intro.

## 8. Section-plan rules

1. The brief lists the section IDs in order. The page must match the order (the script checks).
2. A section may be dropped only with a one-line reason in the outline, grounded in data or in the niche.
3. Every CTA section carries `cta: primary` or `cta: secondary` in its marker. One primary CTA text per page.
4. A section whose content is a list, a process or a comparison uses the matching element, never a text column.
5. Each section has one job, written in the outline.
