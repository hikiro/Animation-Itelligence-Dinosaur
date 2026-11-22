---
id: ACT-028
title: Make the crash through foliage readable
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: spatial, break, through, acting, implementation, qa
source_ids: S46,S47
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-028 — Make the crash through foliage readable

**Creative intention:** Make the viewer understand: the crash through foliage readable.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (120 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Dense fern screens the chase route |
| Perception | F012–F019 | Dinosaur sees travel corridor through leaves |
| Decision | F020–F029 | Keep advancing into the obstructing foliage |
| Anticipation | F030–F041 | Head pushes foliage ahead of torso |
| Action | F042–F084 | Leaves bend before tearing, then separate and fall |
| Consequence | F085–F119 | Branch and leaves retain momentum after passage |

## Character and asset engineering

- **Primary rig/controllers:** foliage joints/body collider.
- **Recommended system:** rig/world coordinates, apertures, collision and camera continuity.
- **Named channel:** `foliageDeflectionPx`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Do not hide every contact with particles
- **Sound objective:** Layered leaf rustle, tearing, delayed falling leaves
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const foliageDeflectionPx = frame < 42 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-028", frame, recipes);
const foliageDeflectionPx = pose.channels.foliageDeflectionPx;
const phase = pose.phase;
// Connect foliageDeflectionPx to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Decorative green particles appear before foliage touched.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Simulate progressive contact response then fragment release.

## Observable acceptance test

- Stimulus visible or intentionally audible: Dense fern screens the chase route
- Perception and decision visibly motivate action: Dinosaur sees travel corridor through leaves; Keep advancing into the obstructing foliage
- Main event actually completed: Leaves bend before tearing, then separate and fall
- Aftermath visible: Branch and leaves retain momentum after passage
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S46,S47; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
