#!/usr/bin/env python3
"""AI-01 deliberate lightweight corpus search. No ML, embeddings or claim of semantic understanding."""
import argparse,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
B=ROOT/'13_ANIMATION_INTELLIGENCE'/'AI-01_ACTION_SEMANTICS'/'02_CORPUS'
F={'lexicon':'LEXICON.jsonl','context':'CONTEXTUAL_LEXICON.jsonl','action':'ACTION_CONTEXT_CASES.jsonl','ambiguity':'AMBIGUITY_TESTS.jsonl','source':'INSPECTED_SOURCE_OBSERVATIONS.jsonl','eval':'DIRECTOR_EVAL_CASES.jsonl'}

def rows(kind):
 for kind0,filename in F.items():
  if kind not in ('all',kind0):continue
  p=B/filename
  with p.open(encoding='utf-8') as f:
   for n,line in enumerate(f,1):
    x=json.loads(line);x['_type']=kind0;x['_file']=str(p.relative_to(ROOT));x['_line']=n
    yield x

def normalize(s):return re.sub(r'[^a-z0-9]+',' ',str(s).lower()).strip()
def rank(q,record):
 q=normalize(q); terms=q.split(); data={k:normalize(v if not isinstance(v,list) else ' '.join(map(str,v))) for k,v in record.items() if k not in ('_file','source_url','note','_type')}
 prim=' '.join(data.get(k,'') for k in ('lemma','base_action','token','display','observed_phenomenon','surface_instruction','meaning','valid_interpretation','director_request','intended_viewer_inference'))
 alltext=' '.join(data.values()); sc=0
 if q and q==data.get('lemma',''):sc+=90
 if q and q==data.get('base_action',''):sc+=90
 if q and q==data.get('token',''):sc+=90
 if q and q in prim:sc+=25
 if q and q in alltext:sc+=5
 for t in terms:
  if re.search(r'\b'+re.escape(t)+r'\b',prim):sc+=8
  if re.search(r'\b'+re.escape(t)+r'\b',alltext):sc+=2
 return sc

def main():
 ap=argparse.ArgumentParser(description='Search AI-01, source and synthetic data clearly labeled')
 ap.add_argument('--query','-q',default='');ap.add_argument('--kind',choices=['all']+list(F),default='all')
 ap.add_argument('--context',choices=['threat','comedy','wonder','tenderness'])
 ap.add_argument('--domain');ap.add_argument('--pos');ap.add_argument('--id');ap.add_argument('--top',type=int,default=10);ap.add_argument('--json',action='store_true')
 a=ap.parse_args()
 if not a.query and not a.id:ap.error('Supply --query or --id')
 selected=[]
 for r in rows(a.kind):
  if a.id and r['id']!=a.id:continue
  if a.context and r.get('context',r.get('scene_context'))!=a.context:continue
  if a.domain and r.get('domain',r.get('semantic_domain'))!=a.domain:continue
  if a.pos and r.get('pos',r.get('part_of_speech'))!=a.pos:continue
  s=rank(a.query,r) if a.query else 100
  if s>0:selected.append((s,r))
 selected.sort(key=lambda it:(-it[0],it[1]['id']))
 selected=selected[:max(1,min(a.top,100))]
 if a.json:
  print(json.dumps([{**x,'_rank':score} for score,x in selected],indent=2,ensure_ascii=False));return
 print(f'AI-01: {len(selected)} results shown, kind={a.kind}, context={a.context or "any"}; ranking is KEYWORD, not learned semantics.')
 for score,r in selected:
  important=r.get('lemma',r.get('base_action',r.get('token',r.get('observed_phenomenon',''))))
  ev=r.get('evidence_level',r.get('status','UNKNOWN'))
  print(f'\n{r["id"]} score={score} [{r["_type"]}] {important} | {ev} | {r["_file"]}:{r["_line"]}')
  for key in ('scene_context','context','meaning','surface_instruction','valid_interpretation','director_request','observed_phenomenon','observable_action','action_completion_test','source_url'):
   if key in r:print(' ',key+':',str(r[key])[:300])
 if not selected:print('No match; query another term, domain, or source. DO NOT INVENT a case.')
if __name__=='__main__':main()
