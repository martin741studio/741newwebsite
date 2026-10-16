#!/usr/bin/env python3
"""M11: every text node of the prototype must exist in approved-copy.md.
Usage: check_text.py <index.html> <approved-copy.md> [--allow "text part" ...]
Exit 1 when a segment differs and is not allowed. Typical allowed: the prototype notice in the footer."""
import re, sys, html
from html.parser import HTMLParser
args = sys.argv[1:]
allow = []
while '--allow' in args:
    i = args.index('--allow'); allow.append(args[i+1].lower()); del args[i:i+2]
page = open(args[0],encoding='utf-8').read()
copy = open(args[1],encoding='utf-8').read()
body = page[page.index('<body'):]
body = re.sub(r'<script.*?</script>','',body,flags=re.S)
body = re.sub(r'<svg.*?</svg>','',body,flags=re.S)
body = re.sub(r'<style.*?</style>','',body,flags=re.S)
class P(HTMLParser):
    def __init__(s): super().__init__(); s.t=[]
    def handle_data(s,d):
        d = re.sub(r'\s+',' ',html.unescape(d)).strip()
        if d: s.t.append(d)
p = P(); p.feed(body)
def norm(x):
    x = x.replace('„','').replace('“','').replace('"','').replace('**','').replace('★','')
    return re.sub(r'\s+',' ',x).strip().lower()
cn = norm(copy)
miss = [t for t in p.t if norm(t) not in cn and not any(a in t.lower() for a in allow)]
print(f'{len(p.t)} text segments, {len(miss)} not found verbatim in approved copy')
for m in miss: print('  DIFF:', m[:160])
sys.exit(1 if miss else 0)
