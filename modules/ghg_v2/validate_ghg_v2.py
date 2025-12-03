import csv
import yaml

def load_rules(rule_file_path):
    with open(rule_file_path, 'r') as f:
        return yaml.safe_load(f)

def validate_row(row, rules):
    errors = []
    for field, rule in rules.items():
        value = row.get(field, '')
        if rule.get("required") and not value:
            errors.append(f"{field} is required.")
        if "type" in rule:
            if rule["type"] == "number":
                try:
                    float(value)
                except ValueError:
                    errors.append(f"{field} must be a number.")
        if "allowed_values" in rule:
            if value not in rule["allowed_values"]:
                errors.append(f"{field} must be one of {rule['allowed_values']}.")
    return errors

def validate_csv(csv_path, rule_path):
    rules = load_rules(rule_path)
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader, start=1):
            errors = validate_row(row, rules)
            if errors:
                print(f"Row {idx} errors: {errors}")
