---
name: material-narrativo
description: "Escolhe, pesquisa ou cria o material visual que corresponde a cada frase temporizada de uma narração para vídeos narrativos: fotos, capturas, GIFs, ícones, documentos, diagramas, motion graphics e desenhos vetoriais."
---

# Material narrativo

Use esta Skill depois de transcrever a narração e antes de montar a timeline. O objetivo é responder, para cada intervalo da fala: “qual imagem faz o espectador entender ou sentir exatamente esta frase?”. Trabalhe em conjunto com `canal-caderno-narrativo`, `media-use`, `hyperframes-creative`, `hyperframes-registry` e `hyperframes-core`.

## Entradas e saída

Entrada mínima: áudio ou transcrição com timestamps, assunto do episódio e destino do vídeo. Podem acompanhar links, arquivos, capturas, identidade visual e restrições de licença.

Saída obrigatória: `material-plan.md` ou JSON equivalente com uma linha por batida:

| início–fim | texto da narração | intenção | melhor material | alternativa | origem/licença | tratamento | legenda | estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

`estado` deve ser `local`, `encontrar`, `criar`, `aguardando autorização` ou `descartado`. Nunca invente uma URL, fonte, citação ou licença.

## Método por segundo e por ideia

1. Transcreva e revise o áudio. Una palavras numa batida semântica; não corte uma imagem no meio de uma frase apenas porque um segundo mudou.
2. Marque entidades, objetos, datas, lugares, ações, emoções, comparação, causa, consequência e punchline. A intenção define o tipo de visual.
3. Escolha a função visual: evidenciar, explicar, localizar, comparar, humanizar, reagir, aumentar tensão, fazer humor ou fazer ponte.
4. Proponha primeiro o material mais específico. Só use uma imagem genérica quando ela realmente acrescentar contexto.
5. Dê preferência a material próprio, domínio público, licença compatível ou ativo cuja autorização foi fornecida. Para cada resultado externo, guardar URL, autor, licença, data e crédito.
6. Ajuste o tempo do material à fala: entrada um pouco antes da palavra-chave, repouso durante a informação, saída depois da conclusão. Um GIF ou meme curto pode ser usado como reação; documento ou captura recebe mais tempo.
7. Quando nenhum ativo explica bem a frase, crie uma composição original: cartão de afirmação, diagrama, linha do tempo, mapa simples, ícone flat, setas, destaque de recorte, janela simulada, gráfico ou ilustração vetorial. A criação deve ser factual e legível.
8. Considere texto complementar sob o visual: nome, data, lugar, fonte, rótulo, consequência ou comentário curto. Use-o quando esclarecer ou pontuar a imagem, deixe-o fora quando repetir a fala. No mapa de casos, o nome sob cada card é obrigatório; numa evidência individual, é opcional.

## Roteamento por tipo de fala

| Fala | Material preferido |
| --- | --- |
| Nome de pessoa, programa ou objeto | foto/ícone autorizado, logotipo oficial quando permitido, ou desenho original reconhecível |
| Data, número ou sequência | card tipográfico, timeline ou gráfico simples; usar documento como prova quando existir |
| “Aconteceu em…” | captura/documento/foto do contexto com legenda de fonte |
| Como algo funcionava | diagrama em etapas, captura de interface ou gravação de tela autorizada |
| Comparação ou negação | `EvidencePair` ou `StatementBoard`, com rótulos explícitos |
| Consequência ou caos | captura/GIF da consequência, composição de camadas, alerta ou reação pontual |
| Piada, ironia ou suspense | imagem de reação, meme autorizado, desenho vetorial ou legenda com parêntese; não usar meme aleatório |
| Transição para novo caso | `CaseBridge`: visão geral, foco/zoom, troca de título-avatar e primeira evidência |

## Pesquisa e criação

Pesquise apenas em destinos acessíveis e aprovados pelo ambiente. Registre consultas e resultados escolhidos. Não trate uma busca por imagem como autorização de reutilização. Se uma página não puder ser acessada, marque `aguardando autorização` e peça o arquivo ou uma fonte alternativa quando isso bloquear a cena.

Para GIFs e vídeos, guardar o intervalo usado, fonte, autor e licença. Para capturas de software, ocultar dados pessoais e não reproduzir credenciais. Para documentos e notícias, preservar manchete/data e não alterar o sentido com um crop enganoso.

Para ícones e desenhos flat, preferir SVG original, formas básicas e cores do guia do canal. Para motion, criar o mínimo necessário: entrada do elemento, destaque do termo, conexão entre nós, ou transformação que explica a fala. Não encher uma cena de partículas ou efeitos só porque estão disponíveis.

## Integração com HyperFrames

Use `media-use` para resolver ou tratar mídia, `hyperframes-registry` para procurar componentes existentes e `hyperframes-animation`/`hyperframes-keyframes` para movimento buscável. Coloque cada ativo em sua própria faixa ou composição, com `data-start`, `data-duration` e origem registrada. Para áudio, use os timestamps da transcrição e `hyperframes-audio`. Valide mídia ausente, proporção, crop, contraste, legibilidade e direitos antes do render.

## Controle de qualidade

- A imagem realmente corresponde às palavras naquele intervalo?
- A entrada acontece no ponto narrativo certo e há tempo de leitura?
- A fonte está registrada e seu uso é permitido?
- O crop preserva contexto e não cria uma afirmação falsa?
- O material tem tamanho, contraste e proporção adequados?
- O visual é original quando a referência só serviu como inspiração?
- Se o ativo falhar, existe uma alternativa criada ou já autorizada?


## Revisão de variedade e movimento (V2)

- Limitar cada imagem, ícone ou desenho ilustrativo a duas aparições por episódio. Contar também imagens embutidas em interfaces. A grade de casos e o avatar persistente são identificadores e ficam fora dessa contagem. Exceções para evidência indispensável precisam de justificativa no plano.
- Variar conteúdo e composição, não apenas trocar a legenda do mesmo desenho. Preferir evidência específica, interfaces, documentos, fotos, clipes e diagramas originais.
- Sincronizar elementos secundários com a palavra que introduz seu significado; o início da cena não implica revelar todos os elementos.
- Evitar saltos: a pose inicial do movimento interno deve coincidir com a primeira pose visível. Não começar um fromTo tardio com posição diferente da posição já exibida. Verificar buscas para frente e para trás.
- Interfaces reconstruídas devem ser identificadas como reconstituição; não inventar citação, usuário, votos, data ou documento oficial. Se uma informação não foi confirmada, separar a alegação da evidência visual.
