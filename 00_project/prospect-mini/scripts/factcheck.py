#!/usr/bin/env python3
"""Prospect mini workflow, step 9.3a: mechanical fact check before the fresh agent (proposal 29, 2026-10-12).

Usage: factcheck.py <slug|prospect_dir> [--json <prospect file>] [--out <md file>]
Checks prospect.json against the evidence, without judgement:
1. Every number must appear in an evidence or findings file. Forms are normalised (1.900 = 1900, 4,1 % = 4.08 rounded,
   0,70 = 0.7). Derived counts (evidence_lib.facts: 2/49, mean 266, distances) count as evidence.
2. Merged keyword variants: demand rows that are one Google variant, and numbers that equal their sum (110 + 110 = 220).
3. Count claims ("Drei der vier Praxen", "2 von 49", "21 / 39") are matched against the derived pairs.
   A claim whose total exists with another count is a MISMATCH.
4. Sentences with "alle", "nur", "die meisten", "immer", "überall" are listed for the fresh agent.
Writes evidence/factcheck-auto.md. Exit 1 when there is a WRONG or MISMATCH line. Read only otherwise. Standard library only.
"""
import datetime, glob, json, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_lib as L

WORDS = {'null': 0, 'kein': 0, 'keine': 0, 'ein': 1, 'eine': 1, 'einer': 1, 'einem': 1, 'zwei': 2, 'drei': 3, 'vier': 4, 'fünf': 5, 'sechs': 6,
         'sieben': 7, 'acht': 8, 'neun': 9, 'zehn': 10, 'elf': 11, 'zwölf': 12}
WRX = '|'.join(sorted(WORDS, key=len, reverse=True))
ABS = r'\b(alle|allen|aller|alles|nur|die meisten|den meisten|der meisten|immer|überall)\b'
SKIP_KEYS = {'sources', 'slug', 'website', 'href', 'photo', 'pos', 'loom_url', 'subject', 'icon', 'tone', 'status', 'type', 'me', 'bold',
             'featured', 'more', 'labels', 'prio', 'effort', 'step', 'mods', 'pose'}
ASSUME = {'calc.budget', 'calc.conv', 'calc.deal', 'calc.vol_min', 'calc.vol_max', 'calc.val_min', 'calc.val_max', 'step3.score_draft', 'system.step3.score_draft'}
CONST = {3, 5, 20, 22, 44, 12, 30}  # page rules: ersten drei / 5 Sekunden / ersten 20 / 22 Punkte / 44 / 12 Monate / 30 Minuten
NUMRX = r'(?<![\w.,])\d{1,3}(?:\.\d{3})+(?![\d,])|\d+(?:,\d+)?|\d+\.\d+'
DATERX = r'\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b'


def plain(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\b741(\.Studio)?\b', '741-Studio', s).replace('741-Studio', 'Studio')  # our brand, not a claim
    return re.sub(r'\s+', ' ', s.replace('&nbsp;', ' ')).strip()


def cands(tok):
    """All numeric readings of a token, with the decimals it shows."""
    out = []
    if re.fullmatch(r'\d{1,3}(?:\.\d{3})+', tok):
        out.append((int(tok.replace('.', '')), 0))
        if tok.count('.') == 1: out.append((float(tok), 3))
    elif ',' in tok: out.append((float(tok.replace(',', '.')), len(tok.split(',')[1])))
    elif '.' in tok: out.append((float(tok), len(tok.split('.')[1])))
    else: out.append((int(tok), 0))
    return out


class Hay:
    """Every number of every evidence file: exact values and rounded forms, each with its file names."""

    def __init__(self):
        self.exact, self.rnd, self.dates, self.pairs = {}, {}, {}, []

    def add(self, v, f):
        if isinstance(v, bool): return
        v = float(v)
        self.exact.setdefault(v, set()).add(f)
        if v != int(v):
            for d in (0, 1, 2): self.rnd.setdefault(round(v, d), set()).add(f)

    def text(self, s, f):
        for m in re.finditer(DATERX, s): self.dates.setdefault(f'{int(m[1]):02d}.{int(m[2]):02d}.{m[3]}', set()).add(f)
        for m in re.finditer(r'\b(\d{4})-(\d{2})-(\d{2})', s): self.dates.setdefault(f'{m[3]}.{m[2]}.{m[1]}', set()).add(f)
        for m in re.finditer(r'(\d+)\s*/\s*(\d+)', s): self.pairs.append((int(m[1]), int(m[2]), f))
        for tok in re.findall(NUMRX, re.sub(DATERX, ' ', s)):
            for v, _ in cands(tok): self.add(v, f)

    def walk(self, x, f):
        if isinstance(x, dict):
            for k, v in x.items():
                self.text(str(k), f); self.walk(v, f)
        elif isinstance(x, list):
            for v in x: self.walk(v, f)
        elif isinstance(x, (int, float)): self.add(x, f)
        elif isinstance(x, str): self.text(x, f)

    def find(self, v, dec):
        if float(v) in self.exact: return 'exact', sorted(self.exact[float(v)])
        if float(v) in self.rnd: return 'rounded', sorted(self.rnd[float(v)])
        return None, []


def haystack(pdir):
    H = Hay()
    files = [f for f in glob.glob(os.path.join(pdir, 'evidence', '*')) if os.path.basename(f) not in ('fact-check.md', 'factcheck-auto.md', 'draft-facts.json')]
    files += [os.path.join(pdir, n) for n in ('intake.md', 'intake.json', 'demand.md', 'site-findings.md', 'homepage.md', 'competitors.md', 'scan-search.md', 'cost_ledger.jsonl')]
    files += glob.glob(os.path.join(pdir, 'evidence', 'google-panel-*.md'))
    for f in sorted(set(files)):
        if not os.path.isfile(f) or not re.search(r'\.(json|jsonl|md|txt)$', f): continue
        rel = os.path.relpath(f, pdir)
        s = open(f, encoding='utf-8', errors='replace').read()
        if f.endswith('.json'):
            try: H.walk(json.loads(s), rel)
            except Exception: H.text(s, rel)
        else: H.text(s, rel)
        if 'falcon-report' in f:  # scan time in local German time
            fr = L.falcon(pdir) or {}
            try:
                from zoneinfo import ZoneInfo
                d = datetime.datetime.fromtimestamp(int(fr['timestamp']), ZoneInfo('Europe/Berlin'))
                H.dates.setdefault(d.strftime('%d.%m.%Y'), set()).add(rel + ' (timestamp)')
            except Exception:  # flat report: US Eastern date; the German date can be the next day
                m = re.match(r'(\d+)/(\d+)/(\d{4}) (\d+):\d+ (AM|PM)', fr.get('date') or '')
                if m:
                    d = datetime.date(int(m[3]), int(m[1]), int(m[2]))
                    H.dates.setdefault(d.strftime('%d.%m.%Y'), set()).add(rel + ' (date, US time)')
                    if m[5] == 'PM' and int(m[4]) % 12 >= 6: H.dates.setdefault((d + datetime.timedelta(days=1)).strftime('%d.%m.%Y'), set()).add(rel + ' (date + 6 h)')
    H.walk(json.load(open(os.path.join(L.MINI, 'case-library.json'), encoding='utf-8')), 'prospect-mini/case-library.json')
    F = L.facts(pdir)
    H.walk(F, 'derived (evidence_lib.facts)')

    def pairs(x, path):
        if isinstance(x, dict):
            for k, v in x.items(): pairs(v, f'{path}.{k}' if path else k)
        elif isinstance(x, str) and re.fullmatch(r'\d+/\d+', x):
            a, b = x.split('/'); H.pairs.append((int(a), int(b), 'derived ' + path))
    pairs(F, '')
    return H, F


def strings(x, path=''):
    """(path, text) for every string in prospect.json except technical keys."""
    if isinstance(x, dict):
        for k, v in x.items():
            if k in SKIP_KEYS: continue
            yield from strings(v, f'{path}.{k}' if path else k)
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from strings(v, f'{path}[{i}]')
    elif isinstance(x, (str, int, float)) and not isinstance(x, bool):
        yield path, x


def main():
    t0 = time.time()
    args = sys.argv[1:]
    jf = out = None
    if '--json' in args: i = args.index('--json'); jf = args[i + 1]; del args[i:i + 2]
    if '--out' in args: i = args.index('--out'); out = args[i + 1]; del args[i:i + 2]
    pdir = args[0] if os.path.isdir(args[0]) else os.path.join(L.ROOT, '00_project', 'prospects', args[0])
    p = json.load(open(jf or os.path.join(pdir, 'prospect.json'), encoding='utf-8'))
    H, F = haystack(pdir)
    rows, _ = L.volumes(pdir)
    real_vols = {r['search_volume'] for r in rows if r.get('search_volume') is not None}
    groups = [g for g in L.merged_groups(rows) if g['volume'] * len(g['keywords']) not in real_vols | CONST]
    nums, merged, fracs, absol = [], [], [], []

    for path, x in strings(p):
        if isinstance(x, (int, float)):
            if path in ASSUME or path.endswith('score_draft'): nums.append((path, str(x), 'ASSUMPTION', 'calc start value or target, label it on the page')); continue
            kind, fs = H.find(x, 0)
            nums.append((path, str(x), 'SUPPORTED' if kind else ('CONST' if x in CONST else 'NOT FOUND'), ', '.join(fs[:3])))
            for g in groups:
                if x == g['volume'] * len(g['keywords']) and len(g['keywords']) > 1:
                    merged.append(('WRONG', path, str(x), f'= {" + ".join(str(g["volume"]) for _ in g["keywords"])}: sum of one merged Google variant ({" = ".join(g["keywords"])}); use {g["volume"]}'))
            continue
        s = plain(x)
        if 'TODO' in s: continue
        for m in re.finditer(DATERX, s):
            d = f'{int(m[1]):02d}.{int(m[2]):02d}.{m[3]}'
            nums.append((path, m[0], 'SUPPORTED' if d in H.dates else 'NOT FOUND', ', '.join(sorted(H.dates.get(d, []))[:2])))
        s2 = re.sub(DATERX, ' ', s)
        # count claims: "2 von 49", "Drei der vier", "21 / 39"
        for m in re.finditer(r'\b(\d+|' + WRX + r')\s+(?:von|der|aus)\s+(?:den\s+|deinen\s+)?(\d+|' + WRX + r')\b(?!\s*(?:km|%|Jahre|Wörter|Minuten|Sekunden|€))|(\d+)\s*/\s*(\d+)', s2, re.I):
            a, b = (m[1], m[2]) if m[1] else (m[3], m[4])
            a, b = WORDS.get(a.lower(), a), WORDS.get(b.lower(), b)
            a, b = int(a), int(b)
            if a > b or b < 2: continue
            same = [(x_, y_, f) for x_, y_, f in H.pairs if y_ == b]
            hit = [f for x_, y_, f in same if x_ == a]
            if hit: fracs.append(('SUPPORTED', path, m[0], hit[0]))
            elif same:
                best = {}
                for x_, y_, f in same:  # one label per pair, the most specific one
                    best.setdefault(x_, set()).add(f)
                fracs.append(('MISMATCH', path, m[0], 'evidence has ' + '; '.join(f'{x_}/{b} (' + ', '.join(sorted(f, key=len)[-2:]) + ')' for x_, f in sorted(best.items()))))
            else: fracs.append(('NO PAIR', path, m[0], f'no derived count with total {b}: the agent checks it'))
        for tok in re.findall(NUMRX, s2):
            vs = cands(tok)
            v, dec = vs[0]
            kind, fs = None, []
            for v_, d_ in vs:
                kind, fs = H.find(v_, d_)
                if kind: v = v_; break
            verdict = 'SUPPORTED' if kind else ('CONST' if v in CONST else 'NOT FOUND')
            nums.append((path, tok, verdict + (' (rounded)' if kind == 'rounded' else ''), ', '.join(fs[:3])))
            for g in groups:
                if len(g['keywords']) > 1 and v == g['volume'] * len(g['keywords']):
                    merged.append(('WRONG', path, tok, f'= {" + ".join(str(g["volume"]) for _ in g["keywords"])}: sum of one merged Google variant ({" = ".join(g["keywords"])}); the real figure is {g["volume"]}'))
        for sent in re.split(r'(?<=[.!?:])\s+', s):
            if re.search(ABS, sent, re.I): absol.append((path, sent))
    dem = [d.get('keyword', '').lower() for d in ((p.get('system') or {}).get('step1') or {}).get('demand') or []]
    for g in L.merged_groups(rows):
        both = [k for k in g['keywords'] if k.lower() in dem]
        if len(both) > 1: merged.append(('WRONG', 'system.step1.demand', ' + '.join(both), f'one merged Google variant ({g["volume"]}) shown {len(both)} times; show it once'))
        txt = json.dumps(p, ensure_ascii=False).lower()
        if all(k.lower() in txt for k in g['keywords']) and len(both) < 2:
            merged.append(('NOTE', '(text)', ' + '.join(g['keywords']), f'both forms named: say that Google counts them together ({g["volume"]}), never add them up'))

    bad = [n for n in nums if n[2].startswith('NOT FOUND')] + [m for m in merged if m[0] == 'WRONG'] + [f for f in fracs if f[0] == 'MISMATCH']
    E = lambda s: str(s).replace('|', '\\|')
    md = [f'# Automatic fact check: {p.get("display_name", p.get("slug"))} ({datetime.date.today().isoformat()}, factcheck.py)', '',
          f'Input: `{os.path.relpath(jf, pdir) if jf else "prospect.json"}`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time {time.time() - t0:.1f} s.', '',
          f'- Numbers: {len(nums)} · supported {sum(1 for n in nums if n[2].startswith("SUPPORTED"))} · not found {sum(1 for n in nums if n[2].startswith("NOT FOUND"))} · rule constants {sum(1 for n in nums if n[2] == "CONST")} · assumptions {sum(1 for n in nums if n[2] == "ASSUMPTION")}',
          f'- Merged-variant errors: {sum(1 for m in merged if m[0] == "WRONG")} · count-claim mismatches: {sum(1 for f in fracs if f[0] == "MISMATCH")} · absolute words: {len(absol)}', '',
          '## Must fix (mechanical)', '']
    for m in merged:
        if m[0] == 'WRONG': md.append(f'- WRONG `{m[1]}`: „{m[2]}“ {m[3]}')
    for f in fracs:
        if f[0] == 'MISMATCH': md.append(f'- MISMATCH `{f[1]}`: „{f[2]}“: {f[3]}')
    if not any(m[0] == 'WRONG' for m in merged) and not any(f[0] == 'MISMATCH' for f in fracs): md.append('- none')
    md += ['', '## For the fresh agent: check only these claims', '', '| Field | Claim | Why listed |', '| --- | --- | --- |']
    for n in nums:
        if n[2].startswith('NOT FOUND'): md.append(f'| `{n[0]}` | {E(n[1])} | number not in any evidence file |')
    for f in fracs:
        if f[0] == 'NO PAIR': md.append(f'| `{f[1]}` | {E(f[2])} | count claim without a derived count |')
    for path, sent in absol: md.append(f'| `{path}` | {E(sent)} | absolute word ({", ".join(sorted(set(w.lower() for w in re.findall(ABS, sent, re.I))))}) |')
    for m in merged:
        if m[0] == 'NOTE': md.append(f'| {m[1]} | {E(m[2])} | {E(m[3])} |')
    md += ['', '## Count claims', '', '| Verdict | Field | Claim | Evidence |', '| --- | --- | --- | --- |']
    md += [f'| {f[0]} | `{f[1]}` | {E(f[2])} | {E(f[3])} |' for f in fracs]
    md += ['', '## All numbers', '', '| Verdict | Field | Value | Evidence file |', '| --- | --- | --- | --- |']
    md += [f'| {n[2]} | `{n[0]}` | {E(n[1])} | {E(n[3])} |' for n in nums]
    out = out or os.path.join(pdir, 'evidence', 'factcheck-auto.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    print(json.dumps({'out': out, 'numbers': len(nums), 'not_found': sum(1 for n in nums if n[2].startswith('NOT FOUND')),
                      'wrong': sum(1 for m in merged if m[0] == 'WRONG'), 'mismatch': sum(1 for f in fracs if f[0] == 'MISMATCH'),
                      'absolute': len(absol), 'secs': round(time.time() - t0, 2)}, ensure_ascii=False))
    sys.exit(1 if [m for m in merged if m[0] == 'WRONG'] or [f for f in fracs if f[0] == 'MISMATCH'] else 0)


if __name__ == '__main__':
    main()
