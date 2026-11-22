# Lesson 05 — Production tests and failure classification

## Gate 1: Does the action exist?

A proposed action must be represented as world-state changes, not only a screenplay verb. Check pre-state, state at decisive frame, and post-state. For portal passage: inside → threshold crossing → outside. For catch: free-falling object → shared contact → held and supported. For footfall: airborne foot → planted foot and load → delayed environment/whole-body response.

## Gate 2: Is the animation physically and spatially coherent?

Sample frames at contact-1, contact, contact+1, and at pose transition boundaries. Compare positions and velocities. Measure signed distance of foot to ground, contact coordinates and prop anchors in world space. Mark intentional stylization separately. A 0-frame collision detection from geometry is stronger evidence than a hand-written timeline comment.

## Gate 3: Are character intention and reaction readable?

Use a silent-viewer test: can someone describe what was noticed, why the actor moved, where contact happened, and what consequence followed? Numeric tests cannot prove all four questions. If a viewer misidentifies the action, send it back to blocking.

## Gate 4: Is camera continuity preserved?

Check subject identity/scale, screen direction, positive/negative space, essential contact visibility, and edit match. If the camera itself changes trajectory, calculate its world coordinates independently from the object's path.

## Gate 5: Does sound belong to the event?

Validate audio onset against exact event frame; distinguish legitimate offscreen anticipation from premature Foley. Check object materials, acoustic distance, music masking, edit bridges and subjective/ordinary sound. Listen on speakers and headphones; inspect waveform only as supporting evidence, not proof of perceptual quality.

## Gate 6: Update learning and avoid false completion

Record `{issue_id, recipe_id, source, timestamp, frame, actual, expected, root_cause, fix, rerender, regression_result, evidence_class}`. Do not promote a recipe from `PROPOSED` to `VERIFIED` because only its code parsed.

## First three educational comparisons

1. **ACT-025 Portal:** no doorway passage vs person inside aperture and later outside. Schematic only; lacks full 3D volume and production-quality planted-foot IK.
2. **ACT-019 Stomp:** premature random jitter before foot impact vs delayed gaze and whole-body response after foot contact. A synthetic footfall is included for timing reference only, not cinematic Foley.
3. **ACT-014 Egg catch:** egg teleport vs continuous fall plus hand interception and transfer. It is a simple 2D illustration, not a final physically simulated catch.

## Critical unresolved issues after diagram tests

- No reviewed target-grade adult/human/juvenile rigs.
- No genuine full portal depth or perspective geometry, only a 2D compositing example.
- No two-dimensional IK solver with stable world-space contacts across the entire walk cycle.
- No final multi-stem sound mix; a single synthetic thump demonstrates an event cue.
- No verified portal benchmark of the approved 270-frame film.

No amount of polished text should change these gate states.
