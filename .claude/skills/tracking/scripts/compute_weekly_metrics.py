#!/usr/bin/env python3
"""741 Tracking Metric Computation Engine (STE).

Computes weekly/monthly metric rollups, WoW/MoM deltas, goal discrepancies,
and cost-per-booked-job metrics for client reporting.

Usage:
  python3 compute_weekly_metrics.py --client <client_id> [--start <date>] [--end <date>]
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone, timedelta

def compute_delta(current, baseline):
    if baseline is None or baseline == 0:
        return 0.0
    return round(((current - baseline) / baseline) * 100.0, 1)

def compute_cpa(spend, conversions):
    if conversions is None or conversions == 0:
        return None
    return round(spend / conversions, 2)

def evaluate_client_metrics(client_id, data):
    calls = data.get("gbp_calls", 0)
    prev_calls = data.get("prev_gbp_calls", 0)
    calls_delta = compute_delta(calls, prev_calls)

    impressions = data.get("gsc_impressions", 0)
    prev_impressions = data.get("prev_gsc_impressions", 0)
    impressions_delta = compute_delta(impressions, prev_impressions)

    leads = data.get("form_leads", 0)
    prev_leads = data.get("prev_form_leads", 0)
    leads_delta = compute_delta(leads, prev_leads)

    booked_jobs = data.get("booked_jobs", 0)
    total_spend = data.get("total_spend", 0.0)
    cpa = compute_cpa(total_spend, booked_jobs)

    # Goal discrepancy: Delta = Actual - Goal
    target_leads = data.get("target_leads", 15)
    lead_gap = leads - target_leads

    return {
        "client_id": client_id,
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
        "metrics": {
            "gbp_calls": {"current": calls, "previous": prev_calls, "delta_pct": calls_delta},
            "gsc_impressions": {"current": impressions, "previous": prev_impressions, "delta_pct": impressions_delta},
            "form_leads": {"current": leads, "previous": prev_leads, "delta_pct": leads_delta},
            "booked_jobs": booked_jobs,
            "total_spend_eur": total_spend,
            "cost_per_booked_job": cpa,
            "goal_discrepancy": {
                "target_leads": target_leads,
                "actual_leads": leads,
                "delta": lead_gap,
                "status": "on_track" if lead_gap >= 0 else "behind"
            }
        }
    }

def main():
    parser = argparse.ArgumentParser(description="741 Weekly Metric Computation Engine")
    parser.add_argument("--client", required=True, help="Client identifier (slug or UUID)")
    parser.add_argument("--input-json", help="Path to input metrics JSON file (optional)")
    args = parser.parse_args()

    data = {}
    if args.input_json and os.path.exists(args.input_json):
        with open(args.input_json, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        # Fallback / sample baseline for offline demonstration
        data = {
            "gbp_calls": 14,
            "prev_gbp_calls": 11,
            "gsc_impressions": 1420,
            "prev_gsc_impressions": 1268,
            "form_leads": 4,
            "prev_form_leads": 3,
            "booked_jobs": 3,
            "total_spend_eur": 120.0,
            "target_leads": 15
        }

    results = evaluate_client_metrics(args.client, data)
    print(json.dumps(results, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
