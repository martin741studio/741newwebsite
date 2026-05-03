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
    return nodes.map(n => {
      const style = window.getComputedStyle(n);
      return {
        id: n.id,
        display: style.display,
        opacity: style.opacity,
        position: style.position,
        top: n.getBoundingClientRect().top,
        height: n.getBoundingClientRect().height
      };
    });
  });
  
  console.log(layout);
  await browser.close();
})();
