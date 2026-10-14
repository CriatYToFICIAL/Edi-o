"""Conservative silence shortening; preserves the original and a source time map."""
import json
import re
import subprocess
import sys
from pathlib import Path

source, destination = sys.argv[1:3]
duration = float(subprocess.check_output(['ffprobe','-v','error','-show_entries',
    'format=duration','-of','default=noprint_wrappers=1:nokey=1',source]))
scan = subprocess.run(['ffmpeg','-hide_banner','-i',source,'-af',
    'silencedetect=noise=-38dB:d=0.45','-f','null','-'],capture_output=True,text=True,check=True)
starts = [float(x) for x in re.findall(r'silence_start: ([\d.]+)',scan.stderr)]
ends = [float(x) for x in re.findall(r'silence_end: ([\d.]+)',scan.stderr)]
cuts = [(a+0.15,b-0.15) for a,b in zip(starts,ends) if b-a > 0.45]
kept = []
cursor = 0.0
outtime = 0.0
for a,b in cuts + [(duration,duration)]:
    if a > cursor:
        kept.append({'source_start':cursor,'source_end':a,'output_start':outtime,
                     'output_end':outtime+a-cursor})
        outtime += a-cursor
    cursor = b
filters = [f'[0:a]atrim=start={s["source_start"]}:end={s["source_end"]},asetpts=PTS-STARTPTS[a{i}]'
           for i,s in enumerate(kept)]
filters.append(''.join(f'[a{i}]' for i in range(len(kept)))+
               f'concat=n={len(kept)}:v=0:a=1,highpass=f=65,loudnorm=I=-16:TP=-1.5:LRA=11[out]')
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',source,
    '-filter_complex',';'.join(filters),'-map','[out]','-ar','48000','-c:a','pcm_s16le',destination],check=True)
Path('audio-edit-map.json').write_text(json.dumps({'source_duration':duration,
    'edited_duration':outtime,'removed_seconds':duration-outtime,'cuts':cuts,'kept':kept},indent=2))
print(json.dumps({'raw_duration':duration,'edited_duration':outtime,
                  'removed_seconds':duration-outtime,'cuts':len(cuts)},indent=2))
