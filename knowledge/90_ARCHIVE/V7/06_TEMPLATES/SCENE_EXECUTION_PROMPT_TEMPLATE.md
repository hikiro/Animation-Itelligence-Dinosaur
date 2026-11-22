# Reusable single-scene agent prompt template

> **DEPARTMENT:** Direct and animate scene `[SCENE_ID]` / shot `[SHOT_ID]` using the attached kit. **READ:** `AGENTS.md`, `09_HANDOFF/STATUS.md`, accepted story state, `01_RESEARCH/05_CONTEXT_COUPLING.md`, selected shot card, relevant rig and sound docs.
>
> **STORY EVENT:** `[what physically changes]`. **ACTOR'S KNOWLEDGE AND GOAL:** `[why it moves]`. **AUDIENCE QUESTION:** `[what to learn or anticipate]`. **REQUIRED VISIBLE PROOF:** `[specific body/object/threshold contact sequence]`. **START STATE:** `[location, facing, object ownership]`. **END STATE:** `[world, actors, portal, props]`.
>
> **MOTION DIRECTION:** `[anticipation, primary poses, contact, inertia, settle, frame ranges]`. **CAMERA DIRECTION:** `[POV, axis, shot size, lens metaphor, move purpose, first/last composition, parallax]`. **SOUND DIRECTION:** `[source, objective/subjective, distance, timing class, bed, Foley, music silence, exact event map]`.
>
> **IMPLEMENTATION:** Frame-addressable, separate camera/world, articulated assets and deterministic seeks. Provide exact paths and render commands.
>
> **QC:** Render actual frames around decisive action; inspect normal speed, mute, SFX-only and full mix; log differences, repair, rerender, regression-check. Do not claim completion if only code or plan exists. If a blocker persists twice, run `04_TRUTH_AND_RECOVERY.md` root-cause isolation. Update status and open defects before concluding.
