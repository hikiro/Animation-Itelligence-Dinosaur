---
id: ACT-037
title: Make the chase easy to follow
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: cinema, track, chase, acting, implementation, qa
source_ids: S46,S49
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-037 — Make the chase easy to follow

**Creative intention:** Make the viewer understand: the chase easy to follow.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (120 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Human runs left and dinosaur follows from right |
| Perception | F012–F022 | Audience must track decreasing gap |
| Decision | F023–F030 | Maintain both subjects spatially legible |
| Anticipation | F031–F044 | Start tracking after running speed is established |
| Action | F045–F082 | Camera moves to retain positions while foreground parallax passes |
| Consequence | F083–F119 | Dinosaur closing distance is measurable |

## Character and asset engineering

- **Primary rig/controllers:** camera root/environment layers.
- **Recommended system:** camera or mixer controls referenced to actor world events.
- **Named channel:** `cameraX`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Side tracking, ground horizon and direction locked
- **Sound objective:** Independent footfalls and whoosh anchored to camera perspective
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const cameraX = frame < 45 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-037", frame, recipes);
const cameraX = pose.channels.cameraX;
const phase = pose.phase;
// Connect cameraX to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Camera crosses axis and swaps predator/prey sides accidentally.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Define chase axis and camera path preserving screen direction.

## Observable acceptance test

- Stimulus visible or intentionally audible: Human runs left and dinosaur follows from right
- Perception and decision visibly motivate action: Audience must track decreasing gap; Maintain both subjects spatially legible
- Main event actually completed: Camera moves to retain positions while foreground parallax passes
- Aftermath visible: Dinosaur closing distance is measurable
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S46,S49; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
