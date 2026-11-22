# ANIMATION RULEBOOK — canonical V8

## Rule metadata
Every rule must state: **meaning**, **when**, **when not**, **mechanism**, **source/evidence**, **failure mode**, **test**, **known uncertainty**. General principles do not replace scene-specific judgment.

### R01. The action must actually happen
**Meaning:** A viewer must see the claimed action cross its real physical or narrative boundary. **When:** portals, doors, catching, lifting, handing off, colliding, landing, noticing. **Don't:** infer an action from a caption, sound or a nearby pose. **Mechanism:** pre-state → transition/contact → post-state, tracked actor/object IDs. **Sources:** SRC-001, SRC-016; V7 lesson LRN-0001. **Test:** silent viewers can identify the action and frame sequence proves contact/occlusion. **Uncertainty:** observer tests still needed for new presets.

### R02. Acting is motivated perception and decision
**Meaning:** Stimulus → attention → interpretation → intention → preparation → motion → consequence → response. **When:** all character-led beats. **Don't:** turn a head merely because the script includes a timestamp. **Source:** SRC-001, SRC-004. **Test:** can we say what the character sees, knows and wants at each pose? **Exception:** reflexes may precede deliberate awareness; document this.

### R03. Stage one dominant piece of information
**Meaning:** Control silhouette, screen direction, contrast, gaze and shot size around the audience's current question. **When:** reveals, action contact, emotional reactions. **Don't:** let decorative camera motion conceal essential action. **Sources:** SRC-001 and V7 cinematography materials (archival). **Test:** mute/thumbnail comprehension and eye-trace review. **Exception:** deliberate ambiguity for suspense must be resolved.

### R04. Physical contacts are world-space events
**Meaning:** A support foot, gripping hand or colliding surface must have a common world-space coordinate and time. **When:** stance, carry, push, stop, chase, portal threshold. **Don't:** fake gravity/contacts with decorative wiggle. **Sources:** SRC-005–SRC-010; V7 lessons LRN-0002/0011. **Test:** foot drift and prop-end-effector separation against scene tolerance; check full contact window. **Exception:** deliberately floaty styles still need internally consistent interactions.

### R05. IK and FK are tools, not art direction
**Meaning:** IK maintains goal-directed endpoints; FK gives clean rotational arcs; hybrids can be used within a shot. **When:** foot plant, grips, reaching, tail/head arcs. **Don't:** equate presence of IK with believable acting. **Sources:** SRC-006–SRC-009. **Test:** test target holding, joint limits, pole direction, transitions and silhouettes. **Exception:** a drawing replacement system may supersede conventional joints.

### R06. Mass is communicated by the complete response
**Meaning:** Momentum, stance width, stride timing, body compression, delayed appendages, environmental reaction and sound perspective jointly communicate weight. **When:** landing, charging, stopping, stomping. **Don't:** use arbitrary slow motion, huge camera shake or low bass as the only mass cue. **Sources:** SRC-001, SRC-011, SRC-012. **Test:** silent viewers perceive intended weight contrast; visible reaction after contact. **Exception:** comic exaggeration is intentional and flagged.

### R07. Creature type and scale change the rig and movement
**Meaning:** Anatomy and number/location of support limbs determine joints, centers of support, contacts, turn mechanics and timing. **When:** any non-human, child, giant, flying or aquatic actor. **Don't:** uniformly scale a human run cycle onto a quadruped or dinosaur. **Sources:** SRC-002, SRC-011–SRC-014. **Test:** anatomical reference comparison, support timeline, turn clearance, no stretching beyond rig limits. **Open:** species-specific reference acquisition still required.

### R08. Camera/motion/sound share a story purpose
**Meaning:** Each directs attention, conveys distance/force and reveals the correct event. **When:** every shot. **Don't:** insert automatic zoom/shake/whoosh simply because action happens. **Sources:** SRC-001 and V7 camera/audio study. **Test:** remove each effect; if comprehension improves, reconsider it. **Exception:** stylistic punctuation may be justified by genre.

### R09. Separate physically plausible, stylized, and impossible-within-world
**Meaning:** A curved camera path is not a curved object trajectory; a speed ramp isn't physical acceleration. **When:** action spectacle, anime, elastic paper-cut. **Don't:** assert artistic exaggeration as real-world mechanics. **Source:** user-approved distinction, V7 `INT-0001`. **Test:** document selected interpretation and consistent scene rules.

### R10. Timing is chosen for perception and emotion
**Meaning:** Hold key poses long enough to register, use anticipation and spacing to communicate force; frames depend on story and delivery format. **When:** all motion. **Don't:** treat cookbook frame counts as universal. **Sources:** SRC-001, SRC-010. **Test:** action reads at normal playback and on target device; no temporal discontinuities.

### R11. Effects are consequences, not replacements
**Meaning:** Roar, flash, rumble, debris and motion blur reinforce visible forces, never prove missing contact. **When:** any effects-heavy beat. **Don't:** mask a broken rig/collision with shake. **Sources:** SRC-003, SRC-016. **Test:** strip effects and check underlying character mechanics.

### R12. Evidence status always accompanies a claim
**Meaning:** A source link, a passed JSON validator, an encoded MP4 and a professionally approved animation are different accomplishments. **When:** research and release. **Don't:** label all 6,146 AI-01 corpus rows real observed action evidence; most are synthetic. **Source:** V7 manifest/learning log. **Test:** every preset contains status, evidence, known limitations and next validation step.

## Open rule questions
- How much stance-foot drift is acceptable for each art style and pixel resolution? Establish experimentally.
- Which creature-specific gait sources apply to invented dinosaurs? Separate reference animals and extrapolations.
- What read-time thresholds work for actual target viewers? Test before publishing global numbers.
- When can motivated camera disorientation outperform conventional continuity? Use controlled comparisons.
