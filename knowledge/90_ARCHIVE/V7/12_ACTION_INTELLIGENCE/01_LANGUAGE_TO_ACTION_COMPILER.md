# Creative-intent compiler: from words to a visible event

## Goal

Take everyday direction (“make her scared”, “the egg catch doesn't read”, “the camera feels cinematic”) and issue a reproducible, testable plan rather than a list of cosmetic effects.

## Deterministic interpretation algorithm

1. **Extract the verb, subject, object, goal and modifiers.** “Catch” implies an object trajectory and at least one converging grasp; “feel heavy” implies load-bearing and inertia, not merely slow motion.
2. **Look up prior lessons.** Search `12_ACTION_INTELLIGENCE/INDEX.md`, `10_KNOWLEDGE/INDEX.md`, `09_HANDOFF/DECISION_LOG.md`. Reuse known fixes, but check project status rather than infer success.
3. **Reconstruct the world and viewpoint.** Who is where, what is in view, who hears or sees what, and which details are deliberately hidden from the audience? Model spatial coordinates and the camera independently.
4. **Build a causal graph.** Stimulus → perception → decision → preparation → action → contact/release → consequence → recovery. Not every scene uses all phases: emergencies or offscreen reactions may omit or compress steps deliberately.
5. **Select primary animation mechanism.** Key poses, locomotion IK, layer masking, collision/parenting, object transfer, camera move, sound cue. Use expressions/spring/wiggle for controlled secondary effects only after primary geometry works.
6. **Choose style only after semantics.** Physics-informed believable, anime limited-action, paper-cut, comedy or realistic? Distinguish projectile arc, perceived curved motion from camera, time dilation, and graphic accents.
7. **Write blocking specification.** Event ID, frame schedule, actors/props, world positions, joint targets, screen axis, rig channels, Foley emitters and constraints.
8. **Create BAD and GOOD references.** “Bad” must isolate one failure (teleport, sliding foot, premature reaction) and “good” must fix that cause, not just increase gloss.
9. **Render, inspect and listen.** Test temporal order, contact truth, silhouettes, spatial continuity and acoustic perspective. Instrument numeric constraints where possible, but retain director-level human review.
10. **Record what actually happened.** Update the source ledger, `LEARNING_LOG`, `DEFECT_LOG`, `STATUS`, prompt revision and index; promote a technique to verified only with reproducible evidence.

## Decision table for ambiguities

| User phrase | Potential meanings | Decision / conflict policy |
|---|---|---|
| “Cinematic curve” | Object path curvature; camera arc; speed graph | Default to physically plausible object path + camera/retiming accent unless user locks magical curve. Flag any style deviation. |
| “Impact should be understandable” | Contact geometry; sound transient; body response; editor emphasis | Require contact/action chain first; accents are optional, not substitutes. |
| “More alive” | Acting, overlapping joints, environment response, extra idle animation | Prioritize actor intent and pose; never add constant jitter as fake vitality. |
| “Smooth” | No teleport; well-spaced motion; no harsh hold; blurred movement | Use velocity continuity only where appropriate; impacts can have deliberate sharp changes. |
| “Manga feeling” | Graphic compositional framing; halftone/cel texture; impact frame | Keep panel logic and readable geography; don't assume speed lines on every shot. |
| “Sound gets louder” | Source approaches; subjective alarm; mix emphasis | Record chosen interpretation in shot cue sheet; don't blindly scale sample gain. |

## Expanded beat template

```yaml
id: ACT-ID
intent: what the viewer must know / feel
source_world_state: precise coordinates, gaze, objects, ownership
stimulus: observable physical event or intentional offscreen cue
awareness: actor's information state and latency
preparation: anticipation / load-bearing or deliberately absent
primary: pose trajectories and contact states
secondary: overlap, force decay, environment response
camera: viewer information; shot, axis, size, move, cut point
sound: emitter, source/material, perspective, cue/onset, mix priority
style: allowed exaggerations and protected physical facts
pass_test: how a reviewer proves that action occurred
fallback_plan: what to simplify if rig or renderer cannot do it
status: PROPOSAL | TESTED_CODE | RENDERED | APPROVED
```

## Example: user says “I need the egg catch to read”

1. Viewer sees egg rock on edge → separate fall begins (do not teleport).
2. Human's eyes track its route → body loads → hands extend.
3. Egg and hands meet at a shared contact coordinate and frame.
4. Hands compress/retract under egg's momentum; ownership changes only at contact.
5. Character rebalances, checks egg; camera holds both contact and support feet.
6. The Foley emphasizes falling, contact, and retention, not disconnected effects.
7. Pass if all five narrative states are observable in the rendered shot, with no discontinuity in egg pose.

**What not to do:** `egg.style.transform = ...` alone is movement, not proof of a catch. The character's decisions, arm contact and prop state must be modeled.
