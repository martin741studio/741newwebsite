const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const layout = await page.evaluate(() => {
    const container = document.querySelector('.hero-draggbles-comp');
    if (!container) return { error: 'No container' };
    
    const nodes = Array.from(container.querySelectorAll('.reveal-item'));
    const results = nodes.map(n => {
      const rect = n.getBoundingClientRect();
      const label = n.querySelector('.hr-node-label');
      const labelRect = label ? label.getBoundingClientRect() : null;
      return {
        id: n.id,
        top: rect.top,
        bottom: rect.bottom,
        height: rect.height,
        labelTop: labelRect ? labelRect.top : null,
        labelHeight: labelRect ? labelRect.height : null
      };
    });
    
    // Sort by visual top position
    results.sort((a, b) => a.top - b.top);
    
    // Check overlaps
    const overlaps = [];
    for (let i = 0; i < results.length - 1; i++) {
      const current = results[i];
      const next = results[i+1];
      // On mobile, flex direction is column, so next item should be BELOW current item
      // Next item's top (or its label's top) should be >= current item's bottom
      const nextTopmost = next.labelTop !== null ? Math.min(next.top, next.labelTop) : next.top;
      if (nextTopmost < current.bottom) {
        overlaps.push(`Overlap between ${current.id} and ${next.id}: Current bottom is ${current.bottom}, next topmost is ${nextTopmost}`);
      }
    }
    
    return {
      containerHeight: container.getBoundingClientRect().height,
      nodes: results,
      overlaps: overlaps
    };
  });
  
  console.log(JSON.stringify(layout, null, 2));
  await browser.close();
})();
