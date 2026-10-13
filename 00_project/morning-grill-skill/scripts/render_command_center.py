#!/usr/bin/env python3
"""Client Command Center: one page that always shows where each client stands (D27).

Top: decisions today, walk queue, agent work. Per client: goal + numbers, program week, roadmap P0-P6 with the real
workflow status from the registry, open items (messages, approvals, blockers, waiting for), next steps to the goal.
Inputs : latest run dir (brief.json, plan.md, scan.json), 00_project/morning-grill-goals.json, registry.json, state/cards.json
Output : 00_project/assets/morning-grill/command-center.html (always the latest) + a copy in the run dir.
Usage  : python3 render_command_center.py --run <run dir>
"""
import argparse, html, json, os, re, shutil, sys

REPO = os.environ.get("MG_REPO", "/Users/martindrendel/741website")
MG = os.path.join(REPO, "00_project", "assets", "morning-grill")
PHASES = [("P0", "Prospect", ["prospect"]), ("P1", "Onboarding", ["lockout"]), ("P2", "Audit", ["audit"]),
          ("P3", "Un-Burning", ["unburning"]), ("P4", "Build-up", ["citations", "phone", "backlink", "cro", "cro_b"]),
          ("P5", "Content", ["pool", "copy"]), ("P6", "Proof + Quarter", ["tracking"])]
WF_LABEL = {"prospect": "Review page", "lockout": "Access lockout", "audit": "Maps audit", "unburning": "Un-Burning",
            "citations": "Citations", "phone": "Phone playbook", "backlink": "Backlinks", "cro": "CRO page", "cro_b": "CRO Track B",
            "pool": "Content pool", "copy": "Content writing", "tracking": "Proof tracking"}
ST = {"freigegeben": ("done", "approved"), "fertig, Freigabe offen": ("wait", "waits for your approval"),
      "in Arbeit": ("run", "in progress"), "Trockenlauf": ("dry", "dry run only"), "Archiv": ("arch", "archived")}
RANK = {"done": 4, "wait": 3, "run": 2, "dry": 1, "arch": 0}
e = lambda s: html.escape(str(s if s is not None else ""))


def load(p, default=None):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def client_of(name, goals):
    t = (name or "").lower()
    for c in goals["clients"]:
        keys = [c["client"].lower(), (c.get("registry_name") or "").lower()] + [a.lower() for a in c.get("aliases", [])]
        if any(k and k in t for k in keys):
            return c["client"]
    return None


def plan_sections(path):
    out, cur = {}, None
    if not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8"):
        if line.startswith("## "):
            cur = line[3:].strip(); out[cur] = []
        elif cur and line.strip().startswith("- "):
            out[cur].append(line.strip()[2:])
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--run", required=True); a = ap.parse_args()
    b = load(os.path.join(a.run, "brief.json"))
    goals = load(os.path.join(REPO, "00_project", "morning-grill-goals.json"))
    reg = load(os.path.join(REPO, "00_project", "workflow-registry", "registry.json"), {"runs": []})
    ledger = load(os.path.join(MG, "state", "cards.json"), {"cards": []})
    scan = load(os.path.join(a.run, "scan.json"), {})
    plan = plan_sections(os.path.join(a.run, "plan.md"))
    standup = {}
    s5 = scan.get("sources", {}).get("S5_standup", {})
    if s5.get("status") == "ok":
        for r in s5["data"]["clients"]:
            c = client_of(r.get("name"), goals)
            if c:
                standup[c] = r
    # registry: best status per client x workflow
    wf = {}
    for r in reg["runs"]:
        c = client_of(r["client"], goals)
        if not c:
            continue
        cls = ST.get(r["status"], ("dry", r["status"]))[0]
        k = (c, r["workflow"])
        if k not in wf or RANK[cls] > RANK[wf[k]["cls"]]:
            wf[k] = {"cls": cls, "label": ST.get(r["status"], (None, r["status"]))[1], "date": r.get("last_run", "")}
    decided = [c for c in ledger.get("cards", []) if c.get("decided_at", "").startswith(b["date"])]
    by_client_dec = {}
    for c in decided:
        by_client_dec.setdefault(client_of(c["client"], goals) or c["client"], []).append(c)
    walk_open = [x for x in plan.get("Walk queue — Martin (1–5 min each)", []) if x.startswith("[ ]")]
    walk_by = {}
    for w in b.get("walk_queue", []):
        walk_by.setdefault(w["client"], []).append(w["item"])
    later_by = {}
    for c in b.get("below_the_line", []):
        later_by.setdefault(c["client"], []).append(c["headline"])

    # ---- top strip + decision cards (approval-dashboard style, D27)
    import base64
    logo_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "logo_black.png")
    logo = "data:image/png;base64," + base64.b64encode(open(logo_p, "rb").read()).decode() if os.path.exists(logo_p) else ""
    led_by_id = {c["id"]: c for c in ledger.get("cards", [])}
    TYPE = {1: "Fire", 2: "Money / contract", 3: "Client deadline", 4: "Approval", 5: "Goal gap", 6: "Pipeline", 7: "741"}
    cards_html, n_open = [], 0
    snap = {"date": b["date"], "read_at": b["read_at"], "bookmark": b.get("bookmark"), "cards": [], "clients": []}
    for n, c in enumerate(b["cards"], 1):
        lc = led_by_id.get(c["id"])
        done = bool(lc and lc.get("status") in ("decided", "parked"))
        snap["cards"].append({"id": c["id"], "n": n, "client": c["client"], "priority": c["priority"], "type": TYPE.get(c["priority"], ""),
                              "headline": c["headline"], "why": c.get("why"), "options": c["options"], "recommended": c.get("recommended"),
                              "then": c.get("then") if isinstance(c.get("then"), dict) else {}, "evidence": c.get("evidence", []),
                              "deadline": c.get("deadline"),
                              "status": (lc or {}).get("status", "open") if done else "open",
                              "answer": (lc or {}).get("answer") if done else None,
                              "answer_text": ((lc or {}).get("park_reason") or (lc or {}).get("answer_text")) if done else None})
        n_open += 0 if done else 1
        tags = ["decided" if done else "open", f"p{c['priority']}", "741" if c["client"].startswith("741") else "client"]
        vars_h = ""
        for k, v in c["options"].items():
            sel = " sel" if done and lc.get("answer") == k else ""
            rec = '<span class="rec">741 recommends</span>' if k == c.get("recommended") else ""
            then = c.get("then", {}).get(k, "") if isinstance(c.get("then"), dict) else ""
            vars_h += (f'<button class="var{sel}" data-k="{e(k)}"><div class="lab">Option {e(k.upper())} {rec}</div>'
                       f'<div class="val">{e(v)}</div>' + (f'<div class="then">Then: {e(then)}</div>' if then else "") + "</button>")
        res = ""
        if done:
            cls = " park" if lc["status"] == "parked" else ""
            res = f'<div class="res{cls}">{"Parked" if lc["status"] == "parked" else "Decided"}: {e(lc.get("park_reason") or lc.get("answer_text") or lc.get("answer"))}</div>'
        ev = "".join(f"<li>{e(x)}</li>" for x in c.get("evidence", []))
        cards_html.append(f'''<article class="item{" done" if done else ""}" data-n="{n}" data-tags="{" ".join(tags)}">
<div class="itop"><span class="type p{c['priority']}">{e(TYPE.get(c['priority'], ''))}</span><span class="cn">{e(c['client'])}</span><span class="dl">card {n} · by {e(c.get('deadline'))}</span></div>
<h2>{e(c['headline'])}</h2><div class="why"><b>Why:</b> {e(c.get('why'))}</div>
<div class="vars">{vars_h}</div>{res}<details class="ev"><summary>Evidence ({len(c.get('evidence', []))})</summary><ul>{ev}</ul></details></article>''')
    need_you = sum(1 for nm in b["clients"] if nm in walk_by or nm in by_client_dec or nm in later_by)
    unread = [k for k, v in b["sources"].items() if v["status"] != "ok"]
    tiles = [(f"{len(decided)}/{len(b['cards'])}", "decisions taken today"), (str(len(walk_open)), "walk-queue clicks open"),
             (str(need_you), f"of {len(b['clients'])} clients need your part"), (str(len(unread)), "unreadable: " + (", ".join(unread) or "none"))]
    tiles_h = "".join(f'<div class="tile"><b>{e(v)}</b><span>{e(s)}</span></div>' for v, s in tiles)
    walk_h = "".join(f'<li><input type="checkbox"><span>{e(x[4:])}</span></li>' for x in walk_open) or "<li>nothing open</li>"
    later_h = "".join(f"<li><b>{e(c['client'])}</b> — {e(c['headline'][:120])}</li>" for c in b.get("below_the_line", [])) or "<li>nothing</li>"
    agent_h = "".join(f"<li>{e(x)}</li>" for x in plan.get("Agent starts", [])) or "<li>nothing started</li>"
    wait_h = "".join(f"<li>{e(x)}</li>" for x in plan.get("Waiting for", [])) or "<li>nothing</li>"
    l741_h = "".join(f"<li>{e(x)}</li>" for x in b.get("line_741", [])) or "<li>nothing</li>"

    import hashlib
    snap["walk"] = [{"id": "walk-" + hashlib.md5(x[4:].encode()).hexdigest()[:8], "text": x[4:], "done": False} for x in walk_open]
    snap["later"] = [{"client": c["client"], "headline": c["headline"]} for c in b.get("below_the_line", [])]
    snap["agents"] = list(plan.get("Agent starts", []))
    snap["waiting"] = list(plan.get("Waiting for", []))
    snap["line_741"] = list(b.get("line_741", []))
    snap["sources"] = [{"id": k, "status": v["status"], "error": v.get("error")} for k, v in b["sources"].items()]
    snap["tiles"] = [{"value": v, "label": l} for v, l in tiles]

    # ---- clients
    order = sorted(goals["clients"], key=lambda c: (c.get("status") == "done", -(len(walk_by.get(c["client"], [])) + len(by_client_dec.get(c["client"], [])) * 2 + len(later_by.get(c["client"], [])))))
    nav, cards_h = [], []
    for g in order:
        name = g["client"]
        if g.get("status") == "done" or name not in b["clients"]:
            continue
        bc = b["clients"][name]
        anchor = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        nav.append(f'<a class="chip" href="#{anchor}">{e(name)}</a>')
        su = standup.get(name, {})
        week = su.get("woche")
        wk = f'<div class="week"><div class="wbar"><i style="width:{min(100, round((week or 0) / 13 * 100))}%"></i></div><span>Program week {e(week)} of 13 · onboarding {e(su.get("ob_fertig"))}/{e(su.get("ob_gesamt"))}</span></div>' if week is not None else '<div class="week"><span>No program week in the portal</span></div>'
        cur = int((g.get("phase") or "P0")[1])
        steps = ""
        for i, (pid, plabel, wfs) in enumerate(PHASES):
            state = "past" if i < cur else ("now" if i == cur else "next")
            pills = ""
            for w in wfs:
                x = wf.get((name, w))
                if x:
                    pills += f'<span class="wf {x["cls"]}" title="{e(x["label"])} · {e(x["date"])}">{e(WF_LABEL[w])}</span>'
            if pid == "P1" and su.get("ob_gesamt"):
                cls = "done" if su.get("ob_fertig") == su.get("ob_gesamt") else "run"
                pills = f'<span class="wf {cls}" title="portal onboarding">Onboarding {e(su.get("ob_fertig"))}/{e(su.get("ob_gesamt"))}</span>' + pills
            steps += f'<div class="step {state}"><span class="sid">{pid}</span><span class="sl">{e(plabel)}</span><div class="wfs">{pills or "<span class=wf>—</span>"}</div></div>'
        nums = "".join(f'<tr><td>{e(n["metric"])}</td><td>{e(n.get("baseline") if n.get("baseline") is not None else "?")}</td><td>{e(n.get("target") if n.get("target") is not None else "?")}</td><td>{e(n.get("due") or "")}</td><td class="{e(n.get("status"))}">{e(n.get("status"))}</td></tr>' for n in g.get("goal_numbers", []))
        nums = f'<table class="nums"><tr><th>Number</th><th>Now</th><th>Target</th><th>Due</th><th></th></tr>{nums}</table>' if nums else '<p class="miss">No goal numbers yet → define card</p>'
        openl = []
        for d in by_client_dec.get(name, []):
            openl.append(("dec", f"Decided today: {d.get('answer_text') or d.get('answer')}"))
        for w in walk_by.get(name, []):
            openl.append(("you", f"Your click: {w}"))
        for w in bc["watch"]:
            lw = w.lower()
            kind = "msg" if ("unread" in lw or "help" in lw) else "appr" if "approval" in lw else "wait" if "waiting" in lw else "block"
            if "0 unread messages, 0 help" in lw:
                continue
            openl.append((kind, w))
        for h in later_by.get(name, []):
            openl.append(("later", f"Later list: {h}"))
        icon = {"dec": "✅", "you": "👆", "msg": "✉️", "appr": "⏳", "wait": "🕒", "block": "⛔", "later": "📋"}
        open_h = "".join(f'<li class="{k}"><span class="ic">{icon[k]}</span><span>{e(t)}</span></li>' for k, t in openl[:12]) or "<li>nothing open</li>"
        nxt = [*(bc["next"] or []), *(bc["today"][:3] or [])]
        next_h = "".join(f'<li><span class="ic">➜</span><span>{e(x)}</span></li>' for x in nxt[:6]) or "<li>no next step set → define card</li>"
        moved_h = "".join(f'<li class="moved"><span class="ic">✓</span><span>{e(x)}</span></li>' for x in bc["fixed"][:4]) or "<li>nothing since the last grill</li>"
        road = []
        for i, (pid, plabel, wfs) in enumerate(PHASES):
            items = [{"label": WF_LABEL[w], "cls": wf[(name, w)]["cls"], "title": f'{wf[(name, w)]["label"]} · {wf[(name, w)]["date"]}'} for w in wfs if (name, w) in wf]
            if pid == "P1" and su.get("ob_gesamt"):
                items.insert(0, {"label": f'Onboarding {su.get("ob_fertig")}/{su.get("ob_gesamt")}', "cls": "done" if su.get("ob_fertig") == su.get("ob_gesamt") else "run", "title": "portal onboarding"})
            road.append({"id": pid, "label": plabel, "state": "past" if i < cur else ("now" if i == cur else "next"), "wfs": items})
        snap["clients"].append({"name": name, "anchor": anchor, "status": g.get("status"), "phase": g.get("phase"), "phase_label": PHASES[cur][1],
                                "goal": g.get("quarter_goal"), "week": week, "ob_done": su.get("ob_fertig"), "ob_total": su.get("ob_gesamt"),
                                "roadmap": road, "open": [{"kind": k, "text": t} for k, t in openl[:12]], "next": nxt[:6], "moved": bc["fixed"][:4],
                                "numbers": [{"metric": n_["metric"], "baseline": n_.get("baseline"), "target": n_.get("target"), "due": n_.get("due"), "status": n_.get("status")} for n_ in g.get("goal_numbers", [])],
                                "milestone": g.get("next_milestone")})
        cards_h.append(f'''<section class="cl" id="{anchor}"><div class="clh"><h2>{e(name)}</h2><span class="pill {e(g.get("status"))}">{e(g.get("status"))}</span>
<span class="pill">{e(g.get("phase"))} · {e(PHASES[cur][1])}</span></div>
<p class="goal"><b>Goal:</b> {e(g.get("quarter_goal") or "missing")}</p>{wk}
<div class="road">{steps}</div>
<div class="cols3"><div><h4>Open now</h4><ul>{open_h}</ul></div>
<div><h4>Next steps to the goal</h4><ul>{next_h}</ul><h4>Moved since last grill</h4><ul>{moved_h}</ul></div>
<div><h4>Goal numbers</h4>{nums}<p class="goal" style="font-size:14px"><b>Milestone:</b> {e(g.get("next_milestone") or "not set")}</p></div></div></section>''')
    tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "command-center-template.html"), encoding="utf-8").read()
    out = (tpl.replace("{{DATE}}", e(b["date"])).replace("{{READ_AT}}", e(b["read_at"])).replace("{{LOGO}}", logo)
           .replace("{{TILES}}", tiles_h).replace("{{N_OPEN}}", str(n_open)).replace("{{CARDS}}", "".join(cards_html))
           .replace("{{WALK}}", walk_h).replace("{{LATER}}", later_h).replace("{{AGENT}}", agent_h).replace("{{WAITING}}", wait_h)
           .replace("{{L741}}", l741_h).replace("{{NAV}}", "".join(nav)).replace("{{CLIENTS}}", "".join(cards_h)))
    dst = os.path.join(MG, "command-center.html")
    open(dst, "w", encoding="utf-8").write(out)
    shutil.copy(dst, os.path.join(a.run, "command-center.html"))
    json.dump(snap, open(os.path.join(a.run, "snapshot.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"command-center.html · {len(cards_h)} clients · {len(decided)} decisions today · {len(walk_open)} walk items open")


if __name__ == "__main__":
    sys.exit(main())
