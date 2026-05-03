const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rules = await page.evaluate(() => {
    const el = document.querySelector('#node1');
    const rect = el.getBoundingClientRect();
    const style = window.getComputedStyle(el);
    return {
      rectHeight: rect.height,
      offsetHeight: el.offsetHeight,
      clientHeight: el.clientHeight,
      marginTop: style.marginTop,
      marginBottom: style.marginBottom,
      transform: style.transform
    };
  });
  
  console.log(rules);
  await browser.close();
})();
