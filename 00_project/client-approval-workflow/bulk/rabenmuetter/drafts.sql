-- Rabenmütter Shop (fbcc70d1-4c56-437c-b5fb-8056e48d3f62): 7 decision cards as DRAFT. Written 13 Oct 2026 by a bulk agent.
-- Status draft = nobody sees them but 741. Martin releases them one by one in the Claude chat. No INSERT was run by the agent.
-- Client: lang de, du-form (portal reports and the 4 live guides use du). Live shop mixes Sie/Ihr/du in marketing text; legal pages use Sie.
-- Not a health client: no HWG check, hwg_checked stays false, risk_class none on all cards. No prices, no invoice talk, no tool names.
--
-- Facts checked on 13 Oct 2026 (sources and dates):
--   Search data = Google Search Console, URL-prefix property https://rabenmuetter-shop.com/, read by the reporting service account.
--     Property data starts 29 Aug 2026. Range used: 29.08.-11.10. (43 days) or 14.09.-11.10. (28 days). 28 days = 50 clicks, 2,816 impressions.
--   E1  366 products (Shopify read): 348 carry the standard text with the typos "Weihnachen" and "kontinuirlich", 346 start with "Es gibt immer, immer einen Anlass".
--       282 product pages had impressions; 265 of them show the standard text (2,998 impressions). 36 pages with >= 20 impressions still show it (1,866 impressions, 21 clicks).
--       20 products have a custom Google title (the batch approved on 04.09.2026, report_feedback rabenmuetter-onpage-2026-09).
--   E2  6 Trauerkarten: only "Traene" has its own text. Ballon, Sternschnuppe, Herz, Stille, Rose carry "Und machmal fehlen einem die Worte..." (typo).
--       "Ballon": 54 impressions, average position 10.4 (29.08.-11.10.). Review on /products/trauerkarte-sternschnuppe: customer took the card for a fold-out card.
--       Picture checked: Ballon = one black balloon on white. "nicht zum Aufklappen" is inferred from the review and "Format: A6 - Postkarte": ask the client to confirm.
--   E3  Homepage: 11 of 50 clicks in 14.09.-11.10. (most of any page). Homepage HTML has no link to any /blogs/news/<article>, only the menu link /blogs/news.
--   E4  Menu check 13.10.: sub-items of "Postkarten" = 12, "Trauerkarten" is the last. Volume "trauerkarte schreiben" 90,500 (DataForSEO 30.08., in the 30.08. site-tree report).
--       Client approved block "5 Kategorien & Navigation" on 30.08. (report_feedback).
--   E5  /blogs/news: <title> "News - Rabenmütter Shop", H1 "News", no meta description. Menu item says "Ratgeber".
--   E6  "sprüche zur geburt" 27,100, "sprüche zur hochzeit" 40,500 (30.08. site-tree report). Collection "Geburt" = 4 products, no intro. No product mentions "Hochzeit".
--       4 guides live: trauerkarte-schreiben, trauersprueche, glueckwuensche-zum-geburtstag (15.09.), muttertagssprueche (10.10.).
--   E7  Homepage H2 "Let customers speak for us" (English default). Product pages show "Customer Reviews", "Write a review".
-- Dropped candidates and reasons: see queue.md.
-- Approver: client_approval_settings has no row. Row below uses approver_user_id NULL on purpose. The client login exists in profiles:
--   user_id 8f1dff6f-4c72-476f-96ad-2c4a1b81389e (Franziska Poerschmann). The main session can set it with an UPDATE after Martin agrees.
--   Until then the client cannot decide.

begin;

insert into public.client_approval_settings (client_id, approver_user_id, approver_name, auto_approve_consent, health_client)
values ('fbcc70d1-4c56-437c-b5fb-8056e48d3f62', null, 'Franziska Poerschmann', false, false)
on conflict (client_id) do nothing;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class, status)
values
 ('fbcc70d1-4c56-437c-b5fb-8056e48d3f62','E1','other','Text','website',
  'Standardtext auf den Produktseiten: eigene Texte für die meistgesehenen Karten?',
  '**36 Karten wurden seit Ende August mindestens 20-mal bei Google angezeigt** und tragen noch den Standardtext mit zwei Tippfehlern („Weihnachen“, „kontinuirlich“).',
  'Google-Suchdaten 29.08. bis 11.10. und Abgleich aller 366 Produktseiten', '2026-10-11',
  '[{"key": "A", "value": "Nur die Tippfehler korrigieren", "label": "betrifft 348 Seiten, der Text bleibt sonst, wie er ist"}, {"key": "B", "value": "Tippfehler korrigieren und für die 36 Karten mit den meisten Anzeigen eigene Texte schreiben", "label": "du siehst jeden Text, bevor er live geht"}, {"key": "C", "value": "Alles lassen, wie es ist", "label": "der Standardtext bleibt auf allen Seiten"}]'::jsonb, 'B',
  null, null, false, null, '{}'::jsonb,
  'Der Standardtext beginnt mit „Es gibt immer, immer einen Anlass für eine Postkarte …“ und steht auf 348 von 366 Produktseiten. Die Sammelseite „Weihnachten“ hat denselben Text mit denselben Tippfehlern.',
  null,
  'none', 'draft'),

 ('fbcc70d1-4c56-437c-b5fb-8056e48d3f62','E2','text','Text','website',
  'Beschreibung der Trauerkarte „Ballon“ (Muster für fünf Karten)',
  '**Nur eine von sechs Trauerkarten hat einen eigenen Text**, obwohl „Ballon“ seit Ende August 54-mal bei Google angezeigt wurde (im Schnitt auf Platz 10).',
  'Google-Suchdaten 29.08. bis 11.10. und Abgleich der sechs Trauerkarten-Seiten', '2026-10-11',
  '[{"key": "A", "value": "Und manchmal fehlen einem die Worte … Die {kw} zeigt einen einzelnen schwarzen Luftballon auf weißem Grund. Still, zurückhaltend, ohne Kitsch. Für den Moment, in dem man einem lieben Menschen nahe sein möchte und nicht weiß, was man schreiben soll. Format: A6-Postkarte mit Umschlag, nicht zum Aufklappen.", "label": "im Ton der Karte „Träne“, die schon online ist"}, {"key": "B", "value": "Die {kw}: ein schwarzer Luftballon, mehr nicht. Eine stille Karte für den Moment, in dem Worte fehlen. A6-Postkarte mit Umschlag, nicht zum Aufklappen.", "label": "kurz"}, {"key": "C", "value": "Und manchmal fehlen einem die Worte … {kw}. Format: A6-Postkarte (nicht zum Aufklappen). Ausstattung: Bilderdruck, matt. Mit Umschlag.", "label": "kleinste Änderung: Tippfehler korrigieren, Hinweis ergänzen"}]'::jsonb, 'A',
  'Und machmal fehlen einem die Worte... Format: A6 - Postkarte Ausstattung: Bilderdruck, matt Mit Umschlag', 'Trauerkarte „Ballon“', true, 'Produktname, Adresse der Seite und Google-Titel ändert nur 741.', '{"page": "/products/trauerkarte-ballon"}'::jsonb,
  'Du entscheidest hier für „Ballon“. Dasselbe Muster gilt dann für „Sternschnuppe“, „Herz“, „Stille“ und „Rose“, jeder Text wird auf die Karte angepasst. Eine Kundin hielt „Sternschnuppe“ für eine Klappkarte, darum steht in jeder Variante, dass es eine Postkarte mit Umschlag ist. „Nicht zum Aufklappen“ haben wir aus ihrer Bewertung und dem Eintrag „A6-Postkarte“ abgeleitet. Stimmt das?',
  'Das Schloss bleibt stehen, weil Menschen genau nach dieser Karte suchen. Den Text darum herum wählst du.',
  'none', 'draft'),

 ('fbcc70d1-4c56-437c-b5fb-8056e48d3f62','E3','other','Startseite','website',
  'Startseite: Links zu den vier Ratgebern',
  '**Die Startseite hat die meisten Google-Klicks (11 von 50 in 28 Tagen)**, verlinkt aber nicht direkt auf einen der vier Ratgeber.',
  'Google-Suchdaten 14.09. bis 11.10. und Abgleich der Startseite', '2026-10-11',
  '[{"key": "A", "value": "Ein Satz mit zwei Links unter den Trauerkarten", "label": "zum Beispiel: „Unsicher, was du schreiben sollst? Hier findest du Hilfe: Trauerkarte schreiben und Trauersprüche.“"}, {"key": "B", "value": "Neuer Abschnitt „Ratgeber“ mit allen vier Ratgebern", "label": "mit Bild und Titel, unter den Postkarten; die Startseite bekommt einen neuen Abschnitt"}, {"key": "C", "value": "Nur über das Menü", "label": "wie jetzt: der Menüpunkt „Ratgeber“ ist der einzige Weg"}]'::jsonb, 'A',
  null, null, false, null, '{}'::jsonb,
  'Die vier Ratgeber sind „Trauerkarte schreiben“, „Trauersprüche“, „Glückwünsche zum Geburtstag“ und „Muttertagssprüche“.',
  null,
  'none', 'draft'),

 ('fbcc70d1-4c56-437c-b5fb-8056e48d3f62','E4','other','Menü','website',
  'Menü: Wo steht „Trauerkarten“?',
  '**„trauerkarte schreiben“ wird 90.500-mal im Monat gesucht**, doch „Trauerkarten“ steht im Menü als letzter von zwölf Punkten unter „Postkarten“.',
  'Google-Suchdaten (Stand 30.08.) und Abgleich des Shop-Menüs (13.10.)', '2026-08-30',
  '[{"key": "A", "value": "Eigener Menüpunkt „Trauerkarten“ neben „Postkarten“", "label": "darunter: alle Trauerkarten, Trauerkarte schreiben, Trauersprüche"}, {"key": "B", "value": "„Trauerkarten“ bleibt unter „Postkarten“ und steht dort ganz oben", "label": "direkt hinter „Alle“"}, {"key": "C", "value": "Das Menü bleibt, wie es ist", "label": "„Trauerkarten“ bleibt der letzte Punkt unter „Postkarten“"}]'::jsonb, 'A',
  null, null, false, null, '{}'::jsonb,
  'Die Ordnung nach Anlass und Motiv hast du am 30.08. freigegeben. Diese Frage klärt nur die Stelle für Trauerkarten.',
  null,
  'none', 'draft'),

 ('fbcc70d1-4c56-437c-b5fb-8056e48d3f62','E5','text','Text','website',
  'Name der Ratgeber-Seite',
  '**Im Menü heißt der Punkt „Ratgeber“, die Seite dahinter heißt „News“** und hat keine Beschreibung für Google.',
  'Abgleich von Menü und Seite im Shop', '2026-10-13',
  '[{"key": "A", "value": "Ratgeber: die richtigen Worte für deine Karte", "label": "Überschrift und Google-Titel"}, {"key": "B", "value": "Ratgeber", "label": "kurz, wie im Menü"}, {"key": "C", "value": "News", "label": "bleibt wie bisher"}]'::jsonb, 'A',
  'News', null, false, null, '{"page": "/blogs/news"}'::jsonb,
  'Die Adresse der Seite bleibt gleich. Dazu schreiben wir eine kurze Beschreibung für Google.',
  null,
  'none', 'draft'),

 ('fbcc70d1-4c56-437c-b5fb-8056e48d3f62','E6','node','Seitenbaum','website',
  'Welcher Ratgeber kommt als Nächstes?',
  '**„sprüche zur geburt“ wird 27.100-mal im Monat gesucht**, und für die Kategorie „Geburt“ gibt es noch keinen Ratgeber.',
  'Google-Suchdaten (Stand 30.08.) und Abgleich der Kategorien im Shop', '2026-08-30',
  '[{"key": "A", "value": "Sprüche zur Geburt", "label": "27.100 Suchen im Monat; die Kategorie „Geburt“ hat 4 Karten"}, {"key": "B", "value": "Sprüche zur Hochzeit", "label": "40.500 Suchen im Monat; im Shop gibt es bisher keine Hochzeitskarte"}, {"key": "C", "value": "Noch kein neuer Ratgeber", "label": "wir messen zuerst, wie die vier vorhandenen laufen"}]'::jsonb, 'A',
  null, null, false, null, '{"node": "/blogs/news/ (neuer Ratgeber)", "node_kind": "Wissen / Ratgeber"}'::jsonb,
  'Der Text entsteht erst nach deiner Wahl. Du siehst ihn als Entwurf, bevor etwas live geht.',
  null,
  'none', 'draft'),

 ('fbcc70d1-4c56-437c-b5fb-8056e48d3f62','E7','text','Text','website',
  'Überschrift über den Kundenstimmen',
  '**Über den Kundenstimmen auf der Startseite steht noch der englische Standardtext „Let customers speak for us“.**',
  'Abgleich der Startseite im Shop', '2026-10-13',
  '[{"key": "A", "value": "Das sagen unsere Kundinnen und Kunden", "label": "klar und freundlich"}, {"key": "B", "value": "Stimmen zu unseren Karten", "label": "kürzer"}, {"key": "C", "value": "Let customers speak for us", "label": "bleibt auf Englisch"}]'::jsonb, 'A',
  'Let customers speak for us', null, false, null, '{"page": "/"}'::jsonb,
  'Auf den Produktseiten stehen im Bewertungsbereich ebenfalls englische Wörter („Customer Reviews“, „Write a review“). Das ziehen wir mit um.',
  null,
  'none', 'draft');

commit;
