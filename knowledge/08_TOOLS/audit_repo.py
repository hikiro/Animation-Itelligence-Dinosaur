#!/usr/bin/env python3
"""Audit V8 canon, preset contracts, logs, search DB, and hash manifest.
This is documentation integrity only. It DOES NOT verify aesthetic or animation quality."""
import hashlib,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
errors=[];checks=0

def check(ok,msg):
    global checks
    checks+=1
    if not ok: errors.append(msg)

mandatory=['README.md','AGENTS.md','00_START_HERE/READ_ORDER.md','00_START_HERE/RECOVERY.md',
 '01_RULES/ANIMATION_RULEBOOK.md','01_RULES/DO_AND_DONT.md','01_RULES/GOOD_ANIMATION.md',
 '01_RULES/CONTEXT_AND_STORY.md','01_RULES/RIGGING_FOUNDATIONS.md','01_RULES/CREATURE_SIZE_ADAPTATION.md',
 '02_RESEARCH/LEARNING_LOG.md','02_RESEARCH/SOURCE_LEDGER.md','02_RESEARCH/ACCESS_GAPS.md',
 '03_PRESET_LIBRARY/SCHEMA.json','03_PRESET_LIBRARY/INDEX.md','03_PRESET_LIBRARY/PRESET_CATALOG.json',
 '06_PROJECTS/DINO/STATUS.md','07_LOGS/CONFLICTS.md','07_LOGS/DECISIONS.md',
 '07_LOGS/SESSION_LOG.md','08_TOOLS/knowledge_search.sqlite','90_ARCHIVE/V7/README.md']
for f in mandatory: check((R/f).is_file(),'Required file missing: '+f)

catalog=json.loads((R/'03_PRESET_LIBRARY/PRESET_CATALOG.json').read_text())
ids=[p['id'] for p in catalog]
check(len(ids)==len(set(ids)), 'Duplicate preset IDs')
check(len(catalog)>=65,'Too few seed presets (expected >=65)')
sections=['Human-language instruction and viewer goal','Required scene context','Causal event graph','Rig, mechanics and interaction plan',
'Camera and editorial direction','Audio and music direction','Context-dependent directing variants','Body plan and size adaptation',
'Failure patterns and safety checks','Acceptance tests','Missing evidence']
sourceids=set(re.findall(r'SRC-\d{3}',(R/'02_RESEARCH/SOURCE_LEDGER.md').read_text()))
for p in catalog:
    path=R/p['path'];check(path.is_file(),p['id']+': missing file')
    if not path.is_file(): continue
    t=path.read_text(encoding='utf8')
    for h in sections: check(h in t,p['id']+': missing '+h)
    check('NOT YET RUN' in t,p['id']+': lost explicit unverified test status')
    check(p['status']=='designed_unverified',p['id']+': unexpected promoted state')
    for src in p['source_ids']:check(src in sourceids,p['id']+': bad source '+src)
check('NOT RENDERED' in (R/'06_PROJECTS/DINO/STATUS.md').read_text(), 'Missing truthful portal benchmark status')

manifest=R/'FILE_MANIFEST_SHA256.txt'
if manifest.exists():
    for line in manifest.read_text(encoding='utf8').splitlines():
        expected,rel=line.split('  ',1)
        path=R/rel
        check(path.is_file(),'Manifest missing '+rel)
        if path.is_file():check(hashlib.sha256(path.read_bytes()).hexdigest()==expected,'Checksum mismatch: '+rel)

print(json.dumps({'checks':checks,'passed':checks-len(errors),'failed':len(errors),'sample_errors':errors[:40],'preset_count':len(catalog)},indent=2))
if errors:sys.exit(1)
