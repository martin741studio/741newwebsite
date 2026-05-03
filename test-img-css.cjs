const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rules = await page.evaluate(() => {
    const cards = document.querySelectorAll('.reveal-item');
    return Array.from(cards).map(card => {
      const style = window.getComputedStyle(card);
      return {
        id: card.id,
        h: style.height,
        minH: style.minHeight
      };
    });
  });
  
  console.log('card styles:', rules);
  await browser.close();
})();
