# Deterministic research and production loop

**Intake → Normalize → Search → Compare → Contextualize → Plan → Implement → Render → Inspect → Repair → Verify → Log → Handoff**.

- **Intake:** Record exact user phrasing and scope; distinguish user factual constraints from brainstormed ideas.
- **Normalize:** Convert verbs, nouns, adjectives, sound descriptions, and locations into role/goal/relationship entities while retaining original wording.
- **Search:** Find presets and existing defect cases. Check claims against source IDs and evidence level.
- **Compare:** Determine which presets are compatible. Surface conflicting style/physics/user constraints; record decisions before overriding.
- **Contextualize:** Describe story goal, audience information, emotion, creature body plan/scale, camera position, audio perspective, preceding and following shots.
- **Plan:** Produce storyboard beats, shot layout, persistent object/character states, rig channels, physical contact events and sound spotting.
- **Implement:** Create reusable, deterministic frame-time functions and rig constraints. Keep aesthetic choices parameterized; never use sound as evidence for an invisible action.
- **Render:** Produce actual inspectable frames and audio; preserve commands and reproducibility metadata.
- **Inspect:** Watch silent for story/action; then camera/story continuity; then audio timing/perspective; then technical specs. Inspect intermediate frames near contacts.
- **Repair:** Record observed defect, hypothesis and exact fix; if repeated twice, investigate anatomy/world-space/rig architecture rather than tuning random curves.
- **Verify:** Re-run defect-specific regression plus broad checks; status may only advance with stored evidence.
- **Log:** Learning entry + source/experiment IDs + do/don't update when principle generalized + conflict and gap entries + status/handoff.
- **Handoff:** State phase, files changed, passed/failed tests, open blockers, immediate next action.
