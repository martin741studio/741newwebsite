# 741 Tracking Metric Catalog (STE Reference)

Version 1.0 · 2026-10-16

---

## 1. Primary Core Metrics (v1 Active)

| ID | Metric Name | Source Channel | Granularity | Description |
|---|---|---|---|---|
| **M01** | `gbp_phone_calls` | Local Falcon GBP read | Weekly | Direct phone call clicks on GBP listing |
| **M02** | `gbp_website_clicks` | Local Falcon GBP read | Weekly | Clicks from Google profile to website |
| **M03** | `gbp_direction_requests` | Local Falcon GBP read | Weekly | Route planning requests |
| **M04** | `gbp_total_interactions` | Local Falcon GBP read | Weekly | Sum of M01 + M02 + M03 |
| **M05** | `form_leads` | Supabase `leads` | Daily / Weekly | Inquiries submitted via site contact forms |
| **M06** | `phone_leads_logged` | Supabase `leads` | Weekly | Phone calls manually confirmed by client |
| **M07** | `booked_jobs` | Supabase `leads` | Weekly / Monthly | Inquiries marked as "gebucht" with value |
| **M08** | `conversion_rate_leads_to_booked` | Computed | Weekly / Monthly | `(booked_jobs / total_leads) * 100` |
| **M09** | `cost_per_booked_job` | Computed | Monthly | `total_monthly_spend / booked_jobs` |
| **M10** | `total_spend_eur` | Supabase `google_campaigns` + fee | Monthly | 741 Retainer + Paid ad budget |
| **M13** | `maps_average_rank_arp` | Local Falcon Grid | Monthly | Average rank position across 7x7 grid points |
| **M14** | `maps_share_of_local_voice_solv`| Local Falcon Grid | Monthly | Share of Local Voice percentage |
| **M20** | `google_review_average` | GBP API | Weekly | Lifetime rating average (1.0 to 5.0) |
| **M21** | `gsc_total_clicks` | Supabase `gsc_daily_performance` | Weekly | Total organic search clicks |
| **M22** | `gsc_total_impressions` | Supabase `gsc_daily_performance` | Weekly | Total organic search impressions |

## 2. Invariant Rules of Calculation
1. **Never Estimate:** If a client hasn't updated booking status for phone leads, record "fehlt seit <Datum>"; leave CAC uncalculated rather than guessed.
2. **Deterministic Scripts:** All percentages, averages, and deltas must be evaluated via `scripts/compute_weekly_metrics.py`.
