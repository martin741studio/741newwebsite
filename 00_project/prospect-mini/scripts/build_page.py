#!/usr/bin/env python3
"""Prospect mini workflow, step 8: render the review page from prospect.json + template.html.

Usage: build_page.py <prospect_dir>
Writes 04_site/review/<slug>/index.html. Never edit that file by hand: change prospect.json and run again.
All text comes from prospect.json. This file only knows the layout.
"""
import html, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
MINI = os.path.join(ROOT, '00_project', 'prospect-mini')
CAL = 'https://cal.com/741-studio-simjzw/30min'
E = html.escape


def t(x):
    """Text that may contain simple inline HTML (<b>, <br>) written by us in prospect.json."""
    return x or ''


def H(p, key, default):
    """Optional headline override from prospect.json "headlines" (used for headline tests)."""
    return (p.get('headlines') or {}).get(key) or default


# ---------------------------------------------------------------- Martin guide
POSE_ALT = {'hello': 'winkt', 'point': 'zeigt auf das Ergebnis', 'think': 'denkt nach', 'insight': 'hat eine Idee', 'celebrate': 'freut sich', 'present': 'stellt vor'}


def guide(p, key, mods=''):
    """One callout per placement. Text in prospect.json guide.<key> (str or {text, pose, mods}). Missing key = no callout."""
    g = (p.get('guide') or {}).get(key)
    if not g:
        return ''
    if isinstance(g, str):
        g = {'text': g}
    pose = g.get('pose', key)
    mods = (mods + ' ' + g.get('mods', '')).strip()
    paras = ''.join(f'<p>{t(x)}</p>' for x in (g['text'] if isinstance(g['text'], list) else [g['text']]))
    return (f'<aside class="mg {mods}" data-reveal><img class="mg__img" src="/review-assets/martin-guide/martin-{pose}.webp" '
            f'alt="Martin von 741 {POSE_ALT.get(pose, "")}" width="112" loading="lazy"><div class="mg__bubble"><span class="mg__name">Martin</span>{paras}</div></aside>')


# ---------------------------------------------------------------- hero
def hero(p):
    h = p['hero']
    if p.get('hide_video') or p.get('no_video'):
        return f'''<section class="section-hero-audit">
    <div class="rvw-hero-single" style="max-width:860px; margin:0 auto; text-align:center;">
      <div class="audit-eyebrow">🔒 PRIVATE WEBSITE- &amp; SICHTBARKEITS-ANALYSE</div>
      <h1 class="audit-headline" style="margin:20px auto 16px;">{H(p, "hero_h1", f'Hallo {E(p["first_name"])},<br>hier ist deine persönliche Analyse deiner <span style="color:var(--brand--lemon);">{E(h.get("accent", "Online-Sichtbarkeit"))}</span>.')}</h1>
      <p class="audit-subheadline" style="max-width:760px; margin:0 auto 28px; text-align:center;">{t(H(p, "hero_sub", h["sub"]))}</p>
      <div class="rvw-hero-actions" style="display:flex; flex-direction:column; align-items:center; gap:12px;">
        <div class="hero-cta-group" style="display:flex; gap:16px; flex-wrap:wrap; justify-content:center;">
          <a href="{CAL}" target="_blank" rel="noopener" class="btn-741-main">Live-Diagnose im gebuchten Termin →</a>
        </div>
        <p class="rvw-cta-note">Persönliche Diagnose: Wir gehen alle Hebel und Quellcode-Punkte im Call gemeinsam durch.</p>
        {guide(p, 'hello', 'mg--small')}
      </div>
    </div>
  </section>
  <script>
  (function(){{
    function fit(){{
      var b=0; document.querySelectorAll('body *').forEach(function(e){{
        var cs=getComputedStyle(e); if((cs.position==='fixed'||cs.position==='sticky')&&e.offsetHeight>0&&e.offsetHeight<window.innerHeight*0.5){{var r=e.getBoundingClientRect(); if(r.top<200&&r.bottom<320&&r.bottom>b) b=r.bottom;}}
      }});
      if(b) document.documentElement.style.setProperty('--rvw-hdr', Math.round(b)+'px');
    }}
    window.addEventListener('load',fit); window.addEventListener('resize',fit); setTimeout(fit,600);
  }})();
  </script>
'''
    if p.get('loom_url'):
        video = (f'<div class="rvw-vcard"><div class="video-responsive"><iframe id="loomIframe" src="{E(p["loom_url"])}" allowfullscreen></iframe></div>'
                 f'<div class="rvw-vbar"><span class="rvw-vpill">🎯 Persönlich aufgenommen für: <strong>{E(p["display_name"])}</strong></span></div></div>')
    else:
        video = ('<div class="rvw-vcard" style="padding:0;"><div style="aspect-ratio:16/9;border-radius:14px;background:#f7f6f2;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center;padding:24px;">'
                 '<div style="width:56px;height:56px;border-radius:50%;background:var(--brand--lemon);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:22px;">▶</div>'
                 '<p style="margin:0;color:#555;font-size:14.5px;">Dein persönliches Video folgt in Kürze – die Analyse unten steht schon komplett.</p></div></div>'
                 '<!-- TODO: loom_url in prospect.json setzen, dann neu bauen -->')
    return f'''<section class="section-hero-audit">
    <div class="rvw-hero-grid">
      <div class="rvw-hero-head">
        <div class="audit-eyebrow">🔒 PRIVATE WEBSITE- &amp; SICHTBARKEITS-ANALYSE</div>
        <h1 class="audit-headline">{H(p, "hero_h1", f'Hallo {E(p["first_name"])},<br>ich habe eine persönliche Analyse deiner <span style="color:var(--brand--lemon);">{E(h.get("accent", "Online-Sichtbarkeit"))}</span> erstellt.')}</h1>
        <p class="audit-subheadline">{t(H(p, "hero_sub", h["sub"]))}</p>
      </div>
      <div class="rvw-hero-video">{video}</div>
      <div class="rvw-hero-actions">
        <div class="hero-cta-group" style="display:flex; gap:16px; flex-wrap:wrap;">
          <a href="{CAL}" target="_blank" rel="noopener" class="btn-741-main">Zeig mir meinen Markt →</a>
        </div>
        <p class="rvw-cta-note">30 Minuten, kostenlos: Ich zeige dir live, wer in deinem Markt oben steht – und warum.</p>
        {guide(p, 'hello', 'mg--small')}
      </div>
    </div>
  </section>
  <script>
  (function(){{
    function fit(){{
      var b=0; document.querySelectorAll('body *').forEach(function(e){{
        var cs=getComputedStyle(e); if((cs.position==='fixed'||cs.position==='sticky')&&e.offsetHeight>0&&e.offsetHeight<window.innerHeight*0.5){{var r=e.getBoundingClientRect(); if(r.top<200&&r.bottom<320&&r.bottom>b) b=r.bottom;}}
      }});
      if(b) document.documentElement.style.setProperty('--rvw-hdr', Math.round(b)+'px');
    }}
    window.addEventListener('load',fit); window.addEventListener('resize',fit); setTimeout(fit,600);
  }})();
  </script>

'''


def facts(p):
    """The 4 fact cards (formerly in the hero), now at the bottom before the final CTA."""
    h = p['hero']
    tone = {'red': 'background:rgba(239,68,68,0.12); color:#b91c1c;', 'amber': 'background:rgba(250,193,24,0.2); color:#b48500;', 'green': 'background:rgba(16,185,129,0.12); color:#047857;'}
    cards = ''
    for c in h['cards']:
        inner = (f'<div class="hero-card-icon">{c["icon"]}</div><div class="hero-card-title">{E(c["title"])}</div>'
                 f'<div class="hero-card-sub">{t(c["sub"])}</div><div class="hero-card-badge" style="{tone[c.get("tone", "amber")]}">{t(c["badge"])}</div>')
        cards += (f'<a class="hero-card-item" href="{E(c["href"])}" target="_blank" rel="noopener" style="text-decoration:none; color:inherit; display:block;">{inner}</a>'
                  if c.get('href') else f'<div class="hero-card-item">{inner}</div>')
    return f'''<section class="rvw-facts" id="ausgangslage">
    <h2>Deine Ausgangslage auf einen Blick</h2>
    <div class="hero-cards-grid">{cards}</div>
  </section>
'''


# ---------------------------------------------------------------- grid
def target_svg(n):
    step = 620 / n
    c = (n - 1) / 2
    col = {1: '#136c2e', 2: '#2e8b34', 3: '#4d9a3f', 4: '#7aa83f'}
    out = []
    for y in range(n):
        for x in range(n):
            d = max(abs(x - c), abs(y - c)) / max(c, 1)
            rank = 1 if d == 0 else (1 if d <= 0.34 else 2 if d <= 0.67 else 3)
            if abs(x - c) == c and abs(y - c) == c: rank = 4
            cx, cy = 40 + step / 2 + x * step, 40 + step / 2 + y * step
            r = step * 0.33
            stroke = ' stroke="#fac118" stroke-width="5"' if x == c and y == c else ''
            out.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="{col[rank]}"{stroke}/><text x="{cx:.0f}" y="{cy + 7:.0f}" fill="#fff">{rank}</text>')
    return ('<svg viewBox="0 0 700 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ziel-Szenario: unter den ersten drei im ganzen Einzugsgebiet (Simulation)">'
            '<rect width="700" height="700" fill="#eef4ee"/><g font-family="Arial, sans-serif" font-weight="bold" font-size="20" text-anchor="middle">'
            + ''.join(out) + '</g><text x="350" y="690" font-family="Arial" font-size="16" fill="#4d6b4d" text-anchor="middle">Ziel-Szenario (Simulation)</text></svg>')


def grid(p):
    g = p['grid']
    chips = ''.join(f'<span class="maps-vs-chip">{t(c)}</span>' for c in g['chips'])
    return f'''<!-- 741 Maps-Scan Beweis START -->
  <section class="maps-vs-section" id="maps-scan">
    <span style="color:var(--brand--lemon); font-weight:800; text-transform:uppercase; font-size:12.8px; letter-spacing:0.1em;">Google-Karte · Sichtbarkeits-Check</span>
    <h2 style="font-size:35.2px; font-weight:800; margin-top:8px;">{t(H(p, "grid_h2", g["h2"]))}</h2>
    <p style="color:#666; max-width:700px; margin:10px auto 0;">{t(g["intro"])}</p>
    <div class="maps-vs-grid">
      <div class="maps-vs-card">
        <span class="maps-vs-badge" style="background:rgba(239,68,68,0.12); color:#dc2626;">● Heute – echte Messung</span>
        <img src="/review-assets/{p.get("assets_slug", p["slug"])}/scan-grid.webp" alt="{E(g["alt"])}" loading="lazy" width="1000" height="1000">
        <p class="maps-vs-caption">{t(g["caption_today"])}</p>
      </div>
      <div class="maps-vs-card">
        <span class="maps-vs-badge" style="background:rgba(34,150,60,0.12); color:#15803d;">● Das Ziel – so kann es aussehen</span>
        {target_svg(int(g.get("grid_size", 7)))}
        <p class="maps-vs-caption">{t(g["caption_goal"])}</p>
      </div>
    </div>
    <div style="max-width:1060px;margin:0 auto;text-align:left;">{guide(p, 'point')}</div>
    <div class="maps-vs-impact">{chips}</div>
    <p style="color:#888; font-size:13px; max-width:640px; margin:18px auto 0;">Wer in der Google-Karte unter den ersten drei steht, bekommt den Großteil aller Klicks, Anrufe und Routen.</p>
  </section>
<!-- 741 Maps-Scan Beweis END -->
''' + proof(p)


# ---------------------------------------------------------------- system (3 steps)
def bar(label, val, mx, cls, shown):
    w = max(2.0, val / mx * 100) if mx else 2.0
    return f'<div class="sys-bar"><span>{E(label)}</span><div class="sys-bar-track"><div class="sys-bar-fill {cls}" style="width:{w:.1f}%"></div></div><b>{E(shown)}</b></div>'


def de(n):
    return f'{n:,}'.replace(',', '.')


def system(p):
    s = p['system']
    st = s['steps']
    steps = ''.join(f'<a class="sys-step" href="#{a}"><div class="sys-step-num">Schritt {i + 1}</div><h3>{E(x["title"])}</h3><p>{t(x["text"])}</p><span class="sys-step-kpi">{t(x["kpi"])}</span></a>'
                    for i, (a, x) in enumerate(zip(['content-pool', 'telefon-klingeln', 'startseite'], st)))
    d1 = s['step1']
    dem = [x for x in d1['demand'] if x.get('volume')]
    mx = max([x['volume'] for x in dem] or [1])
    bars = ''.join(bar(x['keyword'], x['volume'], mx, 'hire' if x['type'] == 'provider' else '', de(x['volume'])) for x in dem)
    nodata = ''
    if d1.get('no_data'):
        nodata = '<p class="sys-note" style="margin-top:8px;"><b>Ohne Zahl bei Google:</b> ' + ', '.join('„' + E(k) + '“' for k in d1['no_data']) + '. Google gibt für viele Begriffe keine Suchzahlen heraus – das heißt nicht, dass niemand sucht.</p>'
    dp = d1['depth']
    big = ''.join(f'<div><div class="n" style="color:{"#dc2626" if b["tone"] == "bad" else "#136c2e" if b["tone"] == "good" else "#252525"};">{E(b["n"])}</div><div class="l">{t(b["label"])}</div></div>' for b in dp['big'])
    mxb = max([b['val'] for b in dp.get('bars', [])] or [1])
    dbars = ''.join(bar(b['label'], b['val'], mxb, {'bad': 'bad', 'good': 'hire'}.get(b['tone'], ''), de(b['val'])) for b in dp.get('bars', []))
    items = ''.join(f'<div class="sys-item"><div class="sys-rank">{i + 1}</div><div><strong>{E(x["title"])}</strong><span><span class="sys-tag">{E(x["tag"])}</span>{t(x["why"])}</span></div></div>' for i, x in enumerate(d1['items'][:6]))

    d2 = s['step2']
    ME = ' class="me"'
    rows = ''.join(f'<tr{ME if r.get("me") else ""}><td>{E(r["name"])}</td><td><span class="cat">{E(r["cats"])}</span></td><td>{E(str(r["reviews"]))}</td><td>{"<b>" if r.get("bold") else ""}{E(r["share"])}{"</b>" if r.get("bold") else ""}</td></tr>' for r in d2['table'])
    checks = ''.join(f'<div class="sys-check"><h4>{E(c["title"])}</h4><p>{t(c["text"])}</p></div>' for c in d2['changes'])
    stats = ''.join(f'<div class="sys-stat"><div class="n">{E(x["n"])}</div><p>{t(x["text"])}</p></div>' for x in d2['cleanup'])
    good2 = f'<div class="sys-good">✓ <b>Die gute Nachricht:</b> {t(d2["good"])}</div>' if d2.get('good') else ''

    d3 = s['step3']
    five = ''.join(f'<div><b>{E(q["q"])}</b>{t(q["a"])}</div>' for q in d3['five'])

    def shot(lbl, color, bg, img, alt, score, pct, cls, note):
        return (f'<div class="sys-card"><span class="sys-badge" style="background:{bg}; color:{color};">● {lbl}</span>'
                f'<img class="sys-shot" src="{img}" alt="{E(alt)}" loading="lazy" width="1200" height="750" tabindex="0"><span class="sys-zoom-hint">🔍 Zum Vergrößern antippen</span>'
                f'<div class="sys-score"><b style="min-width:86px;white-space:nowrap;">{score}</b><div class="sys-bar-track"><div class="sys-bar-fill {cls}" style="width:{pct:.1f}%"></div></div></div>'
                f'<p class="sys-note" style="border:0;padding-top:4px;">{t(note)}</p></div>')
    sc_today, sc_draft = d3['score_today'], d3['score_draft']
    cards3 = (shot('Heute', '#dc2626', 'rgba(239,68,68,0.12)', f'/review-assets/{p.get("assets_slug", p["slug"])}/startseite-heute.webp', d3['alt_today'], f'{sc_today} / 44', sc_today / 44 * 100, 'bad', d3['note_today'])
              + shot('So sollte es aussehen', '#15803d', 'rgba(34,150,60,0.12)', f'/review-assets/{p.get("assets_slug", p["slug"])}/startseite-entwurf.webp', d3['alt_draft'], d3.get('score_draft_label', f'{sc_draft} / 44'), sc_draft / 44 * 100, 'hire', d3['note_draft']))

    return f'''<!-- 741 System-Vorschau START (Suchthemen · Telefon klingeln · Startseite) -->
  <section class="sys-intro" id="system">
    <span class="sys-eyebrow">Was nach der Karte kommt</span>
    <h2 style="font-size:35.2px; font-weight:800; margin-top:8px;">{t(H(p, "system_h2", "Die Karte zeigt, wo du stehst. Hier siehst du, warum – und was konkret passiert."))}</h2>
    <p style="color:#666; max-width:760px; margin:12px auto 0; font-size:16px; line-height:1.6;">{t(s["intro"])}</p>
    <div class="sys-steps">{steps}</div>
  </section>

  <section class="sys-sec alt" id="content-pool">
    <div class="sys-head">
      <span class="sys-eyebrow">Schritt 1 · {E(st[0]["title"])}</span>
      <h2>{t(H(p, "step1_h2", d1["h2"]))}</h2>
      <p>{t(d1["lead"])}</p>
    </div>
    <div class="sys-two">
      <div class="sys-card">
        <h3>Was Menschen bei Google eingeben</h3>
        <div class="sys-sub">{t(d1["demand_sub"])}</div>
        {bars}
        <p class="sys-note"><b>Gelb = Fragen und Themen, grün = Suche nach {t(d1.get("provider_word", "einer Praxis"))}.</b> {t(d1["demand_note"])}</p>
        {nodata}
      </div>
      <div class="sys-card">
        <h3>{t(dp["title"])}</h3>
        <div class="sys-sub">{t(dp["sub"])}</div>
        <div class="sys-big">{big}</div>
        {('<div style="margin-top:16px;">' + dbars + '</div>') if dbars else ''}
        <p class="sys-note">{t(dp["note"])}</p>
      </div>
    </div>
    <div style="max-width:1060px;margin:0 auto;">{guide(p, 'think')}</div>
    <h3 class="sys-sub-h">{t(H(p, "items_h3", "Die 6 wichtigsten neuen Inhalte für deine Website"))}</h3>
    <div class="sys-list">{items}</div>
  </section>

  <section class="sys-sec" id="telefon-klingeln">
    <div class="sys-head">
      <span class="sys-eyebrow">Schritt 2 · {E(st[1]["title"])}</span>
      <h2>{t(H(p, "step2_h2", d2["h2"]))}</h2>
      <p>{t(d2["lead"])}</p>
    </div>
    <div class="sys-table-wrap">
      <table class="sys-table">
        <thead><tr><th>{E(d2.get("col_name", "Praxis"))}</th><th>So ordnet Google sie ein</th><th>Google-Bewertungen</th><th>Oben in der Karte bei „{E(d2["keyword"])}“</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    <p class="sys-swipe">← Tabelle seitwärts wischen →</p>
    <p class="sys-fine">{t(d2["fine"])}</p>
    <div class="sys-good"><b>Was das heißt:</b> {t(d2["meaning"])}</div>
    <div style="max-width:1060px;margin:0 auto;">{guide(p, 'insight', 'mg--right mg--flip')}</div>
    <h3 class="sys-sub-h">{t(H(p, "changes_h3", "Was wir an deinem Google-Eintrag konkret ändern"))}</h3>
    <div class="sys-checks">{checks}</div>
    <h3 class="sys-sub-h">{t(H(p, "cleanup_h3", "Vorher aufräumen: was dich heute Anrufe kostet"))}</h3>
    <div class="sys-stats">{stats}</div>
    {good2}
  </section>

  <section class="sys-sec alt" id="startseite">
    <div class="sys-head">
      <span class="sys-eyebrow">Schritt 3 · {E(st[2]["title"])}</span>
      <h2>{t(H(p, "step3_h2", "Die ersten 5 Sekunden entscheiden, ob jemand anfragt"))}</h2>
      <p>{t(d3["lead"])}</p>
    </div>
    <div class="sys-two">{cards3}</div>
    <h3 class="sys-sub-h">{t(H(p, "five_h3", "Der 5-Sekunden-Test: was dein erster Bildschirm heute nicht beantwortet"))}</h3>
    <div class="sys-five">{five}</div>
  </section>
<div class="rvw-lb" id="rvwLb" role="dialog" aria-label="Bild vergrößert"><b aria-hidden="true">×</b><img alt=""></div>
  <script>
  (function(){{
    var lb=document.getElementById('rvwLb'); if(!lb) return; var im=lb.querySelector('img');
    function open(e){{im.src=e.currentTarget.src; im.alt=e.currentTarget.alt; lb.classList.add('on');}}
    document.querySelectorAll('.sys-shot,.cs-shot').forEach(function(x){{x.addEventListener('click',open); x.addEventListener('keydown',function(ev){{if(ev.key==='Enter')open(ev);}});}});
    lb.addEventListener('click',function(){{lb.classList.remove('on');}});
    document.addEventListener('keydown',function(ev){{if(ev.key==='Escape')lb.classList.remove('on');}});
  }})();
  </script>
<!-- 741 System-Vorschau END -->
'''


# ---------------------------------------------------------------- calculator
CALC_JS = r'''<script>
  (function(){
    var G=%s;
    var all=[];
    Object.keys(G).forEach(function(k){
      var box=document.getElementById(k); if(!box) return;
      G[k].forEach(function(f){
        all.push(f);
        var r=document.createElement("div"); r.className="wr-row";
        r.innerHTML='<div><span>'+f.label+'</span><b id="wv_'+f.id+'"></b></div><input type="range" id="wr_'+f.id+'" min="'+f.min+'" max="'+f.max+'" step="'+f.step+'" value="'+f.val+'">';
        box.appendChild(r);
      });
    });
    if(!all.length) return;
    function eur(n){return Math.round(n).toLocaleString("de-DE")+" €";}
    function fmt(f,v){return f.f==="€"?(v<10&&v%%1?v.toFixed(2).replace(".",",")+" €":eur(v)):(f.f==="%%"?String(v).replace(".",",")+" %%":Math.round(v).toLocaleString("de-DE"));}
    function g(id){return parseFloat(document.getElementById("wr_"+id).value);}
    function calc(){
      all.forEach(function(f){document.getElementById("wv_"+f.id).innerText=fmt(f,g(f.id));});
      var org=g("vol")*g("share")/100, ads=g("cpc")>0?g("budget")/g("cpc"):0;
      var conv=g("conv")/100, deal=g("deal")/100;
      var lOrg=org*conv, lAds=ads*conv, leads=lOrg+lAds, deals=leads*deal;
      document.getElementById("wrVisits").innerText="≈ "+Math.round(org+ads);
      document.getElementById("wrLeads").innerText="≈ "+(Math.round(leads*10)/10).toLocaleString("de-DE");
      document.getElementById("wrDeals").innerText="≈ "+(Math.round(deals*10)/10).toLocaleString("de-DE");
      document.getElementById("wrRevYr").innerText=eur(deals*g("val")*12);
      var po=leads>0?lOrg/leads*100:50;
      document.getElementById("wrBarOrg").style.width=po+"%%";
      document.getElementById("wrBarAds").style.width=(100-po)+"%%";
      document.getElementById("wrSplitTxt").innerText=Math.round(po)+" %% / "+Math.round(100-po)+" %%";
      var dAds=lAds*deal;
      document.getElementById("wrCpa").innerText=dAds>0.01?eur(g("budget")/dAds):"–";
    }
    all.forEach(function(f){document.getElementById("wr_"+f.id).addEventListener("input",calc);});
    calc();
  })();
  </script>'''


def calc(p):
    c = p['calc']
    G = {
        'wrA': [dict(id='vol', label='Passende Google-Suchen / Monat', val=c['vol'], min=c.get('vol_min', 50), max=c.get('vol_max', 6000), step=10, f='n'),
                dict(id='share', label='Anteil der Klicks, den du mit Top-Plätzen bekommst', val=20, min=5, max=60, step=1, f='%')],
        'wrB': [dict(id='budget', label='Werbebudget / Monat', val=c['budget'], min=0, max=3000, step=50, f='€'),
                dict(id='cpc', label='Preis pro Klick', val=c['cpc'], min=0.5, max=20, step=0.1, f='€')],
        'wrC': [dict(id='conv', label='Anteil der Besucher, die anfragen', val=c.get('conv', 4), min=1, max=12, step=0.5, f='%'),
                dict(id='deal', label=c.get('deal_label', 'Anteil der Anfragen, die einen Termin buchen'), val=c.get('deal', 40), min=5, max=80, step=1, f='%'),
                dict(id='val', label=c['val_label'], val=c['val'], min=c.get('val_min', 100), max=c.get('val_max', 5000), step=50, f='€')],
    }
    return f'''<!-- 741 Wachstums-Rechner (Karte + Google-Anzeigen) START -->
  <section class="wr-sec" id="rechner">
    <div style="max-width:780px; margin:0 auto 30px; text-align:center;">
      <span style="color:#b48500; font-weight:800; text-transform:uppercase; font-size:12.8px; letter-spacing:.1em;">Wachstums-Rechner · Sichtbarkeit in Zahlen</span>
      <h2 style="font-size:34px; font-weight:800; margin-top:8px; line-height:1.15;">{t(H(p, "calc_h2", "Was Sichtbarkeit bei Google für dich bedeutet"))}</h2>
      <p style="color:#555; font-size:16px; margin-top:12px; line-height:1.6;">Sichtbarkeit bei Google hat zwei Quellen: <b>bezahlte Google-Anzeigen</b> ganz oben und <b>unbezahlte Plätze</b> in der Karte und in der Suche. Der Rechner zeigt beide getrennt. Zieh an den Reglern – die Startwerte sind vorsichtige Annahmen, im Gespräch setzen wir deine echten Zahlen ein.</p>
      <p style="color:#777; font-size:12.5px; margin-top:10px;">{t(c["volumes_line"])}</p>
    </div>
    <div class="wr-wrap">
      <div class="wr-card">
        <div class="wr-group"><i style="background:#2e8b34"></i>Gefunden in Karte und Suche (unbezahlt)</div><div id="wrA"></div>
        <div class="wr-group" style="margin-top:18px;"><i style="background:#fac118"></i>Google-Anzeigen (bezahlt)</div><div id="wrB"></div>
        <div class="wr-group" style="margin-top:18px;"><i style="background:#252525"></i>{E(c.get("group_c", "Aus Besuchern werden Patienten"))}</div><div id="wrC"></div>
      </div>
      <div class="wr-card" style="display:flex; flex-direction:column; justify-content:center;">
        <div class="wr-kpis">
          <div class="wr-kpi"><div class="n" id="wrVisits">–</div><small>Besucher / Monat</small></div>
          <div class="wr-kpi"><div class="n" id="wrLeads">–</div><small>Anfragen / Monat</small></div>
          <div class="wr-kpi"><div class="n" id="wrDeals">–</div><small>{E(c.get("deals_label", "neue Patienten / Monat"))}</small></div>
          <div class="wr-kpi"><div class="n g" id="wrRevYr">–</div><small>{E(c.get("revenue_label", "Mehrumsatz / Jahr"))}</small></div>
        </div>
        <div class="wr-split">
          <div class="lab"><span>Woher die Anfragen kommen</span><span id="wrSplitTxt"></span></div>
          <div class="wr-bar"><span id="wrBarOrg" style="background:#2e8b34;width:50%"></span><span id="wrBarAds" style="background:#fac118;width:50%"></span></div>
          <div class="lab" style="margin-top:6px;"><span style="color:#2e8b34;font-weight:700;">● Karte + Suche</span><span style="color:#b48500;font-weight:700;">● Google-Anzeigen</span></div>
        </div>
        <p style="font-size:12.5px; color:#666; margin:14px 0 0; text-align:center;">Werbebudget je {E(c.get("per_label", "neuem Patienten"))}: <b id="wrCpa">–</b></p>
      </div>
    </div>
    <div class="wr-levers">
      <div class="wr-lever"><div style="font-size:19px;">⚡</div><h3>Google-Anzeigen: ab dem ersten Tag</h3><p>Anzeigen stehen über der Karte und den Suchergebnissen. Sie bringen Anfragen sofort – solange das Budget läuft. Du zahlst pro Klick.</p></div>
      <div class="wr-lever"><div style="font-size:19px;">📍</div><h3>Karte und Suche: baut sich auf</h3><p>Plätze in der Google-Karte und in der Suche kosten pro Klick nichts. Sie brauchen ein paar Monate – und wirken dann dauerhaft.</p></div>
      <div class="wr-lever"><div style="font-size:19px;">🧲</div><h3>Die Website entscheidet</h3><p>Beides bringt Besucher. Ob daraus eine Anfrage wird, entscheidet deine Startseite – siehe Schritt 3 weiter oben.</p></div>
    </div>
    <p style="color:#888; font-size:11.5px; margin-top:20px; text-align:center;">Alle Werte sind Annahmen zum Selber-Einstellen. Das Werbebudget zahlst du direkt an Google.</p>
  </section>
  ''' + CALC_JS % json.dumps(G, ensure_ascii=False) + '\n<!-- 741 Wachstums-Rechner (Karte + Google-Anzeigen) END -->\n'


# ---------------------------------------------------------------- piano check
PILL = {'ok': ('pn-ok', 'Passt'), 'warn': ('pn-warn', 'Ausbaufähig'), 'crit': ('pn-crit', 'Dringend')}


def check(p):
    strips = ''
    total = 0
    for i, s in enumerate(p['check']):
        rows = s['rows']; total += len(rows)
        c = {k: sum(1 for r in rows if r['status'] == k) for k in PILL}
        parts = [f"{c['crit']} dringend"] * bool(c['crit']) + [f"{c['warn']} ausbaufähig"] * bool(c['warn']) + [f"{c['ok']} passt"] * bool(c['ok'])
        rr = ''.join(f'<div class="pn-row"><span class="pn-pill {PILL[r["status"]][0]}">{PILL[r["status"]][1]}</span><div><b>{E(r["title"])}</b><p>{t(r["text"])}</p></div></div>' for r in rows)
        strips += (f'<article class="pn-strip{" on" if i == 0 else ""}" tabindex="0" style="--bg:url({E(s["photo"])});--pos:{s.get("pos", "50% 50%")}">'
                   f'<span class="pn-open" aria-hidden="true">+</span><div class="pn-in"><span class="pn-ix">(0{i + 1})</span><h3>{E(s["title"])}</h3>'
                   f'<div class="pn-count">{" · ".join(parts)}</div><div class="pn-rows">{rr}</div></div></article>')
    return f'''<!-- Detailed Audit Breakdown Section (Klavier) -->
  <section class="pn-sec" id="check">
    <div style="max-width:760px; margin:0 auto 32px; text-align:center;">
      <span style="color:var(--brand--lemon); font-weight:800; text-transform:uppercase; font-size:12.8px; letter-spacing:.1em;">Der Website-Check</span>
      <h2 style="font-size:35.2px; font-weight:800; margin-top:6px;">{t(H(p, "check_h2", "Was wir auf deiner Website geprüft haben"))}</h2>
      <p style="color:#666;">{len(p["check"])} Bereiche, jeder Punkt an deiner echten Seite geprüft. Fahr über einen Bereich oder tipp ihn an, um ihn zu öffnen.</p>
    </div>
    <div class="pn-strips" id="pnStrips">{strips}</div>
    <p class="pn-hint">{len(p["check"])} Bereiche · {total} Punkte</p>
  </section>
  <script>
  (function(){{
    var ss=[].slice.call(document.querySelectorAll('#pnStrips .pn-strip')); if(!ss.length) return;
    var mq=window.matchMedia('(max-width:900px)');
    function act(s){{ss.forEach(function(x){{x.classList.toggle('on',x===s);}});}}
    ss.forEach(function(s){{
      s.addEventListener('mouseenter',function(){{if(!mq.matches)act(s);}});
      s.addEventListener('focusin',function(){{act(s);}});
      s.addEventListener('click',function(){{act(s);}});
      s.addEventListener('keydown',function(e){{if(e.key==='Enter'||e.key===' '){{e.preventDefault();act(s);}}}});
    }});
  }})();
  </script>

  '''


# ---------------------------------------------------------------- quick wins, roadmap
def quickwins(p):
    box = ''.join('<div class="quickwin-item-box" style="background:#fdfdfd; border:1px solid #eee; padding:20px; border-radius:14px; display:flex; gap:14px;">'
                  '<div class="quickwin-check-icon" style="width:28px; height:28px; border-radius:8px; background:rgba(250,193,24,0.2); color:#b48500; display:flex; align-items:center; justify-content:center; font-weight:900; flex-shrink:0;">✓</div>'
                  f'<div><h4 style="font-size:16px; font-weight:800; margin-bottom:4px;">{E(q["title"])}</h4><p style="font-size:13.6px; color:#666; margin:0;">{t(q["text"])}</p></div></div>' for q in p['quick_wins'])
    return f'''<!-- Quick Wins Section -->
  <section style="padding: 64px 5%; background:#fff; text-align:center;">
    <div style="max-width:760px; margin:0 auto 40px;">
      <span style="color:var(--brand--lemon); font-weight:800; text-transform:uppercase; font-size:12.8px;">Sofort-Maßnahmen</span>
      <h2 style="font-size:35.2px; font-weight:800; margin-top:6px;">{t(H(p, "quickwins_h2", "Was du schon morgen verbessern könntest"))}</h2>
      <p style="color:#666;">{len(p["quick_wins"])} Schritte, die sofort wirken – ohne neue Website.</p>
    </div>
    <div class="quickwins-grid-mobile" style="display:grid; grid-template-columns:repeat(2, 1fr); gap:20px; max-width:1000px; margin:0 auto; text-align:left;">
      {box}
    </div>
  </section>

  '''


def roadmap(p):
    rows = ''.join(f'<tr><td><strong>{E(r["step"])}</strong><br><span style="color:#666;font-size:13.5px;">{t(r["what"])}</span></td>'
                   f'<td><span class="{"pill-critical" if r["prio"] == "Hoch" else "pill-warning"}">{E(r["prio"])}</span></td><td>{E(r["effort"])}</td><td>{t(r["why"])}</td></tr>' for r in p['roadmap'])
    return f'''<!-- Action Roadmap Section -->
  <section style="padding: 64px 5%; background:#fff; text-align:center;">
    <div style="max-width:760px; margin:0 auto 40px;">
      <span style="color:var(--brand--lemon); font-weight:800; text-transform:uppercase; font-size:12.8px;">Priorisierter Plan</span>
      <h2 style="font-size:35.2px; font-weight:800; margin-top:6px;">{t(H(p, "roadmap_h2", "Mein strukturierter Fahrplan"))}</h2>
      <p style="color:#666;">Schritt für Schritt zu echter Sichtbarkeit für {E(p["business_ref"])}.</p>
    </div>
    <div class="audit-table-wrap" style="max-width:1140px; margin:0 auto;">
      <table class="audit-table">
        <thead><tr><th>Maßnahme</th><th>Priorität</th><th>Aufwand</th><th>Warum</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </section>

    '''


# ---------------------------------------------------------------- proof
def proof(p):
    """Results block right under the map: compact teaser row always visible, details behind one toggle (<details>)."""
    lib = json.load(open(os.path.join(MINI, 'case-library.json'), encoding='utf-8'))
    cases = {c['id']: c for c in lib['cases']}
    more = {c['id']: c for c in lib['more']}
    pr = p['proof']

    def pop(c):
        """Hover/focus image: the real map measurement after our work (case-library "proof.nachher")."""
        n = (c.get('proof') or {}).get('nachher')
        return (f'<span class="cs-pop" aria-hidden="true"><img src="{E(n)}" alt="" loading="lazy"><i>Nachher: echte Kartenmessung · {E(c["jump"])}</i></span>') if n else ''
    teaser = ''.join(f'<div class="cs-tz" tabindex="0"><img src="{E(cases[c]["img"])}" alt="{E(cases[c]["name"])}" loading="lazy"><div><b>{E(cases[c]["name"])}</b>'
                     f'<small>{E(cases[c]["sub"])}</small><em>{E(cases[c]["jump"])}</em></div>{pop(cases[c])}</div>' for c in pr['featured'])
    ab = lib.get('about') or {}
    about = ''
    if ab and pr.get('about', True):
        stats = ''.join(f'<div><b>{E(n)}</b><span>{E(l)}</span></div>' for n, l in ab.get('stats', []))
        pts = ''.join(f'<li>{E(x)}</li>' for x in ab.get('points', []))
        about = (f'<div class="cs-me"><img src="{E(ab["photo"])}" alt="{E(ab["name"])}" loading="lazy"><div class="cs-me-txt"><span class="cs-me-k">Wer dahintersteht</span>'
                 f'<b>{E(ab["name"])}</b><small>{E(ab["role"])}</small><ul>{pts}</ul></div><div class="cs-me-stats">{stats}</div></div>')
    cards = ''
    for i, cid in enumerate(pr['featured']):
        c = cases[cid]
        ul = ('<ul>' + ''.join(f'<li>{E(x)}</li>' for x in c['changes']) + '</ul>') if c['changes'] else ''
        shots = ''.join(f'<figure><img class="cs-shot" src="{E(u)}" alt="{E(k.capitalize())}: Kartenmessung {E(c["name"])}" loading="lazy" tabindex="0"><figcaption>{E(k.capitalize())}</figcaption></figure>'
                        for k, u in (c.get('proof') or {}).items())
        ul += f'<div class="cs-proof">{shots}</div>' if shots else ''
        links = ' &nbsp;·&nbsp; '.join(f'<a href="{E(u)}" target="_blank" rel="noopener">{E(l)}</a>' for l, u in c['links'])
        feat = ' feat' if i == 0 and pr.get('first_featured', True) else ''
        cards += (f'<div class="cs-card{feat}"><div class="cs-top"><img src="{E(c["img"])}" alt="{E(c["name"])}" loading="lazy"><div><b>{E(c["name"])}</b><small>{E(c["sub"])}</small></div>'
                  f'<div class="cs-jump"><div class="n">{E(c["jump"])}</div><small>{E(c["jump_sub"])}</small></div></div>'
                  f'<div class="cs-start"><b>{E(pr.get("labels", {}).get(cid, c.get("start_label", "Vorher:")))}</b> {E(c["start"])}</div>{ul}<div class="cs-link">{links}</div></div>')
    chips = ''
    for cid in pr['more']:
        c = more[cid]
        inner = f'<b>{E(c["name"])}</b>{E(c["sub"])}<em>{E(c["jump"])}</em>{pop(c)}'
        chips += f'<a class="cs-chip" href="{E(c["link"])}" target="_blank" rel="noopener">{inner}</a>' if c.get('link') else f'<div class="cs-chip">{inner}</div>'
    n = len(pr['featured'])
    return f'''<!-- Client Proof (individualisiert, unter der Karte, einklappbar) -->
  <section class="cs-sec cs-top-proof" id="ergebnisse">
    <div class="cs-head">
      <span style="color:#b48500; font-weight:800; text-transform:uppercase; font-size:12.8px; letter-spacing:.1em;">Ist der Sprung realistisch?</span>
      <h2>{t(H(p, "proof_h2", E(pr.get("h2_top", "Für diese Betriebe war er es"))))}</h2>
      <p>{t(pr["lead"])}</p>
    </div>
    <div class="cs-teaser">{teaser}</div>
    {about}
    <div style="max-width:1100px;margin:0 auto;">{guide(p, 'celebrate', 'mg--right')}</div>
    <details class="cs-fold">
      <summary><span><b class="o">So haben wir es gemacht – {n} Fälle ansehen</b><b class="c">Fälle schließen</b><i>▾</i></span></summary>
      <div class="cs-grid">{cards}</div>
      <h3 class="cs-more-h">Weitere Ergebnisse</h3>
      <div class="cs-more">{chips}</div>
    </details>
  </section>

'''


WORKFLOW_VIDEO = 'dQ9OE8GSolw'  # "Was Agenturen verstecken: von Anfang bis Ende, nichts versteckt" (04_site/pages/local-seo.html); Martin 2026-10-12


def workflow_video(p):
    """Our whole workflow on video, right after the facts. prospect.json "workflow_video": false hides it."""
    if p.get('workflow_video') is False:
        return ''
    return f'''<!-- 741 Workflow-Video START -->
  <section class="rvw-wv" id="ablauf">
    <span class="rvw-wv-k">Unser ganzer Ablauf</span>
    <h2>{t(H(p, "video_h2", "Was Agenturen verstecken: von Anfang bis Ende, nichts versteckt"))}</h2>
    <p>{t(H(p, "video_p", "In diesem Video zeige ich dir jeden Schritt, den wir für einen Betrieb wie deinen gehen. So weißt du vor dem Gespräch genau, was passiert."))}</p>
    <div class="rvw-wv-frame"><iframe src="https://www.youtube-nocookie.com/embed/{WORKFLOW_VIDEO}?rel=0" title="Was Agenturen verstecken: von Anfang bis Ende, nichts versteckt" loading="lazy"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
  </section>
<!-- 741 Workflow-Video END -->
'''


def final(p):
    f = p['final']
    return facts(p) + workflow_video(p) + f'''<!-- Final CTA Section -->
  <section class="section-video" id="termin" style="background:#000;">
    <div style="max-width:800px; margin:0 auto;">
      <h2 style="font-size:40px; font-weight:900; color:#fff; margin-bottom:16px;">{t(H(p, "final_h2", f["h2"]))}</h2>
      <p style="color:#aaa; font-size:17.6px; margin-bottom:32px;">{t(f["p"])}</p>
      <div class="final-cta-group">
        <a href="{CAL}" target="_blank" class="btn-741-main">Zeig mir meinen Markt →</a>
        <a href="mailto:martin@741.studio?subject={E(f.get("subject", "Sichtbarkeits-Analyse"))}" class="btn-741-dark">✉️ E-Mail schreiben</a>
      </div>
    </div>
  </section>

  '''


PLURAL = [('entscheidet deine Startseite', 'entscheidet eure Startseite'), ('setzen wir deine echten Zahlen ein', 'setzen wir eure echten Zahlen ein'),
          ('jeder Punkt an deiner echten Seite geprüft', 'jeder Punkt an eurer echten Seite geprüft'), ('wer in deinem Markt oben steht', 'wer in eurem Markt oben steht'),
          ('Das Werbebudget zahlst du direkt an Google', 'Das Werbebudget zahlt ihr direkt an Google')]


def main():
    pdir = sys.argv[1]
    pfile = sys.argv[2] if len(sys.argv) > 2 else 'prospect.json'
    p = json.load(open(os.path.join(pdir, pfile), encoding='utf-8'))
    s = open(os.path.join(MINI, 'template.html'), encoding='utf-8').read()
    for name, fn in [('hero', hero), ('grid', grid), ('system', system), ('calc', calc), ('check', check),
                     ('quickwins', quickwins), ('roadmap', roadmap), ('proof', lambda p: ''), ('final', final)]:
        mark = f'<!--SLOT:{name}-->\n'
        assert s.count(mark) == 1, name
        s = s.replace(mark, fn(p))
    if p.get('plural'):  # page speaks to a team, not to an owner ("euer Haus"): switch the fixed template phrases
        for a_, b_ in PLURAL: s = s.replace(a_, b_)
    s = s.replace('%%TITLE%%', E(p['meta']['title'])).replace('%%DESC%%', E(p['meta']['desc'])).replace('%%SLUG%%', p['slug'])
    out = os.path.join(ROOT, '04_site', 'review', p['slug'])
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(s)
    print('built', os.path.join(out, 'index.html'), len(s))


if __name__ == '__main__':
    main()
