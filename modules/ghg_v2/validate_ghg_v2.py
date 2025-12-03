import csv
import yaml
import sys
from datetime import datetime

def load_rules(rule_file_path):
    with open(rule_file_path, 'r') as f:
        return yaml.safe_load(f)

def validate_row(row, rules):
    errors = []
    for field, rule in rules.items():
        value = row.get(field)

        if rule.get("required") and (value is None or value == ""):
            errors.append(f"{field} is required.")

        if rule.get("type") == "number":
            try:
                float(value)
            except (ValueError, TypeError):
                errors.append(f"{field} must be a number.")

        if rule.get("type") == "date":
            try:
                datetime.strptime(value, "%Y-%m-%d")
            except (ValueError, TypeError):
                errors.append(f"{field} must be in YYYY-MM-DD format.")

        if "min" in rule:
            try:
                if float(value) < rule["min"]:
                    errors.append(f"{field} must be at least {rule['min']}.")
            except (ValueError, TypeError):
                pass

        if "max" in rule:
            try:
                if float(value) > rule["max"]:
                    errors.append(f"{field} must be at most {rule['max']}.")
            except (ValueError, TypeError):
                pass

        if "allowed" in rule:
            if value not in rule["allowed"]:
                errors.append(f"{field} has invalid value: {value}")

    return errors

def run_ghg_validation(filepath):
    rules = load_rules("modules/ghg_v2/rules/ghg_rules.yaml")

    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        all_errors = []
        for i, row in enumerate(reader, start=1):
            row_errors = validate_row(row, rules)
            if row_errors:
                all_errors.append((i, row_errors))

    if all_errors:
        print("❌ Validation Errors:")
        for row_num, errs in all_errors:
            for err in errs:
                print(f" - Row {row_num}: {err}")
        sys.exit(1)
    else:
        print("✅ All validations passed!")
