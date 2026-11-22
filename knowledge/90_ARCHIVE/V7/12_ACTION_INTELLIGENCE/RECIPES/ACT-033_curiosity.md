---
id: ACT-033
title: Make him curious about the new world
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: emotion, curiosity, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-033 — Make him curious about the new world

**Creative intention:** Make the viewer understand: him curious about the new world.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (108 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F013 | Human emerges into unfamiliar forest |
| Perception | F014–F023 | Looks at enormous leaves above |
| Decision | F024–F033 | Investigate cautiously |
| Anticipation | F034–F045 | Lean forward while keeping planted foot |
| Action | F046–F077 | Eyes rise, head tilts, hand reaches toward leaf |
| Consequence | F078–F107 | Discovering motivates next movement |

## Character and asset engineering

- **Primary rig/controllers:** eyes/head/neck/arm.
- **Recommended system:** gaze, intention, pose contrasts, breath and whole-body reactions.
- **Named channel:** `headTiltDeg`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Hold revealing foreground plant in shared frame
- **Sound objective:** Gentle leaves and quiet interested breath
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const headTiltDeg = frame < 46 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-033", frame, recipes);
const headTiltDeg = pose.channels.headTiltDeg;
const phase = pose.phase;
// Connect headTiltDeg to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Random tilt without visible subject.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Anchor every glance and reach to a plant or sound.

## Observable acceptance test

- Stimulus visible or intentionally audible: Human emerges into unfamiliar forest
- Perception and decision visibly motivate action: Looks at enormous leaves above; Investigate cautiously
- Main event actually completed: Eyes rise, head tilts, hand reaches toward leaf
- Aftermath visible: Discovering motivates next movement
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
