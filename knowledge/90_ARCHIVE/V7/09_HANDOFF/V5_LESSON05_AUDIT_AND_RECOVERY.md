# V5 handoff: Lesson 05 / Action Intelligence

**Date:** 2026-11-19. **Scope:** documentation, original educational demos and code tests, not finished DINO production.

## What exists and was inspected

- 42 action recipes (6 each: Perception, Locomotion, Object, Force, Spatial, Emotion, Cinema), with stable ACT IDs and searchable Markdown/JSON/CSV.
- A pure JavaScript `action_engine.mjs`, example CLI, and unit assertions for every normalized recipe curve.
- Three actually encoded original four-second 960×540 30fps schematic videos contrasting known faulty patterns with improvement strategies. Original generated single-note/noise stomp sound is included. Contact sheet was visually inspected.
- A contextual camera and sound treatment guide, five small modular prompts, source ledger entries S45–S51, new lessons LRN-0010–LRN-0013, recovery, goal and conflict updates.

## Real test commands and actual results

```bash
python 08_TOOLS/audit_kit.py                  # 76 PASS, 0 FAIL
python 08_TOOLS/audit_knowledge.py            # 235 PASS, 0 FAIL
python 08_TOOLS/audit_lesson05.py             # 1091 PASS, 0 FAIL
node 08_TOOLS/test_lesson05.mjs              # 5617 assertions PASS, 42 recipes
node 08_TOOLS/example_action_recipe.mjs ACT-025 55
python 08_TOOLS/search_knowledge.py "portal crossing" --expand --scope 12_ACTION_INTELLIGENCE --top 4
```

- `ffprobe` checks 120 frames, 30fps and 960×540 for three videos.
- Test verifies a single original synthetic WAV cue on or near 2.000 sec for stomp.
- PNG contact sheet visually compared F030 and F088 for three subjects.

**Limitation:** algorithmic data checks cannot detect unconvincing acting, timing, or art polish; after-effects examples remain untested in AE application.

## Quality-critical unverified issues (carry into next chat)

- Need true depth + hand/front rim/foot plane portal setup. The schematic does not count as the 270-frame entrance benchmark.
- Need animated 2D articulated character rig with stance-foot world anchoring, intentional momentum and body overlap.
- Need prop ownership/contact and two-handed grasp at egg catch.
- Need multi-layer Foley with acoustic perspective and edited musical space.
- Need blind first-viewer story comprehension; original sample durations are not independently validated.

## Resume algorithm

1. Extract ZIP and run the four test commands above, plus manifest verification.
2. Read `AGENTS.md`, `09_HANDOFF/STATUS.md`, `12_ACTION_INTELLIGENCE/README.md`, and `01_LANGUAGE_TO_ACTION_COMPILER.md`.
3. Search by the user's wording; choose one ACT recipe and compare active locked DINO story constraints.
4. Create scene-specific event frames/world state and first rig/camera/audio blocking; render actual evidence.
5. Inspect and write defects; repair; rerender and regress; only then promote that action's status.
6. At turn end update learning log, source ledger, index, status, decision and conflict files; rebuild manifest and ZIP.

**User-approved major project gate:** 9-second / 270-frame portal benchmark prior to full 80-second film remains unchanged and NOT DONE.
