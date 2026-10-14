import json,re,urllib.request
from pathlib import Path
from html import unescape
out=Path(__file__).resolve().parents[1]/'research-v2';out.mkdir(exist_ok=True)
urls={
'cia-area51':'https://www.cia.gov/stories/story/area-51-and-the-accidental-test-flight/',
'nasa-apollo':'https://www.nasa.gov/the-apollo-program/',
'nasa-apollo11':'https://www.nasa.gov/mission/apollo-11/',
'nasa-uap':'https://www.nasa.gov/news-release/update-nasa-shares-uap-independent-study-report-names-director/',
'archives-uap':'https://www.archives.gov/research/topics/uaps',
'pursue':'https://www.war.gov/Pursue/',
'reddit':'https://www.reddit.com/r/finlandConspiracy/',
'finland-facts':'https://finland.fi/facts-stats-and-info/finland-in-facts/',
'illuminati-britannica':'https://www.britannica.com/topic/illuminati-group-designation',
'finland-wiki':'https://en.wikipedia.org/wiki/Finland_does_not_exist',
'moon-hoax-nasa':'https://www.nasa.gov/history/afj/ap11fj/index.html',
}
records=[]
for key,url in urls.items():
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'NarrativeVideoResearch/1.0'}),timeout=25) as r: html=r.read().decode('utf8',errors='replace');status=r.status;final=r.url
        html=re.sub(r'<(script|style)\b[^>]*>.*?</\1>','',html,flags=re.S|re.I)
        txt=unescape(re.sub('<[^>]+>',' ',html));txt=re.sub(r'\s+',' ',txt)
        (out/(key+'.txt')).write_text(txt)
        records.append(dict(key=key,url=url,final=final,status=status));print(key,status,txt[:70],flush=True)
    except Exception as e: records.append(dict(key=key,url=url,error=str(e)));print(key,str(e),flush=True)
    (out/'sources.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
