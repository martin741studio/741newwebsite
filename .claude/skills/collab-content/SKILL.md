---
name: collab-content
description: Execute co-marketing editorial and reciprocal backlink collaborations for 741 clients. Ingests partner profiles, builds a 3-angle Mini-Pool, guides angle selection via Decision Cards (Checkpoint 1), drafts high-E-E-A-T reciprocal articles with natural contextual links, and validates plain-text CMS hygiene and YMYL compliance via deterministic linter before publishing (Checkpoint 2). Trigger on "/collab-content <client> <partner-domain>", "Backlink-Kollaboration für <Kunde>", "Co-Marketing mit <Partner>", or requests to brainstorm and write guest collaborations. Do NOT use for internal client blog posts (use content-writing), directory/citation builds (use citations/backlink-dach), or full site content pools (use content-pool).
---

# Co-Marketing & Backlink Collaboration Workflow (`collab-content`)

Owner: Martin Drendel · 741 Studio Standard v1.0.
Specification: `00_project/collab-content-workflow.md`.

---

## Critical Rules & Hard Guardrails

1. **Strict Plain Text in Client-Editable Textboxes (Hard Rule):**
   Never output raw HTML tags (`<span>`, `<div>`, `<br>`, inline styles) in article body text or headings. All formatting must be strictly Markdown headings, bold text, bullet points, and standard Markdown links `[anchor](url)`.
2. **Contextual Backlinks Only (Anti-Spam Rule):**
   Never create 1:1 reciprocal footer or sidebar links. Every backlink must be embedded naturally within 1,200+ words of genuinely valuable editorial copy.
3. **YMYL & Medical Policy Compliance:**
   Zero disease cure claims. Frame all health benefits factually (e.g., "supports hydration and vitality", not "cures fatigue").
4. **Mandatory Checkpoint Gates:**
   Never draft articles without Martin's explicit Go on the angle (Checkpoint 1). Never publish to CMS or dispatch to partners without Martin's explicit Go on the drafted copy (Checkpoint 2). Always use interactive Decision Cards (`ask_question`).

---

## Operational Checklist

When triggered, execute sequentially:

```
[ ] Phase 1: Ingestion & Boundary Filter
    [ ] Ingest client baseline from 00_project/assets/<client>/01-client/client-baseline.md
    [ ] Scrape partner domain (services, location, audience, content tone)
    [ ] Verify neither brand directly competes for identical physical appointments

[ ] Phase 2: Mini-Pool Formulation
    [ ] Extract synergy matrix (Geographic complement, Modality complement, Audience crossover)
    [ ] Formulate 3 distinct collaboration angles:
        • Angle A: Pre/Post Care or Modality Integration Protocol
        • Angle B: Lifestyle, Longevity & Everyday Habit Guide
        • Angle C: Curated Regional Healing Itinerary / Directory
    [ ] Record manifest in 00_project/assets/<client>/collab/<partner-slug>/spec.json

[ ] Phase 3: Checkpoint 1 Gate (Martin Angle Go)
    [ ] Present the 3 angles to Martin via Decision Card (ask_question)
    [ ] HALT execution until Martin confirms the winning angle

[ ] Phase 4: Reciprocal Copy Generation
    [ ] Draft Article 1 (for client site, featuring partner): 1,200–1,800 words
        • Contextual deep link to partner's core service page
    [ ] Draft Article 2 (for partner site, featuring client): 1,200–1,800 words
        • Contextual deep link to client's core service page
    [ ] Save drafts to:
        • 00_project/assets/<client>/collab/<partner-slug>/article_client.md
        • 00_project/assets/<client>/collab/<partner-slug>/article_partner.md

[ ] Phase 5: Verification & Linting Loop
    [ ] Run deterministic linter:
        python3 .claude/skills/collab-content/scripts/lint_collab.py \
          00_project/assets/<client>/collab/<partner-slug>/article_client.md \
          00_project/assets/<client>/collab/<partner-slug>/article_partner.md
    [ ] Ensure 0 raw HTML tags, 0 YMYL violations, 100% valid links

[ ] Phase 6: Checkpoint 2 Gate (Publishing & Outreach Go)
    [ ] Present linted copy summary and links to Martin via Decision Card (ask_question)
    [ ] Emit telemetry:
        python3 .claude/skills/collab-content/scripts/write_run.py <client> <partner-slug> completed cp2
    [ ] Stage plain-text copy for client CMS and partner email/WhatsApp handoff
```

---

## Reference Documents
- [collab-schema.md](file:///Users/martindrendel/741website/.claude/skills/collab-content/references/collab-schema.md): Schema for `spec.json`.
- [collab-content-workflow.md](file:///Users/martindrendel/741website/00_project/collab-content-workflow.md): Master workflow architecture.
