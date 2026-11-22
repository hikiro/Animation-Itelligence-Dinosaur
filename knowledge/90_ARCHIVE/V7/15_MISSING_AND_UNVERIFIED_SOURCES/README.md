# Missing, unavailable, unverified or not-yet-collected materials — permanent register

**Canonical machine-readable list:** `REGISTER.csv`. Do not delete an item simply because it was later supplied: change status to `RECEIVED`, record artifact path/hash, source permissions and verification outcome in the intake log. Preserve history.

We distinguish: `NOT_PROVIDED`, `NOT_COLLECTED`, `NOT_VERIFIED`, `NOT_TESTED`, `NOT_PRODUCED`, `TOOL_NOT_VERIFIED`, `RIGHTS_REVIEW`, `ACCESS_FAILED`, `LINK_DEAD`, `PAYWALLED`, `UNREADABLE`, `RECEIVED`, `VERIFIED`.

- `NOT_COLLECTED` **does not mean** we searched unsuccessfully or tried the source and failed.
- `NOT_PROVIDED` means the user has not supplied the original item.
- `ACCESS_FAILED` is allowed ONLY with a documented URL, date, tool/method and error.
- `RECEIVED` does not mean authenticity, permission, or correctness verified.
- Each status update must preserve date and evidence in `INTAKE_AND_ACCESS_LOG.md`.

### Quick lookup

```bash
python 08_TOOLS/search_materials.py --list
python 08_TOOLS/search_materials.py --query storyboards
python 08_TOOLS/search_materials.py --status NOT_COLLECTED
python 08_TOOLS/search_materials.py --priority P0
python 08_TOOLS/search_materials.py --id GAP-001
python 08_TOOLS/audit_v7.py
```

### Manual contribution procedure

1. Search for an existing `GAP-###`; do not duplicate entries under a new name.
2. Copy the supplied file into `15_MISSING_AND_UNVERIFIED_SOURCES/INBOX/` or document its exact original URL and rights; never invent a path.
3. Record upload title, supplier, original URL if known, acquisition date, actual file SHA256, format, language, license/usage scope, relevant shots/scene/page/timecode, and whether full audio/video is available.
4. Open **that exact asset** and distinguish directly visible facts from hypotheses. Create a `SOURCE-###` or `REF-STORY-###` note and link it to the relevant AI domain.
5. Change status `RECEIVED`, then `VERIFIED` only after actual source inspection. On access failure, record the command/error.
6. Update `10_KNOWLEDGE/LEARNING_LOG.md`, `10_KNOWLEDGE/INDEX.md`, `09_HANDOFF/STATUS.md`, source ledger, and regenerate manifest/release QA.

Every missing item records **why it matters** and exactly what the user could provide later. Items with P0 are important blockers to full validation, not proof that earlier research is useless.
