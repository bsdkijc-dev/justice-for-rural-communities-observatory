import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src" / "validation"))

import validate_all  # noqa: E402


class TestJRCObservatoryValidation(unittest.TestCase):
    def test_all_12_schemas_valid(self):
        schemas = validate_all.validate_schemas()
        self.assertEqual(len(schemas), 12)

    def test_synthetic_datasets_validate_and_labeled_p5(self):
        schemas = validate_all.validate_schemas()
        count = validate_all.validate_synthetic_data(schemas)
        self.assertGreaterEqual(count, 12)

    def test_source_register_integrity(self):
        source_count = validate_all.validate_source_register()
        self.assertGreaterEqual(source_count, 11)


if __name__ == "__main__":
    unittest.main()
