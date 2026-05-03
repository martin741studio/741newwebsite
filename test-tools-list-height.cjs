const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  await new Promise(r => setTimeout(r, 2000));
  
  const layout = await page.evaluate(() => {
    const list = document.querySelector('.splide.tools-image .splide__list');
    const slide = document.querySelector('.splide.tools-image .splide__slide');
    const pill = document.querySelector('.splide.tools-image .slider-pill');
    const imgWrapper = document.querySelector('.splide.tools-image .slider-pill_img');
    const img = document.querySelector('.splide.tools-image .slider-pill_photo');
    
    return {
      list: list ? list.getBoundingClientRect().height : null,
      slide: slide ? slide.getBoundingClientRect().height : null,
      pill: pill ? pill.getBoundingClientRect().height : null,
      imgWrapper: imgWrapper ? imgWrapper.getBoundingClientRect().height : null,
      img: img ? img.getBoundingClientRect().height : null
    };
  });
  
  console.log('Layout:', layout);
  await browser.close();
})();
