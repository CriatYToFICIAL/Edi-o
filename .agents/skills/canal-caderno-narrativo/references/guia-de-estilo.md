# Guia de estilo e movimento

Valores abaixo são ponto de partida para 1920×1080. Foram normalizados a partir do vídeo 640×360 e das capturas 1920×1080; ajuste depois de renderizar uma cena piloto e comparar lado a lado.

## Tokens da moldura

| Elemento | Especificação inicial |
| --- | --- |
| Formato | 16:9, base 1920×1080, 30 fps; adaptar posição relativa para outros formatos sem esticar. |
| Papel | Branco quente/cinza muito claro, aproximadamente `#f4f4f2` a `#f8f8f7`; textura quase imperceptível. |
| Grade | Linhas cinzas de 1–2 px a cada ~62–64 px em 1080p, sem dominar fotos ou texto. Testar `#d1d1cf` com opacidade moderada. |
| Avatar | Círculo ~140 px, x≈64–70, y≈38–42; contorno preto ~4–6 px. Troca por caso/episódio. Usar avatar original do canal. |
| Título do caso | Centro horizontal, topo y≈40–55; preto, maiúsculas, peso alto, altura visual ~60–70 px; manter faixa vazia ao redor. |
| Fonte | Preferência declarada: Comic Sans MS quando a fonte for fornecida/licenciada; substituto aberto visualmente próximo: Comic Neue Bold. Testar acentos em português. Não usar fonte condensada, futurista ou serifada. |
| Zona principal | Aproximadamente x=70–1850 e y=205–900; deixar a grade respirar em torno dos elementos. |
| Legendas | Geralmente 36–46 px em 1080p, pretas, peso médio/alto; abaixo do card, separação ~8–18 px. Para duas colunas, legenda centralizada sob cada coluna. |
| Sombra | Deslocamento leve para baixo/direita (~6–14 px em 1080p), blur macio (~10–24 px), cinza/preto de baixa opacidade; consistente entre cards. |
| Cores de ênfase | Preto como padrão. Vermelho para proibição, erro, palavra de impacto ou carimbo; amarelo para aviso. Azul vem das interfaces/ativos, não da moldura. |

## Componentes reutilizáveis

1. **CaseShell:** papel quadriculado, avatar, título. Persiste durante todas as cenas do caso; ao mudar de caso, atualizar ambos juntos.
2. **EvidenceCard:** uma foto, documento, captura, ilustração ou vídeo. Manter proporção; aplicar sombra; legenda editorial curta sob o card. Em captura com texto pequeno, destacar uma região com crop ampliado ou redesenhar um excerto fiel, com fonte registrada.
3. **EvidencePair:** dois cards de escala visual similar. Entradas podem ser escalonadas em ~0,2–0,6 s quando a narração apresenta uma ideia de cada vez. Cada card pode ter legenda própria; não competir por largura.
4. **StatementBoard:** ilustração grande em uma metade, 2–3 afirmações curtas na outra. Aparecer por linha ou em etapas de narração; manter amplo espaço vertical. A última linha ou legenda pequena pode virar a expectativa.
5. **ReactionBeat:** GIF, foto ou desenho curto. Usar para consequência irônica ou pausa; voltar rapidamente à linha factual. Não utilizar um meme só por preencher tempo.
6. **EscalationPanel:** um card de interface que acumula janelas, alertas ou erros conforme a história piora. Limitar a desordem ao card; manter moldura e legenda legíveis.
7. **ImpactLabel:** uma palavra/expressão vermelha ou um carimbo sobre a evidência. Usar raramente, com entrada rápida e repouso legível.
8. **CaseBridge:** fechar com resultado ou piada do caso A; introduzir primeiro ativo do caso B; trocar título/avatar quando a narração fizer a mudança explícita.
9. **OverviewGrid:** grade de cards de todos os casos/personagens/itens do episódio. Cada card tem uma imagem ou ícone, cantos arredondados, sombra coerente e nome curto embaixo. Use-a como índice visual antes de aproximar o caso atual.

## Ritmo e animação

- Fazer a troca principal em uma fronteira de frase ou ideia. Começar por 2–5 s por composição; estender documentos/capturas que exigem leitura e encurtar reações. Ajustar ao áudio real, nunca cravar duração antes de escutá-lo.
- Para entrada normal de card: corte limpo ou fade curto (aprox. 0,15–0,45 s) com deslocamento/escala mínimos. Usar saída igualmente curta. Dissolvência de ~0,3–0,7 s é aceitável entre blocos ou casos; o vídeo mostra dissolvências perceptíveis em algumas trocas.
- Não animar a grade, título e avatar em cada frase. Eles ancoram o vídeo. Movimento mais vivo pertence aos ativos narrados (gravação de tela, GIF, pixel art, carimbo, erro).
- Dar a imagens estáticas tempo de repouso antes de sair. Se duas evidências aparecem juntas, atrasar a segunda quando houver ordem na narração.
- Reservar zoom expressivo para revelação, reação ou detalhe que precisa ser lido; evitar Ken Burns em todos os cards.
- Fazer a piada visual aparecer no momento da virada verbal ou logo após ela. A legenda pode carregar a punchline quando a imagem é séria.
- Preservar curiosidade e progressão. Uma lista enorme de prints parados não reproduz o ritmo observado.

### Dinamismo e textos complementares

O vídeo deve permanecer dinâmico mesmo quando o assunto é calmo. Alterne evidência, comparação, frase de apoio, ícone, diagrama, reação e breve movimento conforme a narração muda de ideia. Não transforme cada segundo em uma troca: mantenha repouso suficiente para compreensão.

Use textos complementares abaixo das imagens quando eles acrescentarem identificação, contexto, ironia, fonte, data, consequência ou uma observação curta. Eles devem ser curtos, legíveis e visualmente ligados ao card. Não precisam aparecer em todas as imagens; a ausência também cria ritmo. Evite repetir literalmente a narração ou encher o quadro de legendas.

## Contratos de animação

Toda entrada deve ser descrita no plano com `alvo`, `origem`, `escala inicial/final`, `opacidade`, `duração`, `easing` e `gatilho da narração`. Use quatro fases:

1. **Preparação:** o card ainda não domina o quadro; pode estar menor, deslocado ou transparente.
2. **Entrada:** revela-se em corte, fade curto, escala suave ou deslocamento pequeno. A técnica deve combinar com a função da imagem.
3. **Repouso:** o card fica estável o bastante para ser entendido e lido.
4. **Ênfase/saída:** um zoom, carimbo, destaque ou saída acontece apenas quando a frase pede; depois o card sai ou perde prioridade.

Cards normais devem parecer colocados sobre o papel, com movimento curto e sem elasticidade exagerada. GIFs, gravações de tela, pixel art e telas de erro podem ter movimento interno próprio. O fundo quadriculado, o título e o avatar funcionam como âncora e não devem acompanhar cada entrada.

### Transição de caso

Na abertura ou entre capítulos, montar a sequência em quatro planos: (1) visão geral com todos os cards numa grade, como na referência enviada — imagem/ícone no card e nome curto embaixo; (2) início do zoom direcionado ao centro do card escolhido; (3) aproximação progressiva até o card ocupar a composição, preservando proporção e sombra; (4) confirmação/troca do título e avatar e entrada da primeira evidência do caso. O áudio deve anunciar a escolha durante a aproximação. O zoom deve parecer uma câmera que entra no mapa de casos, não um corte com imagem ampliada. A duração e o easing exatos continuam parâmetros de calibração até haver um trecho em movimento com resolução suficiente.

## Texto editorial

- Título: nome curto do caso, normalmente em maiúsculas.
- Legenda: uma oração ou expressão coloquial. Use reticências para preparar continuação e parênteses para apartes. Não encha o quadro com transcrição integral.
- Afirmação grande: até três linhas curtas, espaçadas; maior impacto para negação, contraste e dado surpreendente.
- Revisar português, acentos, nomes e fatos. Manter consistência de “você”, “pra” e outras escolhas de voz do canal após o primeiro vídeo aprovado.

## Variantes para testar com o usuário

A cor exata do papel, o arquivo da fonte, a intensidade da sombra e o tempo das entradas devem ser calibrados numa cena piloto renderizada. As capturas mostram a disposição com alta fidelidade; o MP4 comprimido não sustenta precisão de cor ou de animação por pixel.


## Revisão de variedade e movimento (V2)

Correção para a continuação: legenda sob o card é opcional. Quando já há uma afirmação grande ou texto explicativo suficiente dentro da imagem, não acrescentar uma segunda explicação embaixo. Usar frases complementares apenas para identificação, contexto indispensável ou humor pertinente. Não colocar no vídeo textos sobre a própria narração, transcrição, processo de produção ou limitações de pesquisa. Apresentar hipóteses como hipóteses e interfaces originais como reconstituições com linguagem natural ao público. Detalhes de verificação e créditos completos pertencem aos documentos de produção e à descrição da publicação.

- Limitar cada imagem, ícone ou desenho ilustrativo a duas aparições por episódio. Contar também imagens embutidas em interfaces. A grade de casos e o avatar persistente são identificadores e ficam fora dessa contagem. Exceções para evidência indispensável precisam de justificativa no plano.
- Variar conteúdo e composição, não apenas trocar a legenda do mesmo desenho. Preferir evidência específica, interfaces, documentos, fotos, clipes e diagramas originais.
- Sincronizar elementos secundários com a palavra que introduz seu significado; o início da cena não implica revelar todos os elementos.
- Evitar saltos: a pose inicial do movimento interno deve coincidir com a primeira pose visível. Não começar um fromTo tardio com posição diferente da posição já exibida. Verificar buscas para frente e para trás.
- Interfaces reconstruídas devem ser identificadas como reconstituição; não inventar citação, usuário, votos, data ou documento oficial. Se uma informação não foi confirmada, separar a alegação da evidência visual.
