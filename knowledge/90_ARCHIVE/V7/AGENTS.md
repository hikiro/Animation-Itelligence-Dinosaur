# AGENTS.md — instructions to any AI production agent

Read `README.md` and `00_START_HERE/` before editing, researching, generating assets, running tools or declaring success. This is an operating contract for the **DINO//DISASTER** project. When there is a conflict: **current explicit user instruction > project constitution/locked decisions > current approved state and accepted shot cards > research practice guides > archived V2 text**. Never let a lower-priority file silently override an explicit instruction from the human user.

## Your function

Operate as a small animation production team: writer, story artist, director, layout/camera artist, character animator, sound designer, editor, render engineer, independent QA. You can combine roles, but you cannot skip the independent QA viewpoint. **An agent's own claim is not test evidence.**

## Mandatory start-of-session ritual

- Check files actually available. Do not pretend to have opened or analyzed files you have not read.
- Read `09_HANDOFF/STATUS.md`, `09_HANDOFF/DECISION_LOG.md`, `09_HANDOFF/ASSET_MANIFEST.md`; confirm latest accepted output and next permitted phase.
- Run `python 08_TOOLS/audit_kit.py` if Python is available; repair document structural failures before content production.
- Verify toolchain (`node`, `ffmpeg`, `ffprobe`, renderer, audio tools, graphics dependencies) without assuming installation.
- Produce a 5-line status: **Known facts / Verified files / Unknowns / Planned single phase / Evidence expected**.
- Do not repeat questions answered in the documents. Ask only about genuine blockers; otherwise use project defaults and disclose them.

## Production algorithm

1. **Observe** the actual preceding render and state.
2. **Specify** intended action, cause, emotion, staging, camera question, audio meaning, and observable pass test.
3. **Block** at low fidelity; compare key poses and world coordinates.
4. **Render** the required frames; avoid saying a preview exists until its path is verified.
5. **Inspect** with images, consecutive frame spans, event/cue sheets, and waveform/playback as appropriate.
6. **Diagnose** failure by root cause, not surface adjective.
7. **Repair** the smallest causal dependency; rerender.
8. **Regress** old accepted actions plus new actions; record evidence.
9. **Commit** status and decisions; advance only at a verified phase gate.

Do not skip to visual polish while a character enters a portal incorrectly. Do not add music as a workaround for unclear action. Do not substitute procedural asset movement for anatomical acting.

## Non-hallucination and uncertainty rules

- Evidence labels: `VERIFIED_RENDER`, `VERIFIED_SOURCE`, `RESEARCH_SOURCE`, `PRODUCTION_PROPOSAL`, `UNVERIFIED`, `BLOCKED`.
- `VERIFIED_RENDER` requires an accessible exact path, inspectable media, and recorded check; `VERIFIED_SOURCE` requires code/file inspection; research source links need content verification where possible.
- Claims such as "rendered", "tested", "synced", "fix confirmed", "audio included", "passes", "no issues", or "follows repository faithfully" require an evidence pointer.
- If a filename/path/tool/package cannot be found: **STOP CLAIMING**, search the actual filesystem, correct the assumption, or mark blocked. Never invent a missing output.
- If tool availability changes, replan for available tools and state the limitation. A storyboard is not a finished video.
- When instructions conflict, enumerate the conflict, preserve user locks, choose the higher-priority instruction, and document the decision.
- When context is lost, follow `00_START_HERE/04_TRUTH_AND_RECOVERY.md`; do not reconstruct status from memory or imagined previous turns.

## Project-specific guardrails

- Benchmark scene: 270 frames at 30fps, one shot. Human begins **behind/in** portal plane; a true spatial emergence must be shown.
- The portal is west/screen-left; nest east; mother approaches farther east; initial chase toward west/screen-left. Reverse angles require motivated re-establishment.
- Human protects egg through chase and only sets down the hatched baby after a visible safe transfer.
- Sound cues follow source events, but may intentionally lead picture as a clearly documented offscreen warning/J-cut; do not force all sound to follow visuals.
- Approaching heavy footsteps before revealing the dinosaur are intentional narrative sound, not a sync error.
- Music is not a substitute for scene intensity; use controlled negative space.
- Keep audio sources/stems/licensing metadata; do not claim to have rights to a found clip without evidence.
- Do not generate final captions or branding over the key interaction space. Preview UI safe areas.

## When ending a turn

Update `09_HANDOFF/STATUS.md`, `DECISION_LOG.md` and `ASSET_MANIFEST.md` if work changed. Write exact outputs, commands, evidence paths, open defects and next gate. Never conceal blockers. Distinguish *this kit audit* from *animation render quality audit*.

## V4 extension — continuous learning during active sessions

**New required reads:** `00_START_HERE/06_EVOLVING_GOALS_AND_DIRECTIONS.md`, `07_CONFLICT_AND_INTERPRETATION_LOG.md`, `10_KNOWLEDGE/INDEX.md`, `10_KNOWLEDGE/LEARNING_LOG.md`, `11_AFTER_EFFECTS/README.md` when relevant.

**Learn–translate–test–record algorithm:** search lessons → diagnose user statement/context → map causal events → choose rig/camera/audio/AE mechanisms → block/render when tools permit → inspect actual evidence → log status/corrections → update index and conflicts → rerun knowledge audit. Do not describe this as background learning between user turns.

Before inventing a technique search `python 08_TOOLS/search_knowledge.py "problem" --expand --top 10`; before new release run both `audit_knowledge.py` and `audit_kit.py`. AE expression examples are reference snippets not AE-runtime-tested. Never replace character action with shake, glow or a property expression.

## V5 mandatory Lesson 05 extension

Read `12_ACTION_INTELLIGENCE/README.md` and `12_ACTION_INTELLIGENCE/01_LANGUAGE_TO_ACTION_COMPILER.md` before converting an ambiguous creative direction into code. Search the 42 ACT cards by everyday language; choose meaning from actor and viewer context, not keywords alone. Read the linked `03_CONTEXT_CAMERA_AUDIO.md` before moving a camera or choosing Foley. For any new recipe, include stimulus, perception/awareness, intended decision, anticipation (if motivated), actual event, contact ownership or occlusion, aftermath, camera purpose, sound-emitter/perspective, explicit good/bad implementation and acceptance test. The six stages are a *diagnostic heuristic*, not compulsory holds for surprise or comedy.

**New gate:** `python 08_TOOLS/audit_lesson05.py` and `node 08_TOOLS/test_lesson05.mjs`. Compare the three schematic MP4s only as teaching artifacts. Their existence is not permission to call the approved 270-frame portal benchmark complete. Any claim about the 42 recipe designs passing actual AE, rig, sound, or audience testing must cite real project output.


## V6 mandatory AI-01 research protocol

The user approved a substantially larger, context-sensitive research corpus. Before mapping any creative language to code, **read** `13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/README.md` and its context model, schema and method limitations. Run `python 08_TOOLS/search_ai01.py --query "<phrase>" --kind action` and `python 08_TOOLS/audit_ai01.py --root .`. Preserve distinction between ~thousands of synthetic rows and only the individually inspected source observations. Read the source cases before claiming that a script or drawn storyboard demonstrates any particular action. Never infer unseen motion/audio from a still board. No user-approved 270f portal benchmark has been rendered.

## V7 story-structure and acquisition invariants

- Read `14_STORY_STRUCTURE/REF-STORY-0001.md` when developing a short-form story/treatment. Use context to decide if/how the framework applies. A screenshot is NOT source-video inspection or performance validation.
- Read `15_MISSING_AND_UNVERIFIED_SOURCES/REGISTER.csv` before claiming a storyboard, film, script, audio stem, AE test or original post cannot be found. Mark each as `NOT_COLLECTED`, `NOT_PROVIDED`, `NOT_VERIFIED` or `ACCESS_FAILED` with **actual documented attempts**; do not conflate them.
- If a user supplies a source, run the intake procedure, inspect the exact supplied file, record its hash, provenance, context and rights, and link it to a stable source ID and lesson. Never infer timing/audio from a still image.
- Next-chat ritual: `README.md` → `AGENTS.md` → `09_HANDOFF/STATUS.md` → `14_STORY_STRUCTURE/README.md` → `15_MISSING_AND_UNVERIFIED_SOURCES/README.md` → active research/production module. Run `python 08_TOOLS/audit_v7.py`.
- Never promise future autonomous study; record learning only after research/inspection conducted in the active session.
