#!/usr/bin/env python3
"""Validate captions.md against the caption format and the dump (deterministic step 5).

Usage:
  validate_captions.py <captions.md> --dump <dump.md> [--max-words 12] [--max-lines 2]
                       [--max-chars 42] [--min-blocks 12] [--max-blocks 60]
Checks:
  numbering 1..n without gaps · block count in range · words per block · lines per block ·
  characters per line · no dashes (em, en, spaced hyphen) · no HTML · no German words ·
  every number in a caption is in the dump (dots and commas stripped; parts of a date count).
Prints one line per problem. Last line: PASS or FAIL (exit 0 / 1).
"""
import argparse, re, sys

GERMAN = {'und', 'nicht', 'ist', 'das', 'der', 'mit', 'für', 'fuer', 'auf', 'heute', 'morgen', 'uhr', 'wir',
          'haben', 'sind', 'auch', 'noch', 'schon', 'keine', 'kein', 'eine', 'einen', 'wenn', 'dann', 'aber',
          'oder', 'nach', 'vom', 'zum', 'zur', 'bei', 'über', 'ueber', 'unser', 'unsere', 'heute', 'abends'}
NUM = re.compile(r'\d[\d.,]*k?', re.I)
BLOCK = re.compile(r'^(\d+)\.\s+(.*\S)\s*$')


def norm(tok):
    return tok.lower().rstrip('.,').replace('.', '').replace(',', '')


def dump_numbers(text):
    s = set()
    for t in NUM.findall(text):
        s.add(norm(t))
        for part in re.split(r'[.,]', t.lower()):
            if part: s.add(part)
    return s


def parse(path):
    blocks, cur = [], None
    for raw in open(path, encoding='utf-8'):
        line = raw.rstrip('\n')
        if line.startswith('#'):
            continue
        m = BLOCK.match(line)
        if m:
            cur = {'n': int(m.group(1)), 'lines': [m.group(2).strip()]}
            blocks.append(cur); continue
        if not line.strip():
            cur = None; continue
        if cur is not None:
            cur['lines'].append(line.strip())
    return blocks


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('captions'); ap.add_argument('--dump', required=True)
    ap.add_argument('--max-words', type=int, default=12); ap.add_argument('--max-lines', type=int, default=2)
    ap.add_argument('--max-chars', type=int, default=42)
    ap.add_argument('--min-blocks', type=int, default=12); ap.add_argument('--max-blocks', type=int, default=60)
    a = ap.parse_args()
    dump = open(a.dump, encoding='utf-8').read()
    dnums = dump_numbers(dump)
    blocks = parse(a.captions)
    problems = []
    if not blocks:
        problems.append('no numbered blocks found (format: "1. text")')
    for i, b in enumerate(blocks, 1):
        if b['n'] != i:
            problems.append(f'block numbering: expected {i}, found {b["n"]}')
    n = len(blocks)
    if n and not (a.min_blocks <= n <= a.max_blocks):
        problems.append(f'block count {n} outside {a.min_blocks}..{a.max_blocks}')
    for b in blocks:
        text = ' '.join(b['lines'])
        tag = f'block {b["n"]}'
        words = len(text.split())
        if words > a.max_words:
            problems.append(f'{tag}: {words} words > {a.max_words}: "{text}"')
        if len(b['lines']) > a.max_lines:
            problems.append(f'{tag}: {len(b["lines"])} lines > {a.max_lines}')
        for ln in b['lines']:
            if len(ln) > a.max_chars:
                problems.append(f'{tag}: line {len(ln)} chars > {a.max_chars}: "{ln}"')
        if '—' in text or '–' in text or ' - ' in text:
            problems.append(f'{tag}: dash found: "{text}"')
        if re.search(r'<[a-zA-Z/!]', text):
            problems.append(f'{tag}: HTML tag found: "{text}"')
        for w in re.findall(r"[A-Za-zÄÖÜäöüß]+", text):
            if w.lower() in GERMAN:
                problems.append(f'{tag}: German word "{w}": "{text}"')
        for t in NUM.findall(text):
            if norm(t) not in dnums:
                problems.append(f'{tag}: number "{t}" is not in the dump: "{text}"')
    for p in problems:
        print('FAIL', p)
    print(f'{n} blocks checked')
    print('PASS' if not problems else f'FAIL ({len(problems)} problems)')
    sys.exit(0 if not problems else 1)


if __name__ == '__main__':
    main()
