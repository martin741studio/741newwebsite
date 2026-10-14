#!/usr/bin/env python3
"""Booking sequence: call time -> prospect time zone, send times, merges and fireAt values.

Usage:
  tz_times.py --start "2026-10-26 16:30" [--tz Asia/Makassar] [--phone +4917...] [--prospect-tz Europe/Berlin]
              [--now "2026-10-14 14:20"] [--out prospects/<slug>/booking/booking.json]

--start  call start as cal.com shows it, in --tz (default Asia/Makassar = Bali, WITA, UTC+8).
--phone  picks the prospect zone from the country code when --prospect-tz is not given.
--now    for tests, in this laptop's zone; default = now.
--out    merges the result into booking.json under "times" (other keys stay).

Timing (Martin 2026-10-14, D7/D8): nothing goes out right after the booking.
  m1 = 24 h before the call (new insight + 5 % example + video)
  m2 = 08:00 in her zone on the call day (insight + success story)
  m3 = 30 min before the call (meeting link + laptop tip)
Rules per message: "slot" = scheduled reminder at fireAt; "now" = the slot is already past or less than
5 min away, Martin sends it from the chat right after the run; "merged_into" = its content goes into another message.
  - call starts before 09:30 her time -> m2 merges into m3 (no 2 messages within 1 hour)
  - m1 "now" and the m2 slot past too -> m2 merges into m1
  - m2 slot past while m1 has a slot -> m2 merges into m3
  - m3 "now" (call in less than 35 min) -> m1 and m2 merge into m3 (one message)
fireAt uses this laptop's offset, because Desktop scheduled tasks run on this laptop.
"""
import argparse, datetime as dt, json, os, sys
from zoneinfo import ZoneInfo

M1_HOURS, M2_LOCAL, M3_MIN, EARLY_CALL, MIN_LEAD_MIN = 24, (8, 0), 30, (9, 30), 5
PREFIX = [('+423', 'Europe/Vaduz'), ('+352', 'Europe/Luxembourg'), ('+351', 'Europe/Lisbon'), ('+49', 'Europe/Berlin'),
          ('+43', 'Europe/Vienna'), ('+41', 'Europe/Zurich'), ('+31', 'Europe/Amsterdam'), ('+32', 'Europe/Brussels'),
          ('+33', 'Europe/Paris'), ('+34', 'Europe/Madrid'), ('+39', 'Europe/Rome'), ('+44', 'Europe/London'),
          ('+45', 'Europe/Copenhagen'), ('+46', 'Europe/Stockholm'), ('+48', 'Europe/Warsaw'), ('+62', 'Asia/Makassar'),
          ('+65', 'Asia/Singapore'), ('+61', 'Australia/Sydney')]
DAYS = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']


def zone_from_phone(phone):
    if not phone: return None
    p = '+' + ''.join(c for c in phone if c.isdigit())
    if phone.strip().startswith('00'): p = '+' + p[3:]
    for pre, z in PREFIX:
        if p.startswith(pre): return z
    return None


def hm(t): return f'{t.hour}:{t.minute:02d}'


def block(t, pz):
    w = t.astimezone(ZoneInfo('Asia/Makassar')); p = t.astimezone(pz)
    return {'wita': f'{DAYS[w.weekday()][:2]} {w:%d.%m.%Y}, {hm(w)} WITA',
            'prospect': f'{DAYS[p.weekday()]}, den {p.day}.{p.month}. um {hm(p)} Uhr',
            'prospect_time': hm(p), 'prospect_date': f'{p.day}.{p.month}.', 'prospect_weekday': DAYS[p.weekday()],
            'prospect_zone_abbr': p.tzname(), 'utc': t.astimezone(dt.timezone.utc).isoformat(timespec='minutes'),
            'fireAt': t.astimezone().isoformat(timespec='seconds')}


def main():
    a = argparse.ArgumentParser(); a.add_argument('--start', required=True); a.add_argument('--tz', default='Asia/Makassar')
    a.add_argument('--phone'); a.add_argument('--prospect-tz'); a.add_argument('--now'); a.add_argument('--out')
    o = a.parse_args()
    start = dt.datetime.fromisoformat(o.start.replace('T', ' ')).replace(tzinfo=ZoneInfo(o.tz))
    pz_name = o.prospect_tz or zone_from_phone(o.phone)
    if not pz_name: sys.exit('No prospect zone: unknown phone prefix. Pass --prospect-tz (e.g. Europe/Berlin).')
    pz = ZoneInfo(pz_name)
    local = dt.datetime.now().astimezone().tzinfo
    now = dt.datetime.fromisoformat(o.now).replace(tzinfo=local) if o.now else dt.datetime.now().astimezone()
    if start <= now: sys.exit(f'Call start is in the past ({start.isoformat()}). Check the booking.')
    sp = start.astimezone(pz)
    t1 = start - dt.timedelta(hours=M1_HOURS)
    t2 = sp.replace(hour=M2_LOCAL[0], minute=M2_LOCAL[1], second=0, microsecond=0)
    t3 = start - dt.timedelta(minutes=M3_MIN)
    lead = now + dt.timedelta(minutes=MIN_LEAD_MIN)
    m = {k: block(t, pz) for k, t in (('m1', t1), ('m2', t2), ('m3', t3))}
    for k, t in (('m1', t1), ('m2', t2), ('m3', t3)):
        m[k].update({'mode': 'slot' if t >= lead else 'now', 'merged_into': None, 'reason': ''})
    early = (sp.hour, sp.minute) < EARLY_CALL
    if early:
        m['m2'].update(mode='merged', merged_into='m3', reason=f'call before {EARLY_CALL[0]}:{EARLY_CALL[1]:02d} her time: m2 goes into m3')
    elif t2 < lead:
        tgt = 'm1' if m['m1']['mode'] == 'now' else 'm3'
        m['m2'].update(mode='merged', merged_into=tgt, reason=f'08:00 slot already past: m2 goes into {tgt}')
    if m['m3']['mode'] == 'now':
        for k in ('m1', 'm2'):
            m[k].update(mode='merged', merged_into='m3', reason='call in less than 35 min: everything goes into one message m3')
    if m['m1']['mode'] == 'now': m['m1']['reason'] = '24 h slot already past: Martin sends m1 right after the run'
    if m['m3']['mode'] == 'now': m['m3']['reason'] = '30-min slot already past: Martin sends m3 right after the run'
    warn = []
    nl = now.astimezone(pz)
    if any(m[k]['mode'] == 'now' for k in m) and not (7 <= nl.hour < 21):
        warn.append(f'now is {hm(nl)} in her zone: a "now" message waits until 07:00 her time')
    if m['m1']['mode'] == 'slot' and not (7 <= t1.astimezone(pz).hour < 21):
        warn.append(f'm1 slot {hm(t1.astimezone(pz))} her time is outside 07:00-21:00 (call outside office hours?)')
    if sp.utcoffset() != now.astimezone(pz).utcoffset():
        warn.append('daylight saving change in her zone between now and the call: times computed with zoneinfo, check the hour in the messages')
    res = {'call': block(start, pz), 'prospect_tz': pz_name, 'source_tz': o.tz, 'hours_to_call': round((start - now).total_seconds() / 3600, 1),
           'computed_at': now.isoformat(timespec='minutes'), 'prospect_now': hm(nl), **m, 'warnings': warn}
    if o.out:
        os.makedirs(os.path.dirname(os.path.abspath(o.out)), exist_ok=True)
        cur = json.load(open(o.out, encoding='utf-8')) if os.path.exists(o.out) else {}
        cur['times'] = res; json.dump(cur, open(o.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
