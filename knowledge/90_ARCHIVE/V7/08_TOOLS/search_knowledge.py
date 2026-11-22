#!/usr/bin/env python3
"""Simple local deterministic full-text Markdown search (no external dependencies).

Examples:
  python 08_TOOLS/search_knowledge.py "make bullet impact read" --expand --top 8
  python 08_TOOLS/search_knowledge.py --id LRN-0009
  python 08_TOOLS/search_knowledge.py "wiggle" --tag expressions --json
"""
from pathlib import Path
from collections import Counter
import argparse, json, re, sys
ROOT=Path(__file__).resolve().parents[1]
PARSER=argparse.ArgumentParser()
PARSER.add_argument('query', nargs='?',default='')
PARSER.add_argument('--expand',action='store_true')
PARSER.add_argument('--top',type=int,default=10)
PARSER.add_argument('--kind')
PARSER.add_argument('--tag')
PARSER.add_argument('--id')
PARSER.add_argument('--related')
PARSER.add_argument('--scope')
PARSER.add_argument('--list-tags',action='store_true')
PARSER.add_argument('--list-docs',action='store_true')
PARSER.add_argument('--json',action='store_true')
args=PARSER.parse_args()

def metadata(s):
    m={}
    if s.startswith('---\n'):
        end=s.find('\n---',4)
        if end>0:
            for line in s[4:end].splitlines():
                if ':' in line:
                    k,v=line.split(':',1);m[k.strip()]=v.strip()
    return m

def tokens(s):return set(re.findall(r'[a-z0-9]+',s.lower()))

alias=json.loads((ROOT/'10_KNOWLEDGE/ALIASES.json').read_text(encoding='utf8'))
q=args.query.lower().strip()
q_alias=[]
if args.expand and q:
    for key,words in alias.items():
        if key in q or key in tokens(q) or any(w in q for w in words):
            q_alias.extend([key]+words)
query_terms=tokens(q)
alt_terms=tokens(' '.join(q_alias))-query_terms
prefixes=('10_KNOWLEDGE','11_AFTER_EFFECTS','01_RESEARCH','00_START_HERE','02_STORY','03_PROMPT_MODULES','04_PRODUCTION','05_QA','09_HANDOFF','12_ACTION_INTELLIGENCE','13_ANIMATION_INTELLIGENCE','14_STORY_STRUCTURE','15_MISSING_AND_UNVERIFIED_SOURCES')
files=[]
for prefix in prefixes:
    d=ROOT/prefix
    if d.is_dir():files+=sorted(d.rglob('*.md'))
files += [ROOT/'README.md',ROOT/'AGENTS.md']
results=[];counts=Counter()
for p in files:
    rel=p.relative_to(ROOT).as_posix()
    if args.scope and not rel.startswith(args.scope):continue
    body=p.read_text(encoding='utf8')
    m=metadata(body)
    tags=[x.strip() for x in m.get('tags','').split(',') if x.strip()]
    counts.update(tags)
    if args.tag and args.tag.lower() not in [x.lower() for x in tags]:continue
    if args.kind and m.get('kind','')!=args.kind:continue
    if args.id and m.get('id','').lower()!=args.id.lower():continue
    if args.related and args.related.lower() not in m.get('related_ids','').lower() and args.related.lower() not in body.lower():continue
    low=body.lower()
    base=5 if q and q in low else 0
    score=base+sum(min(low.count(term),8) for term in query_terms if len(term)>1)*2
    score+=sum(min(low.count(term),5) for term in alt_terms if len(term)>2)*.25
    if q and q in rel.lower():score+=12
    if args.id:score+=100
    if args.list_docs:score=max(score,1)
    if score<=0 and not(args.list_docs or args.related or args.id or args.list_tags):continue
    lines=body.splitlines()
    best=[]
    for i,line in enumerate(lines,1):
        ll=line.lower()
        matches=sum(1 for term in query_terms if term in ll)+(.25*sum(1 for term in alt_terms if term in ll))
        if q in ll and q:matches+=3
        if matches>0:best.append((matches,i,line[:180]))
    best.sort(reverse=True)
    results.append({'path':rel,'id':m.get('id',''),'kind':m.get('kind',''),'status':m.get('status',''),
                    'tags':tags,'score':round(score,2),'snippets':[{'line':i,'text':line} for _,i,line in best[:3]]})
results.sort(key=lambda x:(-x['score'],x['path']))
if args.list_tags:
    print(json.dumps({'tags':dict(sorted(counts.items()))},indent=2) if args.json else '\n'.join(f'{t}: {n}' for t,n in sorted(counts.items())))
    sys.exit(0)
if args.json:
    print(json.dumps({'query':q,'results':results[:max(1,args.top)],'total_hits':len(results),'expanded_aliases':q_alias},indent=2,ensure_ascii=False))
else:
    for r in results[:max(1,args.top)]:
        print(f"{r['score']:5}  {r['path']}  {r['id']} [{r['kind'] or 'document'}; {r['status'] or 'no-status'}]")
        for sn in r['snippets']:print(f"    L{sn['line']}: {sn['text']}")
    print(f"Results: {len(results)} (displayed {min(max(1,args.top),len(results))}); local lexical search, not semantic understanding")
