# AI-01 validation report — 2026-11-19

### Data audit

- Dataset: `02_CORPUS/DATASET_MANIFEST.json` (generated summary; do not quote counts without rerunning audit).
- Source inspection: BBC shooting script PDF + screenshot, BBC radio format PDF + screenshots, Bournemouth University illustrated storyboard PDF + screenshots, studio/public workflow pages; see `01_RESEARCH/SOURCE_LEDGER_AND_INSPECTION.md`.
- Machine checks: `python 08_TOOLS/audit_ai01.py --root .` (record presence/fields/provenance, source references, context coverage, split isolation, false verification flags).
- Cross-kit checks: `python 08_TOOLS/audit_kit.py`, `python 08_TOOLS/audit_knowledge.py`, `python 08_TOOLS/audit_lesson05.py`, `node 08_TOOLS/test_lesson05.mjs`.
- Search examples: `search_ai01.py --query heavy --kind ambiguity`, `search_ai01.py --query stomp --kind action --context comedy`, `search_ai01.py --query 'heavy silence' --kind eval`.

### Validation hierarchy

- **Source-grounded L1 claims:** which script passages, storyboard drawings and technical guidance were inspected. Do **not** extrapolate final acting or frame speed.
- **Structural/code-tested L3:** all JSON rows parse, group splits, context profiles, source fields, and old V5 numeric motion sampler checks. This is NOT L3 proof of each action implementation.
- **Designed L2:** all action recipes and generated contextual lexical pairs; most of corpus.
- **L4 absent:** no new audiovisual AI-01 animation/audio mix. Original original 4-column sheet visually inspected as a diagram only.
- **L5 absent:** no external blind audience or professional animator ratings. Forty held-out language requests remain **UNSCORED**.

### Known open problems

No paired script→board→animatic→final-shot corpus with complete licensing and timestamps; English-heavy wording; 4 context preset templates cannot encode unlimited real-world context; storyboard does not test camera movement and no original audio samples were mixed this phase. Future work should prioritize diverse real licensed paired examples and falsifiable viewer comprehension measures before claiming semantic understanding.

### Verdict

**AI-01 source research and dataset structure: pass conditional on final ZIP audit. Animation-director semantic performance: not evaluated. DINO nine-second portal benchmark: NOT DONE.**

## Actual completed machine audit summary (2026-11-19)

- `audit_ai01.py`: **29,368 assertions, zero failures**. Includes 1,152 lexicon rows, 4,608 contextual variants, 208 action cases, 120 ambiguity readings, 18 source observations and 40 UNSCORED director test prompts.
- `audit_knowledge.py`: **249 assertions, zero failures**.
- `audit_kit.py`: **76 checks, zero failures**.
- `audit_lesson05.py`: **1,091 passes, zero failures** (inherited V5).
- `test_lesson05.mjs`: **5,617 sampler assertions passed** (inherited V5).
- Manual original storyboard visual QC: found and corrected **AI01-D01** premature foot contact and **AI01-D02** gaze before noticing. Open unresolved camera, audio and audience-testing defects remain in `08_LOGS/DEFECT_LOG.md`.

All these numbers concern **software/document checks**, not independent scientific validation of acting or film readability.
