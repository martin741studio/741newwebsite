# 741 Studio — Local-SEO Retargeting Plan (Demand Gen)

Decided 2026-07-30. Retarget **all past website visitors** with the Local-SEO offer, split by location:
DACH → German ads + German LP; everyone else → English ads + English LP.

## Foundation (already in place)
- **Remarketing tag live site-wide:** `AW-564129015` (added via the consent partial today, Consent-Mode-v2-gated). Google Ads is already forming the **"All visitors"** data segment for marketing-consented visitors.
- ⚠️ **List is ~1 day old / near-empty.** Demand Gen needs **≥100 users** in the audience before it serves; it will ramp over days/weeks. RLSA (1,000 users) is a later phase.
- **Pre-req to confirm at build:** Audience Manager → "Your data segments" → ensure remarketing/data collection is ON and the "All visitors" segment exists & is growing.

## Structure — two Demand Gen campaigns (location is campaign-level, so it must be split)
| | Campaign A — DACH | Campaign B — International |
|---|---|---|
| Type | Demand Gen | Demand Gen |
| Locations | Germany, Austria, Switzerland (Presence) | All countries **except** DE/AT/CH (or Worldwide, DACH excluded) |
| Audience | "All visitors" data segment | "All visitors" data segment |
| Ads | German | English |
| Final URL | https://741.studio/de/pages/local-seo.html | https://741.studio/pages/local-seo.html |
| Business name | 741 Studio | 741 Studio |

Budget (proposed): **€5/day each (€10/day total)** to start — the small list won't fully spend anyway; scale as it grows. Bidding: Maximise clicks (or Max conversions once the Lead conversion has data).

## Ad copy — English (Campaign B)
**Headlines (≤40):** Still thinking about local SEO? · Get found on Google Maps · Rank in your local area · Local SEO that actually ranks · Free local visibility audit · More customers from Google · Your free Maps ranking check
**Descriptions (≤90):** See exactly where you rank on Google Maps — and how to reach the top 3. · Local visibility that brings calls, not just clicks. Free audit first. · A personal video audit of your Google presence — no cost, no obligation.
**CTA:** Learn more · **Business name:** 741 Studio

## Ad copy — German (Campaign A)
**Headlines (≤40):** Noch am Local SEO dran? · Bei Google Maps gefunden werden · In deiner Region ganz oben · Local SEO, das wirklich rankt · Kostenlose Sichtbarkeits-Analyse · Mehr Kunden über Google · Dein Maps-Ranking-Check
**Descriptions (≤90):** Sieh, wo du bei Google Maps stehst – und wie du in die Top 3 kommst. · Lokale Sichtbarkeit, die Anrufe bringt, nicht nur Klicks. Erst kostenlose Analyse. · Persönliche Video-Analyse deiner Google-Präsenz – kostenlos & unverbindlich.
**CTA:** Mehr erfahren · **Business name:** 741 Studio

## Assets needed (Demand Gen is image-based)
Per campaign: **logo** (have `logo_white.png`), landscape **1.91:1**, square **1:1**, portrait **4:5** (optional but recommended). Candidate source imagery already on site: the Google-Maps before/after rank images, analytics_*.webp. **Need Martin to supply/approve final visuals or OK using existing site assets.**

## Open inputs before launch
1. **Budget** — confirm €5+€5/day or set your own.
2. **Images** — supply brand visuals or approve me using existing site assets + logo.
3. Publish is spend-gated → the final "publish" click hits the passkey/auth wall and must be Martin's.
