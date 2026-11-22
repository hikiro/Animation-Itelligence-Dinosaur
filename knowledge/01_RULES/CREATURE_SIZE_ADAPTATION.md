# Creature type, size and anatomy adaptation — rig and motion rules

**First identify body plan, locomotion and scale.** A character is not made convincing by uniformly scaling a human walk cycle.

## Anatomy decision tree
1. Number and placement of support appendages: biped, quadruped, hexapod, many-legged, limbless, aquatic, aerial or hybrid.
2. Joint architecture and allowed bending: plantigrade/digitigrade/unguligrade, wings, tail, fins, flexible trunk, tentacles.
3. Mass distribution and body center: head/torso/tail/limb proportions, cargo or prop changes.
4. Primary locomotion mode and terrain: walk, trot, bound, glide, fly, swim, slither, hop, crawl; model contact phase pattern.
5. Acting requirements: face, gaze, shoulders, ears, tail and breathing as expressive channels.
6. Screen scale and shot type: tiny close-up vs enormous wide shot; visibility and timing constraints.
7. Physically plausible or deliberate stylization: declare allowed squash, suspension, step exaggeration and weightless beats.

## Class-specific baseline recipes (research hypotheses, adjust using observational reference)
| Class | Rig focus | Locomotion and contacts | Acting cue | Common failure | Verify |
|---|---|---|---|---|---|
| Human/humanoid biped | pelvis, spine, knees, ankles, foot roll, fingers | alternate foot stance, pelvis over support | gaze leads head and torso | moonwalk; rigid knees | planted-foot track, readable gaze |
| Tiny biped hatchling | short limbs, large head, tail balance, eye shape | small unsteady steps or hops, frequent recovery | head tilts and blinking | adult gait simply shrunk | support changes and silhouette |
| Giant bipedal dinosaur-like (fictional) | heavy pelvis, long tail, head/neck, hindlimbs | long stride, torso sway/inertia, braking steps | head/tail delay, cautious turns | tail rigid, support impossible | foot plants, COM plausibility, tail clearance |
| Mammalian quadruped | spine, shoulder blade/forelimbs, hip/hindlimbs | species-specific gait phases; multiple alternating supports | ear/neck/head | same phase for four feet; biped cycle | grounded four-foot timeline |
| Long-neck quadruped | shoulder/hip stability, flexible neck with limits | slower turn envelope, body/neck compensation | neck orientation before body | impossible neck/tail clipping | joint limits/clearance |
| Bird / winged actor | shoulder complex, wings, tail/rudder | perch/hop/takeoff/flap/glide/land as distinct states | head stability, wing preparation | flapping unrelated to lift | takeoff/landing contact and phase |
| Fish / aquatic actor | spine waves, fins, tail thrust | swim curves depend on species and water resistance | body/orientation/fin accents | ground-walk keyframes underwater | continuous propulsion and drag |
| Snake / limbless actor | spline body, head and lateral body segments | distributed deformation and contact with terrain | head leads, body follows | rigid pipe dragged by head | self-intersection and body trail |
| Insect / six-legged actor | thorax/abdomen and six independent legs | tripod/other gait with stable supports | antennae/head | all legs lift at once | contact schedule and stability |
| Soft-bodied/tentacled | distributed deformer/spline chains | reach/grip with soft volume/length rules | curl, compression | appendage clipping and length popping | contact continuity and silhouette |

## Size is more than a numeric scale factor
- **Change mass cues:** relative inertia, stride cadence, compression, environment response and score/foley perspective; never apply a universal "big means slow" law without assessing behavior/style.
- **Change joint and deformation design:** a huge rigid body, tiny springy body, feathered wing and rubber creature require different deformation controls.
- **Change camera and staging:** low angle can emphasize scale; a wide shot maintains geographic comprehension; an extreme close-up can lose environmental reference.
- **Change sound:** footsteps depend on contact material, force, shoe/foot anatomy, acoustic space and microphone position—not just pitch shifting a sample.
- **Change target visual read:** tiny actor details may need larger silhouette gestures; giant actor may need extra time for the viewer to track whole-body motion. These are directional hypotheses to test.

## Scaling experiment matrix
For the **same event** (plant foot → stop → look), compare actors of relative heights 0.4×, 1× and 4× using consistent world units and framing variants. Instrument foot drift, support duration, reach length, apparent acceleration, shadow/contact and audio sync. Ask independent reviewers which appears heavier and why. **Proposed test, NOT YET RUN.**

## Evidence and caveats
SRC-011 and SRC-012 discuss animal/gait anatomy; SRC-002, SRC-004 and SRC-013 explain story-led rigs; SRC-005–SRC-009 describe controls. They do not certify extinct-animal gaits, universal body-mass scaling laws, or the specific recipes above. **Prioritize real reference video, biomechanics and silhouettes for the selected creature.** Open requests are logged in `02_RESEARCH/ACCESS_GAPS.md`.
