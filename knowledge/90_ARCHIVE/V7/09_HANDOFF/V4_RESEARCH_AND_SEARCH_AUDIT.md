# V4 documentation, search and code-check report — 2026-11-19

**Scope:** Actual local files and deterministic checks; no animation render / After Effects runtime / sound listening test performed.

## Results

- Local knowledge structural audit: **179 passed, 0 failed** (before release report addition).
- Existing project-document audit: **76 passed, 0 failed**.
- SHA256: **103 files checked, zero mismatches, zero extras** (before adding this report and regenerating manifest).
- Five search queries exercised with `--expand --json`: all found the expected category/lesson within top 25 results.
- Expression snippets: **11 examples**; all passed basic Node.js syntax parsing (not AE execution).
- The source ledger now tracks AE source IDs **S26–S44** with what is and is not supported by each reference.
- Creative direction example `INT-0001` is a hypothetical fictional non-graphic action scene, not an event added to the locked dinosaur story.

## Evidentiary limits

- JavaScript parsing is not After Effects expression validation; runtime property semantics, controls, dimensions, effects, and render output remain **UNVERIFIED** until tested in an actual AE project.
- Structural audits do not prove scientific accuracy, storyboard quality, media performance, audio sync or cinema aesthetics.
- External source pages were accessed through research retrieval; they may change in later sessions.
- The approved nine-second DINO portal benchmark has not been rendered as part of V4.

## Next verification

1. Extract this ZIP to a writable directory and rerun `audit_knowledge.py`, `audit_kit.py`, `verify_manifest.py`.
2. Check local search for `bullet impact`, `portal threshold`, `solids track matte`, `wiggle`, `camera sound context`.
3. If an actual After Effects installation is available, implement a short `TEST_EXPR` comp and check all E01–E11 expressions with renders, not merely parsing.
4. Add any observed AE error, fix and frame evidence to `LEARNING_LOG.md` with a stable case ID.
