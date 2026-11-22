---
id: LRN-0006
title: Timing and spatial path are different questions
kind: lesson
status: source-backed
tags: timing, spacing, after-effects, camera
source_ids: S31, S33, S34
related_ids: LRN-0003, LRN-0007
applies_to: 2d, 2.5d, cinematic-animation, prompt-translation
updated: 2026-11-19
---
# LRN-0006 — Timing and spatial path are different questions

## Claim and scope
The spatial path is where a thing goes; timing and speed graph determine how it proceeds along the path. Camera path is separate again.

## Plain-language instruction → technical implementation
Define real path, pose and reference coordinates first. Design ease/holds/speed ramp second. For stylization use deliberate time remap or cutaway.

## Where not to overapply / alternative interpretations
Sharp motion and held poses may be correct for an intentionally snappy style, but accidental discontinuity is not.

## Observable acceptance test
Plot consecutive frame positions and inspect graph near direction changes; maintain screen geography.

## Typical failure
Requesting cinematic curve silently alters physical projectile trajectory, when camera orbit was intended.

## Evidence status and dependencies
**source-backed**; refer to source IDs in `01_RESEARCH/00_SOURCE_LEDGER.md` and directly related lessons. These are reusable principles, not claims of a tested and corrected V4 video. All AE snippets remain runtime-unverified.

## Next learning action
When this scenario is produced, add actual project path/version, frame(s), outcome, and regression evidence in a case study. Link the case ID here without overwriting the earlier claim.
