# Source Verification Policy

Every authoritative source recorded in `sources/source-register.csv` must be verified against the following 12 metadata attributes before use:
1. `source_id` (stable identifier, e.g., `SRC-001`)
2. `institution` (full formal Indonesian institution name)
3. `exact_url` (verified live URL)
4. `dataset_or_document_title`
5. `publication_date` (ISO `YYYY-MM-DD` or `YYYY` if only year published)
6. `observation_period`
7. `geographic_coverage`
8. `methodology`
9. `update_frequency`
10. `access_conditions`
11. `reuse_and_redistribution_terms`
12. `retrieval_date` & `provenance`

Unverified URLs, dead links, or sources with unclear institutional authority must be flagged `PENDING_VERIFICATION` and excluded from `P1` release.
