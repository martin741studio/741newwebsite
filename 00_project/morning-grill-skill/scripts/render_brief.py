#!/usr/bin/env python3
"""Render <run>/brief.json -> <run>/brief.html and <run>/brief.md (one fixed layout, R3).

Layout: header + source status -> Your decisions (cards) -> 741 line -> below the line -> clients (TODAY / FIXED / WATCH / NEXT).
Usage: python3 render_brief.py --run <run dir>
"""
import argparse, html, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "assets", "brief-template.html")
MAX_LINES = 4   # per column per client; the rest is counted, not hidden silently

e = lambda s: html.escape(str(s if s is not None else ""))


def card_html(n, c):
    opts = "".join(
        f'<li class="opt{" rec" if k == c.get("recommended") else ""}"><b>{e(k)}</b> {e(v)}'
        f'{" <span class=tag>recommended</span>" if k == c.get("recommended") else ""}</li>'
        for k, v in c["options"].items())
    ev = "".join(f"<li>{e(x)}</li>" for x in c.get("evidence", []))
    return (f'<article class="card p{c["priority"]}"><header><span class="num">{n}</span>'
            f'<span class="cl">{e(c["client"])}</span><span class="type">{e(c["type"])}</span>'
            f'<span class="due">by {e(c.get("deadline"))}</span></header>'
            f'<h3>{e(c["headline"])}</h3><ul class="opts">{opts}</ul>'
            f'<p class="why">Why: {e(c.get("why"))}</p>'
            f'<details><summary>Evidence ({len(c.get("evidence", []))})</summary><ul class="ev">{ev}</ul></details></article>')


def col(title, items, cls):
    if not items:
        return f'<div class="col {cls}"><h4>{title}</h4><p class="none">nothing</p></div>'
    shown = "".join(f"<li>{e(x)}</li>" for x in items[:MAX_LINES])
    more = f'<li class="more">+{len(items) - MAX_LINES} more in brief.md</li>' if len(items) > MAX_LINES else ""
    return f'<div class="col {cls}"><h4>{title}</h4><ul>{shown}{more}</ul></div>'


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--run", required=True); a = ap.parse_args()
    b = json.load(open(os.path.join(a.run, "brief.json"), encoding="utf-8"))
    src = "".join(f'<span class="src {"ok" if v["status"] == "ok" else "bad"}" title="{e(v.get("error"))}">{e(k.split("_", 1)[0])} {e(k.split("_", 1)[1])}</span>'
                  for k, v in b["sources"].items())
    bad = [f"{k}: {v.get('error')}" for k, v in b["sources"].items() if v["status"] != "ok"]
    cards = "".join(card_html(i + 1, c) for i, c in enumerate(b["cards"]))
    below = "".join(f'<li><b>{e(c["client"])}</b> {e(c["headline"])} <span class="due">by {e(c.get("deadline"))}</span></li>' for c in b["below_the_line"])
    walk = "".join(f'<li><label><input type="checkbox"> <b>{e(w["client"])}</b> {e(w["item"])}</label> <span class="due">by {e(w.get("deadline"))}</span></li>' for w in b.get("walk_queue", []))
    l741 = "".join(f"<li>{e(x)}</li>" for x in b["line_741"])
    order = sorted(b["clients"].items(), key=lambda kv: (kv[1]["status"] != "restart", -len(kv[1]["watch"])))
    clients = ""
    for name, c in order:
        clients += (f'<section class="client"><header><h3>{e(name)}</h3><span class="chip">{e(c.get("phase") or "")}</span>'
                    f'<span class="chip st-{e(c.get("status"))}">{e(c.get("status"))}</span></header>'
                    f'<p class="goal"><b>Quarter goal:</b> {e(c.get("goal") or "missing → define card")}</p>'
                    f'<div class="cols">{col("Today", c["today"], "t")}{col("Fixed", c["fixed"], "f")}{col("Watch", c["watch"], "w")}{col("Next", c["next"], "n")}</div></section>')
    tpl = open(TEMPLATE, encoding="utf-8").read()
    out = (tpl.replace("{{DATE}}", e(b["date"])).replace("{{READ_AT}}", e(b["read_at"])).replace("{{BOOKMARK}}", e(b["bookmark"]))
           .replace("{{SOURCES}}", src).replace("{{N_CARDS}}", str(len(b["cards"]))).replace("{{CARDS}}", cards)
           .replace("{{BELOW}}", below or "<li>nothing</li>").replace("{{N_BELOW}}", str(len(b["below_the_line"])))
           .replace("{{WALK}}", walk or "<li>nothing</li>").replace("{{N_WALK}}", str(len(b.get("walk_queue", [])))).replace("{{L741}}", l741 or "<li>nothing</li>").replace("{{CLIENTS}}", clients)
           .replace("{{UNREADABLE}}", "".join(f"<li>{e(x)}</li>" for x in bad) or "<li>none</li>")
           .replace("{{GOAL_GAPS}}", str(b.get("goal_gaps", 0))))
    open(os.path.join(a.run, "brief.html"), "w", encoding="utf-8").write(out)
    # markdown twin (full lists, no cut)
    md = [f"# Morning brief {b['date']} (WITA)", f"Scan since {b['bookmark']}, read {b['read_at']}.", "", "## Your decisions"]
    for i, c in enumerate(b["cards"], 1):
        md.append(f"{i}. **{c['client']}** — {c['headline']} (by {c.get('deadline')})")
        md += [f"   - {k}{' (recommended)' if k == c.get('recommended') else ''}: {v}" for k, v in c["options"].items()]
        md.append(f"   - Why: {c.get('why')}")
    md += ["", "## Walk queue (your own short checks)", *[f"- [ ] {w['client']}: {w['item']} (by {w.get('deadline')})" for w in b.get("walk_queue", [])]]
    md += ["", "## 741", *[f"- {x}" for x in b["line_741"]], "", "## Below the line", *[f"- {c['client']}: {c['headline']}" for c in b["below_the_line"]], ""]
    for name, c in order:
        md.append(f"## {name} ({c.get('status')}, {c.get('phase')})")
        md.append(f"Goal: {c.get('goal')}")
        for k in ("today", "fixed", "watch", "next"):
            md.append(f"- **{k.title()}:** " + ("; ".join(c[k]) if c[k] else "nothing"))
        md.append("")
    md += ["## Unreadable sources", *[f"- {x}" for x in bad]]
    open(os.path.join(a.run, "brief.md"), "w", encoding="utf-8").write("\n".join(md))
    print(f"brief.html + brief.md written · {len(b['cards'])} cards · {len(order)} clients")


if __name__ == "__main__":
    sys.exit(main())
