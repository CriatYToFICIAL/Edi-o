"""Freeze additional photographic material with provenance. Reject irrelevant search hits."""
import concurrent.futures,json,urllib.request
from pathlib import Path
rows=[
('intitle-quadcopter.json',4,'drone.jpg'),
('intitle-cctv-intitle-camera.json',2,'cctv.jpg'),
('intitle-smartbird.json',1,'smartbird.jpg'),
('intitle-flock-intitle-geese.json',3,'geese.jpg'),
('intitle-amazing-intitle-stories-1926.json',0,'scifi.jpg'),
('intitle-antarctica-intitle-coast.json',1,'ice.jpg'),
('intitle-ocean-intitle-horizon.json',2,'horizon.jpg'),
('intitle-milky-intitle-way.json',0,'galaxy.jpg'),
('intitle-united-intitle-states-intitle-capitol.json',1,'capitol.jpg'),
('intitle-new-york-times-intitle-building.json',3,'nyt.jpg'),
('intitle-pendulum.json',0,'pendulum.gif'),
('intitle-nasa-intitle-logo.json',5,'nasa.png'),
('intitle-galileo-intitle-portrait.json',0,'galileo.jpg'),
('intitle-reptilian-intitle-sign.json',0,'conspiracy-sign.jpg')]
def fetch(row):
 query,index,name=row;r=json.loads((Path('research')/query).read_text())[index]
 url=(r['original_url'] if name.endswith('.gif') else r['url']).split('?')[0]
 req=urllib.request.Request(url,headers={'User-Agent':'NarrativeVideoResearch/1.0'})
 with urllib.request.urlopen(req,timeout=45) as response:data=response.read()
 target=Path('film/public/media/revision')/name;target.write_bytes(data)
 r.update(file='public/media/revision/'+name,download_url=url,reviewed=False)
 print(name,r['license'],flush=True);return r
records=json.loads(Path('asset-ledger.json').read_text())
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(fetch,rows):records.append(r)
records=list({r['file']:r for r in records}.values())
Path('asset-ledger.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
