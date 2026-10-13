#!/usr/bin/env python3
"""Morning grill: detectors -> ranked decision cards + per-client brief lines.

Input : <run>/scan.json, 00_project/morning-grill-goals.json,
        optional <run>/judgment-cards.json (cards the agent writes from chat summaries; high-freedom step)
Output: <run>/brief.json (cards top N, below-the-line, per-client TODAY/FIXED/WATCH/NEXT, 741 line, sources)

Usage: python3 build_cards.py --run <run dir> [--max 7]
Priorities (preferences.md): 1 fire, 2 money/contract, 3 client deadline <= 3 days, 4 approval > 3 days,
5 goal gap, 6 pipeline follow-up, 7 internal.
"""
import argparse, datetime as dt, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get("MG_REPO", "/Users/martindrendel/741website")  # skill may live in ~/.claude/skills
GOALS = os.path.join(REPO, "00_project", "morning-grill-goals.json")
APPROVAL_DAYS = 3      # registry runs older than this become a card
STALE_PLANNED = 20     # planned citations older than 14 days: card above this count
MAX_CARDS_DEFAULT = 7


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def client_of(name, goals):
    t = (name or "").lower()
    for c in goals["clients"]:
        keys = [c["client"].lower(), (c.get("registry_name") or "").lower()] + [a.lower() for a in c.get("aliases", [])]
        if any(k and k in t for k in keys):
            return c["client"]
    return None


def card(cid, client, prio, ctype, headline, evidence, options, rec, why, deadline, then):
    return {"id": cid, "client": client, "priority": prio, "type": ctype, "headline": headline, "evidence": evidence,
            "options": options, "recommended": rec, "why": why, "deadline": deadline, "status": "open",
            "answer": None, "park_reason": None, "then": then}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--max", type=int, default=MAX_CARDS_DEFAULT)
    a = ap.parse_args()
    scan = load(os.path.join(a.run, "scan.json"))
    goals = load(GOALS)
    day = dt.date.fromisoformat(scan["date"])
    tomorrow = (day + dt.timedelta(days=1)).isoformat()
    S = scan["sources"]
    ok = lambda k: S.get(k, {}).get("status") == "ok"
    active = [c for c in goals["clients"] if c.get("status") != "done"]
    lines = {c["client"]: {"today": [], "fixed": [], "watch": [], "next": [], "goal": c.get("quarter_goal"),
                           "status": c.get("status"), "phase": c.get("phase"), "chat": c.get("chat")} for c in active}
    cards = []
    walk_items = []   # Martin's own short hands-on checks (R24): not cards, not counted in the max

    def add_line(client, kind, text):
        if client in lines and text not in lines[client][kind]:
            lines[client][kind].append(text)

    # --- S5 portal standup: messages, help, access, overdue, today's 741 tasks
    if ok("S5_standup"):
        msg_clients = []
        overdue = []
        for r in S["S5_standup"]["data"]["clients"]:
            c = client_of(r.get("name"), goals)
            if not c:
                continue
            if r.get("ungelesen") or r.get("hilfe_angefragt"):
                msg_clients.append(f"{c} ({r.get('ungelesen', 0)} unread, {r.get('hilfe_angefragt', 0)} help)")
                add_line(c, "watch", f"Portal: {r.get('ungelesen', 0)} unread messages, {r.get('hilfe_angefragt', 0)} help requests")
            for t in r.get("heute_741", [])[:3]:
                add_line(c, "today", f"Program task (week {r.get('woche')}): {t}")
            if r.get("zugaenge_offen"):
                add_line(c, "watch", "Access missing: " + ", ".join(r["zugaenge_offen"]))
            if r.get("ueberfaellig", 0) > 0:
                overdue.append((c, r["ueberfaellig"]))
                add_line(c, "watch", f"{r['ueberfaellig']} overdue portal tasks")
            if r.get("ob_gesamt") and r.get("ob_fertig", 0) < r["ob_gesamt"]:
                add_line(c, "watch", f"Onboarding {r.get('ob_fertig')}/{r['ob_gesamt']}, next: {r.get('ob_naechster')}")
            if r.get("letzte_aktivitaet"):
                add_line(c, "watch", f"Last portal activity {r['letzte_aktivitaet']} (portal only; chat work does not show)")
        if msg_clients:
            cards.append(card(f"{day}-741-messages", "741 (all clients)", 1, "decide",
                              f"{len(msg_clients)} clients have unread portal messages or help requests. Who answers today?",
                              [S["S5_standup"]["data"]["file"], "S5"] + msg_clients,
                              {"a": "Agent drafts every reply now; I send them", "b": "I answer them myself today",
                               "c": "Dinakar answers the technical ones, I answer the rest"},
                              "a", "Unanswered client messages are priority 1; drafts take you 2 minutes to send.", scan["date"],
                              {"a": "agent writes drafts per client into plan.md (```text, slop 5/5)", "b": "walk queue item", "c": "portal task drafts + WhatsApp line"}))
        if overdue:
            total = sum(n for _, n in overdue)
            cards.append(card(f"{day}-741-overdue", "741 (all clients)", 4, "decide",
                              f"{total} portal tasks are overdue across {len(overdue)} clients. Many may be done in chats but not ticked.",
                              [S["S5_standup"]["data"]["file"], "S5"] + [f"{c}: {n}" for c, n in overdue],
                              {"a": "Agent matches overdue tasks to chat work and proposes 'needs review' / re-plan per client for Monday",
                               "b": "Re-plan all overdue tasks today", "c": "Ignore the counts until the portal sync exists"},
                              "a", "Default D6 allows 'needs review'; you decide re-plans in the Monday review.", "2026-10-19",
                              {"a": "agent writes overdue-match.md; Monday card", "b": "agent drafts re-plan now", "c": "park with reason"}))

    # --- S3 registry approvals
    if ok("S3_registry"):
        reg = S["S3_registry"]["data"]
        old = [x for x in reg["approvals_open"] if (x["age_days"] or 0) > APPROVAL_DAYS]
        fresh = [x for x in reg["approvals_open"] if (x["age_days"] or 0) <= APPROVAL_DAYS]
        for x in fresh:
            c = client_of(x["client"], goals)
            if c:
                add_line(c, "fixed", f"Run ready, approval open: {x['workflow']} ({x['last_run']})")
        if old:
            by = {}
            for x in old:
                by.setdefault(x["client"], []).append(x["workflow"])
            for cl, wfs in by.items():
                cards.append(card(f"{day}-{cl[:12]}-approve", cl, 4, "approve",
                                  f"{cl}: {len(wfs)} workflow results wait for your approval for more than {APPROVAL_DAYS} days ({', '.join(wfs)}).",
                                  ["00_project/workflow-registry/registry.json", "S3"],
                                  {"a": "Approve all", "b": "Open them now (walk queue)", "c": "Reject, needs rework"},
                                  "b", "Approval needs your eyes; the walk queue keeps it to the results.", tomorrow,
                                  {"a": "workflow_registry.py approve per run", "b": "walk queue with links", "c": "rework task to the agent"}))
        for r in reg["runs_since_bookmark"]:
            c = client_of(r["client"], goals)
            if c:
                add_line(c, "fixed", f"Run {r['workflow']}: {r['status']} ({r['last_run']})")

    # --- S6 night shift
    if ok("S6_nightshift"):
        ns = S["S6_nightshift"]["data"]
        open_items = [(cl, i["item"]) for cl, items in ns["items"].items() for i in items if not i["ticked"]]
        if open_items:
            cards.append(card(f"{day}-741-nightshift", "741 (night shift)", 4, "approve",
                              f"The night shift redoes the same {len(open_items)} drafts every night: nobody approves them and its ledger has {ns['ledger_entries']} entries.",
                              [ns["file"], "S6"] + [f"{cl}: {it}" for cl, it in open_items],
                              {"a": "Approve the 'pass' drafts and write the ledger", "b": "Review them one by one (walk queue)", "c": "Pause the night shift until the grill shows its items"},
                              "b", "They are client-facing texts (GBP, NAP); a short look is the real gate.", tomorrow,
                              {"a": "agent writes processed-feedback.json (needs go, other chat's file)", "b": "walk queue with the 5 file links", "c": "LaunchAgent change needs go"}))
            for cl, it in open_items:
                c = client_of(cl, goals)
                if c:
                    add_line(c, "fixed", f"Night-shift draft ready: {it} (not approved)")

    # --- S7 citations
    if ok("S7_citations"):
        cit = S["S7_citations"]["data"]
        for slug, n in cit["listing_emails_unhandled"].items():
            c = client_of(slug, goals) or slug
            cards.append(card(f"{day}-{slug}-listing-mails", c, 3, "route",
                              f"{c}: {n} directory confirmation emails are unhandled. Verify links can expire.",
                              ["Supabase listing_emails (handled = false)", "S7"],
                              {"a": "Tantri clicks the verify links today (portal task + WhatsApp)", "b": "Agent lists them first, I decide", "c": "Park"},
                              "a", "Group A listings are 741's job; expired links mean a new submission.", scan["date"],
                              {"a": "task draft for Tantri with the list", "b": "agent writes list into plan.md", "c": "park reason required"}))
        stale = {cl: v["planned_stale_14d"] for cl, v in cit["per_client"].items() if v.get("planned_stale_14d", 0) > STALE_PLANNED}
        for cl, v in cit["per_client"].items():
            c = client_of(cl, goals)
            if c:
                add_line(c, "watch", f"Citations: {v.get('live', 0)} live, {v.get('submitted', 0)} submitted, {v.get('planned', 0)} planned"
                         + (f", {v['inconsistent']} inconsistent" if v.get("inconsistent") else ""))
        if stale:
            cards.append(card(f"{day}-741-citations-stale", "741 (citations)", 5, "decide",
                              "Citations stand still: " + ", ".join(f"{k} {n}" for k, n in stale.items()) + " entries are 'planned' for more than 14 days.",
                              ["Supabase client_citations", "S7", "memory citations-listings-module"],
                              {"a": "Tantri works the group-A list this week, 10 per day", "b": "First build the citations workflow (run file, runbook), then work",
                               "c": "Park until the backlink merge is done"},
                              "a", "Citations live is a leading number in every goal sheet; the runbook already exists.", "2026-10-16",
                              {"a": "task drafts per client from reporting/submission-runbook.mjs output", "b": "start ⚙️🖇️ chat task", "c": "park"}))

    # --- S10 calendar
    if ok("S10_calendar"):
        for e in S["S10_calendar"]["data"].get("events", []):
            add_line_741 = f"Calendar: {e['title']} with {e.get('with', '')} at {e.get('start_wita', e.get('start'))} WITA ({e.get('status', '')})"
            scan.setdefault("_741_lines", []).append(add_line_741)

    # --- goal sheet: next milestones, waiting-for, conflicts
    conflicts = []
    for c in active:
        if c.get("next_milestone"):
            add_line(c["client"], "next", c["next_milestone"])
        if c.get("next_workflow"):
            add_line(c["client"], "next", f"Next workflow: {c['next_workflow']}")
        for w in c.get("waiting_for", []):
            add_line(c["client"], "watch", f"Waiting for {w['who']}: {w['what']} since {w['since']}")
        if "conflict" in str(c.get("program_start") or ""):
            conflicts.append(f"{c['client']}: {c['program_start']}")
    stz = [c for c in active if c.get("program_start") is None and c.get("phase") in ("P1",)]
    # D23 (Martin 2026-10-13): start dates are decided client by client -> one walk item each, not a card
    for x in conflicts:
        walk_items.append({"client": x.split(":")[0], "item": f"Which program start date counts? {x.split(':', 1)[1].strip()}", "deadline": "2026-10-15", "id": f"{day}-start-{x[:12]}"})
    for c in stz:
        walk_items.append({"client": c["client"], "item": "No program start date. Set it (start = agreed trigger, e.g. contract or kickoff).", "deadline": "2026-10-15", "id": f"{day}-start-{c['client'][:12]}"})

    # --- S13 deadlines in memory (baseline lesson L7); invoices never shown unasked (memory feedback-no-invoice-talk)
    if ok("S13_deadlines"):
        import re as _re
        money = _re.compile(r"(rechnung|invoice|\brate\b|zahlung|payment|bezahlt)", _re.I)
        for h in S["S13_deadlines"]["data"]:
            if money.search(h["text"]):
                continue
            if h["urgent"] and h["overdue_days"] >= -3:
                cards.append(card(f"{day}-deadline-{h['file'][:20]}", h.get("client") or "741", 1, "decide",
                                  f"Deadline {h['date']} from memory has no 'done' note ({h['overdue_days']} days overdue): {h['text'][:140]}",
                                  [f"memory {h['file']}", "S13"],
                                  {"a": "Still open: agent prepares the next step today", "b": "Already resolved: agent adds a done note to the memory file",
                                   "c": "Park with a reason"},
                                  "b" if h["overdue_days"] > 14 else "a",
                                  "A legal or account deadline must never stay silent; if it is resolved, the note stops the card.",
                                  scan["date"], {"a": "plan item", "b": "memory edit (done note with date)", "c": "park reason"}))
            else:
                (lines[h["client"]]["watch"].append(f"Date in memory {h['date']}: {h['text'][:120]}")
                 if h.get("client") in lines else None)

    # --- judgment cards from the agent (chat summaries, grill answers)
    jp = os.path.join(a.run, "judgment-cards.json")
    if os.path.exists(jp):
        for jc in load(jp):
            if jc.get("walk"):
                walk_items.append({"client": jc["client"], "item": jc["walk"], "deadline": jc.get("deadline"), "id": jc["id"]})
            else:
                cards.append(jc)
            if jc.get("client") in lines and jc.get("line"):
                add_line(jc["client"], jc.get("line_kind", "watch"), jc["line"])
    # chat summaries -> fixed / watch lines
    if ok("S2_chats"):
        for cl, v in S["S2_chats"]["data"].get("clients", {}).items():
            c = client_of(cl, goals)
            if not c:
                continue
            for d in v.get("done", [])[:4]:
                add_line(c, "fixed", d)
            for w in v.get("waiting_for", [])[:3]:
                add_line(c, "watch", f"Waiting for {w.get('who')}: {w.get('what')}")
            for o in v.get("open", [])[:3]:
                add_line(c, "today", f"Open from chat: {o}")

    # --- rank and cut
    cards.sort(key=lambda x: (x["priority"], x["deadline"] or "9999"))
    top, below = cards[:a.max], cards[a.max:]
    l741 = scan.get("_741_lines", [])
    if ok("S12_prospects"):
        pend = [p["client"] for p in S["S12_prospects"]["data"] if (p.get("status") or "").startswith("fertig")]
        if pend:
            l741.append(f"Review pages ready, not sent: {', '.join(pend)}")
    lead_due = [l for l in goals.get("leads", []) if l.get("follow_up_due")]
    for l in lead_due:
        l741.append(f"Lead follow-up: {l['lead']} ({l['follow_up_due']})")
    brief = {"date": scan["date"], "bookmark": scan["bookmark"], "read_at": scan["read_at"], "time_zone": scan["time_zone"],
             "sources": {k: {"status": v["status"], "error": v.get("error")} for k, v in S.items()},
             "cards": top, "below_the_line": below, "walk_queue": walk_items, "clients": lines, "line_741": l741,
             "goal_gaps": len(scan.get("goal_gaps", []))}
    with open(os.path.join(a.run, "brief.json"), "w", encoding="utf-8") as f:
        json.dump(brief, f, ensure_ascii=False, indent=1)
    print(f"brief.json · {len(top)} cards · {len(below)} below the line · {len(lines)} clients")


if __name__ == "__main__":
    sys.exit(main())
