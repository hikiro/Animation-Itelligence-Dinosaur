---
id: ACT-005
title: He sees the branch before ducking
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: perception, spot, hazard, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-005 — He sees the branch before ducking

**Creative intention:** Make the viewer understand: he sees the branch before ducking.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (90 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F008 | Low branch approaches on chase path |
| Perception | F009–F017 | Eyes track branch and available clearance |
| Decision | F018–F026 | Decide to lower his body |
| Anticipation | F027–F038 | Quick head tuck and knee flex |
| Action | F039–F065 | Torso folds; hips lower; feet maintain forward contact sequence |
| Consequence | F066–F089 | Passes safely beneath branch |

## Character and asset engineering

- **Primary rig/controllers:** eyes/head/spine/hips/knees.
- **Recommended system:** eye target then head turn; torso and foot turn only if intention changes.
- **Named channel:** `torsoLowerPx`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Keep branch edge and head in same shot
- **Sound objective:** Wind rush ahead of nearest foliage brush
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const torsoLowerPx = frame < 39 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-005", frame, recipes);
const torsoLowerPx = pose.channels.torsoLowerPx;
const phase = pose.phase;
// Connect torsoLowerPx to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Character ducks before any branch is visible.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Show obstacle well before avoidance beat.

## Observable acceptance test

- Stimulus visible or intentionally audible: Low branch approaches on chase path
- Perception and decision visibly motivate action: Eyes track branch and available clearance; Decide to lower his body
- Main event actually completed: Torso folds; hips lower; feet maintain forward contact sequence
- Aftermath visible: Passes safely beneath branch
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
