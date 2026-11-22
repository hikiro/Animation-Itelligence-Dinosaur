# Rigging foundations — anatomical and performative design

## Start with needed acting, not generic bones
The rig exists to support the script: Can the character look, reach, grab, shift weight, turn, recoil, roll, nuzzle, breathe, and occupy the portal's depth? List required poses and contact events before choosing skeleton complexity. SRC-002, SRC-004 and SRC-013 support performance-led rig design.

## Minimal rig specification
- Actor-local coordinate frame and independent world root; stable, documented scale units.
- Hierarchical joints with correct pivots and rotation constraints; rest pose and deformer/layer coverage.
- Root/center-of-mass control separated from visual torso bounce and camera transform.
- FK controls for expressive arcs, IK effectors for contact targets; pole/bend controls to avoid flips.
- Explicit contact states: `free`, `approaching`, `supported`, `releasing`; world vs attached object ownership.
- Eye-gaze + head-target + chest orientation, not one rigid body translation.
- Deformation/overlap controls for tails, wings, ears, fabric and mass, with silhouette review.
- Robust 2D depth ordering: front and back limbs, nested paper layers, portal interior matte and front rim.
- Animator-facing named parameters; avoid giant undocumented controller lists.

## Core validation poses
Neutral; four silhouette extremes; left/right look; compression/extension; all relevant foot stance extremes; turn; hand target; reach at maximum legal extension; interaction with main prop; fast stop; overlap after motion; portal threshold straddle for DINO.

## FK vs IK
FK: rotate a joint hierarchy for arcs and natural overlap. IK: position target (foot or hand) while solving chain joints. Use IK for planted stance or grip; FK for expressive follow-through or flying appendages. Blending must preserve pose and avoid pop at switch. SRC-005–SRC-009.

## Common faults
Knees flip due to missing pole vector; bone length changes accidentally; hip moving while foot slides; hand object and wrist target disagree; tail crosses torso; root/pose/camera movement double-applies; perspective changes alter perceived rig scale; masks place the leg on the wrong side of the portal rim.

## Production test and source separation
Automated joint limit and FK/IK distance tests are L3 at best. Rendered pose/playback inspection is L4. Species anatomy assumptions require reference and cannot be inferred from fictional anatomy alone. Autodesk (SRC-005–SRC-009) documents tools, not proof of our implementation.
