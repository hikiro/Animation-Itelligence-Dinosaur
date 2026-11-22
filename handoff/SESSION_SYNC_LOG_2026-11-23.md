# GitHub Handover and Sync Operations Log — 2026-11-23

## Scope and authority

The user instructed a complete GitHub backup of this conversation's animation research and all available artifacts at `hikiro/Animation-Itelligence-Dinosaur`, with a current, explicit cross-chat handover. This log records **verified operational results**, not artistic validation. The canonical V8 ZIP and its embedded file manifest are retained **unchanged** so their historical integrity remains reproducible; newer operations are recorded outside that frozen snapshot.

## Evidence-backed actions

1. Inspected target repository via authenticated GitHub connector: repo initially empty, `main` default, push permitted.
2. Reopened available conversation files in `/mnt/data`, including original 4-style source ZIP (13 entries), research ZIPs V2–V8, 12-second preview, independent QA reports and user-provided short-form structure reference. Confirmed original ZIP contained no obvious credentials with basic pattern screening; this is not a security guarantee.
3. Extracted V8 snapshot and read actual `README.md`, `AGENTS.md`, DINO status, benchmark and decisions rather than relying on conversation recollection.
4. Wrote **root** `HANDOVER.md`, `README.md`, `AGENTS.md`, `BACKUP_MANIFEST.md`, `LOCAL_ARTIFACTS_SHA256.tsv` with research goals, immutable decisions, strict context/QA, chronological releases, source gaps and future agent actions.
5. Transferred and committed **365 text files**, including all canonical V8 text except SQLite and larger research datasets (present in V8 ZIP), historical V7 readable documentation, full source audits and cinematic director references.
6. Transferred full original V2–V8 binary ZIPs via base64 staging and authenticated GitHub binary-blob creation. Locally computed Git-blob SHA matched each returned GitHub blob SHA.
7. Transferred exact original user editable source as 10 × 1MB/327,572B binary Git blobs after single 9.3MB request failed with an HTTP/2 body error. Added `tools/reassemble_original.py`. Reconstructed the ZIP locally, validating **9,327,572 bytes**, SHA256 `48cfd510a01155bbfa7d6e40380957e3258b9895f56c1d53fe10a77127216b0e` and no ZIP CRC errors.
8. Transferred preview MP4, short-form reference image and extracted story-logic frame montage. Original contact sheet remains within the editable source ZIP and V8 history.
9. Confirmed GitHub `main` returned **388 file blobs** before this log was appended, Git tree `truncated=false`, expected releases/parts/rulebooks/handovers present, full V8 archive blob size **2,384,297B**.

## Engineering caveats

- A container-hosted direct `git push` was unavailable due lack of DNS/network, so authenticated GitHub connector commits were used.
- A direct 9.3MB blob transfer failed due HTTP/2 response-size constraint, **resolved by binary parts with SHA validation**.
- `knowledge/` browsable documents are a convenience mirror; V8 ZIP is the authoritative whole snapshot containing **large .jsonl corpora, media and database**.
- No exact transcript export of every user/assistant utterance was available; `HANDOVER.md` is a detailed reconciled and source-crosschecked project record, not a verbatim transcript.
- Scope of archive integrity is file presence and hashes; user-approved portal benchmark **remains unproduced**, full 80s short **unfinished**.
- This log is an append-only operational record; do not alter the frozen V8 ZIP manifest to claim an originally older archive had newer work.

## Session continuation steps

1. Clone repository, read `HANDOVER.md` and `AGENTS.md`.
2. `python tools/reassemble_original.py` when the original first prototype is required.
3. Extract `releases/ANIMATION_INTELLIGENCE_KNOWLEDGE_REPO_V8.zip`, run `python 08_TOOLS/audit_repo.py` within its archive root; respect its original expected manifest.
4. Browse `knowledge/01_RULES`, `02_RESEARCH`, `03_PRESET_LIBRARY`, `06_PROJECTS/DINO`, `07_LOGS`.
5. Continue AI-01 context-rich real source study / AI-02 tests, then render and independently QC the 270-frame portal benchmark.
6. Maintain logs and GitHub commits with exact evidence status and a fresh handover; do not edit snapshots retroactively.