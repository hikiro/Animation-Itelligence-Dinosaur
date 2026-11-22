---
id: LRN-0011
title: Use timing curves for channels, constraints for contacts
kind: principle
status: RESEARCH_SYNTHESIS_PARTIALLY_DEMO_TESTED
tags: rig, curves, ik, contact
source_ids: S47,S48
related_ids: LRN-0001, LRN-0002, LRN-0004
applies_to: animation, After Effects, Remotion, paper cutout
updated: 2026-11-19
---

# LRN-0011: Use timing curves for channels, constraints for contacts

## Claim and scope

Easing returns property values; it does not solve object ownership, IK or portal plane geometry. A smoothly animated wrong scene is still wrong.

## Engineering translation

Use event-parameterized channels plus world-locked feet, explicit prop ownership and mask transitions. Derive contacts from actual rig/world geometry.

## Where not to overapply

Do not assume every scene needs fully physically simulated rigging: an expressive limited-animation hold can work if contact continuity is readable.

## Observable acceptance test

In a stance interval, world-space foot anchor drift is at or below shot-defined tolerance; during a catch, hand and egg positions converge before attachment, and attached object remains fixed relative to the hand.

## Evidence

- Research basis S45–S51 (exact source detail in `01_RESEARCH/00_SOURCE_LEDGER.md`); each source supports general studio/software practice, not our timing proposals.
- Related original recipes `12_ACTION_INTELLIGENCE/INDEX.md` and actual schematic tests `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.
- Not approved on the target DINO film, no AE-runtime execution confirmed.
