"""Validate all 12 JSON Schemas, P5 synthetic datasets, and source register."""

import csv
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas"
SYNTH_DIR = ROOT / "data" / "synthetic"
SOURCE_CSV = ROOT / "sources" / "source-register.csv"

EXPECTED_SCHEMAS = [
    "rural-community-profile.schema.json",
    "justice-service-locations.schema.json",
    "geographic-access.schema.json",
    "dispute-metadata.schema.json",
    "legal-aid.schema.json",
    "justice-cost.schema.json",
    "legal-information.schema.json",
    "survey.schema.json",
    "socioeconomic-indicators.schema.json",
    "provenance.schema.json",
    "legal-register.schema.json",
    "policy-register.schema.json",
]


def validate_schemas() -> dict:
    loaded = {}
    for name in EXPECTED_SCHEMAS:
        path = SCHEMA_DIR / name
        if not path.exists():
            raise FileNotFoundError(f"Missing schema: {path}")
        with path.open("r", encoding="utf-8") as f:
            schema = json.load(f)
        Draft202012Validator.check_schema(schema)
        loaded[name] = schema
    return loaded


def validate_synthetic_data(schemas: dict) -> int:
    files = sorted(SYNTH_DIR.glob("ds*.json"))
    if len(files) != 12:
        raise ValueError(f"Expected 12 synthetic dataset files, found {len(files)}")
    total_records = 0
    for path in files:
        with path.open("r", encoding="utf-8") as f:
            payload = json.load(f)
        schema_name = payload.get("schema")
        if schema_name not in schemas:
            raise ValueError(f"{path.name} references unknown schema: {schema_name}")
        validator = Draft202012Validator(schemas[schema_name], format_checker=FormatChecker())
        records = payload.get("records", [])
        if not records:
            raise ValueError(f"{path.name} has no records")
        for idx, rec in enumerate(records):
            validator.validate(rec)
            if rec.get("is_synthetic") is not True:
                raise ValueError(f"{path.name} record {idx} missing is_synthetic=True")
            tier = rec.get("publication_tier") or rec.get("publication_status")
            if tier != "P5":
                raise ValueError(f"{path.name} record {idx} must be labeled P5, got {tier}")
            total_records += 1
    return total_records


def validate_source_register() -> int:
    required_cols = {
        "source_id",
        "institution",
        "exact_url",
        "dataset_or_document_title",
        "publication_date",
        "observation_period",
        "geographic_coverage",
        "methodology",
        "update_frequency",
        "access_conditions",
        "reuse_and_redistribution_terms",
        "retrieval_date",
        "provenance",
        "publication_tier",
        "verification_status",
    }
    with SOURCE_CSV.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or not required_cols.issubset(set(reader.fieldnames)):
            missing = required_cols - set(reader.fieldnames or [])
            raise ValueError(f"source-register.csv missing columns: {missing}")
        rows = list(reader)
        for row in rows:
            if not row["exact_url"].startswith("https://"):
                raise ValueError(f"Invalid URL in {row['source_id']}: {row['exact_url']}")
    return len(rows)


def main() -> None:
    schemas = validate_schemas()
    record_count = validate_synthetic_data(schemas)
    source_count = validate_source_register()
    print(f"OK: {len(schemas)} schemas, {record_count} P5 synthetic records, {source_count} verified sources.")


if __name__ == "__main__":
    main()
