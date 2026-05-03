const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const rules = await page.evaluate(() => {
    const video = document.querySelector('.hero-vid-embed video');
    video.style.height = 'auto'; // Remove 100%
    
    // Force layout recalculation
    const parent = document.querySelector('.hr-card-minimax-video');
    return {
      videoH: window.getComputedStyle(video).height,
      parentH: window.getComputedStyle(parent).height
    };
  });
  
  console.log('After fix:', rules);
  await browser.close();
})();
