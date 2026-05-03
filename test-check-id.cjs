const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rules = await page.evaluate(() => {
    return {
      node6Class: document.querySelector('#node6').className,
      node6Length: document.querySelectorAll('#node6').length
    };
  });
  
  console.log('ID check:', rules);
  await browser.close();
})();
