const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  await new Promise(r => setTimeout(r, 1000));
  
  await page.evaluate(() => {
    const node6 = document.querySelector('#node6');
    if (node6) node6.scrollIntoView({ behavior: 'instant', block: 'center' });
  });
  
  await new Promise(r => setTimeout(r, 1500));
  
  const report = await page.evaluate(() => {
    const node6 = document.querySelector('#node6');
    const video = document.querySelector('.hero-video video');
    const videoContainer = document.querySelector('.hero-video');
    
    return {
      desktopContainer: videoContainer.getBoundingClientRect(),
      desktopVideo: video.getBoundingClientRect()
    };
  });
  
  console.log('Desktop Layout:', report);
  await browser.close();
})();
