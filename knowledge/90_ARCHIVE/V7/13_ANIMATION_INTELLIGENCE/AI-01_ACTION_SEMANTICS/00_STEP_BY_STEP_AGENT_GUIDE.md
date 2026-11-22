# AI-01 — Exact state machine and new-chat recovery

This is the **binding operational order** for any agent continuing the AI-01 research, not a promise of autonomous/background learning.

## One-time intake

**E0 VERIFY FILES** — Extract ZIP. Read `README.md`, `AGENTS.md`, `09_HANDOFF/STATUS.md`, `13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/README.md`. Run `python 08_TOOLS/audit_kit.py`, `python 08_TOOLS/audit_knowledge.py`, `python 08_TOOLS/audit_lesson05.py`, `python 08_TOOLS/audit_ai01.py --root .`, and `python 08_TOOLS/verify_manifest.py`. If any check fails, STOP research changes, report exact failing artifact, repair, rerun. Never infer a missing file exists because a readme claims it does.

**E1 IDENTIFY CURRENT TASK** — Is the request to investigate a word, interpret a director sentence, annotate source script/board, make an action recipe, author a scene, or execute a visual/audio test? Do not jump to rendering a film if the task is research.

**E2 SEARCH BEFORE INVENTING** — `python 08_TOOLS/search_ai01.py --query "phrase" --kind all --top 12`. Search `--kind ambiguity`, context, source and action separately. Also search existing `10_KNOWLEDGE` lessons.

**E3 READ FULL CONTEXT** — Read preceding scene, actor motives/beliefs, props and geography, audience knowledge, emotional genre, intended style, source of every important sound and camera perspective. If a detail is unknown mark `UNKNOWN`; do not hallucinate.

**E4 ANALYZE LANGUAGE** — Parse verbs, adjectives/adverbs, nouns, event sources, grammatical attachment, negations and under-specified terms. For each ambiguous term list at least two plausible meanings with why one is chosen. Identify realistic vs stylized alternatives explicitly.

**E5 WRITE ACTION GRAPH** — World stimulus → actor perception → interpretation (can be wrong) → intention → anticipation if justified → visible action → physical contact/threshold if relevant → consequences → audience inference. Allow reflexes, delayed awareness and montage exceptions; do not force artificial holds.

**E6 SPECIALIST DIRECTIONS** — Draft separate `MOTION`, `CAMERA`, `AUDIO`, `EDITING`, `IMPLEMENTATION` fields and make sure every choice supports the same narrative question. Record the event's source, time, distance, occlusion and physical continuity.

**E7 BUILD A TEST CONTRACT** — Expected action completion, plausible bad output, frame/cue evidence, audience question, source/asset usage rights and test plan. Set evidence level before claiming success.

**E8 TEST IF AVAILABLE** — For code run deterministic checks; for a storyboard inspect each panel and read panel order; for motion render frames and inspect contacts; for sound listen/inspect cue alignment; for mixed media ask blind reviewers. Tests that were NOT run must remain `NOT_RUN`.

**E9 RECORD & CHECKPOINT** — Update `LEARNING_LOG.md`, AI-01 `08_LOGS/`, source ledger, goals, conflict log, handoff `STATUS.md`, indexed lesson/recipe and any modified defect. Run all applicable audits and repackage only after zero mechanical failures.

## Hallucination / context-loss countermeasure

If agent says it already researched/read an inaccessible script, has a successful render without file evidence, supplies imaginary viewer scores, or loses track of action state: **HALT → REOPEN FILE → VERIFY SOURCE/FRAME → DOWNGRADE STATUS → LOG DEFECT → RESUME FROM LAST VERIFIED CHECKPOINT.**

Minimum recovery card to write at end of every session:

```
CURRENT TASK: one sentence
SOURCE(S) OPENED: URLs/pages/files actually inspected
CONTEXT KNOWN: actor belief, goal, world states, audience POV
EVIDENCE LEVEL: L1/L2/L3/L4/L5 with evidence path
NEXT ACTION: one executable step
KNOWN BLOCKERS: explicit
FILES MODIFIED: relative paths
AUDIT COMMANDS / RESULTS: exact
```

## Conflict protocol

User's new direction outranks a draft hypothesis, but does not silently override locked film decisions. If a direction can mean multiple things, interpret using context, state the alternatives and record significant production consequences in `CONFLICT_LOG` before changes. Examples: "sharp impact" can mean sound transient, body snap, or hard edit; "curved projectile" could refer to camera arc, visual trail, or actual path. There are no automatic universal effects.

## Status invariant

AI-01 L1 source notes + L2 corpus + diagrams DO NOT PASS the DINO nine-second portal benchmark. The old 42-action prototype files are educational. Never mark the 80-second movie complete or begin it without its own required benchmark gates.
