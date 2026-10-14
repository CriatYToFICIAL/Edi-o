"""Package the editable episode, channel skills and local assets without caches."""
import zipfile
from pathlib import Path
root=Path('/workspace/Edi-o')
out=Path('/workspace/conspiracoes-parte1-projeto.zip')
exclude={'.git','node_modules','.hyperframes','__pycache__','renders','qc-scenes','qc-export'}
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=5) as z:
    for p in sorted(root.rglob('*')):
        if not p.is_file() or any(s in exclude for s in p.relative_to(root).parts):continue
        if p.name=='render.log':continue
        z.write(p,Path('Edi-o')/p.relative_to(root))
print(out, out.stat().st_size)
