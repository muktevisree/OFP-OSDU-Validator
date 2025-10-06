
# GHG Validation Rules

def validate_ghg_row(row):
    errors = []

    # Required Fields
    required_fields = ["facility_id", "timestamp", "emission_scope", "emission_type", "emission_value", "ghg_category"]
    for field in required_fields:
        if pd.isna(row.get(field)) or str(row.get(field)).strip() == "":
            errors.append(f"Missing required field: {field}")

    # Validate emission_value
    try:
        emission_val = float(row.get("emission_value"))
        if emission_val < 0:
            errors.append("emission_value must be non-negative")
    except (ValueError, TypeError):
        errors.append("Invalid emission_value")

    # Validate emission_scope
    valid_scopes = {"Scope 1", "Scope 2", "Scope 3"}
    if row.get("emission_scope") not in valid_scopes:
        errors.append(f"Invalid emission_scope: {row.get('emission_scope')}")

    # Validate emission_type
    valid_types = {"Direct", "Indirect"}
    if row.get("emission_type") not in valid_types:
        errors.append(f"Invalid emission_type: {row.get('emission_type')}")

    # GHG Category (Optional rule)
    if row.get("ghg_category") and not isinstance(row.get("ghg_category"), str):
        errors.append("ghg_category must be a string")

    return errors
