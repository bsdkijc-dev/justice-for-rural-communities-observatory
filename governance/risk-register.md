# Project Risk Register

| Risk ID | Category | Description | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|---|
| RSK-01 | Legal / ToS | Unauthorized scraping or redistribution of `P2` judicial/statistical portals | Medium | High | Enforce SAFE MODE; verify terms; prefer official bulk/API; block `P2` from `approved-public/` | Data Governance Agent |
| RSK-02 | Privacy | Re-identification of rural litigants or survey respondents in small villages | Medium | High | Strict PII removal; k-anonymity aggregation; separate contact details from Dataset 08 | Privacy / Data Eng Agent |
| RSK-03 | Methodological | Inferring dispute prevalence or causality from filed court cases alone | High | High | Explicit non-causal framing; distinguish filed cases from justiciable problems | Statistical Analysis Agent |
| RSK-04 | Data Quality | Missingness or non-comparability across districts/provinces (e.g., 3T regions) | High | Medium | Zero-imputation policy; explicit missingness flags in Dataset 10; ban premature RJAI rankings | Data Engineering Agent |
| RSK-05 | Reputational | Misperception of official Mahkamah Agung RI endorsement | Medium | High | Prominent independence disclaimer on README, Charter, reports, and public pages | Chief Research Orchestrator |
| RSK-06 | Digital Divide | Over-reliance on online-only dissemination excluding offline rural communities | High | Medium | Produce printable, low-bandwidth, plain-Indonesian guides and audio scripts | Public Knowledge Agent |
