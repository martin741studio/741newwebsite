"""The construction-mode password gate injected into every built page (26.10.2026, Martin).
Real traffic can now reach meandyou.de and the site is not finished, so every page stays behind
a shared team password until Martin lifts this. Split into its own file so assemble.py's string
quoting stays simple."""

GATE_PASSWORD = "pagencymeandyou"
GATE_ENABLED = False

GATE_SNIPPET = """
<style id="mgy-gate-style">html.mgy-locked body>*:not(#mgy-gate){display:none!important}#mgy-gate{display:none}html.mgy-locked #mgy-gate{display:flex}</style>
<div id="mgy-gate" style="position:fixed;inset:0;z-index:99999;background:#FAF8F4;color:#2A2622;align-items:center;justify-content:center;font-family:Inter,system-ui,sans-serif;padding:24px">
 <div style="max-width:420px;width:100%;text-align:center">
  <p style="font:600 12px/1 Inter,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#64809E;margin:0 0 14px">me&amp;you Communication</p>
  <h1 style="font:400 28px/1.25 Georgia,serif;margin:0 0 14px">Diese Seite wird gerade aufgebaut.</h1>
  <p style="color:#7B736B;margin:0 0 24px;font-size:15px">Team-Zugang mit Passwort.</p>
  <form id="mgy-gate-form" style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap">
   <input id="mgy-gate-pw" type="password" placeholder="Passwort" autocomplete="off" style="padding:12px 16px;border-radius:999px;border:1.5px solid rgba(42,38,34,.22);font-size:15px;min-width:200px">
   <button type="submit" style="padding:12px 26px;border-radius:999px;border:none;background:#2B3C52;color:#fff;font:600 15px/1 Inter,sans-serif;cursor:pointer">Ansehen</button>
  </form>
  <p id="mgy-gate-err" style="color:#B0453D;font-size:13px;margin:12px 0 0;display:none">Falsches Passwort.</p>
 </div>
</div>
<script>(function(){
 var KEY='mgy_gate_ok';
 if(localStorage.getItem(KEY)==='1'){return;}
 document.documentElement.classList.add('mgy-locked');
 document.addEventListener('DOMContentLoaded',function(){
  var f=document.getElementById('mgy-gate-form'),pw=document.getElementById('mgy-gate-pw'),err=document.getElementById('mgy-gate-err');
  f.addEventListener('submit',function(e){
   e.preventDefault();
   if(pw.value===GATE_PASSWORD_PLACEHOLDER){localStorage.setItem(KEY,'1');document.documentElement.classList.remove('mgy-locked');}
   else{err.style.display='block';pw.value='';pw.focus();}
  });
 });
})();</script>
""".replace("GATE_PASSWORD_PLACEHOLDER", "'" + GATE_PASSWORD + "'")


import re

PROTO_BADGE_RE = re.compile(r'<div class="proto">[^<]*</div>')


def apply_gate_and_banner(out_dir):
    """Final pass over every built HTML file, including nested paths the PAGES loop never
    reaches (e.g. videokurs/start.html). Strips the preview badge and injects the password gate
    (gate re-enabled 02.11.2026: Martin, the site is not confirmed for public release yet)."""
    import os
    for root, _, files in os.walk(out_dir):
        for fn in files:
            if not fn.endswith(".html"):
                continue
            fp = os.path.join(root, fn)
            html = open(fp, encoding="utf-8").read()
            html = PROTO_BADGE_RE.sub("", html)
            # Gate disabled 04.11.2026: Tajan (Pagency) gave the go to open the site.
            # Set GATE_ENABLED = True to lock the site again with the same password.
            if GATE_ENABLED and 'id="mgy-gate"' not in html and "<body" in html:
                i = html.index(">", html.index("<body")) + 1
                html = html[:i] + GATE_SNIPPET + html[i:]
            open(fp, "w", encoding="utf-8").write(html)
