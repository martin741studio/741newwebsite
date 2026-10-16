# Maria Brasse (ShuiGuru) — Approved Copy & FAQ Updates

Date: 2026-10-16  
Client ID: `444ac77b-747d-4855-89e5-12ac97d2363c`  
Website: `https://shuiguru.de`  
Approved by: Maria Brasse (Decision decisions on 2026-10-15)  

---

## 1. Page: `/ueber-mich-maria-brasse/` (Decision E2)

### Context & Goal
- **Keyword Focus:** „feng shui berater“ (320 searches/mo) & „feng shui beratung“ (260 searches/mo).
- **Placement:** Under the existing section `## Häufige Fragen`.
- **Status:** Variant 1 approved with Maria's custom edit (*"...und warum er sie in ihren Zielen bremst."*).

### Content to Insert

```html
<div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
  <h3 itemprop="name">Was macht eine Feng-Shui-Beraterin?</h3>
  <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
    <div itemprop="text">
      <p>Was macht eine Feng-Shui-Beraterin? Ich schaue mir an, wie Menschen einen Raum tatsächlich nutzen und warum er sie in ihren Zielen bremst. Dazu erfasse ich Gebäude, Grundstück und die Geschichte des Ortes, arbeite mit den vier Himmelsrichtungen und Elementen und übersetze das in <a href="https://shuiguru.de/#angebotsuebersicht">konkrete Schritte</a>: Was wird umgestellt, was kommt weg, was fehlt. Sie bekommen keine Regelliste, sondern eine Rückmeldung für genau Ihren Raum.</p>
      <p><a href="https://shuiguru.de/kaeffchen/" class="btn-link">Käffchen vereinbaren →</a></p>
    </div>
  </div>
</div>
```

---

## 2. Page: `/feng-shui-garten/` (Decision E3)

### Context & Goal
- **Keyword Focus:** „feng shui garten schutz vor nachbarn“ (90 searches/mo).
- **Placement:** Under section `## Häufige Fragen` (and cross-referenced under `## Ruheplätze richtig setzen`).
- **Status:** Variant 1 approved with Maria's complete rewritten text.

### Content to Insert

```html
<div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
  <h3 itemprop="name">Wie schütze ich meinen Garten vor den Blicken der Nachbarn?</h3>
  <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
    <div itemprop="text">
      <p>Schutz muss keine Mauer sein. Probleme zu Nachbarn können vielschichtig und vor allem emotional sein. Erst wenn das genau geklärt ist, können Entscheidungen getroffen werden, denn Hecken und Zäune schützen vor Streit nicht, aber vor einfachen Blicken. Rankgerüste und Bepflanzungen machen nur in den gemeinsamen Verhältnissen Sinn. <a href="https://shuiguru.de/meine-philosophie/">Schamanisches Feng Shui</a> zielt auf die innere Ruhe und Sicherheit der <a href="https://shuiguru.de/hoefe-und-hofgemeinschaften/">Gartenbesitzer</a> ab und weniger auf das Gewinnen von nachbarschaftlichen Auseinandersetzungen.</p>
      <p><a href="https://shuiguru.de/kaeffchen/" class="btn-link">Käffchen vereinbaren →</a></p>
    </div>
  </div>
</div>
```

---

## 3. SEO Schema.org JSON-LD (To Add to Head)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Was macht eine Feng-Shui-Beraterin?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Was macht eine Feng-Shui-Beraterin? Ich schaue mir an, wie Menschen einen Raum tatsächlich nutzen und warum er sie in ihren Zielen bremst. Dazu erfasse ich Gebäude, Grundstück und die Geschichte des Ortes, arbeite mit den vier Himmelsrichtungen und Elementen und übersetze das in konkrete Schritte: Was wird umgestellt, was kommt weg, was fehlt. Sie bekommen keine Regelliste, sondern eine Rückmeldung für genau Ihren Raum."
      }
    }
  ]
}
```
