"""Generate deterministic, editable HyperFrames chapter compositions."""
import html
import json
import re
import shutil
from pathlib import Path
from PIL import Image
from scene_data_v2 import CHAPTERS, REVEALS, TOTAL
from v2_panels import panel, CSS as PANEL_CSS

FILM = Path('film')
PUBLIC = FILM/'public'
COMP = FILM/'compositions'
COMP.mkdir(exist_ok=True)
shutil.copyfile('narracao.wav',PUBLIC/'narracao.wav')
E = html.escape
FONT = '''@font-face{font-family:Comic;src:url("../public/comic-bold.woff2");font-weight:700}@font-face{font-family:Comic;src:url("../public/comic-regular.woff2");font-weight:400}'''
CSS = '''
*{box-sizing:border-box} .clip{position:absolute;inset:0} .case-title{position:absolute;top:40px;left:240px;width:1440px;text-align:center;font-size:72px;font-weight:700;margin:0;color:#070707;line-height:1.2}
.case-avatar{position:absolute;left:64px;top:38px;width:142px;height:142px;border:5px solid #101010;border-radius:50%;overflow:hidden;background:#f6f6f4}
.case-avatar img{width:100%;height:100%;object-fit:cover} .stage{position:absolute;left:90px;top:205px;width:1740px;height:825px;display:flex;align-items:center;justify-content:center;gap:85px}
.card{display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative;flex:none;opacity:0}
.visual{background:#fff;box-shadow:9px 13px 19px #00000030;overflow:hidden;position:relative;flex:none}
.visual img,.visual video{width:100%;height:100%;object-fit:contain;display:block}.art{background:transparent;box-shadow:none;overflow:visible}.art img{filter:drop-shadow(8px 12px 9px #00000022)}
.caption{font-size:44px;line-height:1.15;font-weight:700;color:#050505;text-align:center;max-width:100%;margin:16px 0 0;white-space:normal;-webkit-text-stroke:5px white;paint-order:stroke fill}
.source{font-size:23px;color:#444;line-height:1.15;margin-top:12px;text-align:center;max-width:100%;font-weight:400;background:#f8f8f6;padding:3px 8px}
.big{font-size:77px;font-weight:700;line-height:1.2;text-align:center;color:#080808;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:25px}
.big div{max-width:100%;padding:0 12px} .board-label{color:#b02b3a;font-size:62px;font-weight:700;line-height:1.25;text-align:center}
.overview{overflow:hidden}.world-camera{position:absolute;inset:0;transform-origin:0 0}
.overview-card{position:absolute;width:400px;display:flex;flex-direction:column;align-items:center}
.overview-picture{width:400px;height:320px;overflow:hidden;border-radius:28px;background:#f9f9f7;box-shadow:8px 14px 22px #00000038}
.overview-picture img{width:100%;height:100%;object-fit:cover}.overview-name{font-size:49px;line-height:1.16;font-weight:700;text-align:center;white-space:nowrap;margin-top:21px;color:#050505;-webkit-text-stroke:8px #fff;paint-order:stroke fill}
'''
CASE_MEDIA=['area51-aerial-extra.jpg','moon-flag.jpg','eye.jpg','finland.svg','bird.jpg','reptile.svg','flat-map.jpg']
CASE_NAMES=['ÁREA 51','CHEGADA À LUA','ILLUMINATI','FINLÂNDIA','AVES NÃO SÃO REAIS','REPTILIANOS','TERRA PLANA']
POS=[(55,85),(525,85),(995,85),(1465,85),(290,600),(760,600),(1230,600)]
SOURCES={'area51-aerial-extra.jpg':'Doc Searls • CC BY 2.0',
 'telescope.jpg':'Jodrell Bank • Mike Peel • CC BY-SA 4.0',
 'helsinki.jpg':'Helsinki • Suomen Ilmakuva OY • CC BY 4.0',
 'train.jpg':'Transiberiana • CC BY-SA 3.0',
 'moonflag.mp4':'Montagem de fotos NASA • Anynobody',
 'lro.mp4':'NASA / LRO • imagem orbital com destaques',
 'uap.mp4':'US Navy • FLIR1 • registro de 2004',
 'weishaupt.jpg':'Retrato histórico • domínio público',
 'aldrin.jpg':'NASA • Apollo 11 • 1969',
 'moon-flag.jpg':'NASA / NARA • Apollo 11 • 1969',
 'rocks.jpg':'NASA • amostras Apollo 11',
 'mission-control.jpg':'NASA • controle da missão Apollo 11',
 'u2.jpg':'NASA • Lockheed U-2', 'sr71.jpg':'US Air Force • SR-71'}

# Full source/author/license credits ship in CREDITS.md and asset-ledger.json.
# Editorial captions are optional; no automatic stack of captions and credits.
SOURCES={}

def url(asset):
    return '../public/'+('art/' if asset.endswith('.svg') and asset!='finland.svg' else 'media/')+asset

def dimensions(asset, pair):
    maxw,maxh = (780,610) if pair else (1230,650)
    if asset.startswith('#'):
        return (780,610) if pair else (1260,650)
    if asset.startswith('@'):
        return (760,550) if pair else (1150,590)
    if asset.endswith('.svg') and asset!='finland.svg':
        if asset!='reptile.svg':return (460,430) if pair else (620,590)
        return (780,585) if pair else (1000,650)
    if asset.endswith('.mp4'):
        with Image.open(PUBLIC/'media'/asset.replace('.mp4','.gif')) as im:
            ratio=im.width/im.height
        if asset=='earth-spin.mp4':maxw,maxh=700,650
    elif asset.endswith('.svg'):
        ratio=18/11
    else:
        with Image.open(PUBLIC/'media'/asset) as im:
            ratio=im.width/im.height
    h=min(maxh,maxw/ratio)
    return round(h*ratio),round(h)

transcript=json.loads(Path('transcript-edited.json').read_text())
words=[w for s in transcript['segments'] for w in s['words']]
plan=[]
all_assertions=[]
for chapter in CHAPTERS:
    cid=chapter['id']; offset=chapter['start']; duration=chapter['end']-offset
    # Scope all ids, and keep the styles/scripts inside the transport template.
    body=[]; js=[]; assertions=[]
    first=chapter['shots'][0]['start']-offset
    overview_id=f'{cid}-overview'
    body.append(f'<section id="{overview_id}" class="clip overview" data-start="0" data-duration="{first:.3f}" data-track-index="0"><div id="{cid}-camera" class="world-camera" data-layout-allow-overflow>')
    for i,((x,y),name,asset) in enumerate(zip(POS,CASE_NAMES,CASE_MEDIA)):
        body.append(f'<div class="overview-card" style="left:{x}px;top:{y}px"><div class="overview-picture"><img src="{url(asset)}" alt="{E(name)}"></div><div class="overview-name">{E(name)}</div></div>')
    body.append('</div></section>')
    zoomstart,zoomend=[t-offset for t in chapter['zoom']]
    x,y=POS[chapter['target']]; cx=x+200; cy=y+160; scale=4.7
    js.append(f'tl.fromTo("#{cid}-camera",{{x:0,y:0,scale:1}},{{x:{960-cx*scale},y:{540-cy*scale},scale:{scale},duration:{zoomend-zoomstart:.3f},ease:"power2.inOut"}},{zoomstart:.3f});')
    body.append(f'<section id="{cid}-header" class="clip" data-start="{first:.3f}" data-duration="{duration-first:.3f}" data-track-index="1"><div id="{cid}-heading-wrap"><div class="case-avatar"><img src="{url(CASE_MEDIA[chapter["target"]])}" alt="Ícone do caso"></div><h1 class="case-title">{E(chapter["title"])}</h1></div></section>')
    js.append(f'tl.fromTo("#{cid}-heading-wrap",{{opacity:0}},{{opacity:1,duration:0.18}},{first:.3f});')
    for i,scene in enumerate(chapter['shots']):
        start=scene['start']-offset
        end=(chapter['shots'][i+1]['start'] if i+1<len(chapter['shots']) else chapter['end'])-offset
        length=end-start
        scene['end']=end+offset; scene['chapter']=chapter['title']
        scene['voice_text']=''.join(w['word'] for w in words if scene['start']<=w['start']<scene['end']).strip()
        plan.append(scene.copy())
        sid=f'{cid}-s{i:02d}'; isvideo=any(a.endswith('.mp4') for a in scene['assets'])
        attrs=(f'class="video-scene" style="position:absolute;inset:0;opacity:0"' if isvideo else f'class="clip" data-start="{start:.3f}" data-duration="{length:.3f}" data-track-index="2"')
        body.append(f'<section id="{sid}" {attrs}><div class="stage">')
        if isvideo:
            js.append(f'tl.set("#{sid}",{{autoAlpha:1}},{start:.3f});tl.set("#{sid}",{{autoAlpha:0}},{end:.3f});')
        for j,asset in enumerate(scene['assets']):
            if not asset.startswith(('@','#')) and not (PUBLIC/('art' if asset.endswith('.svg') and asset!='finland.svg' else 'media')/asset).exists():
                raise FileNotFoundError(asset)
            width,height=dimensions(asset,len(scene['assets'])>1)
            elem=f'{sid}-card{j}'; v=f'{elem}-visual'; cap=scene['captions'][j] if j<len(scene['captions']) else ''
            body.append(f'<div id="{elem}" class="card" style="width:{width}px">')
            if asset.startswith('#'):
                content=panel(asset[1:])
                body.append(f'<div id="{v}" class="visual custom-panel {"compact" if len(scene["assets"])>1 else ""}" style="width:{width}px;height:{height}px">'+content+'</div>')
            elif asset.startswith('@'):
                labels=asset[1:].split(' / ')
                body.append(f'<div id="{v}" class="big" style="width:{width}px;height:{height}px">'+''.join(f'<div>{E(t)}</div>' for t in labels)+'</div>')
            else:
                art=' art' if asset.endswith('.svg') and asset!='finland.svg' else ''
                body.append(f'<div id="{v}" class="visual{art}" style="width:{width}px;height:{height}px">')
                if asset.endswith('.mp4'):
                    body.append(f'<video id="{elem}-media" class="clip" src="{url(asset)}" muted playsinline data-start="{start:.3f}" data-duration="{length:.3f}" data-media-start="0" data-track-index="{10+i}"></video>')
                else:
                    body.append(f'<img src="{url(asset)}" alt="{E(cap)}">')
                body.append('</div>')
            if cap:
                body.append(f'<p class="caption">{E(cap)}</p>')
            if asset in SOURCES:
                body.append(f'<p class="source">{E(SOURCES[asset])}</p>')
            body.append('</div>')
            reveal=REVEALS.get((cid,scene['start']),[scene['start']]*len(scene['assets']))[j]-offset
            motion=scene.get('motion','rise')
            dx=(-90 if j==0 else 90) if motion in ('left','right') else 0
            dy=48 if motion=='rise' else 0
            scale=.88 if motion=='pop' else .97
            js.append(f'tl.fromTo("#{elem}",{{opacity:0,x:{dx},y:{dy},scale:{scale}}},{{opacity:1,x:0,y:0,scale:1,duration:0.22,ease:"power2.out",immediateRender:false}},{reveal:.3f});')
            js.append(f'tl.to("#{elem}",{{opacity:0,y:-14,duration:0.10,ease:"power1.in"}},{end-.10:.3f});')
            assertions.append(dict(kind='appearsBy',selector=f'#{elem}',bySec=round(reveal+.27,3)))
            if asset.startswith('#'):
                js.append(f'document.querySelectorAll("#{v} .piece").forEach((el,k)=>{{const d=Number(el.dataset.panelDelay||0);if({reveal:.3f}+d<{end-.25:.3f}){{tl.fromTo(el,{{opacity:0,y:20}},{{opacity:1,y:0,duration:.20,ease:"power2.out",immediateRender:false}},{reveal:.3f}+d);}}}});')
            if asset=='#migration':
                js.append(f'tl.to("#{v} .migrator",{{x:50,y:-12,duration:{max(.1,end-reveal-.5):.3f},ease:"sine.inOut"}},{reveal+.22:.3f});')
        body.append('</div></section>')
    css=FONT+f'#{cid}-root{{position:absolute;inset:0;width:100%;height:100%;font-family:Comic,sans-serif;color:#070707}}'+CSS+PANEL_CSS+' .piece{opacity:0}.compact .panel{padding:18px;gap:16px}.compact h2{font-size:43px}.compact p{font-size:30px}.compact .tile{font-size:30px}.custom-panel svg{max-width:100%;max-height:340px}.custom-panel .content{min-height:0}.custom-panel .panel{overflow:hidden}'
    css += ' .custom-panel svg{max-height:490px}.panel .row>.piece{min-width:0}.panel .row>.piece:has(svg){flex:1}.panel .row svg{width:100%;height:auto;max-height:380px}'
    content=f'<!doctype html><html lang="pt-BR"><body><template><style>{css}</style><div id="{cid}-root" data-composition-id="{cid}" data-width="1920" data-height="1080" data-duration="{duration:.3f}">'+''.join(body)+f'</div><script>(function(){{const tl=gsap.timeline({{paused:true}});'+''.join(js)+f'window.__timelines["{cid}"]=tl;}})();</script></template></body></html>'
    (COMP/f'{cid}.html').write_text(content)
    (COMP/f'{cid}.motion.json').write_text(json.dumps(dict(duration=duration,assertions=assertions),indent=2))
    all_assertions.extend(dict(a,bySec=round(a['bySec']+offset,3)) for a in assertions)

total=TOTAL
hostfont=FONT.replace('../public/','public/')
mounts=''.join(f'<div id="slot-{c["id"]}" class="clip" data-composition-id="{c["id"]}" data-composition-src="compositions/{c["id"]}.html" data-start="{c["start"]}" data-duration="{c["end"]-c["start"]:.3f}" data-width="1920" data-height="1080" data-track-index="1"></div>' for c in CHAPTERS)
main=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=1920,height=1080"><title>Teorias da conspiração • Parte 2</title><script src="public/gsap.min.js"></script><style>{hostfont}*{{box-sizing:border-box}}html,body{{margin:0;width:1920px;height:1080px;overflow:hidden}}#root{{width:100%;height:100%;position:relative;overflow:hidden}}.clip{{position:absolute;inset:0}}.paper{{position:absolute;inset:0;background-color:#f8f8f6;background-image:linear-gradient(#d2d2cf 1.5px,transparent 1.5px),linear-gradient(90deg,#d2d2cf 1.5px,transparent 1.5px);background-size:64px 64px}}</style></head><body><div id="root" data-composition-id="main" data-width="1920" data-height="1080" data-duration="{total}" data-fps="30"><div class="paper" data-layout-ignore></div>{mounts}<audio id="narration" src="public/narracao.wav" data-start="0" data-duration="{total}" data-track-index="20" data-volume="1"></audio></div><script>const tl=gsap.timeline({{paused:true}});window.__timelines["main"]=tl;</script></body></html>'''
(FILM/'index.html').write_text(main)
Path('timing-contract.json').write_text(json.dumps(dict(duration=total,assertions=all_assertions),indent=2))
# The CLI samples at most 300 points across the full film. Keep its deadlines
# on that sampling grid; validate the original exact deadlines independently.
import math
step=total/299
sampled=[dict(a,bySec=round(math.ceil(a['bySec']/step)*step+.002,3)) for a in all_assertions]
# A scene shorter than the sampling interval can fall wholly between samples.
# Such cards remain covered by verify_timing.mjs at the exact original deadline.
ends={f'#{c["id"]}-s{i:02d}':(c['shots'][i+1]['start'] if i+1<len(c['shots']) else c['end']) for c in CHAPTERS for i in range(len(c['shots']))}
sampled=[a for a in sampled if a['bySec']<ends[a['selector'].split('-card')[0]]]
(FILM/'index.motion.json').write_text(json.dumps(dict(duration=total,assertions=sampled),indent=2))
Path('material-plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
rows=['# Plano de material sincronizado','', '| Início–fim | Caso | Fala | Material | Texto complementar | Critério de escolha |','| --- | --- | --- | --- | --- | --- |']
for p in plan:
    rows.append(f'| {p["start"]:.2f}–{p["end"]:.2f} | {p["chapter"]} | {p["voice_text"]} | '+', '.join(p['assets'])+' | '+' / '.join(p['captions'])+' | '+p['rationale']+' |')
Path('material-plan.md').write_text('\n'.join(rows))
Path('STORYBOARD.md').write_text('# Plano de capítulos\n\n'+ '\n'.join(f'## {c["title"]}\n\n{c["start"]:.2f}–{c["end"]:.2f} s; {len(c["shots"])} batidas; composição `film/compositions/{c["id"]}.html`.\n' for c in CHAPTERS))
print(f'{len(plan)} batidas em {len(CHAPTERS)} capítulos; duração {total:.2f} s')
