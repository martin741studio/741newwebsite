"""Lint every card (client-visible new text: prose + new variant values) with deslop_de.py. Needs 5/5 per card."""
import json, os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
cards = json.load(open(os.path.join(HERE, 'cards.json'), encoding='utf-8'))
bad = 0
for c in cards:
    parts = [c['title'], c['why'].replace('**', ''), c.get('lock_note') or '', c.get('note') or '', c.get('guide_text') or ''] + [v.get('label', '') for v in c['variants']] + [v['value'] for v in c['variants']]
    f = tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False, encoding='utf-8'); f.write('\n'.join(p for p in parts if p)); f.close()
    r = subprocess.run(['python3', '/Users/martindrendel/741website/00_project/content-writing-skill/scripts/deslop_de.py', f.name, '--claims', os.path.join(HERE, 'claims.json')], capture_output=True, text=True)
    m = re.search(r'score (\d)/5', r.stdout); sc = int(m.group(1)) if m else 0
    print(c['code'], f'{sc}/5', '' if sc == 5 else r.stdout.strip().replace('\n', ' | ')[:300]); bad += sc < 5; os.unlink(f.name)
sys.exit(1 if bad else 0)
