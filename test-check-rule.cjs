const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rule = await page.evaluate(() => {
    const parent = document.querySelector('.hr-card-minimax-video');
    const heroVid = document.querySelector('.hr-card-minimax-video .hero-video');
    const computedParent = window.getComputedStyle(parent);
    const computedHeroVid = window.getComputedStyle(heroVid);
    return {
      parentHeight: computedParent.height,
      parentAspect: computedParent.aspectRatio,
      heroVidHeight: computedHeroVid.height,
      heroVidPadding: computedHeroVid.paddingTop
    };
  });
  
  console.log('Rules:', rule);
  await browser.close();
})();
