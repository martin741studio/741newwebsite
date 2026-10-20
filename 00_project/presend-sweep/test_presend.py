import importlib.util, os
spec = importlib.util.spec_from_file_location('h', os.path.join(os.path.dirname(__file__), 'presend_sweep_hook.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
BLOCK = {
 'offen_bei_dir': "Alles geprüft.\n\n**Offen bei dir:**\n- Nachricht senden\n- Konto anlegen",
 'offene_punkte': "Ergebnis steht.\nOffene Punkte:\n1. Replay\n2. Löschen",
 'closing_q': "Zap läuft, Tests grün.\n\nSoll ich als Nächstes die Fehlläufe auslesen?",
 'wenn_du_willst': "Fertig mit dem Plan.\nWenn du willst, baue ich das jetzt.",
 'steps_list': "Status ok.\n1. Du musst dich bei Zapier einloggen.\n2. Du klickst auf Publish.\n3. Du löschst die Tests.",
 'en_heading': "Done.\n\nOpen items:\n- send message",
 'sag_bescheid': "Alles drin. Sag mir Bescheid, wenn ich weitermachen soll.",
}
PASS = {
 'plain_report': "Zap v2 ist live. Beide Tests liefen durch. Tag 15229620 hängt am Kontakt.",
 'message_draft': "Fertig.\n\n```text\nHey Marcel,\n\nSoll ich dir die Liste schicken? Sag mir kurz Bescheid.\n\nViele Grüße\n```\n\nCheck 5/5.",
 'fact_status': "Wartet auf Marcels Antwort zur Mail-Frage. Nachtrag startet danach.",
 'empty': "",
 'rule_quote': "Die Regel steht in CLAUDE.md. Offene Fragen werden Karten.",
}
bad = 0
for k, v in BLOCK.items():
    r = h.check(v); ok = bool(r); bad += (not ok); print('BLOCK' if ok else 'MISS ', k, r)
for k, v in PASS.items():
    r = h.check(v); ok = not r; bad += (not ok); print('PASS ' if ok else 'FALSE', k, r)
print('FAILED' if bad else 'ALL OK', bad)
