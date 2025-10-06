# ghg_rules.py

import pandas as pd

def validate_ghg_row(row):
    errors = []

    # Example rule 1: Check for missing 'emission_source'
    if pd.isna(row.get("emission_source", None)):
        errors.append("Missing emission_source")

    # Example rule 2: Validate that 'emission_value' is a number and positive
    emission_value = row.get("emission_value", None)
    if pd.isna(emission_value) or not isinstance(emission_value, (int, float)):
        errors.append("Invalid emission_value")
    elif emission_value < 0:
        errors.append("emission_value cannot be negative")

    # Add more validation rules as needed...

    return errors
