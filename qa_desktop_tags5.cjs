const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  await new Promise(r => setTimeout(r, 2000));
  
  const tagsLayout = await page.evaluate(() => {
    const nodes = [1, 2, 3, 4, 5, 6].map(n => document.querySelector(`#node${n}`));
    
    return nodes.map((node, i) => {
      if (!node) return { node: i+1, status: 'missing' };
      if (window.getComputedStyle(node).display === 'none') return { node: i+1, status: 'hidden' };
      
      const label = node.querySelector('.hr-node-label');
      if (!label) return { node: i+1, status: 'no-label' };
      
      let media = node.querySelector('img') || node.querySelector('.hero-video');
      
      if (i === 0) media = node.querySelector('._3d-model-holder');
      if (i === 3) media = node.children[1]; // just grab the second child (first is the label)
      if (i === 3 && media.classList.contains('drag-handle')) media = node.children[2];
      
      if (!media) return { node: i+1, status: 'no-media' };
      
      const labelRect = label.getBoundingClientRect();
      const mediaRect = media.getBoundingClientRect();
      
      return {
        node: `node${i+1}`,
        distanceFromMediaTop: Math.round((mediaRect.top - labelRect.bottom) * 100) / 100,
        text: label.innerText
      };
    });
  });
  
  console.log('Desktop Tags Visual Layout:');
  console.table(tagsLayout);
  
  await browser.close();
})();
