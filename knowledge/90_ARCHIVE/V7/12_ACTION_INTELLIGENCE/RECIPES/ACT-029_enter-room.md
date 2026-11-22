---
id: ACT-029
title: Make arrival in apartment geographically coherent
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: spatial, enter, room, acting, implementation, qa
source_ids: S46,S47
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-029 — Make arrival in apartment geographically coherent

**Creative intention:** Make the viewer understand: arrival in apartment geographically coherent.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (120 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Portal connects prehistoric forest to apartment |
| Perception | F012–F019 | Human sees a floor immediately beyond rim |
| Decision | F020–F029 | Move into new environment |
| Anticipation | F030–F041 | Leading foot tests carpet |
| Action | F042–F084 | Body crosses plane; contact surface/material changes |
| Consequence | F085–F119 | Footstep texture changes and apartment reverb appears |

## Character and asset engineering

- **Primary rig/controllers:** portal/human/camera/floor.
- **Recommended system:** rig/world coordinates, apertures, collision and camera continuity.
- **Named channel:** `crossingPct`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Match screen direction through plane or clearly re-establish
- **Sound objective:** Cross-portal ambience and carpet foot sound with perspective
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const personX = -50 + frame*6; // slides in from screen edge; no portal depth or occlusion
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-029", frame, recipes);
const crossingPct = pose.channels.crossingPct;
const phase = pose.phase;
// Connect crossingPct to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** New room starts with character already fully in it.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Match portal world transform and mask over cut.

## Observable acceptance test

- Stimulus visible or intentionally audible: Portal connects prehistoric forest to apartment
- Perception and decision visibly motivate action: Human sees a floor immediately beyond rim; Move into new environment
- Main event actually completed: Body crosses plane; contact surface/material changes
- Aftermath visible: Footstep texture changes and apartment reverb appears
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S46,S47; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
