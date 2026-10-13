# Night Shift + Server — hosting options

Status: decision N1 taken 2026-10-13 (Martin): **Hybrid — VPS in Germany for headless night work, Chrome tasks stay on the laptop.**
Facts: `00_project/knowledge/ops-library/_derived/night-shift-server-facts.md` (official docs fetched 2026-10-13). Prices marked "3rd party" come from N03 (2026-09-06). Check them before buying.

| Option | Cost / month | Setup effort | Chrome with Martin's login | MCP / local tools | Limits | Risk |
|---|---|---|---|---|---|---|
| **A Hybrid: Hetzner VPS Nuremberg + laptop for Chrome (chosen)** | CX43 EUR 16.49 excl. VAT (Hetzner page 13.10.; decision N18) + plan usage | Medium: 1 evening for Martin's steps (account, Tailscale, tokens), agent does hardening + install | No (laptop keeps Chrome work as morning click cards) | Yes: local scripts, `.secrets` read keys, Local Falcon remote MCP, Playwright headless | Night runs share the Max plan limits (N2) → cap 14 runs / est. USD 10 | Keys on a rented box → read keys only, Tailscale, non-root user, deny rules |
| B Home desktop + Tailscale | 0 (power) | Low–medium | Yes, possible (visible Chrome with login) | Yes | Same plan limits | Power or Wi-Fi drop in Bali stops the night; same-Wi-Fi SSH today; desktop also holds personal data |
| C Anthropic cloud routines | 0 extra (plan usage) | Low | No | No `.secrets`, no local MCP, no unpushed files; claude.ai connectors only | 1 h min interval; no approvals; runs fully autonomous | Every connector tool runs without asking; most 741 night work cannot run |
| D Claude Managed Agents | Tokens at API rates + USD 0.08 per running hour; can use the Max API credit | High: rebuild on the API | No | Own sandbox; vault secrets; no local repo | Hard USD cap per session; `always_ask` approvals | Low infra risk; big rebuild; not eligible for ZDR |
| E GitHub Actions cron | GitHub minutes + plan or API | Medium | No | Repo only | Job timeouts | Repo secrets; no phone approvals |
| F Mac mini at home / MacStadium | Mac mini from about USD 109 hosted (3rd party) | Medium | Yes | Yes (macOS, same as laptop) | Same plan limits | Highest cost; useful only if Chrome nights become important |

## Why A

1. The night work needs local scripts and read keys. C cannot reach them. D means a rebuild.
2. Martin's laptop can sleep. B depends on home power and Wi-Fi in Bali.
3. Germany (Nuremberg) keeps client data in the EU, next to Supabase Frankfurt (DSGVO).
4. Chrome-bound work does not need the night. It becomes "Your click" cards at 06:13.

## Upgrade path (not now)

- If night runs eat too much of the weekly limit: switch the server to an API key from the Max API credit (N2 revision, one env change) — the runner already reads `total_cost_usd`.
- If Chrome work at night becomes important: option F, or B with a stable power supply.
- Never use the AltusHost cPanel VPS (client production sites; memory `dev-vps-setup-plan`).
