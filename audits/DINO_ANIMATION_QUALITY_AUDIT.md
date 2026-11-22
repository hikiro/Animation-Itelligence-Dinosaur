# DINO//DISASTER — Animation Quality Audit

**Source:** `DINO_FOUR_STYLES_EDITABLE_PROJECT(1).zip`  
**Reviewed:** November 18, 2026  
**Scope:** 4 × 5-second clips; 20-second comparison; `motion.js`, `render.py`, `finalize.py`, `sound.py`, `index.html`, README, and existing QA report.

## Executive verdict

**Technically decodable, creatively below professional short-form motion-design standard.** The first three options are too similar in staging and animation grammar; paper-cut differs materially in styling but shares the same skeletal motion and timeline. The original `qa/validation.json` checks render health, not motion quality. This audit does not equate aesthetic preference with a software bug: some defects are directly measurable, while visual hierarchy and style differentiation are editorial judgments.

**Reviewer scores (subjective, exploratory, /10):** visual-design execution Candy 5, Pop 5.5, Rubber-Hose 4, Paper-Cut 6.5; animation mechanics 3; screen choreography 4; platform-safe composition 2; basic media integrity 8; source portability 3. **Overall readiness: 4/10 as a publishable polished Short**, but a functional proof of concept.

## Independently checked media facts

| Item | Result |
|---|---|
| Four standalone clips | 5.000 s each, 120 frames each |
| Comparison reel | 480 frames, container duration 20.032 s |
| Video | 720×1280, H.264, 24 fps |
| Audio | AAC stereo, 32,000 Hz |
| Decode check | Passed FFmpeg full decode |
| Pixel format / color | `yuvj420p`, full/PC range; reported BT.470BG matrix, unspecified primaries/transfer |
| Native Ant Motion? | **No** — custom JavaScript Canvas, stated in README/source |
| Remotion? | **No** — absent |
| Re-render on Windows from included files? | `render.py` hardcodes Linux `/usr/bin/chromium`; no pinned environment; needs change |

### Measured motion in decoded output

Fraction of image pixels with grayscale value changing by >8 between adjacent decoded frames; the metric includes codec/antialiasing changes and **is not itself a quality score**.

| Clip | Mean moving fraction | Median moving fraction | Mean first 0.5s |
|---|---:|---:|---:|
| Candy | 3.34% | 3.03% | 1.06% |
| Pop | 4.31% | 3.68% | 1.82% |
| Rubber | 4.08% | 3.69% | 1.62% |
| Paper | 3.39% | 2.81% | 1.38% |

Interpretation: large portions of every frame are intentionally held in place, giving the sequences a static-card look. The moving-percent metric must always be paired with human inspection; some excellent animation is intentionally subtle.

## Prioritized defects and how to fix them

**P0 — must fix before a high-quality release**

1. **Large unsupported per-frame displacement; no motion blur.** The deterministic timeline can move the stickman's horizontal anchor ~44.4 px between frames around 0.50–0.54s and the dinosaur ~50.7 px around 1.17–1.21s. Toward the end of the chase, stickman/dino speeds reach approximately 20–32 px per frame. `render.py` captures one sharp Canvas image at each frame with no shutter-time supersampling. On 24 fps output this can read as snapping/judder. **Fix:** stage smaller/smoother moves, normalize timing in physical screen space, use 30/60 fps where appropriate, and perform 3–5 subframe shutter samples or carefully designed directional smears when motion is fast. For the paper-cut style, purposeful stepped holds may be preferable to blur but still require controlled spacing.
2. **No ground-locked feet; unblended gait modes.** `stickman()` (lines ~105–127) animates leg endpoint offsets using global sinusoids and switches into running when `exit > .04`. `dino()`/`dinoLeg()` (lines ~136–143) replace the 7 Hz slow-leg oscillation with a 19 Hz run when `chase > .05`, switching amplitude/frequency abruptly. No inverse kinematics or stance phase anchors the feet to world-space ground. Shadows do not follow actual foot contacts. **Fix:** use explicit stance/swing cycles with locked foot targets, knee/hip articulation, pelvis bob matched to contact, and a 0.15–0.25 s blend into run; test first/last frames of the switch.
3. **Motion direction does not distinguish the first three styles.** All four share the exact same stickman and dinosaur functions, pose definitions, action start times and chase choreography; palette/background/line treatment provide most of the variation. **Fix:** implement style-specific rig/motion systems: Candy = inflated squash/stretch and soft spring; Pop = dramatic comic panels, smash beats, held impact poses; Rubber-Hose = curved flexible limbs, cyclic follow-through, rhythmic extreme arcs; Paper = independent pinned cutouts with depth/parallax and intentional tactile stepping.

**P1 — major visible or production issues**

4. **Premature dinosaur reveal.** At the start (0.00–1.15 s), `dino()` places its body anchor at x=930 but its forward-extending head/muzzle is already partly visible at the right edge, despite the intended later entrance. **Fix:** shift the off-screen spawn by the full silhouette bound; assert no dinosaur pixels enter the shot before the planned cue unless this is a deliberate tease.
5. **Composition feels like a persistent title card, not a designed sequence.** Top title, bottom title and small credit are continuously overlaid; background and framing barely evolve. The story lives in a narrow middle stripe. **Fix:** reserve title lockups for brief story beats, establish a dominant focal point per beat, use close-to-medium shot reframing/camera movement or layered transitions. Keep clean reading holds.
6. **Social platform overlay safety is violated.** Top title begins around y=60–70 on a 1280px frame; the footer label occupies roughly y=1058–1175 and the brand is centered at y=1231. When the established 1080×1920 safe areas are scaled to 720×1280, the exclusion regions are top ~113px and bottom ~173px. Parts of the title/footer and virtually all of the small brand fall in these areas. **Fix:** move priority text into y≈114–1106 or use an even more conservative platform-preview safe template; keep high-priority characters/captions away from right-hand UI overlays.
7. **End chase has no strong narrative payoff.** Stickman exits left while dinosaur remains in frame; the separation between anchor positions *increases* from ~297px at 3.53s to ~425px at 4.85s. This is not objectively wrong for a chase, but it weakens perceived threat or comedic connection. **Fix:** create a collision/near miss/close-follow gag, tighten relative paths, or deliberately communicate the runner's escape.
8. **Lossy intermediary.** `render.py` converts each Canvas frame to JPEG quality=86 before H.264 encoding; this is two lossy compressions and particularly harmful to washi fibers, thin ink lines, and saturated pop-art edges. **Fix:** encode from PNG or lossless raw RGB/RGBA and use H.264 at suitable export quality.
9. **Unmanaged export color metadata.** Decoded clips report `yuvj420p` PC/full color range, BT.470BG color matrix, and unspecified color primaries/transfer. **Fix:** explicitly produce/test standard BT.709 SDR with consistent range signaling; run cross-player and mobile quality checks; do not rely on FFmpeg's defaults.
10. **Not an Ant Motion/Remotion editable project.** The README fairly discloses the engine. If the intended deliverable was native Ant Motion or Remotion, this does not meet it. **Fix:** provide actual component-based project, version-locked dependencies, composition timeline and rendered assets; or label this only as a Canvas storyboard prototype.
11. **Portability and editability limitations.** `/usr/bin/chromium` is hardcoded, `render.py` depends on unspecified Python package versions; no requirements or lock file; the HTML only shows a still frame and requires developer-console calls to scrub. **Fix:** resolve Chromium through Playwright's managed installation, add requirements/lock, and provide a timeline/preview UI and source layer controls.

**P2 — polish and continuity**

12. **Abrupt facial-expression switches.** The stickman mouth uses `if (t>2.65 && t<4.7)` and the dino eyebrow `if (t>2.3 && t<3.8)` with no transition, unlike the roar's blended mouth. **Fix:** transition shapes/opacity over 2–5 frames or use deliberate, motivated single-frame poses.
13. **Audio footsteps are scheduled independently of contact.** `sound.py` inserts foot hits at 1.50, 2.10 and 3.64+0.16s intervals, instead of computing from the actual animated landing instants. **Fix:** drive sounds from the same contact/event curve as foot planting; review at 0.25x speed and normal speed. Auditory timbre judgment was not performed in this audit.
14. **Brand readability on mobile.** `THE CURIOSITY ARCHIVE` is drawn at 20px on a 720px-wide image, only ~10px when displayed at 360px phone width, and is low in the screen near UI controls. **Fix:** give the identity a separate brief legible reveal in a safe zone, rather than a permanent tiny credit.
15. **One identical five-second story for every style is a good A/B control, but insufficient as a finished series concept.** For a style test, preserve the same action; for a production episode, add context, a surprising event and a memorable payoff before the final CTA.
16. **No quality-gate tests beyond technical rendering.** The original `qa/validation.json` checks syntax, deterministic frames, decoding and runtime exceptions. It does not test temporal jerk, velocity, foot sliding, onscreen bound/safe areas, frame readability, compositing, source fidelity, sound-to-contact sync or art-style distinction. **Fix:** maintain separate technical and director sign-off checklists.

## Frame-by-frame direction notes

| Timeline (within each 5s clip) | Observed beat | Concern | Repair direction |
|---|---|---|---|
| 0.00–0.50 | Establishing backdrop and first portal | Low immediate action; dino muzzle peeks prematurely | Strong clean opening pose; ensure planned offscreen characters are fully hidden |
| 0.50–1.20 | Stickman enters | High initial velocity; body travel dominates actual acting | Add anticipation at portal, overshoot, settle; no uncontrolled jumps |
| 1.15–2.35 | Dinosaur enters | Large first-step displacement; same silhouette across variants | Make entrance style-specific, establish weight via delayed hips and tail |
| 2.55–3.30 | Roar/comedic reaction | Face shapes snap; FX placed similarly across styles | Animate eyes, jaw, neck and sound at a shared impact time |
| 3.47–4.93 | Chase | Leg cycle and speed not physically coupled; no shutter blur | Plant feet; blend gait; intentional spacing and readable relative action |
| 4.32–5.00 | End teaser | Static text treatment, runner leaves, weak payoff | Design a style-matched end pose or near-collision reveal, then short legible tag |

## Five-pillar reusable animation QA protocol

### 1. Context — story and attention
- Can a viewer identify the subject in the first 0.5–1s without reading labels?
- Does each beat have a cause and visible consequence? Does action lead to a payoff?
- Watch silently at 1× speed. Does the story still make sense?

### 2. Assets — silhouette and layering
- Inspect at phone size, grayscale and at 25% scale.
- Check character count, appendage pivots, object masks, edge continuity, paper shadow directions and no visible offscreen prematurity.
- Verify all text stays readable and in platform-safe areas.

### 3. Motion — physics and animation fundamentals
- Scrub **every frame** around entrances, accelerations, contact, collisions and transitions.
- Track per-frame object-space displacement, acceleration and abrupt switches; do not use a global threshold without context.
- Foot-ground position must remain stationary during stance. Limbs move from joints, body reacts to mass, tails/hair/props lag the body.
- Check anticipation → main action → overshoot/follow-through → settle and clear timing/spacing.
- Test at 0.25×, 1× and 2× and review fast moves for judder/blur.

### 4. Style — distinct motion grammar
- Enforce a style guide for shape, outline, texture, animation method, camera, sound, transitions and lighting, not just palette.
- For each style: cover the labels and identify the style by movement alone. If impossible, the variants are too similar.

### 5. Output — delivery and reproducibility
- Decode all streams; verify fps, duration, exact frame count, pixel format, audio sample rate and color metadata.
- Export test at actual phone width; review typography and occlusion under the Shorts/Reels UI mockup.
- Require editable source, pinned dependencies and one-command clean-build instructions.
- Compare the exported MP4 visually against lossless frames, especially textures and thin lines.

## Acceptance gate for the next iteration

**Hard blockers:** no missing/cropped assets; no unintended exposure of offscreen characters; zero obvious foot sliding at contact; no unexplained limb-pose jumps; no required text outside designated safe areas; all render/decoder checks green; all claimed technologies actually used.  
**Director sign-off:** distinctive animation grammar for each style; clearly readable subject at phone size; satisfying action and reaction; appropriate blur or intentional stepped cadence; consistent shadows/depth; sound effects hit the drawn impact/contact frames.  
**Documentation:** issue ID, severity, affected timestamp and frame, reproducible screenshot, source line/cause, fix, and pass/fail regression verification.

### Notes on methodology and uncertainty
- Full FFmpeg decode, metadata, source inspection, contact sheets, sampled keyframes and pixel-delta checks were performed here.
- Per-object anchor velocity numbers are calculated from the shipped JavaScript formulas, not inferred from visual tracking.
- Motion quality and style/readability scores are professional **judgments**, not scientific measures of audience retention.
- Audio events were compared to motion code schedules; this was not a human listening test.
- No claim is made that the finished clips have been re-rendered from source in this audit.
