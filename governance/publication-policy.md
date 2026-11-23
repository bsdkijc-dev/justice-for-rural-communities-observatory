# Publication Policy (GitHub, Kaggle & Web)

## 1. Pre-Publication Checklist
Before any dataset, notebook, report, or static site is published to GitHub, Kaggle, or the web, the **Data Governance Agent** must verify and the **Human Reviewer** must approve:
- [ ] Source license and redistribution permission verified (`P1` or `P5` only).
- [ ] Zero PII and low re-identification risk confirmed.
- [ ] Missingness, denominators, and observation periods explicitly documented.
- [ ] Schema validation and automated tests pass (`python3 -m unittest discover -s tests`).
- [ ] Synthetic data (`P5`) clearly labeled and never presented as empirical findings.
- [ ] Disclaimer of institutional independence included.

## 2. Channel Scope
- **GitHub:** Source code, research protocols, JSON schemas, documentation, synthetic examples (`P5`), approved aggregate findings (`P1`), reproducible notebooks.
- **Kaggle:** Approved and documented datasets (`P1`), clearly labeled synthetic training/demo data (`P5`), reproducible notebooks, data dictionaries, and limitations.
- **No Auto-Publication:** No agent may push, upload, or publish without explicit human sign-off.
