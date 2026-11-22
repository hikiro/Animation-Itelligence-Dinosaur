---
id: ACT-002
title: Make him hear something behind him
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: perception, turn, toward, sound, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-002 — Make him hear something behind him

**Creative intention:** Make the viewer understand: him hear something behind him.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (90 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F008 | An offscreen thump reaches him |
| Perception | F009–F017 | Ear/head attention shifts toward sonic source |
| Decision | F018–F026 | Identify where sound came from |
| Anticipation | F027–F038 | Foot freezes and shoulder lifts |
| Action | F039–F065 | Eyes move left; head rotates; torso follows later |
| Consequence | F066–F089 | Now faces the unseen source |

## Character and asset engineering

- **Primary rig/controllers:** head/shoulder/torso/eyes.
- **Recommended system:** eye target then head turn; torso and foot turn only if intention changes.
- **Named channel:** `headTurnDeg`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Begin on his profile, retain screen geography of sound
- **Sound objective:** Offscreen low thump can correctly lead reveal
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const headTurnDeg = frame < 39 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-002", frame, recipes);
const headTurnDeg = pose.channels.headTurnDeg;
const phase = pose.phase;
// Connect headTurnDeg to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Character reacts before thump without an intended premonition.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Key perception after sound onset; let head follow ears.

## Observable acceptance test

- Stimulus visible or intentionally audible: An offscreen thump reaches him
- Perception and decision visibly motivate action: Ear/head attention shifts toward sonic source; Identify where sound came from
- Main event actually completed: Eyes move left; head rotates; torso follows later
- Aftermath visible: Now faces the unseen source
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
