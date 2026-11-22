# Starting in another ChatGPT / coding-agent conversation

## What to upload

Upload the full `DINO_DISASTER_AGENT_KIT_V3.zip`; ask the new chat to extract it and read its `AGENTS.md` and `README.md`. If the new chat can operate only on text, provide the package as files/zip and have it review the documents first. Do not assume a new chat can access the previous conversation's files or environment.

## Copy-paste handoff command

> **DINO//DISASTER — RESUME FROM V3 KIT.** Unzip the attached agent kit. Before making any animation, read `README.md`, `AGENTS.md`, every file in `00_START_HERE/`, `09_HANDOFF/STATUS.md`, the `01_RESEARCH/05_CONTEXT_COUPLING.md` directing framework, and the relevant `02_STORY/` and `03_PROMPT_MODULES/` files. Run `python 08_TOOLS/audit_kit.py`. Tell me which files you actually opened and what stage is VERIFIED. Follow the phase gates; do not generate the full 80-second film until the 9-second/270-frame portal benchmark passes visual, physical, story, camera and sound QC. Never claim work is done without inspectable files and defect evidence. Start from the next action authorized by `09_HANDOFF/STATUS.md`.

## First response expected from the new agent

1. Files found, extracted directory and which files were inspected.
2. Current stage from STATUS, not a guessed stage.
3. Specific acceptance test for the next deliverable.
4. Available toolchain and missing capabilities (do not promise unavailable services).
5. Next concrete operation, with outputs and how they will be reviewed.

## Stage-specific commands

- **Planning only:** “Run P0. Create beat map, geography, asset/rig specifications, camera and sound spotting for benchmark. Do not render yet.”
- **Benchmark execution:** “Run P1/P2. Make the 270-frame portal animation, provide editable project, MP4, consecutive-frame evidence, cue sheet and QA.”
- **Review:** “Audit the actual exported MP4 and source. Use `05_QA/`, log defects, and only propose approval after watching and inspecting evidence.”
- **Expansion:** “The 9-second benchmark is approved. Use frozen rig and portal primitives to develop the full 80-second animatic (P3).”

## If the agent drifts

Say: “STOP. Re-read `00_START_HERE/04_TRUTH_AND_RECOVERY.md` and `09_HANDOFF/STATUS.md`. List only VERIFIED artifacts and unresolved defects. Compare your latest output to the locked story. Repair the first broken gate; do not add features.”

## Do not mistake these for real rendered outputs

`07_REFERENCE_V2/` contains archived prompt text and historical critiques. The V3 package is not itself a rendered nine-second video. The benchmark must be produced and tested in the future chat's environment.

## V4 extension

Also read `10_KNOWLEDGE/INDEX.md`, `LEARNING_LOG.md`, goals/conflict logs, and the applicable `11_AFTER_EFFECTS` material. Use `python 08_TOOLS/search_knowledge.py "user's plain-language issue" --expand` before inventing a solution. Use Prompt 13 for any human-language animation task, Prompt 14 only for AE implementation tasks. Explicitly label AE snippets as not run until tested in an AE runtime. Update living logs, not just chat transcript.
