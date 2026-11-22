---
id: LRN-0014
title: The meaning of an action modifier depends on its attachment and dramatic context
kind: principle
status: RESEARCHED_DESIGNED_NOT_PRODUCTION_VERIFIED
tags: context,polysemy,semantics,actor-belief,camera,sound,action,AI-01
source_ids: S52,S53,S54,S55,S56
related_ids: LRN-0004,LRN-0009,LRN-0012
applies_to: animation, storyboard, sound, After Effects, Remotion
updated: 2026-11-19
---

# LRN-0014 — The meaning of an action modifier depends on its attachment and dramatic context

**Status:** L1 multi-source principle support; L2 authored operational approach; no L5 comprehension experiment yet. **Tags:** context,polysemy,semantics,actor-belief,camera,sound,action,AI-01.

## Claim and scope

Director language such as “heavy,” “sharp,” “hold,” “cut,” or “close” cannot be mapped to a single animation effect without resolving its grammatical and dramatic target. A *heavy foot* points to mass and support; a *heavy emotional pause* concerns narrative rhythm; a *heavy sonic impact* concerns low-frequency body and perceived scale.

## Evidence

- Source S52, BBC Doctor Who shooting script p.18: actor's changing attention/context makes a glance and decision meaningful.
- Source S53, BBC radio-format guide pp.1–3: distinctions in sound source and acoustic perspective are encoded separately from dialogue.
- Source S54, Bournemouth boards pp.13–14: framing/panel relation specifies what is seen, not merely which verb is used.
- S55–S56, Disney/Pixar production pages: staging, acting and story organization are linked.

## Engineering translation — proposed translation rule (L2)

1. Parse actor/object/source of the word.
2. Read actor goal and belief, and knowledge of the viewer.
3. Check physical world, contact and timing constraints.
4. Select motion, camera and audio with different responsibilities.
5. Build explicit visual and auditory acceptance criteria.
6. Compare at least one alternative interpretation when the term is ambiguous.

## Where not to overapply

Do not attach the same word automatically to multiple targets. A dramatic camera or sound effect cannot replace the contact action or body performance.

## Failure pattern

Bad: `heavy` directly triggers full-screen shake, bass boost and slower movement in every shot.

Better: `heavy dinosaur stops` triggers grounded support transfer and torso/tail inertia; audio impact depends on foot-contact event and mic perspective; camera holds or reframes only if the audience needs mass/scale evidence.

## Observable acceptance test

A blind viewer should identify intended cause and emotional interpretation from a rendered scene, and audio-only listening should identify cue source and spatial perspective. These tests have **not** been performed for V6.

## Test and limitations

Inspect the AI-01 `AMBIGUITY_TESTS.jsonl` and four-context `stomp` blueprints. They validate **coverage and proposed distinctions**, not emotional effectiveness. Future render-and-blind-viewer tests must determine whether changes actually communicate threat, comedy, wonder or tenderness.
