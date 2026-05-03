const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '04_site/sections/hero.html');
let content = fs.readFileSync(filePath, 'utf8');

// Replace node 1 (3D RODIN)
content = content.replace(
  /<div\s+style="position:\s*absolute;\s*top:\s*calc\(-30px\s*\+\s*1rem\);[^>]+>\s*<span[^>]+>3D<\/span>&nbsp;&nbsp;<span[^>]+>RODIN 2\.0<\/span>\s*<\/div>/g,
  '<div class="hr-node-label"><span class="bold-txt">3D</span><span class="light-txt">RODIN 2.0</span></div>'
);

// Replace node 2 (COLOR REFERENCE)
content = content.replace(
  /<div\s+style="position:\s*absolute;\s*top:\s*calc\(-30px\s*-\s*4\.5486rem\);[^>]+>\s*<span[^>]+>COLOR<\/span>&nbsp;&nbsp;<span[^>]+>REFERENCE<\/span>\s*<\/div>/g,
  '<div class="hr-node-label"><span class="bold-txt">COLOR</span><span class="light-txt">REFERENCE</span></div>'
);

// Replace node 3 (IMAGE STABLE DIFFUSION)
content = content.replace(
  /<div\s+style="position:\s*absolute;\s*top:\s*-30px;[^>]+>\s*<span[^>]+>IMAGE<\/span>&nbsp;&nbsp;<span[^>]+>STABLE DIFFUSION<\/span>\s*<\/div>/g,
  '<div class="hr-node-label"><span class="bold-txt">IMAGE</span><span class="light-txt">STABLE DIFFUSION</span></div>'
);

// Replace node 5 (IMAGE FLUX PRO 1.1)
content = content.replace(
  /<div\s+style="position:\s*absolute;\s*top:\s*calc\(-30px\s*\+\s*2\.2917rem\);[^>]+>\s*<span[^>]+>IMAGE<\/span>&nbsp;&nbsp;<span[^>]+>FLUX PRO 1\.1<\/span>\s*<\/div>/g,
  '<div class="hr-node-label"><span class="bold-txt">IMAGE</span><span class="light-txt">FLUX PRO 1.1</span></div>'
);

// Replace node 4 (TEXT PROMPT)
content = content.replace(
  /<div\s+style="position:\s*absolute;\s*top:\s*-38px;[^>]+>\s*<span[^>]+>TEXT<\/span>&nbsp;&nbsp;<span[^>]+>PROMPT<\/span>\s*<\/div>/g,
  '<div class="hr-node-label"><span class="bold-txt">TEXT</span><span class="light-txt">PROMPT</span></div>'
);

// Replace node 6 (VIDEO MINIMAX VIDEO)
// Note: In 04_site/sections/hero.html node 6 might already be partially modified or have the label.
// In the current file it is:
// <div
//   style="position: absolute; top: calc(-30px + 1.5rem); left: 0px; font-family: inherit; font-size: 0.8rem; letter-spacing: 0.08em; text-transform: uppercase; white-space: nowrap; z-index: 10;">
//   <span style="font-weight: 700; color: #111;">VIDEO</span>&nbsp;&nbsp;<span style="font-weight: 400; color: #555;">MINIMAX VIDEO</span>
// </div>
content = content.replace(
  /<div\s+style="position:\s*absolute;\s*top:\s*calc\(-30px\s*\+\s*1\.5rem\);[^>]+>\s*<span[^>]+>VIDEO<\/span>&nbsp;&nbsp;<span[^>]+>MINIMAX VIDEO<\/span>\s*<\/div>/g,
  '<div class="hr-node-label"><span class="bold-txt">VIDEO</span><span class="light-txt">MINIMAX VIDEO</span></div>'
);

// Add CSS to the top of <style>
const cssRule = `
      .hr-node-label {
        position: absolute;
        top: -30px;
        left: 0px;
        font-family: inherit;
        font-size: 0.65rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        white-space: nowrap;
        z-index: 10;
      }
      .hr-node-label .bold-txt {
        font-weight: 800;
        color: #111;
        margin-right: 1.5rem;
      }
      .hr-node-label .light-txt {
        font-weight: 600;
        color: #555;
      }
`;

if (!content.includes('.hr-node-label {')) {
  content = content.replace('<style>', '<style>' + cssRule);
}

fs.writeFileSync(filePath, content);
console.log('Labels unified successfully!');
