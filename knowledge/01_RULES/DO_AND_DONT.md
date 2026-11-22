# DO / DON'T — studio operating rules

| Context | DO | DON'T | Acceptance evidence |
|---|---|---|---|
| Story / causality | Identify perception, decision and visible outcome | Translate a word directly into a canned motion | Causal shot beat sheet; silent viewing |
| Timing | Design anticipation, contact, settle per event | Apply the same easing to all movement | Pose/contact chart; continuity playback |
| Feet / balance | Lock stance contacts in world coordinates; track pelvis and support | Translate a walk-cycle sprite over static ground | Drift measurement + review |
| Prop interactions | Explicitly transfer ownership: world → hand → world | Teleport a prop near a hand | Frame-by-frame grasp/release |
| Portal / door | Animate entire body traversing threshold with depth masking | Have character appear from screen edge | inside/crossing/outside evidence |
| Human | Rig feet/knees/hips and gaze/torso hierarchy | Drive only root x/y and fake footsteps | Support and acting QA |
| Quadruped | Design limb phase and spine/shoulder/hip offsets for body plan | Reuse biped gait as-is | Contact charts + animal reference |
| Heavy creature | Show acceleration/braking inertia, ground reaction and overlap | Communicate mass only with shake/bass | Silent perceived-mass test |
| Small creature | Respect faster pose readability, foot/hop support and intentional personality | Treat it as uniformly scaled adult | Scale/context comparison |
| Long tails/wings | Build distributed bend and follow-through with limits | Make appendages rotate rigidly or clip | Intermediate collision silhouettes |
| Sound | Tie cues to event IDs, physical materials and viewpoint | Trigger Foley at arbitrary times | On-frame sync and perspective mix |
| Camera | Reveal/track subject to serve knowledge and feeling | Add constant zoom, whip and shake | Silent camera-only comprehension |
| Style | Define which physics and poses are intentionally exaggerated | Use style to excuse continuity failures | Consistent style rules and audience test |
| Code | Use deterministic time sampling, constraints and named controls | Assume AE expressions replace rigs | Seek-frame regression and rig tests |
| Research | Preserve quotes minimally, cite actual source, distinguish inference | Present synthetic rows as real film evidence | Provenance and status fields |
| QA | Inspect rendered media, log observed defects and regressions | Declare success on successful export alone | Actual images/audio, review log |
| Versions | Keep one canonical rule; archive prior versions | Accumulate conflicting README addenda | Conflict log + source hierarchy |
| Recovery | Verify existence, status, commands and artifacts | Invent work from a handoff summary | Evidence-backed recovery card |

**Exceptions:** Expressive animation can bend realism, use limited animation, or deliberately withhold causality—but only if the audience information goal is explicit and the result is tested. Add the exception to the relevant preset and `07_LOGS/DECISIONS.md`.
