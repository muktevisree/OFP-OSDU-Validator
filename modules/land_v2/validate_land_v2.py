from shared.validator_engine import validate_csv as _validate_csv

def validate_csv(file_path, rule_file_path="modules/land_v2/rules/land_rules.yaml"):
    return _validate_csv(file_path, rule_file_path)
