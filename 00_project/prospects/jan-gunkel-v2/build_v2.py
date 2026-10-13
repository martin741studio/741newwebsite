#!/usr/bin/env python3
"""Build 04_site/review/jan-gunkel-v2/index.html from the jan-gunkel page (Fassung 2, Krisenfall-Deal-Flow).

Keeps head CSS, header/footer partials, scorecard tab script and proof wall of the source page.
Replaces hero, Nachfrage, Konzept, Rechner, Zusammenfassung, Scorecard, Sofort-Maßnahmen, Plan and final CTA.
Drops the old Loom video (old KI analysis) and the three Local-SEO service videos.
Evidence: evidence/dfs-*.json (DataForSEO 13.10.2026), sources.md.
"""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SRC = os.path.join(ROOT, '04_site/review/jan-gunkel/index.html')
OUT = os.path.join(ROOT, '04_site/review/jan-gunkel-v2/index.html')

s = open(SRC, encoding='utf-8').read()


def cut(start_marker, end_marker):
    a = s.index(start_marker)
    b = s.index(end_marker, a)
    return a, b


# ---------- head ----------
head_end = s.index('<!-- Hero Section -->')
head = s[:head_end]
head = re.sub(r'<title>.*?</title>', '<title>Konzept: Krisenfall-Deal-Flow | Jan Dominik Gunkel | 741.Studio</title>', head)
head = head.replace('Dein geschärftes Konzept: qualifizierter Deal-Flow zu Krisen- und Sanierungsfällen für Inupio / Jan Dominik Gunkel.',
                    'Fassung 2: passende Krisen- und Sanierungsfälle in Köln + 60 Minuten für deine Übernahmen.')
head = head.replace('Private Website- &amp; SEO-Analyse — Inupio (Jan Dominik Gunkel)', 'Konzept Krisenfall-Deal-Flow — Inupio (Jan Dominik Gunkel)')
head = head.replace('Dein geschärftes Konzept: qualifizierter Deal-Flow zu Krisen- und Sanierungsfällen, keine Beratungsmandate.',
                    'Passende Krisenfälle für deine Übernahmen, keine Beratungsmandate.')
head = head.replace('https://741.studio/review/jan-gunkel/', 'https://741.studio/review/jan-gunkel-v2/')

# ---------- kept blocks ----------
a, b = cut('<style>\n    .k-section', '</style>')
k_style = s[a:b + len('</style>')]
a, b = cut('<!-- Detailed Audit Breakdown Section -->', '<div id="tab-website"')
score_head = s[a:b]
a, b = cut('<!-- Client Proof Wall (social proof) -->', '<!-- Final CTA Section -->')
proof = s[a:b]
tail = s[s.index('<!-- Official 741.Studio Footer -->'):]

V2_STYLE = '''
  <style>
    .audit-headline{font-size:clamp(28px,2.6vw,40px);}
    .audit-headline .hsub{display:block;font-size:17px;font-weight:500;color:#4a4a4a;letter-spacing:0;margin-top:12px;line-height:1.5;}
    .audit-subheadline{font-size:17px;}
    .k-dcard .src{font-size:12px;color:#888;margin-top:10px;}
    .k-feeds{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:18px;}
    .k-feed{background:#f7f6f2;border-radius:14px;padding:16px 18px;}
    .k-feed .lv{font-size:12px;color:#b48500;font-weight:800;text-transform:uppercase;letter-spacing:.08em;}
    .k-feed h4{font-size:16px;font-weight:800;margin:6px 0 8px;}
    .k-feed p{font-size:14px;line-height:1.55;color:#333;margin:0;}
    .roi-src{font-size:11.5px;color:#8a8a8a;margin-top:3px;}
    .roi-kw{color:#cfcfcf;font-size:12.5px;margin-top:12px;line-height:1.6;}
    .roi-kw b{color:var(--brand--lemon);}
    .funnel-row{display:flex;align-items:center;gap:12px;margin-bottom:9px;}
    .funnel-row .lbl{width:150px;font-size:12px;color:#cfcfcf;}
    .funnel-row .bar{flex:1;background:#242424;border-radius:7px;height:22px;overflow:hidden;}
    .funnel-row .bar div{height:100%;background:linear-gradient(90deg,#4d9a3f,#1e7a46);}
    .funnel-row .n{width:40px;font-size:12px;font-weight:800;text-align:right;}
    @media(max-width:900px){.k-feeds{grid-template-columns:1fr;}}
    @media(max-width:768px){
      .roi-wrap,.roi-levers,.roi-out{grid-template-columns:1fr !important;}
      .audit-headline .hsub{font-size:14px !important;}
      .funnel-row .lbl{width:110px;}
      .k-demand{grid-template-columns:minmax(0,1fr) !important;}
      .k-dcard{min-width:0;padding:18px 16px;}
      .k-dcard li b{white-space:normal;text-align:right;}
      .k-dcard .big{font-size:26px;}
    }
  </style>
'''

HERO = '''<!-- Hero Section -->
  <section class="section-hero-audit">
    <div class="audit-eyebrow">🔒 DEIN KONZEPT · FASSUNG 2</div>
    <h1 class="audit-headline">
      Hallo Dominik, so kommen <span style="color:var(--brand--lemon);">passende Krisenfälle</span> aus deiner Region zu dir.
      <span class="hsub">Für deine Übernahmen: B2B, 20–200 Mitarbeiter, 5–50 Mio. Umsatz, Köln + 60 Minuten. Keine Beratungsmandate.</span>
    </h1>
    <p class="audit-subheadline">
      Du kaufst Firmen in der Krise meist zum symbolischen Preis und führst sie selbst weiter. Dafür brauchst du wenige, aber passende Fälle. Der Rechner zeigt, wie viele im Jahr realistisch sind.
    </p>

    <div class="hero-cta-group">
      <a href="#konzept" class="btn-741-main">▼ Zum Konzept</a>
      <a href="#rechner" class="btn-741-dark">🧮 Zum Fall-Rechner</a>
    </div>

    <div class="hero-cards-grid" style="grid-template-columns:repeat(3,1fr);">
      <div class="hero-card-item"><div class="hero-card-icon">🎯</div><div class="hero-card-title">Dein Zielprofil</div><div class="hero-card-sub">B2B · 20–200 Mitarbeiter · 5–50 Mio. · Köln + 60 Min.</div><div class="hero-card-badge" style="background:rgba(16,185,129,0.12); color:#047857;">1–2 Übernahmen / Jahr</div></div>
      <div class="hero-card-item"><div class="hero-card-icon">📂</div><div class="hero-card-title">609 eröffnete Firmen-Insolvenzen</div><div class="hero-card-sub">2024 im IHK-Bezirk Köln (2023: 440)</div><div class="hero-card-badge" style="background:rgba(250,193,24,0.2); color:#b48500;">+38 % in einem Jahr</div></div>
      <div class="hero-card-item"><div class="hero-card-icon">🔗</div><div class="hero-card-title">inupio.com</div><div class="hero-card-sub">leitet direkt auf LinkedIn weiter</div><div class="hero-card-badge" style="background:rgba(239,68,68,0.12); color:#b91c1c;">Bei „Inupio“ nicht in den Top 10</div></div>
    </div>
  </section>

'''

NACHFRAGE = '''
  <!-- Nachfrage in Zahlen -->
  <section class="k-section" style="background:#f7f6f2;" id="nachfrage">
    <div class="k-head">
      <span class="k-eyebrow">Wo Krisenfälle sichtbar werden</span>
      <h2 class="k-h2">Inhaber in der Krise suchen keinen Käufer. Sie suchen einen Ausweg.</h2>
      <p class="k-sub">Echte Google-Suchen pro Monat und Preis pro Klick (DataForSEO, 13.10.2026). Erste Zahl: Deutschland. In Klammern: NRW.</p>
    </div>
    <div class="k-demand">
      <div class="k-dcard"><h3>Inhaber in der Krise</h3><div class="big">≈ 7.990<small>Suchen / Monat (NRW ≈ 1.620)</small></div>
        <ul><li><span>StaRUG</span><b>2.900 (720) · 5,21 €</b></li><li><span>Insolvenz in Eigenverwaltung</span><b>2.900 (590) · 1,86 €</b></li><li><span>Schutzschirmverfahren</span><b>1.300 (260) · 2,13 €</b></li><li><span>Zahlungsunfähigkeit GmbH</span><b>720 (10)</b></li><li><span>Drohende Zahlungsunfähigkeit</span><b>170 (40) · 6,40 €</b></li></ul>
        <p class="src">Das sind die Wege aus der Krise vor oder in der Insolvenz. Nicht jede Suche kommt von einem Inhaber. Auch Berater suchen danach.</p></div>
      <div class="k-dcard"><h3>Die Verwalter und Berater</h3><div class="big">≈ 4.720<small>Suchen / Monat (NRW ≈ 950)</small></div>
        <ul><li><span>Insolvenzverwalter</span><b>4.400 (880)</b></li><li><span>Sanierungsberater</span><b>320 (70)</b></li><li><span>Insolvenzverwalter Köln</span><b>110</b></li><li><span>Insolvenz Köln</span><b>110</b></li><li><span>Insolvenzanwalt Köln</span><b>110</b></li></ul>
        <p class="src">Jede eröffnete Insolvenz hat einen Verwalter. Er führt auch den Verkauf des Betriebs.</p></div>
      <div class="k-dcard"><h3>Andere Käufer suchen auch</h3><div class="big">≈ 740<small>Suchen / Monat (NRW ≈ 150)</small></div>
        <ul><li><span>Insolvenzmasse kaufen</span><b>390 (70)</b></li><li><span>Firma für 1 Euro kaufen</span><b>210 (50)</b></li><li><span>Insolvente Firma kaufen</span><b>140 (30)</b></li></ul>
        <p class="src">Du bist nicht der einzige Käufer. Wer früh sichtbar ist, bekommt den Anruf zuerst.</p></div>
    </div>
    <p class="k-note">„Unternehmen in der Krise verkaufen“ und „Sanierungsfall Übernahme“ haben zu wenige Suchen für eine Messung. Für „firma für 1 euro kaufen“ zeigt Google in Köln oben Firmenbörsen und Ratgeber. Dazu kommen Anbieter, die GmbHs aufkaufen oder abwickeln. Kein Treffer zeigt einen Käufer, der den Betrieb selbst weiterführt.</p>
  </section>
'''

KONZEPT = '''
  <!-- Konzept: ein Strom -->
  <section class="k-section" style="background:#fff;" id="konzept">
    <div class="k-head">
      <span class="k-eyebrow">Das Konzept · ein Strom</span>
      <h2 class="k-h2">Krisenfall-Deal-Flow: drei Zuläufe, ein Ziel</h2>
      <p class="k-sub">Kein Beratungsangebot. Nur qualifizierte Kontakte zu Firmen in Krise und Sanierung, die du selbst übernimmst und führst.</p>
    </div>
    <div class="k-streams">
      <div class="k-stream">
        <div class="k-stream-top"><div class="k-num">1</div><div><h3>Krisenfall-Deal-Flow für deine Übernahmen</h3><p class="k-why">Krisenfälle laufen über Gerichte und Insolvenzverwalter, oft auch über Sanierungsberater oder die Hausbank. Genau dort setzt das System an.</p></div><span class="k-tag green">Einziger Fokus</span></div>
        <div class="k-cols">
          <div class="k-col"><h4>Befund · echte Zahlen</h4><p>Im IHK-Bezirk Köln wurden 2024 609 Firmen-Insolvenzen eröffnet. 2023 waren es 440. In ganz NRW gab es 2025 6.502 Insolvenzanträge von Firmen, 15,3 % mehr als 2024. Bundesweit haben 81,6 % der insolventen Firmen höchstens 10 Mitarbeiter. Die Fälle für dich sind also wenige. Aber es gibt sie jedes Jahr, und es werden mehr.</p></div>
          <div class="k-col"><h4>Was genau zu tun ist</h4><ol><li><b>Fall-Radar:</b> Wir prüfen jeden Werktag die öffentlichen Insolvenzbekanntmachungen für deine Region. Du bekommst jede Woche eine kurze Liste: Firma, Branche, Größe, zuständiger Verwalter.</li><li><b>Verwalter-Netzwerk:</b> eine Liste der Insolvenzverwalter und Sanierungsberater in Köln + 60 Min., dazu die Bankabteilungen für Krisenkredite. Du gibst ihnen dein Käufer-Profil auf einer Seite zum Weiterleiten.</li><li><b>Käufer-Seite und Anzeigen:</b> inupio.com zeigt, wer du bist und welche Fälle du suchst. Kleine Google-Anzeigen in NRW erreichen Inhaber schon vor dem Insolvenzantrag.</li></ol></div>
          <div class="k-col"><h4>Wie tief</h4><div class="k-depth"><div class="row"><span>Zeitrahmen</span><b>30 Tage Aufbau, dann laufend</b></div><div class="row"><span>Dein Aufwand</span><b>Zielprofil festlegen, Fälle prüfen, Gespräche führen</b></div><div class="row"><span>Mein Aufwand</span><b>Radar, Verwalter-Liste, Käufer-Seite, Anzeigen</b></div><div class="row"><span>Preis pro Klick in NRW</span><b>1,86 € bis 6,40 €</b></div></div></div>
        </div>
        <div class="k-feeds">
          <div class="k-feed"><span class="lv">Zulauf 1</span><h4>Fall-Radar</h4><p>Jeder eröffnete Fall steht öffentlich mit Gericht und Verwalter. Du siehst ihn in derselben Woche, nicht erst über Dritte.</p></div>
          <div class="k-feed"><span class="lv">Zulauf 2</span><h4>Verwalter-Netzwerk</h4><p>Der Verwalter sucht einen Käufer für den Betrieb. Wer ihm ein klares Profil gibt, steht auf seiner kurzen Liste.</p></div>
          <div class="k-feed"><span class="lv">Zulauf 3</span><h4>Vor dem Antrag</h4><p>In NRW suchen jeden Monat ≈ 1.620 Menschen nach StaRUG, Schutzschirm und Eigenverwaltung. Ein Teil davon sind Inhaber, die noch handeln können.</p></div>
        </div>
        <div class="k-measure"><b>Woran du es misst:</b> Fälle im Radar pro Monat, Gespräche mit Verwaltern, Fälle, die deine erste Prüfung bestehen, und Übernahmen (dein Ziel: 1–2 pro Jahr).</div>
      </div>
    </div>
    <p class="k-note">Quellen: IT.NRW über IHK Köln („Wirtschaftsregion Köln in Zahlen“, Ausgabe 2025), IT.NRW über Handwerksblatt (NRW 2025), Creditreform „Insolvenzen in Deutschland 2025“, DataForSEO 13.10.2026. Zeit und Aufwand sind meine Schätzung.</p>
  </section>
'''

RECHNER = '''
  <!-- Fall-Rechner: passende Krisenfälle pro Jahr -->
  <section style="padding:64px 5%; background:#0f0f0f; color:#fff;" id="rechner">
    <div style="max-width:1060px; margin:0 auto;">
      <div style="text-align:center; max-width:760px; margin:0 auto 30px;">
        <span style="color:var(--brand--lemon); font-weight:800; text-transform:uppercase; font-size:12.8px; letter-spacing:0.1em;">Fall-Rechner · passende Fälle pro Jahr</span>
        <h2 style="font-size:34px; font-weight:800; margin-top:8px; line-height:1.15;">Wie viele passende Fälle das System dir im Jahr bringt</h2>
        <p style="color:#b9b9b9; font-size:15px; margin-top:12px;">Zieh an den Reglern. Das Ergebnis ist keine Umsatzzahl. Es ist die Zahl der Fälle, die zu deinem Profil passen.</p>
        <p class="roi-kw">Echte Google-Suchen pro Monat (DataForSEO, 13.10.2026): <b>Insolvenzverwalter 4.400</b> · <b>StaRUG 2.900</b> · <b>Insolvenz in Eigenverwaltung 2.900</b> · <b>Schutzschirmverfahren 1.300</b> · <b>Firma für 1 Euro kaufen 210</b> · <b>Insolvenzverwalter Köln 110</b></p>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px;" class="roi-wrap">
        <div style="background:#161616; border:1px solid #2a2a2a; border-radius:16px; padding:22px;">
          <div style="font-size:12px; color:#9a9a9a; text-transform:uppercase; letter-spacing:.06em; font-weight:800; margin-bottom:14px;">Zahlen und Annahmen</div>
          <div id="roiInputs"></div>
        </div>
        <div style="background:linear-gradient(160deg,#1c1c1c,#141414); border:1px solid #2a2a2a; border-radius:16px; padding:22px; display:flex; flex-direction:column; justify-content:center;">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;" class="roi-out">
            <div style="text-align:center; background:#101010; border:1px solid #262626; border-radius:12px; padding:16px;">
              <div id="outMarket" style="font-size:32px; font-weight:900; color:var(--brand--lemon);">–</div>
              <div style="font-size:12px; color:#cfcfcf; margin-top:4px;">passende Fälle in deiner Region / Jahr</div>
            </div>
            <div style="text-align:center; background:#101010; border:1px solid #262626; border-radius:12px; padding:16px;">
              <div id="outSeen" style="font-size:32px; font-weight:900; color:var(--brand--lemon);">–</div>
              <div style="font-size:12px; color:#cfcfcf; margin-top:4px;">Fälle, die du siehst / Jahr</div>
            </div>
            <div style="text-align:center; background:#101010; border:1px solid #262626; border-radius:12px; padding:16px;">
              <div id="outCheck" style="font-size:26px; font-weight:900; color:#4d9a3f;">–</div>
              <div style="font-size:12px; color:#cfcfcf; margin-top:4px;">Fälle für deine Prüfung / Jahr</div>
            </div>
            <div style="text-align:center; background:#101010; border:1px solid #262626; border-radius:12px; padding:16px;">
              <div style="font-size:26px; font-weight:900; color:#4d9a3f;">1–2</div>
              <div style="font-size:12px; color:#cfcfcf; margin-top:4px;">dein Ziel: Übernahmen / Jahr</div>
            </div>
          </div>
          <div style="margin-top:16px;">
            <div class="funnel-row"><div class="lbl">Passend im Markt</div><div class="bar"><div id="barMarket" style="width:100%;"></div></div><div class="n" id="nMarket">–</div></div>
            <div class="funnel-row"><div class="lbl">Siehst du</div><div class="bar"><div id="barSeen" style="width:60%;"></div></div><div class="n" id="nSeen">–</div></div>
            <div class="funnel-row"><div class="lbl" style="color:#fff;font-weight:700;">Zur Prüfung</div><div class="bar"><div id="barCheck" style="width:12%;"></div></div><div class="n" id="nCheck">–</div></div>
          </div>
          <p id="outMonth" style="font-size:12.5px; color:#cfcfcf; margin-top:12px; text-align:center;"></p>
        </div>
      </div>

      <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-top:22px;" class="roi-levers">
        <div style="background:#1a1a1a; border:1px solid #2a2a2a; border-radius:14px; padding:16px;"><div style="font-size:19px;">📡</div><h3 style="font-size:14.5px; font-weight:800; margin:7px 0 5px;">Fall-Radar</h3><p style="font-size:12px; color:#b9b9b9; line-height:1.5;">Hebt den Anteil der Fälle, die du siehst. Ohne Radar erfährst du von manchen Fällen erst, wenn es zu spät ist.</p></div>
        <div style="background:#1a1a1a; border:1px solid #2a2a2a; border-radius:14px; padding:16px;"><div style="font-size:19px;">🤝</div><h3 style="font-size:14.5px; font-weight:800; margin:7px 0 5px;">Verwalter-Netzwerk</h3><p style="font-size:12px; color:#b9b9b9; line-height:1.5;">Bringt Fälle mit Vorinformation. Der Verwalter kennt Zahlen und Team. Er sagt dir früh, ob es passt.</p></div>
        <div style="background:#1a1a1a; border:1px solid #2a2a2a; border-radius:14px; padding:16px;"><div style="font-size:19px;">🧲</div><h3 style="font-size:14.5px; font-weight:800; margin:7px 0 5px;">Käufer-Seite + Anzeigen</h3><p style="font-size:12px; color:#b9b9b9; line-height:1.5;">Bringt Anfragen vor dem Insolvenzantrag. Diese Fälle stehen in keiner Bekanntmachung.</p></div>
      </div>
      <p style="color:#7c7c7c; font-size:11.5px; margin-top:20px; text-align:center;">Feste Zahlen: IT.NRW über IHK Köln (eröffnete Firmen-Insolvenzen 2024), Creditreform (Größe 2025). Der IHK-Bezirk Köln umfasst Köln, Leverkusen, Rhein-Erft-Kreis, Oberbergischen und Rheinisch-Bergischen Kreis. Bonn, Düsseldorf oder Aachen sind nicht enthalten. Köln + 60 Min. ist also größer. Alle anderen Regler sind Annahmen. Setz deine eigenen Werte ein.</p>
    </div>
  </section>

  <script>
  (function(){
    var F=[
      {id:"base", label:"Eröffnete Firmen-Insolvenzen / Jahr in deiner Region", src:"609 = IHK-Bezirk Köln 2024 (IT.NRW)", val:609, min:300, max:2000, step:1, suf:""},
      {id:"size", label:"Davon mit mehr als 10 Mitarbeitern", src:"18 % = bundesweit 2025 (Creditreform: 81,6 % haben bis 10)", val:18, min:5, max:40, step:1, suf:" %"},
      {id:"b2b",  label:"Davon B2B und in deinen Branchen", src:"Annahme", val:50, min:10, max:90, step:5, suf:" %"},
      {id:"seen", label:"Fälle, die du rechtzeitig siehst (Radar + Verwalter)", src:"Annahme", val:60, min:10, max:90, step:5, suf:" %"},
      {id:"pre",  label:"Anfragen vor dem Insolvenzantrag / Jahr (Käufer-Seite + Anzeigen)", src:"Annahme", val:2, min:0, max:24, step:1, suf:""},
      {id:"pass", label:"Fälle, die deine erste Prüfung bestehen", src:"Annahme", val:20, min:5, max:50, step:1, suf:" %"}
    ];
    var box=document.getElementById("roiInputs"); if(!box) return;
    F.forEach(function(f){
      var row=document.createElement("div"); row.style.marginBottom="13px";
      row.innerHTML='<div style="display:flex; justify-content:space-between; gap:10px; font-size:12.5px; color:#dcdcdc; margin-bottom:5px;"><span>'+f.label+'</span><b id="v_'+f.id+'" style="color:var(--brand--lemon); white-space:nowrap;"></b></div>'+
        '<input type="range" id="'+f.id+'" min="'+f.min+'" max="'+f.max+'" step="'+f.step+'" value="'+f.val+'" style="width:100%; accent-color:#fac118;" aria-label="'+f.label+'">'+
        '<div class="roi-src">'+f.src+'</div>';
      box.appendChild(row);
    });
    function fmt(x){return (Math.round(x*10)/10).toString().replace(".",",");}
    function calc(){
      var g=function(id){return parseFloat(document.getElementById(id).value);};
      F.forEach(function(f){document.getElementById("v_"+f.id).innerText=g(f.id).toLocaleString("de-DE")+f.suf;});
      var market=g("base")*g("size")/100*g("b2b")/100;
      var seen=market*g("seen")/100+g("pre");
      var check=seen*g("pass")/100;
      document.getElementById("outMarket").innerText="≈ "+Math.round(market);
      document.getElementById("outSeen").innerText="≈ "+Math.round(seen);
      document.getElementById("outCheck").innerText="≈ "+Math.round(check);
      var mx=Math.max(market,seen,1);
      document.getElementById("barMarket").style.width=(market/mx*100)+"%";
      document.getElementById("barSeen").style.width=(seen/mx*100)+"%";
      document.getElementById("barCheck").style.width=Math.max(2,check/mx*100)+"%";
      document.getElementById("nMarket").innerText=Math.round(market);
      document.getElementById("nSeen").innerText=Math.round(seen);
      document.getElementById("nCheck").innerText=Math.round(check);
      document.getElementById("outMonth").innerText="Das sind etwa "+fmt(check/12)+" Fälle pro Monat, die du genauer prüfst.";
    }
    F.forEach(function(f){document.getElementById(f.id).addEventListener("input",calc);});
    calc();
  })();
  </script>
'''


def card(level, title, text):
    pill = {'crit': 'pill-critical">Kritisch', 'warn': 'pill-warning">Ausbaufähig', 'ok': 'pill-good">OK'}[level]
    return (f'<div class="audit-score-card"><span class="{pill}</span><strong style="display:block; margin:10px 0 4px; font-size:16px;">'
            f'{title}</strong><p style="font-size:14px; color:#666; margin:0;">{text}</p></div>')


def pane(pid, cards, show=False):
    return (f'    <div id="tab-{pid}" class="tab-pane" style="display:{"block" if show else "none"};">\n'
            f'      <div class="audit-card-grid" style="max-width:1140px; margin:0 auto;">\n        '
            + ''.join(card(*c) for c in cards) + '\n      </div>\n    </div>\n')


SUMMARY = '''
  <!-- Executive Summary Section -->
  <section style="padding: 64px 5%; background:#fff; text-align:center;">
    <div style="max-width:760px; margin:0 auto;">
      <span style="color:var(--brand--lemon); font-weight:800; text-transform:uppercase; font-size:12.8px;">Zusammenfassung</span>
      <h2 style="font-size:35.2px; font-weight:800; margin-top:6px;">Die wichtigsten Funde auf einen Blick</h2>
      <p style="color:#666;">Wo du heute stehst und wo die Fälle herkommen.</p>
    </div>

    <div class="summary-grid" style="max-width:1140px; margin-left:auto; margin-right:auto;">
      <div class="summary-box green"><div class="summary-tag">🟢 Stärken</div><h3 style="font-size:19.2px; font-weight:800; margin-bottom:14px;">Was schon für dich spricht</h3><ul class="summary-ul"><li>Dein Profil ist klar: B2B, 20–200 Mitarbeiter, 5–50 Mio. Umsatz, Köln + 60 Minuten.</li><li>Du führst selbst. Als früherer Geschäftsführer bei Brandt kennst du den Betrieb von innen. Das zählt für einen Verwalter.</li><li>Du investierst schon in Search Funds und kennst Übernahmen aus der Praxis.</li></ul></div>
      <div class="summary-box amber"><div class="summary-tag">🟠 Größte Chance</div><h3 style="font-size:19.2px; font-weight:800; margin-bottom:14px;">Wo die Fälle liegen</h3><ul class="summary-ul"><li><strong>Fälle früh sehen:</strong> 609 eröffnete Firmen-Insolvenzen im Jahr im IHK-Bezirk Köln, jede mit einem Verwalter als Ansprechpartner.</li><li><strong>Vor dem Antrag da sein:</strong> ≈ 1.620 Suchen im Monat in NRW nach StaRUG, Schutzschirm oder Eigenverwaltung.</li><li><strong>Als Käufer auffallen, der weiterführt:</strong> Bei „firma für 1 euro kaufen“ steht in Köln kein solcher Käufer oben.</li></ul></div>
      <div class="summary-box red"><div class="summary-tag">🔴 Lücken</div><h3 style="font-size:19.2px; font-weight:800; margin-bottom:14px;">Was heute fehlt</h3><ul class="summary-ul"><li><strong>inupio.com leitet direkt auf LinkedIn weiter.</strong> Es gibt keine Seite, die ein Verwalter weitergeben kann.</li><li><strong>Bei „Inupio“ zeigt Google andere Firmen.</strong> Du bist nicht unter den ersten 10 Treffern.</li><li><strong>Kein festes System für neue Fälle.</strong> Ohne Radar hängt der Zulauf an Zufall und einzelnen Kontakten.</li></ul></div>
    </div>
  </section>
'''

SCORE = (SUMMARY + '\n  ' + score_head
         .replace('Website- & SEO-Scorecard', 'Dein Auftritt als Käufer')
         .replace('Systematische Analyse nach der 741-Studio-Methodik — jeder Punkt an der Live-Seite geprüft.',
                  'Jeder Punkt an inupio.com und bei Google geprüft (13.10.2026).')
         .replace('>Website & Technik<', '>Website<').replace('>On-Page SEO<', '>Bei Google<')
         .replace('>Analytics & Tracking<', '>Messung<').replace('>Sichtbarkeit & Autorität<', '>Vertrauen<')
         + pane('website', [
             ('crit', 'Eigene Website', 'Keine. inupio.com leitet direkt auf dein LinkedIn-Profil weiter.'),
             ('crit', 'Käufer-Profil', 'Nirgends steht, welche Fälle du suchst und wie schnell du entscheidest.'),
             ('crit', 'Kontaktweg für Verwalter', 'Kein Formular, keine Telefonnummer, kein diskreter Weg für einen Fall.'),
             ('ok', 'Domain vorhanden', 'inupio.com ist registriert. Die Basis ist da, sie wird nur nicht genutzt.'),
             ('warn', 'Abhängigkeit von LinkedIn', 'Dein ganzer Auftritt läuft über eine Plattform, die dir nicht gehört.'),
             ('warn', 'Diskretion sichtbar machen', 'Inhaber in der Krise brauchen das Versprechen, dass nichts nach außen dringt.'),
         ], show=True)
         + pane('seo', [
             ('crit', 'Eigener Firmenname', 'Bei „Inupio“ zeigt Google andere Firmen. Du bist nicht unter den ersten 10 Treffern.'),
             ('crit', 'Name deiner Seite bei Google', 'Keiner. Es gibt keine eigene Seite, die Google zeigen kann.'),
             ('crit', 'Suchwörter der Inhaber', 'Für Suchwörter wie StaRUG oder Schutzschirmverfahren bist du nicht zu finden.'),
             ('warn', 'Suchwörter der Verwalter', '„Insolvenzverwalter Köln“ hat 110 Suchen im Monat. Eine Seite für Verwalter fehlt.'),
             ('warn', 'Firmendaten für Google', 'Firmenname und Region fehlen in einer Form, die Google lesen kann.'),
             ('warn', 'Abgrenzung', 'Zeig klar: Du führst den Betrieb weiter. Du wickelst ihn nicht ab.'),
         ])
         + pane('analytics', [
             ('crit', 'Besucher-Messung', 'Nicht möglich. Es gibt keine eigene Seite, auf der man messen kann.'),
             ('crit', 'Google-Konto für deine Seite', 'Nicht vorhanden. Du siehst nicht, wer nach dir sucht.'),
             ('warn', 'Anfragen zählen', 'Jede Fall-Anfrage soll mit Quelle erfasst werden: Radar, Verwalter oder Anzeige.'),
             ('warn', 'Fall-Liste', 'Eine einfache Liste mit Status: gesehen, geprüft, im Gespräch, abgelehnt.'),
         ])
         + pane('authority', [
             ('ok', 'Persönliche Erfahrung', 'Geschäftsführung, Beirat, Search Funds: Das ist echte Autorität.'),
             ('crit', 'Belege für Verwalter', 'Keine Fallbeispiele, die zeigen, wie du einen Betrieb weiterführst.'),
             ('warn', 'Käufer-Profil als PDF', 'Eine Seite, die Verwalter und Banken an Inhaber weiterleiten können.'),
             ('warn', 'Referenzen', 'Stationen und Übernahmen sichtbar machen, mit Erlaubnis der Beteiligten.'),
         ])
         + '  </section>\n')

QUICK_ITEMS = [
    ('inupio.com als Käufer-Seite aktivieren', 'Eine Seite statt Weiterleitung: wer du bist, was du suchst, wie schnell du entscheidest.'),
    ('Zielprofil auf einer Seite', 'B2B, 20–200 Mitarbeiter, 5–50 Mio., Köln + 60 Min. Als PDF für Verwalter und Banken.'),
    ('Verwalter-Liste für deine Region', 'Die Kanzleien, die in Köln + 60 Min. Firmen-Insolvenzen führen. Dann persönlich anrufen.'),
    ('Insolvenzbekanntmachungen prüfen', 'Jeden Werktag die neuen Fälle aus deiner Region. Nur Firmen, die in dein Profil passen.'),
    ('Anzeigen auf die Suchwörter der Inhaber', 'StaRUG, Schutzschirmverfahren, Eigenverwaltung. Preis pro Klick in NRW 1,86 € bis 6,40 €.'),
    ('Für „Inupio“ gefunden werden', 'Heute zeigt Google bei deinem Firmennamen andere Firmen.'),
]
QW_BOX = ('<div class="quickwin-item-box" style="background:#fdfdfd; border:1px solid #eee; padding:20px; border-radius:14px; display:flex; gap:14px;">'
          '<div class="quickwin-check-icon" style="width:28px; height:28px; border-radius:8px; background:rgba(250,193,24,0.2); color:#b48500; display:flex; align-items:center; justify-content:center; font-weight:900; flex-shrink:0;">✓</div>'
          '<div><h4 style="font-size:16px; font-weight:800; margin-bottom:4px;">{}</h4><p style="font-size:13.6px; color:#666; margin:0;">{}</p></div></div>')

QUICK = '''
  <!-- Quick Wins Section -->
  <section style="padding: 64px 5%; background:#fff; text-align:center;">
    <div style="max-width:760px; margin:0 auto 40px;">
      <span style="color:var(--brand--lemon); font-weight:800; text-transform:uppercase; font-size:12.8px;">Sofort-Maßnahmen</span>
      <h2 style="font-size:35.2px; font-weight:800; margin-top:6px;">Was du schon diese Woche starten kannst</h2>
      <p style="color:#666;">Sechs Schritte, die keinen großen Aufwand brauchen.</p>
    </div>

    <div class="quickwins-grid-mobile" style="display:grid; grid-template-columns:repeat(2, 1fr); gap:20px; max-width:1000px; margin:0 auto; text-align:left;">
      ''' + ''.join(QW_BOX.format(t, d) for t, d in QUICK_ITEMS) + '''
    </div>
  </section>
'''

ROWS = [
    ('Woche 1–2 · Fundament', 'Käufer-Seite auf inupio.com, Zielprofil als PDF, Besucher-Messung', 'crit', 'Hoch', 'Mittel', 'Verwalter brauchen etwas, das sie weitergeben können'),
    ('Woche 2–4 · Fall-Radar', 'Tägliche Prüfung der Insolvenzbekanntmachungen, Wochenliste mit Verwalter', 'crit', 'Hoch', 'Gering', 'Jeder eröffnete Fall hat einen Verwalter als Ansprechpartner'),
    ('Woche 3–8 · Verwalter-Netzwerk', 'Liste der Verwalter und Sanierungsberater, persönliche Ansprache', 'crit', 'Hoch', 'Mittel', 'Der Verwalter führt den Verkauf des Betriebs'),
    ('Ab Woche 4 · Vor dem Antrag', 'Kleine Google-Anzeigen in NRW auf StaRUG, Schutzschirm oder Eigenverwaltung', 'warn', 'Mittel', 'Gering', 'Erreicht Inhaber, bevor ein Gericht beteiligt ist'),
    ('Laufend', 'Fälle prüfen, Zahlen gegen dein Ziel von 1–2 Übernahmen im Jahr messen', 'warn', 'Mittel', 'Gering', 'Deal-Flow ist ein Dauerprozess, kein Projekt mit Enddatum'),
]
PLAN = '''
  <!-- Action Roadmap Section -->
  <section style="padding: 64px 5%; background:#fff; text-align:center;">
    <div style="max-width:760px; margin:0 auto 40px;">
      <span style="color:var(--brand--lemon); font-weight:800; text-transform:uppercase; font-size:12.8px;">Priorisierter Plan</span>
      <h2 style="font-size:35.2px; font-weight:800; margin-top:6px;">Der Fahrplan für deinen Krisenfall-Deal-Flow</h2>
      <p style="color:#666;">Ein Strom, in vier Schritten aufgebaut.</p>
    </div>

    <div class="audit-table-wrap" style="max-width:1140px; margin:0 auto;">
      <table class="audit-table">
        <thead>
          <tr><th>Maßnahme</th><th>Priorität</th><th>Aufwand</th><th>Warum</th></tr>
        </thead>
        <tbody>
''' + ''.join(f'          <tr><td><strong>{a}</strong><br><span style="color:#666;font-size:13.5px;">{b}</span></td><td><span class="pill-{"critical" if c == "crit" else "warning"}">{d}</span></td><td>{e}</td><td>{f}</td></tr>\n' for a, b, c, d, e, f in ROWS) + '''        </tbody>
      </table>
    </div>
  </section>

'''

CTA = '''  <!-- Final CTA Section -->
  <section class="section-video" id="termin" style="background:#000;">
    <div style="max-width:800px; margin:0 auto;">
      <h2 style="font-size:40px; font-weight:900; color:#fff; margin-bottom:16px;">Passt die Richtung, Dominik?</h2>
      <p style="color:#aaa; font-size:17.6px; margin-bottom:32px;">Sag mir, welche Zahl im Rechner du anders siehst. Dann baue ich zuerst das Fall-Radar für deine Region.</p>

      <div class="final-cta-group">
        <a href="https://cal.com/741-studio-simjzw/30min" target="_blank" class="btn-741-main">📅 Kostenloses Gespräch buchen</a>
        <a href="mailto:martin@741.studio?subject=Inupio%20Krisenfall-Deal-Flow" class="btn-741-dark">✉️ E-Mail schreiben</a>
      </div>
    </div>
  </section>

  '''

html = (head + V2_STYLE + '\n  ' + HERO + '\n  ' + k_style + '\n' + NACHFRAGE + KONZEPT + RECHNER
        + SCORE + QUICK + PLAN + '    ' + proof + CTA + tail)
new_parts = [HERO, NACHFRAGE, KONZEPT, RECHNER, SCORE, QUICK, PLAN, CTA]
for part in new_parts:
    fixed = re.sub(r'(\d)–(\d)', r'\1 bis \2', part).replace('>–<', '>…<').replace(' — ', ': ')
    html = html.replace(part, fixed)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(html)
print('wrote', OUT, len(html))
