#!/usr/bin/env python3
"""Verify the phase-2 visual folder before prompts are sent or the page is shown.

Usage: verify_visual.py <visual_dir> [--stage prompts|page] [--no-slop]

--stage prompts (before generation):
  1. brand.md exists with a logo file and a colour table
  2. refs.md exists; at least 3 reference screenshots per idea in refs/ (files named idea<N>-r<k>-...)
  3. prompts.md (or prompts-v3-concepts.md) contains the candid block and no editorial/cinematic wording
--stage page (default, before the page is shown):
  all of the above, plus
  4. images/concepts/ has at least 2 frames per idea (<N><letter>.png)
  5. visual.json has guide, bubbles, ideas with mechanism + proof per concept; open is empty unless --allow-open
  6. board.html exists; no banned internal term; slop lint 5/5 on its text
"""
import glob, html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = '/Users/martindrendel/741website'
BAD_STYLE = ['hyperrealistic photograph', 'editorial photo', 'full-frame camera', 'cinematic', 'color grading', 'colour grading']
CANDID = ['candid phone-video still', 'no editorial polish', 'slight motion blur']


def main(argv):
    vdir = argv[0]
    stage = argv[argv.index('--stage') + 1] if '--stage' in argv else 'page'
    msgs = []
    fail = lambda m: msgs.append('FAIL ' + m)

    bp = os.path.join(vdir, 'brand.md')
    if not os.path.exists(bp):
        fail('brand.md missing')
    else:
        b = open(bp, encoding='utf-8').read()
        if '## Logo' not in b or '## Colours' not in b or '#' not in b.split('## Colours', 1)[-1][:600]:
            fail('brand.md needs a Logo section and a Colours hex table')
        if not glob.glob(os.path.join(vdir, 'brand', 'logo*')):
            fail('no logo file in brand/')

    ideas = sorted({re.match(r'idea(\d)', os.path.basename(f)).group(1) for f in glob.glob(os.path.join(vdir, 'refs', 'idea*-r*')) if re.match(r'idea(\d)', os.path.basename(f))})
    if not os.path.exists(os.path.join(vdir, 'refs.md')):
        fail('refs.md missing — reference research is a gate before any prompt')
    if not ideas:
        fail('no reference screenshots in refs/ (idea<N>-r<k>-<account>-<likes>.jpg)')
    for n in ideas:
        k = len(glob.glob(os.path.join(vdir, 'refs', f'idea{n}-r*')))
        if k < 3:
            fail(f'idea {n}: {k} reference screenshots, need at least 3')

    pp = next((p for p in (os.path.join(vdir, 'prompts-v3-concepts.md'), os.path.join(vdir, 'prompts.md')) if os.path.exists(p)), None)
    if not pp:
        fail('no prompts file')
    else:
        t = open(pp, encoding='utf-8').read().lower()
        for s in BAD_STYLE:
            if s in t:
                fail(f'prompts use editorial wording: "{s}" (Martin: looks like AI / a fable book)')
        if not all(c in t for c in CANDID):
            fail('prompts lack the candid shared block (references/visual-phase.md §3)')

    if stage == 'page':
        for n in ideas:
            k = len(glob.glob(os.path.join(vdir, 'images', 'concepts', f'{n}*.png')))
            if k < 2:
                fail(f'idea {n}: {k} concept frames, need at least 2')
        vj = os.path.join(vdir, 'visual.json')
        if not os.path.exists(vj):
            fail('visual.json missing')
        else:
            d = json.load(open(vj, encoding='utf-8'))
            if d.get('guide') not in ('celine', 'martin'):
                fail('visual.json: guide must be celine or martin')
            if not d.get('bubbles'):
                fail('visual.json: bubbles missing (guide voice)')
            for idea in d.get('ideas', []):
                for c in idea.get('concepts', []):
                    if not c.get('mechanism') or not c.get('proof') or not c.get('ref'):
                        fail(f'idea {idea.get("n")} concept "{c.get("title")}": mechanism, proof and ref are all required')
            if d.get('open') and '--allow-open' not in argv:
                fail('visual.json: open questions on the client page (Martin: no summary block) — empty it or pass --allow-open')
        bh = os.path.join(vdir, 'board.html')
        if not os.path.exists(bh):
            fail('board.html missing (run build_visual_page.py)')
        else:
            r = subprocess.run([sys.executable, os.path.join(HERE, 'label_map.py'), 'scan', bh], capture_output=True, text=True)
            if r.returncode != 0:
                for line in r.stdout.strip().splitlines():
                    fail(line)
            if '--no-slop' not in argv:
                t = open(bh, encoding='utf-8').read()
                t = re.sub(r'<style.*?</style>|<script.*?</script>', '', t, flags=re.S)
                t = html.unescape(re.sub(r'<[^>]+>', '\n', t))
                txt = '\n'.join(l.strip() for l in t.splitlines() if l.strip())
                r = subprocess.run([sys.executable, os.path.join(ROOT, '.claude/skills/slopmonster/tools/deslop.py'), '--text', txt], capture_output=True, text=True)
                if '5/5' not in r.stdout:
                    fail('board page slop lint below 5/5:\n' + '\n'.join(r.stdout.strip().splitlines()[-5:]))
                else:
                    msgs.append('OK slop lint 5/5')

    for m in msgs:
        print(m)
    bad = [m for m in msgs if m.startswith('FAIL')]
    print(f'{"VISUAL PASSED" if not bad else "VISUAL BLOCKED"} · stage {stage} · ideas {",".join(ideas) or "-"} · {len(bad)} failures')
    return 1 if bad else 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
