from shared.validator_engine import validate_csv as _validate_csv

def validate_csv(file_path, rule_file_path="modules/emissions_intensity_v2/rules/emissions_intensity_rules.yaml"):
    return _validate_csv(file_path, rule_file_path)
