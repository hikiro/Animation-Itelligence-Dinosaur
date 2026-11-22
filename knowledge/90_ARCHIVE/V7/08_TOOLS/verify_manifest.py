#!/usr/bin/env python3
"""Verify SHA256 hashes listed in MANIFEST_SHA256.json. Run in extracted project root."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parents[1]
manifest=root/'MANIFEST_SHA256.json'
if not manifest.exists(): print('NO MANIFEST');sys.exit(2)
data=json.loads(manifest.read_text())
bad=[]
for name, sha in data['files'].items():
    p=root/name
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=sha: bad.append(name)
extra=[str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST_SHA256.json' and str(p.relative_to(root)) not in data['files']]
print('Checked',len(data['files']),'files; mismatches',len(bad),'unexpected files',len(extra))
for b in bad:print('MISMATCH',b)
for e in extra:print('EXTRA',e)
sys.exit(1 if bad or extra else 0)
