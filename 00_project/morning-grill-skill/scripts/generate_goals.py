#!/usr/bin/env python3
"""Generate morning-grill-goals.json from Supabase + the hand-kept overlay (goals-data-architecture, 2026-10-15).

Supabase (read only) supplies, for PORTAL clients only (rows in public.clients):
  status, phase (work_phases where status='current'), program_start/program_end (programs),
  quarter_goal (work_goals row with metric_key IS NULL), goal_numbers (work_goals rows with metric_key NOT NULL).
The overlay (00_project/morning-grill-goals-overlay.json, hand-edited) supplies everything Supabase
does not model: non-portal entities in full (Taxi-Zentrale, Marcel Rosenbach, me&you, Tacheles),
leads, and per-portal-client fields with no Supabase column (aliases, chat, client_rules, blockers,
waiting_for, next_workflow, next_milestone, notes, grill, leading, status_override).

Never hand-edit morning-grill-goals.json. Edit Supabase (goal numbers via work_goals, status, phase)
or the overlay (everything else).

Usage: python3 generate_goals.py [--check-only]
  --check-only  print the diff against the current file, write nothing (used by the verification step)
"""
import argparse, datetime as dt, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sb  # noqa: E402  (sibling module, same REST-login pattern as the rest of the skill)

REPO = os.environ.get("MG_REPO", "/Users/martindrendel/741website")
GOALS = os.path.join(REPO, "00_project", "morning-grill-goals.json")
OVERLAY = os.path.join(REPO, "00_project", "morning-grill-goals-overlay.json")
ARCHIVE_LOG = os.path.join(REPO, "00_project", "morning-grill-goals-archive-log.md")
STATUS_TRANSFER = {"active": "active", "onboarding": "active"}  # Supabase state -> goals.json state; overlay status_override wins when set
# work_goals.status check constraint only allows proposed/agreed/reached/dropped (no "confirmed"), but
# scan.py's goal_gaps() flags any goal_numbers row whose status != "confirmed" as a gap. Translate on the
# way out so an agreed/reached goal (Martin already confirmed it) does not show as a false gap.
GOAL_STATUS_OUT = {"agreed": "confirmed", "reached": "confirmed", "proposed": "proposed", "dropped": "dropped"}


def get(path):
    return sb.request("GET", path)


def load_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def fetch_supabase():
    clients = get("clients?select=id,name,status,mode,lang")
    programs = get("programs?select=client_id,start_date,end_date,status")
    phases = get("work_phases?select=client_id,code,label,status&status=eq.current")
    goals = get("work_goals?select=client_id,title,metric_key,baseline,target,due_on,source_link,status")
    by_client = {c["id"]: c for c in clients}
    prog_by_client = {p["client_id"]: p for p in programs}
    phase_by_client = {p["client_id"]: p for p in phases}
    goals_by_client = {}
    for g in goals:
        goals_by_client.setdefault(g["client_id"], []).append(g)
    return by_client, prog_by_client, phase_by_client, goals_by_client


def build_portal_entry(cid, c, prog_by_client, phase_by_client, goals_by_client, overlay_row, overlay_key):
    prog = prog_by_client.get(cid, {})
    phase = phase_by_client.get(cid, {})
    rows = goals_by_client.get(cid, [])
    title_row = next((r for r in rows if not r.get("metric_key")), None)
    number_rows = [r for r in rows if r.get("metric_key")]
    status = overlay_row.get("status_override") or STATUS_TRANSFER.get(c["status"], c["status"])
    entry = {
        "client": overlay_key,
        "registry_name": overlay_row.get("supabase_name", c["name"]),
        "status": status,
        "grill": overlay_row.get("grill", "daily"),
        "phase": phase.get("code"),
        "program_start": prog.get("start_date"),
        "program_end": prog.get("end_date"),
        "quarter_goal": title_row["title"] if title_row else None,
        "goal_numbers": [
            {
                "metric": r["title"],
                "baseline": r.get("baseline"),
                "target": r.get("target"),
                "due": r.get("due_on"),
                "source": r.get("source_link"),
                "status": GOAL_STATUS_OUT.get(r.get("status"), r.get("status")),
            }
            for r in number_rows
        ],
        "leading": overlay_row.get("leading", []),
        "next_milestone": overlay_row.get("next_milestone"),
        "blockers": overlay_row.get("blockers", []),
        "waiting_for": overlay_row.get("waiting_for", []),
        "client_rules": overlay_row.get("client_rules", []),
        "chat": overlay_row.get("chat"),
        "next_workflow": overlay_row.get("next_workflow"),
        "notes": overlay_row.get("notes"),
        "aliases": overlay_row.get("aliases", []),
    }
    warnings = []
    if not phase:
        warnings.append(f"{overlay_key}: no work_phases row with status=current in Supabase")
    if overlay_row.get("status_override") and overlay_row["status_override"] != c["status"]:
        warnings.append(f"{overlay_key}: overlay status_override='{overlay_row['status_override']}' overrides Supabase clients.status='{c['status']}' (expected — Supabase has no matching state)")
    return entry, warnings


def generate():
    by_id, prog_by_client, phase_by_client, goals_by_client = fetch_supabase()
    by_name = {c["name"]: cid for cid, c in by_id.items()}
    overlay = load_json(OVERLAY, {"portal_overlay": {}, "non_portal_clients": [], "leads": []})
    warnings = []
    clients_out = []
    matched_supabase_ids = set()

    for overlay_key, overlay_row in overlay.get("portal_overlay", {}).items():
        supabase_name = overlay_row.get("supabase_name", overlay_key)
        cid = by_name.get(supabase_name)
        if not cid:
            warnings.append(f"{overlay_key}: overlay expects a Supabase client named '{supabase_name}' but none exists — entry dropped, check the overlay or add the client in Supabase")
            continue
        matched_supabase_ids.add(cid)
        entry, w = build_portal_entry(cid, by_id[cid], prog_by_client, phase_by_client, goals_by_client, overlay_row, overlay_key)
        clients_out.append(entry)
        warnings.extend(w)

    unmatched = set(by_id) - matched_supabase_ids
    for cid in unmatched:
        c = by_id[cid]
        if c["name"] == "Testpraxis Musterstadt":
            continue  # demo account, never shown in the grill
        warnings.append(f"Supabase has client '{c['name']}' with no overlay row — add a portal_overlay entry for it")

    clients_out.extend(overlay.get("non_portal_clients", []))
    return {
        "_note": f"GENERATED {dt.datetime.now().isoformat(timespec='minutes')} from Supabase (portal clients: status/phase/program dates/work_goals) + {os.path.basename(OVERLAY)} (everything else). Do not hand-edit this file — edit Supabase or the overlay. Generator: 00_project/morning-grill-skill/scripts/generate_goals.py (goals-data-architecture, 2026-10-15).",
        "clients": clients_out,
        "leads": overlay.get("leads", []),
    }, warnings


def diff_and_log(old, new):
    """One archive-log line per status/phase transition. Never removes a client from view."""
    old_by_name = {c["client"]: c for c in old.get("clients", [])} if old else {}
    lines = []
    for c in new["clients"]:
        prev = old_by_name.get(c["client"])
        if not prev:
            lines.append(f"- {dt.date.today().isoformat()}: NEW client in goal sheet: {c['client']} (status {c['status']})")
            continue
        if prev.get("status") != c.get("status"):
            lines.append(f"- {dt.date.today().isoformat()}: {c['client']}: status {prev.get('status')} -> {c.get('status')}")
        if prev.get("phase") != c.get("phase"):
            lines.append(f"- {dt.date.today().isoformat()}: {c['client']}: phase {prev.get('phase')} -> {c.get('phase')}")
    dropped = set(old_by_name) - {c["client"] for c in new["clients"]}
    for name in dropped:
        lines.append(f"- {dt.date.today().isoformat()}: WARNING client dropped from goal sheet: {name} (should never happen — check the overlay)")
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()
    old = load_json(GOALS)
    new, warnings = generate()
    log_lines = diff_and_log(old, new)
    for w in warnings:
        print("WARNING:", w)
    for l in log_lines:
        print(l)
    if a.check_only:
        print(f"check-only: {len(new['clients'])} clients, {len(log_lines)} changes, {len(warnings)} warnings. Nothing written.")
        return 0
    if old and len(new["clients"]) < len(old.get("clients", [])) and not any("dropped" in l for l in log_lines):
        print("REFUSING to write: client count dropped with no explained removal — check manually.")
        return 1
    tmp = GOALS + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(new, f, ensure_ascii=False, indent=1)
    os.replace(tmp, GOALS)
    if log_lines:
        with open(ARCHIVE_LOG, "a", encoding="utf-8") as f:
            f.write("\n".join(log_lines) + "\n")
    print(f"written {GOALS} · {len(new['clients'])} clients · {len(log_lines)} archive-log lines · {len(warnings)} warnings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
