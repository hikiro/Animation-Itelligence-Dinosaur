---
id: ACT-038
title: Reveal the dinosaur's size dramatically
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: cinema, reveal, threat, acting, implementation, qa
source_ids: S46,S49
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-038 — Reveal the dinosaur's size dramatically

**Creative intention:** Make the viewer understand: reveal the dinosaur's size dramatically.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (120 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Ground begins vibrating before creature appears |
| Perception | F012–F022 | Audience hears offscreen footsteps and sees human reaction |
| Decision | F023–F030 | Build anticipation before identification |
| Anticipation | F031–F044 | Hold lower portion of frame with shadow and foot |
| Action | F045–F082 | Tilt or reframe from foot to massive head |
| Consequence | F083–F119 | Character scale is established in shared geography |

## Character and asset engineering

- **Primary rig/controllers:** camera/ground/shadow/dinosaur.
- **Recommended system:** camera or mixer controls referenced to actor world events.
- **Named channel:** `cameraTiltDeg`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Begin low, let human remain a size reference
- **Sound objective:** Low footfalls can intentionally precede visual reveal
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const cameraTiltDeg = frame < 45 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-038", frame, recipes);
const cameraTiltDeg = pose.channels.cameraTiltDeg;
const phase = pose.phase;
// Connect cameraTiltDeg to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Immediate face close-up removes size information.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Reveal scale by connected view foot→body→head.

## Observable acceptance test

- Stimulus visible or intentionally audible: Ground begins vibrating before creature appears
- Perception and decision visibly motivate action: Audience hears offscreen footsteps and sees human reaction; Build anticipation before identification
- Main event actually completed: Tilt or reframe from foot to massive head
- Aftermath visible: Character scale is established in shared geography
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S46,S49; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
