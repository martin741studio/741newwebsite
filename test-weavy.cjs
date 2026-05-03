const fs = require('fs');
const content = fs.readFileSync('04_site/assets/weavy.css', 'utf8');
const lines = content.split('\n');
let inMobile = false;
for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes('@media screen and (max-width: 767px)')) {
    inMobile = true;
  }
  if (inMobile && lines[i].includes('@media screen and')) {
    if (!lines[i].includes('max-width: 767px')) inMobile = false;
  }
  if (inMobile && lines[i].includes('node4')) {
    console.log(`Line ${i}: ${lines[i]}`);
    for(let j=1; j<10; j++) {
      console.log(`Line ${i+j}: ${lines[i+j]}`);
      if(lines[i+j].includes('}')) break;
    }
  }
}
