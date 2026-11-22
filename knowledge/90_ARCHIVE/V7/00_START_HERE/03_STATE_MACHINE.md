# State machine: plan → animate → inspect → repair → approve

## Phases (never claim a later phase was completed without evidence)

`P0_BRIEF_AND_PREPRODUCTION → P1_BENCHMARK_BLOCKING → P2_BENCHMARK_FINALING → P3_FULL_FILM_ANIMATIC → P4_SHOT_ANIMATION → P5_POST_AUDIO_AND_EDIT → P6_FINAL_QA_AND_DELIVERY`.

A phase may contain multiple iterations. Enter the next phase only when the prior exit criteria are verified. The whole project loops at shot level and at film level.

## Canonical work loop — use for every shot

```text
INPUT: approved story beat + actor state + camera/audio context + prior QA report
1. READ previous accepted state and files.
2. SPECIFY one shot's stimulus, perception, intention, action, contact, consequence,
   recovery, blocking, camera purpose, sonic perspective, and measurable tests.
3. PRE-FLIGHT: validate geography, asset identity, object ownership, time budget,
   tool availability, and input provenance.
4. BLOCK primary poses and exact contact/event frames.
5. RENDER low-fidelity scene + consecutive evidence frames.
6. INSPECT at real playback speed, frame-step, muted, SFX-only, then full mix.
7. LOG differences between intended and observed actions.
8. PRIORITIZE: BLOCKER > MAJOR > MINOR. Fix the root cause, not cosmetic symptom.
9. RE-RENDER affected span; run local AND upstream/downstream regression checks.
10. IF blockers/majors remain: iterate. ELSE freeze accepted version + evidence.
11. UPDATE status, shot card, cue sheet, defect log, asset manifest, and next action.
OUTPUT: verified deliverable OR explicit BLOCKED/PARTIAL state.
```

## Independent gates

| Gate | Exit evidence | Common reject |
|---|---|---|
| P0 | Annotated beat sheet, state diagram, geography, design bible, shot list, audio spotting, risk register | Missing story cause or no portal depth plan |
| P1 | 270 grayscale frames + playable rough 9s clip, visible portal crossing, planted foot state logs | Screen-edge actor entrance or body drawn atop portal |
| P2 | Polished 9s MP4 + editable project + layered rigs + stems + review contact/adjacent frames + QC log | Sliding foot, wrong occlusion, generic sounds unsynced |
| P3 | 2400-frame planning animatic (or re-timed explicit plan), full silent-readability review | Mother/baby intention absent, hidden decisive actions |
| P4 | Approved per-shot renders with valid contacts, screen direction and prop states | Broken handoffs, missing collisions, rig inconsistency |
| P5 | Picture lock, event-aligned Foley, spatial mix, distinct stems, headset/phone/mono review | SFX masking key action, abrupt ambience, loudness guess |
| P6 | Render probes, audio meters, QA signed, output links and exact commands | Cannot verify existence, unsupported “passes” claims |

## Stop-and-escalate conditions

If the same blocker survives **two repair attempts**, stop cosmetic changes. Create a three-hypothesis root-cause analysis (rig, coordinate/camera, rendering/occlusion), test a simplified debug render, and choose a structural repair. If a story beat fails multiple silent viewings, return to the storyboard, not compositing.

## Priorities

`Causal/story coherence > action completion > spatial/physical logic > performance > camera/edit clarity > sound intelligibility > polish`. Audio and camera still developed early in blocking; priority means they cannot excuse a failed causal event.

## File updates at every checkpoint

`09_HANDOFF/STATUS.md` = last verified phase and next action.
`09_HANDOFF/DECISION_LOG.md` = why choices changed.
`09_HANDOFF/ASSET_MANIFEST.md` = asset evidence/license and paths.
`05_QA/DEFECT_LOG_TEMPLATE.csv` or live copy = observed failures and closure.

Never fill a status with invented paths or mark TODO outputs as COMPLETE.
