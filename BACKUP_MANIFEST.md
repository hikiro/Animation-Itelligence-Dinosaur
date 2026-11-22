# Backup Manifest — Verified GitHub Snapshot

**Repository:** https://github.com/hikiro/Animation-Itelligence-Dinosaur  
**Backup date:** 2026-11-23 (Europe/Berlin)  
**Primary entry:** [HANDOVER.md](HANDOVER.md)  
**Evidence:** GitHub main-branch tree inspection plus local Git-blob hash comparisons for binary attachments.  
**Important:** File integrity and GitHub presence do not imply that an animation passed artistic QA.

## Verified material

| Collection | GitHub path | Status |
|---|---|---|
| Root project handover, instructions and artifact inventory | `HANDOVER.md`, `AGENTS.md`, `README.md`, `LOCAL_ARTIFACTS_SHA256.tsv` | Committed, inspectable |
| Canonical V8 rules, 90 draft presets, research, tools, logs, DINO status | `knowledge/` | 354 searchable text files committed; remaining binaries/large datasets in full V8 ZIP |
| Complete portable V8 snapshot including V7 historical archive, original research corpora and binary experiments | `releases/ANIMATION_INTELLIGENCE_KNOWLEDGE_REPO_V8.zip` | Complete ZIP committed |
| V2 cinematic director kit | `releases/DINO_DISASTER_CINEMATIC_DIRECTOR_PACK_V2.zip` | Committed |
| V3 modular director/agent kit | `releases/DINO_DISASTER_STORY_DIRECTOR_AGENT_KIT_V3.zip` | Committed |
| V4 After Effects / expression research kit | `releases/DINO_DISASTER_ANIMATION_LEARNING_AGENT_KIT_V4.zip` | Committed |
| V5 42-action recipe + schematic experiments | `releases/DINO_DISASTER_ANIMATION_LEARNING_AGENT_KIT_V5.zip` | Committed |
| V6 AI-01 context corpus | `releases/DINO_DISASTER_ANIMATION_INTELLIGENCE_AI01_V6.zip` | Committed |
| V7 short-form structure/reference kit | `releases/DINO_DISASTER_ANIMATION_INTELLIGENCE_STORY_REFERENCE_V7.zip` | Committed |
| Original editable 4-style project ZIP (9,327,572 bytes) | `archives/original_four_styles_parts/*.part000–009` | 10 exact binary parts committed; reassemble with script below |
| Silent 12s animation teaching preview | `media/DINO_Animation_Prototype_Preview_Reel.mp4` | Committed; prototype, NOT benchmark |
| Screenshot-based short-form structure reference | `assets/REF-STORY-0001_shortform_stacked_beats.png` | Committed |
| Original QA 4-style contact sheet | Inside original editable ZIP | Preserved byte-for-byte |
| Extracted story-logic frame sequence | `media/logical_story_frames.png` | Committed |
| Three independent critical quality reports | `audits/` | Committed |
| V2 cinematic and audio director texts | `reference_v2/` | Committed |
| Missing sources, human-supplied-data requests | `research/ACCESS_GAPS.md` and `knowledge/02_RESEARCH/ACCESS_GAPS.md` | Committed |

## Restore original editable prototype

The original 9.33 MB archive exceeded the GitHub connector's single-request limit. It is preserved in **10 byte-exact binary chunks**, not in base64 form.

Clone/download this repository; from its root run:

```bash
python tools/reassemble_original.py
```

Restored output: `DINO_FOUR_STYLES_EDITABLE_PROJECT.zip`. Expected byte size `9327572` and SHA256:

`48cfd510a01155bbfa7d6e40380957e3258b9895f56c1d53fe10a77127216b0e`

The parts were reconstructed and independently checked locally before publication: size matched, SHA256 matched and ZIP CRC returned no bad member. Each published binary part's Git SHA was compared against its locally computed Git-blob SHA.

## Full V8 ZIP integrity

- Path: `releases/ANIMATION_INTELLIGENCE_KNOWLEDGE_REPO_V8.zip`
- Size: **2,384,297 bytes**
- SHA256: `249ed45d9d9df91ecc0a7a161586b6edcad1f275e1e6882f0708b5cd219dc09b`
- Git blob: `cba8b6037cf01f21298540fb8c70f2b78667f2a1`
- Contents: 388 files (includes historical V7 archive and non-text resources). The separate browsable tree is a curated mirror, not a substitute for the portable ZIP.

## Evidence and scope limitations

- No verbatim full-chat transcript was available for export here. `HANDOVER.md` reconciles all major decisions, prompts, studies, QA findings and unfinished tasks from the visible conversation.
- 90 scenario presets and corpus examples are largely **designed or synthetic**. Do not assert they have been independently validated as professional footage.
- The 9-second, 270-frame portal entrance has NOT been completed/approved; the 80-second film has NOT been delivered.
- Third-party links in source notes provide research context, not blanket redistribution rights.
- For missing external script/storyboard/rig/audio samples, see the canonical access ledger. Do not infer that a source was inaccessible when no access attempt occurred.

## GitHub verification method

Retrieve the branch tree with `GET /repos/hikiro/Animation-Itelligence-Dinosaur/git/trees/main?recursive=1`; verify `truncated=false`, intended paths, sizes and Git blob SHAs. Before this manifest update, 387 committed files were confirmed present; the separate logical-story evidence image is added by this final update.

Inspect [HANDOVER.md](HANDOVER.md) for all goals, the seven-domain roadmap, recovered mistakes, exact benchmark plan and next-agent instructions.
