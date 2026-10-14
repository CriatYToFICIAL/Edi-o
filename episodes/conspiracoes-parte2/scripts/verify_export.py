"""Verify exported codecs/duration and audio alignment; decode representative frames."""
import json,subprocess
from pathlib import Path
import numpy as np
video=Path('film/renders/conspiracoes-parte2-v2.mp4')
expected=json.loads(Path('audio-edit-map.json').read_text())['edited_duration']
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(video)]))
v=next(x for x in probe['streams'] if x['codec_type']=='video');a=next(x for x in probe['streams'] if x['codec_type']=='audio')
Path('qc-export-v2').mkdir(exist_ok=True)
for name,src in [('reference','narracao.wav'),('export',str(video))]:
 subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vn','-ac','1','-ar','16000','-f','f32le',f'/tmp/conspiracy-{name}.f32'],check=True)
x=np.fromfile('/tmp/conspiracy-reference.f32',np.float32)[::8];y=np.fromfile('/tmp/conspiracy-export.f32',np.float32)[::8]
best=(-1,0)
for lag in range(-40,41):
 xx=x[max(0,-lag):]; yy=y[max(0,lag):]; n=min(len(xx),len(yy));xx=xx[:n];yy=yy[:n]
 corr=float(np.dot(xx,yy)/(np.sqrt(np.dot(xx,xx)*np.dot(yy,yy))+1e-10))
 if corr>best[0]:best=(corr,lag/2000)
decode=subprocess.run(['ffmpeg','-v','error','-i',str(video),'-f','null','-'],capture_output=True,text=True)
times=[.1,.7,7.8,16.5,24.5,38.9,55.5,64.9,74.99,92.5,103.8,112.5,133.8,142.8,153.8,171.5,177.9,191.4,205.8,218.6]
frames=[round(t*30) for t in times]
expr='+'.join(f'eq(n,{n})' for n in frames)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(video),'-vf',f'select={expr.replace(",", chr(92)+",")}', '-fps_mode','vfr','-q:v','3','qc-export-v2/frame-%02d.jpg'],check=True)
result={'duration':float(probe['format']['duration']),'size_bytes':int(probe['format']['size']),'video':{k:v.get(k) for k in ['codec_name','width','height','r_frame_rate','nb_frames']},'audio':{k:a.get(k) for k in ['codec_name','sample_rate','channels']},'audio_correlation':best[0],'audio_offset_seconds':best[1],'decode_exit_code':decode.returncode,'decode_errors':decode.stderr.strip(),'frame_times':times}
result['passed']=v['width']==1920 and v['height']==1080 and v['r_frame_rate']=='30/1' and abs(result['duration']-expected)<.1 and best[0]>.98 and abs(best[1])<.02 and decode.returncode==0 and not decode.stderr.strip()
Path('export-validation-v2.json').write_text(json.dumps(result,indent=2));print(json.dumps(result));raise SystemExit(0 if result['passed'] else 1)
