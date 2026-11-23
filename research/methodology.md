# Research Methodology

## 1. Mixed-Methods Design
The Observatory uses six complementary methods:
1. **Judicial Document Analysis:** Analyze publicly accessible decisions from [Direktori Putusan Mahkamah Agung](https://putusan3.mahkamahagung.go.id) to identify dispute patterns and legal issues. *Constraint:* Never infer community dispute prevalence from filed court cases, and never infer actual execution from a judgment.
2. **Official Statistical Analysis:** Use official aggregate data from [BPS](https://www.bps.go.id) (PODES, Susenas, IP-TIK) and [Kemendesa PDT](https://sid.kemendesa.go.id/indeks-desa) (Indeks Desa). Record definitions, denominators, time periods, and geographic coverage; avoid invalid cross-regional comparisons.
3. **Geographic Accessibility Analysis:** Measure distance and estimated travel time only with verified geographic coordinates and road/maritime network data. Distinguish straight-line (Euclidean) distance from actual travel routes. Document assumptions and never fabricate travel-cost estimates.
4. **Survey Research (Gated):** Requires human and ethics approval prior to deployment. Uses informed consent, documents sampling and non-response, separates contact details from responses, and never presents convenience samples as nationally representative.
5. **Interviews & Case Studies (Gated):** Requires ethics and human approval, informed consent, strict participant anonymization, and protection of vulnerable participants. Never fabricate transcripts or quotations.
6. **Comparative Policy Research:** Compare service models (e.g., *sidang keliling*, *Posbakum Pengadilan*, *Posbankum Desa*) only where comparable evidence exists, accounting for geographic and institutional capacity differences.

## 2. Official Rural Classification & Geography Typology
- **Official Baseline:** [Peraturan Kepala BPS No. 37 Tahun 2010](https://ppid.bps.go.id/upload/doc/Perka_BPS_No_37_Tahun_2010___Klasifikasi_Perkotaan_dan_Perdesaan_Di_Indonesia_Buku_2_-_Jawa_1659514400.pdf) classifies each *desa/kelurahan* as *perkotaan* (urban) or *perdesaan* (rural) using a composite score (< 10 = rural) based on population density, share of agricultural households, and access to urban facilities.
- **Complementary Village Development Status:** [Permendesa PDTT No. 9 Tahun 2024 tentang Indeks Desa](https://jdih.kemendesa.go.id/web/regulations/read/indeks-desa-9-2024) consolidates village development metrics into [Indeks Desa](https://sid.kemendesa.go.id/indeks-desa).
- **Geographic Heterogeneity:** Villages are explicitly differentiated as `rural`, `remote`, `border`, `island`, `mountainous`, `coastal`, or `peri-urban` (`geography_type` in Dataset 01).

## 3. Controlled Dispute Taxonomy (`R01`–`R12`)
- `R01` - Land and agrarian disputes
- `R02` - Agricultural and plantation disputes
- `R03` - Fisheries and coastal livelihood disputes
- `R04` - Inheritance and family disputes
- `R05` - Village governance and administrative disputes
- `R06` - Employment and informal work disputes
- `R07` - Rural commercial and UMKM disputes
- `R08` - Credit, debt, and financial services disputes
- `R09` - Environmental and natural resource disputes
- `R10` - Public service and administrative access disputes
- `R11` - Consumer and digital transaction disputes
- `R12` - Other legally verified disputes

*Classification Rule:* Every dispute record supports primary category, secondary category, source, legal domain, geographic scope, time period, verification status, and confidence level. Never classify solely from a single keyword when contextual review is required.
