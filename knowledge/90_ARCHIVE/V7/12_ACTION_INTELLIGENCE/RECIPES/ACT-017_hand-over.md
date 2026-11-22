---
id: ACT-017
title: Pass an object from one character to another
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: object, hand, over, acting, implementation, qa
source_ids: S45,S47
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-017 — Pass an object from one character to another

**Creative intention:** Make the viewer understand: pass an object from one character to another.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (108 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Receiver reaches toward offered object |
| Perception | F012–F018 | Both characters follow object with gaze |
| Decision | F019–F027 | Perform coordinated transfer |
| Anticipation | F028–F039 | Receiver opens hand; giver slows |
| Action | F040–F075 | Receiver grips at overlap then giver releases |
| Consequence | F076–F107 | Object remains continuously supported |

## Character and asset engineering

- **Primary rig/controllers:** givers hand/receiver hand/prop anchors.
- **Recommended system:** two-hand target constraints, object world pose, ownership transfer.
- **Named channel:** `propX`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Two-shot with hands sharing spatial region
- **Sound objective:** Fabric and soft grip sounds at hand overlap
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const propX = lerp(0, 400, frame/100); // independent movement, no contact/ownership state
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-017", frame, recipes);
const propX = pose.channels.propX;
const phase = pose.phase;
// Connect propX to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Object briefly floats between characters.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Dual-grip interval then explicit ownership change.

## Observable acceptance test

- Stimulus visible or intentionally audible: Receiver reaches toward offered object
- Perception and decision visibly motivate action: Both characters follow object with gaze; Perform coordinated transfer
- Main event actually completed: Receiver grips at overlap then giver releases
- Aftermath visible: Object remains continuously supported
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S47; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
