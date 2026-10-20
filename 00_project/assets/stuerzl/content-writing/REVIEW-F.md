# REVIEW-F: ST-40, ST-41, ST-42, ST-33 (read only, 2026-10-11)

Severity: H = fix before approval, M = fix before live, L = small. Quotes stay German. Scripts found no dashes and no links outside slugs.json. ST-41/ST-42 overlap: 7.5 % / 8.4 % of unique 5-word phrases (limit 25 %), so PASS.

## ST-40 Kontakt: VERDICT FIX FIRST
1. H (B) "Wir sind persönlich erreichbar, auch außerhalb der klassischen Bürozeiten." This is an availability promise from the client's marketing list (kosten.txt). The same page says phone "9:30 bis 14:30 Uhr". ST-43 words it more safely. Fix: "Termine und Erstberatungen sind auch außerhalb der Telefonzeiten nach Absprache möglich."
2. M (B) S04 "erreichen Sie uns über unsere Notfall-Rufnummern" has no documented hours. Only the placeholder guards it. Fix: state the numbers as facts, add no "Sie erreichen uns" until hours are known.
3. M (A/D) "Die Erstberatung bieten wir gegen Pauschale an." The source says "üblicherweise eine Pauschale"; ST-31 keeps "üblicherweise". Fix: add "üblicherweise" here and on ST-41/ST-42.
4. M (A) "Auf Wunsch schreiben wir Ihnen zuerst per E-Mail." Source is pool CP-BRD-003, marked needs_client. Fix: placeholder or cut.
5. M (B) "Das gilt für Ihre Anfrage genauso wie für das Mandat." The saved sources are only the texts of § 43a BRAO and § 203 StGB. They do not cover pre-mandate inquiries. Fix: cite a source or write "alles, was uns in Ausübung des Berufs bekannt wird".
6. L (A) "Beide Büros sind gleichrangig." Source is the internal sitetree job (C19). The Source of Truth calls Frankfurt "Stammsitz". Fix: cut.
7. L (C) Four FAQ questions use "ich" ("Was muss ich in der ersten Anfrage angeben?"). Voice is Sie/wir. Fix: use "Sie".
8. L (A) "Plätze 148 und 146": the Source of Truth lists them but does not say they are visitor spaces. Fix: confirm or cut the numbers (also on ST-41).
OK: NAP, phones, e-mail, hours, Munich access match nap.json. Form fields are topic only. Consent text is a placeholder. CTA text is correct.
Scores: intent 85, depth 70, GEO 82, E-E-A-T 62, local 68, technical 90, schema 55, links 72.
Lowest: schema 55 "WebPage + LegalService", no ContactPage type, no ContactPoint per office. E-E-A-T 62: no credential or Kammer line near the form.
Top gaps: (1) no Frankfurt public-transport route and no entrance rule (Untermainkai 26 vs "Post und Empfang" Nr. 23); (2) 5 visible placeholders block launch; (3) no trust line (title, Verschwiegenheit source) next to the form.

## ST-41 Standort Frankfurt: VERDICT FIX FIRST
1. M (A) "In Hessen sitzen die Steuerfahndungsstellen und die Bußgeld- und Strafsachenstellen bei sechs Finanzämtern" and "Das schreibt die hessische Finanzverwaltung selbst." I re-read finanzamt.hessen.de today. It is a data-protection notice: these Finanzämter "verarbeiten" data and are "verantwortlich". It says nothing about seat, completeness, or both units at each office ("bzw."). Fix: "Nach den Datenschutzhinweisen der hessischen Finanzverwaltung sind die Stellen dieser sechs Finanzämter verantwortlich", or check a Finanzamt directory.
2. H (D) S04 "Wobei wir Sie von Frankfurt aus begleiten" lists six services as if office facts. The list differs from ST-42 without a source: Frankfurt has Gutachten and Schulung, no Compliance. Fix: one neutral list on both pages, heading "Unsere Leistungen", until the client answers.
3. M (A) "Thorben Hoppe ... berät seit Juni 2026 an den Standorten Frankfurt am Main und München." Only the live profile ("ab 06/2026"). Not in nap.json or the Source of Truth. ST-40 and ST-42 omit him. Fix: placeholder, or name him on all three pages.
4. M (B) S04 "Wir begleiten Durchsuchungen und Beschlagnahmen" is unconditional. The FAQ says "Ob eine Begleitung vor Ort im Einzelfall möglich ist". Fix: use the hedge in S04.
5. M (D) Pauschale wording as ST-40 no. 3.
6. L (A) S03 shows § 386 Abs. 2 for "ausschließlich eine Steuerstraftat" only and omits Abs. 3 (Haftbefehl). § 388 text drops "zur Zeit der Einleitung" in point 2. Fix: add "in der Regel" or the missing words.
OK: Untermainkai 26, 60329, phone, e-mail, hours, garage, Wilhelm-Leuschner-Straße 23 match nap.json. Old address absent. §§ 386, 388, 399 match the saved texts. Fachanwältin, DAA and CV match the live profile and the Source of Truth.
Scores: intent 82, depth 68, GEO 80, E-E-A-T 72, local 55, technical 85, schema 48, links 85.
Lowest: schema 48 "department" graph for both offices, no areaServed, page not tied to the Frankfurt office. Local 55: one weak local fact, no catchment.
Top gaps: (1) no Einzugsgebiet (5 km round Untermainkai 26, Stadtteile) and no route from Hauptbahnhof/ÖPNV; (2) no Frankfurt court or Staatsanwaltschaft fact, and the Hessen fact is overstated; (3) services and staff unassigned, no photo or office image.

## ST-42 Standort München: VERDICT FIX FIRST
1. H (B, LR12) "Lea Wimmer, Fachanwältin für Steuerrecht" (S02) and "seit 2017 Fachanwältin für Steuerrecht" (S06). Proof is only the live profile. Claim C01 says "Titel nicht von der Kanzlei bestätigt". No Kammer proof. Not in nap.json or the Source of Truth. Fix: written confirmation or BRAK Fachanwaltssuche, else placeholder.
2. H (D) S04 assigns six services, including Compliance and Zollstrafrecht, to Munich without an office source (same issue as ST-41 no. 2).
3. M (A) "Beide beraten und verteidigen Privatpersonen und Unternehmen." The profiles list only Rechtsgebiete, not client groups. Fix: use the profile wording.
4. M (A) "Neben Steuerdelikten kommen oft Begleitdelikte vor." The source card says only "auch bei Begleitdelikten". "oft" is unbacked. Fix: cut "oft".
5. L (A) Dr. Glogger is named as first contact, but the Source of Truth says 50 % Teilzeit, operative for texts and compliance. Fix: client confirms she takes inquiries.
6. L (D) Hoppe's profile says Munich; the page omits him.
7. M Pauschale wording as ST-40 no. 3.
OK: Oberanger 32, 80331, phone, e-mail, hours, access and parking match nap.json (client text, not MVV-checked). "neun Steuerfahndungsstellen" matches the saved LfSt list (9 names). §§ 387, 388, 370 match the saved texts.
Scores: intent 82, depth 66, GEO 82, E-E-A-T 66, local 68, technical 85, schema 48, links 85.
Lowest: schema 48 (same generic graph as ST-41). E-E-A-T 66: two titles unproven.
Top gaps: (1) no Munich catchment (Altstadt, Isarvorstadt, Umland) and no Munich court or StA fact; (2) person titles unproven, no photos (Google profile has 0 photos); (3) no office-specific schema entity and services unassigned.

## ST-33 Aktuelles: VERDICT FIX FIRST
1. M (C) The page has no CTA. The brief names "Zum Ratgeber", but no button or sentence exists. The sibling ST-49 carries "Vertraulich anfragen". Fix: add one primary CTA block or confirm the template does.
2. M (B) The CMS list will show "Neue JUVE-Rankings", "erfolgreiche Gründerin" and "Spezialisierung, Personal Brand". It also shows "Influencer*innen ... Jetzt vor Strafverfolgung schützen!" That title is a protection promise. It is missing from OPEN-FLAGS A1. Fix: add it to the flags and ask for a retitle before the list goes live.
3. L (A) "aktuelle Beiträge": the list runs back to 2024. Fix: "Beiträge und Hinweise".
4. L The /ratgeber/ link depends on ST-34, still a proposal.
OK: no facts to mismatch. Links are in slugs.json.
Scores: intent 60, depth 25, GEO 35, E-E-A-T 45, local 25, technical 70, schema 40, links 60.
Lowest: depth 25 "51 Wörter, nur Einleitung". Local 25: no place, no NAP.
Top gaps: (1) 51 words, no topics, years or categories in the text; (2) no links to services, /steuerstrafrecht/ or /kontakt/, no CTA; (3) no CollectionPage/ItemList schema for the CMS list.

## Cross-page problems
1. Erstberatung: ST-40/41/42 say flat "gegen Pauschale"; ST-31 says "üblicherweise" and "nennen wir Ihnen vor dem Gespräch". Same amount placeholder repeated on four pages.
2. Out-of-hours availability: ST-40 promises it; ST-43 and ST-41/42 only offer appointments. Emergency-number hours still undocumented; ST-18, ST-40 and ST-43 each show the numbers.
3. Services per office differ between ST-41 and ST-42 with no source. This looks like a uniqueness device, not a client fact.
4. Hoppe: ST-41 puts him in both cities; ST-40 and ST-42 omit him; ST-44 links /thorben-hoppe/, which is not in slugs.json (ST-48 is empty).
5. Wimmer's Fachanwalt title (ST-42, ST-44) rests on the live profile only.
6. 10 visible placeholders in running text (ST-40: 5, ST-41: 3, ST-42: 2). Frankfurt address Untermainkai 26 is correct but the GBP and the live site still show the old one until Martin's go; do not publish earlier.
7. Schema: the same generic graph on all four pages, no per-office entity, no hours.
8. ST-41 and ST-42 follow the same section order and the same FAQ "Was tun, wenn die Steuerfahndung in ... vor der Tür steht?". Overlap is under the limit, but this is template-like.
