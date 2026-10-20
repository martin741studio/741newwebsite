#!/usr/bin/env python3
"""Render the explainer mails (txt) as portal-style HTML (Resend body) + one preview page for Martin."""
import html, json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
MAILS = [  # file, client, to, lang, status
    ("suriya", "Praxis Suriya", "suriyapraxis@gmail.com", "de", "ready"),
    ("huewel", "Praxis Hüwel", "info@praxis-huewel.de", "de", "ready"),
    ("brasse", "Maria Brasse", "kontakt@shuiguru.de", "de", "ready"),
    ("dumann", "Naturheilpraxis Daniela Dumann", "daniela.dumann@live.de", "de", "ready"),
    ("stuerzl", "STÜRZL Steuerstrafrecht", "stuerzl@stuerzl-steuerstrafrecht.de", "de", "ready"),
    ("bali", "Bali Healing", "info@balihealing.com", "en", "ready"),
    ("rabenmuetter", "Rabenmütter Shop", "fp@rocket-libri.com", "de", "after release of 7 cards"),
    ("dumann-login", "Naturheilpraxis Daniela Dumann", "daniela.dumann@live.de", "de", "ready (login reset 14.10.)"),
    ("celine-johni", "Johni Jaya Motor", "celine_rosalina@hotmail.com", "en", "after release of 7 cards + Celine login"),
]
BTN = {"de": "Zu deinen Entscheidungen", "en": "Open your decisions"}

def body_html(lines, lang):
    out, ul = [], []
    def flush():
        if ul:
            out.append('<ul style="margin:0 0 16px;padding-left:20px">' + "".join(f'<li style="margin:4px 0">{x}</li>' for x in ul) + "</ul>"); ul.clear()
    para = []
    def pflush():
        if para:
            out.append('<p style="margin:0 0 16px">' + "<br>".join(para) + "</p>"); para.clear()
    for ln in lines:
        s = ln.rstrip()
        if not s:
            pflush(); flush(); continue
        if s.startswith("• "):
            pflush(); ul.append(html.escape(s[2:])); continue
        flush()
        if re.fullmatch(r"https://clients\.741\.studio/\?view=decisions", s):
            pflush()
            out.append(f'<p style="margin:4px 0 20px"><a href="{s}" style="display:inline-block;background:#fac118;color:#111;font-weight:700;text-decoration:none;padding:12px 22px;border-radius:10px">{BTN[lang]}</a><br><span style="font-size:13px;color:#777">{html.escape(s)}</span></p>')
            continue
        e = html.escape(s)
        e = re.sub(r"(https://[^\s<]+)", r'<a href="\1" style="color:#111">\1</a>', e)
        para.append(e)
    pflush(); flush()
    return "".join(out)

def mail_html(subject, lines, lang):
    return f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>{html.escape(subject)}</title></head>
<body style="margin:0;background:#f6f3ea;font-family:'DM Sans',Arial,sans-serif;color:#111;font-size:16px;line-height:1.55">
<div style="max-width:600px;margin:0 auto;padding:24px 16px">
<div style="font-weight:800;font-size:20px;letter-spacing:-.01em;margin:0 0 14px">741 Studio</div>
<div style="background:#fff;border-radius:14px;padding:26px 26px 10px">{body_html(lines, lang)}</div>
<div style="font-size:12px;color:#888;margin:14px 4px">741 Studio · clients.741.studio</div></div></body></html>'''

cards = []
for f, client, to, lang, status in MAILS:
    t = open(os.path.join(HERE, f + ".txt"), encoding="utf-8").read().strip().splitlines()
    subject = re.sub(r"^(Betreff|Subject):\s*", "", t[0]); lines = t[2:]
    h = mail_html(subject, lines, lang)
    open(os.path.join(HERE, f + ".html"), "w", encoding="utf-8").write(h)
    json.dump({"client": client, "to": to, "subject": subject, "lang": lang, "status": status, "html_file": f + ".html", "text_file": f + ".txt"},
              open(os.path.join(HERE, f + ".meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    badge = "#1f7a3a" if status == "ready" else "#b45309"
    cards.append(f'''<section style="margin:0 0 34px"><div style="font:600 13px Arial;color:#555;margin:0 0 6px">
<b style="font-size:16px;color:#111">{html.escape(client)}</b> · <span style="color:{badge}">{html.escape(status)}</span><br>
From: 741 Studio &lt;portal@741.studio&gt; · To: {html.escape(to)} · Reply-To + BCC: martin@741.studio<br>Subject: <b>{html.escape(subject)}</b></div>
<iframe srcdoc="{html.escape(h, quote=True)}" style="width:100%;max-width:660px;height:760px;border:1px solid #ddd;border-radius:12px;background:#f6f3ea"></iframe></section>''')
open(os.path.join(HERE, "preview.html"), "w", encoding="utf-8").write(
    '<!doctype html><html><head><meta charset="utf-8"><title>Explainer mails preview</title></head><body style="margin:0;padding:24px;background:#eee;font-family:Arial">'
    '<h1 style="font:800 24px Arial">Explainer mails · preview 13.10. · nothing sent</h1>' + "".join(cards) + "</body></html>")
print("rendered", len(cards))
