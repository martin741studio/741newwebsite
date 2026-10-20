import pathlib

ROOT = pathlib.Path('/Users/martindrendel/741website/04_site/de')
src = (ROOT / 'index.html').read_text(encoding='utf8')
here = pathlib.Path(__file__).parent
founder = (here / 'founder_block.html').read_text(encoding='utf8')
extras = (here / 'extras.html').read_text(encoding='utf8')

assert src.count('{{> outcome_de }}') == 1 and src.count('{{> consent }}') == 1
out = src.replace('<head>', '<head>\n<meta name="robots" content="noindex,nofollow">', 1)
out = out.replace('{{> outcome_de }}', '{{> outcome_de }}\n' + founder, 1)
out = out.replace('{{> consent }}', extras + '\n  {{> consent }}', 1)
(ROOT / 'vorschau-v2.html').write_text(out, encoding='utf8')
print('written', len(out))
