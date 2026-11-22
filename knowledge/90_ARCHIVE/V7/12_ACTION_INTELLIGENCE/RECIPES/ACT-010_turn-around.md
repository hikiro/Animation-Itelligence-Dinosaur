---
id: ACT-010
title: Make him turn before running
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: locomotion, turn, around, acting, implementation, qa
source_ids: S45,S48
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-010 — Make him turn before running

**Creative intention:** Make the viewer understand: him turn before running.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (96 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F007 | He notices danger behind him |
| Perception | F008–F015 | Eyes swing toward escape route |
| Decision | F016–F024 | Decide to reverse direction |
| Anticipation | F025–F036 | Hips load supporting foot |
| Action | F037–F072 | Eyes/head/shoulders/hips turn in sequence, feet pivot |
| Consequence | F073–F095 | Exit direction becomes unambiguous |

## Character and asset engineering

- **Primary rig/controllers:** eyes/head/torso/hips/foot anchors.
- **Recommended system:** hips COM, stance foot world-lock, knee IK and overlapping arms.
- **Named channel:** `bodyAngleDeg`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Keep screen direction constant and hold turn in shot
- **Sound objective:** Shoe friction sound on pivot contact
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const bodyAngleDeg = frame < 37 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-010", frame, recipes);
const bodyAngleDeg = pose.channels.bodyAngleDeg;
const phase = pose.phase;
// Connect bodyAngleDeg to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Translate left while torso still faces right.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Use staggered yaw/key poses followed by push off.

## Observable acceptance test

- Stimulus visible or intentionally audible: He notices danger behind him
- Perception and decision visibly motivate action: Eyes swing toward escape route; Decide to reverse direction
- Main event actually completed: Eyes/head/shoulders/hips turn in sequence, feet pivot
- Aftermath visible: Exit direction becomes unambiguous
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S48; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
