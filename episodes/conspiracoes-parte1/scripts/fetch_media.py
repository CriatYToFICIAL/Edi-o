import json
import sys
import urllib.request
import urllib.error
import time
from pathlib import Path

query_file, selection, name = sys.argv[1:4]
asset = json.loads(Path(query_file).read_text())[int(selection)]
target = Path('film/public/media')
target.mkdir(parents=True,exist_ok=True)
download_url = asset['url'] if name.lower().endswith(('.jpg','.png')) else asset['original_url']
download_url = download_url.split('?')[0]
request = urllib.request.Request(download_url,headers={'User-Agent':'NarrativeVideoResearch/1.0'})
for attempt in range(4):
    try:
        with urllib.request.urlopen(request,timeout=45) as response:
            (target/name).write_bytes(response.read())
        break
    except urllib.error.HTTPError as error:
        if error.code != 429 or attempt == 3:
            raise
        wait = int(error.headers.get('Retry-After', 3 * (attempt + 1)))
        if wait > 30:
            raise
        time.sleep(wait)
manifest = Path('asset-ledger.json')
items = json.loads(manifest.read_text()) if manifest.exists() else []
asset.update({'file':'public/media/'+name,'download_url':download_url,'reviewed':False})
items = [item for item in items if item['file'] != asset['file']]+[asset]
manifest.write_text(json.dumps(items,ensure_ascii=False,indent=2))
print(name,asset['title'],asset['license'])
