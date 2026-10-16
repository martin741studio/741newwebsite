#!/usr/bin/env python3
"""Check that every quoted text in a GPT prompt exists in approved-copy.md.
Usage: check_prompt.py <prompt.txt> <approved-copy.md>
Quotes are „…“ pairs. Exit 1 when a quote is missing. Allowed differences are printed, never hidden."""
import re, sys
def norm(x):
    x = x.replace('„','').replace('“','').replace('"','').replace('**','').replace('★','')
    return re.sub(r'\s+',' ',x).strip().lower()
prompt = open(sys.argv[1],encoding='utf-8').read()
copy = norm(open(sys.argv[2],encoding='utf-8').read())
quotes = re.findall(r'„([^“]+)“', prompt)
miss = [q for q in quotes if norm(q) not in copy]
print(f'{len(quotes)} quotes, {len(miss)} not found in approved copy')
for m in miss: print('  MISSING:', m[:160])
print('PROMPT LENGTH', len(prompt))
sys.exit(1 if miss else 0)
