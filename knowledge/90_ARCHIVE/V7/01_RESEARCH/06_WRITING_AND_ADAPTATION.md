# How to write story treatment, script, storyboards and animation prompts that survive production

A production prompt is not literature in command form. It is a layered specification connecting intention → observable event → executable action → evidence of completion. This document explains how another agent may expand scenes and preserve the original purpose.

## The six levels of writing

| Level | Question | Required artifact | Example |
|---|---|---|---|
| Logline | Why care? | One sentence with character, desire, obstacle, irony | Human rescues egg, mother mistakes him for thief |
| Treatment | What changes emotionally and causally? | Prose beats with motivation and reversals | Rescue creates chase; hatch reveals misunderstanding |
| Script | What exactly happens and is perceived? | Ordered scene action, dialogue/sound notes, no impossible simultaneous acts | Foot thud -> nest wobbles -> egg falls -> catch |
| Storyboard / shot cards | What does viewer see and in what order? | Shot size, axis, actor states, focal item, action completion, camera and edit | Full-body portal exit in held shot |
| Animation implementation | How is it executed in frames? | World positions, rigs, state machines, contacts, transforms, speed/easing, cues | Leading foot plant on marked frame; root over stance foot |
| QC contract | How can we disprove success? | Hard acceptance/rejection tests with evidence | Render proves pelvis and trailing foot pass aperture |

Do not skip intermediate layers: a prose treatment alone cannot tell an engine how to mask the portal; a body-position keyframe alone cannot communicate why a mother roars.

## Step-by-step treatment algorithm

1. **Premise:** protagonist, goal, obstacle, emotional promise, visual hook, surprise or reversal.
2. **Want/need/false belief:** human wants to explore safely; he needs to act compassionately despite fear. Mother wants baby safe; she falsely interprets egg-in-human's-hands as theft. Baby wants connection/safety and later follows rescuer.
3. **Cause-and-effect chain:** for each beat say **because X, character believes Y, therefore does Z, which causes W**. Any beat without “because/therefore” must be fixed or deliberately atmospheric.
4. **Plant and payoff:** portal size/flex planted early pays off in the mother's snout; baby's early connection to human pays off in choosing to follow; mother distracted by shell and delayed reaction explains failure to stop baby.
5. **Reversal:** egg hatch changes conflict from danger to reunion. Give silence/reaction time to make reversal felt.
6. **Ending:** a resolved emotional question (baby reunited) opens a new comic problem (baby follows and mother pursues). Avoid contradictory portal closure.
7. **Pacing:** map screen time to perception, acting, contact and reaction; do not make all 8 beats equal duration mechanically.
8. **Silent test:** can someone explain the events with no music, captions or dialogue? If not, rewrite actions.
9. **Sound test:** identify what viewers can infer before picture reveals it; define where audio is objective, subjective or editorial.
10. **Production test:** all decisive verbs require a visible event and test. If impossible with current rig, simplify the shot without altering the intended story.

## A cause-and-effect sentence generator

For each beat, write:
> When **[source event]** occurs, **[observer]** notices **[specific cue]**, assumes **[interpretation]**, and tries to **[goal]** by **[physical action]**. The action **[changes world/relationship]**, while the camera **[shows crucial evidence]** and sound **[conveys source or POV]**. It is complete only if **[viewer can see/contact proof]**.

Example: When a distant footstep shakes the nest, the human notices an egg roll toward the ledge, assumes it will break, and tries to save it by jumping with both hands. The egg collides with his palms and draws his arms down. A full/medium shot shows the falling path and catch while an approaching low thud gives the offscreen source of danger. It is complete only if egg leaves nest, contacts hands, and transfers momentum.

## “Action verb” checklist

- *Emerges:* from which plane? part-by-part in what order? what is occluded? where do feet land?
- *Notices:* eye direction, new information, reaction latency, body adjustment?
- *Runs:* direction, footfall, center of mass, speed, obstacle route?
- *Catches:* object incoming path, hand alignment, contact, attachment, recoil?
- *Roars:* reason, inhale, body contribution, target, human response?
- *Hatches:* visible crack, shell separation, actual body emergence, state transition?
- *Reunites:* safe release, baby movement, mother contact, emotional recognition?
- *Follows:* why choose to leave mother, what does mother know, crossing evidence?

If the prompt uses the verb but omits the proof, the agent may generate an attractive substitute that is **not the action**.

## Script guidelines for silent narrative short

- Write primarily **externalizable actions** instead of internal adjectives. Replace “he is curious” with “he leans out, scans left/right and tentatively places one foot on the ground.”
- Limit simultaneous dramatic information; if roar, egg and portal all move at once, a phone viewer may miss motivation.
- Establish screen geography before reassigning spaces. Reuse landmarks between cuts.
- Include reactive beats: “does X, stops, notices consequence, changes plan.” Do not animate unbroken effort with no cognition.
- Treat narration as an optional alternate edition rather than a crutch. The default film uses nonverbal sounds, not exposition.
- Distinguish aesthetic adjectives from implementation: “cinematic, smooth, dopamine-inducing” are goals; they require an observable camera/action/audio design.

## Modular prompt-writing pattern

Every prompt module should contain:

1. **Role/task:** specific department and output.
2. **Inputs:** approved story state, references, assets, shot IDs.
3. **Locks:** what not to change.
4. **Context:** viewer question, actor goal, emotion, stakes.
5. **Directions:** staging, movement, camera, sonic space, timing.
6. **Deliverables:** filenames/artifact types, debug views, metadata.
7. **Acceptance tests:** observable frames/events/listening.
8. **Failure loop:** what to do when evidence fails, how to update handoff.

Vague prompt: “Animate a man going through a magical portal smoothly with realistic sound.”

Production prompt: “Start with actor fully occluded behind interior aperture; between frames A and B reveal head then leading foot with consistent rim masking; foot contacts world ground, hips transfer over support, trailing limb clears; camera stays wide and stationary so threshold remains visible; portal opens with low shimmer while landing Foley occurs at recorded contact frame; capture sequential debug frames showing crossing; reject if person comes from screen edge.”

## Expansion authority: how another chat may add scenes

1. Copy story state table and define entry/exit states of new beat.
2. Show how new beat increases stakes, reveals information, deepens character, or prepares/payoffs later action. If none, cut it.
3. Update beat order, shot IDs, frame counts, props and ownership, geography, camera axis, cue sheet and QC checks.
4. Preserve the original emotional arc and story logic; adding more creatures/characters/vehicles just to fill time is not allowed without justification.
5. If changing runtime, use a new locked timing table. Avoid “we extended to 90 seconds” while leaving audio cues at original 80s.
6. Set a new evidence-gated benchmark for any new interaction mechanic not covered by original rigs/scene.

## Three creative concepts before a major new visual approach

Offer **three meaningful directions** (not cosmetic color swaps): e.g. tactile paper-puppet theatrical staging; layered cinematic documentary collage; highly graphic limited-animation comedy. Compare performance feasibility, camera vocabulary, sound identity, story comprehension, cost/risk. Pick based on user-approved visual style; do not switch aesthetics solely because it is easier to render.

## Common hallucination in treatment writing

- “Person comes out of portal” but the image shows him entering from offscreen: missing stage mechanics.
- “Mother forgives him” without any visible recognition: emotion stated, not acted.
- “Baby decides to follow” without mother distraction/child attention: missing intention.
- “Dinosaur almost catches him” while actual distance increases: wrong story measurement.
- “Epic sound design” with stock thuds on the beat: missing source and sonic perspective.
- “Cinematic camera” with zoom every two seconds: no specific narrative function.

## Writing-quality acceptance

A complete scene must allow a reviewer to reconstruct **who knew what, when they learned it, why they acted, what physically happened, where everyone was, what the audience was meant to see/hear, and what changed after the scene**. If any one cannot be answered, do not send it to full animation yet.
