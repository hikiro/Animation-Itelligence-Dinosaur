#!/usr/bin/env python3
"""V7 evidence/source organization checks; does not validate creator claims or animation quality."""
from pathlib import Path
import csv,json,hashlib,sys,re
r=Path(__file__).resolve().parents[1];errors=[];checks=0

def test(ok,desc):
 global checks
 checks+=1
 if not ok:errors.append(desc)
image=r/'14_STORY_STRUCTURE/REFERENCES/REF-STORY-0001_shortform_stacked_beats_user_upload.png'
test(image.is_file() and image.stat().st_size>1000,'uploaded screenshot exists')
card=(r/'14_STORY_STRUCTURE/REF-STORY-0001.md').read_text(encoding='utf8')
for label in ('Hook','Lead','Body 1','Open loop','Body 2','Body 3','CTA'):
 test(label in card,'reference contains '+label)
test('NOT_PROVIDED' in (r/'15_MISSING_AND_UNVERIFIED_SOURCES/README.md').read_text(),'distinguish gaps')
test("'14_STORY_STRUCTURE'" in (r/'08_TOOLS/search_knowledge.py').read_text(),'general search indexes story library')
test("'13_ANIMATION_INTELLIGENCE'" in (r/'08_TOOLS/search_knowledge.py').read_text(),'general search indexes AI-01 library')
with (r/'15_MISSING_AND_UNVERIFIED_SOURCES/REGISTER.csv').open(encoding='utf8',newline='') as f: rd=csv.DictReader(f);cols=rd.fieldnames;records=list(rd)
s=json.loads((r/'15_MISSING_AND_UNVERIFIED_SOURCES/SCHEMA.json').read_text())
test(cols==s['required_columns'],'exact register schema')
test(len(records)>=8,'minimum gap coverage')
ids=set()
for x in records:
 test(bool(re.fullmatch(r'GAP-\d{3}',x['id'])),'valid GAP ID '+x['id'])
 test(x['id'] not in ids,'unique '+x['id']);ids.add(x['id'])
 test(x['status'] in s['allowed_statuses'],'valid status '+x['id'])
 test(x['priority'] in s['priority_order'],'priority '+x['id'])
 for field in ('requested_material','reason','known_evidence_path','access_attempt','user_can_provide','related_id'):
  test(bool(x[field].strip()),x['id']+' '+field)
 test((r/x['known_evidence_path']).is_file(),x['id']+' grounded evidence path')
for name in ('README.md','AGENTS.md','00_START_HERE/06_EVOLVING_GOALS_AND_DIRECTIONS.md','09_HANDOFF/STATUS.md','10_KNOWLEDGE/INDEX.md','10_KNOWLEDGE/LEARNING_LOG.md'):
 data=(r/name).read_text(encoding='utf8')
 test('REF-STORY-0001' in data,name+' references source')
for f in ('14_STORY_STRUCTURE/CONTEXT_ADAPTATION_AND_TESTS.md','14_STORY_STRUCTURE/STORY_STRUCTURE_RECORD_SCHEMA.json','15_MISSING_AND_UNVERIFIED_SOURCES/INTAKE_AND_ACCESS_LOG.md','15_MISSING_AND_UNVERIFIED_SOURCES/MANUAL_SUBMISSION_TEMPLATE.md','08_TOOLS/search_materials.py'):
 test((r/f).is_file(),f+' exists')
print(f'V7 organizational audit: {checks-len(errors)}/{checks} checks passed; {len(errors)} failures')
for x in errors:print('FAIL',x)
sys.exit(bool(errors))
