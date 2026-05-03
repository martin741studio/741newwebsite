const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'networkidle2' });
  
  // Scroll down to trigger animations
  await page.evaluate(() => window.scrollTo(0, 1000));
  await new Promise(r => setTimeout(r, 2000)); // wait for GSAP
  
  const layout = await page.evaluate(() => {
    const container = document.querySelector('.hero-draggbles-comp');
    if (!container) return { error: 'No container' };
    
    const nodes = Array.from(container.querySelectorAll('.reveal-item')).filter(n => window.getComputedStyle(n).display !== 'none');
    const results = nodes.map(n => {
      const rect = n.getBoundingClientRect();
      const label = n.querySelector('.hr-node-label');
      const labelRect = label ? label.getBoundingClientRect() : null;
      return {
        id: n.id,
        top: rect.top,
        bottom: rect.bottom,
        labelTop: labelRect ? labelRect.top : null,
      };
    });
    
    results.sort((a, b) => a.top - b.top);
    
    const overlaps = [];
    for (let i = 0; i < results.length - 1; i++) {
      const current = results[i];
      const next = results[i+1];
      const nextTopmost = next.labelTop !== null ? Math.min(next.top, next.labelTop) : next.top;
      if (nextTopmost < current.bottom) {
        overlaps.push(`Overlap between ${current.id} and ${next.id}: Current bottom is ${current.bottom}, next topmost is ${nextTopmost}`);
      }
    }
    
    return overlaps;
  });
  
  console.log('Overlaps after scroll:', layout);
  await browser.close();
})();
