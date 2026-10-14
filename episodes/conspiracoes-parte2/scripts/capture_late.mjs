import fs from 'node:fs';
import path from 'node:path';
import {bundleToSingleHtml,serveStaticProjectHtml,seekCompositionTimeline,waitForRuntimeReady,puppeteer} from './runtime_helpers.mjs';
const film=path.resolve('film');
const server=await serveStaticProjectHtml(film,await bundleToSingleHtml(film));
const browser=await puppeteer.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
try{
 const page=await browser.newPage();await page.setViewport({width:1920,height:1080});
 await page.goto(server.url,{waitUntil:'networkidle0'});await waitForRuntimeReady(page,45000);
 const plan=JSON.parse(fs.readFileSync('material-plan.json'));fs.mkdirSync('qc-late',{recursive:true});
 for(let i=0;i<plan.length;i++){
  await seekCompositionTimeline(page,plan[i].end-.22,{exactTime:true,fallbackToBridgeAndTimelines:true,waitForFontsMs:0});
  await page.screenshot({path:`qc-late/scene-${String(i).padStart(2,'0')}.jpg`,type:'jpeg',quality:70});
 }
 console.log(`Captured ${plan.length} late scene frames`);
}finally{await browser.close();await server.close();}
