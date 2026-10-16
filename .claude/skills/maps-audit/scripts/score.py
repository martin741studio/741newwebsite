"""Derive B09.04 / B11.08 / B11.09, then score a run folder. Deterministic: same input, same output.
Usage: python3 score.py <run_dir>"""
import json, os, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__))
CAT = json.load(open(os.path.join(HERE, '..', 'catalog.json')))
VAL = {'green': 1.0, 'yellow': 0.5, 'red': 0.0}
LIFT_MIN, RHO_MIN, COVERAGE_MIN, STRONG_SOLV = 2.0, 0.30, 0.70, 40.0
def light(x): return 'green' if x >= 0.75 else ('yellow' if x >= 0.40 else 'red')
def load(run, name, default=None):
    p = os.path.join(run, name)
    return json.load(open(p)) if os.path.exists(p) else default
def fm(x): return f'{(x if abs(x) > 0.004 else 0.0):+.2f}'.replace('+0.00','0,00').replace('.', ',')
def run_time(run):
    return (load(run, 'run.json', {}) or {}).get('started_at', '2026-10-11T00:00:00+02:00')
def derive(run, F):
    """F = dict field_id -> finding. Mutates F. Returns realism per keyword + verdict."""
    kws = [k for k in load(run, 'keywords.json', []) if k.get('priority') == 1]
    drivers = load(run, os.path.join('evidence', 'drivers.json'), {})
    rows = []; own_cats = set()
    for k in kws:
        d = drivers.get(k.get('google_report_key'), {})
        if not d or 'category_groups' not in d:
            rows.append(dict(keyword=k['keyword'], result='unknown', reason='no driver data')); continue
        rho = d.get('spearman_reviews_vs_solv')
        own = [cl for cl in d.get('client', []) if not k.get('own_place_id') or cl.get('place_id') == k.get('own_place_id')] or d.get('client', [])
        cats = {c for cl in own for c in cl.get('cats', [])}; own_cats |= cats
        own_solv = max([cl.get('solv', 0) for cl in own] or [0])
        relevant = [x.lower() for x in (load(run, 'run.json', {}).get('params', {}).get('relevant_categories') or [])]
        allowed = lambda c: (not relevant) or any(x in c for x in relevant)   # only categories that fit the real service
        drv_raw = [c for c in d.get('driver_categories', []) if allowed(c)]
        have = lambda n: any(n in c for c in cats)
        miss_raw = [c for c in drv_raw if not have(c)]
        disp = lambda c: c[:1].upper() + c[1:]
        drv = [disp(c) for c in drv_raw]; missing = [disp(c) for c in miss_raw]
        rev_driver = rho is not None and rho >= RHO_MIN
        if own_solv >= STRONG_SOLV: res, why = 'strong', f"Profil führt bereits (Top-3-Fläche {own_solv:.0f} %). Ziel: halten."
        elif missing: res, why = 'realistic', f"Fehlende Treiber-Kategorie(n): {', '.join(missing)} (Aufwand S)"
        elif rev_driver:
            gap = k.get('review_gap'); vel = k.get('velocity', 4); months = gap / vel if gap is not None else None
            res = 'unknown' if months is None else ('realistic' if months <= 9 else ('slow' if months <= 18 else 'unrealistic'))
            why = f"Bewertungen sind Treiber (rho {rho}); Lücke {gap}, {months and round(months)} Monate"
        elif (d.get('name_keyword') or {}).get('lift') and d['name_keyword']['lift'] >= LIFT_MIN and (d['name_keyword'].get('share_top10') or 0) >= 0.3:
            res, why = 'unknown', f"Treiber im Markt ist der Profilname (Suchbegriff im Namen, {d['name_keyword']['share_top10']*100:.0f} % der Top-10, Lift {d['name_keyword']['lift']}). Das ist durch Google-Richtlinien nicht empfohlen (Keyword-Stuffing). Kein steuerbarer Treiber."
        else: res, why = 'unknown', 'Kein steuerbarer Treiber in den Daten gefunden. Weitere Daten nötig (nicht als unrealistisch werten).'
        rows.append(dict(keyword=k['keyword'], result=res, reason=why, rho_reviews=rho, driver_categories=drv, missing=missing,
                         lifts={disp(c): d['category_groups'][c]['lift'] for c in drv_raw}))
    def setf(fid, status, value, text, deps, action=None):
        f = F.get(fid)
        if f is None: return
        f.update(status=status, value=value, finding_de=text, confidence='derived', depends_on=deps, evidence_ids=(['ev_drivers'] if os.path.exists(os.path.join(run, 'evidence', 'drivers.json')) else []), source_tool='derived', source_ref='scripts/score.py (+ evidence/drivers.json if present)',
                 collected_at=run_time(run), action_de=action or f.get('action_de'), why_de=f.get('why_de') or ('Berechnet aus anderen Feldern.' if status == 'unknown' else None))
    n_real = sum(r['result'] in ('realistic', 'strong') for r in rows); n_unreal = sum(r['result'] == 'unrealistic' for r in rows); n_unk = sum(r['result'] == 'unknown' for r in rows)
    rhos0 = [r['rho_reviews'] for r in rows if r.get('rho_reviews') is not None]
    if not rows or all(r.get('reason') == 'no driver data' for r in rows): verdict, vtxt = 'Offen', 'Offen: Für die Prio-1-Begriffe gibt es keine Falcon-Messung. Der Fit-Check braucht mindestens einen Scan je Begriff (Go).'
    elif n_unk == len(rows): verdict, vtxt = 'Offen', ('Offen: In den Marktdaten zeigt sich für die Prio-1-Begriffe kein steuerbarer Treiber (Bewertungen rho ' + (f"{fm(min(rhos0))} bis {fm(max(rhos0))}" if rhos0 else 'n/a') + ', keine passende Kategorie; ein Suchbegriff im Profilnamen wäre ein Richtlinien-Risiko). Der Fit-Check bleibt offen. Die Hindernisse liegen eher im Profil und auf der Seite, nicht im Markt.')
    elif n_real * 2 >= len(rows): verdict = 'Ja'
    elif n_unreal == len(rows): verdict = 'Nein'
    else: verdict = 'Noch nicht'
    miss = sorted({m for r in rows for m in r.get('missing', [])})
    rhos = [r['rho_reviews'] for r in rows if r.get('rho_reviews') is not None]
    if verdict != 'Offen':
        vtxt = (f"{verdict}: Für {n_real} von {len(rows)} Prio-1-Begriffen ist Platz 1 nicht unrealistisch. "
                f"Das Profil führt {', '.join(sorted(c[:1].upper()+c[1:] for c in own_cats)) or 'keine Kategorie'}; die Top-10-Profile führen zusätzlich {', '.join(miss) or 'keine weiteren Treiber-Kategorien'}. Aufwand: klein (S). "
                f"Bewertungen erklären diesen Markt nicht (rho {fm(min(rhos)) if rhos else 'n/a'} bis {fm(max(rhos)) if rhos else 'n/a'}). Grenze: Die Daten zeigen einen Zusammenhang, keinen Beweis für die Ursache.")
    worst = {'realistic': 'green', 'slow': 'yellow', 'unrealistic': 'red', 'unknown': 'grey'}
    setf('B11.08', 'green' if verdict == 'Ja' else ('yellow' if verdict == 'Noch nicht' else ('red' if verdict == 'Nein' else 'unknown')), rows, vtxt, ['B11.09'])
    nmiss = len(miss)
    setf('B11.09', 'green' if rows and nmiss == 0 else ('yellow' if nmiss == 1 else 'red') if rows else 'unknown', dict(per_keyword=rows),
         f"Treiber im Markt: Kategorien {', '.join(sorted({c for r in rows for c in r.get('driver_categories', [])})) or 'keine'}; Bewertungen sind kein Treiber. Dem Profil fehlen {nmiss}.", [], action='Fehlende Treiber-Kategorien im Profil prüfen (siehe B10.01).')
    setf('B09.04', 'unknown' if verdict == 'Offen' else ('green' if verdict == 'Ja' else ('yellow' if verdict == 'Noch nicht' else 'red')), dict(verdict=verdict), vtxt, ['B11.08'])
    return rows, verdict, vtxt
def score(run):
    findings = load(run, 'findings.json')
    F = {f['field_id']: f for f in findings}
    rows, verdict, vtxt = derive(run, F)
    strategy = (load(run, 'run.json', {}).get('params', {}) or {}).get('strategy', 'maps')
    WEIGHTS = CAT.get('block_weights_by_strategy', {}).get(strategy, CAT['block_weights'])
    blocks = {}
    for b, name in CAT['blocks'].items():
        fs = [F[f['field_id']] for f in CAT['fields'] if f['block'] == b and f['field_id'] in F]
        crit = {f['field_id'] for f in CAT['fields'] if f['critical']}
        num = den = 0.0; counted = unknown = 0
        for f in fs:
            st = f['status']
            if st in VAL:
                w = 3 if f['field_id'] in crit else 1
                num += w * VAL[st]; den += w; counted += 1
            elif st == 'unknown': unknown += 1
        cov = counted / (counted + unknown) if counted + unknown else None
        sc = num / den if den else None
        weight = WEIGHTS.get(b, 0)
        if sc is None: lt = 'offen'
        elif cov is not None and cov < COVERAGE_MIN: lt = 'unvollständig'
        else: lt = light(sc)
        blocks[b] = dict(name=name, weight=weight, score=None if sc is None else round(sc * 100), coverage=None if cov is None else round(cov, 2), light=lt, counted=counted, unknown=unknown)
    scored = [(b, v) for b, v in blocks.items() if v['weight'] and v['light'] in ('green', 'yellow', 'red')]
    tw = sum(v['weight'] for b, v in scored)
    total = round(sum(v['weight'] * v['score'] for b, v in scored) / tw) if tw else None
    all_w = sum(v['weight'] for v in blocks.values() if v['weight'])
    cov_total = round(sum(v['weight'] * (v['coverage'] or 0) for v in blocks.values() if v['weight']) / all_w, 2)
    cap = None
    crit_red = [f['field_id'] for f in F.values() if f['field_id'].startswith('B13.') and f['status'] == 'red' and f['field_id'] in {x['field_id'] for x in CAT['fields'] if x['critical']}]
    if total is not None and crit_red and total > 50: cap = dict(applied=True, from_score=total, fields=crit_red); total = 50
    run_meta = load(run, 'run.json', {})
    run_meta.update(strategy=strategy, score_total=total, score_coverage=cov_total, blocks=blocks, verdict=verdict, verdict_reason=vtxt, realism=rows, cap=cap, catalog_version=CAT['catalog_version'])
    json.dump(run_meta, open(os.path.join(run, 'run.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(list(F.values()), open(os.path.join(run, 'findings.json'), 'w'), ensure_ascii=False, indent=1)
    return run_meta
if __name__ == '__main__':
    m = score(sys.argv[1])
    print('score', m['score_total'], 'coverage', m['score_coverage'], 'verdict', m['verdict'], 'cap', m['cap'])
    for b, v in m['blocks'].items(): print(b, v['name'][:34].ljust(34), v['light'].ljust(14), v['score'], v['coverage'], 'w', v['weight'])
