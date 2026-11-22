#!/usr/bin/env python3
"""Structural quality gate for living knowledge (not research truth or AE runtime test)."""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
K=ROOT/'10_KNOWLEDGE'
errors=[]; passes=[]
def check(ok,msg):
    (passes if ok else errors).append(msg)
required=['README.md','INDEX.md','PRINCIPLE_REGISTER.md','LEARNING_LOG.md','SEARCH_GUIDE.md',
          'TAXONOMY.md','ALIASES.json','RESEARCH_BACKLOG.md']
for f in required:check((K/f).is_file(),'required knowledge: '+f)
lessons=sorted((K/'LESSONS').glob('LRN-*.md'))
check(len(lessons)>=9,'minimum nine lesson cards')
ids=set(); pattern=re.compile(r'^([a-z_]+):\s*(.*)$',re.M)
for f in lessons:
    body=f.read_text(encoding='utf8'); head=body.split('---',2)[1] if body.startswith('---') else ''
    m=dict(pattern.findall(head))
    lid=m.get('id','')
    check(bool(re.fullmatch(r'LRN-\d{4}',lid)),f'valid lesson id: {f.name}')
    check(lid not in ids,f'unique lesson ID: {lid}'); ids.add(lid)
    for key in ('title','kind','status','tags','source_ids','related_ids','applies_to','updated'):
        check(bool(m.get(key)),f'{lid} has {key}')
    for name in ('Claim and scope','Where not to overapply','Observable acceptance test'):
        check(name in body,f'{lid} has {name}')
case=K/'CASE_STUDIES/CASE-0001_original_dino_portal_not_crossed.md'
check(case.exists(),'historical case exists')
log=(K/'LEARNING_LOG.md').read_text()
for n in range(1,5):check(f'LOG-{n:04d}' in log,'learning log LOG-'+str(n))
idx=(K/'INDEX.md').read_text()
for lid in ids:check(lid in idx,f'index references {lid}')
source=(ROOT/'01_RESEARCH/00_SOURCE_LEDGER.md').read_text()
for n in range(26,45):check(f'| S{n} |' in source,f'S{n} exists in source ledger')
for path in ['00_START_HERE/06_EVOLVING_GOALS_AND_DIRECTIONS.md','00_START_HERE/07_CONFLICT_AND_INTERPRETATION_LOG.md',
             '03_PROMPT_MODULES/13_NATURAL_LANGUAGE_TO_ANIMATION_TRANSLATOR.md',
             '03_PROMPT_MODULES/14_AFTER_EFFECTS_TECHNICAL_DIRECTOR.md',
             '10_KNOWLEDGE/EXAMPLES/INT-0001_CINEMATIC_IMPACT_TRANSLATION.md',
             '11_AFTER_EFFECTS/04_EXPRESSION_COOKBOOK.md','08_TOOLS/search_knowledge.py']:
    check((ROOT/path).exists(),f'key extension: {path}')
book=(ROOT/'11_AFTER_EFFECTS/04_EXPRESSION_COOKBOOK.md').read_text()
for n in range(1,12):check(bool(re.search(rf'E{n:02d}\b',book)),f'code example E{n:02d}')
check('not been executed' in book.lower() or 'not executed' in book.lower(),'expression status honest')
check('not done' in (ROOT/'09_HANDOFF/STATUS.md').read_text().lower(),'no false render completion')
print(f'KNOWLEDGE AUDIT: {len(passes)} passed, {len(errors)} failed.')
for e in errors:print('FAIL:',e)
print('LIMITATION: validates documentation structure, not external citations or AE runtime.')
sys.exit(1 if errors else 0)
