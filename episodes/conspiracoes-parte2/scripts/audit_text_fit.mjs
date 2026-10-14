// Detect actual line-box clipping at complete entrance, midpoint, and late frame.
import fs from 'node:fs';
import path from 'node:path';
import {bundleToSingleHtml,serveStaticProjectHtml,seekCompositionTimeline,waitForRuntimeReady,puppeteer} from './runtime_helpers.mjs';
const film=path.resolve('film');
const server=await serveStaticProjectHtml(film,await bundleToSingleHtml(film));
const browser=await puppeteer.launch({executablePath:process.env.HYPERFRAMES_BROWSER_PATH||'/usr/bin/chromium',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
const plan=JSON.parse(fs.readFileSync('material-plan.json'));
const results=[];
try{
 const page=await browser.newPage();await page.setViewport({width:1920,height:1080});
 await page.goto(server.url,{waitUntil:'networkidle0'});await waitForRuntimeReady(page,45000);
 for(let i=0;i<plan.length;i++){
  const s=plan[i];const times=[Math.min(s.end-.2,s.start+.4),(s.start+s.end)/2,s.end-.23];
  for(const time of times){
   await seekCompositionTimeline(page,time,{exactTime:true,fallbackToBridgeAndTimelines:true,waitForFontsMs:0});
   const issues=await page.evaluate(()=>{
    const errors=[];
    const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    for(let n;n=walker.nextNode();){
     if(!n.textContent.trim()||!n.parentElement||n.parentElement.closest('script,style,.overview'))continue;
     let visible=true,opacity=1;const ancestors=[];
     for(let e=n.parentElement;e;e=e.parentElement){
      const c=getComputedStyle(e);opacity*=Number(c.opacity);if(c.display==='none'||c.visibility==='hidden')visible=false;
      if(c.overflowX!=='visible'||c.overflowY!=='visible')ancestors.push({el:e,css:c});
     }
     if(!visible||opacity<.9)continue;
     const range=document.createRange();range.selectNodeContents(n);
     for(const r of range.getClientRects()){
      if(!r.width||!r.height)continue;
      let reason=null;
      if(r.left<-3||r.right>1923||r.top<-3||r.bottom>1083)reason='outside canvas';
      for(const a of ancestors){
       const p=a.el.getBoundingClientRect();
       if(a.css.overflowX!=='visible'&&(r.left<p.left-3||r.right>p.right+3))reason='horizontal clipping by '+(a.el.id||a.el.className);
       if(a.css.overflowY!=='visible'&&(r.top<p.top-3||r.bottom>p.bottom+3))reason='vertical clipping by '+(a.el.id||a.el.className);
      }
      if(reason)errors.push({text:n.textContent.trim(),reason,box:{left:r.left,top:r.top,right:r.right,bottom:r.bottom}});
     }
    }
    return errors;
   });
   results.push({scene:i,time,issues});
  }
 }
 const failures=results.filter(r=>r.issues.length);const report={passed:!failures.length,samples:results.length,failures};
 fs.writeFileSync('text-fit-validation-v2.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report));
 if(failures.length)process.exitCode=1;
}finally{await browser.close();await server.close();}
