# Searchable learning index — start here

**Use the search script, not memory alone:** `python 08_TOOLS/search_knowledge.py "impact reads" --expand`.

## Quick lookup

- Portal not emerged / masking / threshold → `LRN-0001`, `LRN-0007`, `CASE-0001`.
- Bad foot contact / pose reaction / shake → `LRN-0002` and `11_AFTER_EFFECTS/02_KEYFRAMES_GRAPH_EDITOR_AND_RIGS.md`.
- After Effects expression meaning / code usage → `LRN-0003`, `11_AFTER_EFFECTS/03_EXPRESSIONS_PLAIN_ENGLISH_DICTIONARY.md`, `04_EXPRESSION_COOKBOOK.md`.
- Camera, sound and motion context → `LRN-0004`, `11_AFTER_EFFECTS/06_CONTEXT_DRIVEN_TECHNIQUE_SELECTOR.md`, `01_RESEARCH/05_CONTEXT_COUPLING.md`.
- Solids/shape/track mattes/precomps → `LRN-0007`, `11_AFTER_EFFECTS/01_LAYERS_SOLIDS_MATTES_AND_PRECOMPS.md`.
- Impact accent flash/FX must follow actual contact → `LRN-0005`.
- Motion arc vs speed ramp vs camera trajectory → `LRN-0006`.
- Natural-language “bullet impact” full example → `LRN-0009`, `10_KNOWLEDGE/EXAMPLES/INT-0001_CINEMATIC_IMPACT_TRANSLATION.md`.
- What is learned vs tested? → `LRN-0008`, `LEARNING_LOG.md`, `09_HANDOFF/STATUS.md`.
- Open goals and conflicts → `00_START_HERE/06_EVOLVING_GOALS_AND_DIRECTIONS.md`, `07_CONFLICT_AND_INTERPRETATION_LOG.md`.

## How to grow this index

Add each stable ID, synonyms and relative file path on the same day as new research/render. Do not claim a lesson is fixed if it is only proposed. Search script scans all MD live, so index is a human shortcut rather than a stale search database.

## Lesson 05 — Action intelligence (V5)

- Event-graph cause and action completion: `LRN-0010`, see `12_ACTION_INTELLIGENCE/01_LANGUAGE_TO_ACTION_COMPILER.md`.
- Property curves versus IK/contact: `LRN-0011`, ACT-007, ACT-014, ACT-025.
- Context-led camera and sound: `LRN-0012`, `12_ACTION_INTELLIGENCE/03_CONTEXT_CAMERA_AUDIO.md`.
- Educational comparisons versus approved production: `LRN-0013`, `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.
- **42-action index:** [`12_ACTION_INTELLIGENCE/INDEX.md`](../12_ACTION_INTELLIGENCE/INDEX.md).
- Search: `python 08_TOOLS/search_knowledge.py "catch egg contact" --expand --scope 12_ACTION_INTELLIGENCE`.

## V6 — AI-01 research and context-dependent corpus

- **Permanent map and research objective** → `13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/01_RESEARCH/RESEARCH_GOAL_AND_SCOPE.md`.
- **Story context and typed event graph** → `13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/01_RESEARCH/CONTEXT_MODEL_AND_ACTION_GRAMMAR.md`.
- **Real scripts / drawn storyboard readings, source level** → `13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/03_CASE_STUDIES/SCRIPT_AND_DRAWN_BOARD_READINGS.md`.
- **Full lexicon, modifiers, nouns, sound and camera** → `13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/02_CORPUS/LEXICON.jsonl`.
- **Word ambiguity e.g. heavy, hold, cut, push, close** → `13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/02_CORPUS/AMBIGUITY_TESTS.jsonl`.
- **Action × threat/comedy/wonder/tenderness** → `13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/02_CORPUS/ACTION_CONTEXT_CASES.jsonl`.
- **Original educational storyboard sheet** → `13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/04_CONTEXT_EXPERIMENTS/stomp_four_contexts_original_storyboard.png` (NOT user tested).
- **New semantic search** → `python 08_TOOLS/search_ai01.py --query "heavy" --kind ambiguity`; source info supports L1 only.
- **Audit** → `python 08_TOOLS/audit_ai01.py --root .`; structural validation is not performance validation.

- `LRN-0014` — Context/grammar must attach every adjective and sound cue to the right actor, prop, shot or acoustic source; do not trigger effects by token alone.

## V7 — Storytelling references and missing-source access

- **User screenshot and eight-beat short-form framework** → `REF-STORY-0001`, `14_STORY_STRUCTURE/REF-STORY-0001.md` (Hook, Lead, Body 1, Open loop, Body 2, Open loop, Body 3, CTA).
- **Context-dependent template selection and payoff tracking** → `14_STORY_STRUCTURE/CONTEXT_ADAPTATION_AND_TESTS.md`, `CONFLICT-011`, `GOAL-019`.
- **Original video not provided, attribution unverified, permissions unreviewed** → `GAP-001`, `GAP-002`, `GAP-009` in `15_MISSING_AND_UNVERIFIED_SOURCES/REGISTER.csv`.
- **Training data manual acquisition requests (scripts, drawn storyboard, animatics, sound stems, AE tests, viewer data)** → `15_MISSING_AND_UNVERIFIED_SOURCES/README.md`, `REGISTER.csv`, `MANUAL_SUBMISSION_TEMPLATE.md`.
- **Material search:** `python 08_TOOLS/search_materials.py --list`; story search: `python 08_TOOLS/search_knowledge.py "Hook Lead open loop" --scope 14_STORY_STRUCTURE`.
