import fs from 'node:fs';
import path from 'node:path';
import {bundleToSingleHtml,serveStaticProjectHtml,seekCompositionTimeline,waitForRuntimeReady,puppeteer} from './runtime_helpers.mjs';
const film=path.resolve('film');
const contract=JSON.parse(fs.readFileSync('timing-contract.json'));
const server=await serveStaticProjectHtml(film,await bundleToSingleHtml(film));
const browser=await puppeteer.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
const checks=[];
try {
 const page=await browser.newPage();
 await page.setViewport({width:1920,height:1080});
 await page.goto(server.url,{waitUntil:'networkidle0'});
 await waitForRuntimeReady(page,45000);
 for(const a of contract.assertions){
  const t=Math.max(0,a.bySec-.30);
  await seekCompositionTimeline(page,t,{exactTime:true,fallbackToBridgeAndTimelines:true,waitForFontsMs:0});
  const opacity=await page.$eval(a.selector,el=>{let o=1;for(let n=el;n;n=n.parentElement){const s=getComputedStyle(n);o*=Number(s.opacity);if(s.visibility==='hidden'||s.display==='none')o=0;}return o;});
  checks.push({...a,beforeReveal:t,opacity,visible:opacity<.05});
 }
 const result={passed:checks.every(c=>c.visible),checks:checks.length,failures:checks.filter(c=>!c.visible),details:checks};
 fs.writeFileSync('timing-early-validation-v2.json',JSON.stringify(result,null,2));
 console.log(JSON.stringify({passed:result.passed,checks:result.checks,failures:result.failures}));
 if(!result.passed)process.exitCode=1;
}finally{await browser.close();await server.close();}
