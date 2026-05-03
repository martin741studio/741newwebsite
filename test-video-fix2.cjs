const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rules = await page.evaluate(() => {
    const parent = document.querySelector('.hero-video');
    parent.style.height = '300px';
    
    return {
      parentH: window.getComputedStyle(document.querySelector('.hr-card-minimax-video')).height,
      videoH: window.getComputedStyle(document.querySelector('.hero-vid-embed video')).height
    };
  });
  
  console.log('After explicitly setting height to 300px:', rules);
  await browser.close();
})();
