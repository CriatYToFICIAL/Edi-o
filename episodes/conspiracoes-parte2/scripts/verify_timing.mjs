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
  await seekCompositionTimeline(page,a.bySec,{exactTime:true,fallbackToBridgeAndTimelines:true,waitForFontsMs:0});
  const state=await page.evaluate(sel=>{
   const el=document.querySelector(sel); if(!el)return {visible:false,reason:'missing'};
   let opacity=1;for(let n=el;n;n=n.parentElement){const s=getComputedStyle(n);opacity*=Number(s.opacity);if(s.display==='none'||s.visibility==='hidden')opacity=0;}
   const r=el.getBoundingClientRect();return {visible:opacity>.9&&r.width>0&&r.height>0&&r.right>0&&r.left<1920&&r.bottom>0&&r.top<1080,opacity};
  },a.selector);
  checks.push({...a,...state});
 }
 // Reverse seeks must also reproduce the same visible state.
 for(const a of [...contract.assertions].reverse().filter((_,i)=>i%10===0)){
  await seekCompositionTimeline(page,a.bySec,{exactTime:true,fallbackToBridgeAndTimelines:true,waitForFontsMs:0});
  const opacity=await page.$eval(a.selector,e=>Number(getComputedStyle(e).opacity));
  checks.push({...a,reverseSeek:true,visible:opacity>.9,opacity});
 }
 const result={passed:checks.every(c=>c.visible),checks:checks.length,failures:checks.filter(c=>!c.visible),details:checks};
 fs.writeFileSync('timing-validation.json',JSON.stringify(result,null,2));
 console.log(JSON.stringify({passed:result.passed,checks:result.checks,failures:result.failures}));
 if(!result.passed)process.exitCode=1;
}finally{await browser.close();await server.close();}
