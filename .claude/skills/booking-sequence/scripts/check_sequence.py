#!/usr/bin/env python3
"""Booking sequence: hard-rule check + slop gate for the 3 WhatsApp messages. Writes the sequence file only on PASS.

Usage: check_sequence.py <slug> [--write]

Reads 00_project/prospects/<slug>/booking/: booking.json (with "times" from tz_times.py), claims.json and one
mX.txt per message whose times.mX.mode is "slot" or "now" (a "merged" message has no file; its content goes into
times.mX.merged_into). Timing (Martin 14.10.): m1 = 24 h before, m2 = 08:00 her time on the call day, m3 = 30 min before.
claims.json: {"claims": [{"text": "...", "numbers": ["2.900"], "source": "<path rel. to prospect dir or repo>",
              "derived": "<calc, only for numbers computed from other claims>", "quote": "<words that must be in the source>"}]}
Every claim needs "numbers", a "quote" or "absent". Facts without a number (a site change, a page feature) use "quote"
(must occur in the source, HTML entities decoded); "something is missing" facts use "absent" (must NOT occur in the source,
e.g. no URL with "wandelzeit" in the URL list).
Checks every message: greeting with the first name, "Martin" as the last line, du (no formal Sie/Ihnen/Ihr mid-sentence),
https links only, no booking link, no tool names, no "unclaimed", no process framing, no jargon (H1, SoLV, Schema, Canonical ...), no markdown, word limit,
every number backed by a claim (times and dates must match the booking), HWG words for health prospects,
then deslop_de.py --claims = 5/5. Content rules (checked in the message that carries the content):
m1 content = video link + search demand + example framing of the traffic number; m2 content = one case from
case-library.json; m3 = meeting link + Laptop/PC, not Handy, screen sharing, 30 min.
--write: on PASS writes 00_project/prospects/<slug>/whatsapp-sequence.md (with a wa.me link per message) and booking/_run.json.
Exit 0 = PASS, 1 = FAIL (fix the flagged message and run again).
"""
import datetime, html, json, os, re, subprocess, sys

ROOT = '/Users/martindrendel/741website'
DESLOP = os.path.join(ROOT, '00_project', 'content-writing-skill', 'scripts', 'deslop_de.py')
CASES = os.path.join(ROOT, '00_project', 'prospect-mini', 'case-library.json')
VIDEO = 'https://www.youtube.com/watch?v=dQ9OE8GSolw'
TOOLS = r'dataforseo|data for seo|local ?falcon|\bfalcon\b|brightlocal|\bmoz\b|ahrefs|semrush|sistrix|apify|supabase|serpapi|pagespeed|lighthouse|screaming ?frog|chatgpt|\bclaude\b|smartlead|zapmail|resend\b|\bloom\b'
UNCLAIMED = r'unclaimed|nicht beansprucht|unbeansprucht|nicht übernommen|herrenlos'
PROCESS = r'gehört bei uns zum|unser(em)? (standard|prozess)|im rahmen unseres|workflow'
BOOKING = r'cal\.com|calendly|cal\.eu|/30min|termin buchen unter'
PROMISE = r'garantier|verspreche|\bsicher(?!heit)\b|\bgarantiert|ganz bestimmt|auf jeden fall mehr'
HWG = r'heil(en|ung|t)\b|geheilt|beschwerdefrei|schmerzfrei|wirkt garantiert|erfolgsgarantie|patienten heilen|garantierte? (wirkung|besserung)|\bwunder'
FORMAL = r'(?<![.!?:\n]\s)(?<![.!?:\n])\b(Sie|Ihnen|Ihr|Ihre|Ihrem|Ihren|Ihrer|Ihres)\b'
JARGON = r'\bh1\b|\bsolv\b|\bnap\b|schema|canonical|\bserps?\b|meta.?(description|beschreibung)|title.?tag|\bcrawl|ranking.?faktor|\bctr\b|\bgbp\b|\bpool\b|sitemap'
LIMIT = {'m1': 150, 'm2': 130, 'm3': 80}
EXTRA = {'m1': 90, 'm2': 90}   # words added to the target's limit per merged message


def load(p, default=None):
    try: return json.load(open(p, encoding='utf-8'))
    except Exception: return default


def nums(t):
    t = re.sub(r'https?://\S+', ' ', t)
    t = re.sub(r'\b\d{1,2}:\d{2}\b', ' ', t)
    t = re.sub(r'\b\d{1,2}\.\d{1,2}\.(\d{2,4})?', ' ', t)
    return [n.rstrip('.,') for n in re.findall(r'\d+(?:[.,]\d+)*', t)]


def cn_ok(c): return bool(c.get('numbers') or c.get('quote') or c.get('absent'))


def plain(n): return n.replace('.', '').replace(',', '.')


def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    slug = sys.argv[1]; write = '--write' in sys.argv
    pdir = os.path.join(ROOT, '00_project', 'prospects', slug); bdir = os.path.join(pdir, 'booking')
    bk = load(os.path.join(bdir, 'booking.json'), {}); tm = bk.get('times') or {}
    errs, notes = [], []
    if not bk: sys.exit(f'FAIL: {bdir}/booking.json missing')
    if not tm: errs.append('booking.json has no "times": run tz_times.py --out booking.json')
    mode = {k: (tm.get(k) or {}).get('mode', 'slot') for k in ('m1', 'm2', 'm3')}
    target = {k: ((tm.get(k) or {}).get('merged_into') or k) for k in ('m1', 'm2', 'm3')}
    names = [k for k in ('m1', 'm2', 'm3') if mode[k] != 'merged']
    merged = any(mode[k] == 'merged' for k in mode)
    msgs = {}
    for n in names:
        p = os.path.join(bdir, n + '.txt')
        if not os.path.exists(p): errs.append(f'{n}.txt missing')
        else: msgs[n] = open(p, encoding='utf-8').read().strip()
    claims = (load(os.path.join(bdir, 'claims.json'), {}) or {}).get('claims', [])
    lib = load(CASES, {}); lib_txt = json.dumps(lib, ensure_ascii=False)
    case_names = [c['name'] for c in lib.get('cases', []) + lib.get('more', [])]
    ok_nums = set()
    for i, c in enumerate(claims):
        src = c.get('source', '')
        sp = next((p for p in (os.path.join(pdir, src), os.path.join(bdir, src), os.path.join(ROOT, src)) if src and os.path.exists(p)), None)
        if not sp: errs.append(f'claims[{i}] "{c.get("text", "")[:40]}": source file missing ({src!r})')
        q, ab = c.get('quote'), c.get('absent')
        body_l = html.unescape(open(sp, encoding='utf-8', errors='ignore').read()).lower() if sp else ''
        if sp and q and q.lower() not in body_l:
            errs.append(f'claims[{i}]: quote {q[:50]!r} not found in {src}')
        if sp and ab and ab.lower() in body_l:
            errs.append(f'claims[{i}]: "absent" {ab[:50]!r} IS in {src} (the claim says it is missing)')
        if not cn_ok(c): errs.append(f'claims[{i}]: needs "numbers", "quote" or "absent"')
        cn = [str(x) for x in c.get('numbers', [])]
        ok_nums.update(cn)
        if sp and not c.get('derived'):
            body = open(sp, encoding='utf-8', errors='ignore').read()
            for x in cn:
                if x not in body and plain(x) not in body and plain(x).rstrip('0').rstrip('.') not in body:
                    errs.append(f'claims[{i}]: number {x} not found in {src}')
    call = tm.get('call', {})
    for n, t in msgs.items():
        low = t.lower(); lines = [l for l in t.splitlines() if l.strip()]
        first = bk.get('first_name', '')
        if first and not re.match(rf'(hallo|hi|liebe[r]?|guten (morgen|tag))\s+{re.escape(first)}\b', t.strip(), re.I):
            errs.append(f'{n}: does not start with a greeting + "{first}"')
        if not lines or lines[-1].strip() != 'Martin': errs.append(f'{n}: last line must be "Martin"')
        for rx, what in ((BOOKING, 'booking link'), (TOOLS, 'tool name'), (UNCLAIMED, '"unclaimed" claim'), (PROCESS, 'process framing'), (PROMISE, 'promise word'), (JARGON, 'jargon (say it in plain words)')):
            for m in re.finditer(rx, low): errs.append(f'{n}: {what}: "{m.group(0)}"')
        if bk.get('health'):
            for m in re.finditer(HWG, low): errs.append(f'{n}: HWG word for a health prospect: "{m.group(0)}"')
        for m in re.finditer(FORMAL, t): errs.append(f'{n}: formal address "{m.group(0)}" (use du)')
        for u in re.findall(r'(?<![\w/])(?:www\.|http://)\S+', t): errs.append(f'{n}: link without https://: {u}')
        if re.search(r'\*\*|^#|^\s*[-*•]\s', t, re.M): errs.append(f'{n}: markdown or bullets (WhatsApp plain text only)')
        lim = LIMIT[n] + sum(EXTRA[k] for k in ('m1', 'm2') if k != n and target[k] == n)
        wc = len(re.sub(r'https?://\S+', '', t).split())
        if wc > lim: errs.append(f'{n}: {wc} words > {lim}')
        for x in nums(t):
            if x not in ok_nums and not (n == 'm3' and x == '30'): errs.append(f'{n}: number {x} has no claim in claims.json')
        for hh in re.findall(r'\b\d{1,2}:\d{2}\b', t):
            if hh != call.get('prospect_time'): errs.append(f'{n}: time {hh} != call time {call.get("prospect_time")} (prospect zone)')
        for d in re.findall(r'\b\d{1,2}\.\d{1,2}\.', t):
            if d != call.get('prospect_date'): errs.append(f'{n}: date {d} != call date {call.get("prospect_date")}')
        for wd in re.findall(r'\b(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag)\b', t):
            if wd != call.get('prospect_weekday'): errs.append(f'{n}: weekday {wd} != call weekday {call.get("prospect_weekday")}')
    m1, m3 = msgs.get(target['m1'], ''), msgs.get('m3', '')
    if m1:
        w = target['m1']
        if VIDEO not in m1: errs.append(f'{w}: video link {VIDEO} missing (m1 content)')
        if not re.search(r'%|prozent', m1, re.I): errs.append(f'{w}: no share example (e.g. "schon 5 Prozent dieser Suchen")')
        if not re.search(r'wären|zum beispiel|beispiel|etwa|rund', m1, re.I): errs.append(f'{w}: traffic number not framed as an example (wären / rund / zum Beispiel)')
        if not re.search(r'such', m1, re.I): errs.append(f'{w}: no search demand mentioned')
    for n, t in msgs.items():
        if call.get('prospect_time') and call['prospect_time'] not in t: errs.append(f'{n}: call time {call.get("prospect_time")} (her zone) missing')
    story = msgs.get(target['m2'], '')
    if story:
        hit = [c for c in case_names if re.search(r'\b' + re.escape(' '.join(c.split()[-2:])) + r'\b', story)]
        if not hit: errs.append(f"{target['m2']}: no success story with a name from case-library.json (m2 content)")
        else: notes.append('case: ' + ', '.join(hit))
    if m3:
        ml = bk.get('meet_link', '')
        if not ml or ml not in m3: errs.append(f'm3: meeting link {ml!r} missing')
        for w in ('Laptop', 'PC', 'Handy', 'Bildschirm'):
            if w.lower() not in m3.lower(): errs.append(f'm3: "{w}" missing (Laptop/PC, nicht am Handy, Bildschirm teilen)')
        if mode['m3'] == 'slot' and not re.search(r'30 Minuten|halben Stunde', m3): errs.append('m3: "30 Minuten" / "halben Stunde" missing (Martin 14.10.: 30 min before)')
    cp = os.path.join(bdir, 'claims.json')
    slop = {}
    for n, t in msgs.items():
        tmp = os.path.join(bdir, f'.{n}.slop.txt'); open(tmp, 'w', encoding='utf-8').write(t)
        r = subprocess.run([sys.executable, DESLOP, tmp, '--claims', cp, '--json'], capture_output=True, text=True)
        os.remove(tmp)
        try: d = json.loads(r.stdout); slop[n] = d['score']
        except Exception: slop[n] = 0; d = {'hits': {'error': [r.stderr[-200:]]}}
        if slop[n] != 5: errs.append(f'{n}: slop {slop[n]}/5: ' + '; '.join(f'{g}: {", ".join(map(str, h))[:120]}' for g, h in d.get('hits', {}).items() if h))
    print(f'check_sequence {slug}: ' + ' · '.join(f'{n} slop {s}/5' for n, s in sorted(slop.items()))
          + ''.join(f' · {k} merged into {target[k]}' for k in mode if mode[k] == 'merged')
          + ''.join(f' · {k} SEND NOW' for k in mode if mode[k] == 'now'))
    for x in notes: print('  note:', x)
    for x in tm.get('warnings', []): print('  warning:', x)
    if errs:
        for e in errs: print('  FAIL', e)
        print(f'RESULT: FAIL ({len(errs)})'); sys.exit(1)
    print('RESULT: PASS')
    if write: write_files(slug, pdir, bdir, bk, tm, msgs, merged, claims)


HEAD = {'m1': '## 1 · 24 h vorher', 'm2': '## 2 · Morgen des Termins', 'm3': '## 3 · 30 Minuten vorher'}


def wa_link(phone, text):
    from urllib.parse import quote
    return 'https://wa.me/' + ''.join(c for c in phone if c.isdigit()) + '?text=' + quote(text, safe='')


def write_files(slug, pdir, bdir, bk, tm, msgs, merged, claims):
    c = tm['call']
    led = os.path.join(bdir, 'cost_ledger.jsonl')
    usd = sum(json.loads(l).get('usd', 0) for l in open(led) if l.strip()) if os.path.exists(led) else 0
    srcs = sorted({x.get('source', '') for x in claims if x.get('source')})
    now = datetime.datetime.now().astimezone()
    out = [f"# WhatsApp sequence: {bk.get('name')} (call {c['wita']} = {c['prospect']} {c['prospect_zone_abbr']})", '',
           f"Booking: cal.com · {bk.get('meet_link', '')} · WhatsApp {bk.get('phone', '')} · review page {bk.get('review_url', '') or 'none'}"
           + (' · TROCKENLAUF (dry run, not a real booking)' if bk.get('mode') == 'Trockenlauf' else ''),
           f"Check: check_sequence.py PASS {now:%d.%m.%Y %H:%M} WITA, slop 5/5 each. Fresh-check cost {usd:.3f} USD. Evidence: {', '.join(srcs)}.",
           "Timing (Martin 14.10.): 1 = 24 h vorher · 2 = 8:00 Uhr ihrer Zeit am Termintag · 3 = 30 Minuten vorher. Claude sendet nichts.", '']
    notes = []
    for k in ('m1', 'm2', 'm3'):
        t = tm[k]
        if t['mode'] == 'merged':
            out += [f"{HEAD[k]}", f"entfällt ({t['reason']}; Inhalt steckt in Nachricht {t['merged_into'][1]})", '']
            continue
        when = f"{t['wita']} / {t['prospect_time']} Uhr {t['prospect_zone_abbr']}"
        if t['mode'] == 'now': when = f"JETZT SENDEN, Slot war {when}"
        out += [f"{HEAD[k]} ({when})", '```text', msgs[k], '```', f"WhatsApp-Link: {wa_link(bk.get('phone', ''), msgs[k])}", '']
        notes.append(f"m{k[1]} {'jetzt' if t['mode'] == 'now' else t['wita']}")
    open(os.path.join(pdir, 'whatsapp-sequence.md'), 'w', encoding='utf-8').write('\n'.join(out))
    run = {'client': bk.get('name'), 'workflow': 'booking-sequence', 'status': 'fertig, Freigabe offen',
           'mode': bk.get('mode', 'Echt'), 'last_run': now.date().isoformat(), 'local': f'00_project/prospects/{slug}/booking',
           'result': f'00_project/prospects/{slug}/whatsapp-sequence.md', 'drive': '',
           'note': f"Call {c['wita']} ({c['prospect']}); " + ', '.join(notes) + f"; Kosten {usd:.3f} USD"}
    if bk.get('mode') == 'Trockenlauf': run['status'] = 'Trockenlauf'
    json.dump(run, open(os.path.join(bdir, '_run.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote', os.path.relpath(os.path.join(pdir, 'whatsapp-sequence.md'), ROOT), 'and booking/_run.json')


if __name__ == '__main__':
    main()
