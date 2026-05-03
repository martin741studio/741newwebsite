const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rules = await page.evaluate(() => {
    const parent = document.querySelector('.hr-card-minimax-video');
    parent.style.aspectRatio = '16 / 9';
    parent.style.width = '100%';
    
    // Remove paddings that cause black bars
    const heroVid = document.querySelector('.hero-video');
    heroVid.style.paddingTop = '0';
    heroVid.style.paddingBottom = '0';
    
    return {
      parentH: window.getComputedStyle(parent).height,
      heroVidH: window.getComputedStyle(heroVid).height,
      embedH: window.getComputedStyle(document.querySelector('.hero-vid-embed')).height,
      videoH: window.getComputedStyle(document.querySelector('.hero-vid-embed video')).height
    };
  });
  
  console.log('Heights:', rules);
  await browser.close();
})();
