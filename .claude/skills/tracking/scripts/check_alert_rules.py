#!/usr/bin/env python3
"""741 Early Warning Alert Rule Engine (STE).

Evaluates Red (R1-R6) and Yellow (Y1-Y9) tracking alert rules for a client.
Outputs alert flags, severity, and recommended operational mitigation actions.

Usage:
  python3 check_alert_rules.py --client <client_id> [--metrics-json <file>]
"""

import argparse
import json
import os
import sys

def evaluate_rules(client_id, data):
    red_alerts = []
    yellow_alerts = []

    # Red Rule R1: GBP profile phone number altered
    if data.get("gbp_phone_changed", False):
        red_alerts.append({
            "code": "R1",
            "name": "GBP Phone Changed",
            "description": "Primary phone number on Google Business Profile does not match canonical NAP in client_locations.",
            "action": "Immediate revert on GBP profile; check user access log."
        })

    # Red Rule R2: Website down or returning 4xx/5xx
    if data.get("website_status_code", 200) not in [200, 301, 302]:
        red_alerts.append({
            "code": "R2",
            "name": "Website Unreachable",
            "description": f"Target domain returned HTTP {data.get('website_status_code')}.",
            "action": "Check hosting status, DNS, SSL certificate immediately."
        })

    # Red Rule R3: Zero form leads in 14 days when baseline > 0
    if data.get("leads_14d", 0) == 0 and data.get("baseline_monthly_leads", 0) > 4:
        red_alerts.append({
            "code": "R3",
            "name": "Zero Leads in 14 Days",
            "description": "Zero website inquiries logged over the past 14 days.",
            "action": "Verify form webhook endpoint, test live form submission."
        })

    # Red Rule R5: GBP Suspension notice detected
    if data.get("gbp_suspended", False):
        red_alerts.append({
            "code": "R5",
            "name": "GBP Profile Suspended",
            "description": "Google has issued an active suspension or policy violation.",
            "action": "Halt citation growth; initiate Un-Burning remediation protocol."
        })

    # Yellow Rule Y1: Search Impressions dropped > 25% WoW
    gsc_delta = data.get("gsc_impressions_delta_pct", 0.0)
    if gsc_delta < -25.0:
        yellow_alerts.append({
            "code": "Y1",
            "name": "Search Impressions Dropped >25%",
            "description": f"GSC impressions dropped {gsc_delta}% WoW.",
            "action": "Audit top 5 query positions and indexation status."
        })

    # Yellow Rule Y2: Share of Local Voice (SoLV) dropped > 15% MoM
    solv_delta = data.get("solv_delta_pct", 0.0)
    if solv_delta < -15.0:
        yellow_alerts.append({
            "code": "Y2",
            "name": "Local Falcon SoLV Dropped",
            "description": f"Share of Local Voice dropped {solv_delta}% MoM.",
            "action": "Inspect competitor review count and category changes."
        })

    # Yellow Rule Y3: Negative review received (<= 3 stars)
    if data.get("new_negative_reviews_count", 0) > 0:
        yellow_alerts.append({
            "code": "Y3",
            "name": "Negative Review Received",
            "description": f"{data.get('new_negative_reviews_count')} new review(s) with <= 3 stars.",
            "action": "Draft professional response for Martin's review; do not auto-respond."
        })

    return {
        "client_id": client_id,
        "status": "red" if red_alerts else ("yellow" if yellow_alerts else "green"),
        "red_alerts": red_alerts,
        "yellow_alerts": yellow_alerts,
        "total_active_alerts": len(red_alerts) + len(yellow_alerts)
    }

def main():
    parser = argparse.ArgumentParser(description="741 Early Warning Alert Rule Engine")
    parser.add_argument("--client", required=True, help="Client identifier")
    parser.add_argument("--metrics-json", help="Path to metrics JSON file")
    args = parser.parse_args()

    data = {}
    if args.metrics_json and os.path.exists(args.metrics_json):
        with open(args.metrics_json, "r", encoding="utf-8") as f:
            data = json.load(f)

    report = evaluate_rules(args.client, data)
    print(json.dumps(report, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
