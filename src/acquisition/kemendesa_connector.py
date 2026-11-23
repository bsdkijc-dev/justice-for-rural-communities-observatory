"""Lawful Kemendesa PDT Indeks Desa / Satu Data Indonesia connector for approved P1 tables.

Operates strictly via:
1. Official Satu Data Indonesia (data.go.id) CKAN API / Kemendesa SID downloads, OR
2. Pre-downloaded official CSV exports placed in data/raw/kemendesa/.

Preserves original values and keeps missing cells as None (zero-imputation policy).
"""

from __future__ import annotations

import csv
import json
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List

from .common import (
    ROOT,
    AcquisitionResult,
    PoliteRateLimiter,
    get_approved_province_codes,
)

CKAN_SEARCH_URL = "https://data.go.id/api/3/action/package_search"
RAW_KEMENDESA_DIR = ROOT / "data" / "raw" / "kemendesa"
OUT_PUBLIC_DIR = ROOT / "data" / "approved-public"


class KemendesaConnector:
    """Connector for Kemendesa PDT Indeks Desa / IDM public open data."""

    def __init__(self, rate_limit_seconds: float = 2.0) -> None:
        self.limiter = PoliteRateLimiter(rate_limit_seconds)

    def build_ckan_search_url(self, query: str = "indeks desa membangun") -> str:
        params = urllib.parse.urlencode({"q": query, "rows": 10})
        return f"{CKAN_SEARCH_URL}?{params}"

    def search_satu_data(self, query: str = "indeks desa membangun") -> Dict[str, Any]:
        url = self.build_ckan_search_url(query)
        self.limiter.wait()
        req = urllib.request.Request(url, headers={"User-Agent": "JRC-Observatory-Research/0.1"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def ingest_local_bulk_csv(
        self,
        csv_path: Path,
        output_filename: str = "kemendesa_p1_pilot_indeks_desa.json",
    ) -> AcquisitionResult:
        """Ingest pre-downloaded official Kemendesa Indeks Desa CSV for approved pilot provinces."""
        approved_provs = set(get_approved_province_codes())
        if not csv_path.exists():
            return AcquisitionResult(
                source_id="SRC-011",
                connector="KemendesaConnector",
                province_codes=sorted(approved_provs),
                record_count=0,
                publication_tier="P1",
                status="NO_LOCAL_FILE",
                output_path=None,
                notes=f"No local bulk file at {csv_path}; place official Kemendesa CSV there.",
            )

        records: List[Dict[str, Any]] = []
        with csv_path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                prov = str(row.get("province_code", "")).strip().zfill(2)
                if prov not in approved_provs:
                    continue
                cleaned = {k: (None if v == "" else v) for k, v in row.items()}
                cleaned["province_code"] = prov
                cleaned["publication_tier"] = "P1"
                cleaned["source_id"] = cleaned.get("source_id") or "SRC-011"
                records.append(cleaned)

        OUT_PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
        out_path = OUT_PUBLIC_DIR / output_filename
        with out_path.open("w", encoding="utf-8") as f:
            json.dump({"source_id": "SRC-011", "publication_tier": "P1", "records": records}, f, indent=2)
            f.write("\n")

        return AcquisitionResult(
            source_id="SRC-011",
            connector="KemendesaConnector",
            province_codes=sorted(approved_provs),
            record_count=len(records),
            publication_tier="P1",
            status="COMPLETED",
            output_path=str(out_path),
            notes="Ingested local Kemendesa Indeks Desa CSV filtered to approved pilot provinces.",
        )
