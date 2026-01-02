from shared.validator_engine import validate_csv as _validate_csv

def validate_csv(file_path, rule_file_path="modules/noise_v2/rules/noise_rules.yaml"):
    return _validate_csv(file_path, rule_file_path)
