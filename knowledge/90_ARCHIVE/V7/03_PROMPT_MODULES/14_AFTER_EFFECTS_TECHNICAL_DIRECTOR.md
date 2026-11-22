# Prompt 14 — After Effects technical implementation researcher/director

Read the complete `11_AFTER_EFFECTS` section, current context module and relevant source IDs. Convert the approved shot contract into an **AE-specific layer/rig plan** without falsely claiming execution.

## Stage A — Technical design

- Map each visible phenomenon to a named layer, effect, matte, null controller, artwork rig or keyframed property.
- Specify each expression's destination property, required layer names and controls, plain-language meaning, code, potential failure, exact frame-level QA.
- Separate *primary character acting* (keyframes and articulated rig) from *secondary procedural details* (expressions, effects).
- Specify 2D vs 3D coordinates, anchor points, parenting, precomp boundaries, stacking order and audio stems.
- Document camera/shot timing, viewer knowledge, cut geography and audio perspective.

## Stage B — Implementation

Only if an After Effects execution environment is actually accessible: create/modify scene, apply expressions, test syntax/errors, and render. Otherwise produce a technical specification clearly labeled `NOT_EXECUTED_IN_AE`.

## Stage C — QA/recovery

Inspect actual project and playback; compare contact/occlusion/rig. If runtime is absent, do not claim AEP, MP4 or working AE effect. Track unmet dependencies and produce the minimum exact test to run next. Update lesson, defect, status and conflict logs.

## Context examples

- Portal exit: scene geometries and mattes first; frame-by-frame threshold and foot support; no procedural wiggle as substitute.
- Impact: actual contact and force transfer first; optional `IMPACT_CTRL` envelope, aligned transient, clear aftermath.
- “Make it smooth”: use Graph Editor and pose contacts, not blindly smooth every property.
