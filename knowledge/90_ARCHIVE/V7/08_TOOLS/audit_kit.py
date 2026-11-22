#!/usr/bin/env python3
"""Deterministic *documentation* audit; not a video-quality test.
Usage: python 08_TOOLS/audit_kit.py [--json]
"""
import argparse, json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
 'README.md','AGENTS.md','00_START_HERE/01_NEW_CHAT_STARTER.md',
 '00_START_HERE/02_PROJECT_CONSTITUTION.md','00_START_HERE/03_STATE_MACHINE.md',
 '00_START_HERE/04_TRUTH_AND_RECOVERY.md',
 '01_RESEARCH/00_SOURCE_LEDGER.md','01_RESEARCH/01_VISUAL_CAMERA_DIRECTION.md',
 '01_RESEARCH/02_SOUND_MUSIC_PERSPECTIVE.md','01_RESEARCH/03_MOTION_ACTING_AND_PHYSICS.md',
 '01_RESEARCH/05_CONTEXT_COUPLING.md','01_RESEARCH/06_WRITING_AND_ADAPTATION.md',
 '02_STORY/01_FILM_TREATMENT.md','02_STORY/02_SCRIPT_AND_TIMELINE.md',
 '02_STORY/03_WORLD_ACTOR_PROP_STATE.md','02_STORY/04_ART_CHARACTER_SOUND_BIBLE.md',
 '03_PROMPT_MODULES/00_ORCHESTRATOR.md','03_PROMPT_MODULES/12_DELIVERY_AND_HANDOFF.md',
 '04_PRODUCTION/01_PHASE_BY_PHASE.md','04_PRODUCTION/02_BENCHMARK_270_FRAMES.md',
 '04_PRODUCTION/03_SHOT_CARDS_01_TO_08.md','04_PRODUCTION/04_SOUND_SPOTTING.md',
 '05_QA/01_FIVE_GATE_QA.md','05_QA/02_SCENE_ACTION_TESTS.md',
 '05_QA/03_ADVERSARIAL_PLAYBOOK.md','05_QA/04_DOCUMENT_KIT_AUDIT.md',
 '06_TEMPLATES/SHOT_CARD_TEMPLATE.md','06_TEMPLATES/SOUND_CUE_TEMPLATE.csv',
 '09_HANDOFF/STATUS.md','09_HANDOFF/RECOVERY_CARD.md',
 '08_TOOLS/audit_kit.py',
]
fail=[]; warn=[]; passed=[]
def check(ok, name, details=''):
    (passed if ok else fail).append(f'{name}{": "+details if details else ""}')
for p in REQUIRED:
    f=ROOT/p
    check(f.is_file(), 'required-file', p)
    if f.is_file() and f.suffix in ('.md','.py'):
        check(len(f.read_text(encoding='utf8').strip())>50, 'nonempty', p)
# Check every relative Markdown link with file targets, incl optional #heading.
for md in ROOT.rglob('*.md'):
    body=md.read_text(encoding='utf8')
    for target in re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)',body):
        target=target.split('#',1)[0].strip().strip('<>')
        if not target or target.startswith(('http://','https://','mailto:','data:','sandbox:')):
            continue
        path=(md.parent/target).resolve()
        try: path.relative_to(ROOT)
        except ValueError:
            fail.append(f'link-escapes-root: {md.relative_to(ROOT)} -> {target}'); continue
        if not path.exists(): fail.append(f'broken-relative-link: {md.relative_to(ROOT)} -> {target}')
# Count modules, all expected (00..12)
modules={p.name[:2] for p in (ROOT/'03_PROMPT_MODULES').glob('*.md') if re.match(r'^\d\d_',p.name)}
check(modules=={f'{i:02d}' for i in range(15)}, 'module-coverage',str(sorted(modules)))
shots=(ROOT/'04_PRODUCTION/03_SHOT_CARDS_01_TO_08.md').read_text()
missing=[f'A{i:02d}' for i in range(1,25) if not re.search(r'\bA%02d\b'%i,shots)]
check(not missing,'shot-coverage',str(missing))
# timeline row read and continuity / duration
script=(ROOT/'02_STORY/02_SCRIPT_AND_TIMELINE.md').read_text()
pattern=re.compile(r'^\|\s*(S\d\d)\s*\|\s*([\d.]+)[–-]([\d.]+)\s*\|\s*(\d+)[–-](\d+)\s*\|',re.M)
entries=[(a,float(b),float(c),int(d),int(e)) for a,b,c,d,e in pattern.findall(script)]
check(len(entries)==8,'scene-count',str(len(entries)))
if len(entries)==8:
    durations=all(abs((end-start)*30-(fend-fstart))<.001 for _,start,end,fstart,fend in entries)
    contiguous=all(entries[i][4]==entries[i+1][3] and abs(entries[i][2]-entries[i+1][1])<.001 for i in range(7))
    check(durations,'scene-time-to-frame-mapping')
    check(contiguous,'no-timeline-gaps')
    check(entries[0][3]==0 and entries[-1][4]==2400 and entries[-1][2]==80,'total-runtime-2400-frames')
# Benchmark and honest status
bench=(ROOT/'04_PRODUCTION/02_BENCHMARK_270_FRAMES.md').read_text()
check('270' in bench and 'portal' in bench.lower() and 'occlu' in bench.lower(),'benchmark-coverage')
ledger=(ROOT/'01_RESEARCH/00_SOURCE_LEDGER.md').read_text()
check(ledger.count('https://')>=12,'source-ledger-url-count',str(ledger.count('https://')))
context=(ROOT/'01_RESEARCH/05_CONTEXT_COUPLING.md').read_text()
for field in ['CAM','SND','TEST','contact','perspective','audience']:
    check(field.lower() in context.lower(),'context-coupling',field)
status=(ROOT/'09_HANDOFF/STATUS.md').read_text().lower()
check(('not verified' in status or 'not done' in status) and 'benchmark' in status,'honest-current-status')
# Check all files can be UTF-8 decoded; check duplicate relative names impossible by filesystem
for path in ROOT.rglob('*.md'):
    if path.stat().st_size < 100: warn.append(f'short document: {path.relative_to(ROOT)}')
result={'root':str(ROOT),'pass_count':len(passed),'failure_count':len(fail),'warning_count':len(warn),'failures':fail,'warnings':warn}
args=argparse.ArgumentParser(); args.add_argument('--json',action='store_true'); opts=args.parse_args()
if opts.json: print(json.dumps(result,indent=2))
else:
    print(f'DOCUMENTATION AUDIT: {len(passed)} checks passed, {len(fail)} failed, {len(warn)} warnings')
    for f in fail: print('FAIL:',f)
    for w in warn: print('WARN:',w)
    print('LIMITATION: Does not inspect rendered animation, original audio or external URLs.')
sys.exit(1 if fail else 0)
