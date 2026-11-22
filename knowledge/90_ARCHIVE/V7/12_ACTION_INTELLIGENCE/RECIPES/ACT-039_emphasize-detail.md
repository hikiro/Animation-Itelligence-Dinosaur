---
id: ACT-039
title: Give the cracking egg cinematic importance
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: cinema, emphasize, detail, acting, implementation, qa
source_ids: S46,S49
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-039 — Give the cracking egg cinematic importance

**Creative intention:** Make the viewer understand: give the cracking egg cinematic importance.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (120 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Egg produces first quiet crack amid noisy chase |
| Perception | F012–F022 | Human hears a small unexpected sound |
| Decision | F023–F030 | Direct viewer to source without losing geography |
| Anticipation | F031–F044 | Brief hold and human glance |
| Action | F045–F082 | Camera gently pushes to shell crack after hand/egg visibility |
| Consequence | F083–F119 | Crack becomes new center of attention |

## Character and asset engineering

- **Primary rig/controllers:** camera/human hands/egg.
- **Recommended system:** camera or mixer controls referenced to actor world events.
- **Named channel:** `cameraScale`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Push-in motivated by recognition, return to wider shot
- **Sound objective:** Duck music so shell transient is audible
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const cameraScale = frame < 45 ? 0 : 1; // abrupt state jump, ignores perception/contact
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-039", frame, recipes);
const cameraScale = pose.channels.cameraScale;
const phase = pose.phase;
// Connect cameraScale to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Random dramatic zoom unrelated to what characters see.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Begin after eye contact establishes source, preserve orientation.

## Observable acceptance test

- Stimulus visible or intentionally audible: Egg produces first quiet crack amid noisy chase
- Perception and decision visibly motivate action: Human hears a small unexpected sound; Direct viewer to source without losing geography
- Main event actually completed: Camera gently pushes to shell crack after hand/egg visibility
- Aftermath visible: Crack becomes new center of attention
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S46,S49; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
