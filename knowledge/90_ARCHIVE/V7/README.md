# CURRENT RELEASE: V7 — See `14_STORY_STRUCTURE/`, `15_MISSING_AND_UNVERIFIED_SOURCES/`, and `09_HANDOFF/STATUS.md` V7 addendum. Prior versions retained for audit.

# DINO//DISASTER — Story-Driven Cinematic Animation Agent Kit V4

**Portable production and learning handbook | Prepared 2026-11-19 | The Curiosity Archive**

This ZIP is a **production specification and cross-chat handoff**, not a completed animation or a working render engine. It contains an expandable story, modular agent prompts, research-backed direction principles, context-sensitive camera/motion/sound decisions, a nine-second benchmark, production templates, automated document audits and recovery rules. It also includes the V2 prompt and previous quality audits as historical context.

## First-time entry — do this in order

1. Extract the entire ZIP to a writable project folder; **do not read a single MD and assume the rest is optional**.
2. Open **`AGENTS.md`** and **`00_START_HERE/01_NEW_CHAT_STARTER.md`**.
3. Read `00_START_HERE/02_PROJECT_CONSTITUTION.md`, `00_START_HERE/03_STATE_MACHINE.md`, `00_START_HERE/04_TRUTH_AND_RECOVERY.md`, and `09_HANDOFF/STATUS.md`.
4. Read the research: `01_RESEARCH/05_CONTEXT_COUPLING.md` is the most important new piece, then camera, sound, animation and treatment-writing documents.
5. Read story locks in `02_STORY/`, then follow `04_PRODUCTION/01_PHASE_BY_PHASE.md`.
6. Use **one modular prompt at a time** from `03_PROMPT_MODULES/`, starting with `00_ORCHESTRATOR.md` and ending each iteration with QA. Do not paste the whole library as a single giant instruction to a video model.
7. **Benchmark scene 01, frames 0–269, before the rest of the film.** Work must be demonstrated by actual inspectable frames and an MP4, not by a plausible description.

## Exact reading path by responsibility

| Need | Read |
|---|---|
| New chat onboarding | `00_START_HERE/01_NEW_CHAT_STARTER.md` |
| Binding decisions and restrictions | `00_START_HERE/02_PROJECT_CONSTITUTION.md` |
| Checkpoint / what is done | `09_HANDOFF/STATUS.md`, `09_HANDOFF/DECISION_LOG.md` |
| Core execution loop | `00_START_HERE/03_STATE_MACHINE.md` |
| Lost context / hallucination prevention | `00_START_HERE/04_TRUTH_AND_RECOVERY.md` |
| Research and citation trail | `01_RESEARCH/00_SOURCE_LEDGER.md` |
| Treating camera/motion/audio as one system | `01_RESEARCH/05_CONTEXT_COUPLING.md` |
| Why and how to write treatment/script/prompts | `01_RESEARCH/06_WRITING_AND_ADAPTATION.md` |
| Story and character states | `02_STORY/` |
| Detailed scene direction | `04_PRODUCTION/03_SHOT_CARDS_01_TO_08.md` |
| 270-frame portal benchmark | `04_PRODUCTION/02_BENCHMARK_270_FRAMES.md` |
| Event-based audio | `04_PRODUCTION/04_SOUND_SPOTTING.md` |
| Acceptance and review | `05_QA/` |
| Legacy findings and earlier prompt | `07_REFERENCE_V2/` |
| Packaging integrity check | `python 08_TOOLS/audit_kit.py` |

## Locked format and narrative

- Short title: **DINO//DISASTER — EPISODE 01: WRONG EXIT**.
- Film intent: **~80 seconds / 2400 frames / 30fps / 1080x1920 vertical**. Scene timing totals exactly 80s in the *planning* timeline. Actual editorial changes require updating the timeline and cue sheets.
- Benchmark: **9 seconds / 270 frames** (indices 0 through 269), single continuous shot, actual human portal crossing.
- Visual language: handmade 2.5D paper-cut stop-motion-inspired animation, articulated rigs, consistent source assets; not a slideshow.
- Story: portal arrival → falling egg rescue → protective mother mistakes rescue for theft → genuine chase → egg hatches → reunion → baby follows human back through portal → mother pushes in → cliffhanger.
- Production: **silent-readable first**, design sound early, mix only after picture continuity is validated.
- Branding: The Curiosity Archive, restrained and legible; critical content out of conservative top 170px/bottom 260px buffers; these are project heuristics, not platform guarantees.

## Absolute non-negotiables

1. A character MUST visibly emerge **from inside the portal**, with front/back occlusion and foot/weight transfer; screen-edge entry is an instant blocker.
2. No unmotivated character movement, camera move or sound cue. Every major event has cause, perception, intent, contact/outcome and recovery.
3. A sound cannot prove that a missing action happened. A camera move cannot hide an impossible crossing.
4. Do not claim rendered, tested, listened, or inspected unless actual files exist and the checks were executed.
5. Do not proceed to all 80 seconds without a benchmark pass and clear documented authorization for the next stage.
6. The agent should be creative **within** locked causal events and style continuity, but should propose any story change that affects motivation or chronology rather than silently altering it.

## Artifacts and honest status

The kit includes source **documents only** and a lightweight audit script. It does **not** include a finished nine-second scene, an eight-scene video, original completed rigs, or recorded Foley. These must be produced in the target execution environment. The legacy package contains the earlier five-second animation QC reports and V2 direction, not evidence that V3's storyboard was rendered.

## Reuse for a different story

Treat camera, sound, motion, writing and QA docs as transferable principles; copy `06_TEMPLATES/`, replace all `02_STORY/` facts, replace the scene timing/cards, update `09_HANDOFF/STATUS.md`, and rerun audit. Do not copy dinosaur-specific motivation into unrelated projects.

## Practice exercises and extra research

Use `01_RESEARCH/07_CONTEXT_REVIEW_EXERCISES.md` to rehearse the same story event under suspense, comedy and curiosity before choosing camera and sound. The source ledger now records supplemental Pixar/Disney and sound-perspective research.

## Verify the ZIP after extracting

Run `python 08_TOOLS/audit_kit.py` and `python 08_TOOLS/verify_manifest.py`. The first checks navigation/timing/coverage; the second checks file hashes and unexpected files. Neither evaluates animation performance.

## NEW IN V4 — Living learning + Adobe After Effects research

The previous V3 director kit is preserved. V4 adds: evolving goals/decision conflicts, searchable knowledge base, 9 reusable lessons, original DINO portal case history, a non-graphic fictional cinematic impact translation example, 8 AE technical guides, 2 specialized prompt modules, searchable script and knowledge-audit script.

**The requested approach is collaborative, not asynchronous:** the user and agent learn as they research and inspect actual outputs during active sessions. All additions must update Markdown source and handoff. No claim of completed After Effects render: AE code samples are documentation pending runtime verification.

**New-chat sequence:** `AGENTS.md` → `00_START_HERE/06_EVOLVING_GOALS_AND_DIRECTIONS.md` → `10_KNOWLEDGE/INDEX.md` → run local search for the request → read context-specific docs → apply prompt module `13_NATURAL_LANGUAGE_TO_ANIMATION_TRANSLATOR.md`; use `14_AFTER_EFFECTS_TECHNICAL_DIRECTOR.md` if AE is relevant.

**Quick lookup:** `python 08_TOOLS/search_knowledge.py "impact recoil camera" --expand --top 8`; `python 08_TOOLS/audit_knowledge.py`; `python 08_TOOLS/audit_kit.py`. Detailed guide: `10_KNOWLEDGE/SEARCH_GUIDE.md`.

## V5 — Lesson 05, Human Language → Action Intelligence

User approved the next research direction: converting natural animation instructions to actor intention, causal visible events, rigs/contact, camera/sound rationale, executable code, bad-vs-good examples, and QA. The new module is **[`12_ACTION_INTELLIGENCE/README.md`](12_ACTION_INTELLIGENCE/README.md)** with an indexed 42-action library (`INDEX.md`, JSON and CSV), 5 smaller execution prompts and 3 actual 4-second educational comparison MP4s. Also includes new source references S45–S51, lessons LRN-0010–0013, and automated tests.

**Run from project root:**

```bash
python 08_TOOLS/audit_kit.py
python 08_TOOLS/audit_knowledge.py
python 08_TOOLS/audit_lesson05.py
node 08_TOOLS/test_lesson05.mjs
python 08_TOOLS/search_knowledge.py "portal exit hand contact" --expand --scope 12_ACTION_INTELLIGENCE --top 6
```

The original DINO production remains on hold before **actual** nine-second benchmark approval. **Do not confuse Lesson 05 schematics with completion of the film or AE runtime testing.**


## V6 — AI-01 context-sensitive semantics corpus

New entry: **[`13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/README.md`](13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/README.md)**. Expands dataset to verbs, nouns, adjectives, sound language, camera/editing vocabulary, context-dependent action cards, hard ambiguous terms, and precise source-page observations from real scripts and drawn storyboards. Records are mostly synthetic L2 design data; they are *not* 6k real observed shots. See dataset manifest for exact checked counts.

Quick commands: `python 08_TOOLS/search_ai01.py --query "heavy" --kind ambiguity`; `python 08_TOOLS/audit_ai01.py --root .`. Retains the entire V5 kit; existing nine-second portal film benchmark is still NOT DONE.

**AI-01 current dataset numbers (see manifest/audit for current truth):** 1,152 lexicon records (1,044 distinct lemmas), 4,608 explicitly synthetic context expansions, 208 designed action/context recipes, 120 ambiguous-word interpretation records, 18 carefully sourced observations and 40 unscored human-language evaluation prompts. **Total 6,146 rows, but only 18 are sourced observations.** This distinction is critical. Run `python 08_TOOLS/audit_ai01.py --root .`; all other rows are L2 design/test materials. No new 270-frame portal benchmark was rendered.

## V7 — New cross-chat storytelling reference and source-acquisition system

**NEW:** `14_STORY_STRUCTURE/README.md` with user-supplied `REF-STORY-0001` (Hook → Lead → Body 1 → Open loop → Body 2 → Open loop → Body 3 → CTA). **IMPORTANT:** this is a screenshot-derived option for appropriate short-form contexts, not a mandatory eight-shot structure or verified retention law. Original video and attribution remain unverified.

**NEW:** `15_MISSING_AND_UNVERIFIED_SOURCES/README.md` + canonical `REGISTER.csv` for materials that couldn't be accessed, were never provided, have not been collected, are unverified, or remain to be tested. **NOT_COLLECTED ≠ ACCESS_FAILED.** Future uploads must be associated with an existing GAP ID and carry context, acquisition, licensing and verification metadata.

**Search:** `python 08_TOOLS/search_knowledge.py "open loop" --scope 14_STORY_STRUCTURE`; `python 08_TOOLS/search_materials.py --list`. **Audit:** `python 08_TOOLS/audit_v7.py`. Read `09_HANDOFF/STATUS.md` for what is actually completed.
