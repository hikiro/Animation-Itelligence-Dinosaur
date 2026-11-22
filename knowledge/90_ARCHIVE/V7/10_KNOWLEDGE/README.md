# Living Animation Knowledge Base — Operating Guide

**This system is designed to grow after every research session, animatic, render, visual audit, audio mix, and regression check.** It is not evidence of continuous background learning: a future agent must actually read, investigate, test and update these files during an active working session. A new chat can start from this ZIP without knowing our earlier conversation.

## What lives where

- `LEARNING_LOG.md` — chronological, **append-only** change log. Every record has date, evidence, confidence, related IDs, and next action.
- `LESSONS/LRN-####_*.md` — one reusable concept per file, with exact problems, conditional guidance, failure modes, counterexamples, source attribution, tests, and unresolved questions.
- `CASE_STUDIES/` — actual observed defects and investigations, separating **observed flaw** from **proposed fix** from **verified correction**.
- `PRINCIPLE_REGISTER.md` — concise lookup table of principles, evidence levels and dependencies.
- `TAXONOMY.md` — official topics, definitions, tags, claim-status vocabulary.
- `RESEARCH_BACKLOG.md` — what is still unknown, with planned experimental tests and study priorities.
- `SEARCH_GUIDE.md` — how to search by topic, concept, source, shot, evidence class, related IDs and exact phrase.
- `TEMPLATES/` — reusable files to document new lessons, sources, experiments and production observations consistently.
- `ALIASES.json` — project-specific synonym groups, useful for terminology mismatches.

## Minimum safe update cycle

1. **Retrieve first.** Run `python 08_TOOLS/search_knowledge.py "your problem" --top 10`, then inspect the referenced full Markdown files. Do not invent a "rule" just because a search returned a keyword match.
2. **Observe and capture.** For a flaw, log an actual render path, version, frame(s), screenshot/audio excerpt, expected vs observed action, and inspection method; otherwise label it `unverified`.
3. **Classify the claim.** `source-backed` is not `render-verified`; `proposed` is not `fixed`; subjective judgments are explicitly marked `editorial-judgment`.
4. **Write a lesson** (or revise an existing one without erasing its history) using the appropriate template and stable `LRN-####` ID. Note applicability, exceptions, and cases where it may fail.
5. **Log the outcome.** Append an entry to `LEARNING_LOG.md` with timestamp/date, source IDs, what changed, what remains uncertain and a link to actual files.
6. **Regression check.** If a render was changed, rerender exact problem frames, compare evidence, and mark `fix-verified` only after viewing/listening to the replacement. Preserve before/after pointers.
7. **Update navigation and handoff.** Review `PRINCIPLE_REGISTER.md`, `INDEX.md`, `RESEARCH_BACKLOG.md`, and `09_HANDOFF/STATUS.md` as appropriate. Run `08_TOOLS/audit_knowledge.py`, `08_TOOLS/audit_kit.py`, and re-create the SHA256 manifest for a new archived release.

## Search in 20 seconds

From the ZIP's extracted root:

```bash
python 08_TOOLS/search_knowledge.py "portal occlusion"
python 08_TOOLS/search_knowledge.py "foot skating" --expand --kind lesson
python 08_TOOLS/search_knowledge.py "why is the audio wrong" --expand --tag audio
python 08_TOOLS/search_knowledge.py --id LRN-0004
python 08_TOOLS/search_knowledge.py --related LRN-0001
python 08_TOOLS/search_knowledge.py --list-tags
python 08_TOOLS/audit_knowledge.py
```

Search is **local, deterministic and dependency-free**, with real file paths and line-numbered snippets. It scans the source Markdown on each query, so there is no stale index to maintain. Alias expansion is an optional curated lexical convenience, not AI semantic understanding.

## Rules against hallucinating lessons

- Never claim to have watched a render you have not opened, or heard a mix you have not played back.
- Never turn an authorial heuristic into a universal TV/film law.
- Use exact source names and `S##` IDs from `01_RESEARCH/00_SOURCE_LEDGER.md`; reverify changing external claims.
- If there is no citation or observed test, write `hypothesis` or `unverified`.
- Never overwrite a failed experiment with only its successful successor; the failure is useful evidence.
- If no tools/files are accessible in a new chat, mark the state `BLOCKED` and describe what would be necessary; do not fabricate a repair.
