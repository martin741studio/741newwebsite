# Research Note: P4/P0 CRO Track B Design-Intense Showcase (`cro_b`)

Date: 2026-10-16
Author: 741 Architecture Agent & Martin Drendel

## 1.1 Building Block Selection
- **Selected Block:** Skill (`cro-track-b`), registered in `workflow_registry.py` under ID `cro_b`.
- **Rationale:** CRO Track B requires a rich, multi-step interactive workflow combining autonomous drafting with mandatory human-in-the-loop checkpoints (B0 Grill-Me questionnaire, B2b interactive Element Pool voting, CP1 copy/concept approval, CP2 prototype verification). A skill package (`SKILL.md` + `scripts/` + `assets/`) is the approved architecture for complex, stateful agency workflows.

## 1.2 Library Search
- **Grep Query:** Searched `00_project/knowledge/workflow-library/` for design verification, visual checks, and interactive component patterns.
- **Key Findings:** Official Claude Code documentation mandates visual verification loops (`best-practices.md`), explicit gate verification scripts (`common-workflows.md`), and safety hooks (`hooks-guide.md`) for destructive or unauthorized actions.

## 1.3 Library Freshness
- `00_project/knowledge/workflow-library/INDEX.md` last updated 2026-10-11 (5 days old; fully active and valid within the <3 month threshold).

## 1.4 Existing 741 Assets Coverage Map
- `00_project/cro-track-b-design-intense-workflow.md`: Complete 133-line master specification defining 10 steps (B0–B9), motion rules, and 10 QA checks.
- `00_project/cro-track-b-questionnaire.md`: 3-round B0 questionnaire preventing vague client/agency assumptions.
- `00_project/assets/stuerzl/cro-b/`: Production-grade pilot run for STÜRZL Steuerstrafrecht (`00-brief-b`, `00-element-pool` with live HTML + python voting server, `04-copy`, `05-gpt-design-doc`, `07-prototype`, `08-handoff`).
- `00_project/cro-homepage-motion-spec.md` & `00_project/cro-homepage-visual-check.md`: Existing baseline motion & QA specifications reused with explicit Track B extensions.

## 1.5 Research Synthesis
CRO Track B is not a redesign of Track A; it is an elevated design layer for clients whose market or brand demands an interactive showpiece (e.g. boutique corporate law, high-end design agencies, premium SaaS). Track B preserves all non-negotiable conversion constraints (above-the-fold CTA at 701px, single CTA color, zero HWG/BRAO violations) while adding: (1) an interactive live Element Pool for voting on micro-interactions, (2) a distinct signature idea, (3) a code-based motion layer with reduced-motion support, (4) a hidden X-ray switch (`?xray=1` or `x`), and (5) a strict 10-point Track B QA suite.
