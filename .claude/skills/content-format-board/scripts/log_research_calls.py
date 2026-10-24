#!/usr/bin/env python3
"""Tally research calls per run (reported, not capped — Martin's decision 2026-10-24).

Usage:
  log_research_calls.py <out_dir> add <tool> "<query or url>" [hits]
  log_research_calls.py <out_dir> report

hits = number of results that are about the client's category AND area (relevant hits),
not the raw result count. 0 = searched, nothing relevant; omit = not counted.
"""
import json, os, sys, datetime


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    out_dir, cmd = argv[0], argv[1]
    os.makedirs(out_dir, exist_ok=True)
    p = os.path.join(out_dir, 'research-calls.jsonl')
    if cmd == 'add':
        tool, query = argv[2], argv[3]
        hits = int(argv[4]) if len(argv) > 4 else None
        with open(p, 'a') as f:
            f.write(json.dumps({'at': datetime.datetime.now().isoformat(timespec='seconds'),
                                'tool': tool, 'query': query, 'hits': hits}) + '\n')
        print(f'logged {tool}: {query[:60]}')
    elif cmd == 'report':
        rows = [json.loads(l) for l in open(p)] if os.path.exists(p) else []
        by = {}
        for r in rows:
            by[r['tool']] = by.get(r['tool'], 0) + 1
        print(f'{len(rows)} research calls this run')
        for k, v in sorted(by.items()):
            print(f'  {k}: {v}')
        zero = [r['query'] for r in rows if r.get('hits') == 0]
        if zero:
            print('  queries with 0 hits (say so in the board, never fill the gap):')
            for q in zero:
                print(f'    - {q}')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
