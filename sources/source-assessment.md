# Source Assessment Report & Pilot Geography Proposal (Phase 2)

**Assessment Date:** 2026-11-23  
**Mode:** SAFE MODE (Verification via public documentation and search; no mass crawling or restricted access)  
**Pilot Approval Status:** **APPROVED** (2026-11-23) — Two-Province Comparative Pilot: **Nusa Tenggara Barat (Province Code `52`)** and **Jawa Barat (Province Code `32`)**.

---

## 1. Summary of Verified Authoritative Sources

| Source ID | Institution | Verified Scope & Role | Access & Reuse Assessment |
|---|---|---|---|
| `SRC-001`, `SRC-002` | Mahkamah Agung RI & Kepaniteraan | [Portal MA](https://www.mahkamahagung.go.id) & [Direktori Putusan](https://putusan3.mahkamahagung.go.id) | `P2`: Publicly viewable; no mass crawling or rate-limit bypass. Upload completeness varies by court; decisions do not measure community dispute prevalence or enforcement. |
| `SRC-003`, `SRC-004` | Ditjen Badilum & Ditjen Badilag MA RI | [SK Dirjen Badilum 1084/2024](https://badilum.mahkamahagung.go.id/attachments/article/4523/SK-Juknis-Perma-1-Tahun-2014-sign.pdf) (Posbakum, *sidang keliling*, *prodeo*) & [Ditjen Badilag](https://badilag.mahkamahagung.go.id/) (e.g., 5 new island/rural PA in NTB, Nov 2026) | `P1`/`P2`: Official regulations and service announcements are `P1` for citation; court-level operational metrics require `P2` review. |
| `SRC-005`, `SRC-006`, `SRC-007` | Badan Pusat Statistik (BPS) | [Perka BPS No. 37/2010](https://ppid.bps.go.id/upload/doc/Perka_BPS_No_37_Tahun_2010___Klasifikasi_Perkotaan_dan_Perdesaan_Di_Indonesia_Buku_2_-_Jawa_1659514400.pdf), [PODES 2021](https://www.bps.go.id/id/publication/2022/03/24/ceab4ec9f942b1a4fdf4cd08/statistik-potensi-desa-indonesia-2021.html) (and 2024/2025 regional releases), [IP-TIK 2023](https://www.bps.go.id/id/publication/2024/09/30/b50f00b8615fc8716c8e02d4/in%E2%80%89deks-pembangunan-teknologi-informasi-dan-komunikasi-2023.html) | `P1`/`P2`: Official rural/urban classification (`P1`); PODES and Susenas/IP-TIK provide village/provincial denominators (`P2` pending bulk redistribution check). |
| `SRC-008`, `SRC-009`, `SRC-010` | BPHN - Kementerian Hukum | [SIDBANKUM](https://sidbankum.bphn.go.id/), [Ruang Paralegal](https://plp.bphn.go.id/) / Posbankum Desa, [JDIHN](https://jdihn.go.id/) | `P1`/`P2`: Authoritative for accredited OBH/PBH locations, paralegal/Posbankum Desa rules, and national/local regulations. |
| `SRC-011` | Kemendesa PDT | [Indeks Desa / IDM](https://sid.kemendesa.go.id/indeks-desa) ([Permendesa PDTT 9/2024](https://jdih.kemendesa.go.id/web/regulations/read/indeks-desa-9-2024)) & [Satu Data Indonesia](https://data.go.id/dataset/dataset/data-indeks-desa-membangun-tahun-2024) | `P2`: Village-level development & service access metrics across Indonesia; verify `data.go.id` license terms before `P1` promotion. |

### Key Institutional & Terminology Updates Verified
- **Kementerian Desa:** Now **Kementerian Desa dan Pembangunan Daerah Tertinggal (Kemendesa PDT)** ([kemendesa.go.id](https://kemendesa.go.id/)), transitioning from IDM (2021–2024) to **Indeks Desa (ID)** under Permendesa PDTT No. 9 Tahun 2024.
- **Kementerian Hukum & BPHN:** Actively expanding **Posbankum Desa/Kelurahan** and village paralegal training ([plp.bphn.go.id](https://plp.bphn.go.id/)) alongside [SIDBANKUM](https://sidbankum.bphn.go.id/).
- **BPS PODES:** 2024 and 2025 regional PODES releases are emerging; national 2021 microdata/publications remain a verified baseline until 2024/2025 national aggregates are uniformly published.

---

## 2. Approved Pilot Geography (Two-Province Comparative Pilot)

**Approved Decision (2026-11-23):** Proceed with a **two-province comparative pilot** combining **Nusa Tenggara Barat (NTB, `52`)** and **Jawa Barat (`32`)**, configured in `src/acquisition/pilot_config.json`.

### Pilot Cluster 1: **Nusa Tenggara Barat (`52`) — Rural, Coastal & Island Contrast**
1. **Active Institutional Expansion:** [Ditjen Badilag](https://badilag.mahkamahagung.go.id/) announced on 23 November 2026 the opening of 5 new Pengadilan Agama in Lombok/NTB to bring services closer to island and rural communities.
2. **Geographic Diversity:** Combines rural agricultural lowlands, mountainous interior villages, coastal fishing communities, and small islands.
3. **Data Availability:** Covered by BPS PODES, Kemendesa Indeks Desa, and NTB provincial/district JDIH ([storage.ntbprov.go.id/jdih](https://storage.ntbprov.go.id/jdih/produk-hukum/Lampiran%20III%20SPM%20Bidang%20Pekerjaan%20Umum.pdf)).

### Pilot Cluster 2: **Jawa Barat (`32`) — Agrarian, Mountainous & Peri-Urban Contrast**
1. **High Case & OBH Density:** Dense network of Pengadilan Negeri/Agama, accredited OBH in SIDBANKUM, and documented *sidang keliling* / Posbakum programs (e.g., [PA Sukabumi](https://pa-sukabumi.go.id/images/Juknis_Pedoman_Layanan_Hukum.pdf), [BPS Sumedang PODES 2024](https://sumedangkab.bps.go.id/en/news/2024/04/17/132/mengenal-potensi-desa--podes--2024.html)).
2. **Rural vs. Peri-Urban Testing:** Ideal for testing BPS Perka 37/2010 *perdesaan* vs. *perkotaan* boundaries and land/agrarian (`R01`), plantation (`R02`), and rural UMKM (`R07`) dispute metadata.
