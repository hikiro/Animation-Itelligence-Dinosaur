# Finding the right lesson without searching the entire conversation

## Search procedure for any incoming task

1. Turn the request into the **physical phenomenon** and the **story context**. Example: "feet look broken" → `foot sliding`, `stance`, `center of mass`, `contact`; "portal didn't work" → `portal`, `occlusion`, `threshold`, `action completion`.
2. Search using a short phrase, inspect top results with file paths and line ranges; rerun with `--expand` if vocabulary differs.
3. Narrow by `--kind lesson` or `--tag sound` / `--tag camera`, not by guessing a filename.
4. Read the **full** top document. Read its `related_ids` and source case studies. Do not use only an excerpt as justification.
5. Before applying a rule, check `When not to apply`, `Limitations`, evidence status, and the particular shot's emotion and audience POV.
6. When finished, append a new `LEARNING_LOG` entry and update the affected lesson with observed outcomes.

## Commands (run from project root)

```bash
# Free text; return exact path, line, metadata, snippet and ranking
python 08_TOOLS/search_knowledge.py "human did not exit portal"

# Expand a synonym family: skating, foot sliding, stance lock, planted foot
python 08_TOOLS/search_knowledge.py "skating" --expand

# Drill down in specialized knowledge
python 08_TOOLS/search_knowledge.py "camera sound reaction" --tag camera
python 08_TOOLS/search_knowledge.py "whole body" --kind lesson
python 08_TOOLS/search_knowledge.py "cut on action" --scope 01_RESEARCH

# Exact entity lookup, related network, and taxonomy browsing
python 08_TOOLS/search_knowledge.py --id LRN-0004
python 08_TOOLS/search_knowledge.py --related LRN-0004
python 08_TOOLS/search_knowledge.py --list-tags
python 08_TOOLS/search_knowledge.py --list-docs --kind case-study

# Machine-readable for an agent: do not assume it is a semantic search service
python 08_TOOLS/search_knowledge.py "portal" --json --top 15
```

PowerShell works identically using `py -3` in place of `python` if configured. Paths with spaces require quotes.

## Query design

- Try **one concise failure phrase**, then **one technical phrase**, then **an alternative contextual phrase** (for example: `character floats`, `ground contact`, `stance freeze`).
- Negative-result fallback: search `--scope 07_REFERENCE_V2` and source ledger, then create a new `RESEARCH_BACKLOG` question. Never invent an existing lesson.
- `--expand` uses authored `ALIASES.json`, not an LLM. It may increase recall but also add irrelevant results; verify the final documents.
- Search reports **document metadata** and line-numbered excerpt. It is not an external web search, PDF search, image embedding retrieval, or audio analysis engine.

## Updating the index

The script scans every source `.md` freshly; no manual reindex step is required for search. Human `INDEX.md` is deliberately curated and must be refreshed on meaningful additions. `python 08_TOOLS/audit_knowledge.py` checks stable IDs and metadata, but cannot determine whether an asserted lesson is true.

## Important separation

- `10_KNOWLEDGE` is **learned principles and experiments**.
- `01_RESEARCH` is **research synthesis and external source tracking**.
- `05_QA` is **acceptance criteria and workflow**.
- `07_REFERENCE_V2` is **archived audit evidence**.
- `09_HANDOFF` is **current production state**, not general lessons.

Always connect them with identifiers and links instead of copying stale claims around.

## V6 — AI-01 specialized lookup

The old Markdown search reads principle notes; the new search reads contextual structured data: `python 08_TOOLS/search_ai01.py --query "sound" --kind lexicon --domain sound_source`. For ambiguity use `--kind ambiguity`; for context-specific action use `--kind action --context threat`; for separately inspected source summaries use `--kind source`; for **unscored** language-evaluation prompts use `--kind eval`.

Search is deterministic keyword matching, not a trained language model; every returned record prints its status and relative file path. The agent must read full context and source constraints, not trust ranking as semantic evidence.
