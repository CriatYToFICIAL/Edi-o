"""Freeze local sources and map ASR timestamps to the conservatively edited audio."""
import json, re, shutil
from pathlib import Path

mapping=json.loads(Path('audio-edit-map.json').read_text())
def mapped(t):
    return t-sum(max(0,min(t,b)-a) for a,b in mapping['cuts'] if t>a)
data=json.loads(Path('transcript-raw.json').read_text())
for s in data['segments']:
    s['start']=round(mapped(s['start']),3);s['end']=round(mapped(s['end']),3)
    for w in s['words']:
        w['start']=round(mapped(w['start']),3);w['end']=round(mapped(w['end']),3)
        w['word']=w['word'].replace('McKindal','McIndoe')
    s['text']=s['text'].replace('McKindal','McIndoe')
Path('transcript-edited.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
Path('transcript.txt').write_text('\n'.join(f"{s['start']:.2f}–{s['end']:.2f} {s['text']}" for s in data['segments']))
print('Edited transcript:',mapping['edited_duration'])
