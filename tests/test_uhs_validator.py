from modules.uhs_rules import validate_uhs_row
import pandas as pd

def test_valid_uhs_row():
    row = pd.Series({
        "facility_id": "UHS001",
        "h2_injected_tonnes": 500,
        "h2_withdrawn_tonnes": 450,
        "h2_losses_tonnes": 20,
        "h2_cushion_gas_tonnes": 30
    })
    errors = validate_uhs_row(row)
    assert isinstance(errors, list)

def test_invalid_uhs_row():
    row = pd.Series({
        "facility_id": None,
        "h2_injected_tonnes": "five hundred",
        "h2_withdrawn_tonnes": -100,
        "h2_losses_tonnes": "N/A"
    })
    errors = validate_uhs_row(row)
    assert len(errors) > 0