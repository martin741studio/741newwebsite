import json, os, sys
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import RUN, now, load_manifest
NOW = now()
EV = {e["id"] for e in load_manifest()["evidence"]}
EXP = "client (Dr. Anja Stürzl / STÜRZL Steuerstrafrecht); 741 = admin"
def A(asset, found, role, status, ev, req, conf, note="", collected=None):
    for e in ev: assert e in EV, e
    return {"asset":asset,"owner_expected":EXP,"owner_found":found,"741_role":role,"status":status,"evidence_ids":ev,"access_request":req,"confidence":conf,"note":note,"collected_at":collected or NOW}
rows = [
 A("domain_registrar","unknown: DENIC and RDAP do not disclose the holder (entities list empty). Status 'connect', last changed 2023-09-11T12:54:04+02:00. Name servers at Artfiles.","unknown","unknown",["EV-A-whois-denic","EV-A-rdap-denic","EV-A-whois"],
   "Frau Jilg / Dr. Stürzl sends a DENIC web-whois screenshot (https://webwhois.denic.de) for stuerzl-steuerstrafrecht.de, or names the registrar account and its holder. Client approves adding Martin as admin contact.","verified","Holder hidden by DENIC policy: recorded as unreadable, not as 'nothing found'."),
 A("dns","Artfiles name servers auth1.artfiles.de, auth2.artfiles.de. SOA serial 2026082604 (zone changed 2026-08-26). TXT: MS=ms12218001 (Microsoft 365 verification), google-site-verification (one token), SPF include:spf.protection.outlook.com ip4:89.63.12.99. No CAA.","unknown (no DNS access)","unconfirmed",["EV-A-dig-ns","EV-A-dig-soa","EV-A-dig-txt","EV-A-dig-caa","EV-A-dig-ns-parent"],
   "Client names who holds the Artfiles customer account; client approves a read-only zone export or a second contact for DNS.","verified"),
 A("hosting","Artfiles New Media GmbH, Hamburg: A 212.53.214.189, rDNS www140.c.artfiles.de, Apache. HTTPS valid (Let's Encrypt YR1, 2026-08-26 to 2026-11-24). Apex redirects to www (301).","none: no FTP or hosting access (client_stated, 2026-10-09)","unconfirmed",["EV-A-dig-a","EV-A-dig-rdns","EV-A-whois-ip","EV-A-headers-https","EV-A-headers-www","EV-A-tls-cert","EV-A-baseline-s9-s11"],
   "Client names the Artfiles account holder (customer number) and approves a full site backup to the client plus 741 as second user.","verified","Hosting is not on a 741 server. TLS expires 2026-11-24 (auto-renew not verifiable)."),
 A("mail","MX mail.stuerzl-steuerstrafrecht.de -> 89.63.12.99 (network WORTMANN AG, DE). SPF includes Microsoft Online Protection. Run by a third party.","none","unknown",["EV-A-dig-mx","EV-A-dig-a-mail","EV-A-dig-txt"],
   "Client names the IT provider for mail and whether Microsoft 365 is used. Needed before any form or lead-intake mail is set up.","verified"),
 A("cms","Joomla / Helix Ultimate / SP Page Builder. Super Users: the technical contact (Linkemann, user adminmili) and Framotec. The 741 account is group 'Administrator'.","Administrator (not Super User)","third_party",["EV-A-baseline-s9-s11","EV-A-memory-excerpt","EV-A-home-html"],
   "Client approves a Super User role for the 741 account (per note of 2026-10-09 requested from Herr Linkemann; the backlog only shows a WhatsApp draft), or lets the contact execute the NAP change. Then read the user list and remove old agency users with the client's go.","client_stated","Blocks H-C-002 to H-C-004.",collected="2026-10-09T00:00:00+02:00"),
 A("gbp_frankfurt","unknown: access was granted to 741studio18 by the former agency contact on 2026-10-07. Primary owner not shown. Place ID ChIJyVGAdikEaW8RUOWpEJs-2XA.","granted 2026-10-07, role not read","unconfirmed",["EV-A-baseline-s9-s11","EV-A-memory-excerpt"],
   "Client approves reading GBP > Settings > People and access (screenshot), and, if Dr. Stürzl is not Primary Owner, a transfer of the primary ownership to a firm-owned Google account with 741 as manager.","client_stated","",collected="2026-10-07T00:00:00+02:00"),
 A("gbp_muenchen","unknown: same grant as Frankfurt (to be confirmed per profile). Profile exists since early 2026 (Oberanger 32).","granted 2026-10-07, role not read","unconfirmed",["EV-A-baseline-s9-s11","EV-A-memory-excerpt"],
   "Same as Frankfurt, for the München profile.","client_stated","Second office, not a duplicate.",collected="2026-10-07T00:00:00+02:00"),
 A("ga4","Property 483853149 created by the former agency (tracking since May 2025). Dr. Stürzl added with anja.stuerzl@googlemail.com, role unknown. 741studio18 has access since 2026-10-07 and set Key Events on 2026-10-09 (an editing role at least). Reporting service account: no access (Data API 403 PERMISSION_DENIED, 2026-10-11).","editing role (not read)","unconfirmed",["EV-A-baseline-s9-s11","EV-A-sa-test"],
   "Client approves reading GA4 > Admin > Access management, makes the firm account Administrator, and adds reporting-bot@studio-apis-503306.iam.gserviceaccount.com as Viewer.","client_stated","Service account result is verified (2026-10-11); ownership facts are client_stated.",collected="2026-10-09T00:00:00+02:00"),
 A("gsc","Domain property sc-domain:stuerzl-steuerstrafrecht.de (TXT google-site-verification present). Holder presumed to be the technical contact (client_stated). Service account lists 5 properties, none for this site; sites.get returns 404 'not a verified Search Console site in this account' (2026-10-11).","none","unknown",["EV-A-dig-txt","EV-A-sa-test","EV-A-baseline-s9-s11"],
   "Client or the technical contact adds the firm's Google account as Owner and 741studio18 plus reporting-bot@studio-apis-503306.iam.gserviceaccount.com as users. Needed for the disavow upload and index checks.","verified","Existence of a DNS verification is verified; who verified it is not."),
 A("gtm","Container GTM-WFPFSTK2 loaded on the site (verified in HTML). Access granted to 741studio18 on 2026-10-07 by the former agency; Version 4 published 2026-10-09 (Martin's go). Account owner not read.","publish rights (Version 4)","unconfirmed",["EV-A-home-html","EV-A-baseline-s9-s11"],
   "Client approves reading GTM > Admin > User management; if the account belongs to the former agency, export the container into a firm-owned account.","client_stated","",collected="2026-10-09T00:00:00+02:00"),
 A("ads","No Google Ads account known. Onboarding call 2026-10-06: Google Ads existed once in the past.","none","unknown",["EV-A-baseline-s9-s11"],
   "Client says whether an old Ads account exists and who manages it. A new account is created under firm ownership with 741 as manager.","client_stated","",collected="2026-10-06T00:00:00+02:00"),
 A("social:linkedin","Company page stuerzl-steuerstrafrecht exists (716 followers, primary location with the old address). Admins not readable without login.","unknown","unknown",["EV-C-search-misc"],
   "Client names the page admins and adds 741 as editor if wanted.","verified"),
 A("social:instagram","No firm-owned Instagram profile appeared in the search results (only third-party posts). Not proof of absence.","none","unknown",["EV-C-search-misc"],"None needed unless the client runs a profile.","verified"),
 A("listing:anwalt.de","Kanzlei profile 5.0/79 plus profiles of Dr. Stürzl (5.0/55) and Lea Wimmer (5.0/23). Content is maintained (uploads, legal tips, reviews). Account holder not readable.","none","unconfirmed",["EV-C-listing-anwalt-de-firm","EV-C-listing-anwalt-de-anja"],
   "Client shares the anwalt.de login via the vault (or edits the address herself after the NAP lock).","verified","Main digital lead channel per client."),
 A("listing:rak_brak","Official lawyers' directory data (seen via the Anwalt-Lotse mirror): Wiesenhüttenstr. 17, Zweigstelle München Oberanger 32, member of RAK Frankfurt.","none (only the lawyer can notify the chamber)","unconfirmed",["EV-C-listing-anwalt-lotse-anja"],
   "Dr. Stürzl reports the new address to the Rechtsanwaltskammer after the NAP lock.","derived","Official site not read."),
 A("listing:cylex_ffm","Entry 16927796, unclaimed ('Eintrag übernehmen').","none","third_party",["EV-C-listing-cylex-ffm"],"Client claims the entry (verification at Cylex).","verified"),
 A("listing:cylex_muc_ok","Entry 17168776 (Oberanger 32), unclaimed.","none","third_party",["EV-C-listing-cylex-muc-ok"],"Client or Lea Wimmer claims the entry.","verified"),
 A("listing:cylex_muc_wrong","Entry 17045957 (Neuhauser Str. 3a, category Software Hersteller), unclaimed. Duplicate of 17168776.","none","third_party",["EV-C-listing-cylex-muc-wrong"],"Client claims it, then asks Cylex to remove it (per-item go).","verified"),
 A("listing:11880","Entry 081314253B114102102; not marked as owner-confirmed. Claim state unknown.","none","unknown",["EV-C-listing-11880"],"Client confirms whether a 11880 account exists; otherwise uses 'Änderungen vorschlagen'.","verified"),
 A("listing:rechtecheck","Two entries (Frankfurt person page, München firm page), both offer 'Daten aktualisieren' (unclaimed).","none","third_party",["EV-C-listing-rechtecheck-frankfurt","EV-C-listing-rechtecheck-muenchen"],"Client registers or claims the entries at rechtecheck.de.","verified"),
 A("listing:infobel","Entry DE109851584 (Frankfurt (Oder)); page behind captcha, claim state unknown.","none","unknown",["EV-C-listing-infobel"],"Client checks in the browser whether an Infobel account exists.","derived"),
 A("listing:bestattorneyusa","Two auto-generated profiles (Tucson, Boston), 'Claim this profile' offered. Not created by the firm.","none","third_party",["EV-C-bestattorneyusa-anja","EV-C-bestattorneyusa-lea"],"Dr. Stürzl and Lea Wimmer each claim or ask for removal (per-item go).","verified"),
 A("listing:bestlawyers","Firm page and two lawyer profiles, all 'Unactivated Profile'.","none","third_party",["EV-C-listing-bestlawyers"],"Client activates the profiles if wanted (also gives control of the address text).","verified"),
 A("listing:juwist","Member list of the association JuWiSt e.V. shows the old address.","none","third_party",["EV-C-search-misc"],"Dr. Stürzl asks the association to update her entry after the NAP lock.","derived"),
]
doc = {"run":"stuerzl-2026-10-11-scan","rule":"100 percent client ownership, agency is admin. Statuses: owned, unconfirmed, third_party, unknown. No asset is marked 'owned' because no ownership proof could be read without a logged-in browser. Rows built on older stored data carry their original date in collected_at.",
       "assets":rows,"collected_at":NOW,
       "service_account_test":{"service_account":"reporting-bot@studio-apis-503306","date":"2026-10-11","gsc":"5 properties visible, none for stuerzl-steuerstrafrecht.de; sites.get 404 for sc-domain and both https variants","ga4":"account summaries list 39 properties, 483853149 is not among them; runReport on properties/483853149 returned 403 PERMISSION_DENIED","evidence_id":"EV-A-sa-test"}}
json.dump(doc, open(os.path.join(RUN,"who-owns-what.json"),"w"), indent=1, ensure_ascii=False)
from collections import Counter
print(Counter(r["status"] for r in rows), len(rows))
