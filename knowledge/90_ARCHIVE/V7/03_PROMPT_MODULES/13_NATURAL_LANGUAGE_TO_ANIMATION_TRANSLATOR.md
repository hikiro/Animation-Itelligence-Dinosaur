# Prompt 13 — Natural-language direction interpreter

**This module is reusable for any film, not limited to dinosaurs.** Before proceeding, read `00_START_HERE/06_EVOLVING_GOALS_AND_DIRECTIONS.md`, `07_CONFLICT_AND_INTERPRETATION_LOG.md`, `10_KNOWLEDGE/INDEX.md`, `11_AFTER_EFFECTS/06_CONTEXT_DRIVEN_TECHNIQUE_SELECTOR.md` and the appropriate prior scene/character state.

## Input

The human's ordinary statement (e.g., “make the bullet hit understandable,” “the dog jumps happily but he recoils,” “the man really comes through the portal,” “the animation looks dead”).

## Mandatory algorithm

1. Quote the exact user direction; separate **literal requested content** from inference.
2. Infer the desired viewer understanding/emotional reaction, not just the adjective.
3. Construct a story-physical event graph with `stimulus, perception, intent, anticipation, initiation, travel, contact, reaction, consequence, recovery`. Mark inapplicable nodes explicitly.
4. Identify all needed actor rigs/props, force directions, contacts, object states, world coordinates and chronology.
5. Propose camera plan that maintains geography and serves audience viewpoint/knowledge; articulate why each move or cut is needed.
6. Design sound with source, distance, subjective/objective mode, event vs editorial cue distinction.
7. Map the plan into actual key poses, layers, masks/mattes, null controllers, keyframes, speed graphs, expressions and effects. State if using AE vs Remotion, and never claim expressions are interchangeable.
8. Surface significant interpretations/conflicts (e.g., curved trajectory vs grounded realism; literal water vs aesthetic metaphor); prioritize higher-level user locks. Don't ask about a nonblocking aesthetic default.
9. Generate **two output versions**: a plain-language director note and a machine-executable shot/asset/property contract.
10. Define objective pass/fail tests (mute audio / disable effects / examine frame-before, event, frame-after; confirm specific verb completed).
11. Label all assumptions and evidence statuses; search `10_KNOWLEDGE` before adding a new unverified rule.

## Required output template

```
USER WORDS:
WHAT VIEWER MUST UNDERSTAND:
PHYSICAL STORY EVENTS:
ACTOR/OBJECT/CONTACT STATE:
CAMERA: (viewpoint, shot, movement, continuity reason)
SOUND: (source, distance, perspective, silence, event timing)
AE OR OTHER IMPLEMENTATION: (layers, rig, key poses, expressions, effects)
CONFLICTS/ALTERNATIVES:
EVIDENCE PLAN:
ACTION COMPLETION TEST:
OPEN QUESTIONS (only blockers):
```

## Guardrails

- No new story event may be inserted into a locked script without user authorization.
- Do not generate irrelevant FX only because their names sound cinematic.
- Do not describe a polished result when only text/code is delivered.
- No claim of AE compatibility until actual installed-version render/error check.
- Record new lesson and evidence in `10_KNOWLEDGE/LEARNING_LOG.md` after completion.
