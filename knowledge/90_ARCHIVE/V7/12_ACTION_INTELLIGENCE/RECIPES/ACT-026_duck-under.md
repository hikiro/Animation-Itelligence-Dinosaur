---
id: ACT-026
title: Make ducking under a branch credible
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: spatial, duck, under, acting, implementation, qa
source_ids: S46,S47
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-026 — Make ducking under a branch credible

**Creative intention:** Make the viewer understand: ducking under a branch credible.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (120 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Branch appears in path ahead |
| Perception | F012–F019 | Eyes measure branch clearance |
| Decision | F020–F029 | Choose to lower center of mass |
| Anticipation | F030–F041 | Head tucks and knees flex |
| Action | F042–F084 | Torso, hips and head move under obstacle while feet continue |
| Consequence | F085–F119 | Character rises only once head clears |

## Character and asset engineering

- **Primary rig/controllers:** neck/hips/knees/branch.
- **Recommended system:** rig/world coordinates, apertures, collision and camera continuity.
- **Named channel:** `headHeightPx`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Hold enough profile for top of head and branch
- **Sound objective:** Near-ear branch swish only at closest pass
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const headHeightPx = frame < 42 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-026", frame, recipes);
const headHeightPx = pose.channels.headHeightPx;
const phase = pose.phase;
// Connect headHeightPx to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Torso drops after head already intersects branch.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Lower before collision and track clearance frame-by-frame.

## Observable acceptance test

- Stimulus visible or intentionally audible: Branch appears in path ahead
- Perception and decision visibly motivate action: Eyes measure branch clearance; Choose to lower center of mass
- Main event actually completed: Torso, hips and head move under obstacle while feet continue
- Aftermath visible: Character rises only once head clears
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S46,S47; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
