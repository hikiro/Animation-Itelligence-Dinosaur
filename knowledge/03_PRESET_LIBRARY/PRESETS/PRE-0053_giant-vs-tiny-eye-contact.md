# PRE-0053 — A giant creature notices a tiny character

**Category:** Creature / scale  
**Tags:** creature / scale, giant vs tiny eye contact  
**State:** `designed_unverified` (L2: authored recipe; not approved animation)  
**Principle/source support:** SRC-002, SRC-011, SRC-012 (sources support methods, NOT proof this exact preset renders correctly)  

## Human-language instruction and viewer goal
**Instruction:** A giant creature notices a tiny character.  
**Audience should understand:** A giant creature notices a tiny character.

## Required scene context
Fill before execution: **actor identity and anatomy**, **relative scale**, **prior pose and velocity**, **who perceives the trigger**, **character goal/belief**, **audience knowledge**, **world/terrain/material**, **style/realism exception**, **camera axis/frame**, **sound source/listener**, **preceding and following shot**. Do not silently infer omitted critical constraints.

## Causal event graph — editable
1. **Stimulus / setup:** Establish safe spatial relationship and size
2. **Perception:** Actor/viewer identifies relevant stimulus within staging
3. **Interpretation / decision:** Goal or emotional response is chosen consistently with scene context
4. **Anticipation / preparation:** Appropriate support, gaze, or controlled pre-action state prepares visible action
5. **Visible action and contact:** Giant gaze lowers, body/neck adjusts, tiny actor responds
6. **Consequence and recovery:** After-state changes visibly, preserving contacts and continuity. Confirm the new state persists in subsequent shot.

## Rig, mechanics and interaction plan
**Suggested controls:** Two rigs of different scales, eye targets, foot supports. Define world-space root, joint pivots, contact target(s), support phase, body mass/center of motion, transfer of held props, overlapping appendages and legal movement ranges. Select IK only when a limb endpoint must meet a goal; do not use an expression-only shake as a replacement for rig/contact.

## Camera and editorial direction
Two-stage wide for scale then eyeline insert. State the viewer question and where the audience should look; preserve axis/scale and contact visibility. Camera trajectory is independent from object trajectory and cannot conceal missing actions.

## Audio and music direction
Giant breaths and tiny reaction within shared acoustic space. Attach a source emitter, material, listener perspective and cue event ID to any sound. Detect impact/footfall from actual visual contact, not an arbitrary fixed musical beat. Use quiet deliberately if character perception requires it.

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
- **Common failed version:** Cut removes scale reference before relationship established.
- **Likely structural cause to investigate:** check causal ordering, foot/contact targets, layer occlusion, prop ownership, joint limits and camera geographies before adjusting effects.
- **Do not:** substitute shake/blur/flash or sound for the physical action, use generic timing as a universal law, or assume the example works on unrelated animals.

## Acceptance tests (NOT YET RUN FOR THIS PRESET)
- **Specific visibility condition:** Both eye targets align in world-space.
- **Geometry:** at contact, world-space end-effector and target agree, with no unmotivated jumps/clipping (tolerance is project calibrated).
- **Acting:** silent normal-speed viewing can identify the trigger, intended action and consequence.
- **Camera:** audience knows actor/object geography before and after shot/cut.
- **Audio:** source/material/distance and event timing are consistent; listen separately.
- **Technical:** deterministic seek/render, stable actor IDs and asset scale.
- **Regression:** archive exact test clip, command, contact-sheet images, audio and review notes before L4/L5.

## Timing and implementation status
Choose from performance/action readability; no universal frame counts. No implementation of this V8 adapted preset is claimed. Inherited media in V7 are schematic and do not independently validate this full production recipe.

## Missing evidence / research request
For a real creature obtain bodyplan-specific gait footage and measurements (GAP-003/004/011). For performance validation obtain silent audience testing (GAP-008), and for AE execution GAP-006. Revisit exact joint/control schema after reference research.
