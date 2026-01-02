from shared.validator_engine import validate_csv as _validate_csv

def validate_csv(file_path, rule_file_path="modules/landuse_v2/rules/landuse_rules.yaml"):
    return _validate_csv(file_path, rule_file_path)
