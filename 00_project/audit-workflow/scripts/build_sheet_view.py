"""Build a formatted xlsx (XlsxWriter, Google-compatible) from a run folder. Usage: <venv python> build_sheet_view.py <run_dir> <out.xlsx>"""
import json, os, sys, xlsxwriter
run_dir, out = sys.argv[1], sys.argv[2]
L = lambda n: json.load(open(os.path.join(run_dir, n)))
run, F, KW, CMP, ACT = L('run.json'), L('findings.json'), L('keywords.json'), L('competitors.json'), L('actions.json')
CAT = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'catalog.json')))
lab = {f['field_id']: f for f in CAT['fields']}
wb = xlsxwriter.Workbook(out)
base = dict(font_name='Arial', font_size=10, valign='top', text_wrap=True, border=1, border_color='#D9D9D9')
fmt = lambda **k: wb.add_format({**base, **k})
H = fmt(bold=True, font_color='#FFFFFF', bg_color='#1C1F23'); T = wb.add_format(dict(font_name='Arial', font_size=14, bold=True)); N = fmt(); Z = fmt(bg_color='#F7F6F2')
ST = {'green': ('grün', '#E6F4EC', '#1F8A4C'), 'yellow': ('gelb', '#FCF3DC', '#B7791F'), 'red': ('rot', '#FBE6E6', '#C53030'), 'grey': ('neutral', '#ECEEF0', '#7A828A'), 'unknown': ('offen', '#ECEEF0', '#7A828A')}
STF = {k: fmt(bold=True, bg_color=v[1], font_color=v[2], align='center') for k, v in ST.items()}
ws = wb.add_worksheet('Befunde'); ws.hide_gridlines(2)
ws.merge_range(0, 0, 0, 8, f"{run['subject_name']} · Maps-Audit {run['mode']} · Lauf {run['run_id']} · Hilfsdaten, nicht für die Kundin", T)
ws.write(1, 0, f"Maps-Readiness {run['score_total']}/100 · Datenlage {int(run['score_coverage']*100)} % · Eignung: {run['verdict']}. Alle Befunde mit Quelle, Datum, Sicherheit. Falsche oder ungenutzte Dateien dürfen in den Papierkorb.", fmt(border=0, italic=True))
cols = ['ID', 'Block', 'Feld', 'Status', 'Befund', 'Nächster Schritt', 'Wer', 'Aufwand', 'Wirkung', 'Quelle', 'Datum', 'Sicherheit', 'Belege']
w = [8, 18, 28, 9, 70, 50, 9, 8, 8, 22, 11, 13, 22]
for i, (c, x) in enumerate(zip(cols, w)): ws.write(3, i, c, H); ws.set_column(i, i, x)
r = 4
for fnd in sorted(F, key=lambda f: f['field_id']):
    meta = lab[fnd['field_id']]; z = Z if r % 2 else N
    vals = [fnd['field_id'], run['blocks'][meta['block']]['name'], meta['label_de'], None, fnd['finding_de'], fnd.get('action_de') or '', fnd.get('owner') or '', fnd.get('effort') or '', fnd.get('impact') or '', fnd['source_tool'], fnd['collected_at'][:10], fnd['confidence'], ', '.join(fnd.get('evidence_ids', []))]
    for i, v in enumerate(vals):
        if i == 3: ws.write(r, i, ST[fnd['status']][0], STF[fnd['status']])
        else: ws.write(r, i, v, z)
    r += 1
ws.freeze_panes(4, 3); ws.autofilter(3, 0, r - 1, len(cols) - 1)
ws2 = wb.add_worksheet('Blöcke'); ws2.hide_gridlines(2)
for i, (c, x) in enumerate(zip(['Block', 'Name', 'Gewicht', 'Ampel', 'Score', 'Datenlage', 'Felder gewertet', 'Felder offen'], [8, 44, 9, 14, 8, 10, 14, 12])): ws2.write(0, i, c, H); ws2.set_column(i, i, x)
for j, (b, v) in enumerate(run['blocks'].items(), 1):
    for i, x in enumerate([b, v['name'], v['weight'], v['light'], v['score'], v['coverage'], v['counted'], v['unknown']]): ws2.write(j, i, x, N if j % 2 else Z)
ws3 = wb.add_worksheet('Wettbewerber'); ws3.hide_gridlines(2)
kws1 = [k['keyword'] for k in KW if k['priority'] == 1]
hd = ['Name', 'Domain'] + [f'{k} Top-3 %' for k in kws1] + ['Bewertungen', 'Kategorien', 'Linking-Domains', 'Spam-Score', 'Auswahlgrund']
wid = [34, 26] + [14] * len(kws1) + [11, 40, 12, 10, 60]
for i, (c, x) in enumerate(zip(hd, wid)): ws3.write(0, i, c, H); ws3.set_column(i, i, x)
for j, c in enumerate(CMP, 1):
    row = [c['name'], c['domain']] + [c['solv'].get(k) for k in kws1] + [c['reviews'], ', '.join(c['categories'] or []), c.get('ref_domains'), c.get('spam_score'), c['pick_reason']]
    for i, x in enumerate(row): ws3.write(j, i, x, N if j % 2 else Z)
ws3.write(len(CMP) + 2, 0, 'Bewertungen der Wettbewerber: ' + (CMP[0].get('reviews_source', '') if CMP else '') + '. Linking-Domains: DataForSEO.', fmt(border=0, italic=True))
ws4 = wb.add_worksheet('Keywords'); ws4.hide_gridlines(2)
hd = ['Keyword', 'Prio', 'Leistung', 'Suchen/Monat', 'Maps Top-3 %', 'Maps Ø-Rang', 'Raster', 'ChatGPT %', 'Gemini %', 'AI Mode %', 'AI Overviews %']
for i, (c, x) in enumerate(zip(hd, [30, 6, 32, 14, 12, 12, 22, 11, 11, 11, 14])): ws4.write(0, i, c, H); ws4.set_column(i, i, x)
for j, k in enumerate(KW, 1):
    g = k['falcon']['google'] or {}; a = k['falcon'].get('ai_platforms_solv') or {}; pr = k['falcon'].get('params', {})
    vol = k.get('volume_de') or k.get('volume_indonesia')
    for i, x in enumerate([k['keyword'], k['priority'], k['service_ref'], vol if vol is not None else 'keine Daten', g.get('solv'), g.get('arp'), f"{pr.get('grid','')} {pr.get('radius','')}", a.get('chatgpt'), a.get('gemini'), a.get('aimode'), a.get('gaio')]): ws4.write(j, i, x, N if j % 2 else Z)
ws5 = wb.add_worksheet('Aktionen'); ws5.hide_gridlines(2)
for i, (c, x) in enumerate(zip(['#', 'Feld', 'Aktion', 'Wer', 'Wirkung', 'Aufwand', 'Go nötig'], [5, 9, 90, 10, 9, 9, 10])): ws5.write(0, i, c, H); ws5.set_column(i, i, x)
for j, a in enumerate(ACT, 1):
    for i, x in enumerate([a['rank'], a['field_id'], a['action_de'], a['owner'], a['impact'], a['effort'], 'ja']): ws5.write(j, i, x, N if j % 2 else Z)
ws5.freeze_panes(1, 0); wb.close(); print('wrote', out)
