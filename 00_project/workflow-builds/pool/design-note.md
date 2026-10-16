# Content Pool & Sitemap Design Note

Workflow ID: pool
Date: 2026-10-16
Owner: Martin

## 1. Concrete Use Cases (Step 2.1)

### Use Case A: New Client Onboarding (e.g. Praxis Suriya / Bali Healing)
- **Trigger:** `/content-pool suriya`
- **Steps:** Load verified services; scrape 3 local competitors; pull DataForSEO SERP and Google autocomplete tree; score fit (3=exact, 2=education, 1=adjacent, 0=cut); validate via `validate_pool.py`; render HTML report; wait for Martin's Checkpoint 1 Go; generate `sitetree.json` and xlsx export at Checkpoint 2.
- **Tools:** `python3 scripts/dfs.py`, `python3 scripts/autocomplete_tree.py`, `python3 scripts/build_pool.py`, `python3 scripts/render_report.py`.
- **Result:** Ranked keyword candidates across 4 pillars, HTML visual report, `pool-top.md` feeding CRO.

### Use Case B: Existing Website Content Rework (e.g. Dumann)
- **Trigger:** "Content-Pool prüfen für Dumann"
- **Steps:** Crawl existing site URLs; pull GSC search queries; benchmark existing pages against competitor median; identify content gaps and cannibalization; produce updated sitetree.
- **Tools:** `python3 scripts/gsc_to_tsv.py`, `python3 scripts/site_urls.py`, `python3 scripts/build_sitetree.py`.
- **Result:** Sitetree migration map with 301 redirects and new page recommendations.

## 2. Real Task Solved by Hand (Step 2.3)
- **Reference Simulation:** Dumann dry run & Praxis Suriya live dataset.
- **Context Noted:**
  - Services must be locked first to prevent targeting irrelevant high-volume terms (e.g. cutting general physiotherapy if client specializes strictly in osteopathy).
  - Healthcare terms require strict HWG compliance checks (no before/after images, no healing guarantees).
  - Cities require DataForSEO `location_code` rather than ambiguous string names.
  - Numbers must be calculated by scripts; human edits are restricted to candidate classification tags.

## 3. Pipeline Map & Checkpoints (Step 2.4)

```
[Martin's Trigger: /content-pool <client>]
                    │
                    ▼
[Step 0–1: Readiness & Client Baseline]
                    │
                    ▼
[Step 2–4: Competitor SERPs + Autocomplete Demand]
                    │ (Raw JSON data)
                    ▼
[Step 5–7: Build Pool & Validate (0 errors)]
                    │
                    ▼
[Step 8: Render HTML Report]
                    │
                    ▼
         🛑 [ CHECKPOINT 1: Martin's Go ] ──> Approved pool-top.md
                    │
                    ▼
[Step 10–12: Sitetree Architecture & Redirect Map]
                    │
                    ▼
         🛑 [ CHECKPOINT 2: Martin's Go ] ──> Final sitetree.json & xlsx
```

## 4. Degrees of Freedom Breakdown (Step 2.5 - Rule R1.7)

| Step | Operation Type | Implementation | Degree of Freedom |
|---|---|---|---|
| Step 0: Input validation | Fragile / Deterministic | Check folder, balance, and GSC access | 0 (Strict script / gate) |
| Step 1: Client baseline | Qualitative | Read services & brand positioning | High (Prompt synthesis) |
| Step 2: Seed generation | Qualitative | Map services × locations × questions | Medium (Structured prompt) |
| Step 3: Competitor SERP | Deterministic | `dfs.py`, `site_urls.py`, `page_metrics.py` | 0 (Python scripts) |
| Step 4: Demand extraction | Deterministic | `autocomplete_tree.py`, GSC TSV export | 0 (Python scripts) |
| Step 5: Candidate classification | Qualitative / Judgment | Fit scoring (0–3), HWG compliance, pillar assignment | High (Agent heuristics) |
| Step 6: Pool aggregation | Deterministic | `build_pool.py` | 0 (Python script) |
| Step 7: Pool validation | Deterministic | `validate_pool.py` (0 errors required) | 0 (Python script) |
| Step 8: Report rendering | Deterministic | `render_report.py` (HTML + xlsx) | 0 (Python script) |
| Checkpoint 1 | Governance | Present HTML report; wait for Martin's Go | Human Gatekeeper |
| Step 10–12: Sitetree build | Deterministic | `build_sitetree.py` | 0 (Python script) |
| Checkpoint 2 | Governance | Present sitetree; wait for Martin's Go | Human Gatekeeper |
