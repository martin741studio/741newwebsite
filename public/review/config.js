/**
 * 741 STUDIO - PROSPECT LOCAL SEO AUDIT CONFIGURATION TEMPLATE
 * 
 * To create a new personalized audit landing page for a prospect:
 * 1. Create a subfolder: `public/review/[company-slug]/` (e.g. `public/review/hotel-bali/`)
 * 2. Copy `public/review/index.html` into `public/review/[company-slug]/index.html`
 * 3. Update the `PROSPECT_DATA` object below inside the page or load this config.
 */

window.PROSPECT_DATA = {
    // Basic Prospect Metadata
    companyName: "Physiotherapie Muster",
    contactName: "Herr Müller",
    prospectSlug: "physiotherapie-muster",
    city: "München",
    branch: "Physiotherapie & Krankengymnastik",
    logoUrl: "", // Optional custom logo path or placeholder
    mapScreenshotUrl: "", // Optional screenshot URL
    websiteScreenshotUrl: "", // Optional screenshot URL
    
    // Video Embed (Loom Share/Embed Link)
    loomUrl: "https://www.loom.com/embed/a77fbc286c0c4515a815a5198e3b3c3b",
    loomDuration: "5 Minuten",
    
    // Key Status Quo Scores
    mapsRankDesktop: "Rang #8",
    mapsRankMobile: "Rang #9",
    focusKeyword: "Physiotherapie München",
    currentReviewsCount: 32,
    currentRating: "4.8",
    mobileSpeedScore: "58/100",
    
    // Hero Copy
    headline: "Hallo Physiotherapie Muster,<br>wir haben eine persönliche Analyse Ihrer <span class=\"accent\">Google-Präsenz</span> erstellt.",
    subheadline: "Vielen Dank, dass Sie sich die Zeit nehmen. Als kleine Aufmerksamkeit haben wir eine individuelle Analyse erstellt, in der wir zeigen, welche Chancen wir für Ihre Sichtbarkeit bei Google Maps und in der lokalen Suche sehen.",
    
    // Personal Note
    personalMessageGreeting: "Hallo Herr Müller,",
    personalMessageText: [
        "vielen Dank, dass Sie sich unser persönliches Video anschauen.",
        "Wir wollten Ihnen nicht einfach irgendeine Standard-Mail schicken.",
        "Deshalb haben wir uns Ihre Website, Ihr Google-Unternehmensprofil und Ihre lokale Sichtbarkeit angesehen und die wichtigsten Punkte in einem kurzen Video zusammengefasst.",
        "Wir hoffen, dass Sie daraus bereits einige hilfreiche Ideen mitnehmen können."
    ],
    authorName: "Martin Drendel",
    authorRole: "Senior Local SEO & Growth Consultancy",
    
    // Executive Summary Cards (🟢 🟠 🔴)
    positives: [
        "Sehr gute Kundenzufriedenheit & positive Rezensionen (Durchschnitt 4.8 Sterne).",
        "Ansprechendes Firmenlogo und professionelles Grund-Erscheinungsbild.",
        "Bestehendes Google Unternehmensprofil ist bereits verifiziert und aktiv."
    ],
    opportunities: [
        "Optimierung der Haupt- und Nebenkategorien für +150% mehr relevante Aufrufe.",
        "Aufbau strukturierter lokaler Landingpages für umliegende Stadtteile.",
        "Einbindung strukturierter Daten (Schema.org) für Dienstleistungen und FAQs."
    ],
    criticalIssues: [
        "Fehlende NAP-Konsistency (Name, Adresse, Telefon) in führenden Branchenverzeichnissen.",
        "Langsame Ladezeiten auf Smartphones (Mobile PageSpeed Score liegt bei 58/100).",
        "Keine direkten Call-to-Action Buttons zur Online-Terminbuchung im ersten Sichtfeld."
    ],

    // PDF Sheet Section 2: Google Business Profil Audit Details
    gbpAudit: [
        { title: "Profil beansprucht & verifiziert", status: "good", desc: "Das Profil ist ordnungsgemäß beansprucht und bei Google bestätigt." },
        { title: "Titel & Name mit Keywords", status: "warning", desc: "Firmierung vorhanden, jedoch fehlen relevante lokale Fokus-Keywords." },
        { title: "Kategorien-Setup (Primär & Sekundär)", status: "warning", desc: "Hauptkategorie korrekt, aber 3 wertvolle Nebenkategorien fehlen völlig." },
        { title: "Leistungen & Services eingetragen", status: "warning", desc: "Services sind nur teilweise gepflegt. Detaillierte Beschreibungen fehlen." },
        { title: "NAP-Konsistenz (Name/Adresse/Tel)", status: "good", desc: "Adresse und Telefonnummer stimmen auf dem Profil exakt." },
        { title: "Unternehmensbeschreibung (750 Z.)", status: "warning", desc: "Beschreibung vorhanden, nutzt jedoch nicht das vollen Keyword-Volumen." },
        { title: "Fotos & Branding Updates", status: "critical", desc: "Wenige Innenaufnahmen. EXIF-Geodaten und aktuelle Team-Fotos fehlen." },
        { title: "Bewertungs-Anzahl & Frequenz", status: "warning", desc: "32 Bewertungen sind gut, aber Top 3 Mitbewerber haben im Schnitt 75+." },
        { title: "Antworten auf Rezensionen", status: "warning", desc: "Nur ca. 40% der Kundenbewertungen wurden von der Praxis beantwortet." },
        { title: "Google Beiträge / Posts", status: "critical", desc: "Seit über 6 Monaten wurden keine aktuellen GBP-Beiträge veröffentlicht." },
        { title: "Q&A (Fragen & Antworten)", status: "critical", desc: "Keine vorgefertigten Antworten auf häufige Patientenfragen eingepflegt." },
        { title: "Attribute & Barrierefreiheit", status: "good", desc: "Attribute wie Rollstuhlgerechtigkeit sind hinterlegt." }
    ],

    // PDF Sheet Section 3: Website & Technisches SEO Audit Details
    websiteAudit: [
        { title: "Mobil-Optimierung & Responsive Design", status: "good", desc: "Die Website passt sich gut an Smartphones und Tablets an." },
        { title: "Ladezeit / PageSpeed (Mobile)", status: "warning", desc: "Mobile Score 58/100. Unkomprimierte Bilder bremsen den Seitenaufbau." },
        { title: "SSL-Zertifikat & HTTPS", status: "good", desc: "Verschlüsselung ist aktiv und sicher konfiguriert." },
        { title: "Google Indexierung & Sichtbarkeit", status: "good", desc: "Alle Kernseiten sind im Google-Index auffindbar." },
        { title: "Meta-Title & Meta-Descriptions", status: "warning", desc: "Meta-Titles sind zu kurz; Meta-Descriptions fehlen auf Unterseiten." },
        { title: "Überschriften-Struktur (H1–H3)", status: "warning", desc: "Mehrere H1-Tags auf der Startseite vorhanden. Strukturierung unsauber." },
        { title: "Schema.org / LocalBusiness Data", status: "critical", desc: "Strukturierte Daten für lokale Dienstleistungen fehlen vollständig." },
        { title: "Conversion & Call-to-Actions", status: "critical", desc: "Kein auffälliger Button zur Online-Terminbuchung im Hero-Bereich." },
        { title: "Bilder-Optimierung & Alt-Texte", status: "warning", desc: "Bilder sind relativ schwer (>1.5MB) und besitzen oft keine Alt-Attribute." },
        { title: "Google Analytics GA4 & Tracking", status: "good", desc: "Basic GA4-Tag ist im Quellcode integriert." }
    ],

    // PDF Sheet Section 4: Lokale Präsenz & Citations
    citationAudit: [
        { title: "NAP-Konsistenz im Netz", status: "critical", desc: "Abweichende Schreibweisen der Adresse auf 4 Verzeichnissen entdeckt." },
        { title: "Branchenbuch-Citations", status: "warning", desc: "Präsent auf DasÖrtliche & GelbeSeiten, aber Einträge auf 12 Portalen fehlen." },
        { title: "Apple Maps & Bing Places", status: "warning", desc: "Profil auf Bing vorhanden, Apple Maps Business Connect fehlt noch." },
        { title: "Lokale Backlinks", status: "warning", desc: "Solide Basis, aber keine Verlinkungen von lokalen Partnern/Vereinen." }
    ],

    // PDF Sheet Section 5: Keyword-Recherche
    keywords: [
        { keyword: "Physiotherapie München", region: "München Zentrum", volume: "4.400 / Mo.", currentRank: "Rang #8" },
        { keyword: "Krankengymnastik München", region: "München Nord", volume: "1.900 / Mo.", currentRank: "Rang #12" },
        { keyword: "Manuelle Therapie München", region: "München", volume: "1.300 / Mo.", currentRank: "Rang #15" },
        { keyword: "Physiotherapeut in der Nähe", region: "Umkreis 5 km", volume: "5.400 / Mo.", currentRank: "Rang #9" }
    ],

    // PDF Sheet Section 6: Wettbewerber (Top 3) Benchmark
    competitors: [
        { name: "PhysioPraxis Zentrum", rank: "Rang #1", reviews: "112 (4.9 ★)", category: "Physiotherapiezentrum", advantage: "Sehr hohe Citations & 95+ Fotos" },
        { name: "Krankengymnastik Am Park", rank: "Rang #2", reviews: "84 (4.8 ★)", category: "Physiotherapiepraxis", advantage: "Lokale Stadtteil-Landingpages" },
        { name: "Physio & Sport München", rank: "Rang #3", reviews: "67 (4.7 ★)", category: "Sportphysiotherapie", advantage: "Sehr aktive Google Posts & Videos" }
    ],

    // Quick Wins ("Was Sie bereits morgen verbessern könnten")
    quickWins: [
        { title: "Spezifischere Google-Kategorien hinzufügen", desc: "Fügen Sie 3-4 exakte Nebenkategorien im Unternehmensprofil hinzu, um sofort für spezialisierte Suchen zu ranken." },
        { title: "Hochauflösende Praxis- & Teamfotos hochladen", desc: "Profile mit regelmäßigen Team- und Praxisfotos erhalten nachweislich 42% mehr Routenanfragen." },
        { title: "Automatisierter Bewertungs-Link per QR-Code", desc: "Geben Sie zufriedenen Patienten nach der Behandlung einen direkten QR-Code zum Bewerten mit." },
        { title: "Lokale Stadtteil-Landingpages aufbauen", desc: "Eigene Landingpages für umliegende Stadtteile sichern Ihnen Neukunden aus dem gesamten Einzugsgebiet." },
        { title: "FAQ & Strukturierte Daten integrieren", desc: "Beantworten Sie die 5 häufigsten Fragen direkt auf der Website für Rich-Snippet-Vorteile." },
        { title: "Google Posts im Profil aktivieren", desc: "Nutzen Sie wöchentliche GBP-Beiträge, um Google Aktivität und Relevanz zu signalisieren." }
    ],

    // Growth Potential Metrics
    growthMetrics: {
        currentRank: "Rang #8",
        targetRank: "Top 3 Pack",
        callsIncrease: "+180%",
        routesIncrease: "+240%",
        leadsIncrease: "+150%",
        trustLabel: "Top 1 lokale Autorität"
    },

    // PDF Sheet Section 7: Priorisierter Fahrplan / Roadmap
    roadmap: [
        { step: "Phase 1", action: "Google Business Profil Kern-Optimierung & Nebenkategorien", priority: "Hoch", effort: "Gering" },
        { step: "Phase 1", action: "Bereinigung aller NAP-Daten in deutschen Branchenverzeichnissen", priority: "Hoch", effort: "Mittel" },
        { step: "Phase 2", action: "Website Ladezeiten-Sprint & Mobile Speed Optimierung", priority: "Hoch", effort: "Mittel" },
        { step: "Phase 2", action: "Erstellung von 3 lokalen Stadtteil-Landingpages mit H1-H3 Keyword-Struktur", priority: "Mittel", effort: "Mittel" },
        { step: "Phase 3", action: "Aufbau eines nachhaltigen Systems für automatisierte Google-Bewertungen", priority: "Hoch", effort: "Gering" },
        { step: "Phase 3", action: "Einbindung von Schema.org LocalBusiness Markup & FAQ Rich Snippets", priority: "Mittel", effort: "Gering" }
    ],

    // Testimonials Placeholders
    testimonials: [
        { quote: "Innerhalb weniger Monate haben wir deutlich mehr qualifizierte Patientenanfragen über Google Maps erhalten.", author: "Dr. med. Thomas Weber", role: "Facharztpraxis für Orthopädie" },
        { quote: "Unsere Praxis wird endlich in den Top 3 in unserer Stadt gefunden. Die Investition hat sich vielfach ausgezahlt.", author: "Sandra Lindner", role: "Inhaberin PhysioVital" },
        { quote: "Sehr professionelle und angenehme Zusammenarbeit. Das Team von 741 Studio versteht es, Ergebnisse zu liefern.", author: "Markus Hoffmann", role: "Geschäftsführer MedCare" }
    ]
};
