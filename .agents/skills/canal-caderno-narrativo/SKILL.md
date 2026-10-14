---
name: canal-caderno-narrativo
description: "Analisa referências e planeja ou produz vídeos narrados de casos de internet no estilo caderno quadriculado: moldura persistente, evidências visuais, legendas editoriais curtas, humor pontual e ritmo guiado pela narração. Use para criar a identidade original do canal, um plano de cenas ou uma composição HyperFrames."
---

# Canal Caderno Narrativo

Esta Skill transforma a linguagem editorial observada nas referências do usuário em um sistema próprio e reutilizável. A referência inicial é `aee.mp4` (120,23 s, 640×360, 30 fps), acompanhada por duas capturas de “VÍRUS MU” em 1920×1080. Leia [a análise com tempos e limites da evidência](references/analise-das-referencias.md) antes de usar os padrões abaixo. Leia [o guia visual e de movimento](references/guia-de-estilo.md) antes de desenhar cenas. Use [o modelo de plano e a revisão](references/producao.md) antes de renderizar.

## Resultado esperado

Produza, conforme a tarefa, um diagnóstico de referência, uma especificação de estilo, um plano de edição com tempos ou um vídeo. Em trabalhos futuros, mantenha a identidade do canal estável e adapte assunto, imagens e piadas ao episódio. Diferencie observação comprovada, inferência e escolha criativa. Uma referência comprimida permite medir estrutura e posição, mas não provar a fonte exata, cor exata ou curva de animação ao nível de pixel.

## Núcleo editorial

1. **Moldura fixa:** fundo claro quadriculado, identificador circular no alto à esquerda e nome curto do caso centralizado no alto. O nome e o avatar mudam quando muda o caso; o fundo continua.
2. **Uma afirmação por batida:** cada card explica uma frase da narração. A legenda é uma síntese editorial de uma linha, colocada sob o elemento a que se refere; não transcreve cada palavra em estilo karaokê.
3. **Evidência concreta primeiro:** telas, páginas, fotos, documentos, interfaces e imagens pertinentes são recortados sobre o caderno como cartões físicos. Ilustrações e memes entram quando simplificam ou pontuam a ideia.
4. **Progressão:** alternar enquadramento único, dois elementos em comparação, cartão de afirmação, reação breve e retorno à evidência. A imagem aparece quando a narração a nomeia ou prepara o sentido; manter o quadro tempo suficiente para ler.
5. **Ponte entre casos:** encerrar o caso atual com uma visão de conjunto dos elementos/personagens já apresentados; fazer uma aproximação gradual (zoom) no elemento que será introduzido em seguida; pousar nele e trocar título/avatar no ponto em que a narração anuncia o próximo caso. O zoom é uma ponte narrativa, não um efeito decorativo. Se a referência concreta não mostrar essa ponte, marcar o comportamento como hipótese e validar com o trecho correspondente.
6. **Humor controlado:** legendas coloquiais, parênteses, elipses, trocadilhos visuais e um meme curto criam respiro. O humor acompanha a informação; não substitui a explicação.
7. **Dinamismo editorial:** manter o vídeo vivo com alternância de cards, comparações, frases de apoio, pequenas entradas e saídas, zooms pontuais, GIFs, ícones, diagramas e reações. A escolha do material deve seguir o assunto do episódio; não transportar elementos de vírus, bugs ou informática para outros temas apenas porque aparecem na referência.

## Ao receber novas referências

- Registre fonte, duração, resolução, formato e trechos relevantes. Para vídeo local, gere contatos de quadros em intervalos de 1–2 s e amplie quadros nas mudanças de cena. Inspecione entradas e saídas em passos menores antes de afirmar uma duração de transição.
- Separe: estrutura narrativa, frequência de mudança visual, disposição, tipografia, tratamento de imagens, movimento, legenda, som e humor. Para cada observação, anote um timestamp ou captura. Não deduza música ou efeitos sonoros apenas de um quadro.
- Compare cada nova referência com o padrão inicial. Atualize o guia quando houver repetição suficiente; trate exceções como variantes de cena.
- Se houver áudio e transcrição disponível, alinhe frases e pausas com os quadros. Se a transcrição não estiver disponível, use o texto visível como evidência parcial e registre a lacuna.
- Preserve os materiais de referência como insumo de análise. Recrie princípios, timing e funções visuais com ativos próprios ou licenciados. Não reutilize avatar, logotipo, montagens, memes protegidos ou cenas do canal de referência no vídeo final sem autorização.

## Ao receber narração e material do novo episódio

1. Inspecione o áudio: duração, idioma, ruído, pausas e picos. Transcreva com tempos por frase ou palavra e corrija nomes, datas e termos técnicos.
2. Divida a narração em afirmações verificáveis. Faça uma linha de plano por batida usando o modelo em `references/producao.md`. Defina o que o público deve entender em cada mudança visual.
3. Associe a cada batida uma evidência, ilustração, captura ou reação. Registre fonte, licença, crédito e posição temporal. Se não houver imagem pertinente, use texto, diagrama ou interface original em vez de material genérico.
4. Distribua os layouts do guia. Dê prioridade à leitura: um card principal ou dois cards relacionados por vez. Reserve a tela de afirmação para negações, números, viradas e sínteses.
5. Desenhe o movimento a serviço da frase: entrada curta, repouso legível, saída discreta. Não aplique zoom contínuo automático a todas as imagens.
6. Modele cada animação como `preparação → entrada → repouso → ênfase → saída`. Registre o alvo, o ponto de origem, a escala, o deslocamento, a opacidade, a duração e o easing. Cards normais entram com pequena escala/opacidade ou deslocamento; cards de impacto podem usar zoom mais evidente; a grade e o cabeçalho não pulsam a cada batida.
7. Para a transição de caso, use `overview-grid → focus zoom → title/avatar swap → first evidence`. O quadro geral apresenta todos os casos em cards numa grade, cada um com imagem/ícone e nome complementar embaixo. A câmera escolhe o card anunciado, aproxima-se progressivamente do centro dele e usa o repouso final para trocar ou confirmar o título/avatar; a primeira evidência entra alinhada à primeira frase do novo bloco. Preserve os outros cards no quadro geral até o zoom começar. Essa transição é uma gramática geral para capítulos, personagens, produtos, lugares ou eventos, sem depender de vírus.
6. Monte uma prévia curta representativa antes de produzir o episódio inteiro. Compare com as referências em ritmo, hierarquia e legibilidade. Ajuste os tokens apenas com evidência visual.
7. Faça revisão factual, visual e sonora; então renderize a versão solicitada. Entregue também o projeto editável, o plano de cenas e o registro de fontes.

## Implementação com HyperFrames

Use a Skill oficial `hyperframes` como porta de entrada e consulte, conforme a tarefa, `hyperframes-core`, `hyperframes-animation`, `hyperframes-keyframes`, `hyperframes-audio`, `media-use` e `hyperframes-cli`. Esta Skill define a linguagem do canal; as Skills oficiais definem a sintaxe e os comandos do motor.

Mantenha fundo, avatar e título como camadas persistentes. Coloque evidências, textos e reações em faixas separadas e com `start`/`duration` explícitos. Animações devem ser determinísticas e buscáveis pelo tempo para que prévia e render final coincidam. Use o mecanismo de mídia e áudio do HyperFrames para posicionar clipes, narração, trilha e fades. Verifique com `hyperframes lint`, `hyperframes check` e capturas em inícios, meios e fins de cenas; assista ao render para validar sincronização e áudio. Não declare uma capacidade como verificada apenas por existir no plano.

## Critérios de aceite

- A moldura, título e avatar estão visíveis e alinhados em todas as cenas do mesmo caso.
- Cada troca visual corresponde a uma nova ideia ou ênfase da narração; cada card tem tempo para ser lido.
- As legendas pertencem visualmente aos cards e não cobrem a evidência.
- Fontes pequenas em capturas são ampliadas, recortadas ou resumidas; não dependem de leitura impossível no vídeo final.
- Imagens não ficam esticadas, deformadas ou com sombras inconsistentes.
- Afirmações factuais e licenças de uso foram verificadas; créditos e URLs permanecem no registro de fontes.
- A prévia e o arquivo final foram inspecionados visualmente e tiveram áudio conferido.
