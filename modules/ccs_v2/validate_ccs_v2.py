from shared.validator_engine import validate_csv as _validate_csv

def validate_csv(file_path, rule_file_path="modules/ccs_v2/rules/ccs_rules.yaml"):
    return _validate_csv(file_path, rule_file_path)
