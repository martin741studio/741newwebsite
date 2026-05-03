const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const html = await page.evaluate(() => {
    return document.querySelector('#node6').outerHTML.substring(0, 300);
  });
  
  console.log('HTML:', html);
  await browser.close();
})();
