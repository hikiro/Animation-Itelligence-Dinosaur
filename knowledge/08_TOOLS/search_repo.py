#!/usr/bin/env python3
"""Build/search full-text index of V8 Markdown. Standard library only."""
import sqlite3, sys, re, argparse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'08_TOOLS/knowledge_search.sqlite'
ALIASES={'heavy':['mass','inertia','weight','stop','stomp'],'stomp':['impact','contact','giant'],'portal':['threshold','doorway','mask','occlusion'],'grab':['grasp','hand','attachment'],'rig':['skeleton','ik','fk','deformation'],'fear':['threat','recoil','panic'],'comedy':['comic','hold','surprise'],'wing':['bird','takeoff','flap'],'snake':['slither','limbless'],'sound':['audio','foley','perspective'],'learn':['learning','lesson','evidence']}

def build():
    if DB.exists(): DB.unlink()
    db=sqlite3.connect(DB)
    db.execute('CREATE VIRTUAL TABLE docs USING fts5(path UNINDEXED, title, body, tokenize="porter")')
    docs=[]
    for p in ROOT.rglob('*.md'):
        if '/90_ARCHIVE/' in p.as_posix(): continue # keep canonical first, V7 search remains via own search scripts
        relative=p.relative_to(ROOT).as_posix()
        txt=p.read_text(encoding='utf8',errors='replace')
        title=next((x.strip('# ').strip() for x in txt.splitlines() if x.startswith('#')),p.stem)
        docs.append((relative,title,txt))
    db.executemany('INSERT INTO docs(path,title,body) VALUES(?,?,?)',docs)
    db.commit(); db.close()
    return len(docs)

def search(query,limit=10):
    if not DB.exists(): build()
    tokens=re.findall(r'[\w-]+',query.lower())
    expanded=[]
    for t in tokens:
        expanded.extend([t]+ALIASES.get(t,[]))
    unique=list(dict.fromkeys(x for x in expanded if len(x)>1))
    if not unique: return []
    fts=' OR '.join('"'+x.replace('"','')+'"' for x in unique)
    db=sqlite3.connect(DB)
    try:
        rows=db.execute('SELECT path,title,snippet(docs,2,"[", "]", "…", 18),bm25(docs) score FROM docs WHERE docs MATCH ? ORDER BY score LIMIT ?', (fts,limit)).fetchall()
    except sqlite3.OperationalError as e:
        print('Search index error:',e,file=sys.stderr); rows=[]
    db.close(); return rows

if __name__=='__main__':
    pa=argparse.ArgumentParser(description=__doc__)
    pa.add_argument('query',nargs='?',default=''); pa.add_argument('--limit',type=int,default=10);pa.add_argument('--rebuild',action='store_true')
    a=pa.parse_args()
    if a.rebuild:
        print('Indexed',build(),'canonical Markdown files'); sys.exit(0)
    for i,(p,title,snip,score) in enumerate(search(a.query,a.limit),1):
        print(f'{i}. {title}\n   {p}\n   {snip[:220]}')
