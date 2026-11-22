---
id: ACT-011
title: Make the dinosaur stop convincingly
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: locomotion, brake, heavy, acting, implementation, qa
source_ids: S45,S48
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-011 — Make the dinosaur stop convincingly

**Creative intention:** Make the viewer understand: the dinosaur stop convincingly.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (96 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F007 | Baby chirp reaches mother mid-run |
| Perception | F008–F015 | Eyes focus on newborn |
| Decision | F016–F024 | Avoid stepping on it |
| Anticipation | F025–F036 | Lower body, shorten stride, forelegs react |
| Action | F037–F072 | Hips decelerate; planted foot skids briefly; tail keeps moving |
| Consequence | F073–F095 | Dinosaur stops with visible mass and tail settle |

## Character and asset engineering

- **Primary rig/controllers:** hips/feet/head/tail.
- **Recommended system:** hips COM, stance foot world-lock, knee IK and overlapping arms.
- **Named channel:** `rootX`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Wider view retains feet and moving tail
- **Sound objective:** Two heavy decelerating footfalls, tail whoosh then quiet
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const rootX = frame < 37 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-011", frame, recipes);
const rootX = pose.channels.rootX;
const phase = pose.phase;
// Connect rootX to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Instant zero velocity with frozen tail.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Apply finite braking distance and delayed tail follow-through.

## Observable acceptance test

- Stimulus visible or intentionally audible: Baby chirp reaches mother mid-run
- Perception and decision visibly motivate action: Eyes focus on newborn; Avoid stepping on it
- Main event actually completed: Hips decelerate; planted foot skids briefly; tail keeps moving
- Aftermath visible: Dinosaur stops with visible mass and tail settle
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S48; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
