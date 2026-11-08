#!/usr/bin/env python3
"""Compare the Drive folder listing with the staged manifest.
Usage: check_drive.py <_drive/MANIFEST.json> <titles.txt>
titles.txt: one file title per line (copy from the Drive search results). Exit 1 when a file is missing."""
import sys, json
man = json.load(open(sys.argv[1])); man.pop('MANIFEST.json', None)
titles = {l.strip() for l in open(sys.argv[2],encoding='utf-8') if l.strip()}
miss = [n for n in man if n not in titles]; extra = [t for t in titles if t not in man]
print(f'{len(man)-len(miss)} of {len(man)} files present in Drive')
for m in miss: print('  MISSING in Drive:', m)
for e in extra: print('  extra in Drive (ok if older version or archive):', e)
sys.exit(1 if miss else 0)
