#!/usr/bin/env python3
"""Topic backlog for personal-posts: a flat idea list, not content-pool's scored
keyword pool. Martin's own dictated thought stays the primary input every run;
this only fills the gap when he has none ready (workflow-builds/personal-posts/
voice-profile.md, "Topic backlog" section, Martin's go 2026-10-22). Covers BOTH
accounts (--account personal|business, Martin's go 2026-10-22) in one file, each
idea tagged with its account and a pillar valid for that account.

Usage:
  topic_backlog.py init                                    create the file with its seed ideas
  topic_backlog.py list --account personal|business [--status open|used|skipped]
  topic_backlog.py add <lane> "<idea>" ["source"] --account personal|business
  topic_backlog.py use <id>                                 mark an idea used today
  topic_backlog.py skip <id>                                mark an idea skipped
"""
import json, os, sys, datetime

ROOT = '/Users/martindrendel/741website'
PATH = os.path.join(ROOT, '00_project', 'assets', '741studio', 'personal-posts', 'topic-backlog.json')
SEED_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets', 'topic-backlog-seed.json')

# Personal account: 7 content pillars (content intelligence brief, 2026-10-22) +
# client-result as a cross-cutting 8th bucket. Business account: 741 Studio's own
# pillars (voice-profile-business.md).
LANES = {
    'personal': (
        'uncomfortable-truths', 'human-behavior', 'entrepreneurship', 'freedom-culture',
        'tech-ai-marketing', 'health-performance', 'personal-stories', 'client-result',
    ),
    'business': (
        'educational', 'client-transformation', 'agency-ops', 'execution-reality',
        'measurable-results',
    ),
}


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


def cmd_list(account, status):
    data = load()
    rows = [i for i in data['ideas'] if i['status'] == status and i['account'] == account]
    if not rows:
        print(f'no {account} ideas with status={status}')
        return
    for i in rows:
        print(f"[{i['id']}] ({i['lane']}) {i['idea']}")


def cmd_add(account, lane, idea, source):
    if account not in LANES:
        sys.exit("account must be 'personal' or 'business'")
    if lane not in LANES[account]:
        sys.exit(f'lane for account={account} must be one of {LANES[account]}')
    data = load()
    next_id = max([i['id'] for i in data['ideas']], default=0) + 1
    data['ideas'].append({
        'id': next_id, 'account': account, 'lane': lane, 'idea': idea, 'source': source or 'chat',
        'status': 'open', 'added': datetime.date.today().isoformat(), 'used_date': None,
    })
    save(data)
    print(f'added idea {next_id} ({account})')


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
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cmd, rest = args[0], args[1:]
    account = None
    if '--account' in rest:
        i = rest.index('--account')
        account = rest[i + 1]
        del rest[i:i + 2]
    if cmd == 'init':
        cmd_init()
    elif cmd == 'list':
        if not account:
            sys.exit('list requires --account personal|business')
        status = 'open'
        if '--status' in rest:
            status = rest[rest.index('--status') + 1]
        cmd_list(account, status)
    elif cmd == 'add':
        if not account or len(rest) < 2:
            sys.exit('usage: add <lane> "<idea>" ["source"] --account personal|business')
        cmd_add(account, rest[0], rest[1], rest[2] if len(rest) > 2 else None)
    elif cmd == 'use':
        cmd_mark(int(rest[0]), 'used')
    elif cmd == 'skip':
        cmd_mark(int(rest[0]), 'skipped')
    else:
        sys.exit(__doc__)
