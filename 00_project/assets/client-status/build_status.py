"""Shared builder for the 741 client status page (one page per client, same look as the Bali Healing roadmap status).
Usage from a per-client script:  from build_status import render; render(cfg, out_html)
cfg keys: lang, title, brand_sub, meta_lines, h1 (plain, em word), lead, theme (accent, accent_fg, ground, ...),
          back_url, status_h (heading of the big box), status_badge, status_lead, sections (list), sources (text).
A section is a dict:  {'kind':'kpis','items':[{cls,l,n,d}]} | {'kind':'table','h':..,'head':[..],'rows':[[..]]} |
                      {'kind':'para','h':..,'text':..} | {'kind':'mg','pose':'hello|point','text':..,'flip':bool}
Cells may contain HTML. Status chips: chip('done'|'progress'|'pending'|'ready', 'Text').
The Martin guide may appear max 2 times per page (rule 13.10.2026). Output is made self-contained with martin-guide/inline.py."""
import os, re, subprocess, html as _h

GUIDE = '/Users/martindrendel/741website/00_project/assets/brand/martin-guide'
esc = lambda s: _h.escape(str(s), quote=False)

def chip(cls, txt):
    return f'<span class="status {cls}" style="margin-left:0">{txt}</span>'

THEME_DEFAULT = dict(ground='#fbf8fd', panel='#ffffff', ink='#262230', ink_soft='#5d5868', grey='#8b8696', line='#ece6f2', line2='#e0d8ea',
                     accent='#783ca0', accent_fg='#ffffff', accent_ink='#5b2d80', accent_soft='rgba(120,60,160,.10)')

CSS = """
:root{--ground:%(ground)s;--panel:%(panel)s;--ink:%(ink)s;--ink-soft:%(ink_soft)s;--grey:%(grey)s;--line:%(line)s;--line-2:%(line2)s;
  --accent:%(accent)s;--accent-fg:%(accent_fg)s;--accent-ink:%(accent_ink)s;--accent-soft:%(accent_soft)s;
  --keep:#2e9e5b;--keep-bg:#e7f5ec;--keep-ln:#bfe4cc;--rev:#b9791b;--rev-bg:#fdf3d7;--rev-ln:#efdca6;
  --dead:#c0392b;--dead-bg:#fdecea;--dead-ln:#f3c9c3;--pend:#8b8696;--pend-bg:#f3f0f7;--pend-ln:#d9d2e3}
:root:not([data-theme="light"]){@media (prefers-color-scheme:dark){--ground:#1b1722;--panel:#241f2d;--ink:#f2eef7;--ink-soft:#c5bdd1;--grey:#968da5;--line:#352e41;--line-2:#40384e;
  --accent:#b27ad6;--accent-fg:#1b1722;--accent-ink:#d9b8ef;--accent-soft:rgba(178,122,214,.16);--keep:#5cc98a;--keep-bg:#182a20;--keep-ln:#2b4a37;--rev:#e0a63a;--rev-bg:#2c2413;--rev-ln:#4a3d1c;--pend:#968da5;--pend-bg:#2a2433;--pend-ln:#40384e}}
*{margin:0;padding:0;box-sizing:border-box}html{-webkit-text-size-adjust:100%%}
body{background:var(--ground);color:var(--ink);font-family:"DM Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;line-height:1.5;-webkit-font-smoothing:antialiased}
.wrap{max-width:1140px;margin:0 auto;padding:38px 24px 90px}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;flex-wrap:wrap;border-bottom:2px solid var(--line);padding-bottom:22px;margin-bottom:26px}
.brand .sub{font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--grey)}
.top .meta{text-align:right;font-size:12.5px;color:var(--grey);line-height:1.7}
h1{font-family:"Anton",sans-serif;font-weight:400;font-size:clamp(30px,4.6vw,50px);line-height:.98;letter-spacing:.3px;text-wrap:balance;margin:8px 0 6px}
h1 em{font-style:normal;color:var(--accent)}
.lead{font-size:15.5px;color:var(--ink-soft);max-width:72ch;margin-bottom:26px}.lead b{color:var(--ink)}
.backlink{display:inline-block;margin:0 0 14px;font-size:12.5px;font-weight:800;text-decoration:none;color:var(--accent-ink);background:var(--accent-soft);padding:7px 13px;border-radius:20px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-bottom:14px}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px 18px;position:relative;overflow:hidden}
.kpi::before{content:"";position:absolute;left:0;top:0;bottom:0;width:5px;background:var(--kc,var(--accent))}
.kpi.k-keep{--kc:var(--keep)}.kpi.k-rev{--kc:var(--rev)}.kpi.k-new{--kc:var(--accent)}.kpi.k-pend{--kc:var(--pend)}.kpi.k-dead{--kc:var(--dead)}
.kpi .n{font-family:"Anton",sans-serif;font-size:34px;line-height:1;letter-spacing:.5px;font-variant-numeric:tabular-nums;margin:2px 0 4px}
.kpi .l{font-size:11.5px;font-weight:700;text-transform:uppercase;letter-spacing:.6px;color:var(--grey)}
.kpi .d{font-size:12.5px;color:var(--ink-soft);margin-top:3px}
.status{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.4px;padding:3px 9px;border-radius:20px;white-space:nowrap;display:inline-block}
.status.ready,.status.done{color:var(--keep);background:var(--keep-bg);border:1px solid var(--keep-ln)}
.status.pending{color:var(--pend);background:var(--pend-bg);border:1px solid var(--pend-ln)}
.status.progress{color:var(--rev);background:var(--rev-bg);border:1px solid var(--rev-ln)}
.mtable{width:100%%;border-collapse:collapse;margin-top:10px;font-size:12.5px}
.mtable th{text-align:left;font-size:10px;text-transform:uppercase;letter-spacing:.4px;color:var(--grey);padding:6px 10px;border-bottom:2px solid var(--line)}
.mtable td{padding:8px 10px;border-bottom:1px solid var(--line);color:var(--ink-soft);vertical-align:top}
.mtable td:first-child{color:var(--ink);font-weight:700}.mtable tr:last-child td{border-bottom:none}
.bigsect{background:var(--panel);border:2px solid var(--accent);border-radius:20px;padding:24px 26px 28px;margin:30px 0}
.bigsect-h{font-family:"Anton",sans-serif;font-weight:400;font-size:26px;letter-spacing:.3px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.bigsect-h .badge2{font-family:"DM Sans",sans-serif;font-size:11px;font-weight:800;letter-spacing:.4px;text-transform:uppercase;color:var(--accent-fg);background:var(--accent);padding:3px 10px;border-radius:20px}
.bigsect-lead{font-size:13.5px;color:var(--ink-soft);max-width:82ch;margin:8px 0 20px}
.subh{font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.5px;color:var(--grey);margin:22px 0 4px;padding-top:16px;border-top:1px solid var(--line)}
.subh:first-of-type{border-top:none;padding-top:0;margin-top:0}
.para{font-size:13.5px;color:var(--ink-soft);max-width:82ch;margin-top:6px}
.srcnote{font-size:12.5px;color:var(--grey);margin-top:14px}
@media (max-width:640px){.mtable,.mtable tbody{display:block}.mtable tr:first-child{display:none}.mtable tr{display:block;padding:10px 0;border-bottom:1px solid var(--line)}.mtable tr:last-child{border-bottom:none}
  .mtable td{display:block;border:0;padding:3px 0}.mtable td:first-child{padding-top:0;font-size:13.5px}.mtable td:not(:first-child)::before{content:attr(data-l);display:block;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.4px;color:var(--grey);margin-top:4px}}
@media (max-width:760px){.bigsect{padding:18px 14px 22px}}
@media (max-width:520px){.top{align-items:flex-start}.top .meta{text-align:left}.wrap{padding:24px 16px 70px}}
"""

def _kpis(s):
    return '<div class="kpis">' + ''.join(
        f'<div class="kpi {k.get("cls","k-new")}"><div class="l">{k["l"]}</div><div class="n">{k["n"]}</div><div class="d">{k["d"]}</div></div>' for k in s['items']) + '</div>'

def _table(s):
    head = ''.join(f'<th>{h}</th>' for h in s['head'])
    rows = ''.join('<tr>' + ''.join(f'<td data-l="{esc(s["head"][i])}">{c}</td>' for i, c in enumerate(r)) + '</tr>' for r in s['rows'])
    return f'<div class="subh">{s["h"]}</div><table class="mtable"><tr>{head}</tr>{rows}</table>'

def render(cfg, out_html):
    here = os.path.dirname(os.path.abspath(out_html))
    th = dict(THEME_DEFAULT); th.update(cfg.get('theme', {}))
    body = []
    mg_count = 0
    for s in cfg['sections']:
        k = s['kind']
        if k == 'kpis': body.append(_kpis(s))
        elif k == 'table': body.append(_table(s))
        elif k == 'para': body.append(f'<div class="subh">{s["h"]}</div><p class="para">{s["text"]}</p>')
        elif k == 'mg':
            mg_count += 1
            body.append(f'<aside class="mg mg--right{" mg--flip" if s.get("flip") else ""}" data-reveal style="margin-top:18px"><img class="mg__img" src="poses/martin-{s["pose"]}.webp" alt="Martin von 741" width="112"><div class="mg__bubble"><span class="mg__name">Martin</span><p>{s["text"]}</p></div></aside>')
    assert mg_count <= 2, 'Martin guide: max 2 callouts per page'
    meta = '<br>'.join(cfg['meta_lines'])
    page = f"""<!doctype html><html lang="{cfg.get('lang','de')}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{esc(cfg['title'])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700;9..40,800&display=swap">
<style>{CSS % th}</style><link rel="stylesheet" href="/review-assets/martin-guide/martin-guide.css"></head><body>
<div class="wrap">
  <a class="backlink" href="https://clients.741.studio/" target="_top">{cfg.get('back_label','← Zurück zum Dashboard')}</a>
  <header class="top"><div class="brand"><span class="sub">{cfg['brand_sub']}</span></div><div class="meta">{meta}</div></header>
  <h1>{cfg['h1']}</h1>
  <p class="lead">{cfg['lead']}</p>
  <div class="bigsect" id="status">
    <div class="bigsect-h">{cfg['status_h']} <span class="badge2">{cfg['status_badge']}</span></div>
    <p class="bigsect-lead">{cfg['status_lead']}</p>
    {''.join(body)}
    <p class="srcnote">{cfg['sources']}</p>
  </div>
</div>
<script src="/review-assets/martin-guide/martin-guide.js" defer></script></body></html>"""
    tmp = os.path.join(here, '_src.html'); open(tmp, 'w', encoding='utf-8').write(page)
    subprocess.run(['python3', os.path.join(GUIDE, 'inline.py'), tmp, out_html], check=True); os.remove(tmp)
    # no vendor names in client view
    visible = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', open(out_html, encoding='utf-8').read(), flags=re.S)
    for bad in ['BrightLocal', 'Local Falcon', 'LocalFalcon', 'DataForSEO', 'Moz', 'Supabase', 'Apify', 'Resend', 'Ahrefs', 'Wix-Editor', 'Dinakar', 'Tantri', 'Gayo', 'Bondan']:
        assert bad not in visible, f'vendor/team name in client page: {bad}'
    return out_html
