# Todas as maiores teorias da conspiração explicadas — parte 1

Vídeo renderizado em film/renders/conspiracoes-parte1.mp4; validações aprovadas em VALIDATION.md.

Projeto HyperFrames horizontal, 1920×1080, 30 fps; duração 333,37 s (5min33s). Quatro capítulos narrados: Área 51, Chegada à Lua, Illuminati e Finlândia. O painel de transições inclui os sete casos solicitados, também Aves não são reais, Reptilianos e Terra plana.

76 batidas visuais combinam fotografias documentais, três trechos animados de fontes públicas, 20 desenhos SVG originais, textos complementares e panorâmica com zoom centrado no card do capítulo. Tipografia Comic Neue como alternativa local à Comic Sans MS, cujo arquivo licenciado não foi fornecido.

## Áudio

Original preservado em source/audiobruto.mp3. Seis pausas abaixo de -38 dB foram encurtadas, preservando respiro: 1,94 s removidos. Filtro de graves 65 Hz e normalização -16 LUFS, teto -1,5 dB. Mapa reversível em audio-edit-map.json. A transcrição local Whisper tem timestamps por palavra; nomes próprios e alegações merecem revisão humana. Não foi realizada audição humana integral.

## Arquivos

- film/index.html e film/compositions/: edição HTML/GSAP, timeline determinística.
- film/public/: áudio, fontes e materiais locais; o projeto não precisa buscar imagens durante o render.
- material-plan.md/json: fala, tempos, material e motivo de seleção por cena.
- CREDITS.md e asset-ledger.json: autoria, links, licenças e materiais excluídos.
- media-review.md e fact-notes.md: revisão de pertinência e limitações factuais.
- timing-contract.json: entradas de elementos com prazos exatos; timing-validation.json: resultado de conferência no runtime.
- check-final.json: validação HyperFrames; amostragem global de movimento de 300 pontos, complementada pelas verificações de tempo exato.

## Reproduzir

Da pasta deste episódio, instalar dependências com npm ci --prefix film. HyperFrames 0.8.154, Node 24, Chromium e FFmpeg. Reconstruir com python scripts/build_film.py (Pillow necessário). Definir HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium quando o navegador local não for detectado. Renderizar com hyperframes render film --quality delivery --workers 4 --output film/renders/conspiracoes-parte1.mp4. A versão exata do CLI está nos scripts npm do projeto.

## Revisão editorial

A alegação sobre Pursue/maio de 2026 e 160 arquivos (aproximadamente 00:59–01:19) não foi confirmada pelas fontes acessíveis. A narração foi preservada e o material não apresenta ilustração como prova. Conferir fact-notes.md antes de publicar. O GIF da bandeira lunar é montagem de fotografias, identificado como tal. Nenhuma publicação externa foi feita.
