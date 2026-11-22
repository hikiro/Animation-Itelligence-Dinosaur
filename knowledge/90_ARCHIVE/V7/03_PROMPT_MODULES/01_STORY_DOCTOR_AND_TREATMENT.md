# PROMPT 01 — Story doctor, script and causal completeness

## Required input

`02_STORY/01_FILM_TREATMENT.md`, `02_STORY/02_SCRIPT_AND_TIMELINE.md`, `02_STORY/03_WORLD_ACTOR_PROP_STATE.md`, `01_RESEARCH/06_WRITING_AND_ADAPTATION.md`, `01_RESEARCH/05_CONTEXT_COUPLING.md`.

## Copy into agent

> Act as a professional animation story artist and screenplay editor. Audit the 80-second DINO//DISASTER treatment **before** rewriting it. Preserve the established character motivations and eight causal beats. For each scene construct a table with: stimulus, observer knowledge, misinterpretation (if any), goal, anticipation, precise visible action, consequence, emotional turn, and planted setup/payoff. Identify any unmotivated action, impossible simultaneous action, missing setup, broken object ownership or continuity. The main critical flaw to prevent is saying a human exits the portal when the shot merely translates a person from offscreen. Also check why the mother attacks, why human runs while holding egg, why she stops, why the baby follows despite reunion, and why the portal stays open. Propose the smallest changes that improve comprehension. Do not silently invent new plot devices. Produce updated treatment/script and a source-of-truth state table, maintaining frame-duration consistency. Write each beat in externally observable physical verbs. Include a silent-viewing question for each scene and distinguish plan from finished film.

## Required outputs

- `treatment_vN.md` with numbered beats and emotional throughline.
- `picture_script_vN.md` with frame allocation and action completion tests.
- `causal_beat_matrix.md` with entry/exit knowledge and decisions.
- `change_request.md` identifying proposed changes requiring approval; if none, state no change.

## Acceptance

Every major action has a reason and consequence; all egg/baby/portal states follow the state machine; sum of scene frames matches locked total unless explicitly revised; silent viewer can reconstruct the misunderstanding and new twist. Reject if “mood” or “cinematic” language replaces actions.
