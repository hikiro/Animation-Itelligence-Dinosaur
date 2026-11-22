# Taxonomy, evidence grades, and tagging conventions

## Categories (`kind`)

- `lesson`: generalizable instruction with limitations and a test
- `case-study`: exact version of a real artifact and what was inspected
- `research-note`: findings grounded in a cited source, distinct from our interpretation
- `experiment`: controlled test with predicted and observed result
- `workflow`: production methods and recovery rules
- `index`: navigation, not primary evidence

## Primary tags (controlled vocabulary)

`story-logic`, `acting`, `motivation`, `gaze`, `anticipation`, `portal`, `occlusion`, `geography`, `rigging`, `stance`, `gait`, `contact`, `weight`, `physics`, `secondary-motion`, `timing`, `spacing`, `style-grammar`, `paper-cut`, `camera`, `blocking`, `composition`, `lenses`, `editing`, `continuity`, `sound`, `foley`, `sound-perspective`, `mixing`, `silence`, `music`, `frame-events`, `export`, `render-qc`, `brand`, `mobile`, `research`, `agent-recovery`, `audience-attention`.

New tags are allowed, but add them here and add an alias where relevant. Use comma-separated tags in metadata. Prefer one subject per lesson rather than extremely broad files. Related documents should link by stable `LRN` or `CASE` IDs.

## Claim statuses (always be specific)

- `observed-issue`: flaw seen in actual available render or source and documented as such
- `source-backed`: source directly supports the stated general principle; does not mean our animation was tested
- `production-heuristic`: a reasonable project practice synthesized from research or experience; context-dependent
- `proposed-fix`: suggested correction, no verified post-fix result yet
- `hypothesis`: uncertain mechanism, to be tested
- `fix-verified`: before/after render and inspection confirm a specific outcome under defined test
- `unverified`: claim or artifact not independently examined
- `editorial-judgment`: subjective director assessment, accompanied by explicit rationale and evidence

An observed original fault plus a proposed remedy is **not** `fix-verified`. Preserve both if a note covers them.

## Metadata convention

New lessons and cases begin with YAML-like flat frontmatter:

```text
---
id: LRN-0001
title: Portal emergence must occur visibly
kind: lesson
status: observed-issue
tags: portal, occlusion, geography, story-logic
source_ids: CASE-0001, S02
related_ids: LRN-0002, LRN-0008
applies_to: scene-01, 2d, 2.5d
updated: 2026-11-19
---
```

The shipped search parser supports plain scalar metadata values, not nested YAML. Keep tags and IDs comma separated. For a source quote, record URL, date reviewed, and passage location; do not use fabricated exact quotations.

## Evidence minimum

| Claim | Minimum supporting record |
|---|---|
| Observed visual flaw | File version/path, timestamp/frame, expected vs actual, inspection method |
| Observed audible flaw | Actual audio path, exact cue/time, listening method/device; otherwise inspect cue schedule only |
| Source-backed statement | Traceable URL/identifier and source-specific claim; separate interpretation |
| Fix verified | Before/after version, contact frames/clip, pass criteria, result |
| Editorial assessment | What viewer should infer, why it fails, and alternative explanations |

A score, arbitrary pixel threshold or single still is never sufficient proof of overall animation quality.

## V4 vocabulary additions

Tags: `after-effects`, `expressions`, `solids`, `layers`, `shape-layers`, `nulls`, `track-matte`, `masks`, `precomps`, `graph-editor`, `speed-curve`, `impact`, `projectile`, `recoil`, `manga`, `viewer-knowledge`, `direction-translator`.

New stable identifiers: `GOAL-###` evolving directions; `CONFLICT-###` trade-offs; `INT-###` input translation examples; `S##` technical research sources. Technical mechanism records must distinguish **verified Adobe tool semantics** from **not-run user-scenario expressions**.
