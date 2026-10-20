"""Builds part-AC/harm-register.json and who-owns-what.json. Pure data. No network."""
import json, os, sys
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import RUN, PART, now, load_manifest
NOW = now()
man = load_manifest()["evidence"]
EVIDS = {e["id"] for e in man}
started = min(e["collected_at"] for e in man)
BLOCK = "wait for NAP lock (Martin + client confirm Untermainkai 26)"
OLD = "Wiesenhüttenstraße 17, 60329 Frankfurt am Main"
NEW = "Untermainkai 26, 60329 Frankfurt am Main"
D = {"2026-10-01":"2026-10-01T00:00:00+02:00","2026-10-07":"2026-10-07T00:00:00+02:00","2026-10-09":"2026-10-09T00:00:00+02:00","2026-05-27":"2025-05-27T00:00:00+02:00"}
items = []
cnt = {"A":0,"C":0}
def add(area, entity, item, why, check, target, severity, action, detail, actor, effort, approval, conf, ev, tool, refetch, *,
        destructive=False, source_field=None, collected=None, client_safe=True, client_text=None, hint="", before=None, after=None, verify=None, depends=None):
    cnt[area] += 1
    for e in ev:
        assert e in EVIDS, e
    it = {"id": f"H-{area}-{cnt[area]:03d}", "area": area, "entity": entity, "item": item, "why": why, "check_id": check,
          "source_field": source_field, "target": target, "severity": severity, "action": action, "action_detail": detail,
          "actor": actor, "effort": effort, "destructive": destructive, "approval": approval, "approved_by": None, "approved_at": None,
          "wave": None, "snapshot_id": None, "rollback": None, "before": before, "after": after, "verify_check": verify or "",
          "done_at": None, "confidence": conf, "collected_at": collected or NOW, "source_tool": tool, "evidence_ids": ev,
          "refetch": refetch, "depends_on": depends or [], "drilldown_hint": hint, "client_safe": client_safe}
    if client_text: it["client_text"] = client_text
    items.append(it)
    return it["id"]
R = lambda tool, **kw: dict(tool=tool, **kw)
FC = lambda url, cost="1 Firecrawl credit": R("firecrawl_scrape", url=url, formats=["markdown"], maxAge=0, cost=cost)

# ===================== AREA A =====================
add("A","domain","Der Inhaber der Domain stuerzl-steuerstrafrecht.de ist öffentlich nicht prüfbar: DENIC und RDAP nennen keinen Inhaber (Status connect, zuletzt geändert 2023-09-11, Nameserver bei Artfiles).",
    "Ohne Nachweis bleibt offen, ob die Domain auf die Kanzlei läuft; die technische Betreuung liegt laut Mandantin bei einem externen Ansprechpartner (client_stated).",
    "UB.A01","stuerzl-steuerstrafrecht.de","cosmetic","keep",
    "Kein Schaden bewiesen. Kundin legt einen DENIC-Web-Whois-Auszug vor (https://webwhois.denic.de) oder nennt das Registrar-Konto. Danach Inhaber in who-owns-what.json eintragen.",
    "client","S","blocked","verified",["EV-A-whois-denic","EV-A-rdap-denic","EV-A-whois","EV-A-dig-ns"],"whois -h whois.denic.de / RDAP (curl)",
    R("whois", cmd="whois -h whois.denic.de stuerzl-steuerstrafrecht.de", cost="0 EUR"),
    verify="Web-Whois oder Registrar-Konto zeigt die Kanzlei (Dr. Stürzl) als Inhaberin", hint="who-owns-what.json asset domain_registrar",
    client_text="Wer die Domain Ihrer Kanzlei formal hält, ist öffentlich nicht einsehbar. Bitte lassen Sie uns einen Registrar-Nachweis zukommen.")

add("A","hosting","DNS und Hosting laufen bei Artfiles (NS auth1/auth2.artfiles.de, A 212.53.214.189, rDNS www140.c.artfiles.de, Apache). Das Zertifikat (Let's Encrypt, gültig 2026-08-26 bis 2026-11-24) und die Weiterleitung auf www sind in Ordnung. Mail läuft getrennt über mail.stuerzl-steuerstrafrecht.de (Wortmann-AG-Netz, SPF mit Microsoft-365-Eintrag).",
    "Kein technischer Schaden gefunden. Konto-Inhaber des Hostings ist nicht belegt; 741 hat laut Befund vom 2026-10-09 keinen FTP- oder Hosting-Zugang (client_stated).",
    "UB.A02","212.53.214.189 / stuerzl-steuerstrafrecht.de","cosmetic","keep",
    "Keine Änderung. Hosting-Konto und Inhaber beim Ansprechpartner der Kanzlei erfragen; vor jeder Änderung vollständiges Seiten-Backup anfordern.",
    "client","S","proposed","verified",["EV-A-dig-ns","EV-A-dig-soa","EV-A-dig-a","EV-A-dig-rdns","EV-A-whois-ip","EV-A-headers-https","EV-A-headers-www","EV-A-tls-cert","EV-A-dig-mx","EV-A-dig-txt","EV-A-baseline-s9-s11"],"dig / curl / openssl / whois",
    R("dig", cmd="dig NS stuerzl-steuerstrafrecht.de", cost="0 EUR"),
    verify="dig NS zeigt auth1/auth2.artfiles.de; openssl zeigt Zertifikat bis 2026-11-24 oder neuer", hint="TLS läuft am 2026-11-24 ab, Erneuerung beobachten",
    client_text="Webseite und Domain-Einstellungen laufen technisch einwandfrei bei einem deutschen Hoster. Offen ist nur, wer das Hosting-Konto führt.")

add("A","cms","Im Joomla-System hat das 741-Konto nur die Gruppe Administrator, nicht Super User. Super User sind laut Mandantin der technische Ansprechpartner und ein weiterer Dienstleister. SP Page Builder (Kontakt, Fußzeile) und Global Configuration lassen sich mit dem 741-Konto nicht bearbeiten (Session mismatched / 403).",
    "Die Anschrift in Fußzeile, Kontaktseite und Schema lässt sich ohne Super-User-Recht nicht ändern; die Kanzlei hat die Kontrolle über ihre Webseite nicht allein.",
    "UB.A03","Joomla-Administration stuerzl-steuerstrafrecht.de","blocks_revenue","claim",
    "Anfrage an die Kanzlei: Super-User-Recht für das 741-Konto freigeben lassen (laut Notiz vom 2026-10-09 beim technischen Ansprechpartner angefragt; Versand per WhatsApp ist im Backlog nur als Entwurf belegt) oder den Ansprechpartner die NAP-Änderung ausführen lassen. Danach Benutzerliste lesen und alte Agentur-Konten prüfen.",
    "client","S","blocked","client_stated",["EV-A-baseline-s9-s11","EV-A-memory-excerpt"],"client statement (Martin's check in the admin, 2026-10-09)",
    R("browser_read", step="Joomla Administration > Benutzer > Liste lesen (angemeldet)", cost="0 EUR, needs Super User or a screenshot from the client"),
    destructive=True, collected=D["2026-10-09"], verify="Benutzerliste zeigt das 741-Konto als Super User und die Kanzlei als Inhaberin", hint="who-owns-what.json asset cms; blockiert H-C-002 bis H-C-004",
    client_text="Für Änderungen an Anschrift und Kontaktdaten auf Ihrer Webseite braucht unser Team erweiterte Zugriffsrechte im Redaktionssystem.")

add("A","gbp","Der Zugang zu den Google-Unternehmensprofilen Frankfurt und München wurde am 2026-10-07 vom früheren Agenturkontakt an das 741-Konto vergeben. Die Rolle des 741-Kontos und der Primary Owner beider Profile sind nicht belegt.",
    "Das Maps-Profil ist der wichtigste Kanal für Neumandate. Solange nicht belegt ist, dass Dr. Stürzl Primary Owner ist, hängt die Kontrolle am früheren Dienstleister.",
    "UB.A04","GBP ChIJyVGAdikEaW8RUOWpEJs-2XA (Frankfurt) und GBP München","blocks_revenue","claim",
    "Im Browser (Konto 741studio18) Einstellungen > Personen und Zugriff beider Profile lesen und per Screenshot sichern. Falls nicht Dr. Stürzl: Primary Owner auf ein Kanzlei-Google-Konto übertragen lassen, 741 bleibt Manager. Nur mit Zustimmung der Kundin und Martins Go.",
    "client","M","blocked","client_stated",["EV-A-baseline-s9-s11","EV-A-memory-excerpt"],"client statement (mail of the former agency, 2026-10-07)",
    R("browser_read", step="GBP > Einstellungen > Personen und Zugriff (beide Profile)", cost="0 EUR, logged-in Chrome as 741studio18"),
    destructive=True, collected=D["2026-10-07"], verify="Screenshot der Verwalterliste: Primary Owner ist die Kanzlei, 741 ist Manager", hint="who-owns-what.json asset gbp_frankfurt, gbp_muenchen",
    client_text="Wir prüfen, wer Inhaber Ihrer beiden Google-Unternehmensprofile ist. Ziel ist, dass die Kanzlei selbst Inhaberin ist.")

add("A","analytics","GA4-Property 483853149 wurde im Mai 2025 von der früheren Agentur angelegt; Dr. Stürzl wurde mit ihrem Google-Konto hinzugefügt (Rolle unbekannt). Das 741-Konto erhielt am 2026-10-07 Zugang und setzte am 2026-10-09 Key Events. Das Reporting-Dienstkonto hat keinen Zugriff (GA4 Data API 403 PERMISSION_DENIED, 2026-10-11).",
    "Mess-Historie und Administrator-Rolle hängen an einer Property, die die frühere Agentur angelegt hat; ob die Kanzlei Administratorin ist, ist nicht belegt.",
    "UB.A05","GA4 property 483853149","cosmetic","claim",
    "GA4 > Verwaltung > Zugriffsverwaltung lesen. Kanzlei-Konto als Administrator sicherstellen, 741 als Bearbeiter. Danach Dienstkonto reporting-bot als Viewer anlegen lassen, damit Berichte ohne Browser laufen.",
    "client","S","blocked","client_stated",["EV-A-baseline-s9-s11","EV-A-sa-test"],"client statement + Google Analytics Data API (service account)",
    R("node", script="scripts/area_ac/a2_sa_test.mjs", cost="0 EUR"),
    destructive=True, collected=D["2026-10-09"], verify="Zugriffsverwaltung zeigt Kanzlei als Administrator; Dienstkonto runReport liefert 200", hint="who-owns-what.json asset ga4",
    client_text="Die Webstatistik läuft. Wir stellen sicher, dass die Kanzlei dort Administratorin ist.")

add("A","search_index","Die Search Console (sc-domain:stuerzl-steuerstrafrecht.de) ist per DNS-TXT-Eintrag verifiziert (google-site-verification vorhanden). Wer sie hält, ist nicht belegt (vermutlich der technische Ansprechpartner, client_stated). 741 hat keinen Zugang; das Reporting-Dienstkonto sieht die Property nicht (404, nicht verifizierte Property in diesem Konto).",
    "Ohne Search-Console-Zugang lassen sich Indexierung, Disavow-Datei und Anfragen zur Neuindexierung nicht steuern; die Kanzlei kann Suchdaten nicht selbst prüfen.",
    "UB.A06","sc-domain:stuerzl-steuerstrafrecht.de","leaks_link_power","claim",
    "Anfrage an den Ansprechpartner: Dr. Stürzls Kanzlei-Google-Konto als Inhaber (Owner) eintragen und das Konto 741studio18 sowie reporting-bot@studio-apis-503306.iam.gserviceaccount.com als Nutzer freigeben. Alternativ neue Domain-Property per DNS-TXT durch die Kanzlei verifizieren lassen.",
    "client","S","blocked","verified",["EV-A-dig-txt","EV-A-sa-test","EV-A-baseline-s9-s11"],"dig TXT + Search Console API (service account)",
    R("node", script="scripts/area_ac/a2_sa_test.mjs", cost="0 EUR"),
    destructive=True, verify="sites.get für sc-domain liefert 200 mit permissionLevel; Nutzerliste zeigt die Kanzlei als Owner", hint="who-owns-what.json asset gsc; blockiert Disavow-Upload (Backlog 16)",
    client_text="Die Suchdaten Ihrer Webseite sind für unser Team noch nicht einsehbar. Wir bitten um Freigabe in der Search Console.")

add("A","analytics","Der Tag-Manager-Container GTM-WFPFSTK2 ist auf der Webseite eingebunden (im HTML gelesen). Zugang erhielt das 741-Konto am 2026-10-07 von der früheren Agentur; Version 4 wurde am 2026-10-09 mit Martins Go veröffentlicht. Konto-Inhaber des Containers ist nicht belegt.",
    "Der Container steuert das Tracking der Kanzlei; liegt das GTM-Konto bei der früheren Agentur, endet die Kontrolle mit deren Zugang.",
    "UB.A07","GTM-WFPFSTK2","cosmetic","claim",
    "GTM > Admin > Benutzerverwaltung lesen. Falls das Konto der früheren Agentur gehört: Container in ein Konto der Kanzlei exportieren/importieren oder Kanzlei-Konto als Konto-Administrator eintragen.",
    "client","S","blocked","client_stated",["EV-A-home-html","EV-A-baseline-s9-s11"],"curl (HTML) + client statement",
    R("browser_read", step="GTM > Admin > Benutzerverwaltung", cost="0 EUR"),
    destructive=True, collected=D["2026-10-09"], verify="Benutzerverwaltung zeigt die Kanzlei als Konto-Administratorin", hint="who-owns-what.json asset gtm",
    client_text="Das Tracking ist aktiv. Wir klären, auf wessen Konto der Tag Manager läuft.")

add("A","analytics","Ein Google-Ads-Konto ist nicht bekannt. Laut Onboarding-Gespräch gab es früher einmal Google Ads. Das Konto und sein Inhaber wurden nicht gelesen; der Start der Kampagne ist für spätestens 2 Wochen nach Projektstart geplant.",
    "Wenn ein altes Konto bei der früheren Agentur existiert, gehören Verlauf und Conversion-Daten dazu; das ist unbelegt.",
    "UB.A07","Google Ads (kein Konto bekannt)","cosmetic","keep",
    "Kundin fragen, ob ein altes Ads-Konto existiert und wer es verwaltet. Neues Konto unter Kundeneigentum anlegen, 741 als Verwalter.",
    "client","S","blocked","client_stated",["EV-A-baseline-s9-s11"],"client statement (onboarding call 2026-10-06)",
    R("browser_read", step="Google Ads > Zugriff und Sicherheit", cost="0 EUR"),
    collected=D["2026-10-01"], verify="Kontoliste der Kanzlei zeigt ein Ads-Konto im Kundeneigentum", hint="who-owns-what.json asset ads",
    client_text="Für Google Ads legen wir ein Konto an, das Ihrer Kanzlei gehört.")

add("A","social","Das LinkedIn-Firmenprofil existiert (716 Follower laut Suchtreffer 2026-10-11) und wird von der Webseite verlinkt. Das anwalt.de-Kanzleiprofil ist gepflegt (Bilder, Rechtstipps, Bewertungen). Die Administratoren beider Konten sind nicht belegt.",
    "Beide Profile tragen die Marke der Kanzlei; fehlende Admin-Klarheit blockiert spätere Adress- und Profiländerungen.",
    "UB.A07","LinkedIn company page; anwalt.de profile","cosmetic","keep",
    "Kundin nennt die Konto-Inhaber (LinkedIn-Seitenadmins, anwalt.de-Login). Zugangsdaten gehören in den Vault, nicht ins Register.",
    "client","S","blocked","verified",["EV-C-search-misc","EV-C-listing-anwalt-de-firm"],"firecrawl_scrape / firecrawl_search",
    FC("https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht"),
    verify="Kundin bestätigt Admin-Konten; Eintrag in client_credentials-Vault", hint="who-owns-what.json assets social:linkedin, listing:anwalt.de",
    client_text="Wir klären, wer die Profile auf LinkedIn und anwalt.de verwaltet.")

# ===================== AREA C =====================
add("C","website","Der Stammdatensatz ist nicht festgelegt. client_locations enthält für diese Mandantin keine Zeile; die Portal-Tabelle locations enthält eine Zeile (Kanzlei Frankfurt, alte Adresse, ohne Telefon und ohne Zeiten, München fehlt). nap-master.json ist als nicht gesperrt (locked=false) markiert.",
    "Ohne gesperrten Stammdatensatz darf keine Adresse an Webseite, Google-Profil oder Verzeichnissen geändert werden.",
    "UB.C01","nap-master.json / Portal locations","blocks_revenue","fix",
    "Martin und Kundin bestätigen: Untermainkai 26, 60329 Frankfurt am Main als Eintragsadresse; verbindliche Öffnungs- und Telefonzeiten; Notfallnummern. Dann nap-master.json sperren (locked_at) und client_locations/locations anlegen (Frankfurt + München).",
    "741","S","blocked","verified",["EV-C-client-locations","EV-C-portal-locations","EV-C-client-citations","EV-C-nap-master","EV-C-baseline-site-s3-s10"],"Supabase PostgREST GET (read-only)",
    R("supabase_get", path="client_locations?client_id=eq.b6f6e303-50e4-4afb-a343-337206cec316", also="locations?client_id=eq...", cost="0 EUR"),
    verify="nap-master.json hat locked_at; client_locations hat 2 Zeilen", hint="Voraussetzung für alle blockierten Items",
    client_text="Bevor wir Adressen überall ändern, bestätigen Sie bitte die endgültige Anschrift und die verbindlichen Erreichbarkeitszeiten.")

add("C","website","Das Impressum nennt als Anschrift weiterhin Wiesenhüttenstraße 17, 60329 Frankfurt am Main (Telefon +49 69 29 80 28 87-0, Fax -9). München steht im Impressum nicht im Text, nur in der Fußzeile.",
    "Die Pflichtangabe zur Anschrift zeigt die Adresse vor dem Umzug vom 2026-10-05.",
    "UB.C02","https://www.stuerzl-steuerstrafrecht.de/index.php/impressum","blocks_revenue","fix",
    BLOCK+". Danach Impressum auf Untermainkai 26 ändern; ob die Niederlassung München im Impressumstext genannt werden soll, entscheidet die Kanzlei.",
    "741","S","blocked","verified",["EV-C-site-impressum","EV-C-site-analysis"],"curl",
    R("curl", url="https://www.stuerzl-steuerstrafrecht.de/index.php/impressum", cost="0 EUR"),
    before=OLD, after=NEW+" (proposed, not locked)", depends=["H-A-003","H-C-001"], verify="Re-Crawl: Impressum zeigt den gesperrten Master-Wert", hint="Seiten-Tausch-Regeln beachten",
    client_text="Das Impressum nennt noch die frühere Anschrift in der Wiesenhüttenstraße.")

add("C","website","Auf Kontaktseite und in der Fußzeile aller 13 geprüften Seiten steht Wiesenhüttenstraße 17; Untermainkai 26 kommt auf keiner Seite vor. Die Kontaktseite beschreibt den Weg zur Wiesenhüttenstraße und Parkplätze im Hof.",
    "Mandanten und Suchmaschinen sehen die alte Adresse; Besucher könnten zur alten Adresse fahren.",
    "UB.C02","https://www.stuerzl-steuerstrafrecht.de/index.php/kontakt und Fußzeile","blocks_revenue","fix",
    BLOCK+". Danach Kontaktseite (Adresse, Anfahrtstext, Parkhinweis) und Fußzeilen-Modul ändern; Telefonnummern und Formularwege unverändert lassen.",
    "741","M","blocked","verified",["EV-C-site-kontakt","EV-C-site-analysis","EV-C-site-home","EV-C-site-team","EV-C-site-faq"],"curl (13 pages)",
    R("python", script="scripts/area_ac/c1_site.py + c1c_site_summary.py", cost="0 EUR"),
    before=OLD, after=NEW+" (proposed, not locked)", depends=["H-A-003","H-C-001"], verify="Re-Crawl: 13 von 13 Seiten zeigen den Master-Wert, 0 zeigen Wiesenhüttenstraße", hint="EV-C-site-analysis hat Zeilen je Seite",
    client_text="Kontaktseite und Fußzeile Ihrer Webseite zeigen noch die frühere Anschrift.")

add("C","website","Das JSON-LD (LegalService) ist auf allen 13 Seiten identisch: Adresse Wiesenhüttenstraße 17, Geo 50.104409/8.66711, Öffnungszeiten Mo-Fr 09:00-18:00, nur Frankfurt, kein Eintrag für München, sameAs nur LinkedIn.",
    "Suchmaschinen und KI-Antworten lesen die alte Adresse und die Zeiten aus dem Schema; der zweite Standort fehlt.",
    "UB.C02","JSON-LD @id #legalservice","blocks_revenue","fix",
    BLOCK+". Danach Schema auf Untermainkai 26 mit neuen Geo-Koordinaten, ein LegalService je Standort (München: Oberanger 32, +49 89 72444170), verbindliche Zeiten, sameAs mit anwalt.de und Kammer.",
    "741","M","blocked","verified",["EV-C-site-analysis","EV-C-site-home"],"curl + JSON parse",
    R("python", script="scripts/area_ac/c1c_site_summary.py", cost="0 EUR"),
    before="Wiesenhüttenstraße 17; geo 50.104409,8.66711; Mo-Fr 09:00-18:00", after="Untermainkai 26 (proposed) mit neuen Koordinaten", depends=["H-A-003","H-C-001"], verify="Rich-Results-Test/JSON-Parse zeigt Master-Adresse und 2 Standorte", hint="Hinweis: Person nur als Name",
    client_text="Die technischen Adressangaben im Hintergrund Ihrer Webseite nennen noch die frühere Anschrift und lassen München aus.")

add("C","website","Die Webseite zeigt die Telefonnummer in drei Schreibweisen (+49 69 29 80 28 87-0, 069 29802887-0, tel:+4969298028870) und Öffnungszeiten, die sich widersprechen: Kontaktseite Telefon Mo-Fr 09:30-14:30 (beide Standorte), Schema 09:00-18:00, anwalt.de und Cylex 09:00-18:00, Google-Profil Frankfurt öffnet 09:00 (Stand 2026-10-01).",
    "Kunden sehen je Quelle andere Zeiten; möglich ist ein echter Unterschied zwischen Bürozeit und Telefonzeit, der aber nirgends erklärt wird.",
    "UB.C02","Kontaktseite, Schema, GBP, anwalt.de, Cylex","cosmetic","fix",
    "Kundin nennt verbindliche Büro- und Telefonzeiten je Standort (offene Frage aus dem Backlog, Frau Jilg). Dann eine Schreibweise der Nummer (+49 69 298028870) und einen Zeitenwert überall setzen.",
    "client","S","blocked","verified",["EV-C-site-kontakt","EV-C-site-analysis","EV-C-listing-anwalt-de-firm","EV-C-listing-cylex-ffm","EV-C-gbp-stored-2026-10-01"],"curl / firecrawl_scrape",
    R("curl", url="https://www.stuerzl-steuerstrafrecht.de/index.php/kontakt", cost="0 EUR"),
    depends=["H-C-001"], verify="Alle Quellen zeigen dieselben Zeiten und dieselbe Nummernschreibweise", hint="Stunden sind nicht Teil des vorläufigen Masters",
    client_text="Auf Ihrer Webseite und in den Verzeichnissen stehen unterschiedliche Zeiten. Bitte nennen Sie uns die verbindlichen Zeiten.")

add("C","gbp","Google-Profil Frankfurt: Name STÜRZL Steuerstrafrecht und Telefon +49 69 298028870 stimmen. Die Adresse wurde laut Stand 2026-10-07 noch nicht auf Untermainkai 26 umgestellt (Bewertungen 5,0 bei 14; nur Kategorie Rechtsanwalt; öffnet 09:00). Das Live-Profil wurde in diesem Lauf nicht gelesen.",
    "Das Maps-Profil ist die wichtigste Quelle für Neumandate; es zeigt voraussichtlich noch die Adresse vor dem Umzug.",
    "UB.C03","GBP ChIJyVGAdikEaW8RUOWpEJs-2XA","blocks_revenue","fix",
    BLOCK+". Danach Adresse im GBP ändern in einem geplanten Schritt (Risiko: erneute Verifizierung, Video-Verifizierung vorbereiten). Live-Profil vorher im Browser oder per Local Falcon lesen und Screenshot sichern.",
    "741","M","blocked","derived",["EV-C-gbp-stored-2026-10-01"],"stored findings (Google Maps read by the team on 2026-10-01; status line of 2026-10-07)",
    R("local_falcon_mcp", step="read listing ChIJyVGAdikEaW8RUOWpEJs-2XA (no scan)", cost="read only; tool not connected in this session"),
    before=OLD+" (derived)", after=NEW+" (proposed, not locked)", collected=D["2026-10-01"], depends=["H-A-004","H-C-001"],
    verify="GBP-Lesung zeigt Master-Adresse, Name, Telefon, Zeiten", hint="GBP live profile unreadable in this run; see params.run_notes",
    client_text="Ihr Google-Profil in Frankfurt muss nach Bestätigung der Anschrift auf die neue Adresse umgestellt werden.")

add("C","gbp","Google-Profil München (Oberanger 32): Name STÜRZL Steuerstrafrecht, Telefon +49 89 72444170, 5,0 bei 1 Bewertung, Kategorie Rechtsanwalt, keine Fotos (Stand 2026-10-01). Adresse und Telefon stimmen mit Webseite, BRAK-Daten, anwalt.de und Cylex-Eintrag überein. Der Standort ist ein zweites Büro und keine Dublette.",
    "Kein Namens- oder Adressschaden. Offen bleiben Fotos und Nebenkategorien, das ist Wachstumsarbeit.",
    "UB.C03","GBP München Oberanger 32","cosmetic","keep",
    "Keine Korrektur. Live-Profil bei Gelegenheit lesen (hier nicht gelesen).",
    "741","S","proposed","derived",["EV-C-gbp-stored-2026-10-01","EV-C-site-kontakt","EV-C-listing-anwalt-lotse-anja"],"stored findings + live cross-check of the address",
    R("local_falcon_mcp", step="read listing for Oberanger 32 (no scan)", cost="read only; tool not connected in this session"),
    collected=D["2026-10-01"], verify="GBP-Lesung zeigt Oberanger 32, 80331 München, +49 89 72444170", hint="Teil des Pakets? offen (Backlog 12)",
    client_text="Ihr Münchner Google-Profil ist in Name, Adresse und Telefon stimmig.")

add("C","listing","In der Citations-Tabelle des Portals gibt es für diese Mandantin keine Zeile (client_citations: 0), und keine Zeile in client_locations. Die Konsistenz der Verzeichnisse ist deshalb bisher nicht dokumentiert; dieser Lauf hat 13 Einträge live gelesen (NAP-Quote gegen den alten Stand 15,4 Prozent streng, gegen den vorgeschlagenen Stand 7,7 Prozent streng).",
    "Ohne Tabelle kann kein Re-Scan Änderungen belegen.",
    "UB.C04","client_citations (Supabase)","cosmetic","keep",
    "Nach Sperre des Masters die 13 gelesenen Einträge aus nap-corrections.json in client_citations übernehmen (Schreiben nur mit Go).",
    "741","S","proposed","verified",["EV-C-client-citations","EV-C-client-locations"],"Supabase PostgREST GET (read-only)",
    R("supabase_get", path="client_citations?client_id=eq.b6f6e303-50e4-4afb-a343-337206cec316", cost="0 EUR"),
    verify="client_citations enthält die gelesenen Einträge mit listing_url und last_checked", hint="nap-corrections.json stats",
    client_text="Die Verzeichniseinträge Ihrer Kanzlei werden von uns jetzt systematisch erfasst.")

add("C","listing","anwalt.de Kanzleiprofil (5,0 bei 79 Bewertungen) zeigt für Frankfurt Wiesenhüttenstraße 17 und München Oberanger 32. Zeiten Mo-Fr 09:00-18:00. Der Profilname trägt das Plattform-Präfix Kanzlei. Das Profil ist laut Mandantin der wichtigste digitale Kanal.",
    "Die meistgenutzte Quelle zeigt für Frankfurt die Adresse vor dem Umzug.",
    "UB.C04","https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht","blocks_revenue","fix",
    BLOCK+". Danach Adresse im anwalt.de-Konto ändern (Login der Kanzlei). Name mit Präfix Kanzlei ist Plattformstandard, keine Korrektur.",
    "client","S","blocked","verified",["EV-C-listing-anwalt-de-firm","EV-C-search-2"],"firecrawl_scrape",
    FC("https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht"),
    before=OLD, after=NEW+" (proposed, not locked)", depends=["H-C-001","H-A-009"], verify="Re-Fetch zeigt Untermainkai 26", hint="nap-corrections.json key anwalt-de-firm-ffm",
    client_text="Auf anwalt.de steht für Frankfurt noch die frühere Anschrift.")

add("C","listing","anwalt.de Personenprofil von Dr. Stürzl (5,0 bei 55 Bewertungen) zeigt Wiesenhüttenstraße 17. Die Fachanwaltsurkunde nennt als Stelle Rechtsanwaltskammer Köln.",
    "Hohe Reichweite, alte Adresse.",
    "UB.C04","https://www.anwalt.de/anja-stuerzl","blocks_revenue","fix",
    BLOCK+". Danach Adresse im Personenprofil ändern.",
    "client","S","blocked","verified",["EV-C-listing-anwalt-de-anja"],"firecrawl_scrape",
    FC("https://www.anwalt.de/anja-stuerzl"),
    before=OLD, after=NEW+" (proposed, not locked)", depends=["H-C-001","H-A-009"], verify="Re-Fetch zeigt Untermainkai 26", hint="nap-corrections.json key anwalt-de-anja",
    client_text="Das persönliche Profil auf anwalt.de zeigt noch die frühere Anschrift.")

add("C","listing","Der Hinweis Rechtsanwaltskammer Köln auf dem anwalt.de-Profil steht im Block der Fachanwaltsurkunde und nennt die Stelle, die den Titel verliehen hat. Die BRAK-Daten (über Anwalt-Lotse) führen Dr. Stürzl als Mitglied der Rechtsanwaltskammer Frankfurt. Das ist deshalb sehr wahrscheinlich kein Adressfehler.",
    "Der frühere Befund RAK Köln wurde als Fehler gewertet; die Quelle stützt das nicht.",
    "UB.C04","https://www.anwalt.de/anja-stuerzl (Qualifikationen)","cosmetic","keep",
    "Nicht ändern. Kundin bestätigt, bei welcher Kammer der Titel verliehen wurde. Erst bei einem anderen Befund ändern.",
    "client","S","proposed","verified",["EV-C-listing-anwalt-de-anja","EV-C-listing-anwalt-lotse-anja"],"firecrawl_scrape",
    FC("https://www.anwalt.de/anja-stuerzl"),
    verify="Kundin bestätigt die Kammer der Titelverleihung", hint="Befund vom 2026-10-08 (RAK Köln) korrigiert", client_safe=False,
    client_text="Der Kammer-Hinweis auf anwalt.de betrifft den Titel und ist voraussichtlich korrekt.")

add("C","listing","Das amtliche Anwaltsverzeichnis der BRAK, gelesen über den Spiegel Anwalt-Lotse (Daten vor etwa 3 Wochen bestätigt), nennt Wiesenhüttenstr. 17, 60329 Frankfurt, Telefon 069-298028870, Fax 069-298028879 und als Zweigstelle München Oberanger 32. Mitglied der Rechtsanwaltskammer Frankfurt. Das Verzeichnis der Kammer selbst wurde nicht gelesen.",
    "Das amtliche Verzeichnis ist die Quelle für viele Portale; dort steht die Adresse vor dem Umzug.",
    "UB.C04","BRAK Anwaltsverzeichnis / Rechtsanwaltskammer Frankfurt","blocks_revenue","fix",
    BLOCK+". Danach meldet die Rechtsanwältin die neue Anschrift ihrer Kammer (Login der Kammer/beA). Danach amtliches Verzeichnis direkt prüfen.",
    "client","S","blocked","derived",["EV-C-listing-anwalt-lotse-anja"],"firecrawl_scrape (mirror of the official directory)",
    FC("https://anwalt-lotse.de/rechtsanwaeltin/anja-stuerzl-frankfurt-5vtd/"),
    before="Wiesenhüttenstr. 17, 60329 Frankfurt", after=NEW+" (proposed, not locked)", depends=["H-C-001"], verify="Kammer- und BRAK-Verzeichnis zeigen Untermainkai 26", hint="official site not read; mirror dated about 3 weeks before 2026-10-11",
    client_text="Die Rechtsanwaltskammer führt Ihre Anschrift noch mit dem alten Standort. Die Änderung melden Sie als Mitglied.")

add("C","listing","11880 zeigt Wiesenhüttenstr. 17, 60329 Frankfurt, (069) 298028870, E-Mail und Webseite (Eintrag aktualisiert 2026-10-04). Der Eintrag ist nicht als vom Inhaber bestätigt gekennzeichnet; als Dienstleistung ist Drogenstrafrecht eingetragen, das auf der Webseite der Kanzlei nicht vorkommt.",
    "Verzeichnis mit eigener Reichweite zeigt die alte Adresse und eine Leistung, die die Kanzlei nicht nennt.",
    "UB.C04","https://www.11880.com/branchenbuch/frankfurt-am-main/081314253B114102102/stuerzl-steuerstrafrecht.html","leaks_link_power","fix",
    BLOCK+". Danach über Änderungen vorschlagen oder Eintragsservice anpassen; Leistungs-Tag mit der Kanzlei klären.",
    "client","S","blocked","verified",["EV-C-listing-11880"],"firecrawl_scrape",
    FC("https://www.11880.com/branchenbuch/frankfurt-am-main/081314253B114102102/stuerzl-steuerstrafrecht.html"),
    before="Wiesenhüttenstr. 17, 60329 Frankfurt", after=NEW+" (proposed, not locked)", depends=["H-C-001"], verify="Re-Fetch zeigt Untermainkai 26", hint="nap-corrections.json key 11880",
    client_text="Im Verzeichnis 11880 steht noch die frühere Anschrift.")

add("C","listing","Cylex Frankfurt (Eintrag 16927796, nicht übernommen) zeigt Wiesenhüttenstraße 17, Zeiten Mo-Fr 09:00-18:00 und im Beschreibungstext als München-Adresse Neuhauser Str. 3a, die nicht zur Kanzlei gehört.",
    "Alte Adresse plus eine falsche Münchner Adresse im Text; Eintrag ist ungeschützt.",
    "UB.C04","https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-16927796.html","leaks_link_power","claim",
    "Eintrag übernehmen (Cylex-Verifizierung durch die Kanzlei). Beschreibung sofort korrigieren (München: Oberanger 32); Frankfurter Adresse erst nach "+BLOCK+".",
    "client","S","blocked","verified",["EV-C-listing-cylex-ffm","EV-C-listing-cylex-search-ffm"],"firecrawl_scrape",
    FC("https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-16927796.html"),
    before=OLD+"; München in Beschreibung: Neuhauser Str. 3a", after=NEW+" (proposed); München: Oberanger 32, 80331 München", depends=["H-C-001"], verify="Re-Fetch zeigt Master-Adresse und Oberanger 32", hint="nap-corrections.json key cylex-ffm",
    client_text="Im Verzeichnis Cylex steht die frühere Anschrift, und im Text ist eine falsche Münchner Adresse genannt.")

add("C","listing","Cylex München führt einen zweiten Eintrag (17045957) mit Neuhauser Str. 3a, 80331 München, derselben Telefonnummer 089 72444170 und der Kategorie Software Hersteller. Neuhauser Straße 3a ist die Anschrift einer anderen Kanzlei. Der richtige Eintrag (17168776, Oberanger 32) existiert daneben.",
    "Doppelter Eintrag mit falscher Straße und falscher Branche führt Mandanten an eine fremde Adresse.",
    "UB.C05","https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17045957.html","leaks_link_power","report",
    "Eintrag übernehmen und danach Eintrag entfernen (Dublette von 17168776). Erst nach Einzel-Go. Zuerst prüfen, ob eine Zusammenführung möglich ist.",
    "client","S","proposed","verified",["EV-C-listing-cylex-muc-wrong","EV-C-listing-cylex-search-muc","EV-C-search-4b"],"firecrawl_scrape",
    FC("https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17045957.html"),
    destructive=True, before="Neuhauser Str. 3a, 80331 München; Software Hersteller", after="Eintrag entfernt, 17168776 bleibt", verify="Cylex-Suche München zeigt nur Oberanger 32", hint="Das Büro München ist keine Dublette; nur dieser zweite Cylex-Eintrag",
    client_text="Bei Cylex gibt es einen doppelten Eintrag für München mit einer falschen Adresse.")

add("C","listing","Cylex München Eintrag 17168776 (Oberanger 32, 089 72444170, nicht übernommen) ist richtig, hat aber keine Branche.",
    "Richtige Daten, ungeschützt und ohne Kategorie.",
    "UB.C04","https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17168776.html","cosmetic","claim",
    "Eintrag übernehmen und Kategorie Rechtsanwälte setzen.",
    "client","S","proposed","verified",["EV-C-listing-cylex-muc-ok","EV-C-listing-cylex-search-muc"],"firecrawl_scrape",
    FC("https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17168776.html"),
    verify="Eintrag ist übernommen und zeigt Kategorie Rechtsanwälte", hint="nap-corrections.json key cylex-muc-ok",
    client_text="Der Münchner Eintrag bei Cylex ist richtig, sollte aber von Ihnen übernommen werden.")

add("C","listing","rechtecheck.de führt die Münchner Kanzlei mit Neuhauser Str. 3a, 80331 München (andere Kanzlei an dieser Adresse) und ohne Telefon. Der Frankfurter Eintrag trägt im Seitentitel Frankfurt (Oder) und zeigt Wiesenhüttenstr. 17.",
    "Falsche Straße für München und falsche Stadtangabe für Frankfurt; beide Einträge sind ungeschützt.",
    "UB.C04","https://rechtecheck.de/anwalt/muenchen/kanzlei/kanzlei-stuerzl-steuerstrafrecht/ und /anwalt/frankfurt/anja-stuerzl/","leaks_link_power","claim",
    "Über Daten aktualisieren: München auf Oberanger 32 und +49 89 72444170 sofort; Frankfurt: Stadtangabe sofort, Adresse erst nach "+BLOCK+".",
    "client","S","blocked","verified",["EV-C-listing-rechtecheck-muenchen","EV-C-listing-rechtecheck-frankfurt","EV-C-search-4b"],"firecrawl_scrape",
    FC("https://rechtecheck.de/anwalt/muenchen/kanzlei/kanzlei-stuerzl-steuerstrafrecht/"),
    before="München: Neuhauser Str. 3a; Frankfurt: Wiesenhüttenstr. 17, Titel Frankfurt (Oder)", after="München: Oberanger 32; Frankfurt: Master-Adresse, Frankfurt am Main", depends=["H-C-001"], verify="Re-Fetch beider Seiten zeigt Master-Werte", hint="nap-corrections.json keys rechtecheck-muc, rechtecheck-ffm",
    client_text="Auf rechtecheck.de stehen eine falsche Münchner Straße und für Frankfurt eine falsche Stadtangabe.")

add("C","listing","Infobel führt die Kanzlei mit Wiesenhüttenstraße 17, 60329 Frankfurt (Oder) und der Nummer 069298028870. Die Seite selbst war hinter einem Captcha nicht lesbar; der Befund stammt aus dem Suchtreffer vom 2026-10-11.",
    "Falsche Stadt (Oder statt Main) plus alte Adresse; das Verzeichnis wird von anderen Portalen übernommen.",
    "UB.C04","https://www.infobel.com/de/germany/sturzl_steuerstrafrecht/frankfurt_oder/DE109851584-069298028870/businessdetails.aspx","leaks_link_power","fix",
    "Stadt sofort auf Frankfurt am Main ändern lassen; Adresse erst nach "+BLOCK+". Änderungsweg bei Infobel im Browser prüfen.",
    "client","S","blocked","derived",["EV-C-listing-infobel","EV-C-search-2"],"firecrawl_search snippet (page behind captcha)",
    R("firecrawl_search", query='"Wiesenhüttenstraße 17" Frankfurt Stürzl', cost="4 Firecrawl credits"),
    before="Wiesenhüttenstraße 17 60329 Frankfurt (Oder)", after=NEW+" (proposed, not locked), Frankfurt am Main", depends=["H-C-001"], verify="Infobel-Seite zeigt Frankfurt am Main und Master-Adresse", hint="nap-corrections.json key infobel",
    client_text="Im Verzeichnis Infobel steht Frankfurt (Oder) statt Frankfurt am Main.")

add("C","listing","LinkedIn-Firmenseite (primärer Standort Wiesenhüttenstraße 17, 60329 Frankfurt laut Suchtreffer 2026-10-11), JuWiSt-Mitgliederliste (Wiesenhüttenstraße 17) und Creditreform (60329 Frankfurt, Straße nicht sichtbar) tragen die alte Adresse oder sind nicht lesbar. Die Seiten selbst wurden nicht geöffnet.",
    "Kleine Quellen mit der alten Adresse, die später mitgezogen werden sollten.",
    "UB.C04","LinkedIn company; juwist.com/mitgliederliste; Creditreform","cosmetic","fix",
    BLOCK+". Danach LinkedIn-Admin ändert den Standort, der Verband JuWiSt wird um Änderung gebeten; Creditreform prüfen.",
    "client","S","blocked","derived",["EV-C-search-misc"],"firecrawl_search snippets",
    R("firecrawl_search", query='"Wiesenhüttenstraße 17" Frankfurt Stürzl', cost="4 Firecrawl credits"),
    before="Wiesenhüttenstraße 17", after=NEW+" (proposed, not locked)", depends=["H-C-001","H-A-009"], verify="Re-Fetch zeigt den Master-Wert", hint="nap-corrections.json keys linkedin-company, juwist, creditreform",
    client_text="Auch auf LinkedIn und in einer Mitgliederliste steht noch die frühere Anschrift.")

add("C","listing","maptons.com und acht Sprach-Subdomains (Scraper-Kopien) zeigen Wiesenhüttenstraße 17 und +49 69 298028870 mit Seitenstempeln von 2026-07-12 bis 2026-09-13. Die Seiten blockieren Abrufe (HTTP 403).",
    "Kopierte Kartendaten, die ohne eigenen Änderungsweg die alte Adresse weiterverbreiten.",
    "UB.C05","https://de.maptons.com/p/3302892716","cosmetic","keep",
    "Keine eigene Maßnahme (kein Änderungsweg). Nach Korrektur von Google-Profil und Hauptverzeichnissen erneut prüfen.",
    "741","S","proposed","derived",["EV-C-search-misc","EV-C-search-3"],"firecrawl_search snippets (page blocked)",
    R("firecrawl_search", query='"069 298028870" Stürzl', cost="4 Firecrawl credits"),
    verify="Re-Check nach Korrektur der Quellen", hint="nap-corrections.json key maptons",
    client_text="Kopien von Kartendaten im Netz tragen die frühere Anschrift; sie ziehen nach, wenn die Hauptquellen geändert sind.")

add("C","listing","bestattorneyusa.com führt Dr. Anja Stürzl automatisch erzeugt als Anja Stürzl, Tucson (Adresse Wiesenhüttenstraße 17 Frankfurt/Main, Bewertung 4,0 mit 1 Bewertungstext unbekannter Herkunft, Auszeichnungstext mit Jahreszahlen). Claim this profile ist möglich.",
    "Ein US-Profil mit falscher Stadt, nicht belegter Bewertung und Auszeichnungstext unter dem Namen einer Rechtsanwältin kann berufsrechtlich und im Wettbewerbsrecht problematisch sein.",
    "UB.C05","https://bestattorneyusa.com/attorneys/anja-sturzl-tucson-20528","cosmetic","claim",
    "Profil über Claim Profile übernehmen und Stadt, Adresse und Texte korrigieren oder löschen lassen. Entfernen nur bei gescheitertem Claim und mit Einzel-Go. Juristische Bewertung entscheidet die Kanzlei.",
    "client","S","proposed","verified",["EV-C-bestattorneyusa-anja","EV-C-bestattorneyusa-lines"],"curl",
    R("curl", url="https://bestattorneyusa.com/attorneys/anja-sturzl-tucson-20528", cost="0 EUR"),
    before="Tucson; Wiesenhüttenstraße 17; 1 Bewertung", after="übernommen und korrigiert oder entfernt", verify="Profil zeigt Frankfurt am Main oder ist entfernt", hint="Kandidat für Report; Claim zuerst",
    client_safe=False, client_text="Ein automatisch erzeugtes US-Verzeichnis führt Ihr Profil mit falscher Stadt. Wir bitten Sie, es zu übernehmen oder entfernen zu lassen.")

add("C","listing","bestattorneyusa.com führt Lea Wimmer automatisch erzeugt als Boston mit der Adresse Neuhauserstraße 3a Munich DE und 4,0 bei 1 Bewertung. Claim this profile ist möglich.",
    "Falsche Stadt und falsche Münchner Straße (Adresse einer anderen Kanzlei).",
    "UB.C05","https://bestattorneyusa.com/attorneys/lea-wimmer-boston-5898","cosmetic","claim",
    "Profil über Claim Profile durch Frau Wimmer übernehmen und korrigieren oder entfernen lassen. Entfernen nur mit Einzel-Go.",
    "client","S","proposed","verified",["EV-C-bestattorneyusa-lea","EV-C-bestattorneyusa-lines"],"curl",
    R("curl", url="https://bestattorneyusa.com/attorneys/lea-wimmer-boston-5898", cost="0 EUR"),
    before="Boston; Neuhauserstraße 3a Munich", after="übernommen und korrigiert (Oberanger 32, 80331 München) oder entfernt", verify="Profil zeigt München und Oberanger 32 oder ist entfernt", hint="Kandidat für Report; Claim zuerst",
    client_safe=False, client_text="Auch für Ihre Münchner Kollegin gibt es ein automatisch erzeugtes US-Profil mit falscher Stadt und Straße.")

add("C","listing","bestattorneyus.com (Zwillingsdomain): unter den Namensmustern der .com-Seite gibt es kein Profil (HTTP 404); die Suche der Seite ignoriert den Suchbegriff. Eine Prüfung war nur über die Adress-Muster möglich.",
    "Kein Schaden gefunden; die Prüfung ist begrenzt.",
    "UB.C05","bestattorneyus.com","cosmetic","keep",
    "Keine Maßnahme. Bei Re-Scan erneut mit Website-Suche prüfen.",
    "741","S","proposed","verified",["EV-C-bestattorneyus-anja","EV-C-bestattorneyus-lea","EV-C-bestattorneyus-search"],"curl",
    R("curl", url="https://bestattorneyus.com/attorneys/anja-sturzl-tucson-20528", cost="0 EUR"),
    verify="Re-Scan findet weiter kein Profil", hint="eingeschränkte Prüfung", client_safe=False,
    client_text="Auf der Zwillingsseite wurde kein Profil gefunden.")

add("C","listing","Gelbe Seiten: keine Treffer für Stürzl Steuerstrafrecht in Frankfurt (0 Treffer, Suchseite gelesen). Das Örtliche: kein exakt passender Eintrag. Kein Falsch-Eintrag vorhanden. Gesuchte Schreibweise Stützel Steuerstrafrecht: kein Treffer im Web.",
    "Kein Schaden; fehlende Einträge sind Aufbauarbeit, keine Entschädigung.",
    "UB.C05","gelbeseiten.de; dasoertliche.de; Suche Stützel","cosmetic","keep",
    "Keine Maßnahme im Un-Burning. Aufbau neuer Einträge erst nach der Bereinigung (Wachstumsarbeit).",
    "741","S","proposed","verified",["EV-C-listing-gelbeseiten","EV-C-listing-oertliche","EV-C-oertliche-raw","EV-C-search-5"],"firecrawl_scrape / curl / firecrawl_search",
    FC("https://www.gelbeseiten.de/suche/st%C3%BCrzl%20steuerstrafrecht/frankfurt-am-main"),
    verify="Re-Scan nach dem Aufbau zeigt Einträge mit dem Master-Wert", hint="Backlog Citations-Modul", client_text="In Gelbe Seiten und Das Örtliche ist die Kanzlei nicht eingetragen.")

add("C","listing","Yelp, Bing Places und Apple Maps konnten nicht gelesen werden: Yelp-Suche wird per JavaScript gerendert (Abruf nicht unterstützt), Bing Places und Apple Maps haben keine öffentliche Seite für diese Prüfung. JUVE führt nur den Namen im Ranking (Stürzl, Frankfurt), kein Kanzleiprofil mit Adresse.",
    "Unlesbare Quellen sind kein Nachweis für Fehlerfreiheit.",
    "UB.C04","yelp.de; Bing Places; Apple Maps; juve.de","cosmetic","keep",
    "Mit Browser-Zugang (Bing Places, Apple Business Connect) beim nächsten Lauf lesen. Kein Eintrag im Register als gefunden.",
    "741","S","blocked","verified",["EV-C-listing-yelp","EV-C-yelp-raw","EV-C-search-misc"],"curl / firecrawl_scrape (failed)",
    R("browser_read", step="Yelp, Bing Places, Apple Business Connect lesen", cost="0 EUR"),
    verify="Lesung liegt vor", hint="als nicht lesbar vermerkt, nicht als nichts gefunden", client_safe=False,
    client_text="Einige Verzeichnisse konnten wir noch nicht lesen.")

add("C","social","Soziale Profile: LinkedIn (siehe oben, alte Adresse laut Suchtreffer). XING-Profil von Lea Wimmer vorhanden (Salary Partnerin, ohne Adresse im Suchtreffer). Kein eigenes Instagram- oder Facebook-Profil der Kanzlei in den Treffern (nur Beiträge Dritter). Eine Suche nach Untermainkai 26 findet noch keine öffentliche Quelle.",
    "Keine falschen Daten gefunden; die neue Adresse ist öffentlich noch nirgends sichtbar.",
    "UB.C06","LinkedIn, XING, Instagram, Facebook","cosmetic","keep",
    "Keine Maßnahme. LinkedIn nach NAP-Sperre mitziehen (siehe Sammelzeile).",
    "741","S","proposed","derived",["EV-C-search-misc","EV-C-search-1"],"firecrawl_search snippets",
    R("firecrawl_search", query='"STÜRZL Steuerstrafrecht" Frankfurt', cost="4 Firecrawl credits"),
    verify="Re-Scan der sozialen Profile nach Sperre", hint="Instagram/Facebook: keine Treffer ist kein Beweis", client_text="Soziale Profile zeigen keine falschen Daten.")

add("C","listing","Tote oder fremde Nummern wurden nicht gefunden: In allen 8 live gelesenen Einträgen mit lesbarer Nummer stimmen die Ziffern (5 weitere Einträge zeigen keine oder nur eine maskierte Nummer) mit +49 69 298028870 (Frankfurt) und +49 89 72444170 (München) überein; abweichend sind nur die Schreibweisen. Eine fremde Stiftung (Kulturstiftung Ukraine) nutzt Adresse und Telefon der Kanzlei in ihrem Impressum.",
    "Keine tote Nummer; die Nutzung von Adresse und Telefon durch die Stiftung zieht beim Umzug ebenfalls um.",
    "UB.C07","alle Quellen; kulturstiftung-ukraine.org","cosmetic","keep",
    "Keine Maßnahme. Kundin informiert die Stiftung über die neue Adresse.",
    "client","S","proposed","verified",["EV-C-listing-anwalt-de-firm","EV-C-listing-11880","EV-C-listing-cylex-ffm","EV-C-listing-cylex-muc-ok","EV-C-listing-anwalt-lotse-anja","EV-C-search-3","EV-C-search-2"],"firecrawl_scrape / firecrawl_search",
    R("firecrawl_search", query='"069 29802887" Stürzl', cost="4 Firecrawl credits"),
    verify="Re-Scan findet keine weitere Nummer", hint="Nummern auf anwalt.de sind maskiert; Quelle ist der tel-Link", 
    client_text="Es wurden keine veralteten Telefonnummern gefunden.")

# the last C item (anwalt.de/Kanzlei hooks reference H-A-009 for the login item) check ids exist
ids = {i["id"] for i in items}
for it in items:
    for d in it["depends_on"]:
        assert d in ids, (it["id"], d)

run = {"run_id":"stuerzl-2026-10-11-scan","client_slug":"stuerzl","client_id":"b6f6e303-50e4-4afb-a343-337206cec316","domain":"stuerzl-steuerstrafrecht.de","mode":"scan",
  "from_audit_run":None,"previous_run_id":None,"started_at":started,"timezone":"Europe/Berlin","catalog_version":"ub-catalog-0.1-draft",
  "params":{"sitemap_url":None,"sitemap_note":"https://www.stuerzl-steuerstrafrecht.de/sitemap.xml returns 404; robots.txt has no sitemap line (2026-10-01 finding, sitemap URL re-checked 2026-10-11)",
            "gsc_property":"sc-domain:stuerzl-steuerstrafrecht.de","crawl":"GET only, 13 fixed pages (home, impressum, kontakt, datenschutz, team, kanzlei, leistungen, faq, steuerstrafrecht, lea-wimmer, dr-anja-stuerzl, aktuelles, selbstanzeigen-steuerliche-korrekturen), UA 741-unburning-scan/1.0",
            "with_backlinks":False,"falcon_scan":False,"dataforseo":False,"nap_master":"nap-master.json (provisional, locked=false)",
            "scanned_areas":["A","C"],"part":"AC",
            "areas_note":"Part AC only (areas A and C). Area A is verify-only with public checks; roles need logged-in reads. Area C compared against the old and the proposed address.",
            "run_notes":["GBP live profile unreadable: no Local Falcon read tool in this session; GBP data are stored values of 2026-10-01 (derived), address status of 2026-10-07.",
                         "Infobel page is behind a captcha: the Infobel row is derived from a search snippet of 2026-10-11.",
                         "LinkedIn, Yelp, Bing Places, Apple Maps, Das Örtliche detail pages: not readable (see items).",
                         "Official RAK Frankfurt/BRAK directory not read; seen through the Anwalt-Lotse mirror (data about 3 weeks old).",
                         "Supabase: client_locations and client_citations hold 0 rows for this client; portal table 'locations' holds 1 row.",
                         "Firecrawl search was rate-limited (HTTP 429) once; the searches were repeated one by one."]},
  "cost":{"eur":0,"credits":47}}
reg = {"run":run,"items":items}
os.makedirs(PART, exist_ok=True)
json.dump(reg, open(os.path.join(PART,"harm-register.json"),"w"), indent=1, ensure_ascii=False)
print(len(items), "items;", cnt)
