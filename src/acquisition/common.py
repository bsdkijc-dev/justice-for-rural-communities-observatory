"""Shared acquisition utilities: polite rate-limiting, provenance logging, and zero-imputation helpers."""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[2]
PILOT_CONFIG_PATH = Path(__file__).resolve().parent / "pilot_config.json"


def load_pilot_config() -> Dict[str, Any]:
    with PILOT_CONFIG_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_approved_province_codes() -> List[str]:
    cfg = load_pilot_config()
    return [p["province_code"] for p in cfg.get("provinces", [])]


@dataclass
class AcquisitionResult:
    source_id: str
    connector: str
    province_codes: List[str]
    record_count: int
    publication_tier: str
    status: str
    output_path: str | None
    notes: str


class PoliteRateLimiter:
    """Enforces minimum delay between lawful API/bulk requests."""

    def __init__(self, min_interval_seconds: float = 2.0) -> None:
        self.min_interval_seconds = min_interval_seconds
        self._last_call: float = 0.0

    def wait(self) -> None:
        now = time.monotonic()
        elapsed = now - self._last_call
        if self._last_call > 0 and elapsed < self.min_interval_seconds:
            time.sleep(self.min_interval_seconds - elapsed)
        self._last_call = time.monotonic()


def build_provenance_record(
    record_id: str,
    dataset_id: str,
    source_id: str,
    validation_status: str,
    missingness_status: str,
    limitations: str,
    publication_status: str = "P1",
) -> Dict[str, Any]:
    return {
        "record_id": record_id,
        "dataset_id": dataset_id,
        "source_id": source_id,
        "validation_status": validation_status,
        "missingness_status": missingness_status,
        "verification_date": date.today().isoformat(),
        "reviewer": "Acquisition Pipeline (Automated Gate)",
        "limitations": limitations,
        "publication_status": publication_status,
    }
