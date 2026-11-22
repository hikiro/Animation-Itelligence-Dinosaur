---
id: LRN-0007
title: Solids, mattes and precomps have specific jobs
kind: lesson
status: source-backed
tags: after-effects, solids, occlusion, layers
source_ids: S28, S35, S36, S37
related_ids: LRN-0001, LRN-0003
applies_to: 2d, 2.5d, cinematic-animation, prompt-translation
updated: 2026-11-19
---
# LRN-0007 — Solids, mattes and precomps have specific jobs

## Claim and scope
A solid is an image surface; masks/mattes control visibility; nulls control other layers; precomps group transforms/effects; none alone creates character physics.

## Plain-language instruction → technical implementation
Use matte to reveal portal crossing, shape vectors for rim/speed lines, solids for effects/displacement control, nulls for actor and camera rigs.

## Where not to overapply / alternative interpretations
Simple graphic title animations may need only a solid and keyframes.

## Observable acceptance test
Toggle matte and near-rim to verify depth order; test precomp effects/render order.

## Typical failure
Put whole actor on single solid and move it past a portal.

## Evidence status and dependencies
**source-backed**; refer to source IDs in `01_RESEARCH/00_SOURCE_LEDGER.md` and directly related lessons. These are reusable principles, not claims of a tested and corrected V4 video. All AE snippets remain runtime-unverified.

## Next learning action
When this scenario is produced, add actual project path/version, frame(s), outcome, and regression evidence in a case study. Link the case ID here without overwriting the earlier claim.
