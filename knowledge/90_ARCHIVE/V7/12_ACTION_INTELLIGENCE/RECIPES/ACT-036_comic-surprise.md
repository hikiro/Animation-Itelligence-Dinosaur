---
id: ACT-036
title: Make a funny delayed reaction
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: emotion, comic, surprise, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-036 — Make a funny delayed reaction

**Creative intention:** Make the viewer understand: a funny delayed reaction.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (108 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F013 | Unexpected giant snout begins stretching portal |
| Perception | F014–F023 | Human perceives odd shadow and hears creak |
| Decision | F024–F033 | Slowly realize what is happening |
| Anticipation | F034–F045 | Character stays still for one beat, eyes shift |
| Action | F046–F077 | Head turns slowly, then body springs in exaggerated shock |
| Consequence | F078–F107 | Pause after reveal lets joke land |

## Character and asset engineering

- **Primary rig/controllers:** eyes/head/shoulders/hips.
- **Recommended system:** gaze, intention, pose contrasts, breath and whole-body reactions.
- **Named channel:** `headTurnDeg`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Keep snout offscreen long enough to earn reveal
- **Sound objective:** Creak then intentionally awkward silence and short accent
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const headTurnDeg = frame < 46 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-036", frame, recipes);
const headTurnDeg = pose.channels.headTurnDeg;
const phase = pose.phase;
// Connect headTurnDeg to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Random instant scream before audience sees the snout.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Set up sightline, delayed recognition, decisive reaction and hold.

## Observable acceptance test

- Stimulus visible or intentionally audible: Unexpected giant snout begins stretching portal
- Perception and decision visibly motivate action: Human perceives odd shadow and hears creak; Slowly realize what is happening
- Main event actually completed: Head turns slowly, then body springs in exaggerated shock
- Aftermath visible: Pause after reveal lets joke land
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
