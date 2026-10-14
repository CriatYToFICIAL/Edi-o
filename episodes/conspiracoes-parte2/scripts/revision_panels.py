"""Bounded visual panels. All drawings are licensed icons or recognizable UI primitives."""
import html
CSS='''
.custom-panel{background:transparent!important;box-shadow:none!important;overflow:visible!important}
.panel{width:100%;height:100%;padding:24px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px;color:#10191d;font-family:Comic,sans-serif;font-weight:700;overflow:visible!important}
.panel>.piece{flex:0 0 auto;max-width:100%}.panel .row{width:100%;display:flex;align-items:center;justify-content:center;gap:30px}.panel .row>.piece{min-width:0;max-width:100%;flex:0 1 auto}.panel h2{font-size:56px;line-height:1.15;text-align:center;margin:0;max-width:100%;overflow-wrap:break-word}.panel p{font-size:38px;line-height:1.2;text-align:center;margin:0}.piece{opacity:0}.panel .small{font-size:24px;color:#495560}.panel .icon{width:360px;height:360px;object-fit:contain;display:block}.panel .photo{width:100%;height:330px;object-fit:contain;display:block}.compact .panel h2{font-size:46px}.compact .panel p{font-size:30px}.compact .icon{width:280px;height:280px}.compact .photo{height:280px}.window{width:100%;height:100%;background:#fff;border:3px solid #687a87;border-radius:16px;box-shadow:9px 13px 19px #0003;overflow:visible}.toolbar{height:62px;display:flex;align-items:center;gap:12px;padding:0 24px;background:#eaf0f3;border-bottom:2px solid #ccd5da;border-radius:13px 13px 0 0;font-size:27px;line-height:1.1}.dot{width:15px;height:15px;background:#a5b0b8;border-radius:50%;flex:none}.window-content{height:calc(100% - 62px);padding:25px 32px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px}.window-content .piece{flex:0 0 auto;max-width:100%}.window-content h2{font-size:50px;line-height:1.15;text-align:center;margin:0}.window-content p{font-size:34px;line-height:1.2;text-align:center;margin:0}.window-content .small{font-size:23px}.post{border:2px solid #d5dbdf;background:#fbfcfa;border-radius:12px;padding:19px;font-size:36px;line-height:1.2;width:100%}.stamp{border:5px solid #ad3039;color:#ad3039;padding:12px 25px;font-size:45px;text-align:center}.doc{width:460px;height:380px;background:#fffefa;border:3px solid #6e808c;box-shadow:9px 13px 19px #0002;border-radius:8px;padding:30px;display:flex;flex-direction:column;justify-content:center;gap:25px}.doc .blackline{height:23px;background:#253b47;border-radius:3px}.timeline{width:90%;height:70px;background:#e4eef1;border:2px solid #80939e;display:flex;gap:10px;padding:10px}.timeline i{height:45px;display:block;flex:1;background:#769ba8}.red{color:#ad3039}
'''
def piece(body,d=0,cls=''):return f'<div class="piece {cls}" data-panel-delay="{d}">{body}</div>'
def title(s,d=0):return piece('<h2>'+html.escape(s)+'</h2>',d)
def text(s,d=0,cls=''):return piece('<p class="'+cls+'">'+html.escape(s)+'</p>',d)
def photo(name,d=0,h=330):return piece(f'<img class="photo" style="height:{h}px" src="../public/media/{name}" alt="Material ilustrativo">',d)
def icon(name,d=0):return piece(f'<img class="icon" src="../public/art/{name}.svg" alt="Ícone {name}">',d)
def row(*parts):return '<div class="row">'+''.join(parts)+'</div>'
def window(name,*blocks):return '<div class="window"><div class="toolbar"><i class="dot"></i><i class="dot"></i><i class="dot"></i>'+html.escape(name)+'</div><div class="window-content">'+''.join(blocks)+'</div></div>'
def panel(key):
 if key=='deadpan':body=icon('thinking')
 elif key=='dimension':body=icon('dimension')+title('OUTRA DIMENSÃO',.1)
 elif key=='social-birds':return window('Discussão online',photo('movement-logo.png',0,330),text('Uma sátira que se espalhou',1.1),text('Reconstituição',0,'small'))
 elif key=='case2013':return window('Caso documentado • 2013',title('UM VÍDEO DE SEGURANÇA\nVIRA BOATO REPTILIANO'),text('O caso do agente de Obama',.3),text('Fonte: Wikipedia • caso citado no Wired',0,'small'))
 elif key=='editing':return window('Recortes e edição',photo('revision/obama-still.jpg',0,320),piece('<div class="timeline"><i></i><i></i><i></i><i></i><i></i></div>',.2),text('Reconstituição de interface',0,'small'))
 elif key=='secrecy':body=title('A ALEGAÇÃO DO SEGREDO GLOBAL')+piece('<div class="doc"><div class="blackline"></div><div class="blackline"></div><div class="blackline"></div><div class="blackline"></div></div>',.4)
 elif key=='photo-claim':body=title('A ALEGAÇÃO:')+text('FOTOS FABRICADAS',.12,'red')
 elif key=='web-flat':return window('Vídeos e fóruns',title('TERRA PLANA'),piece('<div class="post">Experimentos e observações</div>',.5),piece('<div class="post">Debates compartilhados online</div>',1.2),text('Reconstituição',0,'small'))
 elif key=='accumulation':body=photo('flat-theory.png',0,360)+piece('<div class="stamp">MAIS ALEGAÇÕES</div>',1.4)
 elif key=='comment':body=row(icon('speech'),title('QUAL É A SUA CURIOSIDADE?'))+text('Conta nos comentários',1.2)+text('Pode virar o próximo vídeo',7.38)
 else:raise ValueError(key)
 return '<div class="panel">'+body+'</div>'
