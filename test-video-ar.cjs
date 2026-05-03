const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'networkidle2' });
  
  const ar = await page.evaluate(() => {
    const video = document.querySelector('.hero-vid-embed video');
    return {
      vw: video.videoWidth,
      vh: video.videoHeight
    };
  });
  
  console.log('Video dimensions:', ar);
  await browser.close();
})();
