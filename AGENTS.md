# Global Agent Guidelines & Rules

## WordPress Client-Editable Text Boxes (Hard-Coded Rule)
Never put raw HTML tags (`<span>`, `<br>`, `<strong>`, `<div>`, inline style attributes, etc.) inside text boxes, headings, or fields where clients make text edits.

- Clients get confused by HTML tags, accidentally delete tags, or break layouts.
- Client-facing text inputs must remain strictly **plain text**.
- All styling, color accents, line breaks, and font settings must be handled natively through widget controls, theme styling, dedicated sub-fields, or CSS classes on the container/wrapper.

## Client Roadmap & Milestone Pre-Flight (Hard-Coded Rule)
Whenever an agent begins work on a client (e.g. Talkinfive, Praxis Suriya, Stürzl, Katharina Kisser), the agent MUST inspect the client's roadmap before proposing or executing changes:
- Run: `python3 .claude/skills/client-roadmap/scripts/get_roadmap.py <client>` (or read `00_project/assets/<client>/roadmap.json`).
- Announce active milestone and primary constraint:
  `[741 ROADMAP ACTIVE] <Client> · Active Milestone: M<x> (<Title>)`
- Agents must strictly align tasks with the active milestone ($M_1 \to M_4$) and never drift into unapproved changes.

