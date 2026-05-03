const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  await new Promise(r => setTimeout(r, 1000));
  
  const report = await page.evaluate(() => {
    const video = document.querySelector('.hero-video video');
    const container = document.querySelector('.hero-video');
    const cRect = container ? container.getBoundingClientRect() : null;
    const vRect = video ? video.getBoundingClientRect() : null;
    return {
      container: cRect ? { w: cRect.width, h: cRect.height, ratio: cRect.width/cRect.height } : null,
      video: vRect ? { w: vRect.width, h: vRect.height, ratio: vRect.width/vRect.height } : null,
      videoStyle: video ? { objectFit: window.getComputedStyle(video).objectFit } : null
    };
  });
  
  console.log('Desktop Layout:', report);
  
  await page.setViewport({ width: 390, height: 844 });
  await new Promise(r => setTimeout(r, 500));
  const reportMobile = await page.evaluate(() => {
    const video = document.querySelector('.hero-video video');
    const container = document.querySelector('.hero-video');
    const cRect = container ? container.getBoundingClientRect() : null;
    const vRect = video ? video.getBoundingClientRect() : null;
    return {
      container: cRect ? { w: cRect.width, h: cRect.height, ratio: cRect.width/cRect.height } : null,
      video: vRect ? { w: vRect.width, h: vRect.height, ratio: vRect.width/vRect.height } : null,
      videoStyle: video ? { objectFit: window.getComputedStyle(video).objectFit } : null
    };
  });
  console.log('Mobile Layout:', reportMobile);
  await browser.close();
})();
