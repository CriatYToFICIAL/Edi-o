"""Search Wikimedia Commons with provenance; selection remains editorial."""
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

query = ' '.join(sys.argv[1:])
params = dict(action='query',format='json',generator='search',gsrnamespace=6,
              gsrsearch=query,gsrlimit=8,prop='imageinfo',iiprop='url|extmetadata',iiurlwidth=1200)
if query.startswith('File:'):
    params = dict(action='query',format='json',titles=query,prop='imageinfo',
                  iiprop='url|extmetadata',iiurlwidth=1200)
url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(params)
req = urllib.request.Request(url,headers={'User-Agent':'NarrativeVideoResearch/1.0 (editorial reference research)'})
with urllib.request.urlopen(req,timeout=30) as response:
    data = json.load(response)
results = []
for page in sorted(data.get('query',{}).get('pages',{}).values(),key=lambda p:p.get('index',0)):
    info = page.get('imageinfo',[{}])[0]
    metadata = info.get('extmetadata',{})
    result = {'title':page['title'],'url':info.get('thumburl',info.get('url')),
              'page':info.get('descriptionurl'),'original_url':info.get('url'),
              'license':metadata.get('LicenseShortName',{}).get('value'),
              'artist':metadata.get('Artist',{}).get('value'),
              'description':metadata.get('ImageDescription',{}).get('value')}
    results.append(result)
Path('research').mkdir(exist_ok=True)
slug = ''.join(c if c.isalnum() else '-' for c in query).strip('-').lower()
Path('research',slug+'.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
for n,item in enumerate(results):
    print(n,item['title'],item['license'],item['url'])
