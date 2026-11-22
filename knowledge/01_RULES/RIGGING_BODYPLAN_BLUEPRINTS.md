# Rigging blueprints for different body plans (reference-driven)

**Status:** authored implementation guidance L2, with underlying rig principles supported by SRC-002, SRC-004–SRC-013. No rigs in this file have been production-rendered and approved. A character rig should be designed for the performances required in the script, not copied from an arbitrary humanoid template.

## Common coordinates and event states

Every actor defines: `world_root`, `body_root`, `COM_target`, named joints, joint limits, rig controllers, contact end-effectors, a stable world scale reference, action state, gaze targets, dynamic appendage controls and material/deformation layers. World position cannot be silently merged into camera transforms. Contacts use world-space targets or baked contact trajectories. Animated prop ownership states are `world`, `shared`, `actor.socket`, and `released`, with explicit transfer events.

## Blueprint A — humanoid biped

Suggested hierarchy: `world_root → pelvis → spine_0 → chest → neck → head → eyes`; `pelvis → L/R hip → knee → ankle → ball → toe`; `chest → shoulder → elbow → wrist → hand`. Controls: pelvis and head FK, gaze look-at, knee poles, heel/toe foot roll, IK/FK hands, world/local space switches, one-foot support and two-foot support transitions. Test walk, run, stop, pivot, recoil, reach, catch, kneel, and portal straddle. *Common failure:* moving root x across ground with cycling legs but no foot locking. *Fix:* contact schedule before keyframe polish.

## Blueprint B — large biped with tail (fictional dinosaur-like)

Suggested hierarchy: `pelvis → left/right hindleg`, `pelvis → multiple spine/chest joints → neck → head/jaw`, `pelvis → tail_base → tail segments`. Tail is a delayed control chain, not a rigid counterweight keyed independently of hip turn. Choose whether forelimbs grasp or gesture; don't make them behave as hidden legs. A heavy stop uses gait-support sequence, deceleration, hip settling, neck and tail follow-through. Check head-to-hip turn clearance and tail-to-environment intersections. *Reference caveat:* living animals and reconstructed extinct-animal movement are analogies, not measured behavior of a fictional dinosaur.

## Blueprint C — quadruped mammal

`world_root → chest + pelvis` through a deformable spine; each foreleg and hindleg gets its own IK target and bend direction; head/neck and tail may have FK/IK assist. A gait table records contact onsets, lift-offs and swing phases. Different animals use different phase relationships and joint types; research animal-specific reference. Avoid translating a two-foot biped walk to four legs or forcing all legs to contact simultaneously. Compare: standing support, start, steady gait, turn, slow stop, look down, rear back. Test two- and three-dimensional support geometry according to movement mode.

## Blueprint D — winged bird

Model torso/chest, shoulder/scapular attachment, upper wing, elbow/wrist equivalents, flight-feather silhouette (as layered mesh or discrete poses), tail and articulated feet. Separate ground/perch states from airborne states; takeoff must include push-off and landing must end in supported feet. Wing pose requires a silhouette check at each extreme; test full span against camera and other actors. Airborne motion must have a sustained propulsion/glide model appropriate to genre; a wing flap alone does not imply coherent flight.

## Blueprint E — fish and aquatic creatures

Use a flexible body spline with caudal fin and species-appropriate paired fins; coordinate traveling deformation with direction and speed. Model water-depth coordinates distinct from camera transforms. Transition from forward swimming to turning by bending the traveling wave, not rigidly rotating the whole actor. Interaction audio should represent water perspective rather than terrestrial footfalls. Test volume preservation and no self-intersections or abrupt fin flips.

## Blueprint F — snake or limbless body

Represent centerline curve and adaptive local frames with ordered samples along body length. Head leads toward goal; trailing body follows a time-/distance-dependent path with contact/collision constraints. Prevent abrupt shape discontinuities, surface penetration and tail teleportation. A simple chain of rotations may need a spline solver or procedural deformation at high curvature; test at tight turns and in obstacles.

## Blueprint G — insect or multiple-legged creature

Separate thorax, abdomen, head and each leg chain. Define contact groups and gait phase offsets; tripod gait is a useful *starting test* for some six-legged insects, not a rule for all species, speeds or terrain. Antennae and abdomen may convey curiosity/threat while feet maintain balance. Test intentional turn, acceleration, obstacle traversal and whether the support contacts allow the body to remain plausible.

## Blueprint H — soft-bodied or tentacled creature

Replace rigid skeleton assumptions with splines, cage deformers or distributed controls. End tips may use IK targets while length/volume constraints and contact states keep appendages from teleporting. Grasping is contact propagation, wrap, load transfer and release—not only tip proximity. Check for mesh intersections and unintended length pops.

## Scaling checklist (every blueprint)

1. **Proportions:** change head, torso, limb and appendage ratios, not simply `scale(4)`.
2. **World coordinates:** preserve real floor/prop positions after size change; reevaluate reachable targets and step clearance.
3. **Timing and rhythm:** re-block anticipation, stride and settle for anatomy, motivation, genre and actual visual framing; no universal mathematical slowdown.
4. **Camera:** establish relative size using props, terrain and shot coverage. An extreme close-up without environmental reference does not demonstrate magnitude.
5. **Audio:** foot/wing/water emitter changes material, source size and listening perspective; do not assume one pitch-shift suffices.
6. **QA:** actual contact targets, joint legality, body intersections, shape volume, silent audience perception and audio event alignment.

## Reference protocol
Use `02_RESEARCH/REFERENCE_STUDY_PROTOCOL.md` for video observations and data rights. Link each rig decision to a species/model photo/video, timecode and its confidence. Source documents: `02_RESEARCH/SOURCE_LEDGER.md`; source gaps: `02_RESEARCH/ACCESS_GAPS.md`.
