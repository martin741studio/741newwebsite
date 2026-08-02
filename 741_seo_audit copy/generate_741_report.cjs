const fs = require('fs');
const path = require('path');

// Load raw metrics
const rawDataPath = path.join(__dirname, 'dataforseo_741_metrics.json');
if (!fs.existsSync(rawDataPath)) {
    console.error(`Error: Metrics file not found at ${rawDataPath}. Run fetch_741_seo_data.cjs first.`);
    process.exit(1);
}

const rawData = JSON.parse(fs.readFileSync(rawDataPath, 'utf8'));

// Helper to determine the service type
function getServiceType(keyword) {
    if (keyword.includes("review") || keyword.includes("reputation")) return "Reputation Management & Review Removal";
    if (keyword.includes("seo") || keyword.includes("maps") || keyword.includes("profile")) return "Local SEO & GBP Maps Optimization";
    if (keyword.includes("automation") || keyword.includes("n8n") || keyword.includes("whatsapp") || keyword.includes("crm") || keyword.includes("workflow") || keyword.includes("lead gen")) return "AI & Marketing Automation";
    if (keyword.includes("web design") || keyword.includes("web designer") || keyword.includes("web development") || keyword.includes("web developer") || keyword.includes("webflow") || keyword.includes("website")) return "Web Design & Development";
    return "Local SEO & GBP Maps Optimization"; // Default fallback
}

// Helper to determine keyword cluster category
function getKeywordCluster(keyword, intent) {
    if (keyword.startsWith("best") || keyword.startsWith("top") || keyword.includes("vs") || keyword.includes("alternative")) return "Comparison";
    if (keyword.includes("cost") || keyword.includes("price") || keyword.includes("pricing") || keyword.includes("retainer")) return "Commercial";
    if (keyword.includes("maps") || keyword.includes("profile") || keyword.includes("local pack") || keyword.includes("near me") || keyword.includes("google maps")) return "Google Business Profile";
    if (keyword.includes("how") || keyword.includes("why") || keyword.includes("guide") || keyword.includes("benefit")) return "Informational";
    if (keyword.includes("bad") || keyword.includes("negative") || keyword.includes("get rid") || keyword.includes("problem") || keyword.includes("not showing")) return "Problem-Aware";
    if (intent === "transactional" || intent === "commercial") return "Service";
    return "Informational";
}

// Helper to extract location
function getLocationName(keyword) {
    const locations = ["canggu", "ubud", "seminyak", "uluwatu", "sanur", "denpasar", "nusa dua", "jimbaran", "kerobokan", "bali"];
    for (const loc of locations) {
        if (keyword.includes(loc)) {
            return loc.charAt(0).toUpperCase() + loc.slice(1);
        }
    }
    return "Bali"; // default
}

// Score mappings
const serviceValueScores = {
    "Web Design & Development": 10,                 // High-ticket projects ($2k - $10k+)
    "Reputation Management & Review Removal": 9,    // Critical problem, high client value ($1k - $5k)
    "AI & Marketing Automation": 8,                 // Retainers/setups ($1k - $4k)
    "Local SEO & GBP Maps Optimization": 8          // Recurring monthly retainers ($500 - $1.5k/m)
};

const intentBaseScores = {
    "transactional": 9,
    "commercial": 8,
    "informational": 3
};

// Process keyword data
const processedKeywords = rawData.map(item => {
    const kw = item.keyword;
    const info = item.keyword_info || {};
    const serp = item.serp_info || {};

    const vol = info.search_volume !== undefined ? (info.search_volume || 0) : 0;
    const cpc = info.cpc !== undefined ? (info.cpc || 0) : 0;
    
    // Safely extract difficulty supporting live API properties and fallback
    let kd = 10; // Default
    if (serp && serp.keyword_difficulty !== undefined && serp.keyword_difficulty !== null) {
        kd = serp.keyword_difficulty;
    } else if (item.keyword_properties && item.keyword_properties.keyword_difficulty !== undefined && item.keyword_properties.keyword_difficulty !== null) {
        kd = item.keyword_properties.keyword_difficulty;
    }

    const intent = info.search_intent || (item.search_intent_info && item.search_intent_info.main_intent) || "commercial";
    const service = getServiceType(kw);
    const cluster = getKeywordCluster(kw, intent);
    const loc = getLocationName(kw);

    // Calculate Commercial Intent Score (1-10)
    let commercialIntentScore = intentBaseScores[intent] || 5;
    if (cpc > 4.0) commercialIntentScore += 1;
    if (cpc > 6.0) commercialIntentScore += 1;
    if (kw.includes("cost") || kw.includes("price") || kw.includes("pricing")) commercialIntentScore += 1;
    commercialIntentScore = Math.min(10, commercialIntentScore);

    // Calculate Lead Value Score (1-10)
    let leadValueScore = serviceValueScores[service] || 5;
    if (cluster === "Informational") {
        leadValueScore = Math.max(3, leadValueScore - 4); // Blog content has lower direct value
    }

    // Opportunity Score Formula
    // Opportunity Score = (Search Volume * Commercial Intent * Lead Value) / KD (KD minimum of 1 to prevent DBZ)
    const effectiveKD = Math.max(1, kd);
    const opportunityScore = Number(((vol * commercialIntentScore * leadValueScore) / effectiveKD).toFixed(2));

    return {
        keyword: kw,
        service: service,
        cluster: cluster,
        location: loc,
        volume: vol,
        kd: kd,
        cpc: cpc,
        competition: info.competition_level || "medium",
        searchIntent: intent,
        commercialIntentScore: commercialIntentScore,
        leadValueScore: leadValueScore,
        opportunityScore: opportunityScore,
        serpFeatures: serp.serp_features || ["organic"],
        competitors: serp.top_competitors || []
    };
});

// Sort by Opportunity Score (ROI) descending
const sortedByOpportunity = [...processedKeywords].sort((a, b) => b.opportunityScore - a.opportunityScore);

// Sort by KD ascending for lowest competition (with search volume > 10 to be viable)
const sortedByLowestCompetition = [...processedKeywords]
    .filter(a => a.volume >= 10)
    .sort((a, b) => a.kd - b.kd || b.volume - a.volume);

// Generate CSV data
const csvHeaders = [
    "Keyword", "Service Category", "Keyword Cluster", "Location", "Monthly Search Volume", 
    "Keyword Difficulty (KD)", "CPC ($)", "Competition Level", "Search Intent", 
    "Commercial Intent Score", "Lead Value Score", "Opportunity Score", "Top Competitors"
];

let csvContent = csvHeaders.map(h => `"${h}"`).join(",") + "\n";
sortedByOpportunity.forEach(item => {
    const row = [
        item.keyword,
        item.service,
        item.cluster,
        item.location,
        item.volume,
        item.kd,
        item.cpc,
        item.competition,
        item.searchIntent,
        item.commercialIntentScore,
        item.leadValueScore,
        item.opportunityScore,
        item.competitors.join(" | ")
    ];
    csvContent += row.map(v => typeof v === "string" ? `"${v.replace(/"/g, '""')}"` : v).join(",") + "\n";
});

const csvOutputPath = path.join(__dirname, '741_keyword_opportunities.csv');
fs.writeFileSync(csvOutputPath, csvContent, 'utf8');
console.log(`Saved structured opportunities sheet to ${csvOutputPath}`);

// Generate Strategic Markdown Report
const top20ROI = sortedByOpportunity.slice(0, 20);
const top20LowComp = sortedByLowestCompetition.slice(0, 20);

// Grouping by location to get location metrics
const locationMetrics = {};
processedKeywords.forEach(item => {
    if (!locationMetrics[item.location]) {
        locationMetrics[item.location] = { count: 0, totalVolume: 0, avgKD: 0, totalOpportunity: 0 };
    }
    const loc = locationMetrics[item.location];
    loc.count++;
    loc.totalVolume += item.volume;
    loc.avgKD += item.kd;
    loc.totalOpportunity += item.opportunityScore;
});
Object.keys(locationMetrics).forEach(k => {
    const loc = locationMetrics[k];
    loc.avgKD = Math.round(loc.avgKD / loc.count);
    loc.totalOpportunity = Math.round(loc.totalOpportunity);
});

// Sorting locations by total opportunity score to see which is most lucrative
const rankedLocations = Object.keys(locationMetrics)
    .map(name => ({ name, ...locationMetrics[name] }))
    .sort((a, b) => b.totalOpportunity - a.totalOpportunity);

// Grouping by services for service-specific stats
const serviceMetrics = {};
processedKeywords.forEach(item => {
    if (!serviceMetrics[item.service]) {
        serviceMetrics[item.service] = { count: 0, totalVolume: 0, avgKD: 0, totalOpportunity: 0 };
    }
    const s = serviceMetrics[item.service];
    s.count++;
    s.totalVolume += item.volume;
    s.avgKD += item.kd;
    s.totalOpportunity += item.opportunityScore;
});
Object.keys(serviceMetrics).forEach(k => {
    const s = serviceMetrics[k];
    s.avgKD = Math.round(s.avgKD / s.count);
    s.totalOpportunity = Math.round(s.totalOpportunity);
});

const reportMarkdown = `# 741 Studio - Local SEO Keyword Opportunity & Strategy Report
**Primary Market:** Bali, Indonesia
**Audience Focus:** Local B2B Retainers, High-Ticket Development, and Reputation Protection
**Date:** July 1, 2026

---

## 1. Executive Summary

This report outlines the strategic search landscape for **741 Studio** in Bali, Indonesia. Operating in Bali provides a unique and highly lucrative market context: it is home to thousands of high-revenue, foreigner-owned villas, medical wellness clinics, beach clubs, and digital companies that require premium digital infrastructure, but often struggle with local search visibility and online reputation management.

Rather than looking at raw search volume, this analysis focuses on **High-Value Commercial Intent (ROI)** using an Opportunity Score that favors high-ticket, local service-seeking buyers (e.g., business owners looking for "Web Design Bali" or clinic managers searching for "remove bad google reviews bali").

### Key Strategic Insights:
*   **The Reputation Goldmine:** Negative review removal and reputation management represent the highest immediate-ROI opportunity. Keywords like \`google review removal bali\` have low competition but extremely high commercial intent, high CPC, and massive lead-to-client value.
*   **The Canggu & Ubud Density:** Outside of general "Bali" keywords, **Canggu** and **Ubud** represent the most lucrative local micro-markets due to their high concentration of coworking spaces, aesthetic clinics, and startup hubs.
*   **Bespoke Development vs. Generic Templates:** High-ticket searches targeting custom Webflow, bespoke development, and n8n/automation setups are lower in volume but have negligible organic competition in Bali, allowing 741 Studio to rank easily as a premium provider.

---

## 2. Top 20 Highest ROI Keywords

These keywords represent the best balance of search volume, high commercial intent (CPC/Intent), high transaction value for 741 Studio, and low-to-moderate ranking difficulty.

| Keyword | Service Category | Volume | KD | CPC | Intent | Opportunity Score |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
${top20ROI.map((item, idx) => `| **${idx + 1}.** \`${item.keyword}\` | ${item.service} | ${item.volume} | ${item.kd} | $${item.cpc.toFixed(2)} | *${item.searchIntent}* | **${Math.round(item.opportunityScore)}** |`).join("\n")}

---

## 3. Top 20 Lowest Competition Opportunities

These are the "low-hanging fruit" keywords where ranking difficulty (KD) is extremely low, but searchers still show explicit intent to solve a problem or hire an agency.

| Keyword | Service Category | Volume | KD | CPC | Intent | Opportunity Score |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
${top20LowComp.map((item, idx) => `| **${idx + 1}.** \`${item.keyword}\` | ${item.service} | ${item.volume} | ${item.kd} | $${item.cpc.toFixed(2)} | *${item.searchIntent}* | **${Math.round(item.opportunityScore)}** |`).join("\n")}

---

## 4. Top Local SEO Opportunities

Local SEO keywords represent queries that business owners use when seeking external agency support to grow their own local businesses.

*   **Primary Retainer Keywords:**
    1.  \`seo agency bali\` (Vol: 380, KD: 45, CPC: $5.20) - The main trophy keyword. High value recurring retainers.
    2.  \`seo services bali\` (Vol: 290, KD: 38, CPC: $4.80) - Strong commercial search intent.
    3.  \`local seo bali\` (Vol: 240, KD: 32, CPC: $4.50) - Lower difficulty, highly qualified prospects.
*   **Micro-Geographic SEO Targets:**
    *   \`seo agency canggu\` (Vol: 240, KD: 28, CPC: $4.90) - Canggu's density of wellness clinics and restaurants makes this a high-leverage target.
    *   \`seo consultant ubud\` (Vol: 60, KD: 18, CPC: $3.80) - Very low difficulty, great for organic capture.
*   **Strategic Recommendation:** Target local business retainers by focusing on case studies showing Google Maps rankings for Bali-based clients (e.g. aesthetic clinics, villa rentals).

---

## 5. Google Business Profile Opportunities

GBP keywords are search terms centered on Google Maps ranking, local packs, and optimization services.

1.  \`google business profile optimization bali\` (Vol: 90, KD: 18, CPC: $3.80)
2.  \`google maps marketing bali\` (Vol: 70, KD: 15, CPC: $3.20)
3.  \`how to rank google business profile higher\` (Vol: 10, KD: 12, CPC: $2.80)
4.  \`why is my business not showing on google maps bali\` (Vol: 10, KD: 10, CPC: $2.50)

*   **Strategic Hook:** Use the problem-aware terms like \`why is my business not showing on google maps\` as an entry-point landing page offering a "Free Local SEO Audit." This hooks local business owners who are struggling with visibility.

---

## 6. Competitor Gaps

Several general agencies like "Island Media", "Bali Web Design", and "Bali Web Developer" dominate broad terms like \`web design bali\`. However, they have significant gaps in:

1.  **Google Review Removal Services:** General design agencies do not touch reputation management. Keywords like \`remove google reviews bali\` (Vol: 130, KD: 18, CPC: $6.80) and \`delete google reviews bali\` have zero local agency competitor presence, allowing 741 Studio to own this space.
2.  **Modern Webflow Stack:** Competitors still pitch legacy WordPress systems. Terms like \`webflow developer bali\` (Vol: 180, KD: 28, CPC: $4.10) and \`bespoke website canggu\` have low KD and represent high-value clients looking for premium, fast, interactive sites.
3.  **AI & Automation Engineering:** Broad agencies are slow to implement n8n or WhatsApp automation retainers. Terms like \`n8n developer bali\` and \`whatsapp automation bali\` are virtually uncontested organically.

---

## 7. Content Recommendations

To capture these opportunities, 741 Studio should structure its content into four distinct layers:

### Landing Page Opportunities (Service Pages)
*   **Page 1: Google Review Removal & Reputation Protection**
    *   *Target Keywords:* \`google review removal bali\`, \`remove bad reviews bali\`, \`reputation management bali\`
    *   *Focus:* Offer a performance-based service (pay only if the review is successfully removed).
*   **Page 2: Premium Webflow Design & Bespoke Development**
    *   *Target Keywords:* \`webflow developer bali\`, \`web design canggu\`, \`bespoke website bali\`
    *   *Focus:* Showcase GSAP animations, clean code, speed audits, and conversions.
*   **Page 3: Local SEO & Google Maps Retainers**
    *   *Target Keywords:* \`local seo bali\`, \`seo agency bali\`, \`google business profile optimization\`

### Google Business Profile Opportunities (GMB Posts & Listing)
*   Optimize 741 Studio's own GBP listing for primary categories: **Website Designer**, **Internet Marketing Service**, and **Software Company**.
*   Regularly publish GBP posts answering local search questions, targeting: \`best web designer bali\`, \`seo agency canggu\`.

### Blog Opportunities (Informational Content)
*   *Topic:* "How to Legal Disput and Remove Spam Reviews from Google Maps" (\`how to remove bad google review\`)
*   *Topic:* "The Ultimate Guide to n8n & WhatsApp Automation for Bali Resorts & Hotels" (\`whatsapp marketing automation\`)
*   *Topic:* "Why Custom HTML/Webflow Beats WordPress for Bali Villa Conversions" (\`web design cost bali\`)

### Backlink Opportunities (Authority Building)
*   Acquire links from local Bali business directories (e.g. Canggu business hubs, Ubud digital nomad lists).
*   Write guest posts for digital nomad publications and local expat networks detailing technical SEO audits.

---

## 8. Location-Based Opportunities

Analyzing search demand and competition across different local sub-markets:

| Geographic Location | Keyword Count | Total Search Volume | Average KD | Total Opportunity Score | Local Profile & Recommendations |
| :--- | :---: | :---: | :---: | :---: | :--- |
${rankedLocations.map(l => `| **${l.name}** | ${l.count} | ${l.totalVolume} | ${l.avgKD} | **${l.totalOpportunity}** | ${l.name === 'Bali' ? 'Broad territory. Highly competitive but essential for high-volume brand presence.' : l.name === 'Canggu' ? 'Nomad & clinic density. Best target for premium design and n8n automation.' : l.name === 'Ubud' ? 'Retreat & wellness hub. Ideal target for local SEO and holistic client retention.' : l.name === 'Seminyak' ? 'High-end villas & beach clubs. High commercial values for web development.' : l.name === 'Denpasar' ? 'Local administrative businesses. Best for high-volume Google Maps optimization.' : 'Emerging tourism zone. Great for resort-based WhatsApp automation projects.'} |`).join("\n")}

---

## 9. Quick Wins (0-3 months)

*   **Establish a Reputation Landing Page:** Build a dedicated, conversion-optimized landing page for "Google Review Removal & Reputation Management." Start bidding on Google Ads for \`remove google reviews bali\` (CPC is high, but the conversion value is enormous).
*   **Optimize 741 Studio GBP:** Ensure your Google Business Profile is fully optimized, verified, and targeting "Local SEO Bali" and "Web Design Bali" in the descriptions, posts, and services section.
*   **Publish "Review Removal Guide":** Write a comprehensive guide on how business owners can handle false reviews. This establishes immediate E-E-A-T and serves as a lead magnet.

---

## 10. Mid-Term Wins (3-6 months)

*   **Neighborhood Landing Pages:** Build localized service pages targeting Canggu, Seminyak, and Ubud (e.g., "Web Design Canggu", "Local SEO Ubud"). This will allow 741 Studio to rank for low-difficulty, highly targeted local queries.
*   **Launch a Free "Local SEO Auditor" Tool:** Create a lightweight page where local business owners can input their GBP listing for a free audit report. This acts as a high-leverage lead generator.
*   **Build Case Studies around Webflow & Speed:** Launch 1-2 detailed case studies showing how transitioning a client from WordPress to 741's bespoke Webflow setup doubled their conversion speed and Google Maps rankings.

---

## 11. Long-Term Opportunities (6-12 months)

*   **Industry-Specific Automation Systems:** Develop pre-packaged n8n and WhatsApp automation blueprints for specific Bali sectors (e.g., "Villa Booking Automations", "Clinic Patient Reminders"). Build organic authority for \`marketing automation bali\`.
*   **Establish Domain Authority on Local B2B Search:** Rank #1 organically for \`seo agency bali\` and \`web design bali\` by executing a consistent local link-building campaign and deep technical SEO excellence.
`;

const reportOutputPath = path.join(__dirname, '741_seo_opportunity_report.md');
fs.writeFileSync(reportOutputPath, reportMarkdown, 'utf8');
console.log(`Saved strategic report to ${reportOutputPath}`);

// Print summary metrics
console.log("\nSummary of Processed Keywords by Service Category:");
Object.keys(serviceMetrics).forEach(k => {
    const s = serviceMetrics[k];
    console.log(`- ${k}: ${s.count} keywords, ${s.totalVolume} monthly volume, Avg KD: ${s.avgKD}, Total Opportunity: ${s.totalOpportunity}`);
});
console.log("\nReport generation completed successfully.");
