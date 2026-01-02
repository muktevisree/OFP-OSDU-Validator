from shared.validator_engine import validate_csv as _validate_csv

def validate_csv(file_path, rule_file_path="modules/water_v2/rules/water_rules.yaml"):
    return _validate_csv(file_path, rule_file_path)
