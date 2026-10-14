"""Original explanatory panels. Source images remain independent media assets."""
import html

CSS='''
.panel{width:100%;height:100%;position:relative;font-family:Comic,sans-serif;font-weight:700;color:#141718;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:30px;gap:26px;box-sizing:border-box}
.panel h2,.panel p{margin:0}.panel h2{font-size:64px;text-align:center;line-height:1.15}.panel p{font-size:42px;line-height:1.25;text-align:center}.panel .small{font-size:27px;color:#45494d}.panel .red{color:#a42729}.panel .blue{color:#245e7c}
.panel .row{display:flex;align-items:center;justify-content:center;gap:42px;width:100%}.panel .piece{opacity:0}.panel .tile{background:#fffefa;border:3px solid #313a3c;border-radius:13px;padding:24px 30px;text-align:center;font-size:43px;box-shadow:7px 10px 0 #24303916}.panel .arrow{font-size:76px;color:#465a62}.panel .num{font-size:110px;line-height:1.1}.panel svg{display:block;overflow:visible}.panel .label{font-size:42px}
.panel.browser{padding:0;display:block;background:#fff;border:3px solid #5c646a;border-radius:15px;overflow:hidden;box-shadow:10px 15px 22px #0002}.browser .toolbar{height:70px;display:flex;align-items:center;background:#edf0f2;border-bottom:2px solid #ccd1d4;gap:14px;padding:0 24px;font-size:26px}.browser .dot{width:16px;height:16px;border-radius:50%;background:#a7afb3}.browser .address{margin-left:20px;border-radius:9px;padding:8px 22px;background:#fff;font-size:25px;flex:1;color:#4d5458}.browser .content{padding:22px 36px;display:flex;flex-direction:column;gap:18px}.browser .post{padding:25px;border:2px solid #d6dbde;background:#fafbf9;border-radius:13px;font-size:32px;line-height:1.25}.browser .byline{font-size:27px;color:#4b5357;display:flex;align-items:center;gap:16px}.browser .brand{display:flex;align-items:center;gap:18px;font-size:51px}.browser .brand img{width:150px;height:66px;object-fit:contain}.browser .badge{font-size:23px;padding:7px 14px;background:#edf0f2;border-radius:8px;margin-left:auto}.browser .post-title{font-size:48px;color:#252b30}.browser .reconstruction{font-size:25px;color:#52585c;text-align:left}.panel .page{background:#fffef9;border:2px solid #b6aaa0;box-shadow:8px 12px 18px #0002;padding:32px;min-width:330px;text-align:center}.panel .line{height:14px;background:#b9c0c4;margin:20px 0;border-radius:6px}.panel .seal{border:6px solid #a42729;color:#a42729;padding:12px 23px;font-size:54px;transform:rotate(-8deg)}
'''

def piece(body,delay=0,cls=''):
    return f'<div class="piece {cls}" data-panel-delay="{delay}">{body}</div>'
def tile(text,delay=0):return piece(html.escape(text),delay,'tile')
def row(*parts):return '<div class="row">'+''.join(parts)+'</div>'
def svg(body,w=740,h=380):return f'<svg width="{w}" height="{h}" viewBox="0 0 740 380" xmlns="http://www.w3.org/2000/svg">{body}</svg>'
def title(s,delay=0):return piece('<h2>'+html.escape(s)+'</h2>',delay)
def text(s,delay=0,cls=''):return piece('<p class="'+cls+'">'+html.escape(s)+'</p>',delay)
def browser(content,address='Discussão ilustrativa'):
    return '<div class="panel browser"><div class="toolbar"><i class="dot"></i><i class="dot"></i><i class="dot"></i><span class="address">'+address+'</span></div><div class="content">'+content+'</div></div>'

def panel(key):
    if key=='reddit':
        return browser(
            '<div class="brand"><img src="../public/media/v2/reddit-logo.svg" alt="Reddit"><span class="badge">Reconstituição editorial</span></div>'+
            piece('<div class="byline">u/Rarragans (nome citado no áudio) <span class="small">• autoria original não confirmada</span></div>',3.75)+
            piece('<div class="post-title">A Finlândia não existe?</div>',2.8)+
            piece('<div class="post">A família teria ensinado que a Finlândia era falsa.</div>',6.5)+
            '<p class="reconstruction">Paráfrase em português • não é captura nem citação literal.</p>', 'Reddit • história citada na narração')
    if key.startswith('web-'):
        labels={'web-area':('ÁREA 51','Relatos de avistamentos','Segredo militar ou extraterrestres?'),
                'web-moon':('CHEGADA À LUA','As imagens em discussão','Novas alegações, antigas dúvidas'),
                'web-eye':('ILLUMINATI','Símbolos e coincidências','A teoria se espalha')}
        a,b,c=labels[key]
        return browser(title(a)+piece('<div class="post">'+b+'</div>',.20)+piece('<div class="post">'+c+'</div>',.65)+'<p class="reconstruction">Interface ilustrativa</p>')
    if key=='door':
        content=piece(svg('<path d="M235 340V35h270v305" fill="#b9c5c6" stroke="#28373b" stroke-width="8"/><path d="M260 340V60h220v280" fill="#e7e0c9" stroke="#28373b" stroke-width="6"/><circle cx="445" cy="210" r="13" fill="#28373b"/><path d="M310 115q0-70 65-60t0 100v30" fill="none" stroke="#a42729" stroke-width="15" stroke-linecap="round"/><circle cx="374" cy="220" r="9" fill="#a42729"/>'))+text('O que escondiam ali?',.35)
    elif key in ('radar','trajectory'):
        grid=''.join(f'<path d="M{x} 20V350 M30 {x/2}H710" stroke="#ccd4d4"/>' for x in range(50,701,80))
        content=title('RELATOS DE TESTEMUNHAS' if key=='radar' else 'MOVIMENTOS INCOMUNS')+piece(svg(grid+'<path d="M70 290Q210 270 275 160T650 65" fill="none" stroke="#527e8d" stroke-width="7" stroke-dasharray="12 12"/><g class="traveler"><ellipse cx="120" cy="230" rx="48" ry="15" fill="#b7d9df" stroke="#28373b" stroke-width="5"/><path d="M90 225Q120 175 150 225" fill="#d1e8ee" stroke="#28373b" stroke-width="5"/></g>'),.15)+text('Trajetória ilustrativa • não é registro de radar',.3,'small')
    elif key=='technology':
        content=title('TECNOLOGIA EXTRATERRESTRE?')+row(tile('MILITARES',0),piece('→',.35,'arrow'),tile('ESTUDO',.65),piece('→',.9,'arrow'),tile('ORIGEM?',1.15))+text('Era a crença que ganhava força',1.45)
    elif key=='decades':
        content=title('O MISTÉRIO GANHA ESPAÇO')+row(piece('<div class="num">1980</div>',.7),piece('→',1.1,'arrow'),piece('<div class="num">1990</div>',2.04))
    elif key=='pursue':
        content=text('INICIATIVA CITADA NA NARRAÇÃO',0,'small')+title('MAIO DE 2026',.5)+row(tile('PURSUE',3.24),piece('→',4.0,'arrow'),piece('<div class="num">160+</div><p>arquivos</p>',5.44))+text('Fonte específica ainda não confirmada',5.7,'small')
    elif key=='film-window':
        return browser(title('FILMADO NA TERRA?')+row(piece('<img src="../public/art/v2/film-set.svg" style="width:470px;height:330px" alt="Ilustração de um estúdio">'),piece('<div class="seal">ALEGAÇÃO</div>',.7)),'Cena ilustrativa • hipótese de encenação')
    elif key=='seventies':
        content=title('A DESCONFIANÇA CRESCE')+piece('<div class="num">ANOS 1970</div>',2.44)+text('As fotos passam a ser questionadas',3.8)
    elif key=='stars':
        content=title('CADÊ AS ESTRELAS?')+row(tile('ASTRONAUTA\nILUMINADO'),piece('→',.15,'arrow'),tile('EXPOSIÇÃO\nCURTA',.3))+text('Estrelas fracas não aparecem na fotografia',.5)
    elif key=='shadows':
        content=title('SOMBRAS E PERSPECTIVA')+piece(svg('<circle cx="80" cy="70" r="34" fill="#e8c56f" stroke="#2f3638" stroke-width="5"/><path d="M130 90L655 290M130 90L480 320" stroke="#dbb85f" stroke-width="5"/><path d="M80 300L660 300" stroke="#7d9292" stroke-width="5"/><path d="M280 190V300M450 210V300" stroke="#334247" stroke-width="14"/><path d="M280 300L440 335M450 300L650 340" stroke="#56616b" stroke-width="13"/>'))
    elif key=='computer':
        content=title('TECNOLOGIA DE 1969')+row(piece('<div class="page"><p>NAVEGAÇÃO</p><div class="line"></div><div class="line"></div><div class="line"></div><p>APOLLO</p></div>'),piece('<div class="num">?</div>',.8))+text('Era suficiente para ir e voltar?',1.3)
    elif key=='coverup':
        content=title('UM ACOBERTAMENTO?')+row(tile('NASA'),piece('↔',.25,'arrow'),tile('AUTORIDADES',.45))+piece('<div class="page"><p>DÉCADAS DE SEGREDO?</p><div class="line"></div><div class="line"></div></div>',1.4)
    elif key=='tracking':
        content=title('RASTREAMENTO')+row(tile('TERRA'),piece('↔',.2,'arrow'),tile('APOLLO',.35))+text('Sinais acompanhados em tempo real',.55)
    elif key=='institutions':
        content=title('ALVOS DA TEORIA')+row(tile('PODER',0),tile('FAMA',1.14),tile('INSTITUIÇÕES',2.04))+text('Associação não comprova participação',2.4,'small')
    elif key=='connections':
        content=title('TUDO PARECE CONECTADO...')+row(tile('SÍMBOLO'),piece('↔',.3,'arrow'),tile('EVENTO',.6),piece('↔',.9,'arrow'),tile('COINCIDÊNCIA',1.2))
    elif key=='year1776':
        content=piece('<div class="num">1776</div>')+text('BAVIERA',.3)+text('A origem histórica da ordem',.6)
    elif key=='reason':
        content=title('RAZÃO')+row(tile('PENSAMENTO'),piece('×',.4,'arrow'),tile('INFLUÊNCIA EXCESSIVA',.7))+text('Política e religião',2.25)
    elif key=='dissolve':
        content=row(tile('PROIBIÇÃO'),piece('→',.25,'arrow'),tile('DECLÍNIO',.6))+title('POUCOS ANOS',1.1)
    elif key=='evidence':
        content=piece('<div class="page"><h2>EVIDÊNCIA CONFIÁVEL?</h2><div class="line"></div><div class="line"></div><div class="line"></div></div>')+piece('<div class="seal">NÃO COMPROVADO</div>',.56)+text('Controle dos acontecimentos do mundo',2.62)
    elif key=='share':
        content=title('DE PIADA A TEORIA')+row(tile('RELATO'),piece('→',.3,'arrow'),tile('FÓRUNS',.65),piece('→',.95,'arrow'),tile('REDES',1.35))
    elif key=='agreement':
        content=piece('<div class="page"><h2>ACORDO SECRETO?</h2><div class="line"></div><div class="line"></div><div class="line"></div></div>')+text('Segundo a teoria',.4,'small')
    elif key=='sea-land':
        content=row(tile('MAR'),piece('≠',.15,'arrow'),tile('TERRA',.3))+text('A história transformava o país em oceano',.5)
    elif key=='satire':
        content=title('ONDE TERMINA A PIADA?')+row(tile('SÁTIRA'),piece('↔',.3,'arrow'),tile('CRENÇA',.65))
    else:raise KeyError(key)
    return '<div class="panel">'+content+'</div>'
