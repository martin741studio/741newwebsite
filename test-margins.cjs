const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rules = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.reveal-item')).map(n => {
      const style = window.getComputedStyle(n);
      return {
        id: n.id,
        marginTop: style.marginTop,
        marginBottom: style.marginBottom,
        order: style.order
      };
    });
  });
  
  console.log(rules);
  await browser.close();
})();
