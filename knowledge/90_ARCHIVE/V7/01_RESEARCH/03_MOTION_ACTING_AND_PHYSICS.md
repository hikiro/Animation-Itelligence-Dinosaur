# Animation performance and physical plausibility — context-sensitive direction

**Research links:** S03/S16/S17/S18 in `00_SOURCE_LEDGER.md`. **Do not conflate** realistic physics with expressive animation: stylization can exaggerate mechanics, but it must preserve intention, contact, force and readable consequences.

## The character is making decisions, not moving coordinates

For every action record this chain:
`trigger -> noticed (eyes/head) -> interpretation -> goal -> anticipatory pose -> force/trajectory -> impact or threshold -> settling -> changed state`.

Example: human hears roar (trigger) → pupils jump toward dinosaur → head turns → sees mouth opening → weight shifts away → trailing foot pushes off → full-body pivot → fleeing stride → heart-racing breath → ongoing goal “protect egg while escaping”. If the code starts `human.x -= speed` without those poses, the animation may be mathematically smooth but dramatically wrong.

## 12 principles: how to use rather than recite

| Principle | Main intention | Portal/chase practical rule |
|---|---|---|
| Squash & stretch | Convey force and material | Subtle compression on foot contact; portal rim flexing, not skeleton distortion |
| Anticipation | Prepare viewer for action | Gaze and shoulder turn before human push-off; mother inhale before roar |
| Staging | Make one idea readable | Silhouette portal crossing and full foot plant kept visible |
| Straight-ahead / pose-to-pose | Control spontaneous detail vs key intentions | Primary contact poses keyed; leaves/tail secondary procedural |
| Follow-through/overlap | Inertia and hierarchy | Tail/head continue after dinosaur root stops |
| Slow in/out | Show effort and settling | Human cautious step slows at plant, heavy dinosaur acceleration staged |
| Arcs | Natural motion paths | Arms catch egg along curved reach; dinosaur head lower along arc |
| Secondary action | Support primary narrative | Blink, breathing and rustle only if main action remains clear |
| Timing | Weight, mood, characterization | Human fast, mother heavy; reunion held longer than chase inserts |
| Exaggeration | Emphasize intent | Huge eye reaction to baby and restrained squash for comedy |
| Solid drawing | Coherent volumes and rigging | Continuous limb lengths, anatomical pivots, 2.5D depth ordering |
| Appeal | Readable, engaging design/acting | Clear silhouettes, consistent face language, not excess complexity |

## Full-body response test

A movement should have a coherent chain of force: `foot → ankle → knee → pelvis → torso → shoulders/head/arms`, or `hands/catch → arms → chest → hips/feet` depending on contact. The 80 Level example emphasizes this for a jump: moving just the model up is not equivalent to animating a jumping performance. Apply same principle to bracing against roar, stopping in a chase, and receiving egg momentum.

## Locomotion specs

### Walking

Define contact, passing and recovery poses; choose stride frequency according to root speed and style; preserve planted foot in world coordinates during stance. Swing foot may move relative to body; planted foot cannot. Hips transfer weight, shoulders counter-rotate, torso stabilizes gaze, foot lifts clear before forward arc.

### Running

Show lean and acceleration, stride and cadence dependent on speed, flight/contact distribution appropriate to design, arm swing with body balance, head stabilization and breathing. During high speed, blur/spacing may be stylized; do not mask pose popping.

### Dinosaur heavy gait

Use wide support stance, large stride inertia, center-of-mass motion, pelvis and chest movement, delayed tail/head response. The tail is not a decorative sine wave independent of direction changes. Synchronize camera tremor/grass and foot sound to *world-space* contact events.

### Turning/stopping

Eyes aim toward a goal; head starts; chest and hips rotate; leading foot plants in new direction; weight shifts; the trailing limb follows. Stopping includes deceleration, recovery step or squat, and overlapping head/tail motion. A 180-degree instant sprite flip is a continuity violation unless it is an intentional one-frame graphic device explained in shot card.

## The portal is a 3D *event* inside a stylized 2.5D presentation

The portal is a plane that separates two spaces. Build a local threshold coordinate `crossingDepth` relative to portal plane; actor has **inside**, **crossing**, **outside** states. Need depth masking or physically correct near/far layer ordering: rear rim + aperture background behind actor's emerging body, front rim partially in front during threshold crossing, trailing torso/leg occluded until cleared. A human walking laterally beneath a floating portal is NOT crossing.

For the 9s entrance the order is head inside aperture → hand contacts/appears → torso projects through → leading foot crosses and plants on ground OUTSIDE → pelvis passes threshold → trailing foot crosses → full body settles outside. No step is allowed to appear by unrelated screen-edge translation. Portal's bottom is on same world ground plane as destination footprint.

## Object ownership state machine

Egg can be only in one primary state at a time: `NESTED -> ROLLING -> FREE_FALL -> TWO_HAND_CATCH -> HELD_CHEST -> CRACKING -> HATCHED_BABY_HELD -> BABY_FEET_PLANTED -> FREE_BABY`. The two hands take ownership at contact, not frames before; shadow, orientation and inertia follow parent transforms. At ground transfer, baby feet must establish contact before parent hand grip releases.

## Secondary environmental movement

- Every impact has cause, magnitude and decay. Mother footfall affects grass and pebbles nearest foot, not every tree simultaneously.
- Leaves displaced by a broken branch have varied arcs and settling; keep cutout proportions stable.
- Portal light may cast cyan highlight and shift nearby paper shadows, but never reverse the scene key without motivation.
- Use breathing, blinks and tail motion for life during holds; **never** randomize every component each frame.
- Paper-cut joint covers can be beautiful if elbows, knees and hip masses remain articulated; do not use them to hide detached limbs.

## Choosing motion energy from context

| Emotion | Pose/timing | Secondary action | Rejection |
|---|---|---|---|
| Curiosity | Lean, controlled cautious step, pauses to inspect | Small blink, breath, head tilt | Running entrance before any surprise |
| Focused rescue | Sudden eye fixation, clear bend/reach/catch/recovery | Fingers open/close, shell rattle | Egg snaps into hands |
| Fear | Compression/recoil, pivot, explosive takeoff | Breath, asymmetric arms | Human translates left while facing front |
| Pursuit | Dynamic acceleration, mother closing distance | Tail lag, foliage impacts | Loop gait at constant speed while root accelerates |
| Wonder | Motion decelerates, close attention to egg | Gentle micro head movement | Constant jitter during baby reveal |
| Reassurance | Open body posture, careful lowering | Slow nose nuzzle, subtle exhale | Mother switches anger to smile without baby recognition |
| Comic panic | Contrast between stillness and large sudden reveal | Eye widening, delayed head tilt | Every element simultaneously shakes |

## Operational QA

Frame sample contact events ±5 frames, direction changes ±8 frames, shot boundaries last/first 4 frames, portal crossing every 2–3 frames. Watch 1x and 0.5x and inspect world-space debug markers. Look for unnatural velocity jumps, joint inversions, missing contact forces, unintended deformations, depth ordering, scale popping and reaction-before-trigger. Render motion blur both off (for diagnosis) and on (for final judgement). A clean blurred frame does not excuse a broken base pose.
