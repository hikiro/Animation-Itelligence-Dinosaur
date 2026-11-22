#!/usr/bin/env python3
"""Build deterministic V7 SHA256 manifest. Excludes the JSON manifest itself (avoids a cycle)."""
from pathlib import Path
import json,hashlib,sys
root=Path(__file__).resolve().parents[1]
txt=root/'FILE_MANIFEST_SHA256.txt'; manifest=root/'MANIFEST_SHA256.json'
files=sorted([p for p in root.rglob('*') if p.is_file() and p not in (manifest,txt)])
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
txt.write_text(''.join(f'{sha(p)}  {p.relative_to(root).as_posix()}\n' for p in files),encoding='utf8')
items={p.relative_to(root).as_posix():sha(p) for p in files+[txt]}
manifest.write_text(json.dumps({'package':'DINO_DISASTER_ANIMATION_LEARNING_AGENT_KIT_V7','created_utc':'2026-11-19','files':dict(sorted(items.items()))},indent=2)+'\n',encoding='utf8')
print('Generated manifest with',len(items),'files')
