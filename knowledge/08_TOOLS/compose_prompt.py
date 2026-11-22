#!/usr/bin/env python3
"""Build a director planning brief from selected preset IDs. NOT an automatic animation generator."""
import argparse,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def excerpt(md,label):
    m=re.search(r'^## '+re.escape(label)+r'.*?\n(.*?)(?=^## |\Z)',md,flags=re.M|re.S)
    return m.group(1).strip() if m else 'NOT SUPPLIED — inspect preset.'

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('ids',nargs='+');ap.add_argument('--context',default='unresolved; specify dramatic intention')
    ap.add_argument('--creature',default='not yet specified');ap.add_argument('--scale',default='not yet specified')
    ap.add_argument('--story',default='not yet specified');ap.add_argument('--out')
    a=ap.parse_args()
    catalog=json.loads((ROOT/'03_PRESET_LIBRARY/PRESET_CATALOG.json').read_text(encoding='utf8'))
    match={x['id']:x for x in catalog}
    unresolved=[x for x in a.ids if x not in match]
    if unresolved: ap.error('Unknown IDs: '+', '.join(unresolved))
    out=[f'# Production-planning prompt (generated, NOT validated)\n\nStory: {a.story}\nContext: {a.context}\nCreature: {a.creature}\nScale: {a.scale}\n',
         '## Safety and evidence requirements\nAll presets are L2 designs until rendered/inspected. Resolve contact, prop ownership, world geography and narrative conflicts before code. Do not claim approval on prompt assembly.\n']
    for id in a.ids:
        rec=match[id]; md=(ROOT/rec['path']).read_text(encoding='utf8')
        out.append(f"## {id} — {rec['title']}\n")
        for key in ['Human-language instruction and viewer goal','Causal event graph — editable','Rig, mechanics and interaction plan','Camera and editorial direction','Audio and music direction','Failure patterns and safety checks','Acceptance tests (NOT YET RUN FOR THIS PRESET)']:
            out.append(f'### {key}\n{excerpt(md,key)}\n')
    out.append('## Mandatory next step\nCreate event graph/world-space state and a shot animatic, then render and test actual output; update logs and record unresolved conflicts.\n')
    txt='\n'.join(out)
    if a.out: Path(a.out).write_text(txt,encoding='utf8'); print('Wrote',a.out)
    else: print(txt)
