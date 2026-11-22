---
id: ACT-015
title: Keep egg attached during chase
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: object, carry, prop, acting, implementation, qa
source_ids: S45,S47
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-015 — Keep egg attached during chase

**Creative intention:** Make the viewer understand: keep egg attached during chase.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (108 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Human has just caught egg |
| Perception | F012–F018 | Checks that it is stable |
| Decision | F019–F027 | Protect egg while running |
| Anticipation | F028–F039 | Bring elbows close to ribs |
| Action | F040–F075 | Arms counteract gait; egg stays in torso-relative cup |
| Consequence | F076–F107 | Egg never clips torso or floats outside hands |

## Character and asset engineering

- **Primary rig/controllers:** torso/arm/hand/prop constraint.
- **Recommended system:** two-hand target constraints, object world pose, ownership transfer.
- **Named channel:** `eggAnchorX`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Use frame including chest, hands, and escape path
- **Sound objective:** Subtle shell/rubbing noise, no separate random thumps
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
const propX = lerp(0, 400, frame/100); // independent movement, no contact/ownership state
```

**Better, event-addressable implementation**

```js
import { sampleAction } from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
const pose = sampleAction("ACT-015", frame, recipes);
const eggAnchorX = pose.channels.eggAnchorX;
const phase = pose.phase;
// Connect eggAnchorX to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Egg independently interpolates with its own X movement.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Drive egg from established hand attachment transform.

## Observable acceptance test

- Stimulus visible or intentionally audible: Human has just caught egg
- Perception and decision visibly motivate action: Checks that it is stable; Protect egg while running
- Main event actually completed: Arms counteract gait; egg stays in torso-relative cup
- Aftermath visible: Egg never clips torso or floats outside hands
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S47; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
