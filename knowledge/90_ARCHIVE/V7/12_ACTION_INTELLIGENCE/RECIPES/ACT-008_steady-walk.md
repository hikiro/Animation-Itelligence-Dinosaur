---
id: ACT-008
title: Make the character walk naturally
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: locomotion, steady, walk, acting, implementation, qa
source_ids: S45,S48
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-008 — Make the character walk naturally

**Creative intention:** Make the viewer understand: the character walk naturally.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (96 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F007 | Character sees desired destination |
| Perception | F008–F015 | Eyes lead travel direction |
| Decision | F016–F024 | Maintain controlled pace |
| Anticipation | F025–F036 | Body leans by small angle |
| Action | F037–F072 | Alternate stance and swing with independent support foot |
| Consequence | F073–F095 | Head and arms overlap the stride |

## Character and asset engineering

- **Primary rig/controllers:** hips/leg IK/arms/head.
- **Recommended system:** hips COM, stance foot world-lock, knee IK and overlapping arms.
- **Named channel:** `rootX`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Side-on readable feet and floor
- **Sound objective:** Footfalls at support transitions; footsteps vary slightly
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const footWorldX = hipX + 30*Math.sin(frame*.3); // planted foot slides with root
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-008", frame, recipes);
const rootX = pose.channels.rootX;
const phase = pose.phase;
// Connect rootX to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Sinusoidal legs with no support lock.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Use stride phase and world-space support anchors.

## Observable acceptance test

- Stimulus visible or intentionally audible: Character sees desired destination
- Perception and decision visibly motivate action: Eyes lead travel direction; Maintain controlled pace
- Main event actually completed: Alternate stance and swing with independent support foot
- Aftermath visible: Head and arms overlap the stride
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S48; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
