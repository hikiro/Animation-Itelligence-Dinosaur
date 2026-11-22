---
id: LRN-0001
title: Action is completed only when visible
kind: lesson
status: observed-issue
tags: story-logic, contact, acting, portal
source_ids: CASE-0001, S02, S03
related_ids: LRN-0002, LRN-0004
applies_to: 2d, 2.5d, cinematic-animation, prompt-translation
updated: 2026-11-19
---
# LRN-0001 — Action is completed only when visible

## Claim and scope
A character cannot be judged to have emerged, grabbed, hit, or fallen from dialogue or an offscreen slide; the event must show its defining boundary/contact and stable before/after states.

## Plain-language instruction → technical implementation
For a portal: render human inside aperture, straddling threshold, first planted foot, hips/trailing foot clearing, fully outside. Use front/back occlusion and body weight transfer.

## Where not to overapply / alternative interpretations
Visual grammar may intentionally conceal a portion for suspense, but the audience still needs unambiguous confirmation.

## Observable acceptance test
Inspect keyframes plus 1-frame-before/after at threshold, mute audio and ask viewer to name action.

## Typical failure
A flash and “portal whoosh” play while actor just slides in from left edge.

## Evidence status and dependencies
**observed-issue**; refer to source IDs in `01_RESEARCH/00_SOURCE_LEDGER.md` and directly related lessons. These are reusable principles, not claims of a tested and corrected V4 video. All AE snippets remain runtime-unverified.

## Next learning action
When this scenario is produced, add actual project path/version, frame(s), outcome, and regression evidence in a case study. Link the case ID here without overwriting the earlier claim.
