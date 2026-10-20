#!/usr/bin/env python3
"""Prospect mini workflow, step 7: check the built page before anybody sees it.

Usage: validate.py <prospect_dir>
Fails (exit 1) on: jargon in visible text, missing local images, text from another prospect,
empty sections, missing sources block. Warns on: "Sie" in the reader text (house form is "du").
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
JARGON = ['Pool', 'H1', 'SoLV', 'Schema', 'Sitemap', 'Citation', 'Backlink', 'NAP', 'Canonical', 'E-E-A-T', 'Local Pack',
          'Lawyer', 'attorney', 'Physical therapist', 'Counselor', 'CRO', 'Un-Burning', 'Falcon', 'DataForSEO', 'SERP', 'Keyword', 'Book a call']
FOREIGN = ['Stürzl', 'STÜRZL', 'Steuerstraf', 'Kanzlei', 'Mandant']


def main():
    pdir = sys.argv[1]
    p = json.load(open(os.path.join(pdir, sys.argv[2] if len(sys.argv) > 2 else 'prospect.json'), encoding='utf-8'))
    page = os.path.join(ROOT, '04_site', 'review', p['slug'], 'index.html')
    s = open(page, encoding='utf-8').read()
    body = s[s.index('<body'):]
    vis = re.sub(r'<style.*?</style>|<script.*?</script>|<svg.*?</svg>|<!--.*?-->', ' ', body, flags=re.S)
    vis = re.sub(r'<[^>]+>', ' ', vis)
    vis = re.sub(r'\{\{>[^}]*\}\}', ' ', vis)
    errs, warns = [], []
    for w in JARGON:
        if re.search(r'(?<![\w-])' + re.escape(w) + r'(?![\w-])', vis):
            errs.append(f'jargon: {w}')
    own = (p.get('company', '') + ' ' + p.get('display_name', '')).lower()
    for w in FOREIGN:
        if w in vis and w.lower() not in own:
            errs.append(f'foreign text: {w}')
    for src in set(re.findall(r'(?:src=|url\()"?(/review-assets/[^")\s]+)', s)):
        if not os.path.exists(os.path.join(ROOT, '04_site', 'public', src.lstrip('/'))):
            errs.append(f'missing image: {src}')
    if 'SLOT:' in s or '%%' in s.replace('%%"', ''):
        errs.append('unfilled slot or placeholder')
    if not p.get('sources'):
        errs.append('no sources block in prospect.json')
    sie = len(re.findall(r'\b(Sie|Ihre|Ihren|Ihrer)\b', vis))
    if sie:
        warns.append(f'"Sie"-forms in visible text: {sie} (header/footer partials are excluded; check draft quotes)')
    if not p.get('loom_url'):
        warns.append('no loom_url: hero shows the video placeholder')
    print(json.dumps({'page': page, 'errors': errs, 'warnings': warns}, ensure_ascii=False, indent=1))
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main()
