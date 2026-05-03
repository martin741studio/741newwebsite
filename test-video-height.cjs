const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const dims = await page.evaluate(() => {
    const card = document.querySelector('.hr-card-minimax-video');
    const heroVid = document.querySelector('.hero-video');
    const embed = document.querySelector('.hero-vid-embed');
    const video = document.querySelector('.hero-vid-embed video');
    return {
      card: card ? { h: card.clientHeight, w: card.clientWidth } : null,
      heroVid: heroVid ? { h: heroVid.clientHeight, w: heroVid.clientWidth } : null,
      embed: embed ? { h: embed.clientHeight, w: embed.clientWidth } : null,
      video: video ? { h: video.clientHeight, w: video.clientWidth } : null,
    };
  });
  
  console.log('Mobile 390px Viewport Dimensions:', dims);
  await browser.close();
})();
