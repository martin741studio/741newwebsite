# 741 Developer Onboarding & First Task Briefing

**Recipient:** Dinakar (`dinakar@741.studio`)  
**From:** Martin Drendel (`741 Studio`)  
**Date:** 2026-10-16  
**Role:** Delivery Engineer / Frontend Developer  

---

## 1. Welcome to 741 Studio

Welcome to the 741 delivery team, Dinakar! 

You are joining our client execution flow where high-precision engineering meets automated intelligence. To get you started smoothly, your account has been provisioned and your first client task is assigned.

### Your Portal Access
* **Portal URL:** `https://clients.741.studio/`
* **Login Email:** `dinakar@741.studio`
* **Initial Password:** `Dinakar741!Studio#2026` *(please change upon first login)*
* **Role:** `delivery`
* **Actor ID:** `598feba9-7b77-4d5a-8aae-3905325b1338`

---

## 2. Operations Guide & Workflow Rules

Before starting, please review our master playbook in [`README.md`](file:///Users/martindrendel/741website/README.md).

### Core Working Principles
1. **Supabase is the Single Source of Truth (`public.work_items`, `public.decisions`):**
   * All task assignments, statuses, and links live in the database.
2. **Dual-Storage Operational Layer (Google Drive):**
   * Working assets, mockups, and client deliverables are organized under Google Drive:  
     `741 Clients / <Client Name> /`
3. **The Proof Protocol (Rule 02-8 / 03-9):**
   * When you finish work on a task, you update its status to **`needs_check`** and attach proof (screenshot, URL, or commit hash).
   * Postgres triggers strictly enforce that only human sign-off (`verified_by: Martin`) moves a task to **`done`** once valid evidence is attached in `public.work_evidence`.
   * Never leave a task without verifiable proof.

---

## 3. First Assigned Task: Praxis Suriya

* **Client:** Praxis Suriya (Heilpraktikerin Coralie & Team)
* **Website:** `https://praxis-suriya.de`
* **CMS:** WordPress + Elementor Pro
* **Task ID:** `591bfc3a-a856-4914-9ae7-f20b2baa5f06`
* **Task Title:** *Fix footer: link Impressum + Datenschutz (pages exist, just not linked)*
* **Current Status:** `in_progress` (Assigned to Dinakar)
* **Priority:** Normal

### Task Scope & Steps
1. **Access WordPress Admin for Praxis Suriya:**
   * Navigate to `Templates > Theme Builder > Footer` (or the global footer container in Elementor).
2. **Inspect Existing Pages:**
   * Verify target pages:
     * Impressum: `https://praxis-suriya.de/impressum/`
     * Datenschutz: `https://praxis-suriya.de/datenschutz/`
3. **Set Links in Footer:**
   * Connect the text elements "Impressum" and "Datenschutz" to their respective relative URLs (`/impressum/` and `/datenschutz/`).
   * Ensure links open in the same tab (`_self`) and adhere to standard legal compliance styling.
4. **Testing:**
   * Test clickability on both Desktop and Mobile viewport sizes.
   * Verify that no layout shift or visual breakage occurs.
5. **Handover & Proof:**
   * Take 1 desktop screenshot and 1 mobile screenshot showing the clickable footer links.
   * Update the task in the portal or notify Martin with the proof URL/screenshot to set status to **`needs_check`**.

---

## 4. Questions & Support
If you have any questions or need WordPress credentials, reach out directly to Martin via Telegram or agency email (`martin@741.studio`).
