const fs = require('fs');
const path = require('path');
const puppeteer = require('/workspace/.tools/hyperframes/node_modules/puppeteer-core');
const dir = path.resolve(__dirname, '../film/public/art/v2');
(async () => {
 const browser = await puppeteer.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage']});
 const page = await browser.newPage();
 await page.setViewport({width:1280,height:1120,deviceScaleFactor:1});
 const names = JSON.parse(fs.readFileSync(path.join(dir,'inventory.json'),'utf8')).map(x=>x.file);
 await page.setContent('<style>body{margin:0;background:#f6f6f1;display:grid;grid-template-columns:repeat(4,320px);font:18px sans-serif}section{text-align:center;height:280px}svg{display:block;width:320px;height:250px}</style>'+names.map(n=>'<section>'+fs.readFileSync(path.join(dir,n),'utf8')+n+'</section>').join(''));
 await page.screenshot({path:'/tmp/art-v2-contact.png'});
 await browser.close();
})();
