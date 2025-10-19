import pandas as pd

def validate_ghg_row(row):
    errors = []

    # ✅ Aligned with uploaded dataset headers
    required_fields = [
        "Facility_ID", "Company", "Country", "Reporting_Year", "Emission_Value_tCO2e"
    ]

    for field in required_fields:
        val = row.get(field)
        if pd.isna(val) or str(val).strip() == "":
            errors.append(f"Missing or empty value in column: {field}")

    # ✅ Validate year is reasonable
    try:
        year = int(row.get("Reporting_Year", 0))
        if year < 1990 or year > 2100:
            errors.append(f"Invalid Reporting_Year: {year}")
    except:
        errors.append(f"Non-numeric Reporting_Year: {row.get('Reporting_Year')}")

    # ✅ Emission value must be numeric and non-negative
    try:
        value = float(row.get("Emission_Value_tCO2e", 0))
        if value < 0:
            errors.append("Emission_Value_tCO2e cannot be negative")
    except:
        errors.append(f"Invalid Emission_Value_tCO2e: {row.get('Emission_Value_tCO2e')}")

    # ✅ Optional scope columns: should be numeric if present
    for scope_col in ["Scope_1_tCO2e", "Scope_2_tCO2e", "Scope_3_tCO2e"]:
        if scope_col in row:
            try:
                val = float(row.get(scope_col, 0))
                if val < 0:
                    errors.append(f"{scope_col} cannot be negative")
            except:
                errors.append(f"Invalid value in {scope_col}: {row.get(scope_col)}")

    return errors
