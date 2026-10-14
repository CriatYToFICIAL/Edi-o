import json
import sys
import os
from pathlib import Path
from faster_whisper import WhisperModel

source, destination = sys.argv[1:3]
model = WhisperModel(os.environ.get('WHISPER_MODEL','small'), device='cpu', compute_type='int8', cpu_threads=3,
                     download_root='/workspace/.cache/whisper')
segments, info = model.transcribe(source, language='pt', beam_size=5,
                                  word_timestamps=True, vad_filter=True)
result = []
for segment in segments:
    item = {'start': segment.start, 'end': segment.end, 'text': segment.text,
            'words': [{'start': w.start, 'end': w.end, 'word': w.word,
                       'probability': w.probability} for w in segment.words or []]}
    result.append(item)
    print(f'{segment.start:.2f}–{segment.end:.2f} {segment.text}', flush=True)
Path(destination).write_text(json.dumps({'language': info.language, 'segments': result},
                                        ensure_ascii=False, indent=2))
