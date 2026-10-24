#!/usr/bin/env python3
"""Read the named 741 infrastructure/campaign memory files and report their
real state as a fact lookup, not a judgment call (Step 2.5, degrees of
freedom: this is the deterministic half of the grill's "read phase").

Never trust a prior AskUserQuestion round's memory of these facts -- always
re-run this before Round 1, so a stale fact (like a team member who no
longer exists) cannot leak into a card. See the 2026-10-25 hand-run.

Usage:
  check_infra_state.py                 # the default 741-marketing set
  check_infra_state.py <name> [<name> ...]   # a custom set of memory names

Each memory file is reported as:
  LIVE      - no red flags found in a quick scan of the text
  FLAGGED   - a line containing a known red-flag phrase was found (shown)
  NOT FOUND - no memory file with this name exists

This is a crude text scan, not a verified status. It exists to surface the
file's own red flags for a human to read, never to assert a definitive
"working" / "broken" verdict on its own.
"""
import os
import re
import sys

MEMORY_DIR = os.path.expanduser(
    '~/.claude/projects/-Users-martindrendel-741website/memory')

DEFAULT_SET = [
    'coldemail-sending-infra',
    'smartlead-cold-email',
    'hubspot-leads-segmentation',
    'leadgen-funnel-infra',
    'stipendium-giveaway-page',
    'marketing-quarter-campaign',
    'revenue-model-100k',
    'team-roster',
    '741-youtube-channel-avatar',
]

RED_FLAGS = [
    r'RETIRED', r'EXPIRED', r'PAUSED', r'STOPPED', r'CLOSED', r'blocked',
    r'NOT yet', r'not yet deployed', r'ENTWURF', r'TODO', r'offen',
    r'Abmahnung', r'not deployed', r'stalled', r'on paper',
]
RED_FLAG_RE = re.compile('|'.join(RED_FLAGS))


def scan_one(name):
    path = os.path.join(MEMORY_DIR, f'{name}.md')
    if not os.path.exists(path):
        return name, 'NOT FOUND', []
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
    hits = [ln.strip() for ln in lines if RED_FLAG_RE.search(ln)]
    status = 'FLAGGED' if hits else 'LIVE'
    return name, status, hits[:3]


def main(argv):
    names = argv if argv else DEFAULT_SET
    print(f'Infra-state scan of {len(names)} memory file(s)'
          f' (source: {MEMORY_DIR}):\n')
    for name in names:
        name, status, hits = scan_one(name)
        print(f'{status:10s} {name}')
        for h in hits:
            print(f'           > {h[:160]}')
    print('\nThis is a text scan for red-flag phrases only. Read the full'
          ' file before stating a state as fact in a card.')


if __name__ == '__main__':
    main(sys.argv[1:])
