# PROMPT 02 — Paper-cut look development, model sheets and asset construction

## Required input

`02_STORY/04_ART_CHARACTER_SOUND_BIBLE.md`, `02_STORY/03_WORLD_ACTOR_PROP_STATE.md`, `01_RESEARCH/01_VISUAL_CAMERA_DIRECTION.md`, `01_RESEARCH/03_MOTION_ACTING_AND_PHYSICS.md`.

## Copy into agent

> Work as character art director, paper-cut puppet designer and technical rigger. Produce an asset specification for human, mother dinosaur, baby, portal, egg/shell, forest depth planes, nest/branch/root and apartment. Define original consistent character silhouettes from at least front/profile/three-quarter views if turns need them. Provide dimensions in a shared world-unit system; rig hierarchy with correct anatomical pivots; z-order and occlusion; facial expression sheets; hand grip points; foot sole and ground collision points; tail and head overlap controls; texture and contact-shadow rules. Design paper-joint covers as deliberate articulated overlapping layers, not as a way to conceal broken anatomy. Build portal as a passable depth plane: back rim, aperture interior and far-world, front rim and body-crossing mask. First test simple articulated pose transitions and portal-crossing debug geometry; do not move a single flattened sprite and call it a rig. Keep asset provenance, editable source, and light/palette continuity. Every output must be inspected at actual mobile view size and at full resolution.

## Deliverables

`MODEL_SHEETS.md`, `RIG_SCHEMA.md`, asset files in their real paths, `ASSET_MANIFEST`, scale proof contact sheet, first-frame portal depth diagram, test poses, and problems discovered. If image/design tools are unavailable, provide an honest construction specification and label assets not yet built.

## Reject if

Characters vary identity across scenes, portal cannot occlude a body, limbs are attached incorrectly, foot-contact point is not defined, egg lacks stable grip anchor, required facing direction is impossible, or 2.5D camera suggests views with no corresponding assets.
