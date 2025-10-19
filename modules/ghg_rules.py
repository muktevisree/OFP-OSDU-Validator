import pandas as pd

def validate_ghg_row(row):
    errors = []

    # ✅ Basic required field validation (customize list based on schema)
    required_fields = [
        "record_id", "organization", "country_code",
        "reporting_year", "emission_scope",
        "emission_source_category", "emission_value"
    ]

    for field in required_fields:
        value = row.get(field, None)
        if pd.isna(value) or str(value).strip() == "":
            errors.append(f"Missing or empty value in column: {field}")

    # ✅ Validate reporting year is numeric and in a valid range
    try:
        year = int(row.get("reporting_year", 0))
        if year < 1990 or year > 2100:
            errors.append(f"Invalid reporting year: {year}")
    except:
        errors.append(f"Reporting year must be a number: {row.get('reporting_year')}")

    # ✅ Validate emission value is numeric
    try:
        emission = float(row.get("emission_value", 0))
        if emission < 0:
            errors.append("Emission value cannot be negative")
    except:
        errors.append(f"Invalid emission value: {row.get('emission_value')}")

    # ✅ Enforce Scope must be 1, 2, or 3 only
    valid_scopes = ["Scope 1", "Scope 2", "Scope 3", "1", "2", "3"]
    scope = str(row.get("emission_scope", "")).strip()
    if scope not in valid_scopes:
        errors.append(f"Invalid emission scope: {scope}. Must be Scope 1, 2, or 3.")

    return errors
