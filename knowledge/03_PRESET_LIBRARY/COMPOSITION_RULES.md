# Preset composition and conflict handling

Never concatenate canned keyframe streams without checking shared physical state.

1. Declare persistent actor IDs and object IDs; store world root and local rigs separately.
2. Build a timeline DAG (event IDs, prerequisites, resource/contact ownership, consequences).
3. Select one primary narrative goal per shot, plus supporting camera and audio presets.
4. Insert actors' `perceive/decide/prepare` stages; allow reflex exceptions only with intent.
5. Resolve hand/foot/doorway/contact resources: one foot cannot be fixed to two inconsistent supports; a prop cannot be exclusively owned by both hands unless explicitly shared.
6. Camera and sound follow the same information graph but have independent transforms/audio world locations.
7. Conditional variants: change style/emotion or bodyplan/scaling only after reviewing `01_RULES/CREATURE_SIZE_ADAPTATION.md`.
8. Before code generation, surface conflicts and choose a grounded resolution. A "cinematic" adjective alone never justifies altering physical path.
9. Output pre-state, event timeline, pose/contact table, camera shot plan, sound event spotting, failures, validation plan and knowledge source IDs.
10. Promote evidence only after implementation and inspection; structured preset generation alone is L2.
