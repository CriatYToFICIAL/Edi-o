"""Original visual explanations, with word-aligned fragment cues and no fourth-wall copy."""
import html
CSS='''
.custom-panel{background:transparent!important;box-shadow:none!important;overflow:visible!important}
.panel{width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:30px;padding:25px;font-family:Comic,sans-serif;color:#10191d;font-weight:700}
.panel h2{font-size:62px;margin:0;text-align:center;line-height:1.15}.panel p{font-size:42px;margin:0;text-align:center;line-height:1.2}.panel .small{font-size:26px;color:#48525a}.panel .row{display:flex;align-items:center;justify-content:center;gap:35px;width:100%}.piece{opacity:0}.tile{background:#fffefa;border:3px solid #293b44;border-radius:14px;padding:22px 30px;font-size:42px;text-align:center;box-shadow:8px 12px 20px #0002}.arrow{font-size:70px}.red{color:#ad3039}.panel svg{max-width:100%;display:block}.panel img.icon{width:220px;height:220px;object-fit:contain}.window{width:100%;height:100%;background:#fff;border:3px solid #71818b;border-radius:16px;box-shadow:9px 13px 19px #0003;overflow:hidden}.toolbar{height:65px;background:#eaf0f3;padding:15px 24px;border-bottom:2px solid #ccd5da;display:flex;align-items:center;gap:12px;font-size:27px}.dot{width:15px;height:15px;background:#a5b0b8;border-radius:50%}.window-content{padding:34px 38px;display:flex;flex-direction:column;gap:22px}.window h2{font-size:52px}.post{border:2px solid #d5dbdf;background:#fbfcfa;border-radius:12px;padding:25px;font-size:39px;line-height:1.2}.small-note{font-size:23px!important;color:#58636b}.compact h2{font-size:44px}.compact p{font-size:31px}.compact .tile{font-size:30px;padding:18px}.compact .icon{width:180px!important;height:180px!important}.compact .window-content{padding:24px;gap:16px}.compact .post{font-size:31px}.compact .toolbar{font-size:23px}.panel .num{font-size:100px}.board{background:#fffefa;box-shadow:9px 14px 22px #0002;border:3px solid #53616a;border-radius:14px;padding:34px;width:95%}.stamp{color:#ad3039;border:6px solid #ad3039;padding:13px 25px;font-size:52px}
'''
def piece(body,delay=0,cls=''):
    return f'<div class="piece {cls}" data-panel-delay="{delay}">{body}</div>'
def title(s,delay=0):return piece('<h2>'+html.escape(s)+'</h2>',delay)
def text(s,delay=0,cls=''):return piece('<p class="'+cls+'">'+html.escape(s)+'</p>',delay)
def tile(s,d=0):return piece(html.escape(s),d,'tile')
def row(*parts):return '<div class="row">'+''.join(parts)+'</div>'
def svg(body):return '<svg width="1100" height="525" viewBox="0 0 900 430" xmlns="http://www.w3.org/2000/svg">'+body+'</svg>'
def drawing(body,d=0):return piece(svg(body),d)
def icon(name,d=0):return piece(f'<img class="icon" src="../public/art/{name}.svg" alt="{name}">',d)
def window(name,*blocks):return '<div class="window"><div class="toolbar"><i class="dot"></i><i class="dot"></i><i class="dot"></i>'+name+'</div><div class="window-content">'+''.join(blocks)+'</div></div>'
def face(fill='#b7c9d3',eyes=True):
    return f'<path d="M240 390Q240 270 450 270T660 390" fill="#365369" stroke="#273c45" stroke-width="7"/><ellipse cx="450" cy="155" rx="100" ry="115" fill="{fill}" stroke="#273c45" stroke-width="7"/>'+('<circle cx="413" cy="143" r="10"/><circle cx="487" cy="143" r="10"/><path d="M408 218H492" stroke="#273c45" stroke-width="7"/>' if eyes else '')
def bird():return '<path d="M220 275Q140 150 270 130Q360 90 414 155L520 170 417 210Q400 310 260 320Z" fill="#a7c9d0" stroke="#273c45" stroke-width="7"/><path d="M247 225Q330 270 370 210" fill="none" stroke="#273c45" stroke-width="7"/><circle cx="372" cy="169" r="11"/><path d="M210 277L150 320 260 300M295 313V352M325 313V352" stroke="#273c45" stroke-width="7"/>'
def panel(key):
    body=''
    if key=='bird-drone':
        body=drawing(bird())+piece(svg('<g><rect x="520" y="105" width="170" height="130" rx="20" fill="#728c9c" stroke="#273c45" stroke-width="7"/><circle cx="605" cy="169" r="45" fill="#29485f"/><circle cx="605" cy="169" r="22" fill="#8ac7d3"/><path d="M415 185H518" stroke="#273c45" stroke-width="7" stroke-dasharray="15 12"/></g>'),1.68)
        return '<div class="panel" style="position:relative">'+drawing(bird())+'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">'+piece(svg('<rect x="520" y="105" width="170" height="130" rx="20" fill="#728c9c" stroke="#273c45" stroke-width="7"/><circle cx="605" cy="169" r="45" fill="#29485f"/><circle cx="605" cy="169" r="22" fill="#8ac7d3"/><path d="M415 185H518" stroke="#273c45" stroke-width="7" stroke-dasharray="15 12"/>'),1.68)+'</div></div>'
    elif key=='monitor':body=title('OLHOS EM TODA PARTE?')+drawing('<circle cx="160" cy="100" r="65" fill="#a7c9d0" stroke="#273c45" stroke-width="7"/><circle cx="160" cy="100" r="25" fill="#365369"/><path d="M210 140L720 340M210 140L400 340" stroke="#ad3039" stroke-width="6" stroke-dasharray="16 13"/>'+''.join(f'<circle cx="{x}" cy="295" r="30" fill="#dfc6a6"/><path d="M{x-45} 390V360Q{x} 315 {x+45} 360V390" fill="#657f93"/>' for x in [400,560,720]))
    elif key=='robot':body=drawing(bird().replace('#a7c9d0','#c3ccd1')+'<circle cx="270" cy="230" r="38" fill="#607c8a"/><path d="M230 230H310M270 190V270" stroke="#eee" stroke-width="6"/><path d="M330 290L400 260" stroke="#ad3039" stroke-width="5"/>')
    elif key=='serious':body=drawing(face())+text('É sério?',3.6)
    elif key=='curious':body=title('AS ALEGAÇÕES MAIS CURIOSAS')
    elif key=='charge':body=row(icon('battery'),piece('<div class="num">+</div>',.10))+text('RECARREGANDO?',.15)
    elif key=='migration':body=drawing('<path d="M140 280Q390 20 730 270" fill="none" stroke="#607e91" stroke-width="8" stroke-dasharray="18 12"/><path d="M700 237L750 278 694 291" fill="#607e91"/><circle cx="140" cy="280" r="45" fill="#bdd2a0"/><circle cx="730" cy="280" r="45" fill="#dfc296"/>'+''.join(f'<path class="migrator" d="M{x} {y}q25 -35 50 0q25 -35 50 0" fill="none" stroke="#273c45" stroke-width="8"/>' for x,y in [(230,170),(410,105),(560,170)]))
    elif key.startswith('web-'):
        names={'web-birds':('AVES NÃO SÃO REAIS','Pássaros ou drones?','Uma piada que virou movimento.'),'web-reptiles':('REPTILIANOS','Vídeos editados','Boatos compartilhados'),'web-flat':('TERRA PLANA','Vídeos e fóruns','Debates na internet')};a,b,c=names[key]
        return window('Discussão online',title(a),piece('<div class="post">'+b+'</div>',.25),piece('<div class="post">'+c+'</div>',1.2),text('Reconstituição',0,'small-note'))
    elif key=='interview':body=row(icon('microphone'),title('ENTREVISTA'))+text('The New York Times',.52)+piece('<div class="num">2021</div>',1.46)
    elif key in ('rumor','misinformation'):body=row(tile('IDEIA'),piece('<div class="arrow">→</div>',.2),tile('COMPARTILHAMENTO',.55))+row(tile('NOVAS VERSÕES',1.1),tile('DESINFORMAÇÃO',1.7))
    elif key=='disguise':body=drawing(face('#8ebd89'))+text('Um disfarce humano?',.15)
    elif key=='institutions':body=title('CONTROLE NOS BASTIDORES?')+row(tile('POLÍTICA'),tile('PODER',.6),tile('INSTITUIÇÕES',1.2))
    elif key=='podium':body=drawing(face()+'<path d="M275 300H625L590 410H310Z" fill="#a57b57" stroke="#273c45" stroke-width="7"/><path d="M520 310V240H470" stroke="#273c45" stroke-width="7"/>')
    elif key=='portal':body=drawing('<ellipse cx="240" cy="210" rx="100" ry="170" fill="#e1d6eb" stroke="#61738e" stroke-width="9"/><ellipse cx="240" cy="210" rx="58" ry="117" fill="#8d8fac"/><path d="M400 210H530M500 180L535 210 500 240" stroke="#273c45" stroke-width="7" fill="none"/><circle cx="665" cy="210" r="92" fill="#517c93"/><ellipse cx="665" cy="210" rx="145" ry="45" fill="none" stroke="#b4c8a1" stroke-width="12"/>')+text('Outra dimensão • sistema estelar',1.14)
    elif key=='fear':body=row(tile('MEDO'),piece('<div class="arrow">+</div>',.2),tile('INFLUÊNCIA',.64))+text('A hipótese do controle',.3)
    elif key=='video-face':return window('Vídeo',drawing(face()),text('Um quadro fora de contexto?',2.1))
    elif key=='distortion':
        body=row(drawing(face()),drawing(face('#acc6ae')+'<path d="M350 120H550V150H350ZM360 195H545V221H360Z" fill="#c6d9df"/>',.28))+row(tile('QUADRO NORMAL'),tile('ARTEFATO VISUAL',.38))
    elif key=='compression':body=title('FALHA DE IMAGEM')+drawing(''.join(f'<rect x="{220+x*65}" y="{50+y*65}" width="61" height="61" fill="{["#a8bfcd","#7996a6","#d2dde2","#586f82"][(x+y)%4]}"/>' for x in range(7) for y in range(5)))
    elif key=='suspicion':body=row(tile('DISTORÇÃO'),piece('<div class="arrow">≠</div>',.25),tile('PROVA',.45))
    elif key in ('connections','conspiracy'):
        labels=['IMAGEM','BOATO','COINCIDÊNCIA'] if key=='connections' else ['AGÊNCIA ESPACIAL','GELO','SEGREDO']
        body=title('TUDO PARECE CONECTADO...')+row(tile(labels[0]),tile(labels[1],.7),tile(labels[2],1.3))+drawing('<path d="M130 100L450 260 770 100M130 100H770" stroke="#ad3039" stroke-width="7" fill="none"/>',1.8)
    elif key=='fiction':body=drawing('<path d="M150 65H420Q450 60 450 90Q450 60 480 65H750V360H480Q450 360 450 385Q450 360 420 360H150Z" fill="#fffefa" stroke="#273c45" stroke-width="7"/><path d="M450 90V380" stroke="#273c45" stroke-width="6"/><circle cx="300" cy="200" r="72" fill="#8394b4"/><ellipse cx="300" cy="200" rx="105" ry="30" fill="none" stroke="#cfb986" stroke-width="10"/><path d="M515 130H700M515 185H700M515 240H700M515 295H650" stroke="#a9b6bc" stroke-width="9"/>')+title('FICÇÃO CIENTÍFICA',.25)
    elif key=='myth':body=drawing('<rect x="220" y="30" width="460" height="360" rx="18" fill="#e8dac2" stroke="#786d5c" stroke-width="6"/><path d="M365 335C630 330 210 200 460 200S350 40 550 100" fill="none" stroke="#9a7457" stroke-width="23"/><path d="M530 85L570 90 550 115Z" fill="#9a7457"/>')+text('Mitologia',.1)
    elif key=='disk':body=drawing('<ellipse cx="450" cy="270" rx="310" ry="115" fill="#6aa3b5" stroke="#273c45" stroke-width="7"/><path d="M230 250Q280 180 380 265L465 225 530 285 610 225" fill="#abc693"/><path d="M165 290Q450 440 735 290L735 340Q450 485 165 340Z" fill="#d8e9ef" stroke="#557788" stroke-width="6"/>')+text('Um disco cercado de gelo?',1.34)
    elif key=='secrecy':body=row(tile('GOVERNOS'),tile('AGÊNCIAS',.58))+drawing('<rect x="340" y="60" width="220" height="260" rx="12" fill="#fffefa" stroke="#273c45" stroke-width="7"/>'+''.join(f'<path d="M375 {y}H525" stroke="#273c45" stroke-width="17"/>' for y in [125,180,235]),1.6)
    elif key=='photo-claim':body=title('FOTOGRAFIA FABRICADA?')+piece('<div class="stamp">A ALEGAÇÃO</div>',.3)
    elif key=='horizon':body=drawing('<path d="M65 200H835" stroke="#4f89a1" stroke-width="7"/><path d="M65 230Q450 215 835 230" stroke="#4f89a1" stroke-width="5" stroke-dasharray="15 12"/><circle cx="450" cy="146" r="22" fill="#c0a387"/><path d="M450 170V202" stroke="#273c45" stroke-width="8"/>')+text('Aparência local ≠ formato global',.2)
    elif key=='gravity':body=drawing('<circle cx="450" cy="245" r="135" fill="#8eafbc" stroke="#273c45" stroke-width="6"/>'+''.join(f'<path d="M{x} {y}L450 245" stroke="#ad3039" stroke-width="5" stroke-dasharray="12 10"/>' for x,y in [(200,60),(700,60),(140,300),(760,300)]))+text('E a gravidade?',.2)
    elif key=='experiment':return window('Experimento caseiro',drawing('<path d="M100 340H800M235 130V340M665 130V340" stroke="#273c45" stroke-width="7"/><path d="M240 195H660" stroke="#ad3039" stroke-width="6"/><circle cx="235" cy="195" r="25" fill="#c2d597"/><rect x="600" y="170" width="65" height="65" fill="#d9c198"/>'),text('Observação • interpretação',.9))
    elif key=='share-flat':return window('Discussão',piece('<div class="post">Experimentos pessoais</div>'),piece('<div class="post">Observações compartilhadas</div>',.6),text('Reconstituição',0,'small-note'))
    elif key=='agency':body=row(icon('satellite'),title('NASA'))
    elif key=='antarctica':body=drawing('<circle cx="450" cy="210" r="185" fill="#77a8bc" stroke="#273c45" stroke-width="7"/><path d="M320 220L350 170 390 190 420 135 465 180 510 170 565 225 545 260 480 255 440 290 385 260 335 280Z" fill="#f2f7f8" stroke="#527585" stroke-width="5"/>')+title('ANTÁRTIDA',.2)
    elif key=='observation':body=row(tile('OBSERVAÇÃO'),tile('SATÉLITES',.86),tile('FÍSICA',2.38))+drawing('<circle cx="450" cy="185" r="120" fill="#7dabbc" stroke="#273c45" stroke-width="6"/><ellipse cx="450" cy="185" rx="240" ry="85" fill="none" stroke="#78905b" stroke-width="6"/><rect x="625" y="90" width="50" height="50" fill="#d8bc7e"/>',.2)
    elif key=='comment':body=row(icon('speech'),title('QUAL É A SUA CURIOSIDADE?'))+text('Conta nos comentários',1.2)+text('Pode virar o próximo vídeo',7.38)
    else:raise ValueError(key)
    return '<div class="panel">'+body+'</div>'
