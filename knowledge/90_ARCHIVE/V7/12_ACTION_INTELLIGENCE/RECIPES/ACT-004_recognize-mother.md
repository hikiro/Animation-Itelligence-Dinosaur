---
id: ACT-004
title: She realizes the egg belongs to her
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: perception, recognize, mother, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-004 — She realizes the egg belongs to her

**Creative intention:** Make the viewer understand: she realizes the egg belongs to her.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (90 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F008 | Mother finds nest empty then sees egg in human arms |
| Perception | F009–F017 | Her gaze alternates between nest and egg |
| Decision | F018–F026 | Conclude human has the baby |
| Anticipation | F027–F038 | Body stiffens; nostrils widen |
| Action | F039–F065 | Head lowers and body points toward egg |
| Consequence | F066–F089 | Aggression becomes understandable |

## Character and asset engineering

- **Primary rig/controllers:** eyes/head/neck/hips/tail.
- **Recommended system:** eye target then head turn; torso and foot turn only if intention changes.
- **Named channel:** `headLowerPx`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Over-shoulder or shared axis includes nest, egg, mother
- **Sound objective:** One low breath rising toward roar
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const headLowerPx = frame < 39 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-004", frame, recipes);
const headLowerPx = pose.channels.headLowerPx;
const phase = pose.phase;
// Connect headLowerPx to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Instant anger before seeing empty nest or egg.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Stage empty nest and egg eyeline before posture change.

## Observable acceptance test

- Stimulus visible or intentionally audible: Mother finds nest empty then sees egg in human arms
- Perception and decision visibly motivate action: Her gaze alternates between nest and egg; Conclude human has the baby
- Main event actually completed: Head lowers and body points toward egg
- Aftermath visible: Aggression becomes understandable
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
