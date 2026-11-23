# Justice for Rural Communities Observatory (JRC Observatory)

**Tagline:** *Justice Within Reach. Stronger Rural Communities.*  
**Parent Initiative:** MA Open Justice & Public Prosperity Initiative 2027–2030  
**Status:** Independent research and public-interest knowledge project (SAFE MODE — Phase 1 & Phase 2 setup).  
**Disclaimer:** This project is an independent research initiative. It does not claim official endorsement, authorization, or institutional representation by Mahkamah Agung RI, Badan Pusat Statistik (BPS), Badan Pembinaan Hukum Nasional (BPHN), Kementerian Desa dan Pembangunan Daerah Tertinggal (Kemendesa PDT), or any other government institution.

---

## Research Question

> **How does access to justice shape the wellbeing and economic security of Indonesia's rural communities?**

The Observatory investigates geographic, economic, informational, procedural, digital, and institutional barriers to justice for rural households, smallholder farmers, small-scale fishers, rural informal workers, village-based micro and small enterprises (UMKM), rural women, older persons, persons with disabilities, and communities in remote, border, island, mountainous, coastal, and peri-urban areas.

---

## Repository Structure

```text
justice-for-rural-communities-observatory/
├── README.md
├── LICENSE
├── CITATION.cff
├── CONTRIBUTING.md
├── CHANGELOG.md
├── governance/          # Charter, data governance, privacy, publication, ethics, source verification, risk register
├── research/            # Research questions, conceptual framework, methodology, hypotheses, indicators, limitations
├── schemas/             # 12 JSON Schema (Draft 2020-12) definitions for Datasets 01–12
├── sources/             # Authoritative source register, source assessment report, legal authorities
├── data/                # raw/, interim/, processed/, synthetic/ (P5), approved-public/ (P1)
├── notebooks/           # Reproducible Jupyter notebooks (01–10)
├── src/                 # acquisition/, validation/, transformation/, analysis/, reporting/
├── reports/             # baseline/, thematic/, policy-briefs/, annual/
├── public_knowledge/    # plain_language/, audio_scripts/, frequently_asked_questions/, community_guides/
├── dashboard/           # Lightweight static dashboard prototype (future phase)
├── website/             # Static public knowledge site (future phase)
├── tests/               # Automated schema, taxonomy, and data-hygiene validation tests
└── .github/workflows/   # CI validation workflow
```

---

## Setup & Quickstart

### Prerequisites
- Python 3.11+
- `jsonschema` (`>=4.20`), `pandas` (`>=2.0`), `pyyaml` (`>=6.0`)

### Local Setup
```bash
git clone <repository-url>
cd justice-for-rural-communities-observatory
python3 -m venv .venv
source .venv/bin/activate
pip install jsonschema pandas pyyaml
```

### Run Validation Tests
```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```
Or run the standalone validation script:
```bash
python3 src/validation/validate_all.py
```

---

## Governance & Safe Mode Guardrails

1. **Publication Classification:** Data is strictly classified as `P1` (Public & approved), `P2` (Public source, reuse review required), `P3` (Internal working), `P4` (Restricted/sensitive), or `P5` (Synthetic test data). Only `P1` and reviewed `P5` data may enter public release workflows.
2. **Zero-Imputation & No Fabrication:** Missing official values remain empty (`null`/empty cell) with explicit missingness flags. Synthetic records in `data/synthetic/` are strictly labeled `P5` and must never be used to claim empirical findings.
3. **Human Approval Gates:** No external institutional outreach, survey deployment, restricted system access, or public dataset/report release may proceed without explicit human approval.
4. **Lawful Collection:** No CAPTCHA bypass, authentication bypass, rate-limit circumvention, or unauthorized mass crawling.
