import unittest
import pandas as pd
import tempfile
import os

from modules.ccs_v2.validate_ccs_v2 import validate_csv


class TestCCSValidator(unittest.TestCase):

    def _write_temp_csv(self, df):
        """Helper to write DataFrame to a temp CSV file"""
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
        df.to_csv(tmp.name, index=False)
        return tmp.name

    def test_valid_data(self):
        valid_df = pd.DataFrame({
            "case_id": ["CASE-001"],
            "capture_tech": ["Post-combustion"],
            "co2_captured_tonnes": [50000],
            "well_id": ["WELL-01"],
            "co2_injected_tonnes": [48000],
            "injection_start_date": ["2024-01-01"],
            "mmv_methods": ["pressure, seismic"]
        })

        csv_path = self._write_temp_csv(valid_df)
        errors = validate_csv(csv_path)

        os.unlink(csv_path)
        self.assertEqual(errors, [])

    def test_invalid_data(self):
        invalid_df = pd.DataFrame({
            "case_id": ["CASE-002"],
            "capture_tech": ["Post-combustion"],
            "co2_captured_tonnes": [-100],  # invalid
            "well_id": ["WELL-02"],
            "co2_injected_tonnes": [2000000],  # exceeds max
            "injection_start_date": ["bad-date"],
            "mmv_methods": ["unknown_method"]
        })

        csv_path = self._write_temp_csv(invalid_df)
        errors = validate_csv(csv_path)

        os.unlink(csv_path)
        self.assertTrue(len(errors) > 0)


if __name__ == "__main__":
    unittest.main()
