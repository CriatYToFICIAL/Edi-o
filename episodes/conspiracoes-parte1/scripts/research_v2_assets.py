"""Download explicitly selected Commons assets with provenance, separately from V1."""
import json, re, urllib.request, time
from pathlib import Path
base=Path(__file__).resolve().parents[1]
out=base/'film/public/media/v2'; out.mkdir(parents=True,exist_ok=True)
research=base/'research-v2'; research.mkdir(exist_ok=True)
selections=[('apollo-11-crew-portrait',0,'apollo-crew.jpg'),('apollo-11-launch',0,'apollo-launch.jpg'),('apollo-11-launch',7,'apollo-launch.gif'),('apollo-11-lunar-module',0,'lunar-module.jpg'),('apollo-11-lunar-module',2,'bootprint.jpg'),('apollo-mission-control-1969',6,'mission-control.jpg'),('apollo-11-filetype-video',6,'aldrin-steps.ogv'),('helsinki-parliament-house',2,'parliament.jpg'),('baltic-sea-map',1,'historical-scandinavia.jpg'),('baltic-sea-map',7,'baltic-map.png'),('groom-lake-desert',1,'area51-region.png'),('groom-lake-road-sign',1,'extraterrestrial-highway.jpg'),('reddit-logo',0,'reddit-logo.svg'),('illuminati--weishaupt',5,'minerval.png'),('adam-weishaupt-portrait',1,'weishaupt-engraving.jpg'),('fishing-baltic-trawler',0,'helsinki-fishing-market.png')]
selections += [('finnish-declaration-independence',0,'finland-declaration.jpg'),('illuminati-bavarian-order',0,'illuminati-history.jpg')]
ledger=[]
for query,i,name in selections:
    item=json.loads((base/'research'/f'{query}.json').read_text())[i]
    url=(item['original_url'] if name.endswith(('.gif','.ogv','.svg')) else item['url']).split('?')[0]
    row=dict(filename='public/media/v2/'+name,author=re.sub('<[^>]+>','',item.get('artist') or ''),license=item['license'],sourcepage=item['page'],url=url,description=re.sub('<[^>]+>','',item.get('description') or ''))
    try:
        if not (out/name).exists():
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'NarrativeVideoResearch/1.0'}),timeout=60) as response: (out/name).write_bytes(response.read())
        row['status']='downloaded'; print(name,(out/name).stat().st_size,flush=True)
    except Exception as exc: row['status']='failed';row['error']=str(exc);print(name,str(exc),flush=True)
    ledger.append(row)
    (research/'assets.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2))
    time.sleep(1)
