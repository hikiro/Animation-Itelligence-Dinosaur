#!/usr/bin/env python3
"""Mechanical/semantic-schema audit only, NOT independent motion or viewer validation."""
import argparse,json,sys,collections,hashlib,random
from pathlib import Path

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',default=None);ap.add_argument('--json',action='store_true');a=ap.parse_args()
 R=Path(a.root).resolve() if a.root else Path(__file__).resolve().parent.parent
 B=R/'13_ANIMATION_INTELLIGENCE'/'AI-01_ACTION_SEMANTICS'/'02_CORPUS'
 files={'lexicon':'LEXICON.jsonl','context':'CONTEXTUAL_LEXICON.jsonl','action':'ACTION_CONTEXT_CASES.jsonl','ambiguity':'AMBIGUITY_TESTS.jsonl','source':'INSPECTED_SOURCE_OBSERVATIONS.jsonl','eval':'DIRECTOR_EVAL_CASES.jsonl'}
 E=[];check=0
 def assert_(ok,msg):
  nonlocal check;check+=1
  if not ok:E.append(msg)
 rows={}
 for k,v in files.items():
  p=B/v
  assert_(p.is_file(),f'Missing {p}')
  rows[k]=[]
  if p.is_file():
   for n,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
    try:r=json.loads(line);rows[k].append(r)
    except Exception as ex:E.append(f'{k}:{n}:invalid JSON: {ex}')
 assert_(all(len(v)>0 for v in rows.values()),'Empty corpus file')
 mani=json.loads((B/'DATASET_MANIFEST.json').read_text())
 for k,field in [('lexicon','lexicon_entries'),('context','lexical_context_rows'),('action','action_scenarios'),('ambiguity','ambiguity_readings'),('source','source_observations'),('eval','evaluation_prompts')]:
  assert_(len(rows[k])==mani[field],f'Count mismatch {k} {len(rows[k])} vs {mani[field]}')
 assert_(sum(map(len,rows.values()))==mani['total_records'],'Total mismatch')
 ids=[]
 for k,xx in rows.items():
  for x in xx:
   assert_('id' in x,f'{k} no id')
   ids.append(x.get('id'))
 assert_(len(ids)==len(set(ids)),'Nonunique record IDs')
 lexids=set(x['id'] for x in rows['lexicon'])
 sourcecatalog=json.loads((B/'SOURCE_CATALOG.json').read_text())
 sourceids=set(x['id'] for x in sourcecatalog)
 group=collections.defaultdict(list)
 for x in rows['context']:
  assert_(x.get('lexeme_id') in lexids,f'context {x.get("id")} missing lexeme')
  assert_(x.get('origin')=='synthetic_template_expansion_NOT_A_REAL_SCRIPT',f'false provenance context {x.get("id")}')
  assert_(x.get('evidence_level')=='L2_GENERATED_NOT_VALIDATED',f'false L2 context {x.get("id")}')
  assert_(x.get('source_ids')==[],f'Synthetic context illegitimately cites source {x.get("id")}')
  group[x['lexeme_id']].append(x['context'])
 for k,v in group.items():assert_(sorted(v)==sorted(['threat','comedy','wonder','tenderness']),f'4 contexts absent/duplicate for {k}')
 actiongroups=collections.defaultdict(list)
 for x in rows['action']:
  for f in ('observable_action','action_completion_test','stimulus','character_belief','camera_direction','audio_direction','prior_state','actor_goal'):
   assert_(isinstance(x.get(f),str) and len(x[f])>8,f'Action field empty {x["id"]}.{f}')
  assert_(x['production_verified'] is False,f'action fake verified {x["id"]}')
  assert_(x['evidence_level']=='L2_DESIGN_NOT_RENDER_VERIFIED',f'action wrong evidence {x["id"]}')
  actiongroups[x['base_action']].append(x)
 for k,v in actiongroups.items():
  assert_(len(v)==4 and {x['scene_context'] for x in v}=={'threat','comedy','wonder','tenderness'},f'action variants {k}')
  assert_(len({x['split'] for x in v})==1,f'action split leakage {k}')
  assert_(len({x['camera_direction'] for x in v})==4,f'context camera not different {k}')
  assert_(len({x['audio_direction'] for x in v})==4,f'context sound not different {k}')
 for x in rows['source']:
  assert_(x['source_id'] in sourceids,f'unknown source {x["source_id"]}')
  assert_(x['source_url'].startswith('https://'),f'bad URL {x["id"]}')
  assert_(x['evidence_level'].startswith('L1'),f'source status not L1 {x["id"]}')
 for x in rows['ambiguity']:
  assert_(x['anti_assumption'],f'ambiguity without stop condition {x["id"]}')
 amb=collections.Counter(x['token'] for x in rows['ambiguity'])
 for k,n in amb.items():assert_(n>=3,f'word not adequately ambiguous {k}')
 splits=collections.defaultdict(set)
 for x in rows['lexicon']+rows['context']:splits[x['lemma']].add(x['split'])
 for k,sp in splits.items():assert_(len(sp)==1,f'lexeme split leakage {k}')
 assert_(len(rows['lexicon'])>=500,'Lexicon too small')
 assert_(len(rows['action'])>=100,'Actions too few')
 assert_(len(rows['source'])>=10,'Inspected sources too few')
 assert_(len(rows['ambiguity'])>=100,'Ambiguity tests too few')
 assert_(len(rows['eval'])>=30,'Not enough held-out evaluation prompts')
 assert_(any(x['scene_context']=='suspense' for x in rows['eval']),'No out-of-profile context holdout')
 for x in rows['eval']:
  assert_(x['status']=='UNSCORED_MANUALLY_AUTHORED_TEST_CASE',f'Fake evaluator success {x["id"]}')
  assert_(x.get('requires_blind_human_rating') is True,f'Missing human test warning {x["id"]}')
 # sanity of supervised-style record claims
 assert_(all('NOT' in x['origin'] or x['origin']=='designed_contextual_example' for x in rows['context']+rows['action']),'origin claim looks misleading')
 report={'checks':check,'failures':len(E),'errors':E[:100], 'counts':{k:len(v) for k,v in rows.items()},'source_observations_vs_synthetic':{'source':len(rows['source']),'synthetic_or_authored':mani['total_records']-len(rows['source'])},'IMPORTANT':'A passing audit validates record structure and certain schema relations, NOT story correctness or animated performance.'}
 print(json.dumps(report,indent=2) if a.json else f'AI-01 structural audit: {check} checks, {len(E)} failures. Counts: '+str(report['counts'])+'\n'+ ('\n'.join(E[:20]) if E else report['IMPORTANT']))
 sys.exit(1 if E else 0)
if __name__=='__main__':main()
