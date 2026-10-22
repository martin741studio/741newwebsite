#!/usr/bin/env python3
"""Topic backlog for personal-posts: a flat idea list, not content-pool's scored
keyword pool. Martin's own dictated thought stays the primary input every run;
this only fills the gap when he has none ready (workflow-builds/personal-posts/
voice-profile.md, "Topic backlog" section, Martin's go 2026-10-22).

Usage:
  topic_backlog.py init                           create the file with its seed ideas
  topic_backlog.py list [--status open|used|skipped]   list ideas (default: open)
  topic_backlog.py add <lane> "<idea>" ["source"]  add a new idea
  topic_backlog.py use <id>                        mark an idea used today
  topic_backlog.py skip <id>                       mark an idea skipped
"""
import json, os, sys, datetime

ROOT = '/Users/martindrendel/741website'
PATH = os.path.join(ROOT, '00_project', 'assets', '741studio', 'personal-posts', 'topic-backlog.json')
SEED_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets', 'topic-backlog-seed.json')
LANES = ('agency-insight', 'seo-opinion', 'client-result', 'mindset')


def load():
    if not os.path.exists(PATH):
        return {'ideas': []}
    with open(PATH) as f:
        return json.load(f)


def save(data):
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    with open(PATH, 'w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')


def cmd_init():
    if os.path.exists(PATH):
        print(f'already exists: {PATH}')
        return
    with open(SEED_PATH) as f:
        seed = json.load(f)
    save(seed)
    print(f'created {PATH} with {len(seed["ideas"])} seed ideas')


def cmd_list(status):
    data = load()
    rows = [i for i in data['ideas'] if i['status'] == status]
    if not rows:
        print(f'no ideas with status={status}')
        return
    for i in rows:
        print(f"[{i['id']}] ({i['lane']}) {i['idea']}")


def cmd_add(lane, idea, source):
    if lane not in LANES:
        sys.exit(f'lane must be one of {LANES}')
    data = load()
    next_id = max([i['id'] for i in data['ideas']], default=0) + 1
    data['ideas'].append({
        'id': next_id, 'lane': lane, 'idea': idea, 'source': source or 'chat',
        'status': 'open', 'added': datetime.date.today().isoformat(), 'used_date': None,
    })
    save(data)
    print(f'added idea {next_id}')


def cmd_mark(id_, status):
    data = load()
    for i in data['ideas']:
        if i['id'] == id_:
            i['status'] = status
            if status == 'used':
                i['used_date'] = datetime.date.today().isoformat()
            save(data)
            print(f'idea {id_} -> {status}')
            return
    sys.exit(f'no idea with id {id_}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, rest = sys.argv[1], sys.argv[2:]
    if cmd == 'init':
        cmd_init()
    elif cmd == 'list':
        status = 'open'
        if '--status' in rest:
            status = rest[rest.index('--status') + 1]
        cmd_list(status)
    elif cmd == 'add':
        if len(rest) < 2:
            sys.exit('usage: add <lane> "<idea>" ["source"]')
        cmd_add(rest[0], rest[1], rest[2] if len(rest) > 2 else None)
    elif cmd == 'use':
        cmd_mark(int(rest[0]), 'used')
    elif cmd == 'skip':
        cmd_mark(int(rest[0]), 'skipped')
    else:
        sys.exit(__doc__)
