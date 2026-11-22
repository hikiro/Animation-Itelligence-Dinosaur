# Portable release workflow

After any canonical research/preset change:

1. Append a contextual learning entry with source IDs, tests actually run and evidence level.
2. Update living Do/Don't and Rulebook only if a general principle changed; retain exceptions. Update `07_LOGS/DECISIONS.md` and `07_LOGS/CONFLICTS.md` if user direction altered a prior constraint.
3. Add new preset and catalog/index entry with a stable unique ID; never reuse a retired ID.
4. `python 08_TOOLS/search_repo.py --rebuild`.
5. `python 08_TOOLS/release_zip.py --audit` generates the SHA256 manifest, checks structural contracts and produces a portable zip. Use an explicit release filename; never overwrite historical ZIP without recording the version.
6. Extract release elsewhere and run `python 08_TOOLS/audit_repo.py` again.
7. Report structural results separately from media/camera/sound evaluations. Store render evidence and tests in the project folder before moving to L4/L5.

Original V7 files under `90_ARCHIVE/V7/` must not be edited. To correct historic inaccuracies, add an errata lesson or canonical supersession record and link it back.
