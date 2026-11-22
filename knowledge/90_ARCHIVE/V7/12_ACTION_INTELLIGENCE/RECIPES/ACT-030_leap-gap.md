---
id: ACT-030
title: Make a gap jump visually plausible
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: spatial, leap, gap, acting, implementation, qa
source_ids: S46,S47
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-030 — Make a gap jump visually plausible

**Creative intention:** Make the viewer understand: a gap jump visually plausible.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (120 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Character sees missing ground ahead |
| Perception | F012–F019 | Eyes estimate landing zone |
| Decision | F020–F029 | Choose jump instead of stopping |
| Anticipation | F030–F041 | Knees compress and arms swing back |
| Action | F042–F084 | Takeoff occurs at edge, airborne arc crosses gap |
| Consequence | F085–F119 | Landing contacts far side and absorbs momentum |

## Character and asset engineering

- **Primary rig/controllers:** legs/hips/arms/root.
- **Recommended system:** rig/world coordinates, apertures, collision and camera continuity.
- **Named channel:** `rootY`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Wide shot shows both edges and full trajectory
- **Sound objective:** Takeoff scrape, airborne quiet, landing thump
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const rootY = frame < 42 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-030", frame, recipes);
const rootY = pose.channels.rootY;
const phase = pose.phase;
// Connect rootY to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Character teleports over gap with linear root X and constant Y.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Define takeoff/contact frames and continuous ballistic-like arc.

## Observable acceptance test

- Stimulus visible or intentionally audible: Character sees missing ground ahead
- Perception and decision visibly motivate action: Eyes estimate landing zone; Choose jump instead of stopping
- Main event actually completed: Takeoff occurs at edge, airborne arc crosses gap
- Aftermath visible: Landing contacts far side and absorbs momentum
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S46,S47; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
