from pathlib import Path
import shutil
import subprocess

source = Path('source/media')
source.mkdir(parents=True,exist_ok=True)
for media in Path('film/public/media').glob('*.jpg'):
    if not (source/media.name).exists():
        shutil.copyfile(media,source/media.name)
    subprocess.run(['magick',str(source/media.name),'-resize','1920x1920>',
                    '-quality','88',str(media)],check=True)
print('JPEG proxies optimized; downloads retained in source/media.')
