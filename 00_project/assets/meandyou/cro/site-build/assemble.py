"""Assemble all approved me&you CRO prototypes into one clickable local site.
Run: python3 assemble.py  ->  ../_site/ (serve with: python3 -m http.server 8819 --directory ../_site)
Pages are taken from their run folders. A page is included as soon as its 07-prototype/index.html exists.
Links to the v2 preview are rewritten to the local pages; pages that do not exist yet keep the preview link."""
import os, re, shutil

CRO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(CRO, '_site')
V2 = 'https://clients.741.studio/meandyou/v2/'

# local file name -> run folder (relative to cro/)
PAGES = {
    'index.html': '.',
    'seminare.html': 'seminare',
    'michael.html': 'michael',
    'rhetorik.html': 'rhetorik',
    'stimmen.html': 'stimmen',
    'faq.html': 'faq',
    'gespraech-buchen.html': 'termin',
    'lp-undersold.html': 'lp-undersold',
    'lp-replayers.html': 'lp-replayers/07-prototype/v2',  # community version (39 €), approved 12.10.
    'lp-overlooked.html': 'lp-overlooked',
    'impressum.html': 'impressum', 'datenschutz.html': 'datenschutz', 'agb.html': 'agb',
}
# 'optionen.html': 'optionen' was live 13.10. for a few hours. Pauspapier decided the same day: "Optionen ansehen" always leads to the booking page. Source kept in cro/optionen/.
# Round Table 12.10. + Pauspapier 13.10.: main button label "Gespräch buchen" -> "Optionen ansehen"; the target stays the booking page. Not on Replayers (community) and the booking page.
OPTIONS_BUTTON_SKIP = {'lp-replayers.html', 'gespraech-buchen.html', 'optionen.html'}
# v2 preview file -> local file
V2MAP = {'index.html': 'index.html', 'seminare.html': 'seminare.html', 'michael.html': 'michael.html', 'rhetorik.html': 'rhetorik.html',
         'stimmen.html': 'stimmen.html', 'faq.html': 'faq.html', 'termin.html': 'gespraech-buchen.html',
         'lp-undersold.html': 'lp-undersold.html', 'lp-replayers.html': 'lp-replayers.html', 'lp-overlooked.html': 'lp-overlooked.html'}


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    src_of = lambda d: os.path.join(CRO, d) if d.endswith('/v2') else os.path.join(CRO, d, '07-prototype')
    present = {f: d for f, d in PAGES.items() if os.path.isfile(os.path.join(src_of(d), 'index.html'))}
    for fname, folder in present.items():
        src = src_of(folder)
        slug = 'home' if folder == '.' else folder.split('/')[0]
        shutil.copytree(os.path.join(src, 'assets'), os.path.join(OUT, 'assets', slug))
        html = open(os.path.join(src, 'index.html'), encoding='utf-8').read()
        html = html.replace('src="assets/', f'src="assets/{slug}/').replace("url(assets/", f"url(assets/{slug}/")

        def rep(m):
            target = V2MAP.get(m.group(1))
            if target and target in present:
                return target
            return m.group(0)
        html = re.sub(r'https://clients\.741\.studio/meandyou/v2/([a-z\-]+\.html)', rep, html)
        # the Stimmen nav item points to the homepage section until a Stimmen page exists
        if 'stimmen.html' in present:
            html = html.replace('href="index.html#stimmen"', 'href="stimmen.html"')
            if fname == 'index.html':
                html = html.replace('<a href="#stimmen">Stimmen</a>', '<a href="stimmen.html">Stimmen</a>')
        if 'faq.html' in present and fname == 'index.html':
            html = html.replace('<a href="#faq">FAQ</a>', '<a href="faq.html">FAQ</a>')
        # Entity fix 19.10. (Martin): footer + schema used the old German GmbH; the Impressum names the Dubai FZCO. Use the FZCO everywhere.
        html = html.replace('<p class="addr">Institut Michael Ehlers GmbH<br>Landsknechtstraße 50<br>96103 Hallstadt</p>',
                             '<p class="addr">Me&You Communication FZCO<br>Dubai Silicon Oasis, DDP, Building A1<br>Dubai, VAE</p>')
        html = re.sub(r'"name":\s*"Institut Michael Ehlers GmbH"', '"name":"Me&You Communication FZCO"', html)
        html = html.replace('"address":{"@type":"PostalAddress","streetAddress":"Landsknechtstraße 50","postalCode":"96103","addressLocality":"Hallstadt","addressCountry":"DE"}',
                             '"address":{"@type":"PostalAddress","streetAddress":"Dubai Silicon Oasis, DDP, Building A1","addressLocality":"Dubai","addressCountry":"AE"}')
        for ext, local in (('https://www.meandyou.de/impressum', 'impressum.html'), ('https://www.meandyou.de/datenschutz', 'datenschutz.html'), ('https://www.meandyou.de/agb', 'agb.html')):
            if local in present:
                html = html.replace(f'href="{ext}"', f'href="{local}"')
        if fname not in OPTIONS_BUTTON_SKIP:
            # sections that explain the call itself (steps, costs) keep "Gespräch buchen"
            keep_call = {'ablauf', 'gespraech', 'kosten'} | ({'abschluss'} if fname == 'lp-undersold.html' else set())
            def swap(m):
                content = re.search(r'utm_content=([\w-]+)', m.group(2))
                if content and content.group(1) in keep_call:
                    return m.group(0)
                return f'<a {m.group(1)}href="gespraech-buchen.html?{m.group(2)}" data-event="booking_click">Optionen ansehen</a>'
            html = re.sub(r'<a ([^>]*)href="gespraech-buchen\.html\?([^"]*)">Gespräch buchen</a>', swap, html)
        html = html.replace('Prototyp · nicht live', 'Prototyp · nicht live · lokale Gesamtversion')
        open(os.path.join(OUT, fname), 'w', encoding='utf-8').write(html)
    missing = [f for f in PAGES if f not in present]
    open(os.path.join(OUT, 'README.txt'), 'w').write('me&you Gesamtversion (lokal)\nSeiten: ' + ', '.join(present) + '\nNoch nicht fertig (Links zeigen auf die v2-Vorschau): ' + (', '.join(missing) or 'keine') + '\n')
    print('pages:', list(present), '| missing:', missing)


if __name__ == '__main__':
    main()
