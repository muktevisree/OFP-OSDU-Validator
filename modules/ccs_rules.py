def validate_ccs_row(row):
    errors = []

    # Check if total_emitted = injection_volume - retained_volume
    expected_emitted = row['injection_volume'] - row['retained_volume']
    if abs(row['total_emitted'] - expected_emitted) > 1e-6:
        errors.append(f"total_emitted should be injection_volume - retained_volume ({expected_emitted})")

    # Ensure reservoir type is one of accepted types
    valid_reservoir_types = ['saline_aquifer', 'depleted_oil_gas_field', 'basalt', 'coal_seam']
    if row['reservoir_type'] not in valid_reservoir_types:
        errors.append(f"reservoir_type '{row['reservoir_type']}' is invalid. Valid options: {valid_reservoir_types}")

    return errors