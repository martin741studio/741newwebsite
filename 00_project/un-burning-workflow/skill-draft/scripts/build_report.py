#!/usr/bin/env python3
"""Build report/internal.html (or client.html) from an Un-Burning run folder. Standard library only.

Usage: python3 -I build_report.py <run-folder> [--client] [--form sie|du] [--out <file>]
Reads: harm-register.json (required), manifest.json, nap-corrections.json,
       redirect-map.json, index-intended.json, link-plan.json, metrics.json (all optional).
Never invents data: a missing file shows "nicht gelesen". Counts come from the register.
Client view shows only items that have a reviewed client_text (plain German, no tool or table names).
--client builds the client-safe view: no tool names, no hashes, no internal severity words,
only items with client_safe != false, destructive rows only when done.
"""
import json, sys, html, pathlib, datetime

SEV = {"blocks_revenue": ("Umsatz blockiert", "sev-rev"),
       "leaks_link_power": ("Linkkraft verloren", "sev-link"),
       "cosmetic": ("kosmetisch", "sev-cos")}
ACT = {"keep": "Behalten", "fix": "Reparieren", "merge": "Zusammenführen", "redirect": "Weiterleiten (301)",
       "delete": "Entfernen", "report": "Melden", "claim": "Beanspruchen"}
WHO = {"client": "Kundin / Kunde", "741": "741", "google": "Google"}
APPR = {"proposed": "vorgeschlagen", "approved": "freigegeben", "rejected": "abgelehnt", "done": "erledigt", "blocked": "blockiert"}
AREA_NAME = {"B": "Rettung gesperrter Profile", "C": "Identität und NAP",
             "D": "Schadensbehebung", "E": "Index und Crawl-Pfad"}
LIGHT_LABEL = {"green": "grün", "yellow": "gelb", "red": "rot", "grey": "grau"}
EFF_ORDER = {"S": 0, "M": 1, "L": 2}
SEV_ORDER = {"blocks_revenue": 0, "leaks_link_power": 1, "cosmetic": 2}


def e(x):
    return html.escape("" if x is None else str(x))


def short(s, n=120):
    s = "" if s is None else str(s)
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"


def load(folder, name):
    p = folder / name
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def is_open(it):
    if it.get("action") == "keep" or it.get("approval") == "done":
        return False
    if it.get("approval") == "rejected" and it.get("action_detail"):
        return False
    return True


def bedrock(items, scanned):
    areas, counts = {}, {}
    for a in "BCDE":
        its = [i for i in items if i["area"] == a]
        if a not in scanned:
            areas[a] = "grey"; counts[a] = (0, 0, 0); continue
        op = [i for i in its if is_open(i)]
        blocks = [i for i in op if i["severity"] == "blocks_revenue"]
        leaks_all = [i for i in its if i["severity"] == "leaks_link_power" and i.get("action") != "keep"]
        leaks_open = [i for i in op if i["severity"] == "leaks_link_power"]
        share = len(leaks_open) / len(leaks_all) if leaks_all else 0
        areas[a] = "red" if blocks else ("yellow" if share > 0.10 else "green")
        counts[a] = (len(op), len(blocks), len(leaks_open))
    ready = all(areas[a] == "green" for a in "CDE") and "red" not in areas.values()
    return areas, counts, ready


CSS = """
:root{--bg:#f6f5f1;--card:#fff;--ink:#1c1b19;--mute:#6b6963;--line:#e3e0d8;--accent:#fac118;--accent-ink:#1c1b19;
--green:#1f8a4c;--yellow:#c78a00;--red:#c62f2f;--grey:#8b8a85;--green-bg:#e4f4ea;--yellow-bg:#fbf0d4;--red-bg:#f9e0e0;--grey-bg:#ececea;}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#161512;--card:#201f1b;--ink:#f1efe8;--mute:#a09d94;--line:#34322c;
--green:#58c885;--yellow:#e8b43b;--red:#f07070;--grey:#9a998f;--green-bg:#1b3326;--yellow-bg:#3a2f12;--red-bg:#3c1b1b;--grey-bg:#2b2a26;}}
:root[data-theme="dark"]{--bg:#161512;--card:#201f1b;--ink:#f1efe8;--mute:#a09d94;--line:#34322c;--green:#58c885;--yellow:#e8b43b;--red:#f07070;--grey:#9a998f;
--green-bg:#1b3326;--yellow-bg:#3a2f12;--red-bg:#3c1b1b;--grey-bg:#2b2a26;}
*{box-sizing:border-box}html{font-size:16px}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 "DM Sans",system-ui,-apple-system,"Segoe UI",sans-serif}
h1,h2,h3{font-family:"Anton","DM Sans",system-ui,sans-serif;font-weight:400;letter-spacing:.02em;text-transform:uppercase;margin:0}
.wrap{max-width:1280px;margin:0 auto;padding:0 16px 64px}
.top{display:flex;gap:12px;align-items:center;justify-content:space-between;padding:16px 0;border-bottom:1px solid var(--line);flex-wrap:wrap}
.brand{display:flex;gap:10px;align-items:center}.logo{background:var(--accent);color:var(--accent-ink);font-family:Anton,sans-serif;padding:2px 8px;border-radius:4px}
.meta{color:var(--mute);font-size:13px}.pill{border:1px solid var(--line);border-radius:999px;padding:2px 10px;font-size:12px;color:var(--mute);background:var(--card)}
h1{font-size:30px;margin:24px 0 4px}h2{font-size:22px;margin:40px 0 12px}h3{font-size:16px;margin:0 0 10px;color:var(--mute)}
.lights{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:16px 0}
.light{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;border-top-width:5px}
.light.green{border-top-color:var(--green)}.light.yellow{border-top-color:var(--yellow)}.light.red{border-top-color:var(--red)}.light.grey{border-top-color:var(--grey)}
.light .k{font-family:Anton,sans-serif;font-size:26px}.light .n{font-size:13px;color:var(--mute);min-height:2.6em}.light .s{font-size:12px;margin-top:6px;font-weight:600}
.light.green .s{color:var(--green)}.light.yellow .s{color:var(--yellow)}.light.red .s{color:var(--red)}.light.grey .s{color:var(--grey)}
.verdict{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--accent);border-radius:10px;padding:12px 16px;margin:8px 0 20px}
.grid2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}.card{min-width:0;overflow-wrap:anywhere;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px}
.tally{display:flex;gap:20px;flex-wrap:wrap}.tally div{min-width:96px}.tally b{display:block;font-family:Anton,sans-serif;font-size:34px;font-weight:400}
.tally span{font-size:12px;color:var(--mute)}
ol.leaks,ol.next{margin:0;padding-left:20px}ol.leaks li,ol.next li{margin:0 0 8px}
.chip{display:inline-block;border-radius:999px;padding:1px 9px;font-size:12px;font-weight:600;white-space:nowrap}
.sev-rev{background:var(--red-bg);color:var(--red)}.sev-link{background:var(--yellow-bg);color:var(--yellow)}.sev-cos{background:var(--grey-bg);color:var(--grey)}
.st{background:var(--grey-bg);color:var(--mute)}.st-done{background:var(--green-bg);color:var(--green)}.st-ok{background:var(--yellow-bg);color:var(--yellow)}
table{width:100%;border-collapse:collapse;font-size:13.5px;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}th{font-size:12px;color:var(--mute);background:var(--bg);font-weight:600}
tr:last-child td{border-bottom:0}td:first-child{white-space:nowrap}td code{word-break:break-all;display:inline-block;min-width:150px}.tw{overflow-x:auto}
details{margin:10px 0;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:0 14px}summary{cursor:pointer;padding:12px 0;font-weight:600}
.btns{display:flex;gap:4px;flex-wrap:wrap}.btn{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:6px;padding:3px 8px;font-size:12px;cursor:pointer}
.btn.on{background:var(--accent);color:var(--accent-ink);border-color:var(--accent);font-weight:600}.btn.prim{background:var(--accent);color:var(--accent-ink);border-color:var(--accent);font-weight:600;padding:6px 12px;font-size:13px}
.lock{color:var(--red);font-size:12px}.muted{color:var(--mute)}code{font-size:12px;background:var(--bg);padding:1px 5px;border-radius:4px}
a{color:var(--ink);text-decoration-color:var(--accent);text-underline-offset:3px;font-weight:600}
.note{font-size:12.5px;color:var(--mute);margin-top:8px}
@media (max-width:900px){.lights{grid-template-columns:repeat(2,minmax(0,1fr))}.grid2{grid-template-columns:minmax(0,1fr)}.light,.verdict,.card{overflow-wrap:anywhere}.top .meta{overflow-wrap:anywhere}}
"""

JS = """
const decisions={};
document.querySelectorAll('[data-item]').forEach(row=>{row.querySelectorAll('.btn[data-d]').forEach(b=>b.addEventListener('click',()=>{
 const id=row.dataset.item;decisions[id]=b.dataset.d;row.querySelectorAll('.btn[data-d]').forEach(x=>x.classList.toggle('on',x===b));
 document.getElementById('dcount').textContent=Object.keys(decisions).length;}));});
const ex=document.getElementById('export');if(ex)ex.addEventListener('click',()=>{
 const blob=new Blob([JSON.stringify({exported_at:new Date().toISOString(),decisions},null,2)],{type:'application/json'});
 const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='approvals.json';a.click();});
"""


def main(argv):
    folder = pathlib.Path(argv[1])
    client = "--client" in argv
    sie = "--form" in argv and argv[argv.index("--form") + 1] == "sie"
    T = ({"ready": "Ihr Fundament steht. Jetzt kann das Wachstum starten.", "work": "Wir arbeiten gerade an Ihrem Fundament. Danach starten wir mit dem Wachstum.",
          "todo": "Was Sie tun müssen", "todo_text": "Aktuell nichts, oder nur die Bestätigungen aus Ihrer Checkliste."} if sie else
         {"ready": "Dein Fundament steht. Jetzt kann das Wachstum starten.", "work": "Wir arbeiten gerade an deinem Fundament. Danach starten wir mit dem Wachstum.",
          "todo": "Was du tun musst", "todo_text": "Aktuell nichts, oder nur die Bestätigungen aus deiner Checkliste."})
    out = None
    if "--out" in argv:
        out = pathlib.Path(argv[argv.index("--out") + 1])
    reg = load(folder, "harm-register.json")
    run = reg["run"]
    items = reg["items"]
    if client:
        items = [i for i in items if i.get("client_safe", True) and i.get("client_text")
                 and (not i.get("destructive") or i.get("approval") == "done")]
    manifest = load(folder, "manifest.json") or {}
    mentries = manifest.get("evidence", manifest) if isinstance(manifest, dict) else manifest
    if isinstance(mentries, dict):
        mentries = [{"id": k, **v} for k, v in mentries.items()]
    nap = load(folder, "nap-corrections.json")
    redir = load(folder, "redirect-map.json")
    idx = load(folder, "index-intended.json")
    plan = load(folder, "link-plan.json")
    metrics = load(folder, "metrics.json")
    runjson = load(folder, "run.json") or {}
    scanned = set(run.get("params", {}).get("scanned_areas", list("BCDE")))
    areas, counts, ready = bedrock(items, scanned)

    open_items = [i for i in items if is_open(i)]
    tally = {k: len([i for i in open_items if i["severity"] == k]) for k in SEV}
    leaks = sorted(open_items, key=lambda i: (SEV_ORDER[i["severity"]], EFF_ORDER.get(i["effort"], 9), i["id"]))[:5]
    nxt = sorted([i for i in open_items if i["approval"] in ("proposed", "approved")],
                 key=lambda i: (EFF_ORDER.get(i["effort"], 9), SEV_ORDER[i["severity"]], i["id"]))
    nxt = [i for i in nxt if i["effort"] == "S"][:3] or nxt[:3]
    waiting = [i for i in open_items if i["approval"] == "proposed"]
    destr = [i for i in waiting if i.get("destructive")]
    conf = {}
    for i in items:
        conf[i["confidence"]] = conf.get(i["confidence"], 0) + 1
    ncount = max(1, len(items))
    conf_txt = " · ".join(f"{k} {round(100 * v / ncount)} %" for k, v in sorted(conf.items()))
    unread = runjson.get("sources_unreadable") or run.get("params", {}).get("sources_unreadable", [])
    n_ready = sum(1 for a in "CDE" if areas[a] == "green")

    h = []
    title = "Dein Fundament" if client else f"Un-Burning · {e(run['client_slug'])}"
    h.append(f"<!doctype html><html lang=\"de\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">")
    h.append(f"<title>{e(title)}</title><style>{CSS}</style></head><body><div class=\"wrap\">")
    h.append("<div class=\"top\"><div class=\"brand\"><span class=\"logo\">741</span><b>Un-Burning</b></div>")
    status = "Entwurf" if True else ""
    h.append("<div class=\"meta\">" + (f"{e(run['client_slug'])} <span class=\"pill\">{status}</span>" if client else f"{e(run['client_slug'])} · Lauf {e(run['run_id'])} · Modus {e(run['mode'])} <span class=\"pill\">{status}</span>") + "</div></div>")
    h.append(f"<h1>{'Was wir bereinigt haben' if client else 'Schadensbilanz'}</h1>")
    h.append(f"<div class=\"meta\">Stand: {e(run['started_at'][:10])} · Quelle: Google-Daten und Live-Prüfung</div>")

    # --- page 1
    h.append("<div class=\"lights\">")
    for a in "BCDE":
        op, bl, lk = counts[a]
        note = "nicht geprüft" if areas[a] == "grey" else (f"{op} offen" if client else f"{op} offen · {bl} blockieren Umsatz")
        h.append(f"<div class=\"light {areas[a]}\"><div class=\"k\">{a}</div><div class=\"n\">{e(AREA_NAME[a])}<br>{e(note)}</div>"
                 f"<div class=\"s\">{LIGHT_LABEL[areas[a]].upper()}</div></div>")
    h.append("</div>")
    verdict = ("Bereit für Wachstums-SEO." if ready else
               f"Noch nicht bereit für Wachstums-SEO: {n_ready} von 3 Kernbereichen (C, D, E) sind grün. Grau heißt nicht geprüft, nie grün.")
    if not client:
        h.append(f"<div class=\"verdict\"><b>Fundament-Check</b> · {e(verdict)}</div>")
    if client:
        verdict_c = T["ready"] if ready else T["work"]
        h.append(f"<div class=\"verdict\"><b>Stand</b> · {e(verdict_c)}</div>")
        done = [i for i in items if i["approval"] == "done"]
        todo = sorted([i for i in items if is_open(i) and i["approval"] in ("proposed", "approved") and not i.get("destructive")],
                      key=lambda i: (SEV_ORDER[i["severity"]], EFF_ORDER.get(i["effort"], 9), i["id"]))[:5]
        h.append("<div class=\"grid2\"><div class=\"card\"><h3>Schon erledigt</h3>")
        if done:
            h.append("<ul>" + "".join(f"<li>{e(short(i['item']))}</li>" for i in done) + "</ul>")
        else:
            h.append("<p class=\"muted\">Noch nichts. Wir haben gerade erst angefangen.</p>")
        h.append("</div><div class=\"card\"><h3>Das ist als Nächstes dran</h3><ol class=\"next\">")
        for i in todo:
            h.append(f"<li>{e(short(i.get('client_text') or i['item'], 130))}</li>")
        h.append("</ol></div></div>")
        h.append("<div class=\"grid2\" style=\"margin-top:16px\"><div class=\"card\"><h3>" + T["todo"] + "</h3><p>" + T["todo_text"] + "</p></div>")
        h.append("<div class=\"card\"><h3>Wirkung (vorher / nachher)</h3>")
        if metrics:
            h.append("<div class=\"tw\"><table><tr><th>Kennzahl</th><th>Vorher</th><th>Jetzt</th></tr>")
            for m in metrics.get("metrics", []):
                h.append(f"<tr><td>{e(m['name'])}</td><td>{e(m.get('baseline'))}<div class=\"muted\">{e(m.get('baseline_date'))}</div></td><td>{e(m.get('now', '–'))}</td></tr>")
            h.append("</table></div><div class=\"note\">Bewegung kann auch andere Ursachen haben. Verglichen wird nur mit gleichen Zeiträumen.</div>")
        h.append("</div></div></div></body></html>")
        path = out or (folder / "report" / "client.html")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("".join(h), encoding="utf-8")
        print(f"wrote {path} (client-safe, {len(done)} done, {len(todo)} next)")
        return 0

    h.append("<div class=\"grid2\"><div class=\"card\"><h3>Schadensbilanz</h3><div class=\"tally\">")
    h.append(f"<div><b>{len(open_items)}</b><span>offene Einträge</span></div>")
    h.append(f"<div><b style=\"color:var(--red)\">{tally['blocks_revenue']}</b><span>blockieren Umsatz</span></div>")
    h.append(f"<div><b style=\"color:var(--yellow)\">{tally['leaks_link_power']}</b><span>kosten Linkkraft</span></div>")
    h.append(f"<div><b style=\"color:var(--grey)\">{tally['cosmetic']}</b><span>kosmetisch</span></div></div></div>")
    h.append("<div class=\"card\"><h3>Die 5 größten Lecks</h3><ol class=\"leaks\">")
    for i in leaks:
        lab, cls = SEV[i["severity"]]
        h.append(f"<li><span class=\"chip {cls}\">{lab}</span> {e(short(i['item']))} <span class=\"muted\">· Bereich {i['area']} · Aufwand {i['effort']}</span></li>")
    h.append("</ol></div></div>")

    h.append("<div class=\"grid2\" style=\"margin-top:16px\"><div class=\"card\"><h3>Nächste 3 Aktionen</h3><ol class=\"next\">")
    for i in nxt:
        detail = short(i.get("action_detail") or ACT[i["action"]], 130)
        h.append(f"<li>{e(detail)} <span class=\"muted\">· wer: {e(WHO[i['actor']])} · Aufwand {i['effort']}</span></li>")
    h.append("</ol></div>")
    if client:
        h.append("<div class=\"card\"><h3>" + T["todo"] + "</h3><p>" + T["todo_text"] + "</p></div></div>")
    else:
        h.append(f"<div class=\"card\"><h3>Deine Freigaben (GO-1)</h3><p><b>{len(waiting)}</b> Einträge warten auf Entscheidung. "
                 f"<b>{len(destr)}</b> davon sind destruktiv und brauchen ein Einzel-Go.</p><p><a href=\"#killlist\">Zur Liste</a></p></div></div>")

    h.append("<div class=\"grid2\" style=\"margin-top:16px\"><div class=\"card\"><h3>Wirkung (vorher / nachher)</h3>")
    if metrics:
        h.append("<div class=\"tw\"><table><tr><th>Kennzahl</th><th>Basis</th><th>Jetzt</th><th>Hinweis</th></tr>")
        for m in metrics.get("metrics", []):
            h.append(f"<tr><td>{e(m['name'])}</td><td>{e(m.get('baseline'))}<div class=\"muted\">{e(m.get('baseline_date'))}</div></td>"
                     f"<td>{e(m.get('now', '–'))}<div class=\"muted\">{e(m.get('now_date', ''))}</div></td><td class=\"muted\">{e(m.get('note', ''))}</td></tr>")
        h.append("</table></div><div class=\"note\">Bewegung kann auch andere Ursachen haben. Verglichen wird nur mit gleichen Zeiträumen.</div>")
    else:
        h.append("<p class=\"muted\">nicht gelesen (keine metrics.json)</p>")
    h.append("</div>")
    h.append("<div class=\"card\"><h3>Datenlage</h3>")
    h.append(f"<p>Einträge: <b>{len(items)}</b> · Vertrauen: {e(conf_txt)}</p>")
    if unread:
        h.append(f"<p>Nicht lesbar oder nicht geprüft: <b>{len(unread)}</b> Quellen</p><ul>")
        for u in unread[:12]:
            h.append("<li>" + (e(u.get("source", "")) + " <span class=\"muted\">· " + e(u.get("error", "")) + "</span>" if isinstance(u, dict) else e(u)) + "</li>")
        h.append("</ul>")
    else:
        h.append("<p class=\"muted\">Keine nicht lesbaren Quellen gemeldet.</p>")
    h.append("</div></div>")

    # --- area tables
    h.append("<h2>Bereiche B bis E</h2>")
    for a in "BCDE":
        its = sorted([i for i in items if i["area"] == a], key=lambda i: (SEV_ORDER[i["severity"]], i["id"]))
        light = areas[a]
        h.append(f"<details {'open' if its and light in ('red','yellow') else ''}><summary>{a} · {e(AREA_NAME[a])} <span class=\"chip st\">{LIGHT_LABEL[light]}</span> <span class=\"muted\">{len(its)} Einträge</span></summary>")
        if not its:
            h.append("<p class=\"muted\">Keine Einträge" + (" (Bereich nicht geprüft)." if a not in scanned else ".") + "</p></details>")
            continue
        h.append("<div class=\"tw\"><table><tr><th>ID</th><th>Eintrag</th><th>Ziel</th><th>Schwere</th><th>Aktion</th><th>Wer</th><th>Aufw.</th><th>Status</th><th>Vorher → Nachher</th>" + ("" if client else "<th>Beleg</th>") + "</tr>")
        for i in its:
            lab, cls = SEV[i["severity"]]
            sc = "st-done" if i["approval"] == "done" else ("st-ok" if i["approval"] == "approved" else "st")
            ba = f"{e(i.get('before', ''))} → {e(i.get('after', ''))}" if i.get("after") is not None else e(i.get("before", ""))
            ev = ", ".join(e(x) for x in i.get("evidence_ids", []))
            lock = " <span class=\"lock\">🔒</span>" if i.get("destructive") else ""
            h.append(f"<tr><td>{e(i['id'])}</td><td>{e(i['item'])}<div class=\"muted\">{e(i.get('why', ''))}</div></td><td><code title=\"{e(i.get('target', ''))}\">{e(short((i.get('target') or '').replace('https://', '').replace('http://', ''), 34))}</code></td>"
                     f"<td><span class=\"chip {cls}\">{lab}</span></td><td>{e(ACT[i['action']])}{lock}</td><td>{e(WHO[i['actor']])}</td><td>{e(i['effort'])}</td>"
                     f"<td><span class=\"chip {sc}\">{e(APPR[i['approval']])}</span></td><td>{ba}</td>" + ("" if client else f"<td>{ev}</td>") + "</tr>")
        h.append("</table></div></details>")

    # --- kill list
    if not client:
        h.append("<h2 id=\"killlist\">Behalten · Reparieren · Entfernen (GO-1)</h2>")
        h.append("<p class=\"note\">Die Seite speichert nichts. Der Export erzeugt <code>approvals.json</code> für den Agenten. 🔒 = Einzel-Go nötig.</p>")
        h.append("<p><button class=\"btn prim\" id=\"export\">approvals.json exportieren</button> <span class=\"muted\">Entscheidungen: <b id=\"dcount\">0</b></span></p>")
        h.append("<div class=\"tw\"><table><tr><th>ID</th><th>Eintrag</th><th>Vorschlag</th><th>Entscheidung</th></tr>")
        for i in sorted(waiting, key=lambda i: (SEV_ORDER[i["severity"]], i["id"])):
            lab, cls = SEV[i["severity"]]
            lock = " <span class=\"lock\">🔒 Einzel-Go</span>" if i.get("destructive") else ""
            h.append(f"<tr data-item=\"{e(i['id'])}\"><td>{e(i['id'])}</td><td><span class=\"chip {cls}\">{lab}</span> {e(i['item'])}</td>"
                     f"<td>{e(i.get('action_detail') or ACT[i['action']])}{lock}</td><td><div class=\"btns\">"
                     "<button class=\"btn\" data-d=\"keep\">Behalten</button><button class=\"btn\" data-d=\"fix\">Reparieren</button>"
                     "<button class=\"btn\" data-d=\"kill\">Entfernen</button><button class=\"btn\" data-d=\"hold\">Zurückstellen</button></div></td></tr>")
        h.append("</table></div>")

    # --- companion summaries
    def count_of(x):
        if x is None:
            return None
        if isinstance(x, list):
            return len(x)
        for k in ("rows", "entries", "corrections", "redirects", "urls", "pages", "items"):
            if k in x and isinstance(x[k], list):
                return len(x[k])
        return None
    h.append("<h2>Begleitansichten</h2><div class=\"tw\"><table><tr><th>Ansicht</th><th>Zeilen</th><th>Datei</th></tr>")
    for label, data, fn in [("NAP-Korrekturen", nap, "nap-corrections.json"), ("Weiterleitungs-Karte", redir, "redirect-map.json"),
                            ("Indexiert vs. gewollt", idx, "index-intended.json"), ("Link-Plan (umgekehrter Baum)", plan, "link-plan.json")]:
        c = count_of(data)
        h.append(f"<tr><td>{label}</td><td>{'nicht gelesen' if data is None else (c if c is not None else 'Objekt')}</td><td><code>{fn}</code></td></tr>")
    h.append("</table></div>")

    # --- evidence index
    if not client:
        h.append("<h2>Belegindex</h2><div class=\"tw\"><table><tr><th>ID</th><th>Typ / Tool</th><th>Datum</th><th>sha256</th><th>Datei</th></tr>")
        for m in (mentries or [])[:200]:
            h.append(f"<tr><td>{e(m.get('id'))}</td><td>{e(m.get('kind', ''))} {e(m.get('tool', ''))}</td><td>{e(m.get('collected_at', m.get('date', '')))}</td>"
                     f"<td><code>{e(str(m.get('sha256', ''))[:12])}</code></td><td><code>{e(m.get('file', m.get('storage_path', '')))}</code></td></tr>")
        h.append("</table></div>")
        data = json.dumps(reg, ensure_ascii=False).replace("</", "<\\/")
        h.append(f"<script type=\"application/json\" id=\"un-burning-data\">{data}</script>")

    h.append("</div><script>" + JS + "</script></body></html>")
    path = out or (folder / "report" / ("client.html" if client else "internal.html"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(h), encoding="utf-8")
    print(f"wrote {path} ({len(items)} items, areas {areas}, ready={ready})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
