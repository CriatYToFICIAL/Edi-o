from PIL import Image,ImageOps,ImageDraw
from pathlib import Path
import subprocess,json
base=Path(__file__).resolve().parents[1];folder=base/'film/public/media/v2';research=base/'research-v2'
for name in ['aldrin-steps','apollo-launch']:
    for sec in [1,5,10]:
        subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss',str(sec),'-i',str(folder/(name+'.mp4')),'-frames:v','1',str(research/(name+str(sec)+'.jpg'))],check=True)
files=[p for p in folder.iterdir() if p.suffix.lower() in ['.jpg','.png']]+list(research.glob('aldrin-steps*.jpg'))+list(research.glob('apollo-launch*.jpg'))
sheet=Image.new('RGB',(1280,((len(files)+3)//4)*240),'#ececec');draw=ImageDraw.Draw(sheet)
for i,path in enumerate(files):
    im=Image.open(path).convert('RGB');im.thumbnail((310,208));x=(i%4)*320;y=(i//4)*240;sheet.paste(im,(x+(320-im.width)//2,y));draw.text((x+5,y+210),path.name,fill='black')
sheet.save(research/'contact.jpg')
