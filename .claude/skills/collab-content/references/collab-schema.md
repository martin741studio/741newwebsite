# Collaboration Schemas

## 1. `shortlist.json` (per client, in `collab/_screening/`)

```json
{
  "client": "<client-slug>",
  "screened_at": "YYYY-MM-DD",
  "candidates": [
    {
      "name": "...",
      "domain": "...",
      "location": "...",
      "location_status": "verified | inferred | unanswered",
      "relevant_services": ["..."],
      "criteria": {
        "geographic_relevance": "...",
        "audience_relevance": "...",
        "values_alignment": "...",
        "service_compatibility": "...",
        "recommendation_fit": "...",
        "editorial_quality": "..."
      },
      "requires_partner_confirmation": ["..."],
      "seo_value": {
        "local_relevance": "...",
        "organic_referral": "...",
        "local_visibility": "..."
      },
      "angle": "...",
      "uncertainties": ["..."],
      "recommendation": "proceed | confirm_fit | reject",
      "evidence": ["<url>", "..."]
    }
  ],
  "nonlocal_authority": [ { "name": "...", "domain": "...", "note": "..." } ],
  "rejected": [ { "name": "...", "domain": "...", "reason": "..." } ]
}
```

## 2. `spec.json` (per partner, in `collab/<partner-slug>/`)

- `client`: client slug.
- `partner`: `{ name, domain, location, core_services[] }`.
- `screening_ref`: path to the shortlist entry.
- `content_ideas[]`: each with `id`, `title_working`, `audience_intent`, `topic_terms[]`, `contributions` (client / partner), `roles` (how services relate, where they differ), `structure[]`, `internal_links` (reciprocal — see below), `backlink_placement`, `reader_next_step`, `requires_partner_confirmation[]`.
  - `internal_links.client_article`: the link(s) **that `article_client.md` must point OUT to** — these are pages on the **partner's** domain (the backlink the client-side piece owes the partner). Not the client's own pages.
  - `internal_links.partner_article`: the link(s) **that `article_partner.md` must point OUT to** — these are pages on the **client's** domain. Not the partner's own pages.
  - A 2026-10-22 batch got this backwards for four partners (client_article linked to the client's own pages instead), which passed the old lint and only surfaced when a partner noticed the missing backlink. `lint_collab.py --client-domain --partner-domain` now catches this; double-check the field direction above before saving `spec.json`.
- `selected_angle`: the idea approved at Checkpoint 1, with `approved_at`.
- `articles`: `article_client` and `article_partner`, each `{ target_site, working_title, seo_title, meta_description, slug, target_url(s), anchor_text, file_path }`.
- `status`: `client_reviewed`, `shortlist_ready`, `partner_approved`, `ideas_ready`, `angle_approved`, `drafted`, `linted`, `cp2_go`, `cp2_stopped`, `published`.

## 3. Article invariants
- `target_site`: domain where the article will be hosted.
- `target_url`: exact deep link to the featured business's relevant page.
- `anchor_text`: descriptive phrase inside paragraph copy; varied across the pair.
- Each draft starts with `Title:`, `SEO title:`, `Meta description:`, `Slug:` lines.
