import pandas as pd

def validate_ccs_row(row):
    errors = []

    # Use .get() with default values to avoid KeyErrors
    try:
        captured = float(row.get("co2_captured_tonnes", 0))
        stored = float(row.get("co2_net_stored_tonnes", 0))
        transport_loss = float(row.get("transport_loss_tonnes", 0))
        leak = float(row.get("leak_mass_tonnes", 0))

        expected_output = stored + leak + transport_loss
        diff = abs(captured - expected_output)

        if diff > 1000:
            errors.append(
                f"Mass balance issue: captured={captured}, expected={expected_output}, diff={diff:.2f}"
            )
    except Exception as e:
        errors.append(f"Error in mass balance calc: {e}")

    # Optional: validate required fields are not blank
    required = [
        "record_id", "facility_id", "capture_tech", "transport_mode",
        "reservoir_type", "avg_reservoir_pressure_MPa", "avg_reservoir_temp_C",
        "injection_start_date", "injection_end_date", "mmv_methods"
    ]

    for field in required:
        val = row.get(field, None)
        if pd.isna(val) or str(val).strip() == "":
            errors.append(f"Missing or blank field: {field}")

    return errors
