# AI-01 — Action Semantics, Context, and Character Intention

> **Status: source-researched and structurally tested; NOT actor-performance validated, NOT a licensed source-script corpus.** Created 2026-11-19.

This is a continuously growing **context-sensitive directing research corpus**. It extends, not replaces, `12_ACTION_INTELLIGENCE` (42 V5 recipes). It targets phrases like “make it feel heavy”, “the character realizes it”, “more suspenseful”, “the roar sounds close”, “a foot hits the ground”, and translates them **conditionally** into causally consistent decisions about character behavior, camera, sound, editing, layers, rigs and proof.

## Required entry / reading order

1. Project `AGENTS.md` and `09_HANDOFF/STATUS.md` for authoritative status.
2. This README and `01_RESEARCH/RESEARCH_GOAL_AND_SCOPE.md`.
3. `01_RESEARCH/SOURCE_LEDGER_AND_INSPECTION.md`, `03_CASE_STUDIES/SCRIPT_AND_DRAWN_BOARD_READINGS.md`.
4. `01_RESEARCH/CONTEXT_MODEL_AND_ACTION_GRAMMAR.md`, `01_RESEARCH/DATASET_METHOD_LIMITATIONS.md`.
5. `02_CORPUS/DATASET_MANIFEST.json` + `02_CORPUS/SCHEMA.md`.
6. `04_CONTEXT_EXPERIMENTS/EXPERIMENT_DESIGN.md` and `07_AUDIT/TEST_REPORT.md`.
7. `06_PROMPTS/00_AI01_ORCHESTRATOR.md` and only the module needed.

## Corpus reality check

- `LEXICON.jsonl`: individually authored candidate terms; overlapping lemmas are intentional when terms have multiple production functions.
- `CONTEXTUAL_LEXICON.jsonl`: **synthetic templates** combining those terms with four contexts. These rows are NOT observations of 4,000 separate scripts.
- `ACTION_CONTEXT_CASES.jsonl`: 52 deliberately structured action scenarios × 4 emotional contexts (each retains its own visible action evidence).
- `AMBIGUITY_TESTS.jsonl`: 30 ambiguous tokens × four interpretive possibilities; intended to prevent keyword-only auto-effects.
- `DIRECTOR_EVAL_CASES.jsonl`: forty **held-out, authored and UNSCORED** normal-language requests, including suspense/realism conflicts not represented by the four synthetic context presets. These should be used for blind interpretation evaluation, not model training.
- `INSPECTED_SOURCE_OBSERVATIONS.jsonl`: compact source-grounded, **paraphrased** observations with page/section and inspectability notes.
- The old V5 `ACT` library remains a separate project component and is not silently counted as independently observed evidence here.

## Quick lookup

```bash
python 08_TOOLS/search_ai01.py --query "hesitate" --context threat --kind action
python 08_TOOLS/search_ai01.py --query "heavy" --kind ambiguity
python 08_TOOLS/search_ai01.py --query "thud" --kind lexicon --domain sound_source
python 08_TOOLS/search_ai01.py --query "portal" --kind source
python 08_TOOLS/audit_ai01.py --root .
python 08_TOOLS/search_knowledge.py "impact reaction" --expand --top 8
```

## Evidence ladder

- **L1_SOURCE_INSPECTED:** directly inspected textual passage or drawn board; describes the **source**, not a successful generated animation.
- **L1_LIMITED_ACCESS:** source summary/index only; do not claim to have seen inaccessible underlying shots.
- **L2_DESIGN / L2_GENERATED:** authored theoretical directorial decisions or generated lexical context expansion; NOT audience validation.
- **L3_CODE_TESTED:** passed mechanical/syntactic/runtime tests; does not prove a believable acting choice.
- **L4_RENDER_INSPECTED:** actual frames or audio inspected and defects documented.
- **L5_PRODUCTION_VERIFIED:** independently reviewed for readability across audiences and passed regressions.

## Operating invariant

**Interpret meaning + actor belief + physical world + viewer knowledge before selecting an effect.** If unsure between two valid readings, present the alternatives; don't hallucinate an action that doesn't follow from context.

## Preserved production lock

`DINO//DISASTER` production still requires a separate, approved **9-second 270-frame portal entrance benchmark**. AI-01 research, vocabulary, boards or mini tests must never be mistaken for that benchmark or the 80-second film.

## V7 supplemental source and context log

- User-provided short-form story sequence `REF-STORY-0001` is in `14_STORY_STRUCTURE/`. It adds narrative beats (Hook→Lead→Body1→OpenLoop→Body2→OpenLoop→Body3→CTA) to the AI-01 context vocabulary, **not** a universal retention law.
- All missing originals, uncertain attribution and uncollected matched storyboard/video/audio samples are tracked in `15_MISSING_AND_UNVERIFIED_SOURCES/REGISTER.csv`. Do not call those evidence-backed observations unless actually inspected.
