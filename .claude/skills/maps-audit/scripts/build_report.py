"""Build report/internal.html and report/client.html from a scored run folder. Usage: python3 build_report.py <run_dir>"""
import json, os, sys, html, re
HERE = os.path.dirname(os.path.abspath(__file__))
CAT = json.load(open(os.path.join(HERE, '..', 'catalog.json')))
run_dir = sys.argv[1]
L = lambda n, d=None: json.load(open(os.path.join(run_dir, n))) if os.path.exists(os.path.join(run_dir, n)) else d
run, F, KW, CMP, MAN, ACT, TK = L('run.json'), L('findings.json'), L('keywords.json'), L('competitors.json'), L('manifest.json'), L('actions.json'), L('takeaways.json', {})
FB = {f['field_id']: f for f in F}; labels = {f['field_id']: f for f in CAT['fields']}
e = lambda s: html.escape(str(s if s is not None else ''), quote=True)
LIGHT = {'green': ('●', 'grün'), 'yellow': ('●', 'gelb'), 'red': ('●', 'rot'), 'grey': ('○', 'neutral'), 'unknown': ('○', 'offen'), 'offen': ('○', 'offen'), 'unvollständig': ('◐', 'unvollständig')}
def dot(st): g, t = LIGHT.get(st, ('○', st)); return f'<span class="dot {st}" title="{t}"><b aria-hidden="true">{g}</b><span class="sr">{t}</span></span>'
def date_of(f): return f['collected_at'][8:10] + '.' + f['collected_at'][5:7] + '.'
CSS = """
:root{--bg:#f7f6f2;--card:#fff;--ink:#1c1f23;--mut:#5d646c;--line:#e3e1da;--acc:#fac118;--g:#1f8a4c;--y:#b7791f;--r:#c53030;--n:#7a828a;--gbg:#e6f4ec;--ybg:#fcf3dc;--rbg:#fbe6e6;--nbg:#eceef0}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#15171a;--card:#1e2125;--ink:#ecebe6;--mut:#a3a9b0;--line:#33373c;--g:#4cc27f;--y:#e5b04a;--r:#f07a7a;--n:#9aa1a8;--gbg:#17301f;--ybg:#352b12;--rbg:#3a1c1c;--nbg:#2a2d31}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 'DM Sans',system-ui,-apple-system,Segoe UI,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:24px 16px 64px}h1{font-size:22px;margin:0}h2{font-size:17px;margin:28px 0 10px}h3{font-size:15px;margin:0}
.top{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px;align-items:baseline;border-bottom:3px solid var(--acc);padding-bottom:10px}.meta{color:var(--mut);font-size:13px}
.grid2{display:grid;grid-template-columns:minmax(220px,1fr) 2fr;gap:14px;margin-top:16px}@media(max-width:760px){.grid2{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}
.score{font-size:56px;font-weight:700;line-height:1}.score small{font-size:20px;color:var(--mut);font-weight:500}
.chip{display:inline-block;padding:3px 12px;border-radius:99px;font-weight:700;font-size:14px}.chip.Ja{background:var(--gbg);color:var(--g)}.chip.Noch\\ nicht{background:var(--ybg);color:var(--y)}.chip.Nein{background:var(--rbg);color:var(--r)}.chip.Offen{background:var(--nbg);color:var(--n)}
.dot b{font-size:16px;line-height:1}.dot.green{color:var(--g)}.dot.yellow{color:var(--y)}.dot.red{color:var(--r)}.dot.grey,.dot.unknown,.dot.offen,.dot.unvollständig{color:var(--n)}.sr{position:absolute;left:-9999px}
.bar{height:10px;border-radius:6px;background:var(--nbg);overflow:hidden}.bar i{display:block;height:100%;background:var(--acc)}
.kw{display:grid;grid-template-columns:minmax(150px,1.1fr) 2fr minmax(110px,1fr);gap:10px;align-items:center;padding:7px 0;border-top:1px solid var(--line)}.kw:first-of-type{border-top:0}
@media(max-width:640px){.kw{grid-template-columns:1fr}}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px}.tile{display:block;color:inherit;text-decoration:none;background:var(--card);border:1px solid var(--line);border-left:5px solid var(--n);border-radius:10px;padding:10px 12px}
.tile.green{border-left-color:var(--g)}.tile.yellow{border-left-color:var(--y)}.tile.red{border-left-color:var(--r)}.tile .id{font-size:12px;color:var(--mut)}.tile p{margin:4px 0 0;font-size:13px;color:var(--mut)}.tile:hover{border-color:var(--acc)}
table{width:100%;border-collapse:collapse;font-size:14px}th,td{text-align:left;padding:7px 8px;border-top:1px solid var(--line);vertical-align:top}th{font-size:12px;color:var(--mut);font-weight:600}
.badge{display:inline-block;font-size:11px;padding:1px 7px;border-radius:99px;background:var(--nbg);color:var(--mut);white-space:nowrap;text-decoration:none}a.badge:hover{background:var(--acc);color:#1c1f23}
details.blk{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:10px 0;padding:0 14px}details.blk>summary{cursor:pointer;padding:12px 0;display:flex;gap:10px;align-items:center;flex-wrap:wrap;list-style:none}details.blk>summary::-webkit-details-marker{display:none}
details.blk>summary .nm{font-weight:700}details.blk>summary .tk{color:var(--mut);font-size:13px;flex-basis:100%}
details.row summary{cursor:pointer}details.row .more{margin:6px 0 4px;padding:8px 10px;background:var(--bg);border-radius:8px;font-size:13px;color:var(--mut)}.more b{color:var(--ink)}
.flag{border-left:4px solid var(--r);padding:6px 10px;margin:6px 0;background:var(--rbg);border-radius:6px;font-size:14px}.miss{border-left:4px solid var(--n);padding:6px 10px;margin:6px 0;background:var(--nbg);border-radius:6px;font-size:14px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media(max-width:760px){.two{grid-template-columns:1fr}}
.note{font-size:12px;color:var(--mut)}code{font-size:12px;background:var(--nbg);padding:1px 5px;border-radius:4px}.draft{background:var(--ybg);color:var(--y);padding:6px 12px;border-radius:8px;font-weight:600;font-size:13px;display:inline-block;margin-top:8px}
footer{margin-top:40px;color:var(--mut);font-size:12px}
@media print{body{background:#fff}.wrap{padding:0}details.blk:not([open])>*:not(summary){display:none}}
"""
def cut(t, n=170):
    t = str(t)
    if len(t) <= n: return t
    parts = re.split(r'(?<=[.!?]) ', t); out = ''
    for q in parts:
        if len(out) + len(q) + 1 > n: break
        out += (' ' if out else '') + q
    return out or t[:n].rsplit(' ', 1)[0] + '…'
RES = {'realistic': 'realistisch', 'slow': 'langsam', 'unrealistic': 'unrealistisch', 'unknown': 'offen'}
def fmt_pct(x): return f"{x:.0f} %" if x is not None else 'n/a'
ORDER = ['B05', 'B10', 'B11', 'B06', 'B07', 'B13', 'B12', 'B04', 'B01', 'B02', 'B03', 'B08', 'B09']
def tiles(blocks, client=False):
    out = []
    for b in blocks:
        v = run['blocks'][b]; st = v['light']; cls = st if st in ('green', 'yellow', 'red') else ''
        sc = f"{v['score']}/100" if v['weight'] and v['score'] is not None and st in ('green', 'yellow', 'red') else ('Datenlage ' + fmt_pct((v['coverage'] or 0) * 100) if st != 'offen' else 'offen')
        out.append(f'<a class="tile {cls}" href="#{b}">{dot(st)} <b>{e(v["name"])}</b><div class="id">{b} · {sc}</div><p>{e(TK.get(b, ""))}</p></a>')
    return '<div class="tiles">' + ''.join(out) + '</div>'
def kw_rows():
    r = []
    for k in KW:
        if k['priority'] != 1: continue
        g = k['falcon']['google'] or {}; s = g.get('solv'); lead = k.get('leader')
        r.append(f'<div class="kw"><div><b>{e(k["keyword"])}</b><div class="note">Prio 1 · Suchen/Monat: {(k.get("volume_de") or k.get("volume_indonesia")) or "keine Daten"}</div></div><div><div class="bar" role="img" aria-label="Top-3-Fläche {s} Prozent"><i style="width:{max(2,s or 0)}%"></i></div><div class="note">Top-3-Fläche {fmt_pct(s) if s is not None else "nicht gemessen"} · Ø-Rang {g.get("arp") if g.get("arp") is not None else "–"}</div></div><div class="note">{("Führend: " + e(lead["name"][:34]) + f" {lead['solv']:.0f} %") if lead else ""}</div></div>')
    return ''.join(r)
def evlink(eid):
    m = next((x for x in MAN['evidence'] if x['id'] == eid), None)
    return m
def src_badge(f):
    ids = f.get('evidence_ids') or []
    inner = f"{e(f['source_tool'])} · {date_of(f)}"
    return f'<a class="badge" href="#ev-{ids[0]}" title="Beleg {ids[0]}">{inner}</a>' if ids else f'<span class="badge">{inner}</span>'
def row(f, client=False):
    lab = labels[f['field_id']]['label_de']
    if client: lab = re.sub(r'\s*\(.*?\)', '', lab)
    text = f.get('client_text_de') if client else f['finding_de']
    if client and not text: return ''
    more = []
    if not client:
        if f.get('why_de'): more.append(f"<b>Warum wichtig:</b> {e(f['why_de'])}")
        if f.get('action_de'): more.append(f"<b>Nächster Schritt:</b> {e(f['action_de'])} · Wer: {e(f.get('owner'))} · Aufwand {e(f.get('effort'))} · Wirkung {e(f.get('impact'))}/5")
        more.append(f"<b>Sicherheit:</b> {e(f['confidence'])}" + (f" · <b>Rohdaten:</b> " + ', '.join(f'<a href="#ev-{i}">{i}</a>' for i in f.get('evidence_ids', [])) if f.get('evidence_ids') else ''))
        if f.get('drilldown_hint'): more.append(f"<b>Tiefer prüfen:</b> {e(f['drilldown_hint'])}")
        if f.get('refetch'): more.append(f"<b>Wiederholen:</b> <code>{e(json.dumps(f['refetch'], ensure_ascii=False))}</code>")
    short = text if len(text) < 160 else text[:157] + '…'
    body = f'<details class="row"><summary>{e(short)}</summary><div class="more">{"<br>".join(more) if more else e(text)}</div></details>' if (more and not client) else e(text)
    badge = f'<span class="badge">Google-Daten · {date_of(f)}</span>' if client else src_badge(f)
    attrs = '' if client else f' data-field-id="{f["field_id"]}" data-status="{f["status"]}" data-evidence="{",".join(f.get("evidence_ids", []))}"'
    return f'<tr{attrs}><td>{dot(f["status"])}</td><td class="note">{f["field_id"]}</td><td>{e(lab)}</td><td>{body}</td><td>{badge}</td></tr>'
def block(b, client=False):
    v = run['blocks'][b]; rows = ''.join(row(f, client) for f in CAT['fields'] if f['block'] == b for f in [FB[f['field_id']]] if (not client) or f['client_safe'])
    if client and not rows: return ''
    extra = ''
    if b == 'B11' and not client:
        kws = [k['keyword'] for k in KW if k['priority'] == 1]
        hdr = '<tr><th>Wettbewerber</th>' + ''.join(f'<th>{e(k)} Top-3 %</th>' for k in kws) + '<th>Bewertungen</th><th>Kategorien</th><th>Linking-Domains</th></tr>'
        rs = ''.join(f"<tr><td><b>{e(c['name'])}</b><div class='note'>{e(c['pick_reason'])}</div></td>" + ''.join(f"<td>{c['solv'].get(k, '–')}</td>" for k in kws) + f"<td>{c['reviews'] if c['reviews'] is not None else '–'}</td><td>{e(', '.join(c['categories'] or []))}</td><td>{c['ref_domains'] if c.get('ref_domains') is not None else '–'}</td></tr>" for c in CMP)
        o = run.get('own')
        own = (f"<tr><td><b>{e(o['name'])}</b></td>" + ''.join(f"<td>{o['solv'].get(k, '–')}</td>" for k in kws) + f"<td>{o['reviews']}</td><td>{e(', '.join(o['categories']))}</td><td>{o['ref_domains']}</td></tr>") if o else ''
        extra = f'<div style="overflow-x:auto"><table><thead>{hdr}</thead><tbody>{rs}{own}</tbody></table></div><p class="note">SoLV in %, Google Maps, Raster und Datum siehe Kopf. Bewertungen der Wettbewerber: {e((CMP[0].get('reviews_source') if CMP else '') or 'öffentliches Google-Profil')}. 0 kann „keine Daten" heißen.</p>'
    sc = f"{v['score']}/100" if v['score'] is not None and v['weight'] else ('Datenlage ' + fmt_pct((v['coverage'] or 0) * 100))
    return f'<details class="blk" id="{b}"{" open" if v["light"]=="red" and v["weight"]>=15 and not client else ""}><summary>{dot(v["light"])} <span class="nm">{b} {e(v["name"])}</span> <span class="badge">{sc}</span><span class="tk">{e(TK.get(b, ""))}</span></summary>{extra}<div style="overflow-x:auto"><table><thead><tr><th></th><th>ID</th><th>Feld</th><th>Befund</th><th>Quelle</th></tr></thead><tbody>{rows}</tbody></table></div></details>'
CLIENT_ACTIONS = {'B10.01': 'Kategorien im Profil mit Ihnen abstimmen und ergänzen (zum Beispiel "Tax attorney").', 'B05.06': 'Messraster mit der neuen Adresse festlegen und die Sichtbarkeit neu messen.',
    'B06.05': 'Neue Adresse festlegen und in Profil, Website und Verzeichnissen in einer geplanten Reihenfolge angleichen.', 'B10.02': 'Leistungen im Profil anlegen, zu denen Ihre Website eine eigene Seite hat.',
    'B06.02': 'Startseite um sichtbare Telefonnummer und Anfrage-Möglichkeit ergänzen.', 'B06.01': 'Eigentümer-Rollen der Konten gemeinsam prüfen.'}
def actions(client=False, n=3):
    rows = []
    for a in ACT:
        f = FB[a['field_id']]
        if client and not (f['client_safe'] and f.get('client_text_de')): continue
        if client and a['field_id'] not in CLIENT_ACTIONS: continue
        t = CLIENT_ACTIONS[a['field_id']] if client else a['action_de']
        who = {'741': '741', 'Kunde': 'Ihre Kanzlei' if client else 'Kundin', 'Dritte': 'Website-Betreuung' if client else 'Dritte'}.get(a['owner'], a['owner'])
        rows.append(f"<tr><td><b>{len(rows)+1}</b></td><td>{e(t)}</td><td>{'●' * (a['impact'] or 0)}{'○' * (5 - (a['impact'] or 0))}</td><td>{e(a['effort'])}</td><td>{e(who)}</td></tr>")
        if len(rows) == n: break
    return '<table><thead><tr><th></th><th>Aktion</th><th>Wirkung</th><th>Aufwand</th><th>Wer</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table>'
def internal():
    crit = {f['field_id'] for f in CAT['fields'] if f['critical']}
    flags = [f for f in sorted(F, key=lambda f: (-run['blocks'][f['field_id'][:3]]['weight'], f.get('priority_rank') or 99)) if (f['field_id'] in crit or (f.get('impact') or 0) >= 5) and f['status'] == 'red']
    flags += [FB[i] for i in ('B13.02', 'B09.03', 'B06.01', 'B13.05', 'B06.05') if FB[i]['status'] == 'yellow' and FB[i] not in flags]
    flags = flags[:5]
    miss = [f for f in F if f['status'] == 'unknown' and f['field_id'] not in ('B09.04', 'B11.08', 'B11.09')]
    cap = run.get('cap')
    ev_rows = ''.join(f"<tr id='ev-{m['id']}'><td><code>{m['id']}</code></td><td>{e(m['kind'])}</td><td>{e(m['tool'])}</td><td>{m['collected_at'][:10]}</td><td>{e(m['note'])}</td><td><a href='../{e(m['file'])}'>{e(os.path.basename(m['file']))}</a></td><td class='note'>{m['sha256'][:10]}</td></tr>" for m in MAN['evidence'])
    kw_rows_raw = ''.join(f"<tr><td>{e(k['keyword'])}</td><td>{k['priority']}</td><td>{k['volume_de'] if k['volume_de'] is not None else 'k. D.'}</td><td>{(k['falcon']['google'] or {}).get('solv', '–')}</td><td>{', '.join(f'{p} {v}' for p, v in k['falcon']['ai_platforms_solv'].items())}</td></tr>" for k in KW)
    data = json.dumps(dict(run=run, findings=F, keywords=KW, competitors=CMP), ensure_ascii=False).replace('</', '<\\/')
    realism = ''.join(f"<li><b>{e(r['keyword'])}</b>: {e(RES.get(r['result'], r['result']))} — {e(r['reason'])}</li>" for r in run['realism'])
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Maps-Audit {e(run['subject_name'])}</title><style>{CSS}</style></head><body><div class="wrap">
<div class="top"><h1>{e(run['subject_name'])} · Maps-Audit ({e(run['mode'])})</h1><div class="meta">Stand {run['started_at'][8:10]}.{run['started_at'][5:7]}.{run['started_at'][:4]} · Datenlage {int(run['score_coverage']*100)} % · intern · Entwurf</div></div>
<div class="grid2"><div class="card"><div class="meta">{"Traffic-Readiness (Ads)" if run.get("strategy") == "paid" else "Maps-Readiness"}</div><div class="score">{run['score_total']}<small> / 100</small></div><div class="note">Datenlage {int(run['score_coverage']*100)} %. Erste Messreihe, kein Trend.{(' Deckel 50 wegen ' + ', '.join(cap['fields'])) if cap else ''}</div></div>
<div class="card"><div class="meta">Eignung (Fit-Check)</div><p><span class="chip {e(run['verdict'])}">{e(run['verdict'])}</span></p><p>{e(run['verdict_reason'])}</p></div></div>
<h2>Wo wir stehen — Top-3-Fläche je Suchbegriff (Google Maps, {e(run['params']['grid'])}, {e(run['params']['radius'])})</h2><div class="card">{kw_rows()}<p class="note">{e(run.get('kw_note') or '')}</p></div>
<h2>{'Traffic-Readiness (Ads): 9 Blöcke' if run.get('strategy') == 'paid' else 'Maps-Readiness: 8 Blöcke'}</h2>{tiles([b for b in (['B06','B05','B03','B04','B13','B10','B07','B11','B12'] if run.get('strategy') == 'paid' else ['B05','B10','B11','B06','B07','B13','B12','B04']) if run['blocks'][b]['weight']])}
<h2>Geschäftliche Eignung (zählen nicht in den Score)</h2>{tiles([b for b in ['B01','B02','B03','B08','B09'] if not run['blocks'][b]['weight']])}
<h2>Die 3 ersten Aktionen</h2><div class="card">{actions(False)}<p class="note">Jede Änderung an Profil, Website oder Verzeichnissen braucht Martins Go einzeln.</p></div>
<div class="two"><div><h2>Rote Flaggen</h2>{''.join(f'<div class="flag">{dot(f["status"])} <b>{f["field_id"]}</b> {e(cut(f["finding_de"], 190))}</div>' for f in flags)}</div>
<div><h2>Was fehlt ({len(miss)} Felder offen)</h2>{''.join(f'<div class="miss"><b>{f["field_id"]}</b> {e(cut(f["finding_de"], 130))}</div>' for f in miss[:5])}<details><summary class="note">Alle {len(miss)} anzeigen</summary>{''.join(f'<div class="miss"><b>{f["field_id"]}</b> {e(cut(f["finding_de"], 130))}</div>' for f in miss[5:])}</details></div></div>
<h2>Realismus für Platz 1 je Prio-1-Begriff</h2><div class="card"><ul>{realism}</ul><p class="note">Regel D1: erst Treiber finden (Spearman Bewertungen gegen Sichtbarkeit; Kategorie-Lift), dann prüfen, was steuerbar ist.</p></div>
<h2>Detail je Block</h2>{''.join(block(b) for b in ORDER)}
<h2>Rohdaten</h2><div class="card" style="overflow-x:auto"><h3>Belege</h3><table><thead><tr><th>ID</th><th>Art</th><th>Tool</th><th>Datum</th><th>Inhalt</th><th>Datei</th><th>Hash</th></tr></thead><tbody>{ev_rows}</tbody></table>
<h3 style="margin-top:16px">Keywords</h3><table><thead><tr><th>Keyword</th><th>Prio</th><th>Suchen/Monat DE</th><th>Maps Top-3 %</th><th>KI-Plattformen Top-3 %</th></tr></thead><tbody>{kw_rows_raw}</tbody></table>
<h3 style="margin-top:16px">Kosten</h3><p>DataForSEO {run['cost']['dataforseo_usd']} USD (Limit 8 EUR). Local Falcon 0 Credits neu (Limit 800; Konto am 11.10.: 797 nutzbar). Go-A: {e(run['go_a']['decision'])}</p></div>
<footer>Lauf {e(run['run_id'])} · Katalog {e(run['catalog_version'])} · Modus {e(run['mode'])} · Raster {e(run['params']['grid'])}, {e(run['params']['radius'])}</footer></div>
<script type="application/json" id="audit-data">{data}</script></body></html>"""
def client():
    blocks = ['B05', 'B10', 'B06', 'B13', 'B12', 'B04', 'B07']
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Ihre Sichtbarkeit auf Google Maps</title><style>{CSS}</style></head><body><div class="wrap">
<div class="top"><h1>{e(run['subject_name'])} · Sichtbarkeit auf Google Maps</h1><div class="meta">Stand {run['started_at'][8:10]}.{run['started_at'][5:7]}.{run['started_at'][:4]}</div></div><span class="draft">Entwurf – noch nicht freigegeben</span>
<div class="grid2"><div class="card"><div class="meta">Maps-Readiness</div><div class="score">{run['score_total']}<small> / 100</small></div><div class="note">Erste Messung. Sie dient als Ausgangspunkt für die nächsten Monate.</div></div>
<div class="card"><h3>Was das Ergebnis sagt</h3><p>Ihre Kanzlei ist bei Google gut bewertet, aber das Profil und die Website nutzen noch wenig von dem, was Google für ein Ranking in Maps prüft. Die größten Hebel sind die Kategorien im Profil, die Leistungen, die Adresse nach dem Umzug und eine klare Anfrage-Möglichkeit auf der Website.</p></div></div>
<h2>Wo Sie stehen</h2><div class="card">{kw_rows()}</div>
<h2>Die ersten Schritte</h2><div class="card">{actions(True)}<p class="note">Änderungen am Profil, an der Website und an Verzeichnissen setzen wir erst nach Ihrer Freigabe um.</p></div>
<h2>Bereiche</h2>{tiles([b for b in blocks if block(b, True)], True)}
<h2>Detail</h2>{''.join(block(b, True) for b in blocks)}
<footer>Quelle: Google-Daten. Messungen vom 09.10. bis 11.10.2026.</footer></div></body></html>"""
os.makedirs(os.path.join(run_dir, 'report'), exist_ok=True)
open(os.path.join(run_dir, 'report', 'internal.html'), 'w').write(internal())
if run.get('client_lang', 'de') == 'de': open(os.path.join(run_dir, 'report', 'client.html'), 'w').write(client())
else: print('client.html skipped: client language is', run.get('client_lang'), '(client text needs English, build after Go-B)')
print('built', os.path.join(run_dir, 'report'))
