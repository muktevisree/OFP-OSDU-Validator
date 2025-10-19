import pandas as pd

def validate_ccs_row(row):
    errors = []

    # Fields expected to be present and non-empty
    required_fields = [
        "record_id", "case_id", "facility_id", "country_code",
        "capture_tech", "co2_captured_tonnes", "capture_energy_MWh",
        "transport_mode", "reservoir_type", "avg_reservoir_pressure_MPa",
        "avg_reservoir_temp_C", "mmv_methods", "leak_mass_tonnes",
        "transport_loss_tonnes", "co2_net_stored_tonnes", "injection_start_date",
        "injection_end_date"
    ]

    for field in required_fields:
        if field not in row or pd.isna(row[field]) or str(row[field]).strip() == "":
            errors.append(f"Missing or empty field: {field}")

    # Check date format (basic)
    for date_field in ["injection_start_date", "injection_end_date"]:
        try:
            pd.to_datetime(row[date_field])
        except Exception:
            errors.append(f"Invalid date format in {date_field}: {row[date_field]}")

    # Validate MMV methods
    allowed_methods = ["pressure", "microseismic", "4D seismic", "tracers"]
    mmv_str = str(row.get("mmv_methods", "")).lower()
    if not any(method in mmv_str for method in allowed_methods):
        errors.append("MMV methods do not include standard options (pressure, microseismic, etc.)")

    # Mass balance check (with transport loss + leak)
    try:
        captured = float(row["co2_captured_tonnes"])
        stored = float(row["co2_net_stored_tonnes"])
        transport_loss = float(row["transport_loss_tonnes"])
        leak = float(row["leak_mass_tonnes"])

        expected_output = stored + transport_loss + leak
        if abs(captured - expected_output) > 1000:
            errors.append(
                f"Mass balance mismatch: captured={captured}, expected_output={expected_output}, diff={abs(captured - expected_output)}"
            )
    except Exception as e:
        errors.append(f"Mass balance calculation error: {e}")

    return errors
