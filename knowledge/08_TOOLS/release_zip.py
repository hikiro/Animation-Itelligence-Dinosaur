#!/usr/bin/env python3
"""Rebuild manifest/portable zip for CURRENT extracted root; documentation QA only."""
from pathlib import Path
import argparse,hashlib,subprocess,sys,zipfile
ROOT=Path(__file__).resolve().parents[1]

ap=argparse.ArgumentParser();ap.add_argument('--audit',action='store_true');ap.add_argument('--output',default=str(ROOT.parent/(ROOT.name+'.zip')));a=ap.parse_args()
subprocess.run([sys.executable,str(ROOT/'08_TOOLS/search_repo.py'),'--rebuild'],check=True)
manifest=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='FILE_MANIFEST_SHA256.txt':
        manifest.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix())
(ROOT/'FILE_MANIFEST_SHA256.txt').write_text('\n'.join(manifest)+'\n',encoding='utf8')
if a.audit:subprocess.run([sys.executable,str(ROOT/'08_TOOLS/audit_repo.py')],check=True)
out=Path(a.output)
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as z:
    for p in ROOT.rglob('*'):
        if p.is_file():z.write(p,arcname=str(Path(ROOT.name)/p.relative_to(ROOT)))
with zipfile.ZipFile(out) as z:
    error=z.testzip()
    if error:raise RuntimeError('ZIP CRC failed '+error)
print('Wrote',out,'with',len(manifest)+1,'files')
