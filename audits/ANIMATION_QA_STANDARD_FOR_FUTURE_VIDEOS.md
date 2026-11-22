# Animation QA Standard — The Curiosity Archive

This checklist must be run on each shot and each final exported video **before** declaring it complete. A technically valid render is a prerequisite, not the acceptance criterion.

## The 3-pass audit

### Pass 1 — Mechanical/technical
- [ ] Files decode; frame count, fps and aspect ratio correct.
- [ ] No black frames, duplicated accident frames or premature silhouettes.
- [ ] Export colors and edge fidelity match approved reference.
- [ ] No unexpected audio clips, sync drift, clicks or clipped peaks.
- [ ] Safe area: keep top 170px and bottom 260px clear of essential text for 1080×1920 work; check right-hand platform overlays.
- [ ] Project is reproducible on its target OS and dependencies are pinned.

### Pass 2 — Motion/continuity, frame by frame
- [ ] Animatic and intended beats matched by frame index.
- [ ] Entrances start offscreen if intended; exits finish completely outside frame.
- [ ] Anticipation, follow-through and settles exist where the movement needs them.
- [ ] No discontinuity at switch between idle/walk/run/roar poses.
- [ ] Feet do not skate during stance; grounded characters have consistent shadows.
- [ ] Relative movement, overlaps and gaze direction support the story.
- [ ] Fast movement has readable spacing at final fps; shutter blur/smears if appropriate.
- [ ] All scene transitions and layer stacking have a defined, tested order.

### Pass 3 — Director quality
- [ ] The intended story is comprehensible without a title card.
- [ ] At phone size, subject, focal point and text are immediately readable.
- [ ] Scene has strong visual hierarchy and motion guides the viewer's attention.
- [ ] Distinct proposed styles have **distinct timing and physical animation**, not merely hue changes.
- [ ] Voice/subtitles, SFX, visual action and accents synchronize precisely.
- [ ] Finished sequence is not a static slideshow with tiny movements.
- [ ] End beat pays off an open loop or clearly delivers a meaningful next question.

## Review cadence

1. **Storyboard:** check Context + Asset intention, no render yet.
2. **Blocking playblast:** check continuity, screen motion and camera paths with text overlays disabled.
3. **Final animation:** check timing curves, physics, secondary motion and typography.
4. **Sound/brand pass:** check speaker-time sync, SFX contacts, logo fidelity and safe areas.
5. **Export pass:** check actual MP4 and final platform-size playback, not just editor preview.

## Issue format to keep forever

`ISSUE-ID | severity P0/P1/P2 | style/shot | timestamp/frame | expected | observed | code/source | screenshot | fix | verification status`

**Do not mark “QA passed” solely because a video is valid, editable, or free of runtime exceptions.**
