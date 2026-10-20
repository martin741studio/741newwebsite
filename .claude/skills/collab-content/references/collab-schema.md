# Collaboration Specification Schema (`spec.json`)

## Table of Contents
1. Top-Level Fields
2. Partner Specification
3. Synergy Matrix
4. Selected Angle
5. Reciprocal Article Schemas

---

### 1. Top-Level Fields
- `client`: String. Canonical client slug matching `00_project/assets/<client>/`.
- `partner`: Object. Partner metadata and service offerings.
- `synergy`: Object. Extracted mutual value propositions.
- `selected_angle`: Object. The approved angle chosen at Checkpoint 1.
- `articles`: Object. Mapping of client-side and partner-side article specifications.
- `status`: String. One of `mini_pool_ready`, `angle_approved`, `drafted`, `linted`, `published`.

### 2. Reciprocal Article Invariants
- `target_site`: Domain where the article will be hosted.
- `target_url`: The exact deep link URL pointing to the featured partner's relevant service page.
- `anchor_text`: Descriptive, non-spammy phrase contextually embedded in paragraph copy.
- `file_path`: Path relative to `00_project/assets/<client>/collab/<partner-slug>/`.
