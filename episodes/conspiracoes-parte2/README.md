# Todas as maiores teorias da conspiração — Parte 2

Continuação da Parte 1: Aves não são reais, Reptilianos e Terra plana.

O projeto preserva a grade, fonte Comic Neue, cabeçalho, sete casos no índice e zoom de seleção. As legendas são opcionais. Imagens, GIFs e ícones foram escolhidos por função narrativa, com entradas secundárias temporizadas por palavra. Nenhum texto visível fala sobre os bastidores da narração.

## Editar e reconstruir

Edite `scripts/scene_data_v2.py` para imagens, textos e tempos; `scripts/v2_panels.py` para as explicações vetoriais/interfaces; `scripts/build_film.py` para os tokens de layout e a montagem. Os arquivos HTML em `film/compositions/` também são editáveis diretamente; reconstruir sobrescreve esses HTML.

Na pasta deste episódio:

```bash
python -m pip install Pillow
python scripts/build_film.py
cd film
npm ci
npm run check
npm run render -- --output renders/conspiracoes-parte2.mp4 --workers 4
```

Requisitos: Python 3, Node.js, FFmpeg e Chromium. Em Linux, se necessário, defina `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium`. HyperFrames está fixado em 0.8.156.

`source/parte2.mp3` é o original. `narracao.wav` é o áudio tratado; `audio-edit-map.json` registra cada corte. `transcript-edited.json` contém a transcrição temporizada com os tempos remapeados após os cortes. Não é necessário transcrever novamente para mudar elementos visuais.

Consulte `material-plan.md`, `CREDITS.md`, `research/facts.md` e os relatórios de validação. Os créditos acompanham a distribuição do vídeo e devem ser preservados na descrição de publicação. Mantenha as licenças dos ativos reutilizados.
