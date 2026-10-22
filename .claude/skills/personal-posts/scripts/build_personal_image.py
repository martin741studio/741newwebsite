#!/usr/bin/env python3
"""Build the Instagram/Facebook image for a personal post: reuses the existing
07_social headless-Chrome render pipeline (social-visuals-workflow), with the
NEW minimal, non-741-branded template `07_social/templates/personal_post_quote.html`
(Martin's go, 2026-10-22: personal posts carry no 741 branding).

Usage:
  build_personal_image.py "<pull-quote text>" "<author, e.g. Martin Drendel>" <platform>

platform: instagram | facebook (both render 1080x1080; same image serves both)
Writes to 07_social/output/personal/<platform>_<slug>.png and prints its path.
"""
import html, os, re, subprocess, sys, tempfile, time

ROOT = '/Users/martindrendel/741website'
TEMPLATE = os.path.join(ROOT, '07_social', 'templates', 'personal_post_quote.html')
OUT_DIR = os.path.join(ROOT, '07_social', 'output', 'personal')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:40]


def build(quote, author, platform):
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(TEMPLATE) as f:
        page = f.read()
    page = page.replace('{{QUOTE}}', html.escape(quote)).replace('{{AUTHOR}}', html.escape(author))

    tmp_html = tempfile.NamedTemporaryFile(suffix='.html', delete=False, dir=OUT_DIR)
    tmp_html.write(page.encode('utf-8'))
    tmp_html.close()

    slug = slugify(quote.split('.')[0] or quote)
    out_png = os.path.join(OUT_DIR, f'{platform}_{slug}.png')

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
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    quote, author, platform = sys.argv[1], sys.argv[2], sys.argv[3]
    if platform not in ('instagram', 'facebook'):
        sys.exit('platform must be instagram or facebook')
    path = build(quote, author, platform)
    print(path)
