# Finding answers without rereading a giant ZIP

From extracted repo root, use:

```bash
python 08_TOOLS/search_repo.py --rebuild
python 08_TOOLS/search_repo.py "giant stomp" --limit 10
python 08_TOOLS/search_repo.py "snake support gait" --limit 10
python 08_TOOLS/search_repo.py "portal threshold mask" --limit 10
python 08_TOOLS/search_repo.py "quiet chirp" --limit 10
python 08_TOOLS/compose_prompt.py PRE-0019 PRE-0044 --context threat --creature "giant dinosaur" --scale giant --story "human is frightened by approaching creature" --out example_prompt.md
```

The example IDs are syntax examples, not guaranteed semantic matches; **always read `03_PRESET_LIBRARY/INDEX.md` for actual IDs.**

Search covers canonical V8 Markdown using a dependency-free local SQLite FTS5 database and expands a small synonym list. To find inherited research dataset records, use `python 90_ARCHIVE/V7/08_TOOLS/search_ai01.py --help` and follow that tool's expected root arguments. The archived 6,146-row corpus is mostly synthetic and not automatically approved. Avoid duplicating the same finding across README addenda; link a stable record ID.

For broader search use plain `grep -Rni "phrase" 03_PRESET_LIBRARY 01_RULES 02_RESEARCH`. For source citations read `02_RESEARCH/SOURCE_LEDGER.md`, and for unresolved source acquisition `02_RESEARCH/ACCESS_GAPS.md`.
