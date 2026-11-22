# PRE-0003 — Have the character search the forest

**Category:** Perception  
**Tags:** perception, scan danger, legacy-derived  
**State:** `designed_unverified` (L2: authored recipe; not approved animation)  
**Principle/source support:** SRC-001, SRC-016 (sources support methods, NOT proof this exact preset renders correctly)  
**Legacy origin:** `90_ARCHIVE/V7/12_ACTION_INTELLIGENCE/RECIPES/ACT-003_scan-danger.md` (the older educational recipe is not validated production rigging).

## Human-language instruction and viewer goal
**Instruction:** Have the character search the forest.  
**Audience should understand:** Make the viewer understand: have the character search the forest..

## Required scene context
Fill before execution: **actor identity and anatomy**, **relative scale**, **prior pose and velocity**, **who perceives the trigger**, **character goal/belief**, **audience knowledge**, **world/terrain/material**, **style/realism exception**, **camera axis/frame**, **sound source/listener**, **preceding and following shot**. Do not silently infer omitted critical constraints.

## Causal event graph — editable
1. **Stimulus / setup:** Ambience suddenly becomes quieter
2. **Perception:** Notices gaps in known animal sounds
3. **Interpretation / decision:** Search for a hidden threat
4. **Anticipation / preparation:** Pause gait and adjust balance
5. **Visible action and contact:** Eye scan left-right; head catches up; step to clear obstruction
6. **Consequence and recovery:** Threat location becomes a plausible next reveal. Confirm the new state persists in subsequent shot.

## Rig, mechanics and interaction plan
**Suggested controls:** eyes/head/neck/pelvis. Define world-space root, joint pivots, contact target(s), support phase, body mass/center of motion, transfer of held props, overlapping appendages and legal movement ranges. Select IK only when a limb endpoint must meet a goal; do not use an expression-only shake as a replacement for rig/contact.

## Camera and editorial direction
Do not cut away during essential glance changes. State the viewer question and where the audience should look; preserve axis/scale and contact visibility. Camera trajectory is independent from object trajectory and cannot conceal missing actions.

## Audio and music direction
Fade bird ambience then focused leaf rustle. Attach a source emitter, material, listener perspective and cue event ID to any sound. Detect impact/footfall from actual visual contact, not an arbitrary fixed musical beat. Use quiet deliberately if character perception requires it.

## Context-dependent directing variants (select, then adapt)
- **Threat:** Compress the decision window, establish source and plausible danger; protect spatial legibility. Sound can warn before image only if intentional.
- **Comedy:** Allow a readable expectation hold then a crisp surprise/recovery; keep the whole physical interaction in frame so the joke is visible.
- **Wonder:** Lengthen perception/reveal and provide stable scale cues; favor attentive gaze and less aggressive sound effects.
- **Tenderness:** Prioritize microgaze, gentle support and touch; quieter sound and restrained camera motion; do not force a spectacular accent.

## Body plan and size adaptation (review before copying motion)
- **tiny:** Reevaluate head-to-body ratio, limb reach, contact cadence, silhouette and mix perspective; do NOT uniformly shrink adult animation.
- **human scale:** Ground contacts and pelvis support remain explicit; check reach against shoulder/arm anatomy and world scale.
- **giant:** Consider greater turn clearance, step response, tail/appendage lag, camera scale cues and environment response; not a universal slow-down factor.
- **quadruped:** Replace biped stance schedule with verified bodyplan-specific multi-leg gait and spine/shoulder/hip motion.
- **winged aquatic limbfree:** Replace generic feet/IK assumptions with mode-appropriate support/propulsion; verify anatomy references.

## Failure patterns and safety checks
- **Common failed version:** Random head wiggle with no visual target.
- **Likely structural cause to investigate:** check causal ordering, foot/contact targets, layer occlusion, prop ownership, joint limits and camera geographies before adjusting effects.
- **Do not:** substitute shake/blur/flash or sound for the physical action, use generic timing as a universal law, or assume the example works on unrelated animals.

## Acceptance tests (NOT YET RUN FOR THIS PRESET)
- **Specific visibility condition:** Stimulus visible or intentionally audible: Ambience suddenly becomes quieter; Perception and decision visibly motivate action: Notices gaps in known animal sounds; Search for a hidden threat; Main event actually completed: Eye scan left-right; head catches up; step to clear obstruction.
- **Geometry:** at contact, world-space end-effector and target agree, with no unmotivated jumps/clipping (tolerance is project calibrated).
- **Acting:** silent normal-speed viewing can identify the trigger, intended action and consequence.
- **Camera:** audience knows actor/object geography before and after shot/cut.
- **Audio:** source/material/distance and event timing are consistent; listen separately.
- **Technical:** deterministic seek/render, stable actor IDs and asset scale.
- **Regression:** archive exact test clip, command, contact-sheet images, audio and review notes before L4/L5.

## Timing and implementation status
Example inherited phase schedule: 90 frames at 30fps, not universal. No implementation of this V8 adapted preset is claimed. Inherited media in V7 are schematic and do not independently validate this full production recipe.

## Missing evidence / research request
For a real creature obtain bodyplan-specific gait footage and measurements (GAP-003/004/011). For performance validation obtain silent audience testing (GAP-008), and for AE execution GAP-006. Revisit exact joint/control schema after reference research.
