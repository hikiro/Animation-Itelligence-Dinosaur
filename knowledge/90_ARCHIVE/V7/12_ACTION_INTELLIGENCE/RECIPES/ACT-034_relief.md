---
id: ACT-034
title: Make the relief after the chase feel earned
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: emotion, relief, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-034 — Make the relief after the chase feel earned

**Creative intention:** Make the viewer understand: the relief after the chase feel earned.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (108 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F013 | Mother nuzzles newborn instead of threatening |
| Perception | F014–F023 | Human verifies she is calm |
| Decision | F024–F033 | Release protective tension |
| Anticipation | F034–F045 | Chest holds breath then softens |
| Action | F046–F077 | Shoulders lower, grip relaxes, knees unlock |
| Consequence | F078–F107 | Human smiles and regains normal posture |

## Character and asset engineering

- **Primary rig/controllers:** eyes/shoulders/arms/hips.
- **Recommended system:** gaze, intention, pose contrasts, breath and whole-body reactions.
- **Named channel:** `shoulderDropPx`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Move to less compressed medium framing only after recognition
- **Sound objective:** Music opens after safe nuzzle; exhale prominent
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const shoulderDropPx = frame < 46 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-034", frame, recipes);
const shoulderDropPx = pose.channels.shoulderDropPx;
const phase = pose.phase;
// Connect shoulderDropPx to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Instant smile at first appearance of baby despite danger.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Make mother-behavior verification precede relaxation.

## Observable acceptance test

- Stimulus visible or intentionally audible: Mother nuzzles newborn instead of threatening
- Perception and decision visibly motivate action: Human verifies she is calm; Release protective tension
- Main event actually completed: Shoulders lower, grip relaxes, knees unlock
- Aftermath visible: Human smiles and regains normal posture
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
