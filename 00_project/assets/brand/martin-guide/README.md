# Martin guide: the 741 character that points things out

Version 1, 2026-10-12. Source: `character-sheet.png` (Martin's character sheet). The cut-out poses are in `poses/` as PNG and WebP, about 20 KB each and about 240 px wide.

The website copy is in `04_site/public/review-assets/martin-guide/`, served as `/review-assets/martin-guide/` after a deploy. A deploy needs Martin's go.

Component files: `martin-guide.css`, `martin-guide.js`, demo `demo.html` with the screenshots `demo-1440.png` and `demo-500.png`. For a self-contained HTML deliverable such as a PDF source, a report in the portal or a file on `clients.741.studio/r/`, run `python3 inline.py in.html out.html`. It embeds the poses, CSS and JS.

## What the character is for

Martin points out the ONE thing in a section that the reader must not miss. Examples are a key number, the biggest lever, an open question, or a win. He makes a long deliverable easy to scan. He never decorates.

## Poses and when to use each

| Pose | File | Use it for |
| --- | --- | --- |
| hello | `martin-hello.webp` | Greeting at the top of a page or deliverable (once) |
| present | `martin-present.webp` | Introducing a section or an overview |
| point | `martin-point.webp` | The key finding or the number that matters. Place him so he points at it |
| think | `martin-think.webp` | Open questions, data to confirm, `[von Kunde bestätigen]` items |
| insight | `martin-insight.webp` | Recommendation, biggest lever, next step |
| celebrate | `martin-celebrate.webp` | A real win or result (with source and date) |
| front, three-quarter, side | `martin-front.webp` … | Intros, video thumbnails, title slides. Not for callouts |

## Markup

```html
<link rel="stylesheet" href="/review-assets/martin-guide/martin-guide.css">
<aside class="mg" data-reveal>
  <img class="mg__img" src="/review-assets/martin-guide/martin-point.webp" alt="Martin von 741 zeigt auf die Zahl" width="112">
  <div class="mg__bubble"><span class="mg__name">Martin</span><p>Diese Zahl zählt. Im Westen der Stadt sieht dich fast niemand.</p></div>
</aside>
<script src="/review-assets/martin-guide/martin-guide.js" defer></script>
```

Modifiers:
- `mg--right` puts Martin on the right and the bubble on the left.
- `mg--flip` mirrors him, so he faces or points the other way.
- `mg--small` is the compact size for lists and tables.
- `mg--dark` is for dark sections.
- `data-reveal` fades him in once and respects reduced motion.

## Rules

1. Use Martin only in deliverables that 741 authors and that a client or prospect sees. Examples are review pages, audit reports, content pool and sitemap reports, Un-Burning reports, the Maps playbook board, tracking dashboards, weekly PDFs, the quarterly war-room pack, offer PDFs, handover runbooks, portal pages and video intros or thumbnails.
2. Never use him on the client's own website, in a CRO prototype, in page copy for the client, in client emails, or in internal-only working files. For a CRO run, he may appear only in the presentation wrapper around the prototype, never inside it.
3. Use at most 1 callout per section and about 5 per page. If everything is pointed out, nothing is.
4. The bubble text is Martin speaking in first person ("ich") and uses "du" with prospects and "du" clients. It is at most 2 short sentences in plain client language, with no jargon and no tool names.
5. Every number in a bubble needs a real source and date in the section. Martin never says more than the data shows.
6. For health clients, the bubble follows the HWG rules: no healing or success promise.
7. Put the bubble text in HTML, never inside the image, so it stays editable, translatable and accessible. The alt text is "Martin von 741 …" plus the pose.
8. Place him next to the element he points at. "point" stands left of the target. Use `mg--right mg--flip` to point from the right.
9. Check the rendered page at desktop and mobile width with a screenshot before delivery.
10. The poses are about 240 px wide, which is enough for callouts up to about 120 px. For large hero use, have a high-resolution version generated from `character-sheet.png` first.

## Where it fits per workflow (state 2026-10-12)

| Workflow | Deliverable | Where Martin appears |
| --- | --- | --- |
| Review page (skill local-seo-review-page) | Prospect review page | hello in the hero, point at the grid scan result, insight at the biggest lever, think at open data, celebrate at proof |
| Maps audit (maps-audit) | Client report `client.html`, Befunde | point at the score and the top 3 findings, insight at the first lever, think at missing data |
| Content pool | Pool report and sitemap (client version) | present at each pillar, point at the A priorities, think at client questions |
| Un-Burning | Damage map and report | point at the biggest leak, insight at the first fix, celebrate when an area turns green |
| Maps playbook ("phone") | Board, client view | point at the top 5 tasks, think at open gates |
| Tracking and quarterly round | Dashboard, weekly PDF, war-room pack | point at the calls and cost per booked job, think at warnings, celebrate at wins, insight at the next quarter's lever |
| Automation build | Client runbook and handover | present at the data flow, think at "what you must do" |
| CRO Track A and B | Presentation wrapper only | insight next to the change rationale, never inside the prototype |
| Content writing | Not on client page copy | none |
| Backlink DACH | Google Sheet | none |
| Client access lockout (skill client-access-lockout) | Work overview PDF and reply to the client | none: a trust case needs a plain, factual document |
| Offer PDF, social visuals, video intros and thumbnails | Sales material | hello, present or insight as a title figure |
