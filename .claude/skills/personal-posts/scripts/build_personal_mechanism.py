#!/usr/bin/env python3
"""Build a "what people assume / what's actually true" mechanism-diagram image
for a personal-account post (Martin's go, 2026-10-22: richer visuals beyond the
single quote card, strongest fit for pillar-1 "uncomfortable truths" posts).
Same render pipeline as build_personal_image.py, no 741 branding, new template
(07_social/templates/personal_mechanism_diagram.html).

Usage:
  build_personal_mechanism.py "<what people assume>" "<what's actually true>" "<author>" <platform>

platform: instagram | facebook (both render 1080x1080; same image serves both)
Writes to 07_social/output/personal/<platform>_mechanism_<slug>.png and prints its path.
"""
import html, os, re, subprocess, sys, tempfile

ROOT = '/Users/martindrendel/741website'
TEMPLATE = os.path.join(ROOT, '07_social', 'templates', 'personal_mechanism_diagram.html')
OUT_DIR = os.path.join(ROOT, '07_social', 'output', 'personal')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:40]


def build(assumption, reality, author, platform):
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(TEMPLATE) as f:
        page = f.read()
    page = (page.replace('{{ASSUMPTION}}', html.escape(assumption))
                .replace('{{REALITY}}', html.escape(reality))
                .replace('{{AUTHOR}}', html.escape(author)))

    tmp_html = tempfile.NamedTemporaryFile(suffix='.html', delete=False, dir=OUT_DIR)
    tmp_html.write(page.encode('utf-8'))
    tmp_html.close()

    slug = slugify(reality.split('.')[0] or reality)
    out_png = os.path.join(OUT_DIR, f'{platform}_mechanism_{slug}.png')

    cmd = [
        CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
        '--force-device-scale-factor=1', '--window-size=1080,1080',
        '--virtual-time-budget=12000', f'--screenshot={out_png}',
        f'file://{tmp_html.name}',
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    os.unlink(tmp_html.name)
    return out_png


if __name__ == '__main__':
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    assumption, reality, author, platform = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    if platform not in ('instagram', 'facebook'):
        sys.exit('platform must be instagram or facebook')
    path = build(assumption, reality, author, platform)
    print(path)
