const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const styles = await page.evaluate(() => {
    const embed = document.querySelector('.hero-vid-embed');
    const video = document.querySelector('.hero-vid-embed video');
    return {
      embedPos: window.getComputedStyle(embed).position,
      embedHeight: window.getComputedStyle(embed).height,
      videoPos: window.getComputedStyle(video).position,
      videoHeight: window.getComputedStyle(video).height
    };
  });
  
  console.log('Styles:', styles);
  await browser.close();
})();
