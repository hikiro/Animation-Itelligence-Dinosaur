---
id: ACT-024
title: Make the dinosaur break the branch
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: force, crash, branch, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-024 — Make the dinosaur break the branch

**Creative intention:** Make the viewer understand: the dinosaur break the branch.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (90 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F009 | Branch lies across mother's pursuit path |
| Perception | F010–F016 | She sees branch too late |
| Decision | F017–F024 | Continue chase through the obstacle without stopping |
| Anticipation | F025–F037 | Neck ducks imperfectly; shoulders drive forward |
| Action | F038–F068 | Head/shoulder impacts branch; bending precedes snapping |
| Consequence | F069–F089 | Pieces move outward with gravity and drag |

## Character and asset engineering

- **Primary rig/controllers:** head/neck/branch joints/fragments.
- **Recommended system:** contact-driven force envelope plus hips/head/tail/limb overlap.
- **Named channel:** `branchDeflectionPx`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Preserve recognizable branch and dinosaur contact point
- **Sound objective:** Wood strain then sharp crack at fracture, leaves after
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
const pose = sampleAction("ACT-024", frame, recipes);
const branchDeflectionPx = pose.channels.branchDeflectionPx;
const phase = pose.phase;
// Connect branchDeflectionPx to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Branch explodes before dinosaur reaches it.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Fracture only on predicted geometry contact and threshold.

## Observable acceptance test

- Stimulus visible or intentionally audible: Branch lies across mother's pursuit path
- Perception and decision visibly motivate action: She sees branch too late; Continue chase through the obstacle without stopping
- Main event actually completed: Head/shoulder impacts branch; bending precedes snapping
- Aftermath visible: Pieces move outward with gravity and drag
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
