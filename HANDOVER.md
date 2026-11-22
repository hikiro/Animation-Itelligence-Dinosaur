# FULL HANDOVER — Animation Intelligence / DINO//DISASTER

**Last reconciled:** 2026-11-23 (Europe/Berlin)  
**Canonical GitHub repository:** https://github.com/hikiro/Animation-Itelligence-Dinosaur  
**Primary current knowledge release:** V8 (`releases/ANIMATION_INTELLIGENCE_KNOWLEDGE_REPO_V8.zip`, once verified on GitHub)  
**State:** Knowledge engineering / AI-01 research active; cinematic 9-second portal benchmark **not yet produced and approved**.

> **Start here.** This document contains the decisions, research philosophy, assets, evidence status, open work, pitfalls, and exact navigation required for a new ChatGPT conversation or coding agent. Do not infer that past reports describing a check mean an animation is artistically correct.

## 0. The next agent's mandatory first 10 actions

1. Read `HANDOVER.md` completely. Then `AGENTS.md`, `README.md`, `knowledge/README.md`, `knowledge/AGENTS.md`, `knowledge/00_START_HERE/READ_ORDER.md` (if the unpacked tree is present).
2. Read `knowledge/01_RULES/ANIMATION_RULEBOOK.md`, `DO_AND_DONT.md`, `GOOD_ANIMATION.md`, `CONTEXT_AND_STORY.md`, `RIGGING_BODYPLAN_BLUEPRINTS.md`, `CREATURE_SIZE_ADAPTATION.md`.
3. Read `knowledge/06_PROJECTS/DINO/STATUS.md` and `BENCHMARK.md`; read `knowledge/07_LOGS/DECISIONS.md`, `CONFLICTS.md`, `SESSION_LOG.md`.
4. Identify actual available binaries and media in `assets/` or `releases/`; check `BACKUP_MANIFEST.md`. Historical artifacts are not necessarily included in the unpacked canonical tree.
5. Run `python knowledge/08_TOOLS/audit_repo.py` if that folder is present. If using only the ZIP, extract it and run `python 08_TOOLS/audit_repo.py` inside the extracted project root.
6. Search existing research **before inventing a technique**: `python knowledge/08_TOOLS/search_repo.py "portal crossing"` and inspect `knowledge/03_PRESET_LIBRARY/INDEX.md`.
7. Read `knowledge/02_RESEARCH/ACCESS_GAPS.md` and `research/ACCESS_GAPS.md`; they distinguish *not acquired*, *not attempted*, *inaccessible*, and *not validated*.
8. Confirm a task's scope and evidence level. Preserve approved decisions. Reproduce a test; do not assert an L5 completion based on source syntax, JSON validation, or file existence.
9. Work the `PLAN → BUILD → RENDER → INSPECT → LOG → FIX → RE-TEST → CHECKPOINT` loop, with exact evidence, error logs, frame references, and causal action-completion criteria.
10. Update `knowledge/02_RESEARCH/LEARNING_LOG.md`, `knowledge/07_LOGS/SESSION_LOG.md`, relevant preset/defect, `HANDOVER.md` and `BACKUP_MANIFEST.md` at the end of every milestone. Commit files; verify on GitHub after writing. If a tool is inaccessible, report exactly what was not uploaded.

## 1. North-star vision (the user's intent)

Build **Animation Intelligence**, a deeply organized, evergreen knowledge repository plus reusable, composable scenario presets, designed so ordinary/general language models can create credible animation from natural language. The system is not a finite lookup table: the agent must understand scene context, characters' knowledge and goals, emotion, physical and compositional constraints, the audience's knowledge, style, scale, camera and sound—and then select and adapt techniques.

Translate both directions:
- **Human direction →** story intention, event graph, acting poses, joints and constraints, staged action, camera plan, sound cues, layers/solids/rigs/expressions, deterministic rendering code, QA.
- **Code and render →** plain-language explanation of what happened, why a technique works/fails, contextual alternatives, reproducible fix.

Example: “make the impact understandable” means a visible causal chain, not simply `wiggle()` or a flash. A shooter may anticipate and recoil; projectile travel may receive a cinematic camera treatment or stylized time remapping; target contact must be spatially unambiguous; the target then responds, recoils, and falls or recovers. Physical projectile curve, camera tracking curve and time/speed curve are **different** choices—never conflate them.

## 2. Stable seven research domains — NEVER renumber these

| Domain | Mission | Current reality |
|---|---|---|
| AI-01 Action semantics and character intention | Phrases, verbs/adjectives/nouns, scripts, drawn boards, goal/belief/perception, causality | **CURRENT PRIORITY**. 42-action experiments and 6,146-row mixed-provenance corpus exist; mostly synthetic; real matched examples remain needed |
| AI-02 Physics / rigging / interaction | Center of mass, ground/hand contacts, IK, constraints, scale, anatomy, creature locomotion | Researched/design stage; production-ready rig, interaction engine unverified |
| AI-03 Camera intelligence and visual perception | Lens, blocking, 180-degree rule, gaze matches, motivated framing, eye-trace, viewpoint | Rulebooks researched; decision engine not validated |
| AI-04 Sound-event intelligence | Source/material, Foley, distance, perspective, silence, music and event-driven timing | Rules researched; sound-event engine and perceptual validation pending |
| AI-05 Code and expression engineering | After Effects expressions/solids/mattes/puppet and cross-engine Remotion implementations | Examples documented, some syntax-checked; **not tested in actual AE** |
| AI-06 Automated + human QA | Contact tracking, continuity, viewer comprehension, media/audio QC | Structural test harnesses built; advanced perception testing incomplete |
| AI-07 Style-specific animation grammars | Anime, paper-cut, rubber hose, pixel art, collage, documentary, motion graphics | Style concepts/presets drafted; specific variations not L5 validated |

**Research records must include:** unique ID, human phrase, exact context, character/audience beliefs, emotional intention, physical state, camera/audio interpretation, implementation, source/provenance, observation vs synthetic status, assumptions, failure cases, tested proof, confidence/evidence level and dependencies. Context is not optional. Maintain an unresolved sources ledger so the user can supply missing training data later.

## 3. Required permanent documents / anti-hallucination protocol

- `knowledge/01_RULES/ANIMATION_RULEBOOK.md`: immutable/fundamental quality criteria, exceptions, tests.
- `knowledge/01_RULES/DO_AND_DONT.md`: grounded best/bad practices with relevant contexts.
- `knowledge/01_RULES/GOOD_ANIMATION.md`: separate story/acting/physics/camera/editing/audio/craft rubric.
- `knowledge/01_RULES/RIGGING_BODYPLAN_BLUEPRINTS.md`, `CREATURE_SIZE_ADAPTATION.md`: morphology/body plan, support contacts, limb lengths, mass cues, creature size, orientation, audience scale cues; don't equate mass directly to animation speed.
- `knowledge/02_RESEARCH/LEARNING_LOG.md`: accumulated, dated, reference-linked lessons; always updated.
- `knowledge/02_RESEARCH/SOURCE_LEDGER.md`, `ACCESS_GAPS.md`: source provenance and items unavailable/not yet obtained (do not invent failed lookups).
- `knowledge/07_LOGS/DECISIONS.md`, `CONFLICTS.md`, `SESSION_LOG.md`, `VALIDATION.md`: why choices were made, conflicts, session work and actual tests.
- `knowledge/03_PRESET_LIBRARY/`: 90 draft presets designed for broad composability, not evidence of 90 approved animations.
- `HANDOVER.md` and `BACKUP_MANIFEST.md`: precise current state and backup completeness.

**Evidence levels**: L1 = source-backed principle; L2 = researched design/hypothesis/preset; L3 = code executed/structural check; L4 = actual visual and audio media inspected; L5 = defined production-quality gates and regression tests passed. Tag claims separately; never upgrade whole projects by proxy.

**Lost/confused/hallucination response:** STOP → inspect actual repository and Git refs → identify last verified commit/asset hashes → list claims lacking evidence → read AGENTS/STATUS/defects → reproduce small failing case → log new hypothesis → change approach after two failed fixes → rerender and inspect → update logs. Do not improvise non-existent paths, files, metrics or successful upload claims.

## 4. DINO//DISASTER — locked story and production constraints

**Episode 1:** `WRONG EXIT`, approximately 80 seconds, 1080×1920 at 30fps (2,400 planned frames), handmade Japanese-inspired layered paper-cut / original 2D animation, largely dialogue-free with original character Foley/ambience/music. User-approved short series continues across episodes.

Narrative beats: portal opens → human **really crosses** out → egg falls from nest and human catches it → protective mother misreads the scene as theft → she charges and chases → egg cracks and baby hatches → human places baby safely, mother reunites → human exits through portal → baby deliberately follows → mother notices and pushes into modern apartment → cliffhanger. This is an 8-scene *treatment*, not a film already delivered.

Character motivation: human curious/kind/easily frightened; mother protective, not inherently evil; baby bonds with rescuer. Must preserve continuity of eye targets, awareness, gaze before body, mass/stride/contacts, egg ownership/release, scale, world screen direction, portal front/back depth masks and position. Sounds must be tied to actual visual contact frames and acoustic perspective, not arbitrary timestamps.

**LOCKED first production task:** produce a **9-second / frames 0–269 / 30fps / uninterrupted portal-crossing benchmark** before building the 80-second film. Planned action timing:
- 0.0–1.6s portal materializes with base physically touching ground and environmental interaction.
- 1.6–2.8s human appears *inside the opening*, not on offscreen margin.
- 2.8–4.2s leading foot visibly crosses threshold, plants on terrain, weight transfers.
- 4.2–6.4s hips/torso/trailing leg cross; front/back masking remains correct.
- 6.4–7.2s settles, knees/arms follow through.
- 7.2–9.0s eye and head lead an intentional curious environmental reaction.

Audio: portal opens with intentional distance/perspective, ground footsteps on actual planted events, breathing, atmospheric birds/forest; no annoying constant synth or music that masks Foley. Camera motivated by audience understanding and held long enough for threshold proof.

**As of this handover, benchmark has NOT been production-rendered and approved.** Existing short MP4s are schematic teaching comparisons and 12-sec silent preview reel; they do not satisfy the benchmark. Do not claim otherwise.

## 5. Retrospective: what was wrong in original 4-style DINO footage

Original `DINO_FOUR_STYLES_EDITABLE_PROJECT(1).zip` includes ~5-second Candy, Pop-art, Rubber-hose and Paper-cut experiments and a comparison reel. Technical video decode passed but creative quality failed:
- person slides in from the **screen edge**, *does not* actually come out of portal; portal too high above feet, missing occlusion/threshold staging;
- dinosaur visible prematurely; no discovery/recognition before threat; human reaction not connected to stimulus;
- fast entrances (~44–51 px/frame observed), missing convincing contact, foot slide/skating; arbitrary locomotion/pose switches;
- first three styles differ mainly in appearance rather than movement grammar; chase lacks spatial threat/closure; weak cliffhanger;
- typography/mobile safe-area problems; audio and Foley not consistently contact-linked;
- native project is custom Canvas animation inspired by techniques rather than native Remotion/Ant Motion, per source audit.

Source reports: `audits/DINO_ANIMATION_QUALITY_AUDIT.md`, `audits/ANIMATION_QA_STANDARD_FOR_FUTURE_VIDEOS.md`, `audits/MOTION_STORY_LOGIC_QA.md` (if published), and `archives/` original editable ZIP. A technically valid render must not be called artistically good.

## 6. Historical releases & inherited research (do not discard)

- V2: cinema/camera/sound rulebook and 80-second master director prompt.
- V3: modular 13 prompt system, 24 shot cards, agent state/recovery workflow, 270-frame benchmark specification.
- V4: After Effects expression concepts, layered compositing and context-language translation research.
- V5: 42 action recipes and three **schematic** before/after comparison MP4s, JS action sampler.
- V6: AI-01 corpus: 1,152 lemmas, 4,608 synthetic context variations, 208 action/context combinations, 120 ambiguities, 18 source-linked observations, 40 evaluation prompts (reported total 6,146). These are NOT 6,146 independently proven filmmaking observations.
- V7: user storyboard/short-form framework **Hook → Lead → Body 1 → Open loop → Body 2 → Open loop → Body 3 → CTA** (reference `REF-STORY-0001`; use contextually, not dogmatically). Added missing-source register and research index.
- V8: canonical 90 composable, **design-level** scenario presets; body plans/creature size, rulebook, logs and preserved V7 history. Reorganization and structural tests, not 90 L5 animations.

The complete V8 archive is preferable to copying old V7 files out of context; its `90_ARCHIVE/V7/` preserves provenance. All earlier release ZIPs are historical snapshots, not active truth.

## 7. Current evidence limits and next work

**Current priority: deepen AI-01 real-production evidence, then AI-02 physical interaction testing.** Acquire licensed/accessibly inspectable matched script → storyboard drawings → animatic → final shots, add audio cues/stems, annotate actor goals, emotion, staging and event source. Collect diverse verbs/adjectives/nouns/sound cues, not just ~50 actions. Run 3-context same-event experiment (dinosaur stomp: threat, comedy, wonder); keep constant world/physical event, change gaze/poses/camera/audio/timing, assess viewer comprehension. Distinguish synthetic training material from real production evidence.

Then implement properly articulated rig, ground locking, reach/grip/release, full-body recoil, portal occlusion, and the nine-second actual render. Key open evidence: actual Adobe After Effects expression execution, creature species-specific locomotion reference, real sound stems/licenses, matched professional storyboard footage, independent silent-viewer comprehension, calibrated perceptual quality thresholds.

**Blocked / missing**: see `knowledge/02_RESEARCH/ACCESS_GAPS.md`, and inherited `knowledge/90_ARCHIVE/V7/15_MISSING_AND_UNVERIFIED_SOURCES/`. User can provide manuals, licensed clips, storyboards, rigs, screenshots and audio. Record exact source and permissions; do not fabricate attempted retrievals.

## 8. How to use the repository in a new chat

Suggested opening message:
> Take over https://github.com/hikiro/Animation-Itelligence-Dinosaur. Read HANDOVER.md, AGENTS.md, README.md, knowledge/README.md and the rulebooks, then audit actual file presence. Do not assume any film is finished. Use the seven-domain taxonomy; preserve all user-approved decisions. Find research context, open gaps and current DINO benchmark status. Continue from the next incomplete evidence-backed task; maintain detailed learning/source/defect/decision/conflict logs, update HANDOVER.md and commit. Ask for external assets only when they are required and unavailable; never invent successful tests or uploads.

**Resume point:** AI-01 real matched-source evidence / context-specific acting experiments or AI-02 foundational interaction tests; do **not** skip to 80s final render. For hands-on creation, prioritize nine-second portal benchmark as the gated product deliverable.

## 9. Backup integrity boundary

This handover is a **reconstructed and reconciled project record**, not a verbatim export of every chat message. Media, ZIPs and original attachments must be checked in the GitHub repository individually; paths in this document are planned until verified in `BACKUP_MANIFEST.md`. GitHub storage is an explicit backup of uploaded content; it is not proof of animation quality or provenance clearance. Do not publish private tokens or third-party nonredistributable materials.
