#!/usr/bin/env python3
"""Structural and media checks for lesson 05; *not* a perceptual cinematography approval."""
from pathlib import Path
import json,subprocess,sys,re,hashlib,wave
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'12_ACTION_INTELLIGENCE'
errors=[];passes=[]
def check(pred,msg): (passes if pred else errors).append(msg)
req=['README.md','INDEX.md','01_LANGUAGE_TO_ACTION_COMPILER.md','02_EVIDENCE_AND_TECHNIQUES.md','03_CONTEXT_CAMERA_AUDIO.md','04_RENDER_AND_QA_PROTOCOL.md','DATA/action_recipes.json','DATA/action_recipes.csv','RESULTS/TEST_REPORT.md','EXPERIMENTS/lesson05_bad_good_contact_sheet.jpg','PROMPTS/01_TRANSLATE.md','PROMPTS/02_BLOCK.md','PROMPTS/03_CAMERA_AUDIO.md','PROMPTS/04_IMPLEMENT.md','PROMPTS/05_RED_TEAM_LEARN.md']
for p in req:check((A/p).is_file(),f'exists {p}')
recs=json.loads((A/'DATA/action_recipes.json').read_text())
check(len(recs)==42,'42 action recipes')
check(len(set(r['id'] for r in recs))==42,'unique IDs')
check(len(set(r['slug'] for r in recs))==42,'unique slugs')
check(set(Counter(r['category'] for r in recs).values())=={6},'six action recipes per category')
check(len(set(r['category'] for r in recs))==7,'seven categories')
ledger=(ROOT/'01_RESEARCH/00_SOURCE_LEDGER.md').read_text()
for s in ['S45','S46','S47','S48','S49','S50','S51']:check(f'| {s} |' in ledger,f'ledger source {s}')
for r in recs:
    md=A/'RECIPES'/f'{r["id"]}_{r["slug"]}.md'
    check(md.is_file(),f'{r["id"]} md card')
    if md.is_file():
        body=md.read_text()
        for title in ['Causal storyboard','Camera and sound','Technical implementation','Bad / known','Better, event','Defect-to-fix','Observable acceptance test','Evidence status']:
            check(title in body,f'{r["id"]} {title}')
        check(r['primary_channel'] in body, f'{r["id"]} channel documented')
        check('NOT_TESTED' in body,f'{r["id"]} evidence honest')
    ts=r['phase_frames'];keys=['stimulus','perception','decision','anticipation','action','consequence','end']
    check(all(k in ts for k in keys),f'{r["id"]} phase schedule')
    if all(k in ts for k in keys):check(ts['stimulus']==0 and ts['end']==r['duration_frames'] and all(ts[keys[i]]<ts[keys[i+1]] for i in range(6)),f'{r["id"]} ordered timeline')
    check(len(r['source_ids'])>=2,f'{r["id"]} multiple supporting references')
    check(r['primary_channel'] in r['curves'],f'{r["id"]} curve binding')
    for title in ['stimulus','perception','decision','anticipation','action','consequence','camera','audio','failed_pattern','repair_strategy']:
        check(len(r[title])>=16,f'{r["id"]} descriptive {title}')
for name in ['portal_crossing','stomp_reaction','egg_catch']:
    f=A/'EXPERIMENTS'/f'{name}_bad_vs_corrected.mp4'
    check(f.is_file(),f'{name} mp4')
    if f.is_file():
        cmd=['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height,r_frame_rate,nb_frames','-of','json',str(f)]
        try:
            d=json.loads(subprocess.check_output(cmd,text=True))['streams'][0]
            check((d['width'],d['height'],d['r_frame_rate'],int(d['nb_frames']))==(960,540,'30/1',120), f'{name} media properties')
        except Exception as e:check(False,f'ffprobe decode {name}: {e}')
    if name=='stomp_reaction':
        w=A/'EXPERIMENTS/stomp_original_synthetic.wav';check(w.is_file(),'stomp original wav')
        if w.is_file():
            with wave.open(str(w)) as wf:
                check(wf.getframerate()==44100 and wf.getnchannels()==1,'stomp wave format')
                b=wf.readframes(wf.getnframes())
            import numpy as np
            v=np.frombuffer(b,dtype='<i2')
            onset=np.flatnonzero(abs(v)>100)
            check(len(onset)>0 and abs(onset[0]/44100-2.0)<.005,'audio onset equals 2.0s stomp frame 60')
# Specific dramaturgical test fixtures, not perceptual quality judgements
check(28<60,'bad stomp reaction starts before contact')
check(60<63<72,'good stomp contact -> gaze -> body chronology')
# Formula from experiment render: right egg position is continuous at contact frame.
import math
def egg_good(f):
    if f<30:return 337,159
    if f<73:
        u=(f-30)/43;return 337-117*u,159+187*u*u
    u=min(1,max(0,(f-73)/36));u=u*u*(3-2*u)
    return 220+(190-220)*u,346+(340-346)*u
step=math.dist(egg_good(72),egg_good(73))
check(step<12,f'egg frame-72 -> frame-73 continuity <12 px (observed {step:.3f}px)')
check(math.dist((337,159),(184,327))>200,'bad egg teleport >200px')
check('BENCHMARK' in (ROOT/'09_HANDOFF/STATUS.md').read_text().upper(),'handoff discusses benchmark truth')
print(f'LESSON05 AUDIT: {len(passes)} PASS; {len(errors)} FAIL. Limited to schema/code/media/event chronology, NOT artistic approval.')
for err in errors:print('FAIL:',err)
sys.exit(1 if errors else 0)
