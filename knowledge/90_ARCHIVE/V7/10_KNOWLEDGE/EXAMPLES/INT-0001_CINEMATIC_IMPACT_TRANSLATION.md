---
id: INT-0001
title: Natural-language projectile impact to director and AE implementation
kind: workflow
status: production-heuristic
tags: impact, acting, camera, sound, after-effects, expressions
source_ids: LRN-0002, LRN-0004, LRN-0009
related_ids: LRN-0005, LRN-0006
applies_to: fictional non-graphic impact examples
updated: 2026-11-19
---
# INT-0001 — Full translation example from human speech

## Input (human-level)

“Make it clear that the projectile hits. There should be recoil; the projectile feels cinematic and cuts through the water; maybe zoom in with manga-style art, zoom out to the character, then a flash, character vibrates and falls slowly.”

## Interpret, don't copy literally

**Meaning:** Visual and auditory proof of cause → travel → contact → force → character response → aftermath, with stylized focus and time dilation. “Through the water” could mean literal underwater travel (ripples/bubbles/refraction) **or** metaphorical air-slicing trails. These are different effects. Document the selected interpretation; don't silently add a physical ocean to an unrelated scene.

**Non-graphic fictional framing:** This exercise explores animation comprehensibility; omit instructions about actual weapon handling or physical injury and avoid graphic injury detail.

## Proposed shot chain (illustrative beat lengths, not fixed production timing)

| Beat | Action and state | Camera language | Sound perspective | AE building blocks | Visual pass test |
|---|---|---|---|---|---|
| 1. Perceive/prepare | Shooter knows decision, visible body preparation | Medium establishes both geography and launch direction | Breath/low ambience, expectant drop | Layered rig, keyed hand/torso/foot support | Viewer knows source and orientation |
| 2. Launch/recoil | Event occurs, source arm/shoulders/torso/feet respond | Hold briefly on launch to prove causality | One tightly placed launch transient; no exaggerated pre-impact audio | Pose keys; parented prop; slight inertial settle | Recoil occurs *after/same time* as launch, not before |
| 3. Flight | Projectile remains visible with continuity | Motivated side-tracking insert or carefully matched cut; don't lose screen direction | Whistle/water wake if the world is actually underwater | Shape path, distinct projectile layer, motion blur, trail, time remap if stylized | Viewer sees where it came from and where it's going |
| 4. Stylized emphasis | Manga graphic frame reinforces speed, not unrelated decoration | Extreme close insert with intentionally compressed perspective; cut back on motion vector | Narrow filtered whoosh, optional sonic perspective shift | Trim Paths, Repeater, directional lines, layered graphic hold | Insert retains origin/destination association |
| 5. Contact | Projectile occupies exact target location at hit frame | Reframe/widen enough to prove recipient contact | Sharp synchronized transient and brief reflected/tactile layer | Contact null, tracked accent, selective matte, brief opacity envelope | Exact collision before target's response |
| 6. Receiving force | Character compresses/deflects, loses balance, staggers | Stable or modest offset; avoid masking pose | Body/clothing/ground detail; score may retreat | Full-body keyed pose, root motion, feet, decaying secondary rotations | Whole body responds to force, not camera shake alone |
| 7. Fall/recovery | Character reaches ground or retains balance; physical consequence persists | Restraint/hold for outcome; controlled slow motion only when intentional | Contact with ground and decaying room/environment tone | Keyframe gravity-ish arc and contact; secondary settle; optional time remap | Viewer can identify final state even with effects off |

## Explicit conflicts to resolve

- A literal curved projectile path and a grounded physical shot differ. Default: preserve path continuity, allow *camera perspective* to curve; only stylize actual path when clearly intended.
- Underwater travel requires bubbles, wakes and refraction; “water-like” streak as a metaphor does not imply underwater physics.
- Slow fall may look floaty; distinguish a fast reaction from time-dilated editorial depiction of its aftermath.
- A harsh full-frame flash/shake could obscure the impact and pose; use a brief local accent, then inspect without it.

## Output contract the agent should generate

1. `INTENT`: audience should unambiguously understand projectile-to-recipient impact.
2. `CAUSAL_STATES`: launch, travel, contact, force transfer, fall/settle.
3. `WORLD`: start/target geographic positions, direction, depths, contact anchors.
4. `STAGING`: coverage and viewer knowledge at each cut; realism/stylization selected.
5. `MOTION`: poses, path, foot/hip support, recoil timing, secondary follow-through.
6. `AE_LAYER_MAP`: rig nulls, separate shape/projectile/streak, masks/solid accents, contact control.
7. `EXPRESSIONS`: only the procedural accent envelope, delay, or linked controller—not primary contact acting.
8. `AUDIO`: events derived from actual time-coded contacts plus editorial perspective exceptions.
9. `TEST`: no FX/no audio and with FX/audio; frame-before/on/after; compare contact and fall.
10. `UNKNOWN`: ambiguity surfaced as alternatives; ask only if selecting would change the story.

## Lesson reference

See `11_AFTER_EFFECTS/04_EXPRESSION_COOKBOOK.md` for decay and rig-control samples. These examples have **not** been rendered in After Effects; use the actual implementation environment to validate.
