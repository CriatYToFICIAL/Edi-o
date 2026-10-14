"""Download selected, licensed assets with complete source records."""
import concurrent.futures, html, json, re, urllib.request
from pathlib import Path

items=[
('intitle-birds-intitle-real.json',1,'movement-logo.png'),
('intitle-birds-intitle-real.json',2,'movement-sign.jpg'),
('intitle-peter-intitle-mcindoe.json',0,'peter.png'),
('intitle-birds-intitle-wire.json',0,'wire-birds.jpg'),
('intitle-common-intitle-raven.json',5,'raven.jpg'),
('intitle-david-intitle-icke.json',0,'icke.jpg'),
('intitle-chameleon.json',1,'chameleon.jpg'),
('intitle-frilled-intitle-lizard.json',1,'lizard.jpg'),
('intitle-flat-intitle-earth.json',0,'ferguson.jpg'),
('intitle-flat-intitle-earth.json',2,'flat-theory.png'),
('intitle-earth-intitle-blue-intitle-marble.json',0,'blue-marble.jpg'),
('intitle-earth-intitle-iss.json',4,'orbit.jpg'),
('file-rotating-earth--large--gif.json',0,'earth-spin.gif')]
def fetch(row):
    query,index,name=row;record=json.loads((Path('research')/query).read_text())[index]
    url=record['original_url'] if name.endswith('.gif') else record['url']
    url=url.split('?')[0]
    req=urllib.request.Request(url,headers={'User-Agent':'NarrativeVideoResearch/1.0'})
    with urllib.request.urlopen(req,timeout=50) as r:content=r.read()
    (Path('film/public/media')/name).write_bytes(content)
    record.update(file='public/media/'+name,download_url=url,reviewed=False)
    print(name,record['license'],flush=True);return record
records=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
    for future in ex.map(fetch,items):records.append(future)
icons={'camera':'1F4F9','microphone':'1F3A4','battery':'1F50B','satellite':'1F6F0','microscope':'1F52C','snake':'1F40D','speech':'1F4AC','tools':'1F6E0','globe':'1F30D','bird-icon':'1F426'}
for name,code in icons.items():
    url=f'https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/svg/{code}.svg'
    try:
        with urllib.request.urlopen(url,timeout=30) as r:content=r.read()
        (Path('film/public/art')/(name+'.svg')).write_bytes(content)
        records.append(dict(file='public/art/'+name+'.svg',title='OpenMoji '+name,page='https://openmoji.org/',download_url=url,artist='OpenMoji contributors',license='CC BY-SA 4.0',reviewed=False))
        print('icon',name,flush=True)
    except Exception as e:print('Unavailable',name,str(e),flush=True)
Path('asset-ledger.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
