const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rules = await page.evaluate(() => {
    const parent = document.querySelector('.hr-card-minimax-video');
    const style = window.getComputedStyle(parent);
    return {
      display: style.display,
      flexDirection: style.flexDirection,
      flexGrow: style.flexGrow,
      height: style.height,
      minHeight: style.minHeight,
    };
  });
  
  console.log('parent styles:', rules);
  await browser.close();
})();
