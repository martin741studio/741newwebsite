#!/usr/bin/env python3
"""Look up client-facing labels and find banned internal terms.

Usage:
  label_map.py show [--lang en|de]          # print the internal -> client-facing table
  label_map.py get <key> [--lang en|de]     # e.g. get yap-l3
  label_map.py scan <file>                  # list banned internal terms found (exit 1 if any)
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'assets', 'label-map.json')


def load():
    with open(DATA) as f:
        return json.load(f)


def scan(path):
    d = load()
    text = open(path, encoding='utf-8').read()
    low = text.lower()
    hits = []
    for term in d['banned']:
        for m in re.finditer(re.escape(term), low):
            line = low.count('\n', 0, m.start()) + 1
            hits.append((line, term.strip()))
    return hits


def main(argv):
    if not argv:
        sys.exit(__doc__)
    cmd = argv[0]
    lang = 'en'
    if '--lang' in argv:
        lang = argv[argv.index('--lang') + 1]
    d = load()
    if cmd == 'show':
        for k, v in d['labels'][lang].items():
            print(f'{k:14} -> {v}')
    elif cmd == 'get':
        print(d['labels'][lang][argv[1]])
    elif cmd == 'scan':
        hits = scan(argv[1])
        if not hits:
            print('OK no banned internal terms')
            return 0
        for line, term in sorted(set(hits)):
            print(f'BANNED line {line}: "{term}"')
        return 1
    else:
        sys.exit(__doc__)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
