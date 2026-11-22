# Layer architecture — how drawings acquire depth and behavior

**Source-backed overview:** [Adobe layer creation](https://helpx.adobe.com/after-effects/desktop/work-with-layers/create-layers/creating-layers.html), [parenting](https://helpx.adobe.com/after-effects/desktop/work-with-layers/layer-properties/layer-properties.html), [precomposing](https://helpx.adobe.com/after-effects/desktop/work-with-compositions/precomposing-and-nesting/precomposing-nesting-pre-rendering.html), [track mattes](https://helpx.adobe.com/after-effects/using/track-mattes-and-traveling-mattes.html), [shape layer operations](https://helpx.adobe.com/after-effects/desktop/drawing-painting-and-paths/shapes-and-shape-attributes/shape-attributes-paint-operations-path.html).

| Tool/layer | Plain language | Good use | Bad use / pitfall |
|---|---|---|---|
| **Solid** | An arbitrarily sized single-color pixel surface on which to paint effects or make masks | Background color, control image for displacement, shockwave/flash under masks, effects requiring an input | A flat rectangle used as a substitute for properly articulated character anatomy |
| **Shape layer** | Native vector paths whose geometry, fills, strokes, Trim Paths and Repeater can animate | Manga speed lines, water streaks, projectile trail, motion arcs, portal rim | Using a thousand hand-placed vector shapes when one controlled path/repeater suffices |
| **Artwork/PSD/AI layers** | Independent images at different depths, often split into body parts and scenery | Head, torso, limbs, near/far foliage, parallax landscape | Keeping whole character in one image if bends and contacts matter |
| **Null** | Invisible control object for parenting and coordinated movement | Root actor position, pelvis, target gaze, camera rig, speed-line direction | Putting character motion only on root without articulated pose animation |
| **Adjustment layer** | A compositing effects layer affecting the accumulated image below it in stacking order | Short scene-wide color accent, local glow/blur within a mask | Applying it unintentionally to captions or all layers, creating flicker or legibility loss |
| **Track matte** | One layer uses another layer's alpha/luminance to determine visible parts | Character emerging through doorway, bullet crossing behind a foreground object | A mask that moves independently and clips objects without a physical cause |
| **Mask** | Bounds visibility/effects within a path on a layer | Portal aperture, controlled spill, silhouette reveal | Hard-edged clipping that fails on motion blur/antialiasing |
| **Precomp** | Many layers packaged as one reusable composition | Actor rig, particle cluster, camera insert, impact visual group | Precomp nesting that unintentionally breaks 3D depth, transform order or motion blur |
| **3D layer** | A flat card in a 3D scene with position/rotation/depth; 2.5D staging | Multi-plane parallax, camera dolly, foreground/background size changes | Mistaking flat cards for full volumetric models |
| **Camera layer** | A view through the composition's 3D space | Motivated dolly, follow, rack focus in 2.5D | Camera zoom used as a replacement for character blocking |
| **Audio layer** | Footsteps, source sounds, ambience, music and stem references | Cue-based emotional/factual sound context | Assuming sound is automatically synchronized because it is on the timeline |

## How a 2D paper-cut character becomes alive

1. Split artwork into front/back hands, feet, arms, shins, thighs, torso, eyes, jaw, hips, and tail as applicable.
2. Align each layer's anchor point at the **physical pivot**, not its visual center (knee near joint, tail base at root).
3. Parent joint children sensibly; use nulls for actor root, pelvis, hands and gaze target.
4. Animate **silhouette key poses first**, then joint rotations and root spacing. A child should inherit movement while preserving local poses.
5. Animate contact separately: hand touching egg, foot planted on ground, body entering aperture. Parenting alone **does not** create inverse kinematics or contact locking.
6. Apply deformation (Puppet Pins or shape paths) for flex and flesh, not to conceal impossible joint angles.
7. Add overshoot/settle/secondary motion only after coherent poses and contact exist.
8. Use layered foreground/environment reactions to create depth and material response; inspect screen direction and screen-safe area.

## Solids in our concrete use cases

- **Portal**: dark-blue solid/shape as back interior, masked reveal, animated irregular rim as shape layers, optional colored/blurred duplicates; separate near rim to occlude the actor while crossing and separate far rim behind.
- **Projectile insert**: a narrow blurred solid or masked shape for composited streak, a vector silhouette for the actual projectile, and separate camera rig; don't fake the projectile's location by moving only the background.
- **Impact accent**: limited-duration pale-colored solid/shape with controlled opacity and mask. Do not alternate large full-frame flashes repeatedly.
- **Water stylization**: separate distortion/displacement control layer and ripples; particle wake should be attached to the projectile's path if the scene is actually underwater, otherwise treat as a visual metaphor.

## Failure classes

- **Paper-doll skating**: root slides but foot and hips don't transfer weight.
- **Mismatched z-order**: character appears on top of portal rim even while supposedly behind its plane.
- **Puppet rubberiness**: whole figure stretches where hinge articulation is required.
- **Unbounded FX**: shockwave/glow covers the important pose or reaction.
- **Hidden continuity bug**: camera insert changes geographic screen direction after the cut.

Record the node/layer graph and literal names with each shot so another agent can reconstruct or debug the composition.
