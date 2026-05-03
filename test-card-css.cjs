const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rules = await page.evaluate(() => {
    const card = document.querySelector('.hr-card-minimax-video');
    const style = window.getComputedStyle(card);
    const heroVidStyle = window.getComputedStyle(document.querySelector('.hero-video'));
    return {
      cardPos: style.position,
      cardFloat: style.float,
      cardDisplay: style.display,
      cardHeight: style.height,
      heroVidPos: heroVidStyle.position,
      heroVidHeight: heroVidStyle.height
    };
  });
  
  console.log('card styles:', rules);
  await browser.close();
})();
