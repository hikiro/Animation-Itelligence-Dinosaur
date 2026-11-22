---
id: CASE-0001
title: Original DINO comparison reel did not show portal crossing
kind: case-study
status: observed-issue
tags: portal, occlusion, story-logic, contact
source_ids: LRN-0001, LRN-0007
related_ids: LRN-0001, LRN-0008
applies_to: historic-reel
updated: 2026-11-19
---
# CASE-0001 — Portal crossing failure in original DINO samples

**Observed in prior completed audit** archived at `07_REFERENCE_V2/DINO_ANIMATION_QUALITY_AUDIT.md` and `07_REFERENCE_V2/MOTION_STORY_LOGIC_QA.md`; the historic source reel is NOT included in this learning kit. Prior reviewer noted the human moves horizontally near the portal but does not visibly emerge from inside its aperture, and threshold/ground positions do not match.

**Expected:** Human starts inside aperture, appears partially occluded, crosses threshold, plants first foot, transfers weight, trailing foot clears, fully exits.

**Observed:** Horizontal screen-edge motion made actor appear beside the portal; portal didn't spatially contain the character. Portal animation and movement appear as separate events.

**Probable cause:** Root sprite translation without coordinated near/far matte geometry, foot/hip poses or true depth crossing.

**Proposed repair:** Establish portal plane and contact-ground coordinate, front rim/back rim/aperture matte; animate multi-phase real crossing with articulated rig; test transparent debug visualization.

**Fix status:** `proposed-fix`, not verified; no new V4 benchmark video rendered. Inspect target production files before claiming this particular defect repaired.

**Regression tests:** At 0–269 benchmark frames, check partly inside / straddling / outside; verify no outside-screen entry; foot contact plant and clean rim occlusion; audio muted still readable.
