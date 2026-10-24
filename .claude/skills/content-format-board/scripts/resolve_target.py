#!/usr/bin/env python3
"""Resolve a client/prospect name to its folders. Deterministic step 1 of the skill.

Usage: resolve_target.py "<name or slug>"
Prints JSON: slug, kind (prospect|client|unknown), source_dir, existing_files, out_dir.
Exit 2 when nothing matches (the skill then asks Martin which folder, never guesses).
"""
import json, os, re, sys, datetime, unicodedata

ROOT = '/Users/martindrendel/741website'
PROSPECTS = os.path.join(ROOT, '00_project', 'prospects')
ASSETS = os.path.join(ROOT, '00_project', 'assets')
REUSE = ('intake.md', 'demand.md', 'competitors.md', 'prospect.json', 'intake.json',
         'voice.md', 'roadmap.json', 'client.md', 'baseline.md', 'claims.json')


def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return s


def candidates(slug, base):
    if not os.path.isdir(base):
        return []
    names = sorted(os.listdir(base))
    exact = [n for n in names if n == slug]
    if exact:
        return exact
    parts = [p for p in slug.split('-') if len(p) > 2]
    return [n for n in names if os.path.isdir(os.path.join(base, n)) and all(p in n for p in parts)]


def main(name):
    slug = slugify(name)
    kind, source_dir, match = 'unknown', None, None
    pros = candidates(slug, PROSPECTS)
    cli = candidates(slug, ASSETS)
    if cli:
        kind, match = 'client', cli
    elif pros:
        kind, match = 'prospect', pros
    if match and len(match) > 1:
        print(json.dumps({'slug': slug, 'kind': kind, 'ambiguous': match}, indent=2))
        return 2
    if match:
        slug = match[0]
        source_dir = os.path.join(PROSPECTS if kind == 'prospect' else ASSETS, slug)
    day = datetime.date.today().isoformat()
    out_dir = os.path.join(ASSETS, slug, 'content-format-board', day)
    existing = set()
    if source_dir:
        for f in os.listdir(source_dir):
            if f.endswith(('.md', '.json')) and os.path.isfile(os.path.join(source_dir, f)):
                existing.add(os.path.relpath(os.path.join(source_dir, f), ROOT))
        for root, _dirs, files in os.walk(source_dir):
            for f in files:
                if f in REUSE:
                    existing.add(os.path.relpath(os.path.join(root, f), ROOT))
    print(json.dumps({'slug': slug, 'kind': kind, 'source_dir': source_dir,
                      'existing_files': sorted(existing), 'out_dir': out_dir}, indent=2))
    return 0 if kind != 'unknown' else 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(' '.join(sys.argv[1:])))
