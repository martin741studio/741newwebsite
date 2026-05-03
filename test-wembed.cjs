const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rules = await page.evaluate(() => {
    const embed = document.querySelector('.hero-vid-embed');
    const style = window.getComputedStyle(embed);
    return {
      display: style.display,
      float: style.float,
      overflow: style.overflow,
      height: style.height,
      minHeight: style.minHeight,
      paddingBottom: style.paddingBottom,
    };
  });
  
  console.log('w-embed styles:', rules);
  await browser.close();
})();
