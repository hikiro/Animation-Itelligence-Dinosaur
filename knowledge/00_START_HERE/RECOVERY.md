# Recovery and hallucination countermeasures

When uncertainty arises:
1. STOP modifications and invalidate unsupported completion claims.
2. Read `06_PROJECTS/DINO/STATUS.md`, last `07_LOGS/SESSION_LOG.md`, and active defect items.
3. Verify real file existence, sizes and hashes; run `python 08_TOOLS/audit_repo.py`.
4. Recover actual render command, seed, source version and inspected frames/audio. If absent, classify as **NOT VERIFIED**.
5. Trace every major decision to a user lock, source or explicitly labeled creative inference.
6. If documentation conflicts: current explicit user instruction > canonical V8 rules > approved current project decisions > legacy archive; log the conflict, do not silently erase it.
7. Produce a small reproducible test rather than hallucinating a large artifact.
8. Log a recovery entry with original failure, evidence read, corrected understanding, remaining uncertainty and next step.

**Source failure policy:** `02_RESEARCH/ACCESS_GAPS.md` must distinguish unattempted, blocked, permission required, missing, incomplete, and not validated. Never record an unattempted request as a failed access attempt.
