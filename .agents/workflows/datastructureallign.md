---
description: In the beginning of the project we allign to thsi structure
---


741 Website Build System (Anti-Gravity + Git Workflow) This data is only for structure in the beginning of the project and doesnt need to be changed, it is just a helpful explainer.

1. Core Idea of the System

Every website project follows the exact same structure and workflow.

This allows developers or AI agents to:
	•	understand the project instantly
	•	access reference designs quickly
	•	follow branding rules automatically
	•	build sections independently
	•	avoid overriding other sections
	•	maintain clean Git version control
	•	push backups daily

Each website project works like a mini operating system with clear rules.

⸻

2. Standard Project Folder Structure (Anti-Gravity)

Every project must start with this structure.

/project-name
│
├── 00_project
│   ├── project-overview.md
│   ├── checklist.md
│   └── sitemap.json
│
├── 01_reference
│   ├── reference-site.html
│   ├── reference-sections/
│   └── screenshots/
│
├── 02_branding
│   ├── brand.json
│   ├── colors.json
│   ├── typography.json
│   └── logos/
│
├── 03_design
│   ├── wireframes/
│   └── section-plans/
│
├── 04_site
│   ├── index.html
│   ├── pages/
│   ├── sections/
│   ├── components/
│   └── assets/
│
├── 05_scripts
│   ├── build.sh
│   └── deploy.sh
│
├── 06_environment
│   ├── .env
│   └── api-config.json
│
└── README.md

This structure ensures:
	•	clear navigation
	•	modular website architecture
	•	safe development without section conflicts

⸻

3. Website Code Structure (Modern Frontend Standard)

Inside /04_site the website must follow modular development.

site/
│
├── index.html
│
├── components/
│   ├── header.html
│   ├── footer.html
│   └── navigation.html
│
├── sections/
│   ├── hero.html
│   ├── services.html
│   ├── testimonials.html
│   ├── cta.html
│
├── pages/
│   ├── home.html
│   ├── services.html
│   └── contact.html
│
├── assets/
│   ├── css/
│   ├── js/
│   └── images/

Each section exists independently.

This prevents:
	•	accidental layout breaks
	•	CSS conflicts
	•	component overrides

⸻

4. Website Creation Checklist

Create a checklist.md inside every project.

⸻

Phase 1 — Project Setup

[ ] Create project folder
[ ] Initialize Git repository
[ ] Connect GitHub remote repo
[ ] Create base folder structure
[ ] Create README.md


⸻

Phase 2 — Reference Research

[ ] Find reference websites
[ ] Save reference HTML
[ ] Save screenshots of key sections
[ ] Extract reusable components
[ ] Document layout structure

Typical website structure:

Hero
Features
Services
Testimonials
Pricing
CTA
Footer


⸻

Phase 3 — Branding Setup (MANDATORY BEFORE DEVELOPMENT)

Before any design or coding begins, create brand.json.

Example:

{
 "brand_name": "",
 "primary_color": "",
 "secondary_color": "",
 "font_primary": "",
 "font_secondary": "",
 "button_style": "rounded",
 "image_style": ""
}

Checklist:

[ ] Create brand.json
[ ] Define colors
[ ] Define typography
[ ] Save logo files
[ ] Define UI style

Branding must be completed before section development begins.

⸻

Phase 4 — Sitemap Planning

Create sitemap.json.

Example:

{
 "pages":[
  "home",
  "services",
  "about",
  "contact"
 ]
}

Checklist:

[ ] Define website pages
[ ] Define navigation structure
[ ] Define landing pages
[ ] Define SEO pages

This step is critical for Local SEO structure.

⸻

5. Section-Based Development Process

Websites must be built section-by-section, never all at once.

Example section checklist:

[ ] Hero
[ ] Value Proposition
[ ] Services
[ ] Testimonials
[ ] About
[ ] CTA
[ ] Footer

Each section is saved in:

/04_site/sections

Example:

hero.html
services.html
testimonials.html
cta.html
footer.html


⸻

6. Modification Boundary Rules (MB Rules)

To prevent code conflicts, each task must define:

Modification Scope
Allowed Files
Forbidden Files

Example task:

Update Services Section

Allowed files:

sections/services.html
assets/css/services.css

Forbidden files:

components/header.html
components/footer.html
sections/hero.html
assets/css/global.css

This prevents accidental overrides of other sections.

⸻

7. Reference Code Preservation Rule

Reference HTML must remain structurally unchanged unless explicitly approved.

Allowed modifications:

text
images
icons
colors
branding classes

Not allowed:

changing HTML hierarchy
removing wrapper containers
modifying grid system
modifying scroll behavior

If structural changes are required, confirmation must be requested.

⸻

8. Daily Development Workflow

Developers must follow this daily workflow.

1 Pull latest Git repository
2 Work on assigned section
3 Test locally
4 Commit changes
5 Push to GitHub

Example commit:

git add .
git commit -m "services section completed"
git push


⸻

9. End-of-Day Backup Protocol

Every development day must end with:

[ ] Git commit
[ ] Git push
[ ] Checklist update
[ ] Progress log update

Example progress log:

Day 1
- project setup
- hero section created
- navigation component created


⸻

10. Agent Instruction File

Each project must include:

agent-rules.md

Example:

1 Always check brand.json before styling
2 Preserve reference HTML structure
3 Store sections in /sections folder
4 Do not modify global components
5 Follow modification boundaries
6 Commit work after completing each section
7 Keep code modular


⸻

11. Environment & API Setup

If APIs are required, configure environment variables.

Example .env

GOOGLE_MAPS_KEY=
STRIPE_KEY=
FORM_ENDPOINT=

Checklist:

[ ] create .env file
[ ] configure API keys
[ ] test integrations


⸻

12. Deployment Checklist

Before deploying the website:

[ ] compress images
[ ] run Lighthouse test
[ ] test mobile responsiveness
[ ] test forms
[ ] verify SEO metadata
[ ] push final build
[ ] upload to server


⸻

13. Lighthouse & SEO Quality Standard

Minimum performance requirements:

Performance 80+
Accessibility 80+
SEO 80+
Best Practices 80+


⸻

14. README Template

Every project requires a README containing:

Project Name
Client
Project Goal
Branding Rules
Website Pages
Reference Websites
Deployment Instructions


⸻

15. Template Repository (Recommended)

Create a reusable GitHub template:

website-template

Every new website should start from this template.

Benefits:
	•	faster project creation
	•	consistent structure
	•	easier onboarding for developers
	•	better AI agent compatibility

⸻

Final Goal

This system allows:
	•	safe modular development
	•	AI-assisted website building
	•	Git version control
	•	fast onboarding of new developers
	•	scalable website production

Which is exactly what you need to scale 741 Studio.

