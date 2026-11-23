import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.acquisition.bps_connector import BPSConnector
from src.acquisition.common import get_approved_province_codes, load_pilot_config
from src.acquisition.kemendesa_connector import KemendesaConnector


class TestAcquisitionConnectors(unittest.TestCase):
    def test_pilot_config_approved(self):
        cfg = load_pilot_config()
        self.assertEqual(cfg["approval_status"], "APPROVED")
        self.assertEqual(get_approved_province_codes(), ["52", "32"])

    def test_bps_connector_missing_file_returns_zero(self):
        conn = BPSConnector(api_key="dummy-key", rate_limit_seconds=0.0)
        url = conn.build_api_url(model="data", domain="5200", var_id="123")
        self.assertIn("webapi.bps.go.id", url)
        res = conn.ingest_local_bulk_csv(Path("/nonexistent/bps.csv"))
        self.assertEqual(res.status, "NO_LOCAL_FILE")
        self.assertEqual(res.record_count, 0)

    def test_kemendesa_connector_filters_provinces_and_zero_imputation(self):
        conn = KemendesaConnector(rate_limit_seconds=0.0)
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_csv = Path(tmpdir) / "indeks_desa.csv"
            with tmp_csv.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["province_code", "village_code", "indeks_desa_score"])
                writer.writerow(["52", "5201010001", "0.71"])
                writer.writerow(["32", "3201010001", ""])  # missing value must stay None
                writer.writerow(["11", "1101010001", "0.65"])  # non-pilot province filtered out

            out_name = "_test_kemendesa_output.json"
            res = conn.ingest_local_bulk_csv(tmp_csv, output_filename=out_name)
            self.assertEqual(res.status, "COMPLETED")
            self.assertEqual(res.record_count, 2)
            out_path = Path(res.output_path)
            with out_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertEqual(data["publication_tier"], "P1")
            self.assertIsNone(data["records"][1]["indeks_desa_score"])
            out_path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
