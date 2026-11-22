# Context-first action grammar — from text to directing decisions

## Context state model

Treat a brief as an incomplete state record, not an effect command.

```json
{
  "actor": {"id":"HUMAN", "current_goal":"protect egg", "belief":"dinosaur may attack", "emotion":"alarm", "physical_state":"holding egg, planted foot"},
  "others": [{"id":"MOTHER", "belief":"human stole egg", "goal":"recover egg"}],
  "trigger": {"type":"dinosaur foot ground contact", "world_time":"shot beat t0", "origin":"offscreen right", "visible":true},
  "world": {"ground_plane":"forest", "egg_owner":"human hands", "portal":"open", "blocking":"human left of mother"},
  "viewer": {"knowledge":"egg was rescued", "must_infer":"mother misunderstands", "point_of_view":"near human"},
  "aesthetic": {"medium":"2.5D cutout", "tone":"threat", "realism":"stylized grounded physics"},
  "output": {"format":"storyboard + animatic + event list", "duration_s":4}
}
```

Unknown fields remain unknown; mark `MISSING` rather than silently assigning facts. Different actor beliefs and audience knowledge can yield radically different direction from identical literal action.

## Typed event graph

- `STIMULUS`: physical or social event in world.
- `PERCEPTION`: sensory evidence reaches actor (may be delayed, masked, mistaken).
- `INTERPRETATION`: meaning actor assigns; explicitly separate from objective truth.
- `INTENT`: actor's immediate choice and priority.
- `PREPARATION`: changing posture, gaze, breath, body loading **only where appropriate**.
- `ACTION`: continuous visible performance with goal.
- `CONTACT`: causal crossing, touch, support, impact, handoff when required.
- `CONSEQUENCE`: environment and other characters' response.
- `RECOVERY`: balance, emotional change and new scene state.
- `AUDIENCE_INFERENCE`: what viewer can understand after seeing/hearing evidence.

These are graph *node types*, not a mandatory fixed-duration formula: surprise reflexes may bypass conscious decision; characters may act before becoming aware; comedy deliberately delays recognition; suspense may hide source from viewers without hiding it from actors.

## Word classes and what they do

- **Verbs** specify candidate state transitions (`reach`, `notice`, `leave`, `protect`). Do not assume completed contact from `reach`.
- **Nouns** identify actors, props, sound sources, surfaces, stakes (`egg`, `threshold`, `thud`). A noun may refer to narrative concept rather than physical prop (`reunion`).
- **Adjectives and adverbs** modify meaning, intensity, style, scale or timing, dependent on noun attachment (`heavy foot` ≠ `heavy pause` ≠ `heavy bass`).
- **Onomatopoeia** gives perceptual sound *intent* (`THUD`, `plink`), not a licensed sample or universal acoustic recipe.
- **Camera directions** encode a viewpoint transformation or editing decision (`push in`, `cut to`, `hold`); they do not transform world geometry without explanation.
- **Negative directives** constrain outcomes (`no slide`, `no camera shake`); never ignore them because an effect preset contains it.

## Compiler pipeline

1. **Parse:** actor, action, modifier, target, location, cause, goal, physical stakes, and negative constraints.
2. **Search:** source observations, past cases and synonyms. Note evidence level.
3. **Disambiguate:** produce multiple possible readings for polysemous terms. Resolve with grammatical attachment and story context; ask only when a missing distinction is indispensable.
4. **World-state audit:** where are actors? who holds what? what can touch/cross? what has viewer already seen?
5. **Graph:** produce causal typed events, temporal partial order and explicit completion condition.
6. **Direct:** choose gaze/pose, camera reveal and point of audition from audience goal. Keep source orientation.
7. **Plan code:** identify rigs, constraints, camera channels, animatable properties and required audio event triggers.
8. **Render evidence:** only if actual code/tool exists; a good description is not visual proof.
9. **Review:** sound-off story clarity; audio-only information audit; frame-by-frame contacts; context match.
10. **Record:** log source, assumptions, variants, rendered results, defects, decisions and regression tests.

## Context-dependent examples

**“Make the stomp heavy.”**
- If `heavy` modifies physical mass: slow support transfer, compression of ground/grass, torso inertia, appropriate body follow-through.
- If it modifies audio: dense low-frequency body paired with clear contact transient; don't overdo subbass for phone playback.
- If it modifies editing rhythm: hold around reaction to give event weight; not necessarily a slower foot.
- If the style is comedy: timing may contrast massive body with a small squeaky accent, without making the foot physically weightless.

**“Make the bullet travel in a curve.”**
- Check whether the user wants a curved *physical path*, curved *camera path*, *speed ramp*, or *graphic trail*. Do not invent ballistics or time-of-flight from adjectives. Treat impossible visual effects as explicitly stylized, and show clear source → travel → contact → consequence.

## Conflict strategy

Classify conflict as `PHYSICS_vs_STYLE`, `AUDIENCE_KNOWLEDGE`, `SCREEN_DIRECTION`, `AUDIO_PERSPECTIVE`, `LOCKED_STORY`, or `UNVERIFIED_CAPABILITY`. Record alternatives, preserve intent, choose justified interpretation, update `CONFLICT_LOG` before production changes. A future agent must never claim a prompt alone makes a physical action happen.
