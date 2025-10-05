def validate_uhs_row(row):
    errors = []

    # Check total storage capacity = cushion + working
    expected_total = row['cushion_gas_volume'] + row['working_gas_volume']
    if abs(row['total_storage_capacity'] - expected_total) > 1e-6:
        errors.append(f"total_storage_capacity should be cushion_gas_volume + working_gas_volume ({expected_total})")

    # Check net flow = injection - withdrawal
    expected_net_flow = row['injection_volume'] - row['withdrawal_volume']
    if abs(row['net_flow'] - expected_net_flow) > 1e-6:
        errors.append(f"net_flow should be injection_volume - withdrawal_volume ({expected_net_flow})")

    return errors