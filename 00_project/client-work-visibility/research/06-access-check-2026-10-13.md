# 06 — Access check of open "required" grants (13.10.2026)

Read-only check. The agent changed no table, file, setting or account. The agent sent no message.

Source list: Supabase `741-portal`, table `access_grants`, filter `required` and status not in `erteilt`, `geprueft`, `entfaellt`. Result: 12 rows.

Account check: the Search Console users page and the Google Ads account picker both name `741studio18@gmail.com` as the active Chrome account (authuser=1).

## Table

| # | client | platform | portal status + since | finding | evidence (source + date) | proposed action |
|---|---|---|---|---|---|---|
| 1 | Johni Jaya Motor | Google Analytics (GA4) | ausstehend since 2026-08-17 | we have it — tick it | Chrome 13.10.: GA4 account "Google Pages" (296199981), property "JJMotors" (488665039). `741studio18@gmail.com` has the role Administrator. Web stream `https://johnijayamotor.com` shows "Receiving traffic in past 48 hours". The site loads `G-XZCKK6Z6BJ` (curl 13.10.). The reporting-bot does not see this property, because it has access only to the account "741 Clients". | Set to `erteilt`. Separate task for Martin: add `reporting-bot@studio-apis-503306.iam.gserviceaccount.com` as Viewer for reports. |
| 2 | Johni Jaya Motor | Google Business Profile | ausstehend since 2026-08-17 | we have it — tick it | Chrome 13.10.: Business Profile Manager of `741studio18` lists "BENGKEL JOHNI JAYA MOTOR", Jl. Raya Cilincing No.7, status "Verified". The agent did not read the role (owner or manager). | Set to `erteilt`. Martin can check the role in the profile if it is important. |
| 3 | Johni Jaya Motor | Google Search Console | ausstehend since 2026-08-17 | we have it — tick it | Chrome 13.10.: property `https://johnijayamotor.com/`, Users page: "741 Studio (you) 741studio18@gmail.com Owner, Verified". | Set to `erteilt`. Separate task: add the reporting-bot as user (reporting-bot list 13.10. has 5 sites, Johni is not in it). |
| 4 | Maria Brasse | Google Tag Manager | hilfe_angefragt since 2026-09-02 | not needed | The site uses no GTM. curl 13.10.: shuiguru.de loads only `G-8B0M7DXENR`, no GTM ID. Memory `maria-brasse-client.md` (30.09.): GA4 runs through the MU plugin `shuiguru-consent-analytics.php`, without GTM. | Set to `entfaellt`. If GTM becomes necessary, 741 creates the container in its own account. |
| 5 | Naturheilpraxis Daniela Dumann | Google Analytics (GA4) | hilfe_angefragt since 2026-08-28 | we have it — tick it | reporting-bot API 13.10.: property "Naturheilpraxis Daniela Dumann - GA4" (556758063) in account "741 Clients". Memory `dumann-client.md` (30.09.): 741 created the property, ID `G-3NTQVLCFG0`, connected in Wix. | Set to `erteilt`. |
| 6 | Naturheilpraxis Daniela Dumann | Google Search Console | hilfe_angefragt since 2026-08-29 | we have it — tick it | reporting-bot API 13.10.: `https://www.danieladumann.de/` with `siteFullUser`. Memory `dumann-client.md` (30.09.): verification moved to `741studio18@gmail.com`. | Set to `erteilt`. |
| 7 | Naturheilpraxis Daniela Dumann | Google Tag Manager | hilfe_angefragt since 2026-08-29 | not needed | Memory `dumann-client.md` (30.09.): the Wix site sends GA4 through the Wix integration "Google Tag (Basic Consent Mode)". The memory names no GTM container for this site. | Set to `entfaellt`. Ask again only if Ads conversions need GTM. |
| 8 | Praxis Hüwel | Google Tag Manager | hilfe_angefragt since 2026-08-19 | not needed | Portal note (18.08.): "Hüwel hat keinen GTM — 741 richtet den Container ein". Since 06.10. the site is the 741 build on GitHub Pages (memory `huewel-website-live-state.md`). The client cannot give access to a container that does not exist. | Set to `entfaellt` for the client. Side finding: curl 13.10. and a grep of `~/huewel-site` show no GA4 tag and no GTM tag on the new site. The GA4 property gets no data from it. This needs a separate decision and a go from Martin. |
| 9 | Praxis Suriya | Google Tag Manager | hilfe_angefragt since 2026-08-12 | we have it — tick it | Memory `praxis-suriya-client.md` (09.10.): 741 created account "Praxis Suriya" (6381503342), container `GTM-K9MDDN7P`, under `741studio18`. curl 13.10.: suriya-praxis.de loads `GTM-K9MDDN7P`. | Set to `erteilt`. The access lockout of 12.10. affects only Search Console and WordPress, not this container. |
| 10 | STÜRZL Steuerstrafrecht | Google Ads | ausstehend since 2026-10-01 | really open | Goals file `morning-grill-goals.json` (13.10.): blocker "Google Ads access". Memory `anja-stuerzl-client.md` (07.10.): "Offen: … Google Ads". Week-1 file (01.10.): "Google-Ads-Konto: besteht eins?". Chrome 13.10.: the Ads account list of `741studio18` shows no Stürzl account. curl 13.10.: no `AW-` tag on the site. The agent did not read the sub-account list of the manager account 741.Studio (476-158-5143), because Chrome disconnected. | Keep open. Martin asks Linkemann if an Ads account exists. If no account exists, 741 creates one under 741.Studio. |
| 11 | STÜRZL Steuerstrafrecht | Google Search Console | ausstehend since 2026-10-01 | we have it — tick it | Memory `anja-stuerzl-client.md` (13.10.): property verified by HTML tag with `741studio18`, 16 months of data, disavow list uploaded on 13.10. The reporting-bot does not have access yet (bot list 13.10.). | Set to `erteilt`. Separate task (already in the brief 13.10.): "Add user" for the reporting-bot. |
| 12 | STÜRZL Steuerstrafrecht | Website / Hosting / CMS | ausstehend since 2026-10-01 | we have it — tick it | Memory `anja-stuerzl-client.md` (13.10.): the 741 Joomla account has the role Super User. The Artfiles hosting login is in `.secrets/stuerzl-artfiles.env`. | Set to `erteilt`. Note: the hosting login is possibly a shared login. The method asks for an own 741 account. Martin decides if this is sufficient. |

## Summary

| class | count | rows |
|---|---|---|
| we have it — tick it | 8 | 1, 2, 3, 5, 6, 9, 11, 12 |
| not needed | 3 | 4, 7, 8 |
| really open | 1 | 10 |
| unclear | 0 | — |

## Notes for Martin

1. The Morning Grill plan of 13.10. says that 741 has no Johni access for GA4, GBP and GSC. That check used only the reporting-bot. The Chrome check with `741studio18` shows that 741 has all three. The open item is only the reporting-bot access.
2. The reporting-bot sees only GA4 account "741 Clients" and 5 Search Console sites. Johni (GA4 and GSC) and Stürzl (GSC) are not in its lists. Reports for these clients need a manual grant to the bot.
3. The Hüwel site has no tracking tag since the move on 06.10. This is a separate decision.
4. The Chrome tab that the agent opened stays open, because the Chrome extension disconnected. Martin can close it.
