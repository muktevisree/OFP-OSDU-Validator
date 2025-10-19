import pandas as pd

def validate_ccs_row(row):
    errors = []

    # Safe access using .get() to avoid KeyError
    try:
        captured = float(row.get("co2_captured_tonnes", 0))
        stored = float(row.get("co2_net_stored_tonnes", 0))
        transport_loss = float(row.get("transport_loss_tonnes", 0))
        leak = float(row.get("leak_mass_tonnes", 0))

        expected = stored + transport_loss + leak
        diff = abs(captured - expected)

        if diff > 1000:
            errors.append(
                f"Mass balance mismatch: captured={captured}, total out={expected}, diff={diff:.2f}"
            )

    except Exception as e:
        errors.append(f"Error computing mass balance: {e}")

    # Check for missing required fields (optional but recommended)
    required_fields = [
        "record_id", "facility_id", "capture_tech", "transport_mode",
        "reservoir_type", "avg_reservoir_pressure_MPa", "avg_reservoir_temp_C",
        "mmv_methods", "injection_start_date", "injection_end_date"
    ]

    for col in required_fields:
        val = row.get(col)
        if pd.isna(val) or str(val).strip() == "":
            errors.append(f"Missing or empty field: {col}")

    return errors
