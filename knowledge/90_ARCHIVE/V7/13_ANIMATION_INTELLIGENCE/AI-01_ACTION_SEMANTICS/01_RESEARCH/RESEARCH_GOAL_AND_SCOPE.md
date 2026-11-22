# AI-01 research charter and permanent seven-domain map

## Research question

Can we reliably translate a director's ordinary-language sentence into **the intended cinematic event** rather than a superficial keyword effect? Can the system retrieve previous validated evidence, compare alternative interpretations, and state honestly where its proposals are untested?

## Permanent stable domains (do not renumber)

| ID | Domain | Why relevant to AI-01 |
|---|---|---|
| AI-01 | Action semantics and character intention | Prose, nouns, adjectives, actors, awareness, belief, choices, observable actions |
| AI-02 | Physical mechanics and rigging | Constraints and body mass make the chosen action possible |
| AI-03 | Camera intelligence and perception | Camera must reveal enough evidence, from an intentional audience POV |
| AI-04 | Sound-event intelligence | Sound source and point of audition influence meaning and comprehension |
| AI-05 | Code / expression engineering | Translate intended behavior into appropriate implementation, NOT vice versa |
| AI-06 | Automated and human QA | Prove cause, contact, readability, continuity and audio alignment |
| AI-07 | Style-specific motion grammar | Timing and accent style can change; causality remains comprehensible |

## What the dataset must contain

Individual terms (verbs, adjectives, adverbs, nouns, onomatopoeia), multiword creative directions, story actions, cinematic shot vocabulary, acoustic events, actors and entities, modifiers, and negative instructions. Each has a **context of use**: actor and goal, environment, timeline, physical feasibility, who knows what, emotion, medium/style, audio perspective, visual audience needs, optional uncertainty.

A corpus is **not sufficient** merely because it has many rows. The training/evaluation split must prevent same-lemma leakage; natural source examples must remain separate from authored and generated cases; tests must include hard ambiguities and contradictory requests.

## Demonstration case: a dinosaur's foot lands by a human

Same cause and physical contact; three meanings:

- **Threat**: audience connects heavy foot to danger; character stiffens then recoils; a low camera angle establishes scale; transient and low-frequency body of footfall, ambience dip, source direction intact.
- **Comedy**: audience gets stable wide geography; a delayed double take makes the joke; tiny squeak or deliberate audio gap contradicts large physical mass without erasing contact.
- **Wonder**: character slowly discovers enormous animal; camera follows the gaze upward; softer musical/harmonic emphasis allows awe while keeping physical footstep credible.

**Important:** In this module the *fourth* context, tenderness, probes affectionate/careful movement and acoustic intimacy. Context presets are hypotheses, not automatically correct for every scene.

## Future data collection priorities

1. Pair scripts with drawings and animatics of the **same** accessible project; report asset-level rights.
2. Code manually annotated, real production shot pairs before increasing synthetic template counts.
3. Add audience-comprehension studies with clearly described cohorts and questions.
4. Expand language coverage (regional vocabulary, non-English prompts, gesture and acoustic onomatopoeia) without falsely presenting translations as validated.
5. Add real rig events and sound measurements when actual files exist.

## Non-goals

We are not training a model from copyrighted screenplay text or redistributing third-party storyboard images. The examples are *our own designed records*, except the explicitly sourced brief observations. We are not claiming all production methods or emotional meanings are universal.
