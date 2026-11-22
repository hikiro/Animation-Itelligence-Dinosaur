# Composable scenario preset library

These presets are **context-sensitive production hypotheses**, not guaranteed ready-made animation. Each has intention, event phases, rig/contact, camera, sound, body-size adaptation, failure pattern, QA and provenance. Combine compatible presets with `08_TOOLS/compose_prompt.py` then revise based on actor and story.

Presets are atomic by design: e.g. `notice sound` + `heavy stomp` + `turn away` + `panic run` + `camera reveal` + `offscreen footstep` can be assembled for one threat scene. Structural completeness is not media validation.

**Composition order:** story goal → actor/world state → causal event graph → rig/contact → camera → audio → timing → QA. Flag conflicting requirements and fixed actor ownership (one prop cannot be attached to two noncoincident hands without transfer). Crossfades/blur/shake do not solve incompatible world positions.

Use `python 08_TOOLS/search_repo.py "stomp"` and `python 08_TOOLS/compose_prompt.py PRE-0019 PRE-0044 --context threat --out /tmp/director_prompt.md` with actual IDs from index. For novel scenarios, use `03_PRESET_LIBRARY/TEMPLATE.md` and assign next ID.
