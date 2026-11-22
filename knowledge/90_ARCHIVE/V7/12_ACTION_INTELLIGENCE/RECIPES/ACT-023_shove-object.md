---
id: ACT-023
title: Make him push a heavy boulder
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: force, shove, object, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-023 — Make him push a heavy boulder

**Creative intention:** Make the viewer understand: him push a heavy boulder.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (90 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F009 | Boulder blocks travel |
| Perception | F010–F016 | Hands test surface and resistance |
| Decision | F017–F024 | Commit more effort |
| Anticipation | F025–F037 | Feet spread; torso leans; hands press |
| Action | F038–F068 | Shoulders drive force and boulder begins moving after resistance |
| Consequence | F069–F089 | Character follows moving mass slowly |

## Character and asset engineering

- **Primary rig/controllers:** feet/hips/arms/hands/object.
- **Recommended system:** contact-driven force envelope plus hips/head/tail/limb overlap.
- **Named channel:** `objectX`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Wide framing includes feet, contact and boulder
- **Sound objective:** Stone scraping begins after applied force
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const objectX = frame < 38 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-023", frame, recipes);
const objectX = pose.channels.objectX;
const phase = pose.phase;
// Connect objectX to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Boulder glides away before character touches it.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Constraint requires hand contact and push threshold.

## Observable acceptance test

- Stimulus visible or intentionally audible: Boulder blocks travel
- Perception and decision visibly motivate action: Hands test surface and resistance; Commit more effort
- Main event actually completed: Shoulders drive force and boulder begins moving after resistance
- Aftermath visible: Character follows moving mass slowly
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
