// QA helpers resolve from the pinned local dependency, not this cloud's tool paths.
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const require=createRequire(path.resolve('film/package.json'));
const dist=path.join(path.dirname(require.resolve('hyperframes/package.json')),'dist');
async function exported(name){
 for(const file of fs.readdirSync(dist).filter(f=>f.endsWith('.js'))){
  const source=fs.readFileSync(path.join(dist,file),'utf8');
  const blocks=[...source.matchAll(/export\s*\{([^}]+)\}/g)];
  if(blocks.some(b=>b[1].split(',').some(s=>s.trim()===name))){
   const module=await import(pathToFileURL(path.join(dist,file)).href);
   if(module[name])return module[name];
  }
 }
 throw new Error(`Pinned HyperFrames helper not found: ${name}`);
}
export const bundleToSingleHtml=await exported('bundleToSingleHtml');
export const serveStaticProjectHtml=await exported('serveStaticProjectHtml');
export const seekCompositionTimeline=await exported('seekCompositionTimeline');
export const waitForRuntimeReady=await exported('waitForRuntimeReady');
export const puppeteer=require('puppeteer-core');
