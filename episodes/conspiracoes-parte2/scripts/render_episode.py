"""Render with the pinned engine. A short pilot shares all production assets."""
import argparse,json,os,re,subprocess
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
if Path('/usr/bin/chromium').exists():
    os.environ.setdefault('HYPERFRAMES_BROWSER_PATH','/usr/bin/chromium')
os.environ['HYPERFRAMES_NO_TELEMETRY']='1'
local=Path('film/node_modules/.bin/hyperframes'+('.cmd' if os.name=='nt' else '')).resolve()
cli=str(local) if local.exists() else 'hyperframes'
if args.pilot:
    source=Path('film/index.html').read_text()
    source=re.sub(r'(data-composition-id="main"[^>]*data-duration=")[^"]+',r'\g<1>20',source,count=1)
    Path('film/pilot.html').write_text(source)
    command=[cli,'render','film','-c','pilot.html','-o',str(Path('/tmp/parte2-pilot.mp4')),'--workers','4','--quality','looks']
else:
    command=[cli,'render','film','-o',str(Path('film/renders/conspiracoes-parte2.mp4').resolve()),'--workers','4','--quality','looks']
subprocess.run(command,check=True)
