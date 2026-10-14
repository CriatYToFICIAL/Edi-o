"""Record sources, licensing, editorial decisions, and reusable source text."""
import html,json,re,shutil
from html.parser import HTMLParser
from pathlib import Path
from collections import Counter
from scene_data_revision import CHAPTERS,TOTAL

class Text(HTMLParser):
    def __init__(self):super().__init__();self.parts=[];self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):self.skip+=1
        if tag in ('p','h2','h3','li'):self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style'):self.skip=max(0,self.skip-1)
    def handle_data(self,data):
        if not self.skip:self.parts.append(data)
sources=[('birds','https://en.wikipedia.org/wiki/Birds_Aren%27t_Real','/tmp/birds-page.html'),('reptiles','https://en.wikipedia.org/wiki/Reptilian_conspiracy_theory','/tmp/reptiles-page.html'),('earth','https://en.wikipedia.org/wiki/Spherical_Earth','/tmp/earth-page.html'),('flat','https://en.wikipedia.org/wiki/Modern_flat_Earth_beliefs','/tmp/flat-page.html')]
for key,url,file in sources:
    parser=Text();parser.feed(Path(file).read_text());text=''.join(parser.parts)
    Path('research',key+'-source.txt').write_text(text)
    snippets=[l.strip() for l in text.splitlines() if len(l.strip())>90 and any(w in l.lower() for w in ['mcindoe','2021','satire','icke','1999','1990','spherical','photograph'])]
    print(key,'\n'.join(snippets[:4])[:2500])
records=json.loads(Path('asset-ledger.json').read_text())
byfile={r['file']:r for r in records}
origin=byfile.get('public/media/revision/obama.ogv')
if origin:
    for name,treatment in [('obama.mp4','Excerpt 8–18s; crop to main subjects; muted; 30 fps'),('obama-low.mp4','Same excerpt with deliberately reduced resolution: clearly labeled demonstration'),('obama-still.jpg','Frame at 10s of the source, no added reptilian features'),('obama-detail.jpg','Crop of the original frame at 10s for a labeled enlargement')]:
        clone=dict(origin);clone.update(file='public/media/revision/'+name,derivative=treatment);records.append(clone)
for name,code in [('thinking','1F914'),('dimension','1F30C'),('apple','1F34E')]:
    records.append(dict(file='public/art/'+name+'.svg',title='OpenMoji '+name,artist='OpenMoji contributors',license='CC BY-SA 4.0',page='https://openmoji.org/',download_url=f'https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/svg/{code}.svg',reviewed=True))
old=json.loads(Path('../conspiracoes-parte1/asset-ledger.json').read_text())
copied={'area51-aerial-extra.jpg','moon-flag.jpg','eye.jpg','bird.jpg','flat-map.jpg'}
for r in old:
    if Path(r.get('file','')).name in copied and r.get('file','').startswith('public/media/'):
        records.append(r)
for r in list(records):
    if r['file'].endswith('.gif'):
        clone=dict(r);clone.update(file=r['file'].replace('.gif','.mp4'),derivative='Converted from licensed GIF, 30 fps, 1-second keyframe interval, muted, 8 seconds');records.append(clone)
used={a for c in CHAPTERS for s in c['shots'] for a in s['assets'] if not a.startswith(('#','@'))}
used.update(['movement-logo.png','revision/obama-still.jpg','flat-theory.png','thinking.svg','dimension.svg','speech.svg'])
records=list({r['file']:r for r in records}.values())
for r in records:
    name=r['file'].replace('public/media/','').replace('public/art/','')
    r['used_in_film']=name in used or Path(r['file']).name in copied
    r['reviewed']=r['used_in_film']
Path('asset-ledger.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
rows=['# Créditos — Parte 2','','Preserve estes créditos na descrição do vídeo e quando redistribuir o projeto. As licenças aplicáveis a cada ativo continuam valendo. Interfaces e desenhos explicativos são originais; não são documentos oficiais nem postagens reais.','','| Arquivo | Autor | Licença | Origem |','| --- | --- | --- | --- |']
for r in records:
    if r['used_in_film'] or '/art/' in r['file']:
        clean=lambda s:' '.join(re.sub('<[^>]+>','',html.unescape(str(s))).replace('|','/').split())
        rows.append('| '+' | '.join(clean(r.get(k,'')) for k in ['file','artist','license','page'])+' |')
rows+=['','Fonte tipográfica: Comic Neue, SIL Open Font License (arquivo incluído).','Ícones flat: OpenMoji contributors, CC BY-SA 4.0, https://openmoji.org/ — arquivos locais sem modificações gráficas.','Painéis, diagramas e personagens vetoriais: originais para este episódio.','Avatar dos Reptilianos e grade de sete casos: continuidade do projeto original.']
Path('CREDITS.md').write_text('\n'.join(rows))
counts=Counter(a for c in CHAPTERS for s in c['shots'] for a in s['assets'] if not a.startswith(('#','@')))
counts.update({'movement-logo.png':1,'revision/obama-still.jpg':1,'flat-theory.png':1})
Path('reuse-audit.json').write_text(json.dumps(dict(limit=2,counts=dict(counts),exceptions='Overview, avatares e fotografia central da Terra',violations={k:v for k,v in counts.items() if v>2}),indent=2))
