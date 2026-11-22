---
id: LRN-0005
title: Impact accents are consequences, not causes
kind: lesson
status: production-heuristic
tags: impact, compositing, camera, sound
source_ids: S29, S30, S31
related_ids: LRN-0002, LRN-0004
applies_to: 2d, 2.5d, cinematic-animation, prompt-translation
updated: 2026-11-19
---
# LRN-0005 — Impact accents are consequences, not causes

## Claim and scope
A graphic impact flash, distortion, speed line, and transient only work once contact position and reaction are understandable.

## Plain-language instruction → technical implementation
Create separate contact-target layer; attach mask/solid to that point; write time-envelope expression to ensure it starts on contact, decays without strobe.

## Where not to overapply / alternative interpretations
Highly abstract manga montage may omit literal detail, but then must establish impact with other reliable cues.

## Observable acceptance test
Turn all accent layers off; if hit disappears as an intelligible event, animation fails.

## Typical failure
Long camera shake covers the only frame of contact.

## Evidence status and dependencies
**production-heuristic**; refer to source IDs in `01_RESEARCH/00_SOURCE_LEDGER.md` and directly related lessons. These are reusable principles, not claims of a tested and corrected V4 video. All AE snippets remain runtime-unverified.

## Next learning action
When this scenario is produced, add actual project path/version, frame(s), outcome, and regression evidence in a case study. Link the case ID here without overwriting the earlier claim.
