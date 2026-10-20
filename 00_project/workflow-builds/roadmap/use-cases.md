# Use Cases: Client Roadmap & Goal Engine (`roadmap`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `roadmap`

---

## Use Case 1: Initial Roadmap Creation from Client Audit & Competitor Benchmark
- **Trigger:** "Erstelle die Roadmap für <Kunde>" or `/client-roadmap create <client>`
- **Prerequisites:** Client exists in Supabase `public.clients`. Technical audit file or URL available.
- **Steps:**
  1. Script ingests client audit metrics (PageSpeed, TTFB, media weight, SEO ranking baseline).
  2. Script/Agent fetches niche benchmark data (from competitor scrapes or established 741 standards).
  3. Gap Analysis: Computes $\Delta = \text{Client Baseline} - \text{Market Benchmark}$.
  4. Synthesizes North Star Goal and decomposes it into 3–4 sequential milestones ($M_1 \to M_4$).
  5. Presents draft roadmap to Martin for approval via Decision Card.
  6. Writes approved roadmap to `00_project/assets/<client>/roadmap.json` and updates Supabase `client_goals`.
- **Tools:** `read_file`, `search_web`, `write_to_file`, `ask_question`, Supabase REST/SQL.
- **Result:** Machine-readable `roadmap.json` established as the operational baseline for all subsequent agent work.

---

## Use Case 2: Agent Pre-Flight Ingestion (Mandatory Orientation at Chat Start)
- **Trigger:** Any agent chat or subagent session started to work on a client asset (e.g. "Mach Brand Atlas schneller" or "Überarbeite die Ayurveda-Seite").
- **Steps:**
  1. Agent automatically detects client entity and loads `00_project/assets/<client>/roadmap.json` (or calls `scripts/get_roadmap.py <client>`).
  2. Reads active milestone, client rules, and pending blockers.
  3. Outputs a concise 2-line pre-flight confirmation:
     `[ROADMAP ACTIVE] Kunde: <Name> | Phase: <Phase> | Aktiver Meilenstein: M<x> (<Title>)`
  4. Constrains execution strictly within the scope of the active milestone and client rules.
- **Tools:** `view_file` or `run_command` (`python3 scripts/get_roadmap.py`).
- **Result:** Zero blind drift; agent executes only within approved milestone boundaries.

---

## Use Case 3: Milestone Telemetry Update & Downstream Unlock
- **Trigger:** Completion of a specific client task (e.g. 3 GIFs converted to video, WP Fastest Cache activated).
- **Steps:**
  1. Agent runs programmatic verification (e.g. HTTP status, file size check, TTFB test).
  2. Emits standardized `00_project/assets/<client>/roadmap/_run.json` containing metrics.
  3. Updates `roadmap.json`: Marks current milestone task as `completed`, records completion timestamp, and evaluates gate for next milestone.
  4. Syncs updated milestone state to Supabase `work_goals` and `morning-grill-goals.json`.
- **Tools:** `run_command`, `write_to_file`, `replace_file_content`.
- **Result:** Telemetry permanently captured; next agent immediately picks up where the last agent stopped.
