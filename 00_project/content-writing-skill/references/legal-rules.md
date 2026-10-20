# Legal rules for copy (HWG health, BRAO and UWG law)

Not legal advice. Grey areas go to Martin, with the sentence and the reason. The script `check_legal.py` reads `legal-terms.json`. Block hits fail the gate. Review hits are for the human check. Sources: memory `hwg-fallstudien-guideline`, `program-deliverable-rules` (rule 2), CRO rule 10 and L8/L9, the pool flags, `behandler-seite` rule 2 and 3.

## HWG mode (health: Heilpraktiker, Ärzte, Therapeuten, Physio, Coaches in health)

- LR1 IF the copy promises healing, a cure, a guaranteed result, a result time, or a result tied to a condition THEN cut it. Allowed: situations, experience, process, qualifications, service facts. (§ 3 HWG)
- LR2 IF the copy says what a method does THEN use "kann", "Ziel", "unterstützen", "wird in der Fachliteratur diskutiert", "ich prüfe individuell". The script lists sentences with "hilft, wirkt, lindert, verbessert" and no softener.
- LR3 IF a before/after story, a case with a result, or a patient story with healing appears THEN rewrite it as personal motivation. Never with treatment result, even when the client has it on the live page. (§ 11 HWG, `behandler-seite`)
- LR4 IF fear is used (Angst-Wörter, "gefährlich", "Lebensgefahr") THEN cut it. (L8)
- LR5 IF an illness named in § 12 HWG Anlage is advertised to the public THEN do not advertise it. The script lists disease words for review. Migräne and Verspannung are not on the list (memory). Grey areas: Martin, or a medical-law specialist. (§ 12 HWG)
- LR6 IF reviews are used THEN only experience content, first name and source, text unchanged. Photo or full name only with consent (DSGVO, KUG). (L9)
- LR7 Mandatory notice box on every health page: "ersetzt keine ärztliche Diagnose; Ergebnisse individuell" and for non-recognised methods "wissenschaftlich umstritten / schulmedizinisch nicht allgemein anerkannt". The script checks the text "ersetzt keine ärztliche Diagnose".
- LR8 IF the target group is named THEN the sentence is harmonious: name the focus, then "genauso bist du hier richtig, wenn …". Never "am liebsten Frauen" or "nur für".

## BRAO / UWG mode (law firms)

- LR10 No result promise: no "Straffreiheit", "Strafe vermeiden", "gewinnen", "Erfolgsquote". (§ 43b BRAO, § 6 BORA, UWG)
- LR11 No superlative and no "Spezialist", "Experte", "Expertise", "führend", "beste", "Exzellenz", "einzigartig", "hart in der Sache".
- LR12 IF "Fachanwalt/Fachanwältin" appears THEN the Kammer title must be proven in the claim list (type `credential`). A Fachanwaltslehrgang is not the title. Never "Fachanwalt für Strafrecht" without proof. Write "Schwerpunkt" or "Interessenschwerpunkt" only with proof, and with the client's exact wording.
- LR13 No "kostenlos", "gratis", "Festpreis" unless true and stated with the exact terms. Price claims only with the RVG basis or the agreed model from the client.
- LR14 Client quotes only about communication and way of working. Cut result parts with [...]. Case examples only anonymised and with consent. Confidentiality: the CTA asks for a topic, not for case details. (§ 203 StGB)
- LR15 Practice areas the client does not prove stay out.
- LR16 No fear wording ("Albtraum", "Ruin", "Haft droht").

- LR17 (research 2026-10-11, second-hand, check the official text before relying on it) § 7 BORA treats "Spezialist", "Spezialgebiet" and "Experte" as qualifying terms. They need proven theoretical knowledge and substantial practical work in the field, and the lawyer carries the burden of proof (BGH, 24.07.2014, I ZR 53/13). The Satzungsversammlung changed §§ 6, 8 and 10 BORA on 26.05.2025. The new § 6 refers to UWG limits and asks for the client's express consent before advertising with clients or cases. No source found on "beste" and similar superlatives: stay with the ban until a source says otherwise.

## Mode "none" (other trades)

Result claims are allowed when the dataset backs them with real data (CRO rule 10). Garantie only with the exact terms.

## Process

1. The G2 script runs on every draft and after the cleanse.
2. Review hits go into the gate report as a list. Martin decides on grey areas at checkpoint 2.
3. The reviewer subagent checks the notice box and the title proof.
4. A new rule from a client or from Martin goes into this file and into `legal-terms.json` in the same edit.
