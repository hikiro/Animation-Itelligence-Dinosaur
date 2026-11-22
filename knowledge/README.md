# Animation Intelligence Knowledge Repository — V8

**Purpose:** a reusable, context-first, searchable knowledge base so a general-purpose language model can translate natural-language story/animation direction into planned scenes, rigs, camera, audio, code, and honest QA evidence. Not a finished animation engine or a validated universal preset library.

## Begin here (strict)
1. Read [`AGENTS.md`](AGENTS.md) and [`00_START_HERE/READ_ORDER.md`](00_START_HERE/READ_ORDER.md).
2. Read the **authoritative** [`01_RULES/ANIMATION_RULEBOOK.md`](01_RULES/ANIMATION_RULEBOOK.md) and [`01_RULES/DO_AND_DONT.md`](01_RULES/DO_AND_DONT.md).
3. Read [`01_RULES/CONTEXT_AND_STORY.md`](01_RULES/CONTEXT_AND_STORY.md), [`01_RULES/RIGGING_FOUNDATIONS.md`](01_RULES/RIGGING_FOUNDATIONS.md), and [`01_RULES/CREATURE_SIZE_ADAPTATION.md`](01_RULES/CREATURE_SIZE_ADAPTATION.md) before generating character performance.
4. Search for a relevant scenario using `python 08_TOOLS/search_repo.py "portal emergence"` and open its record from [`03_PRESET_LIBRARY/INDEX.md`](03_PRESET_LIBRARY/INDEX.md).
5. Consult source/evidence status and outstanding research needs before implementing. Run `python 08_TOOLS/audit_repo.py` on extracted kit.
6. Implement and inspect short tests. Update `02_RESEARCH/LEARNING_LOG.md`, `07_LOGS/SESSION_LOG.md`, and `06_PROJECTS/DINO/STATUS.md` when project state changes.

## Trusted hierarchy
- **Canonical current requirements**: `01_RULES/`, `02_RESEARCH/`, `03_PRESET_LIBRARY/`, `06_PROJECTS/`, `07_LOGS/`.
- **Inherited supporting material**: `90_ARCHIVE/V7/`, retained byte-for-byte as provenance; superseded when conflicting with a V8 canonical rule and explicitly flagged in `07_LOGS/CONFLICTS.md`.
- **Evidence**: A source is not a verified render; a passed JSON auditor is not a passed animation.

## Content
- `00_START_HERE/`: read order, workflow, hallucination recovery and contributor protocol
- `01_RULES/`: enduring rulebook, do/don't, creative context, creature-specific rigging
- `02_RESEARCH/`: evidence references, accessible/unavailable register, cumulative learning log
- `03_PRESET_LIBRARY/`: composable context-dependent scenario presets with uniform schema
- `04_ENGINEERING/`: engine bridges and character specs
- `05_QA/`: tests and defect triage
- `06_PROJECTS/DINO/`: approved DINO story and nine-second benchmark status
- `07_LOGS/`: authoritative decisions, conflicts, changes, intake and session history
- `08_TOOLS/`: indexed search, prompt assembly, dataset and package checks
- `90_ARCHIVE/V7/`: historical originals unchanged

**Scope boundary:** We aspire to broad scenario coverage through modular composition, NOT a finite pretense that every possible event is covered. Every preset has a lifecycle status and known gaps. No new 270-frame portal benchmark or full film was rendered in this release.
