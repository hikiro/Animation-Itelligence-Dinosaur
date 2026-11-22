# AI-01 data contract

All JSON Lines are UTF-8; each line is an independent JSON object. Generated CSVs are convenience exports and may encode lists as JSON strings.

## Dataset rows

`LEXICON.jsonl`: `id`, `lemma`, `display`, `pos`, `domain`, `group`, `tags`, `origin`, `status`, `source_ids`, `note`, `split`.

`CONTEXTUAL_LEXICON.jsonl`: `id`, `lexeme_id`, `lemma`, `part_of_speech`, `semantic_domain`, `context`, `context_intent`, `example_request`, `contextual_interpretation`, `camera_policy`, `sound_policy`, `motion_policy`, `negative_constraint`, `origin`, `evidence_level`, `source_ids`, `tags`, `split`.

`ACTION_CONTEXT_CASES.jsonl`: `id`, `base_action`, `surface_instruction`, `meaning`, `scene_context`, `actor_role`, `stimulus`, `prior_state`, `character_belief`, `actor_goal`, `observable_action`, `body_cues`, `camera_direction`, `audio_direction`, `editorial_direction`, `action_completion_test`, `contact_or_ownership_required`, `context_warning`, `origin`, `evidence_level`, `source_ids`, `production_verified`, `scene_id`, `tags`, `split`.

`AMBIGUITY_TESTS.jsonl`: `id`, `token`, `valid_interpretation`, `domain_hint`, `required_context`, `anti_assumption`, `status`.

`DIRECTOR_EVAL_CASES.jsonl`: `id`, `director_request`, `scene_context`, `intended_viewer_inference`, `required_action_evidence`, `ambiguity_resolution`, `reject_if`, `status`, `source_ids`, `requires_blind_human_rating`, `audio_required`, `notes`. They are **unscored** evaluation prompts, not a score or observed scripted events.

`INSPECTED_SOURCE_OBSERVATIONS.jsonl`: `id`, `work`, `source_id`, `source_url`, `location`, `observed_phenomenon`, `usable_principle`, `inspection_method`, `evidence_level`, `copyright_policy`, `observed_by`.

## Runtime constraints

- No record may claim `L4` or `L5` without actual media evidence and independently recorded pass/fail.
- Source IDs must match `SOURCE_CATALOG.json`; `[]` is correct for synthetic data.
- `source_url` points to an external source; do not embed source assets or long copied text.
- Every generated context variation retains `lexeme_id` or `base_action`; context isn't a new independent human annotation.
- Split leakage: same lemma or base action may not appear in multiple splits.
- `production_verified: false` on all current AI-01 action cases; these are proposal blueprints.

## Future schema evolution

New fields should be additive and versioned. For truly annotated media, add `asset_license`, `media_hash`, `shot_timestamp`, `panel_coordinates`, `actor_visible`, `source_sound_time`, `camera_pose`, `annotation_author`, `reviewer`, `inter_annotator_agreement`, and `evidence_filepath`. Never populate such fields with invented measurements.

## Source-of-truth and export updates

The JSONL files are canonical research records. If edited, run `python 08_TOOLS/rebuild_ai01_csv.py` for deterministic CSV convenience exports. The CSV is not an independent annotation source and must not be counted twice. `CONTEXTUAL_LEXICON.jsonl` is an explicitly generated expansion; edit these records carefully and keep stable `lexeme_id` and `context`, then rerun AI-01 audit.
