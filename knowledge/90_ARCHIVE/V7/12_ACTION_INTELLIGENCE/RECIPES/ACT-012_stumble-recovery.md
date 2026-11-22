---
id: ACT-012
title: Make him nearly fall but recover
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: locomotion, stumble, recovery, acting, implementation, qa
source_ids: S45,S48
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-012 — Make him nearly fall but recover

**Creative intention:** Make the viewer understand: him nearly fall but recover.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (96 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F007 | One shoe catches exposed root |
| Perception | F008–F015 | Sees falling ground and egg at risk |
| Decision | F016–F024 | Keep egg safe and restore balance |
| Anticipation | F025–F036 | Arms clamp egg; torso pitches |
| Action | F037–F072 | Recovery step lands ahead of tipping center of mass |
| Consequence | F073–F095 | Body regains balance without dropping egg |

## Character and asset engineering

- **Primary rig/controllers:** root/hips/feet/egg hands.
- **Recommended system:** hips COM, stance foot world-lock, knee IK and overlapping arms.
- **Named channel:** `torsoTiltDeg`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Hold continuous medium-wide to show foot and hands
- **Sound objective:** Scuff, gasp, heavy recovery step
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const torsoTiltDeg = frame < 37 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-012", frame, recipes);
const torsoTiltDeg = pose.channels.torsoTiltDeg;
const phase = pose.phase;
// Connect torsoTiltDeg to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Sudden spin or squash with no visible trip cause.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Root contact first; move COM toward failure then plant recovery foot.

## Observable acceptance test

- Stimulus visible or intentionally audible: One shoe catches exposed root
- Perception and decision visibly motivate action: Sees falling ground and egg at risk; Keep egg safe and restore balance
- Main event actually completed: Recovery step lands ahead of tipping center of mass
- Aftermath visible: Body regains balance without dropping egg
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S48; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
