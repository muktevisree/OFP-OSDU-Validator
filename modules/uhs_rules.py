import pandas as pd

def validate_uhs_row(row, threshold=500):
    errors = []

    # ✅ Required fields check
    required_fields = [
        "record_id", "facility_id", "well_id", "injection_start_date", "injection_end_date",
        "h2_injected_tonnes", "h2_withdrawn_tonnes", "h2_cushion_gas_tonnes",
        "h2_losses_tonnes", "h2_net_stored_tonnes", "compression_energy_MWh",
        "avg_reservoir_pressure_MPa", "avg_reservoir_temp_C", "mmv_methods"
    ]

    for field in required_fields:
        val = row.get(field)
        if pd.isna(val) or str(val).strip() == "":
            errors.append(f"Missing or blank field: {field}")

    # ✅ Mass balance: injected ≈ withdrawn + losses
    try:
        injected = float(row.get("h2_injected_tonnes", 0))
        withdrawn = float(row.get("h2_withdrawn_tonnes", 0))
        losses = float(row.get("h2_losses_tonnes", 0))
        expected = withdrawn + losses
        diff = abs(injected - expected)

        if diff > threshold:  # dynamic tolerance
            errors.append(
                f"Mass balance mismatch: injected={injected}, expected={expected}, diff={diff:.2f} > threshold={threshold}"
            )
    except Exception as e:
        errors.append(f"Error in mass balance check: {e}")

    # ✅ Date format check
    for date_field in ["injection_start_date", "injection_end_date"]:
        try:
            pd.to_datetime(row.get(date_field))
        except Exception:
            errors.append(f"Invalid date format in {date_field}: {row.get(date_field)}")

    # ✅ MMV method validation
    mmv_value = str(row.get("mmv_methods", "")).lower()
    expected_keywords = ["pressure", "seismic", "tracer"]
    if not any(keyword in mmv_value for keyword in expected_keywords):
        errors.append("mmv_methods does not contain expected keywords (e.g., pressure, seismic, tracer)")

    return errors
