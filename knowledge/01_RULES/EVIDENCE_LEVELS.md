# Evidence model

**Evidence is per claim, not per document.**
- **L0 UNKNOWN / UNATTEMPTED:** Not inspected, no test.
- **L1 SOURCE-GROUNDED:** Authority supports general technique; record exact URL, location, date, claim, limits. Does not imply effect verified in project.
- **L2 DESIGNED:** Proposed semantic interpretation, preset, script or inferred method; label synthetic/generated as such.
- **L3 EXECUTED:** Code or parser tested on documented hardware/runtime; record command/log. Technical success only.
- **L4 MEDIA-INSPECTED:** Actual render/audio inspected at time positions; store artifacts and notes. Does not imply independent audience comprehension.
- **L5 APPROVED:** Explicit story/rig/camera/sound acceptance gates passed with regression and review record.

**Allowed status vocabulary:** `source_backed`, `designed_unverified`, `technical_tested`, `render_inspected`, `production_approved`, `rejected`, `superseded`. Each present-tense claim must point to matching evidence.

**Data integrity:** Synthetic lexicon/context rows must remain synthetic; provenance of supplied visuals must not be guessed. External source access must be separately recorded from licensing/permissions and actual content inspection.
