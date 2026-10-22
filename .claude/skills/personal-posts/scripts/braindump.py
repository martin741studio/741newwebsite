#!/usr/bin/env python3
"""Braindump store for personal-posts: raw, unprocessed thoughts, kept exactly as
given, separate from the topic backlog (which holds short, ready-to-draft prompts).
Martin's own words, 2026-10-22: a place to dump raw thinking without it being
treated as post-ready. A dump is never drafted into a post directly -- it is
first distilled (editorial method, voice-profile.md) into an actual insight or
mechanism, confirmed with Martin, and only then does normal angle generation
(SKILL.md step 4) start.

Usage:
  braindump.py add <account> "<raw text>"      store a new raw dump
  braindump.py list [--account personal|business] [--status raw|distilled|archived]
  braindump.py mark <id> <status>               raw -> distilled -> archived
"""
import json, os, sys, datetime

ROOT = '/Users/martindrendel/741website'
PATH = os.path.join(ROOT, '00_project', 'assets', '741studio', 'personal-posts', 'braindump.json')


def load():
    if not os.path.exists(PATH):
        return {'dumps': []}
    with open(PATH) as f:
        return json.load(f)


def save(data):
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    with open(PATH, 'w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')


def cmd_add(account, text):
    if account not in ('personal', 'business'):
        sys.exit("account must be 'personal' or 'business'")
    data = load()
    next_id = max([d['id'] for d in data['dumps']], default=0) + 1
    data['dumps'].append({
        'id': next_id, 'account': account, 'text': text, 'status': 'raw',
        'added': datetime.date.today().isoformat(), 'distilled_idea_id': None,
    })
    save(data)
    print(f'saved dump {next_id} ({account}, {len(text)} chars)')


def cmd_list(account, status):
    data = load()
    rows = data['dumps']
    if account:
        rows = [d for d in rows if d['account'] == account]
    if status:
        rows = [d for d in rows if d['status'] == status]
    if not rows:
        print('no dumps match')
        return
    for d in rows:
        preview = d['text'][:80].replace('\n', ' ')
        print(f"[{d['id']}] ({d['account']}, {d['status']}, {d['added']}) {preview}...")


def cmd_mark(id_, status):
    if status not in ('raw', 'distilled', 'archived'):
        sys.exit("status must be raw, distilled, or archived")
    data = load()
    for d in data['dumps']:
        if d['id'] == id_:
            d['status'] = status
            save(data)
            print(f'dump {id_} -> {status}')
            return
    sys.exit(f'no dump with id {id_}')


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cmd, rest = args[0], args[1:]
    if cmd == 'add':
        if len(rest) < 2:
            sys.exit('usage: add <account> "<raw text>"')
        cmd_add(rest[0], rest[1])
    elif cmd == 'list':
        account = None
        status = None
        if '--account' in rest:
            account = rest[rest.index('--account') + 1]
        if '--status' in rest:
            status = rest[rest.index('--status') + 1]
        cmd_list(account, status)
    elif cmd == 'mark':
        cmd_mark(int(rest[0]), rest[1])
    else:
        sys.exit(__doc__)
