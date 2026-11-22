---
id: ACT-022
title: Make the jump landing have weight
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: force, land, from, jump, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-022 — Make the jump landing have weight

**Creative intention:** Make the viewer understand: the jump landing have weight.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (90 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F009 | Character falls toward chosen landing spot |
| Perception | F010–F016 | Feet orient toward contact plane |
| Decision | F017–F024 | Absorb downward momentum |
| Anticipation | F025–F037 | Knees begin extending toward floor |
| Action | F038–F068 | Feet touch then knees/hips compress |
| Consequence | F069–F089 | Torso settles; arms counterbalance and recover |

## Character and asset engineering

- **Primary rig/controllers:** feet/knees/hips/arms.
- **Recommended system:** contact-driven force envelope plus hips/head/tail/limb overlap.
- **Named channel:** `hipDropPx`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Wide view with feet and landing plane
- **Sound objective:** Foot impact at measured contact frame, small fabric tail
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const hipDropPx = frame < 38 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-022", frame, recipes);
const hipDropPx = pose.channels.hipDropPx;
const phase = pose.phase;
// Connect hipDropPx to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Instantly frozen pose at ground y.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Vertical path intersects floor then compressed body pose.

## Observable acceptance test

- Stimulus visible or intentionally audible: Character falls toward chosen landing spot
- Perception and decision visibly motivate action: Feet orient toward contact plane; Absorb downward momentum
- Main event actually completed: Feet touch then knees/hips compress
- Aftermath visible: Torso settles; arms counterbalance and recover
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
