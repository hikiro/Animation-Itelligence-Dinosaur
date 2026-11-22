---
id: LRN-0003
title: Expressions augment rigged poses, not replace animation
kind: lesson
status: source-backed
tags: after-effects, expressions, rigging, timing
source_ids: S26, S27, S28, S32
related_ids: LRN-0002, LRN-0006
applies_to: 2d, 2.5d, cinematic-animation, prompt-translation
updated: 2026-11-19
---
# LRN-0003 — Expressions augment rigged poses, not replace animation

## Claim and scope
AE expression executes a per-property calculation; it does not create parent layers, a pose library, collisions, or a finished story.

## Plain-language instruction → technical implementation
Use authored keyframes for intention/stance/contact, controllers and expressions for procedural offset/settle, and AE scripts for scene construction if needed.

## Where not to overapply / alternative interpretations
A few simple motion-graphics tasks can be created almost entirely procedurally, but character acting still needs a thought-through pose/beat design.

## Observable acceptance test
Confirm properties, controllers, and small AE test renders, not simply valid-looking syntax.

## Typical failure
Paste `wiggle(4,20)` on actor root to “make impact strong” without contact.

## Evidence status and dependencies
**source-backed**; refer to source IDs in `01_RESEARCH/00_SOURCE_LEDGER.md` and directly related lessons. These are reusable principles, not claims of a tested and corrected V4 video. All AE snippets remain runtime-unverified.

## Next learning action
When this scenario is produced, add actual project path/version, frame(s), outcome, and regression evidence in a case study. Link the case ID here without overwriting the earlier claim.
