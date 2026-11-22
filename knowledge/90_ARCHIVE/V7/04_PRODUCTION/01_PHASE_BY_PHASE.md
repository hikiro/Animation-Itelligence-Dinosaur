# Operator's step-by-step production runbook

This is the actionable roadmap for the future agent. Follow **in order**. A checklist in a Markdown file does not prove completion: record real source/media evidence and acceptance before checking a phase off.

## Phase 0 — preflight and story/layout preparation

**Input:** full V3 ZIP extracted, confirmed toolchain and current handoff.

1. Read AGENTS/README, constitution, state, research context, script, character/object state and all active defects.
2. Verify tools (`python`, `node/npm`, `ffmpeg/ffprobe`, renderer, SVG/canvas/image export, audio design/mixing). Record versions. If any missing, disclose and choose a supported plan.
3. Run `python 08_TOOLS/audit_kit.py` from extracted kit root. Fix document errors; do not mistake document audit for film QC.
4. Establish 2.5D world-stage coordinates, portal aperture/ground intersection, rig scale, world-to-camera transform.
5. Draw/test 8-scene beat map, geography map, color arc and audio perspective arc.
6. Create model/rig sheets and a shot-card for benchmark that includes camera purpose, source sound, action test and exact frame intervals.
7. Make a portal geometry-only occlusion test with a simple rectangular dummy body to prove masking before detailed art.
8. Confirm one-shot 270-frame shot plan, and write its event list with planned vs actual flags.

**Exit evidence:** actual design files/diagrams, written world-coordinate conventions, scene proof plan, no unresolved story/portal design blocker. Next: P1.

## Phase 1 — nine-second benchmark BLOCKING

1. Build a no-frills articulated person and portal plane, no music, no motion blur, minimal forest.
2. Use `04_PRODUCTION/02_BENCHMARK_270_FRAMES.md` as authoritative beats; place character **inside** portal from frame 0; no offscreen entering motion.
3. Key head reveal, hand, torso, lead leg, planted foot, pelvis, trail leg, two-foot settle, eyes/head wonder.
4. Render frame range and full rough 9-second clip; show an occlusion debug view and planted-foot markers.
5. Review at 1x and slow, including consecutive frames through threshold and foot contact.
6. Reject any portal mislayer, detached body part, floating foot, camera moving instead of actor, or unexplained disappearance.
7. Fix blocking until viewer truly sees crossing. Update status and defect log.

**Exit evidence:** rough clip, frame set, verified actual crossing, zero blocking blockers/majors. Next: P2.

## Phase 2 — benchmark LOOK/ACTING/AUDIO FINALING

1. Replace debug assets with consistent original paper-cut layers and joint covers. Preserve proven crossing and planted contact constraints.
2. Add controlled forest depth, ground shadows, cyan portal light and subtle hand/head facial performance.
3. Apply camera framing for one continuous proof shot; keep footprint, aperture and body readable. No unjustified zoom/orbit/shake.
4. Build early 48kHz ambience/portal/footstep/character layers using actual contact/crossing events; use original/licensed SFX.
5. Render MP4 with actual sound, audio stems, contact-sheet and adjacent frame exports, plus scene source and reproduction commands.
6. Audit visual, physical, story, spatial/camera, sound, export integrity independently.
7. For every failure write exact frame and repair; repeat without losing accepted contact mechanics.

**Exit evidence:** passing nine-second MP4, editable rig/portal, stems, event log, review sheet, zero blocker/major defects. Obtain/record approval before P3.

## Phase 3 — full picture animatic (80s plan)

1. Freeze known-good benchmark primitives; do not rebuild them from scratch without cause.
2. Block scenes S02–S08 in causally ordered rough poses, eight emotional beats.
3. Establish mother size/entry, nest and chase west route, root/branch placements and apartment portal geography.
4. Pre-spot sound as story: distant thud before source seen, roar after mother's perception, crack interrupts chase, chirp causes mother recognition, apartment contrast.
5. Make 2400-frame planning edit or explicitly revised frame schedule; no invisible catches/transfers/crossings.
6. Play in silence to several reviewers if possible. Ask eight comprehension questions from treatment. Inspect knowledge/pacing transitions.
7. Rework storyboarding if any essential event fails; don't begin detailed animation.

**Exit evidence:** rough film animatic, cut/frame table, shot cards and event spot plan, silent-readability review. Next: P4.

## Phase 4 — animation, shot by shot

For each A02–A24 after A01:

A. Confirm entry actors' world positions, headings, object ownership, eye/gaze and audio bed.
B. Block anticipation, major poses and decisive contacts.
C. Refine root motion, feet/ground, whole-body mass and prop attachment; create contact-event data.
D. Add secondary motion, then camera/light/style refinements, rather than using camera shake to mask errors.
E. Render and inspect critical frames; use `05_QA/02_SCENE_ACTION_TESTS.md`.
F. Update next-shot entry state and spot/audio events.
G. Fix defects, regression-check adjacent shots and mark approved only after actual evidence.

**Exit evidence:** full set of approved scene outputs, coherent state and cut continuity, stable identities. Next: P5.

## Phase 5 — sound design, editorial, grading and final mix

1. Picture lock only after major action/camera continuity errors resolved.
2. Sync Foley to final `CONTACT_LOCKED` events; add intentionally advanced offscreen/POV sounds and trailing sound bridges.
3. Mix ambiences/characters/props/designed sounds first, original restrained score second.
4. Preserve quiet and foreground egg crack/hatch/reunion; test on headphones and phone; mono sum test.
5. Measure sound peaks/true peak/integrated loudness/LRA; target delivery by current YouTube spec; avoid pretending broadcast -23 LUFS is mandatory.
6. Color consistency and safe area UI overlay check; correct camera shaking/text errors.
7. Render single high-quality distribution master and preserve editable intermediate/stems.

**Exit evidence:** actual full video with included sound, stems, editorial and mix report. Next: P6.

## Phase 6 — adversarial QA and delivery

1. Run `ffprobe` on actual files: duration, resolution, frame rate, video/audio streams, color tags.
2. Inspect opening, each action contact, transitions, and final reveal at actual speed and frame-by-frame.
3. Independent muted review and SFX-only/full-mix listening; review for physical, emotional and causal continuity.
4. Check phone readability, UI safe areas, stable branding, missing frames, incorrect motion blur and timing drift.
5. Record defect log with blocker/major/minor; repair/re-render until zero unresolved blockers/majors.
6. Pack editable project with reproducible instructions and license trail; update manifest/status/next-chat note.
7. State exactly what was really rendered and inspected; disclose any still-unverified quality aspects.

**Final acceptance:** passes all 5 gates `story, physical interaction, camera/editorial, sound, technical/export`, with actual media evidence. The document kit's audit alone does not satisfy this.

## Sample tools (illustrative; adapt to actual project, never fake success)

```bash
python 08_TOOLS/audit_kit.py
ffprobe -v error -show_entries format=duration:stream=index,codec_type,codec_name,width,height,avg_frame_rate,sample_rate -of json path/to/render.mp4
ffmpeg -i path/to/render.mp4 -vf fps=1 path/to/qa/frame_%03d.png
ffmpeg -i path/to/render.mp4 -vn -acodec pcm_s16le path/to/qa/audio_review.wav
```

Where render commands are tool-specific, put verified actual command in target project's `RUNBOOK.md` rather than guessing. The examples above are **not evidence those commands ran on a film**.
