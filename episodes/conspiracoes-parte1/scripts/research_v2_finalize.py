import json,shutil
from pathlib import Path
base=Path(__file__).resolve().parents[1];r=base/'research-v2';dest=base/'film/public/media/v2'
shutil.copyfile(r/'illuminati-page7.jpg',dest/'illuminati-history.jpg')
items=json.loads((r/'assets.json').read_text())
for a in items:
    a['reviewed_visual']=True
    if a['filename'].endswith('illuminati-history.jpg'):
        a['url']=a['url'].replace('page1-','page7-');a['description']='Title page, New England and the Bavarian Illuminati, Vernon Stauffer, 1918. Historical scholarship, not a document issued by the original order.'
    if a['filename'].endswith('baltic-map.png'):a['editorial_note']='Czech-language geographical map. Translate labels in an original diagram if large readable labels are needed.'
    if a['filename'].endswith('minerval.png'):a['editorial_note']='Actual title page of Das verbesserte System der Illuminaten with owl/book insignia; not just isolated icon.'
    if a['filename'].endswith('helsinki-fishing-market.png'):a['editorial_note']='Real Helsinki herring market, not proof of conspiratorial secret fisheries; best used near reality conclusion or caption illustrative.'
    if a['filename'].endswith('reddit-logo.svg'):a['editorial_note']='Commons public-domain simple logo; trademark identification only, no endorsement implied.'
for src,out,start,end in [('apollo-launch.gif','apollo-launch.mp4',0,6.5),('aldrin-steps.ogv','aldrin-steps.mp4',0,16)]:
    row=next(x for x in items if x['filename'].endswith('/'+src)).copy();row.update(filename='public/media/v2/'+out,derived_from=src,source_interval_seconds=[start,end],transformation='Mute H.264 proxy, 960px wide, 30fps',reviewed_visual=True);items.append(row)
(r/'assets.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
