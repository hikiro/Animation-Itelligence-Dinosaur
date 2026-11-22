---
id: ACT-040
title: Cut between views without teleporting
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: cinema, match, action, acting, implementation, qa
source_ids: S46,S49
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-040 — Cut between views without teleporting

**Creative intention:** Make the viewer understand: cut between views without teleporting.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (120 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Human begins lifting baby in wide shot |
| Perception | F012–F022 | Audience recognizes start of lift |
| Decision | F023–F030 | Show hand contact close, then return wide |
| Anticipation | F031–F044 | Hand approaches, cut on continuous movement |
| Action | F045–F082 | New shot continues same hand/egg positions and phase |
| Consequence | F083–F119 | Object geography remains consistent over cut |

## Character and asset engineering

- **Primary rig/controllers:** camera/hand/baby.
- **Recommended system:** camera or mixer controls referenced to actor world events.
- **Named channel:** `handY`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Match hand vector/axis, not just any position
- **Sound objective:** Maintain one continuous Foley trajectory across cut
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const handY = frame < 45 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-040", frame, recipes);
const handY = pose.channels.handY;
const phase = pose.phase;
// Connect handY to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Hands reset to old position after cut.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Record world state at edit and reconstruct new camera pose.

## Observable acceptance test

- Stimulus visible or intentionally audible: Human begins lifting baby in wide shot
- Perception and decision visibly motivate action: Audience recognizes start of lift; Show hand contact close, then return wide
- Main event actually completed: New shot continues same hand/egg positions and phase
- Aftermath visible: Object geography remains consistent over cut
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S46,S49; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
