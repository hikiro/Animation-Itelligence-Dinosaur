#!/usr/bin/env python3
"""Check basic event ordering from a future scene's actual event log.

Schema: {"fps":30, "events":[{"id":"human_head_visible_inside","frame":55},...]}
This helps with mechanical order, but doesn't validate *visible* portal masking.
Use only with events derived from actual animation, not placeholder records.
"""
import argparse, json, sys
from pathlib import Path

ap=argparse.ArgumentParser()
ap.add_argument('event_log',help='Actual scene event JSON file')
a=ap.parse_args()
p=Path(a.event_log)
if not p.is_file(): sys.exit('BLOCKED: event log file missing')
x=json.loads(p.read_text(encoding='utf-8'))
events=x.get('events')
if not isinstance(events,list): sys.exit('FAIL: expected JSON top-level events list')
for e in events:
    if not isinstance(e,dict) or 'id' not in e or not isinstance(e.get('frame'),int):
        sys.exit('FAIL: event lacks ID or verified integer frame')
seen={e['id']:e['frame'] for e in events}
seq=['human_head_visible_inside','human_lead_crossing','human_lead_foot_contact','human_pelvis_crossing','human_trailing_foot_clear','human_full_exit']
missing=[k for k in seq if k not in seen]
if missing:
    sys.exit('UNVERIFIED: cannot evaluate event chain; missing '+', '.join(missing))
frames=[seen[k] for k in seq]
if frames!=sorted(frames) or len(set(frames))!=len(frames):
    sys.exit(f'FAIL: portal event order invalid: {dict(zip(seq,frames))}')
if frames[0]<0 or frames[-1]>=270:
    sys.exit('FAIL: portal exit sequence is outside benchmark 0–269')
print('PASS: declared portal event order is valid within 270 frames:',dict(zip(seq,frames)))
print('LIMITATION: Only event order in JSON was checked. Rendered occlusion, foot slip and actual action still require inspection.')
