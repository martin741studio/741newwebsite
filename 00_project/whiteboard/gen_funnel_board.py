import json
FX, FW = 40, 2400
items = []   # frames + cards
harrows = [] # (x1,x2,yc,color)
varrows = [] # (x,y1,y2,color)

def frame(y, h, color, title):
    items.append(dict(type='frame', x=FX, y=y, w=FW, h=h, color=color, content=title))

def row(y, h, w, gap, cards, x0=80):
    pos = []
    for i, (color, text) in enumerate(cards):
        x = x0 + i*(w+gap)
        items.append(dict(type='card', x=x, y=y, w=w, h=h, color=color, content=text))
        pos.append((x, y, w, h))
    for i in range(len(pos)-1):
        x1 = pos[i][0]+pos[i][2]+6; x2 = pos[i+1][0]-6
        harrows.append((x1, x2, y+h//2, 'gray'))
    return pos

# ---- Frame 1: Ist
frame(40, 340, 'gray', '1  Ist-Zustand (Stand 06.10.2026): von der Ad bis zum Setter-Call')
ist = row(130, 190, 270, 70, [
 ('blue',   '1  META-AD\n8 aktive Ads (Seite "Institut Michael Ehlers")\nVersprechen: kostenloses Training, in 30 Tagen zum Kommunikations-Profi'),
 ('red',    '2  SEITE /sichtbarkeit-neu\nVideo + Button "Kostenloses persönliches Gespräch buchen"\nBruch: Ad sagt Training, Seite sagt Gespräch'),
 ('orange', '3  KALENDER /sichtbarkeit-termin\nCalendly, direkt eingebettet\nGanzer Monat offen: lange Wartezeit'),
 ('red',    '4  FORMULAR\nName, E-Mail, Telefon\nKeine Fragen, keine Qualifizierung'),
 ('yellow', '5  ERINNERUNGEN (alles manuell)\nBestätigungsmail von Calendly\nWhatsApp 24 h vorher: Insights\nMorgens oder 1 h vorher\n15 min vorher: Link'),
 ('red',    '6  SETTER-CALL\n80 bis 85 % erscheinen nicht\nNormalwert: ca. 60 %'),
])

# ---- Frame 2: Soll
frame(420, 440, 'green', '2  Soll-Zustand: mit den No-Show-Maßnahmen')
soll = row(510, 190, 270, 70, [
 ('green',  '1  META-AD\nVersprechen passt zur Seite\nz. B. "Kostenloses Gespräch" statt "Training"'),
 ('green',  '2  SEITE\nGleiches Versprechen wie die Ad\nVideo bleibt\nOptional: zwei Fragen vor dem Kalender'),
 ('green',  '3  KALENDER\nBuchbar nur 48 bis 72 h im Voraus\nKurze Wartezeit = mehr Shows'),
 ('green',  '4  FORMULAR\n3 Pflichtfragen: Situation, Ziel, Zeitpunkt\nWer sich Mühe gibt, erscheint'),
 ('purple', '5  BESTÄTIGUNGSSEITE (neu)\nVideo von Michael, 1 bis 2 min\n"Das bringst du mit"\nHinweis auf die WhatsApp vom Setter'),
 ('yellow', '6  SEQUENZ (siehe Frame 3)\nFrage 5 min nach Buchung\nInsights 24 h vorher\n2 Erinnerungen am Termintag\n15 min vorher: Link\nJede Nachricht mit Umbuchungslink'),
 ('green',  '7  SETTER-CALL\nZiel (Schätzung): erst 40 %, später ca. 60 % Show-Rate'),
])
# no-show fallback under step 7
nx = soll[6][0]
items.append(dict(type='card', x=nx-300, y=750, w=570, h=80, color='orange',
  content='NO-SHOW: innerhalb von 10 min Nachricht mit 2 neuen Terminen. Keine Antwort auf die 24-h-Nachricht: kurzer Anruf am Morgen.'))
varrows.append((nx+soll[6][2]//2, 510+190+6, 750-6, 'gray'))

# ---- Frame 3: Sequenz
frame(900, 430, 'yellow', '3  Erinnerungs-Sequenz: von der Buchung bis zum Gespräch (Sender: Setter)')
seq = row(990, 190, 270, 70, [
 ('white',  'SOFORT\nBestätigungsmail + Bestätigungsseite\nUmbuchungslink im Text'),
 ('yellow', '+5 MIN  WhatsApp\nKurze Frage: Was ist die eine Situation, in der du mehr Wirkung willst?\nZiel: Antwort bekommen'),
 ('green',  '24 H VORHER  WhatsApp\nInsights zu den Angaben des Leads\nStärkster Hebel. Bleibt.\nZiel: "Passt der Termin noch?"'),
 ('yellow', 'TERMINTAG MORGENS\nKurze Erinnerung\nVoice-Note von Michael (30 bis 40 s, nicht personalisiert)'),
 ('yellow', '1 H VORHER  WhatsApp\nKurze Erinnerung\nFrage: Bist du dabei? Sonst hier umbuchen'),
 ('blue',   '15 MIN VORHER  WhatsApp\nLink zum Call\nKein weiterer Text'),
 ('red',    '+10 MIN NACH TERMIN\nNur bei No-Show\nWhatsApp mit 2 neuen Terminen'),
])
fx = seq[2][0]
items.append(dict(type='card', x=fx, y=1210, w=270+70+270, h=80, color='orange',
  content='Keine Antwort auf die 24-h-Nachricht? Kurzer Anruf am Terminmorgen.'))
varrows.append((fx+135, 990+190+6, 1210-6, 'gray'))

# ---- Frame 4: Zugänge + Entscheidungen
frame(1370, 440, 'blue', '4  Zugänge und Entscheidungen')
row(1460, 110, 340, 40, [
 ('blue', 'ZUGANG  Calendly\nNötig zum Start: Show-Rate, Fragen, Fenster, Weiterleitung'),
 ('blue', 'ZUGANG  Framer (meandyou.de)\nSeite angleichen, Bestätigungsseite einbinden'),
 ('blue', 'ZUGANG  Meta Werbeanzeigenmanager\nAds anpassen, qualifizierte Buchungen melden'),
 ('gray', 'ZUGANG  Superchat\nWhatsApp-Versand. Später.'),
 ('gray', 'ZUGANG  Close (CRM)\nStatus erschienen / nicht erschienen. Später.'),
 ('gray', 'ZUGANG  Wistia\nNur optional, fürs Video'),
])
harrows[:] = [a for a in harrows if not (1460 <= a[2] <= 1600)]  # no arrows in this row
row(1640, 110, 340, 40, [
 ('orange', 'ENTSCHEIDUNG\nWer verschickt die Nachrichten?'),
 ('orange', 'ENTSCHEIDUNG (Michael)\nKaution oder kleiner Betrag bei Buchung: ja / nein?'),
 ('orange', 'ENTSCHEIDUNG (Michael)\nWer filmt das Video für die Bestätigungsseite?'),
 ('orange', 'ENTSCHEIDUNG\nSequenz erst manuell, dann automatisieren?'),
])
harrows[:] = [a for a in harrows if not (1640 <= a[2] <= 1780)]

def q(s): return "$q$" + s + "$q$"
vals = ",\n".join(
  f"({q(i['type'])},{i['x']},{i['y']},{i['w']},{i['h']},{q(i['color'])},{q(i['content'])})" for i in items)
harr = ",\n".join(f"({a[0]},{a[1]},{a[2]},{q(a[3])})" for a in harrows)
varr = ",\n".join(f"({a[0]},{a[1]},{a[2]},{q(a[3])})" for a in varrows)
sql = f"""
with b as (
  insert into whiteboards (slug, title) values ('meandyou-funnel', 'me&you: Funnel Ist/Soll (No-Show)') returning id
), ins_items as (
  insert into whiteboard_items (board_id, type, x, y, w, h, color, content, z)
  select b.id, v.t, v.x, v.y, v.w, v.h, v.c, v.txt, case when v.t='frame' then 0 else 10 end
  from b, (values
{vals}
  ) as v(t,x,y,w,h,c,txt)
  returning 1
), ins_h as (
  insert into whiteboard_items (board_id, type, x, y, w, h, color, content, z)
  select b.id, 'draw', a.x1, a.yc-12, a.x2-a.x1, 24, a.c,
    jsonb_build_object('points', jsonb_build_array(jsonb_build_array(0,12), jsonb_build_array(a.x2-a.x1,12), jsonb_build_array(a.x2-a.x1-10,5), jsonb_build_array(a.x2-a.x1,12), jsonb_build_array(a.x2-a.x1-10,19)), 'width', 3)::text, 20
  from b, (values
{harr}
  ) as a(x1,x2,yc,c)
  returning 1
), ins_v as (
  insert into whiteboard_items (board_id, type, x, y, w, h, color, content, z)
  select b.id, 'draw', a.x-12, a.y1, 24, a.y2-a.y1, a.c,
    jsonb_build_object('points', jsonb_build_array(jsonb_build_array(12,0), jsonb_build_array(12,a.y2-a.y1), jsonb_build_array(5,a.y2-a.y1-10), jsonb_build_array(12,a.y2-a.y1), jsonb_build_array(19,a.y2-a.y1-10)), 'width', 3)::text, 20
  from b, (values
{varr}
  ) as a(x,y1,y2,c)
  returning 1
)
select (select count(*) from ins_items) as items, (select count(*) from ins_h) as h_arrows, (select count(*) from ins_v) as v_arrows;
"""
open('board.sql','w').write(sql)
print(len(sql), len(items), len(harrows), len(varrows))

# ---------- static render for check + Drive image ----------
import re, html as H
css = open('../wb.html').read()
m = re.search(r'<style>(.*?)</style>', css, re.S)
base = m.group(1)
SC = {'yellow':'#ffdc4a','blue':'#659df2','green':'#2dc75c','red':'#ff6464','purple':'#8f7fee','orange':'#fe9f4d','gray':'#8a8a7e','black':'#000','white':'#fff'}
out = []
for it in sorted(items, key=lambda i: 0 if i['type']=='frame' else 1):
    if it['type']=='frame':
        out.append(f'<div class="item frame color-{it["color"]}" style="left:{it["x"]}px;top:{it["y"]}px;width:{it["w"]}px;height:{it["h"]}px"><div class="frame-head">{H.escape(it["content"])}</div></div>')
    else:
        out.append(f'<div class="item card color-{it["color"]}" style="left:{it["x"]}px;top:{it["y"]}px;width:{it["w"]}px;height:{it["h"]}px;z-index:10">{H.escape(it["content"])}</div>')
for x1,x2,yc,c in harrows:
    w=x2-x1
    out.append(f'<svg style="position:absolute;left:{x1}px;top:{yc-12}px;z-index:20;overflow:visible" width="{w}" height="24"><path d="M0 12 L{w} 12 L{w-10} 5 L{w} 12 L{w-10} 19" fill="none" stroke="{SC[c]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>')
for x,y1,y2,c in varrows:
    h=y2-y1
    out.append(f'<svg style="position:absolute;left:{x-12}px;top:{y1}px;z-index:20;overflow:visible" width="24" height="{h}"><path d="M12 0 L12 {h} L5 {h-10} L12 {h} L19 {h-10}" fill="none" stroke="{SC[c]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>')
page = f'<!doctype html><html lang="de"><head><meta charset="utf-8"><style>{base}\nhtml,body{{overflow:visible!important;height:auto!important;background:#f2f2ef}} #canvas{{position:relative;width:2480px;height:1850px}}</style></head><body><div id="canvas" style="transition:none">{"".join(out)}</div></body></html>'
open('board-static.html','w').write(page)
print('static ok')

# ---------- icons (lucide-static, ISC license) ----------
import base64, re as _re, os
ICON_MAP = [
 ('1  META-AD','megaphone'),('2  SEITE','panel-top'),('3  KALENDER','calendar-days'),('4  FORMULAR','clipboard-list'),
 ('5  ERINNERUNGEN','bell-ring'),('5  BESTÄTIGUNGSSEITE','video'),('6  SEQUENZ','message-circle'),
 ('6  SETTER-CALL','phone-call'),('7  SETTER-CALL','phone-call'),('NO-SHOW:','user-x'),
 ('SOFORT','mail'),('+5 MIN','message-circle'),('24 H','lightbulb'),('TERMINTAG','mic'),('1 H VORHER','clock'),
 ('15 MIN','link'),('+10 MIN','user-x'),('Keine Antwort','phone-call'),
 ('ZUGANG  Calendly','calendar-days'),('ZUGANG  Framer','panel-top'),('ZUGANG  Meta','megaphone'),
 ('ZUGANG  Superchat','message-circle'),('ZUGANG  Close','contact'),('ZUGANG  Wistia','video'),
 ('ENTSCHEIDUNG\nWer verschickt','send'),('ENTSCHEIDUNG (Michael)\nKaution','wallet'),
 ('ENTSCHEIDUNG (Michael)\nWer filmt','video'),('ENTSCHEIDUNG\nSequenz','settings'),
]
COLOR = {'yellow':'#c99a00','blue':'#2f6fd6','green':'#1f9d4a','red':'#d93a3a','purple':'#6a5acd','orange':'#d9700f','gray':'#5f5f55','white':'#1a1a1a','black':'#1a1a1a'}
def icon_uri(name, color):
    svg = open(f'icons/{name}.svg').read()
    svg = _re.sub(r'<!--.*?-->', '', svg, flags=_re.S)
    svg = _re.sub(r'\s+', ' ', svg).replace('> <','><').replace('" >','">').replace(' />','/>')
    svg = svg.replace('currentColor', color).replace('viewBox="0 0 24 24"', 'viewBox="-4 -4 32 32"')
    svg = _re.sub(r'\s+class="[^"]*"', '', svg, count=1)
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()
S = 40
icons = []
for it in items:
    if it['type'] != 'card': continue
    name = next((n for k, n in ICON_MAP if it['content'].startswith(k)), None)
    if not name: print('NO ICON', it['content'][:30]); continue
    side = it['content'].startswith(('NO-SHOW:','Keine Antwort'))
    icons.append(dict(x=(it['x']-S-8 if side else it['x']), y=(it['y']+16 if side else it['y']-S-8), w=S, h=S, content=icon_uri(name, COLOR[it['color']]), name=name))
isql = "insert into whiteboard_items (board_id, type, x, y, w, h, color, content, z)\nselect b.id, 'image', v.x, v.y, v.w, v.h, 'white', v.c, 15 from whiteboards b, (values\n" + ",\n".join(f"({i['x']},{i['y']},{i['w']},{i['h']},$q${i['content']}$q$)" for i in icons) + "\n) as v(x,y,w,h,c) where b.slug='meandyou-funnel' returning 1;"
open('icons.sql','w').write(isql)
tags = "".join(f'<div class="item image" style="left:{i["x"]}px;top:{i["y"]}px;width:{i["w"]}px;height:{i["h"]}px;z-index:15;background:#fff"><img src="{i["content"]}" style="width:100%;height:100%;display:block"></div>' for i in icons)
pg = open('board-static.html').read().replace('</div></body></html>', tags + '</div></body></html>')
open('board-static.html','w').write(pg)
print('icons', len(icons), len(isql))
