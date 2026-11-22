---
id: ACT-021
title: Make the hit clearly understandable
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: force, impact, body, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-021 — Make the hit clearly understandable

**Creative intention:** Make the viewer understand: the hit clearly understandable.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (90 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F009 | Moving object visibly reaches target |
| Perception | F010–F016 | Target registers force at contact |
| Decision | F017–F024 | Balance must respond |
| Anticipation | F025–F037 | Body has braced or remains unaware as intended |
| Action | F038–F068 | Contact compression; torso moves, limbs and head lag |
| Consequence | F069–F089 | Body recoils or falls with follow-through |

## Character and asset engineering

- **Primary rig/controllers:** torso/hips/neck/limbs/ground.
- **Recommended system:** contact-driven force envelope plus hips/head/tail/limb overlap.
- **Named channel:** `torsoDisplacePx`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Show target contact clearly before close emphasis
- **Sound objective:** Contact transient then clothes/grunt and lingering room tone
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const shake = Math.sin(frame*7)*18; // fake impact, no defined contact impulse or body reaction
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-021", frame, recipes);
const torsoDisplacePx = pose.channels.torsoDisplacePx;
const phase = pose.phase;
// Connect torsoDisplacePx to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Random wiggle and flash without actual collision.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Drive recoil by contact time, force direction and coordinated poses.

## Observable acceptance test

- Stimulus visible or intentionally audible: Moving object visibly reaches target
- Perception and decision visibly motivate action: Target registers force at contact; Balance must respond
- Main event actually completed: Contact compression; torso moves, limbs and head lag
- Aftermath visible: Body recoils or falls with follow-through
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
