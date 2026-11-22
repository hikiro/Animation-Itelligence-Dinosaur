# Learning log — chronological, append only

This log records research **performed in a session**, not autonomous, continuous background study. Always distinguish source inspection from runtime validation.

## 2026-11-18 — Original DINO quality inspection (historical audit)

- **ID:** LOG-0001 | **Source:** `07_REFERENCE_V2/DINO_ANIMATION_QUALITY_AUDIT.md`, `07_REFERENCE_V2/MOTION_STORY_LOGIC_QA.md` | **Evidence:** historic original contact sheets and source inspection summarized in archive.
- **Observed:** portal entrance not visibly completed; gait, body reactions, temporal spacing, camera/story action independence were weak.
- **Result:** `LRN-0001`, `LRN-0002`, `CASE-0001`; proposed a causal action-completion test.
- **Status:** observed original issue; subsequent repair NOT verified.

## 2026-11-19 — Film grammar and sound context research (V3 carried forward)

- **ID:** LOG-0002 | **Sources:** S01–S25 in source ledger.
- **Learned:** camera, motion and sound must be chosen for the same story event and viewer knowledge; cut on action, depth, offscreen sound, sound perspective, score priority.
- **Result:** `LRN-0004`; `01_RESEARCH/05_CONTEXT_COUPLING.md`.
- **Status:** sourced practice + project synthesis; not a new render.

## 2026-11-19 — After Effects expression/layer research

- **ID:** LOG-0003 | **Sources:** Adobe expression language, layers/solids/mattes, Puppet, Graph Editor, AE cameras/motion blur, effects/controls, Dan Ebberts bounce references (S26–S44).
- **Learned:** expressions are per-property computed values, not scene-creation scripts; built rigs/mattes/keyframes do primary storytelling; `wiggle`, `ease`, `valueAtTime`, `loopOut`, `posterizeTime`, controls and layer-space conversion each have specific uses/limitations.
- **Result:** `11_AFTER_EFFECTS/` study track, `LRN-0003`, `LRN-0006`, `LRN-0007`.
- **Status:** source-backed concepts; snippets **NOT TESTED IN AE**, no AEP or new MP4.

## 2026-11-19 — User's natural-language-to-code example

- **ID:** LOG-0004 | **Input:** fictional projectile impact should clearly show cause, recoil, travel, camera insert, manga/water aesthetic, contact, character shake and fall.
- **Learned:** don't literalize adjectives: translate into physical action graph, visual emphasis, editorial coverage, sound perspective, implementation layers and observability tests. Distinguish stylized path/time and objective physical motion.
- **Result:** `INT-0001`, `LRN-0005`, `LRN-0009`, new `GOAL-001/004/008`, `CONFLICT-001–007`.
- **Status:** authored translation example; still needs actual test animation.

## Pending experiments

- `EXP-0001`: AE portal cross with front/back mattes and planted foot; inspect inside / straddling / outside.
- `EXP-0002`: AE property comparison for contact-only pose vs contact + shake; silent viewer action-identification test.
- `EXP-0003`: Separate actual projectile path and camera path; compare geographical comprehension.
- `EXP-0004`: Verify all expression snippets in a real AE version with screenshot and render evidence.
- `EXP-0005`: Search quality testing on synonyms, IDs and titles across new chats.

## 2026-11-19 — Lesson 05: natural-language action compiler and schematic rendering (V5)

- **ID:** LOG-0005 | **User direction:** approve the suggested action-intelligence research program and practical demonstrations.
- **Sources:** Disney character animation/story/layout, Adobe Puppet/speed graphs, Blender inverse kinematics, Remotion frame curves, Disney editorial and Adobe Foley (S45–S51). They support *general methods*, not the sample schedules.
- **Production proposal:** 42 action cards in seven categories; six causal stages, rig/contact plan, contextual camera and sound, faulty and improved code examples, QA contract. Original sample schedules are deliberately pedagogical; adjust for actual shot context.
- **Implemented code:** pure JS frame sampler (`08_TOOLS/action_engine.mjs`); unit test sample curves over 42 recipes (see `08_TOOLS/test_lesson05.mjs`). Structural audit (`08_TOOLS/audit_lesson05.py`).
- **Actually rendered:** three side-by-side four-second educational clips, 960×540 @30fps, and contact sheet; stomp clip includes one original synthetic audio impact. See `12_ACTION_INTELLIGENCE/EXPERIMENTS/` and `RESULTS/TEST_REPORT.md`.
- **Observed limitations:** crossing is a simplified 2D matte, no fully solved IK; stomp is rudimentary acting/one synthesized thump; egg catch lacks rigorous finger/prop constraint; timings only context-neutral educational examples.
- **Outcome:** lessons `LRN-0010`–`LRN-0013` created, searchable action library/index added. **Nine-second approved DINO portal benchmark still NOT DONE.** No AE runtime verification.
- **Next tests:** independent silent comprehension test, true articulated portal crossing, world-space stance-foot drift instrumentation, prop ownership/contact at egg capture, layered Foley and sonic perspective.


## 2026-11-19 — AI-01 expanded context-annotated research corpus (V6)

**User directive:** make research substantially larger, including sounds, nouns, adjectives, script and drawn storyboard observations; context must change interpretation; keep all sources, hypotheses, decisions and tests traceable.

**Source observations (L1):** BBC Doctor Who p.18 distinguishes observation/reconsideration; BBC radio format p.1–3 connects cue notation to sound perspective; Bournemouth storyboard pp.13–14 shows action/framing/panel transitions; Disney and Pixar public process documents support integrating story/shot design. Sources with restricted/incomplete inspection explicitly labelled.

**Our design hypotheses (L2, not source facts):** contextualize lexical terms under threat, comedy, wonder, tenderness; create action-performance blueprints and ambiguity alternatives. Each synthetic row is labelled; corpus size is *not* count of independent source observations.

**Known defects / open research:** source video/animatic pairs not acquired; no real audience studies, actor mocap annotations, audio-only listening tests, or AE runtime validation. DINO 270f benchmark remains NOT_RENDERED.

**Next:** execute AI-01 search and audit on extracted kit, sample 30 rows for expert review, then follow multi-shot semantic validation before promoting to L4/L5.

## 2026-11-19 — V7 user-supplied short-form storytelling structure and evidence backlog

- **ID:** LOG-0007 | **Input/evidence:** exact user-supplied screenshot (internal `REF-STORY-0001`), image personally inspected from `/mnt/data/image(20261119-054259).png`; labels: Hook, Lead, Body 1, Open loop, Body 2, Open loop, Body 3, CTA.
- **Direct observation:** image has eight ordered bars and calls itself “The perfect structure” for short-form content. Visible handle appears to read `robin_linkerpro`, not independently verified. No audio, shot timings or original post/video inspected.
- **Interpretation / context:** possible framework for fact-based Shorts; open loops require resolution, not generic delays; for character-driven fiction use only where it enhances story causality/emotional payoff. Claims about retention improvements remain HYPOTHESES.
- **Artifacts:** `14_STORY_STRUCTURE/REF-STORY-0001.md`, internal reference screenshot, context matrix, record schema; `15_MISSING_AND_UNVERIFIED_SOURCES/REGISTER.csv`, access history, intake template, new search/audit tools; updated README/AGENTS/status and goals/decisions/conflicts.
- **Validation:** check V7 package test outputs and SHA256; no additional real-world creator/video inspection or viewer study claimed. **Open:** GAP-001, GAP-002, GAP-006, GAP-009; request original video/source URL for deeper study.
