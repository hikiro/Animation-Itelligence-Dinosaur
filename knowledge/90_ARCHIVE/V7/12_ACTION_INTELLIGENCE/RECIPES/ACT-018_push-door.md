---
id: ACT-018
title: Make a door open when pushed
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: object, push, door, acting, implementation, qa
source_ids: S45,S47
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-018 — Make a door open when pushed

**Creative intention:** Make the viewer understand: a door open when pushed.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (108 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Closed door blocks character route |
| Perception | F012–F018 | Eyes settle on handle and hinge |
| Decision | F019–F027 | Open it with appropriate force |
| Anticipation | F028–F039 | Feet brace and shoulder leans |
| Action | F040–F075 | Hand contacts door; shoulder and arm push, door rotates at hinge |
| Consequence | F076–F107 | Character steps through clear opening |

## Character and asset engineering

- **Primary rig/controllers:** feet/shoulder/hand/door hinge.
- **Recommended system:** two-hand target constraints, object world pose, ownership transfer.
- **Named channel:** `doorAngleDeg`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Three-quarter shot demonstrates hinge axis
- **Sound objective:** Latch click then hinge creak and footstep
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const doorAngleDeg = frame < 40 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-018", frame, recipes);
const doorAngleDeg = pose.channels.doorAngleDeg;
const phase = pose.phase;
// Connect doorAngleDeg to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Door swings before hand reaches it.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Hinge angle driven only after visible hand force begins.

## Observable acceptance test

- Stimulus visible or intentionally audible: Closed door blocks character route
- Perception and decision visibly motivate action: Eyes settle on handle and hinge; Open it with appropriate force
- Main event actually completed: Hand contacts door; shoulder and arm push, door rotates at hinge
- Aftermath visible: Character steps through clear opening
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S47; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
