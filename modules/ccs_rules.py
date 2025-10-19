import pandas as pd

def validate_ccs_row(row, threshold=1000):
    errors = []

    # ✅ Mass balance check with user-defined threshold
    try:
        captured = float(row.get("co2_captured_tonnes", 0))
        stored = float(row.get("co2_net_stored_tonnes", 0))
        transport_loss = float(row.get("transport_loss_tonnes", 0))
        leak = float(row.get("leak_mass_tonnes", 0))

        expected_output = stored + leak + transport_loss
        diff = abs(captured - expected_output)

        if diff > threshold:
            errors.append(
                f"Mass balance issue: captured={captured}, expected={expected_output}, diff={diff:.2f} > threshold={threshold}"
            )
    except Exception as e:
        errors.append(f"Error in mass balance calc: {e}")

    # ✅ Required field check
    required = [
        "record_id", "facility_id", "capture_tech", "transport_mode",
        "reservoir_type", "avg_reservoir_pressure_MPa", "avg_reservoir_temp_C",
        "injection_start_date", "injection_end_date", "mmv_methods"
    ]

    for field in required:
        val = row.get(field, None)
        if pd.isna(val) or str(val).strip() == "":
            errors.append(f"Missing or blank field: {field}")

    # ✅ Date format check
    for date_field in ["injection_start_date", "injection_end_date"]:
        try:
            pd.to_datetime(row.get(date_field))
        except Exception:
            errors.append(f"Invalid date format in {date_field}: {row.get(date_field)}")

    # ✅ MMV method check for keywords
    mmv_value = str(row.get("mmv_methods", "")).lower()
    expected_keywords = ["pressure", "seismic", "tracer"]
    if not any(keyword in mmv_value for keyword in expected_keywords):
        errors.append("mmv_methods does not contain expected keywords (e.g., pressure, seismic, tracer)")

    return errors
