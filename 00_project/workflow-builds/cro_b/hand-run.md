# Step 2.3 Hand-Run Documentation: STÜRZL Steuerstrafrecht Track B Pilot

Date: 2026-10-16
Client: Dr. Anja Stürzl (STÜRZL Steuerstrafrecht, München & Frankfurt)
Location: `00_project/assets/stuerzl/cro-b/`
Workflow: `cro_b` (CRO Track B Design-Intense Showcase)
Participants: Martin Drendel & Agent

---

## 1. Context and Objective
Dr. Stürzl is a high-ticket legal client paying €7,999 + Ads retainer. In addition to the calm, standard Track A prototype (`../cro/`), Martin requested a design-intense Track B variant ("Variante B: Briefbogen") to give the client a tangible choice reflecting the high prestige of corporate criminal tax defense in Frankfurt and Munich.

## 2. Hand-Run Execution Sequence

### Phase 1: Intake & Data (B0–B1)
- B0 Questionnaire completed in `00-brief-b/brief-b.md`. Established the "Briefbogen" aesthetic, emotional state of target clients (high stress, shame, demand for discretion), and strict Anwaltswerbe-Check rules (no handcuffs, no scales of justice, no fear graphics, address form Sie).
- Reused verified brand facts from Track A (`01-input/INVENTORY.md`, `02-data/brand.md`, `02-data/dataset.md`). Locked colors: Anthrazit `#323335`, Salbei `#8DA38E`, CTA-Salbei `#4E6F55`, Creme `#F4F1EC`.

### Phase 2: Reference Board & Live Element Pool (B2–B2b)
- Curated 5 references and element catalog in `02-data/elements-catalog.md`.
- Built live interactive Element Pool in `00-element-pool/index.html` and `pool2.html` featuring interactive cards with live hover, scroll, and SVG animations.
- Martin reviewed the live pool in browser and voted on elements:
  - Ja: Large condensed serif headline, subtle animated wave separator, illuminated paragraph focus, numbered case step blocks, discreet plus-FAQ, dark emergency closing banner.
  - Nein: Gimmicky cursor followers, game mechanics, excessive 3D motion.
- Stored votes into `votes.json`.

### Phase 3: Concept & Storyboard (B4)
- Formulated signature idea: *"Der digitale Briefbogen"* — an editorial, architectural layout evoking high-end legal stationery with subtle kinetic line drawings.
- Mapped section storyboard in `05-gpt-design-doc/concept/concept.md` ensuring every motion component has a conversion rationale.

### Phase 4: Build & Motion Layer (B7)
- Coded desktop 1440px HTML prototype with custom SVG line animations, CSS smooth transitions, and an integrated X-ray switch (`key 'x'` and `?xray=1`).
- Included full `prefers-reduced-motion` CSS overrides ensuring zero layout breakage when animations are disabled.

### Phase 5: Verification & Handoff (B8–B9)
- Executed visual check and self-check (`07-prototype/visual-check.md`, `07-prototype/self-check.md`).
- Verified performance budget (<2.5 MB above fold, zero layout shifts).
- Assembled handoff pack (`08-handoff/handoff.md`) with component documentation, CMS implementation notes, and staged Drive files in `_drive/`.

## 3. Key Takeaways for Meta-Architecture
1. **Live Element Pool is Essential:** Martin cannot reliably vote on written animation descriptions; he must interact with working demos in client brand colors.
2. **Strict Component Cap:** Limiting interactive components to maximum 4 prevents visual clutter and protects Core Web Vitals.
3. **Safety First:** Upload guard (`guard_upload.py`) prevents accidental deployment of prototypes to client staging or production servers.
