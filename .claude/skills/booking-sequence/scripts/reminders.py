#!/usr/bin/env python3
"""Booking sequence: build the reminder task definitions from booking.json (times from tz_times.py).

Usage: reminders.py <slug>

Prints {"create": [...], "not_scheduled": [...]}. One object per message whose times.mX.mode is "slot"
(taskId, title, description, fireAt, fireAt_utc, prompt). fireAt_utc = the same moment in UTC, because
list_scheduled_tasks shows fireAt in UTC (Z); compare with that value. "now" and "merged" messages get no task.
Timing (Martin 14.10.): m1 = 24 h before, m2 = 08:00 her time on the call day, m3 = 30 min before.
The prompt comes from assets/reminder-prompt.md; no placeholder may stay open.
"""
import json, os, sys

ROOT = '/Users/martindrendel/741website'
HERE = os.path.dirname(os.path.abspath(__file__))
TPL = open(os.path.join(HERE, '..', 'assets', 'reminder-prompt.md'), encoding='utf-8').read()


def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    slug = sys.argv[1]
    b = json.load(open(os.path.join(ROOT, '00_project', 'prospects', slug, 'booking', 'booking.json'), encoding='utf-8'))
    t = b['times']; c = t['call']; name = b['name']
    line = f"{c['prospect']} {c['prospect_zone_abbr']} ({c['wita']}), {b.get('meet_link') or 'Link folgt'}"
    land = 'DE' if t['prospect_tz'] == 'Europe/Berlin' else t['prospect_tz'].split('/')[-1]
    bali = c['wita'].split(', ')[-1].replace(' WITA', '')
    recheck = (f'Run `python3 {ROOT}/.claude/skills/booking-sequence/scripts/quick_check.py {slug} --recheck`. '
               'If it prints CHANGED lines, add them and the line "Achtung: Die Seite hat sich seit der Prüfung geändert. '
               'Text vor dem Senden prüfen." If it fails, add "Seite nicht erreichbar, Text vor dem Senden prüfen."')
    spec = {
        'm1': dict(n='1', tid=f'{slug}-whatsapp-1-24h', when='24 h before the call', label='24 h vor dem Call', section='## 1 · 24 h vorher',
                   late='If now is less than 3 hours before the call start, add the line "Spät dran: Nachricht 1 nur senden, wenn es noch passt."',
                   recheck=recheck, body=f"Call morgen {c['prospect_time']} Uhr {land} / {bali} Bali. Text liegt bereit."),
        'm2': dict(n='2', tid=f'{slug}-whatsapp-2-morning', when='08:00 her time on the call day', label='Morgen des Termins', section='## 2 · Morgen des Termins',
                   late='If now is less than 30 minutes before the call start, add the line "Spät dran: Nachricht 2 nur senden, wenn es noch passt."',
                   recheck='(no check needed for this message)', body=f"Call heute {c['prospect_time']} Uhr {land} / {bali} Bali. Text liegt bereit."),
        'm3': dict(n='3', tid=f'{slug}-whatsapp-3-30min', when='30 min before the call', label='30 Min vor dem Call', section='## 3 · 30 Minuten vorher',
                   late='If now is less than 5 minutes before the call start, add the line "Der Call beginnt gleich: nur den Link schicken."',
                   recheck='(no check needed for this message)', body='Call in 30 Minuten. Text mit Link liegt bereit.')}
    out, skipped = [], []
    for k, s in spec.items():
        m = t[k]
        if m.get('mode') != 'slot':
            skipped.append({'message': s['n'], 'mode': m.get('mode'), 'reason': m.get('reason')}); continue
        v = {'NAME': name, 'SLUG': slug, 'PHONE': b.get('phone', ''), 'CALL_UTC': c['utc'], 'CALL_LINE': line, 'N': s['n'],
             'SECTION': s['section'], 'LATE_RULE': s['late'], 'RECHECK': s['recheck'],
             'PUSH_TITLE': f"Jetzt WhatsApp {s['n']} an {name} senden", 'PUSH_BODY': s['body']}
        p = TPL
        for key, x in v.items(): p = p.replace('{{' + key + '}}', x)
        if '{{' in p: sys.exit(f"open placeholder in reminder {s['n']}")
        out.append({'taskId': s['tid'], 'title': f"{name}: WhatsApp {s['n']} ({s['label']})",
                    'description': f"Reminds Martin to send WhatsApp message {s['n']} to {name} ({s['when']}); never sends",
                    'fireAt': m['fireAt'], 'fireAt_utc': m['utc'], 'prompt': p})
    print(json.dumps({'create': out, 'not_scheduled': skipped}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
