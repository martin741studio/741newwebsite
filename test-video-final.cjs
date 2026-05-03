const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rules = await page.evaluate(() => {
    const parent = document.querySelector('.hr-card-minimax-video');
    const heroVid = document.querySelector('.hero-video');
    return {
      parentH: window.getComputedStyle(parent).height,
      heroVidH: window.getComputedStyle(heroVid).height,
      embedH: window.getComputedStyle(document.querySelector('.hero-vid-embed')).height,
      videoH: window.getComputedStyle(document.querySelector('.hero-vid-embed video')).height
    };
  });
  
  console.log('Final Heights:', rules);
  await browser.close();
})();
