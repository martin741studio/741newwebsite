const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rule = await page.evaluate(() => {
    const el = document.querySelector('#node4');
    if (!el) return 'Not found';
    
    // Check matched rules
    const rules = window.getMatchedCSSRules ? window.getMatchedCSSRules(el) : [];
    let source = 'unknown';
    
    // In Puppeteer, getting the matched rule might be tricky without CDP.
    // Let's just check if it has a class that sets display: none
    for (const sheet of Array.from(document.styleSheets)) {
      try {
        const cssRules = sheet.cssRules || sheet.rules;
        if (cssRules) {
          for (const cssRule of Array.from(cssRules)) {
            if (cssRule.selectorText && el.matches(cssRule.selectorText)) {
              if (cssRule.style.display === 'none') {
                 source = cssRule.selectorText;
              }
            }
          }
        }
      } catch (e) {
        // CORS or similar
      }
    }
    
    return {
      display: window.getComputedStyle(el).display,
      source: source
    };
  });
  
  console.log(rule);
  await browser.close();
})();
