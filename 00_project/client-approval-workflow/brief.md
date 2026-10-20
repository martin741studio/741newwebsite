# Client-Approval-Workflow — Brief (Grill-me, 2026-10-13)

Status: Grill-me done (13.10.). Research done (13.10., 61 sources). Design go from Martin on the prototype (13.10.: "How it's built … can be used for the client as well"), including the Martin-guide placement. Next: build into the portal on staging (workflow-creation step 3).

## Job
The client sees our prepared work in the portal and chooses from it. Sources: client audit, content pool, CRO homepage run, site tree, GBP plan. The client joins the process, and 741 keeps the results on track (visibility in Google Maps, Google Search and on the website).

## Scope (what the client sees)
1. Visual elements and design (hero images, sections, design elements)
2. Text and headline changes (with keywords)
3. Branding elements
4. Website content and the site tree (per node: "I offer this" / "I have content" / "No")
5. Google Business Profile: categories, services + descriptions, photos + posts, opening hours / NAP / attributes

## Decisions (Martin, 2026-10-13)
| Topic | Decision |
| --- | --- |
| Client role | Chooses from 2–3 pre-checked variants per item. One variant is marked "741 empfiehlt". |
| Conflict with ranking needs | SEO lock: for ranking-critical items the client chooses only the wording, not whether the keyword stays. One sentence in the element says why. |
| Place | Portal `clients.741.studio` (login, votes per client in Supabase `741-portal`, history stays). Portal rules apply: fresh file, backup, staging, live only after go. |
| Timing | Continuous: each element goes into the dashboard when it is ready. |
| Notification | Max. one digest mail per day ("X new items wait for you") with a direct link, plus a counter in the portal. |
| Silence | Reminder after 3 days. After 7 days "741 empfiehlt" counts as approved, with a note in the decision log. The deadline is visible on the element. |
| GBP | Client sees all four groups before a change: categories, services + descriptions, photos + posts, opening hours / NAP / attributes. |
| Images | Shown in page context (hero section with headline and button). Real photos come first. AI images are marked "Richtung" and come with a shoot list. |
| Text | Before / after: current text on the left, 2–3 variants on the right, keyword marked, one "why" line with real data (e.g. search volume). Lock icon on the keyword. |
| Live change | Client approval goes to a "ready for live" list. Live only after Martin's go (rule [[no-website-changes-without-go]] stays). |
| Pilot | Praxis Suriya. First real element (2026-10-13): price of a single session, 95 € ("741 empfiehlt") vs. 85 €, active yes required. Source: `00_project/assets/suriya/content-pool/06-abgleich-live-2026-10-13.md`. |

## Site tree: why each node exists (explanation for the client)
1. Service + location page: brings rankings and requests. Client confirms the service is real.
2. Knowledge / guide page: answers patient questions, supports service pages and AI answers. Client is the best source.
3. Ads landing page: paid traffic only, not indexed. Approval only when ads run.
4. Trust page (about, team, reviews): supports all other pages.

## Patterns to reuse
- 741 element pool (yes / maybe / no + notes, replay) from the Track B runs — becomes a portal tab with Supabase storage.
- Site-tree report with text draft at the node ([[client-textdraft-delivery]], [[client-structure-page-playbook]]).
- Portal staging table `page_change_requests` ([[portal-single-file-workflow]]).
- From the ECC repo (Zenith chat): `santa-method` (two independent reviewers before an item reaches the client), `architecture-decision-records` (decision log per client), `brand-discovery` (resumable interview modules).

## Research scope (knowledge base, sources max. 3 months old)
1. Approval tools and UX (Pastel, Markup.io, Ziflow, Figma comments, agency portals)
2. Agency client processes (how SEO / web agencies involve clients without losing results)
3. Decision psychology (few options, default recommendation, one-line reason, decision fatigue)
4. GBP and SEO risks of changes (what triggers suspensions or ranking loss → what gets a lock)

## Changes from the research (2026-10-13, for Martin's design go)
Library: `00_project/knowledge/client-approval-library/INDEX.md` (61 sources, 4 extracts).
1. **7-day rule needs consent and has exceptions.** Silence counts as approval only if the client agreed in writing (contract clause or portal onboarding step). Health, treatment, price and legal claims always need an active yes (02, 03). No tool auto-approves after a deadline, so this is our own design (01).
2. **Active "Passt so" beats silence.** Silent defaults hold worse later than an active yes (03). One click on the recommendation must be easier than waiting.
3. **Three fixed buttons:** approve · approve with a small change · request change (01).
4. **One approver per client.** Others may only comment (02).
5. **Deadline set when the item goes out.** Reminders before, at and after it; stop after the decision (01).
6. **Decision log fields:** person, time, item version, type ("client" or "auto after 7 days") (01).
7. **Lock scope (04):** primary category, business name, address, map pin, service-area setting and GBP website URL are agency-only. Titles and H1s: keyword stays, wording is free. URL changes only with a 301. Save the old value before every locked change, so a revert takes minutes. Monitoring window: GBP 3–7 days and 4 weeks; website 14+ days.
8. **Low-risk fields stay open:** special hours, photos and normal copy outside locked elements need only a log entry (04).
9. **Google-suggested edits:** owners have 4 days to reject them, so the portal must warn within hours (02).
10. **Keyword first:** fix the keyword before the client sees text variants. A later keyword change is a new item (02).

## Hard limits
- No live change without Martin's go.
- No unverified data in a "why" line ([[claims-need-real-data]]).
- HWG check before a health client sees an item.
- No method sources named to the client ([[no-method-sources-in-deliverables]]).

## Martin guide (2026-10-13)
Client view only, never in the internal 741 view. Max. 4 per page: `hello` at the top, `think` at items that need an active yes (price), `point` at the SEO lock of a text item, `celebrate` when all items are decided. Bubble in Ich-Form, du, max. 2 sentences, HWG-safe. Rules: `00_project/assets/brand/martin-guide/README.md`. Prototype: `prototype/index.html`.
