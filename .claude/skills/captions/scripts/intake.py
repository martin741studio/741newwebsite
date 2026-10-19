#!/usr/bin/env python3
"""Captions intake (deterministic step 1 and step 7 of the captions skill).

Usage:
  intake.py start --source <file|-> [--date YYYY-MM-DD] [--drive-url <url>] [--note "..."]
      Makes 00_project/assets/youtube-captions/<date>/, writes dump.md from the source text,
      keeps an older captions.md as captions-v<n>.md, writes _run.json (status "in Arbeit").
      Source "-" reads stdin (use a heredoc). Exits 2 when the dump is empty or too short.
  intake.py finish --date YYYY-MM-DD --result <drive link> [--note "..."]
      Sets _run.json status "fertig" and the result link.
  intake.py status [--date YYYY-MM-DD]
      Prints the run folder state.
Exit codes: 0 ok, 1 usage error, 2 empty dump.
"""
import argparse, datetime, json, os, shutil, sys

ROOT = '/Users/martindrendel/741website'
BASE = os.path.join(ROOT, '00_project', 'assets', 'youtube-captions')
DRIVE_FOLDER = 'https://drive.google.com/drive/folders/1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm'
MIN_CHARS = 40


def run_dir(date):
    return os.path.join(BASE, date)


def write_run(d, **kw):
    p = os.path.join(d, '_run.json')
    data = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    data.update(kw)
    tmp = p + '.tmp'
    json.dump(data, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    os.replace(tmp, p)
    return p


def cmd_start(a):
    date = a.date or datetime.date.today().isoformat()
    text = sys.stdin.read() if a.source == '-' else open(a.source, encoding='utf-8').read()
    text = text.strip()
    if len(text) < MIN_CHARS:
        print(f'EMPTY DUMP: {len(text)} characters, need at least {MIN_CHARS}. Stop and ask Martin for the dump.')
        sys.exit(2)
    d = run_dir(date)
    os.makedirs(d, exist_ok=True)
    cap = os.path.join(d, 'captions.md')
    if os.path.exists(cap):
        n = 1 + len([f for f in os.listdir(d) if f.startswith('captions-v')])
        shutil.move(cap, os.path.join(d, f'captions-v{n}.md'))
        print(f'kept old captions as captions-v{n}.md')
    src = a.drive_url or 'pasted text'
    with open(os.path.join(d, 'dump.md'), 'w', encoding='utf-8') as f:
        f.write(f'# Dump {date}\n\nSource: {src}\n\n{text}\n')
    p = write_run(d, client='Martin + Celine (daily video)', workflow='captions', status='in Arbeit',
                  mode='Echt', last_run=date, local=os.path.relpath(d, ROOT), result='',
                  note=a.note or f'dump {len(text)} chars, {text.count(chr(10)) + 1} lines', drive=DRIVE_FOLDER)
    print('RUN_DIR', os.path.relpath(d, ROOT))
    print('DUMP', os.path.relpath(os.path.join(d, 'dump.md'), ROOT))
    print('RUN_JSON', os.path.relpath(p, ROOT))


def cmd_finish(a):
    d = run_dir(a.date)
    if not os.path.exists(os.path.join(d, 'captions.md')):
        print('no captions.md in', d); sys.exit(1)
    p = write_run(d, status='fertig', result=a.result, last_run=a.date,
                  note=a.note or 'captions delivered, Drive copy made')
    print('RUN_JSON', os.path.relpath(p, ROOT), 'status fertig')


def cmd_status(a):
    date = a.date or datetime.date.today().isoformat()
    d = run_dir(date)
    if not os.path.exists(d):
        print('no run for', date); return
    print('RUN_DIR', os.path.relpath(d, ROOT))
    for f in sorted(os.listdir(d)):
        print(' ', f, os.path.getsize(os.path.join(d, f)), 'bytes')
    p = os.path.join(d, '_run.json')
    if os.path.exists(p):
        print(open(p, encoding='utf-8').read())


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=['start', 'finish', 'status'])
    ap.add_argument('--source'); ap.add_argument('--date'); ap.add_argument('--drive-url')
    ap.add_argument('--note'); ap.add_argument('--result')
    a = ap.parse_args()
    if a.cmd == 'start':
        if not a.source: ap.error('--source <file|-> is required'); 
        cmd_start(a)
    elif a.cmd == 'finish':
        if not (a.date and a.result): ap.error('--date and --result are required')
        cmd_finish(a)
    else:
        cmd_status(a)
