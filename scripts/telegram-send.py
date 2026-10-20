#!/usr/bin/env python3
# Sendet Bilder als Telegram-Alben (max 10/Album) an den 741-Bot-Chat.
# Aufruf: python3 telegram-send.py <intro-text> <file1> [file2 ...]
import sys, os, json, subprocess

ENV="/Users/martindrendel/741website/.secrets/telegram-741.env"
tok=chat=None
for line in open(ENV):
    line=line.strip()
    if line.startswith("TELEGRAM_BOT_TOKEN="): tok=line.split("=",1)[1]
    if line.startswith("TELEGRAM_CHAT_ID="):   chat=line.split("=",1)[1]

intro=sys.argv[1]; files=sys.argv[2:]
API=f"https://api.telegram.org/bot{tok}"

# Intro-Nachricht
subprocess.run(["curl","-s","-X","POST",f"{API}/sendMessage",
  "-d",f"chat_id={chat}","--data-urlencode",f"text={intro}"],
  stdout=subprocess.DEVNULL)

def cap(path):
    b=os.path.basename(path).rsplit(".",1)[0]
    slug,_,lang=b.rpartition("_")
    names={"laserstein":"Bernd Laserstein","schlirf":"Veronika Schlirf","kraft":"Physiotherapie Kraft",
      "abel":"Maria Abel","balihealing":"Bali Healing","reset":"Reset Stuttgart","boehme":"Sven Böhme",
      "marita":"Marita Biel","everitt":"Angelina Everitt","lengauer":"Astrid Lengauer","hotelalpi":"Hotel Alpi",
      "bamberger":"Werbeagentur Bamberger","mediaberater":"Die Mediaberater","doerfler":"Dennis Dörfler"}
    return f"{names.get(slug,slug)} ({lang.upper()})"

ok=0
for i in range(0,len(files),10):
    chunk=files[i:i+10]
    media=[]; forms=[]
    for j,f in enumerate(chunk):
        key=f"f{j}"
        media.append({"type":"photo","media":f"attach://{key}","caption":cap(f)})
        forms+= ["-F",f"{key}=@{f}"]
    cmd=["curl","-s","-X","POST",f"{API}/sendMediaGroup","-F",f"chat_id={chat}",
         "-F","media="+json.dumps(media)]+forms
    r=subprocess.run(cmd,capture_output=True,text=True)
    try:
        j=json.loads(r.stdout); good=j.get("ok")
        n=len(j.get("result",[])) if good else 0
        ok+=n
        print(f"group {i//10+1}: ok={good} sent={n}"+("" if good else f" err={j.get('description')}"))
    except Exception as e:
        print("group",i//10+1,"parse-fail",r.stdout[:200])
print(f"\n{ok}/{len(files)} photos sent")
