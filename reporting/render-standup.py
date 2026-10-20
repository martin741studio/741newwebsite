#!/usr/bin/env python3
"""Rendert den Daily Client Standup.
Nutzung:  select daily_standup();  -> JSON  ->  python3 render-standup.py < brief.json
"""
import sys, json, datetime

d = json.load(sys.stdin)
if isinstance(d, dict): d = d.get("brief", [])
heute = datetime.date.today().strftime("%d.%m.%Y")
W = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"][datetime.date.today().weekday()]

out = []
out.append("═" * 62)
out.append(f"  741 · DAILY CLIENT STANDUP — {W}, {heute}")
out.append("═" * 62)

blocker_gesamt, delegierbar, nachfassen = [], 0, []

for c in d:
    name, mode = c["name"], c["mode"]
    prog = c.get("woche")
    kopf = f"▓ {name}"
    if mode == "program":
        kopf += f"  ·  Woche {prog}" if prog else "  ·  NOCH NICHT GESTARTET"
    else:
        kopf += "  ·  Report-Kunde"
    out.append("")
    out.append(kopf)
    out.append("-" * 62)

    # Blocker zuerst
    zg = c.get("zugaenge_offen") or []
    if zg:
        out.append(f"  🔴 BLOCKER — Zugänge fehlen ({len(zg)}): " + ", ".join(zg))
        blocker_gesamt.append((name, len(zg)))
    if c.get("hilfe_angefragt"):
        out.append(f"  🟠 Kunde hat {c['hilfe_angefragt']}× Hilfe angefragt → antworten")
        nachfassen.append(f"{name}: Hilfe-Anfrage beantworten")
    if c.get("ungelesen"):
        out.append(f"  💬 {c['ungelesen']} ungelesene Kundennachricht(en)")
        nachfassen.append(f"{name}: Nachricht beantworten")
    if c.get("ueberfaellig"):
        out.append(f"  ⏰ {c['ueberfaellig']} überfällige Aufgaben aus Vorwochen")

    # Onboarding
    if c.get("ob_gesamt"):
        f_, g_ = c["ob_fertig"], c["ob_gesamt"]
        bar = "█" * f_ + "░" * (g_ - f_)
        nxt = f"  → nächster: {c['ob_naechster']}" if c.get("ob_naechster") else "  ✓ komplett"
        out.append(f"  Onboarding: {bar} {f_}/{g_}{nxt}")

    # Heute zu tun
    t741 = c.get("heute_741") or []
    tk = c.get("heute_kunde") or []
    if t741:
        out.append(f"  ▸ WIR ({len(t741)}) — delegierbar:")
        for t in t741[:6]:
            out.append(f"      □ {t}")
        if len(t741) > 6: out.append(f"      … +{len(t741)-6} weitere")
        delegierbar += len(t741)
    if tk:
        out.append(f"  ▸ KUNDE ({len(tk)}) — nachfassen:")
        for t in tk[:4]:
            out.append(f"      ○ {t}")

    # Programm-Klarheit
    pr = c.get("pruefen") or []
    if pr:
        out.append("  ⚠️  Zu klären:")
        for p in pr:
            out.append(f"      • {p}")

    la = c.get("letzte_aktivitaet")
    out.append(f"  Letzte Aktivität: {la or '— keine —'}")

out.append("")
out.append("═" * 62)
out.append("  TAGESFOKUS")
out.append("═" * 62)
if blocker_gesamt:
    out.append("  1) Zugänge freischalten lassen (blockiert die Arbeit):")
    for n, k in sorted(blocker_gesamt, key=lambda x: -x[1]):
        out.append(f"       · {n} — {k} offen")
if nachfassen:
    out.append("  2) Antworten/Nachfassen:")
    for n in nachfassen:
        out.append(f"       · {n}")
out.append(f"  3) {delegierbar} Aufgaben in dieser Woche bei uns → delegieren/einplanen")
out.append("")
print("\n".join(out))
