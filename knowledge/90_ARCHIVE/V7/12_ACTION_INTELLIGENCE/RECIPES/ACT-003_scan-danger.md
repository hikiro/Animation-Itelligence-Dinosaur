---
id: ACT-003
title: Have the character search the forest
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: perception, scan, danger, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-003 — Have the character search the forest

**Creative intention:** Make the viewer understand: have the character search the forest.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (90 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F008 | Ambience suddenly becomes quieter |
| Perception | F009–F017 | Notices gaps in known animal sounds |
| Decision | F018–F026 | Search for a hidden threat |
| Anticipation | F027–F038 | Pause gait and adjust balance |
| Action | F039–F065 | Eye scan left-right; head catches up; step to clear obstruction |
| Consequence | F066–F089 | Threat location becomes a plausible next reveal |

## Character and asset engineering

- **Primary rig/controllers:** eyes/head/neck/pelvis.
- **Recommended system:** eye target then head turn; torso and foot turn only if intention changes.
- **Named channel:** `gazeX`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Do not cut away during essential glance changes
- **Sound objective:** Fade bird ambience then focused leaf rustle
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const gazeX = frame < 39 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-003", frame, recipes);
const gazeX = pose.channels.gazeX;
const phase = pose.phase;
// Connect gazeX to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Random head wiggle with no visual target.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Assign three look targets tied to sound and scene geometry.

## Observable acceptance test

- Stimulus visible or intentionally audible: Ambience suddenly becomes quieter
- Perception and decision visibly motivate action: Notices gaps in known animal sounds; Search for a hidden threat
- Main event actually completed: Eye scan left-right; head catches up; step to clear obstruction
- Aftermath visible: Threat location becomes a plausible next reveal
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
