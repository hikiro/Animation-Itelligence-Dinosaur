---
id: ACT-016
title: Make him gently put the baby down
kind: action_recipe
status: PROPOSED_NOT_PRODUCTION_VERIFIED
tags: object, put, down, acting, implementation, qa
source_ids: S45,S47
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: 2D, AE, Remotion, storyboard
updated: 2026-11-19
---

# ACT-016 — Make him gently put the baby down

**Creative intention:** Make the viewer understand: him gently put the baby down.

**Context dependency:** Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps. This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps (108 frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
| Stimulus | F000–F011 | Mother waits and baby wriggles |
| Perception | F012–F018 | Human identifies safe landing spot |
| Decision | F019–F027 | Set baby down safely |
| Anticipation | F028–F039 | Crouch and align baby over ground |
| Action | F040–F075 | Lower baby until feet contact; open hands after support |
| Consequence | F076–F107 | Hands withdraw; baby stands independently |

## Character and asset engineering

- **Primary rig/controllers:** root/hips/knees/hands/baby.
- **Recommended system:** two-hand target constraints, object world pose, ownership transfer.
- **Named channel:** `handHeightPx`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** Avoid cut at release; feet must remain visible
- **Sound objective:** Soft toe contact precedes cloth release sound
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
const pose = sampleAction("ACT-016", frame, recipes);
const handHeightPx = pose.channels.handHeightPx;
const phase = pose.phase;
// Connect handHeightPx to the appropriate rig/camera/audio property.
// Extra collision/IK/occlusion constraints are mandatory when listed below.
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** Baby teleports from hands to ground.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** Release ownership only after ground contact constraint is valid.

## Observable acceptance test

- Stimulus visible or intentionally audible: Mother waits and baby wriggles
- Perception and decision visibly motivate action: Human identifies safe landing spot; Set baby down safely
- Main event actually completed: Lower baby until feet contact; open hands after support
- Aftermath visible: Hands withdraw; baby stands independently
- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: S45,S47; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
