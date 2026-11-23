"""Ingest Daftar_Lokasi_PN_PA_OBH_NTB_Jawa_Barat_2026.xlsx into schema-validated DS02 and DS05 JSONs."""

from __future__ import annotations

import json
from pathlib import Path
import pandas as pd
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
RAW_XLSX = ROOT / "data" / "raw" / "justice" / "Daftar_Lokasi_PN_PA_OBH_NTB_Jawa_Barat_2026.xlsx"
OUT_DIR = ROOT / "data" / "approved-public"
SCHEMA_DIR = ROOT / "schemas"

PROV_CODE = {
    "Nusa Tenggara Barat": "52",
    "Jawa Barat": "32",
}


def main() -> None:
    courts_df = pd.read_excel(RAW_XLSX, sheet_name="Pengadilan")
    obh_df = pd.read_excel(RAW_XLSX, sheet_name="OBH_BPHN")

    ds02_records = []
    for idx, row in courts_df.iterrows():
        prov_name = str(row["province"]).strip()
        prov_code = PROV_CODE[prov_name]
        addr = str(row["address_from_source"]).strip()
        verif = "pending_verification" if "perlu konfirmasi" in addr.lower() else "verified"
        ds02_records.append({
            "service_id": f"JRC-CRT-{prov_code}-{idx+1:03d}",
            "service_type": "court",
            "institution_type": str(row["court_type"]).strip(),
            "court_name": str(row["court_name"]).strip(),
            "jurisdiction": str(row["jurisdiction"]).strip(),
            "class_from_source": str(row["class_from_source"]).strip(),
            "address_from_source": addr,
            "province_code": prov_code,
            "district_code": f"{prov_code}00",
            "coordinates_if_authorized": None,
            "source_id": "SRC-001",
            "source_url": str(row["source_url"]).strip(),
            "verification_status": verif,
            "publication_tier": "P1",
            "is_synthetic": False,
        })

    ds05_records = []
    for idx, row in obh_df.iterrows():
        prov_name = str(row["province"]).strip()
        prov_code = PROV_CODE[prov_name]
        accred = str(row["BPHN_accreditation_code_as_displayed"]).strip()
        ds05_records.append({
            "area_id": f"{prov_code}00",
            "provider_id": f"JRC-OBH-{prov_code}-{idx+1:03d}",
            "provider_type": "obh_accredited",
            "obh_name_as_published": str(row["obh_name_as_published"]).strip(),
            "address_as_published": str(row["address_as_published"]).strip(),
            "accreditation_grade_displayed": accred,
            "service_availability": "available_in_district",
            "eligibility_information": "UU No. 16 Tahun 2011 (Masyarakat Miskin); BPHN directory listing does not prove specific court Posbakum contract.",
            "service_channel": "in_person",
            "source_reference": str(row["source_url"]).strip(),
            "observation_period": "2026-11-23",
            "verification_status_note": str(row["verification_status"]).strip(),
            "publication_tier": "P1",
            "is_synthetic": False,
        })

    with (SCHEMA_DIR / "justice-service-locations.schema.json").open("r", encoding="utf-8") as f:
        s02 = json.load(f)
    with (SCHEMA_DIR / "legal-aid.schema.json").open("r", encoding="utf-8") as f:
        s05 = json.load(f)

    v02 = Draft202012Validator(s02, format_checker=FormatChecker())
    v05 = Draft202012Validator(s05, format_checker=FormatChecker())
    for r in ds02_records:
        v02.validate(r)
    for r in ds05_records:
        v05.validate(r)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "ds02_pilot_courts_ntb_jabar.json").write_text(
        json.dumps({"dataset_id": "DS02", "publication_tier": "P1", "record_count": len(ds02_records), "records": ds02_records}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (OUT_DIR / "ds05_pilot_obh_ntb_jabar.json").write_text(
        json.dumps({"dataset_id": "DS05", "publication_tier": "P1", "record_count": len(ds05_records), "records": ds05_records}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Validated & wrote {len(ds02_records)} DS02 court records and {len(ds05_records)} DS05 OBH records.")


if __name__ == "__main__":
    main()
