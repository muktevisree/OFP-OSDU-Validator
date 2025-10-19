from modules.ccs_rules import validate_ccs_row
import pandas as pd

def test_valid_ccs_row():
    row = pd.Series({
        "facility_id": "CCS001",
        "co2_captured_tonnes": 1000,
        "co2_injected_tonnes": 950,
        "co2_leaked_tonnes": 30,
        "transport_mode": "pipeline"
    })
    errors = validate_ccs_row(row)
    assert isinstance(errors, list)

def test_invalid_ccs_row():
    row = pd.Series({
        "facility_id": "",
        "co2_captured_tonnes": "N/A",
        "co2_injected_tonnes": -50,
        "co2_leaked_tonnes": None
    })
    errors = validate_ccs_row(row)
    assert len(errors) > 0