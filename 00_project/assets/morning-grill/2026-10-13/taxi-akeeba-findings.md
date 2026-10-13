# Taxi Nürnberg: Akeeba download key + spam (read only, 13.10.2026)

Request: Daniel Leibold (partner agency) via Martin. Screenshot: Joomla Update Sites show "The Download Key is missing" for "Admin Tools Professional package" (latest 7.9.3) and "Akeeba Backup Professional for Joomla!" (latest 10.4.0). Daniel: the key was entered in July 26 as "yearly" (75,-). He also asks if Akeeba is the spam protection (900 spam mails in the Zentrale overnight).

## Verified
1. Joomla admin (taxi-nuernberg.de/administrator) is NOT logged in in my Chrome window. I did not enter credentials.
2. Earlier dump of 03.08.2026 (taxi chat scratch, `joomla_status.json`): Admin Tools 7.8.9, Akeeba Backup 10.3.6 installed; both update sites point to the Pro package XML files. Latest versions on Daniel's screenshot are 7.9.3 and 10.4.0, so updates are pending.
3. Daniel's hours sheet (Drive): July 26 "Taxi updates 2 h", "Taxi Malware 15.07: DDOS attack and menu fix, password reset through database 3.5 h". The "Akeeba Plugin 75,- Yearly" line is in his spreadsheet picture, not in the Drive file I could read.
4. Public forms (checked in Chrome, no login):
   • /kontakt/formulare: 3 SP Page Builder forms (Fundsachen, Bestellung Fahraufträge, a third) with captcha_type "default" and NO captcha widget; 1 RSForm complaint form WITH reCAPTCHA.
   • /kontakt: form 1 has a simple question field (captcha_question); form 2 (first name, last name, email, subject, message) has no captcha.
   • /ihretaxizentrale/taxi-aussenwerbung-buchen: SP Page Builder ajax form, honeypot field only.
   • On 03.08. the Joomla invisible reCAPTCHA plugin was disabled; only the RSForm reCAPTCHA plugin was enabled. "default" in SP Page Builder therefore most likely means no captcha (current setting not verified).

## Not verified (needs a login)
• Akeeba subscription status and Download ID (akeeba.com account).
• Whether the key was ever saved in Joomla, and why it is missing now.
• Which form sent the 900 mails (needs 2 to 3 sample mails with full headers).
• Current Admin Tools and Akeeba versions installed.

## What this means
• A missing download key does not switch off the installed plugins. It blocks updates (security rule updates included). Confirm in the Joomla admin.
• Akeeba is not a form spam filter. Admin Tools Pro is the firewall, Akeeba Backup only makes backups.
• The likely spam source is a form without captcha. Not proven.

## Next steps (all need Martin's own login or go)
1. akeeba.com account: check the subscription is active (bought July 26, yearly) and copy the Download ID.
2. Joomla admin > System > Update Sites: open both Pro entries, paste the key, save. Use Martin's real Chrome (Cloudflare blocks automated admin saves). A download key is a licence key: Martin enters it, not the agent.
3. Backup first (Akeeba Backup), then update Admin Tools and Akeeba Backup.
4. Spam: get sample mails, then add a captcha to the forms without one (Joomla reCAPTCHA or Cloudflare Turnstile) and a rate limit in Cloudflare. Each live change needs Martin's go.
