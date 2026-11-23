"""Lawful BPS connector for approved P1 aggregate tables (Perka 37/2010, PODES, IP-TIK).

Operates strictly via:
1. Official BPS Web API (requires user-supplied BPS API key via BPS_API_KEY env var), OR
2. Pre-downloaded official BPS CSV/JSON bulk exports placed in data/raw/bps/.

Never scrapes HTML pages or bypasses rate limits/authentication.
"""

from __future__ import annotations

import csv
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

from .common import (
    ROOT,
    AcquisitionResult,
    PoliteRateLimiter,
    get_approved_province_codes,
)

BPS_API_BASE = "https://webapi.bps.go.id/v1/api/list"
RAW_BPS_DIR = ROOT / "data" / "raw" / "bps"
OUT_PUBLIC_DIR = ROOT / "data" / "approved-public"


class BPSConnector:
    """Connector for official Badan Pusat Statistik (BPS) aggregate tables."""

    def __init__(self, api_key: Optional[str] = None, rate_limit_seconds: float = 2.0) -> None:
        self.api_key = api_key or os.environ.get("BPS_API_KEY")
        self.limiter = PoliteRateLimiter(rate_limit_seconds)

    def build_api_url(self, model: str, domain: str, var_id: Optional[str] = None) -> str:
        if not self.api_key:
            raise ValueError("BPS_API_KEY is required for live BPS Web API requests.")
        params: Dict[str, str] = {
            "model": model,
            "domain": domain,
            "key": self.api_key,
        }
        if var_id:
            params["var"] = var_id
        return f"{BPS_API_BASE}/{urllib.parse.urlencode(params)}"

    def fetch_live_variable(self, domain: str, var_id: str) -> Dict[str, Any]:
        """Fetch a single official BPS statistical variable via documented Web API."""
        url = self.build_api_url(model="data", domain=domain, var_id=var_id)
        self.limiter.wait()
        req = urllib.request.Request(url, headers={"User-Agent": "JRC-Observatory-Research/0.1"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def ingest_local_bulk_csv(
        self,
        csv_path: Path,
        output_filename: str = "bps_p1_pilot_aggregate.json",
    ) -> AcquisitionResult:
        """Ingest a pre-downloaded official BPS CSV, filtering to approved pilot provinces.

        Preserves empty strings as None (zero-imputation policy).
        """
        approved_provs = set(get_approved_province_codes())
        if not csv_path.exists():
            return AcquisitionResult(
                source_id="SRC-006",
                connector="BPSConnector",
                province_codes=sorted(approved_provs),
                record_count=0,
                publication_tier="P1",
                status="NO_LOCAL_FILE",
                output_path=None,
                notes=f"No local bulk file at {csv_path}; place official BPS CSV there or supply BPS_API_KEY.",
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
                cleaned["source_id"] = cleaned.get("source_id") or "SRC-006"
                records.append(cleaned)

        OUT_PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
        out_path = OUT_PUBLIC_DIR / output_filename
        with out_path.open("w", encoding="utf-8") as f:
            json.dump({"source_id": "SRC-006", "publication_tier": "P1", "records": records}, f, indent=2)
            f.write("\n")

        return AcquisitionResult(
            source_id="SRC-006",
            connector="BPSConnector",
            province_codes=sorted(approved_provs),
            record_count=len(records),
            publication_tier="P1",
            status="COMPLETED",
            output_path=str(out_path),
            notes="Ingested local BPS bulk CSV filtered to approved pilot provinces with zero imputation.",
        )
