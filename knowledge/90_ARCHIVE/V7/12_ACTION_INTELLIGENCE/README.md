# Lesson 05: From everyday directing language to animated action

**Version:** V5, 2026-11-19. **Scope:** research + 42 proposed action recipes + three educational comparison videos. This is **NOT** completion of the approved DINO portal entrance benchmark or its 80-second film.

## Read in order

1. `README.md` (this file); then `01_LANGUAGE_TO_ACTION_COMPILER.md`.
2. `02_EVIDENCE_AND_TECHNIQUES.md` to understand what sources actually support.
3. `03_CONTEXT_CAMERA_AUDIO.md` for story-dependent selection rules.
4. `INDEX.md` or `python 08_TOOLS/search_knowledge.py "<question>" --expand --scope 12_ACTION_INTELLIGENCE`.
5. One or more `RECIPES/ACT-*.md` relevant to the user's direction.
6. `04_RENDER_AND_QA_PROTOCOL.md` and `RESULTS/TEST_REPORT.md` before interpreting the videos.
7. `PROMPTS/` modules for reusable agent prompts.
8. `09_HANDOFF/STATUS.md`, `10_KNOWLEDGE/LEARNING_LOG.md`, `00_START_HERE/06_EVOLVING_GOALS_AND_DIRECTIONS.md` before finishing.

## Action library contents

- 42 detailed original action-card proposals: 6 each in Perception, Locomotion, Object, Force, Spatial, Emotion, Cinema.
- Every card has a causal storyboard, rig and controller plan, per-phase sample frames, camera and sound rationale, intentionally flawed code, improved time-addressable JS sampler example, likely defects, corrections and observable tests.
- `DATA/action_recipes.json` and `.csv` are portable for code and spreadsheet inspection.
- `08_TOOLS/action_engine.mjs` is pure frame-addressable timing/interpolation code; its output requires actual rig, audio and collision implementations.
- Original **schematic** bad-vs-corrected clips for portal emergence, footfall reaction, egg catch (`EXPERIMENTS/`). Not the approved nine-second benchmark.

## How to run

From the kit root:

```bash
python 08_TOOLS/audit_kit.py
python 08_TOOLS/audit_knowledge.py
python 08_TOOLS/audit_lesson05.py
node 08_TOOLS/test_lesson05.mjs
python 08_TOOLS/search_knowledge.py "someone catches an egg" --expand --scope 12_ACTION_INTELLIGENCE --top 5
# Optional, requires Pillow/numpy/ffmpeg; recreates the diagrams and their media:
python 08_TOOLS/render_lesson05_demos.py
```

## Evidence taxonomy

- `RESEARCH_SOURCE`: confirmed general guidance from documented source (S45–S51).
- `PROPOSED_RECIPE`: our own implementation idea, scene logic and timing.
- `TESTED_CODE`: JS sampler unit testing executed; no pose/rig integrated.
- `RENDERED_DEMO`: encoded schematic frames; manual inspection still needed to determine failure/resolution.
- `NOT_VERIFIED`: 42 recipes have not been individually run in production rigs; AE application execution has not happened.

## Hard gate for interpreting the results

The old DINO portal shot still failed. A cartoon of a portal exit is **not** evidence the approved production shot is fixed. Do not update the project to `BENCHMARK_APPROVED` unless the original 270-frame shot's real geometry, articulation, contact and sound have actually been rendered and independently reviewed.
