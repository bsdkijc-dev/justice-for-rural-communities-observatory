# Data Governance Policy

## 1. Core Data Principles
1. **Publicly Accessible != Freely Redistributable:** Every external dataset or document must have its reuse, redistribution, and licensing terms verified before ingestion or republication.
2. **Lawful Acquisition Only:** Prefer official bulk downloads and documented APIs. Strictly prohibit CAPTCHA bypass, authentication bypass, rate-limit circumvention, or unauthorized mass crawling. Respect `robots.txt` and website terms of service.
3. **Zero-Imputation & Value Preservation:** Preserve original source values verbatim. Store transformed or derived fields separately. Never fill missing values with invented estimates; keep missing cells empty (`null`) with explicit missingness flags.
4. **Stable Identifiers & ISO Dates:** Use deterministic, stable IDs and ISO 8601 (`YYYY-MM-DD`) dates across all datasets.

## 2. Publication Classification Tiers
| Tier | Label | Definition | Public Release Eligible? |
|---|---|---|---|
| **P1** | Public & Approved | Verified public data with explicit redistribution permission and zero PII | Yes (after human approval) |
| **P2** | Public Source, Review Required | Publicly viewable source where redistribution/bulk reuse terms require legal/policy review | No (until cleared to P1) |
| **P3** | Internal Working Material | Intermediate joins, working notes, unverified drafts | No |
| **P4** | Restricted / Sensitive Data | Personal data, identifiable case records, unredacted survey/interview records | Never |
| **P5** | Synthetic / Test Data | Programmatically generated test records clearly labeled `SYNTHETIC` | Yes (for schema/pipeline demo only, with human approval) |
