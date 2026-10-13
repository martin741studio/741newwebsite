# Commit proposal for the server (decision N21) — 2026-10-13

Measured: 9,615 untracked files, 1.44 GB. Nothing committed yet. Martin ticks groups; the agent then commits only those paths and pushes after Martin's go.

| Group | Paths | Size | Night needs it? | Proposal |
|---|---|---|---|---|
| G1 Workflow + knowledge text (CHOSEN N22) | `00_project/knowledge/`, `00_project/*-skill/`, `00_project/*-workflow/`, `00_project/client-*`, `00_project/prospect-mini/`, `00_project/workflow-registry/`, `00_project/cro-registry/`, `00_project/*.md`, `reporting/*` scripts | ~60 MB | yes: skills, rules, specs | commit to GitHub |
| G2 Client text in assets | `00_project/assets/**` without media (md, json, html, csv, py) + `00_project/prospects/` text, `00_project/maria-brasse-pages/` | ~150 MB | yes: client context, briefs, past drafts | commit to GitHub |
| G3 Client media | images, video, PDF, audio in `00_project/assets/` | ~1.06 GB | rarely (screenshots, logos) | rsync once to the server over Tailscale, not to GitHub |
| G4 Site build output | `dist/`, `04_site/public/`, `04_site/review/`, `07_social/output/` | ~160 MB | no (generated, deployed by day) | stays on the laptop |

Check before commit: no secrets (scan for keys/passwords), no file > 50 MB, `.DS_Store` ignored.
