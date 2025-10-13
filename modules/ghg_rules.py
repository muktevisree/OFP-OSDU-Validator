def validate_ghg_row(row):
    errors = []

    required_fields = [
        "facility_id",
        "reporting_year",
        "emission_source",
        "ghg_type",
        "emission_value",
        "unit"
    ]

    for field in required_fields:
        value = row.get(field)
        if pd.isna(value) or str(value).strip() == "":
            errors.append(f"Missing or empty value in required field: {field}")

    # emission_value must be a positive number
    try:
        emission_value = float(row.get("emission_value"))
        if emission_value <= 0:
            errors.append("Invalid emission_value: must be > 0")
    except (ValueError, TypeError):
        errors.append("Invalid emission_value: not a number")

    # reporting_year should be a valid integer year
    try:
        year = int(row.get("reporting_year"))
        if year < 1900 or year > 2100:
            errors.append("Invalid reporting_year")
    except (ValueError, TypeError):
        errors.append("Invalid reporting_year: not an integer")

    return errors
