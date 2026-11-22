# Lesson 05 — Experimental render and QA report

**Date:** 2026-11-19. **Reviewer:** inspecting schematic contact sheet; deterministic code/media checks.

## Produced actual files

| Demo | File | Media | Main contrast | Human verdict |
|---|---|---|---|---|
| Portal passage | `../EXPERIMENTS/portal_crossing_bad_vs_corrected.mp4` | 4.0s, 30fps, 960×540 | Offscreen slide against portal-contained emergence | Schematic concept visible; *not* a fully rigged or 3D portal crossing |
| Dinosaur footfall | `../EXPERIMENTS/stomp_reaction_bad_vs_corrected.mp4` | 4.0s, 30fps, 960×540, one original synthesized mono footfall | Premature response vs contact→gaze→body | Cause-order lesson visible; acting still rudimentary |
| Falling egg catch | `../EXPERIMENTS/egg_catch_bad_vs_corrected.mp4` | 4.0s, 30fps, 960×540 | Egg teleport vs continuous trajectory and hand contact | Object-continuity lesson visible; geometry needs a production-grade grasp/IK pass |

**Visual comparison:** `../EXPERIMENTS/lesson05_bad_good_contact_sheet.jpg` presents F030 and F088 from each clip. The images are schematics; they do not aim to meet the project's paper-cut character-art standards.

## Actual automated measurements / logged intent

- Each exported video: 120 encoded frames at 30fps, 960 × 540. See `render_metrics.json` and `python 08_TOOLS/audit_lesson05.py`.
- Stomp 'wrong' actor response is scripted from F028, before physical contact at F060. In the corrected half, sound begins at F060, eye/head gaze at F063 and body response at F072. **These event orders are deliberately chosen**, not independently detected from the rendered pixels.
- Correct egg path from F072 to F073 has continuous Euclidean displacement below 12 pixels (test script computes exact value); flawed variant jumps more than 200 pixels at F061.
- Corrected portal demonstrates a person visible inside its aperture first and afterward fully outside. The mask intersects a simple 2D plane. It does **not** prove true physical depth geometry or perfect footfall mechanics.
- `node 08_TOOLS/test_lesson05.mjs` checks normalized curves for all 42 recipes; it does **not** prove pose readability, sound quality or collision accuracy.

## Self-critique and defects that remain

| ID | Severity | Defect / limitation | Required next proof |
|---|---|---|---|
| L05-D01 | Critical for production / accepted in teaching demo | Portal character uses a 2D ellipse/rectangle matte union; no general layered scene z-depth or anatomical weight transfer | Real 270-frame benchmark with inside, crossing, outside frames and foot locks |
| L05-D02 | Major | Stickman geometry is rudimentary; foot and knee shapes are not a full articulated IK rig | Per-frame pose and stance-foot drift audit in production rig |
| L05-D03 | Major | Egg hand contact is symbolic and lacks robust finger gripping/prop ownership controller | Unified object attachment coordinates, explicit contact/release constraints and visual QA |
| L05-D04 | Major | Synthetic stomp is a single tone/noise burst, not a professionally designed dinosaur Foley mix | Material-layered Foley stem test, phone/mono listening, measured onset |
| L05-D05 | Moderate | Uniform per-category default timing is pedagogical; pacing isn't customized by shot tension/style | Blind silent-viewer narrative comprehension test after custom beat timing |
| L05-D06 | Major | None of the 42 action recipes have been individually production-rendered or AE-runtime tested | Selected scene implementation and before/after director review |

## Decisions

- `TESTED_CODE` is not `VISUALLY_VERIFIED`.
- The three rendered clips are educational comparator tests. They do not advance the locked DINO production phase.
- Preserve F000–F269 / 9s portal benchmark and full film gate unchanged.

## Reproduction

```bash
python 08_TOOLS/render_lesson05_demos.py
node 08_TOOLS/test_lesson05.mjs
python 08_TOOLS/audit_lesson05.py
ffprobe -v error -show_streams 12_ACTION_INTELLIGENCE/EXPERIMENTS/stomp_reaction_bad_vs_corrected.mp4
```

The encoder and script rerun generate media, but the subjective evaluation must be repeated with the actual results.
