#!/usr/bin/env python3
"""741 Client Roadmap - Agent Pre-Flight Reader.

Outputs the active milestone, target goals, and operational constraints
for any client in 00_project/assets/<client>/roadmap.json.
"""
import sys
import os
import json

ROOT = "/Users/martindrendel/741website"
ASSETS_DIR = os.path.join(ROOT, "00_project", "assets")

def resolve_client_dir(client_query):
    query = client_query.lower().strip()
    # Direct match
    direct = os.path.join(ASSETS_DIR, query)
    if os.path.isdir(direct):
        return direct
    
    # Fuzzy / alias match
    aliases = {
        "celine": "talkinfive",
        "coralie": "suriya",
        "kisser": "katharina-kisser",
        "anja": "stuerzl"
    }
    target = aliases.get(query, query)
    match_dir = os.path.join(ASSETS_DIR, target)
    if os.path.isdir(match_dir):
        return match_dir
    
    # Substring search
    for item in os.listdir(ASSETS_DIR):
        p = os.path.join(ASSETS_DIR, item)
        if os.path.isdir(p) and query in item.lower():
            return p
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: get_roadmap.py <client_name_or_slug>", file=sys.stderr)
        sys.exit(1)
        
    client_name = sys.argv[1]
    client_dir = resolve_client_dir(client_name)
    
    if not client_dir:
        print(f"[ROADMAP WARNING] No client folder found for: {client_name}", file=sys.stderr)
        sys.exit(1)
        
    roadmap_path = os.path.join(client_dir, "roadmap.json")
    if not os.path.exists(roadmap_path):
        print(f"[ROADMAP MISSING] No roadmap.json found in {client_dir}", file=sys.stderr)
        sys.exit(2)
        
    with open(roadmap_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    client = data.get("client", os.path.basename(client_dir))
    phase = data.get("phase", "P4")
    north_star = data.get("north_star_goal", {}).get("title", "No primary goal specified")
    
    # Find active milestone
    milestones = data.get("milestones", [])
    active_m = None
    for m in milestones:
        if m.get("status") in ("in_progress", "ready_for_execution", "active"):
            active_m = m
            break
            
    if not active_m and milestones:
        # Default to first pending
        for m in milestones:
            if m.get("status") != "completed":
                active_m = m
                break
                
    m_title = f"{active_m.get('id', 'M?')}: {active_m.get('title', 'Unknown')}" if active_m else "None (All Complete)"
    rules = data.get("client_rules", [])
    top_rule = rules[0] if rules else "Strict plain text in client fields"
    
    print(f"[741 ROADMAP ACTIVE] {client} · Phase: {phase} · Active Milestone: {m_title}")
    print(f"Goal: {north_star} | Top Constraint: {top_rule}")
    
    if active_m and "tasks" in active_m:
        print("Active Tasks:")
        for t in active_m["tasks"]:
            status_symbol = "✓" if t.get("status") == "completed" else "○"
            print(f"  {status_symbol} [{t.get('id', '-')}] {t.get('task')}")

if __name__ == "__main__":
    main()
