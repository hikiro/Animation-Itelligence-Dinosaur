---
id: ACT-031
title: Make the character hesitate before acting
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: emotion, hesitation, acting, implementation, qa
source_ids: S45,S46
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-031 — Make the character hesitate before acting

**Creative intention:** Make the viewer understand: the character hesitate before acting.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (108 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F013 | An uncertain obstacle threatens success |
| Perception | F014–F023 | Looks at obstacle then possible exit |
| Decision | F024–F033 | Weigh competing actions |
| Anticipation | F034–F045 | Small backward weight shift and incomplete reach |
| Action | F046–F077 | First movement aborts, brief hold, second committed gesture |
| Consequence | F078–F107 | Decision becomes visible through contrast |

## Character and asset engineering

- **Primary rig/controllers:** eyes/shoulders/hand/feet.
- **Recommended system:** gaze, intention, pose contrasts, breath and whole-body reactions.
- **Named channel:** `handReachPx`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Keep medium composition stable to read micro-actions
- **Sound objective:** Small breath and pause; avoid excessive stinger
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const handReachPx = frame < 46 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-031", frame, recipes);
const handReachPx = pose.channels.handReachPx;
const phase = pose.phase;
// Connect handReachPx to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Uniform slow movement called hesitation.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Distinct blocked attempt, pause and committed pose.

## Observable acceptance test

- Stimulus visible or intentionally audible: An uncertain obstacle threatens success
- Perception and decision visibly motivate action: Looks at obstacle then possible exit; Weigh competing actions
- Main event actually completed: First movement aborts, brief hold, second committed gesture
- Aftermath visible: Decision becomes visible through contrast
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S46; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
