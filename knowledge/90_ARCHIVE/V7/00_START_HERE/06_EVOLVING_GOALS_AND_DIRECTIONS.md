# Living goals and directions — user-authorized design contract

**Updated:** 2026-11-19. **Status:** ongoing learning; no claim of autonomous background research.

## Goals and priority

| ID | Priority | Goal | Verification | Status |
|---|---|---|---|---|
| GOAL-001 | P0 | Translate everyday natural-language creative direction into story-causal, executable animation instructions | Direction contract contains meaning, beats, cameras, rigs, layers, audio, expressions/effects, QA tests | Active |
| GOAL-002 | P0 | Preserve detailed evolving lessons across conversations as portable Markdown | Searchable lessons, append-only log, source evidence, uncertainty, stable IDs, local search tests | V4 documentation created |
| GOAL-003 | P0 | Every character movement motivated, legible and physically coordinated | Stimulus → noticing → decision → anticipation → action → consequence and recovery | Principle; unverified on new render |
| GOAL-004 | P0 | Learn Adobe After Effects layers, solids, mattes, puppet/rigs, keyframes, graph editor, expressions, cameras, sound context | Technical guide, expression map, runnable-in-AE examples, provenance; verify in actual AE before claiming tested | Research documented, AE runtime untested |
| GOAL-005 | P0 | Camera, motion and sound jointly communicate the exact story event and emotional context | Context triplet and sound/event cues for each major beat | Documentation created |
| GOAL-006 | P0 | Detect hallucinations, unsupported claims, mis-sequenced actions, and missing outputs | Evidence labels, anti-hallucination stop rule, recovery card and defects | Operating contract active |
| GOAL-007 | P1 | Build professional 9-second portal crossing before full 80-second film | Inspectable 270-frame rendered scene, true portal passage, foot contacts, audio evidence | Not rendered; acceptance unchanged |
| GOAL-008 | P1 | Distinguish expressive stylization from grounded physics, and flag ambiguous/conflicting direction | Alternatives + decision log + no silent style switch | Ongoing |
| GOAL-009 | P2 | Generalize reusable animations beyond dinosaur project | Neutral templates and context translator applicable to any non-graphic story | Architecture created |

## Most recent user direction (INT-0001)

> “If I say the bullet impact should be understood, infer connected recoil, traveled projectile, cinematic tracking/speed, manga-like art emphasis, actual hit, physical reaction, and slow fall.”

Treat this as a **translation case study**, not authorization to add a shooting event to DINO//DISASTER. This shows how abstract adjectives or verbs imply a causal action graph.

## Editing protocol

- On every new task, compare user language with active goals and locked project rules.
- Distinguish `APPROVED`, `PROPOSED`, `RESEARCHED`, `RENDERED_VERIFIED`, `NOT_TESTED`.
- When direction changes a locked narrative event, document `CONFLICT-####` before modifying story.
- Update this file plus `09_HANDOFF/DECISION_LOG.md`, `10_KNOWLEDGE/LEARNING_LOG.md`, relevant lessons, and a searchable index.
- If no actual tool research or render takes place, do not mark it done. No claim of unattended or future background work.

## Working human-language vocabulary

- “More alive” → clear intention, anticipatory posture, delayed overlap, expressive gaze and purposeful recovery.
- “More punchy” → shorter anticipation/stronger contrast, decisive contact accent, controlled audiovisual peak; not random screen shake.
- “Cinematic” → viewer-aligned framing, lens/perspective choices, motivated camera path, rhythmic editing, selective sound perspective.
- “Impact reads” → source, trajectory, exact contact, force response, causal sound, aftermath and a readability check.
- “Smooth” → controlled spacing/velocity continuity as intended; not smoothing deliberate impact or hold poses.
- “Realistic” → believable causality, inertia, contact, plausible dynamics; do not over-stylize without noting change.
- “Anime/manga” → intentional graphic style, impact frames, speed lines, holds, compositional compression, dramatic contrast; avoid assuming every technique applies.

## V5 user-approved research direction — Lesson 05, 2026-11-19

| ID | Priority | New objective | Work performed | Next evidence gate |
|---|---|---|---|---|
| GOAL-010 | P0 | Translate natural speech into a causal action graph, not cosmetic motion | 42 action cards across 7 categories, compiler, event phases | Independent comprehension on target rigs |
| GOAL-011 | P0 | Couple camera, motion, sound to actor/audience information context | Per-action context fields + 3-context stomp comparison matrix | Render three context variants, listening/viewer evaluation |
| GOAL-012 | P0 | Test deliberately faulty versus corrected code and report limitations honestly | 3 schematic comparison MP4s and scripted event tests | Production rig and sound-level tests; teaching demos not film passes |
| GOAL-013 | P1 | Make lesson/action knowledge searchable and cross-chat recoverable | ACT IDs, JSON/CSV/MD, search aliases, source ledger, log and handoff | Confirm keyword and synonym retrieval in extracted ZIP |

**Locked production directive unchanged:** nine-second 270-frame portal entrance benchmark before full 80-second film. Lesson 05 demonstrations are adjacent research and are not that film's approved render.

## V6 approved expansion — AI-01 research context and scale

| ID | Priority | User-authorized research goal | Required validation | Status |
|---|---|---|---|---|
| GOAL-014 | P0 | Maintain the original seven AI-01…AI-07 domains as permanent map; AI-01 first | Stable IDs + cross-links | Implemented in AI-01 research charter |
| GOAL-015 | P0 | Expand far beyond 50 acting terms; include verbs/nouns/adjectives/adverbs, sound, camera, script and storyboard language | Machine-readable corpus; explicit synthetic/source provenance | V6 corpus authored; domain validation ongoing |
| GOAL-016 | P0 | Context can change meaning; do not map adjectives to one preset | Hard ambiguity tests + alternate contexts | V6 ambiguity set and context cases, not audience verified |
| GOAL-017 | P0 | Use real scripts and drawn boards as research evidence | Source/shot/page inspection + separate source ledger; no copyrighted copies | V6 source observations recorded (small sample only) |
| GOAL-018 | P0 | All research claims require source or test evidence and detailed logging | L1–L5 levels, split isolation, QA, cross-chat handoff | Research/structural audits, no L5 claims |

## V7 authorized goals — 2026-11-19

| ID | Priority | Goal | Evidence/acceptance | Status |
|---|---|---|---|---|
| GOAL-019 | P0 | Preserve user-uploaded short-form structure: Hook → Lead → Body 1 → Open loop → Body 2 → Open loop → Body 3 → CTA | Exact screenshot, transcribed beat order, context applicability/counterexamples in `REF-STORY-0001` | Source image inspected; retention/creator interpretation unverified |
| GOAL-020 | P0 | Maintain permanent detailed register of inaccessible, missing, not-yet-collected and unverified animation research materials, for manual supply later | `REGISTER.csv`, source attempt history, user intake template, search tool, audit | V7 implemented; no external access attempts inferred |
| GOAL-021 | P0 | Organize all evidence and context so another chat can recover without inventing research or progress | ID taxonomy, source chain, log updates, handoff, recovery/search instructions | V7 documentation organized and structurally audited |
