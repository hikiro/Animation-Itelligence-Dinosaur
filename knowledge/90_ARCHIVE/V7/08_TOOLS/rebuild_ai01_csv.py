#!/usr/bin/env python3
"""Regenerate convenience CSVs from canonical AI-01 JSONL files; no source text copied."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1]
B=R/'13_ANIMATION_INTELLIGENCE'/'AI-01_ACTION_SEMANTICS'/'02_CORPUS'
for basename in ['LEXICON','ACTION_CONTEXT_CASES']:
 p=B/(basename+'.jsonl')
 rows=[json.loads(s) for s in p.read_text(encoding='utf-8').splitlines()]
 keys=[]
 for r in rows:
  for k in r:
   if k not in keys:keys.append(k)
 with (B/(basename+'.csv')).open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=keys,extrasaction='ignore');w.writeheader()
  for r in rows:w.writerow({k:(json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v) for k,v in r.items()})
 print('Regenerated',basename+'.csv',len(rows),'rows')
