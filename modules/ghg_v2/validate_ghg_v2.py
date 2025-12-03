import csv
import yaml
from datetime import datetime


def load_rules(rule_file_path):
    with open(rule_file_path, "r") as f:
        return yaml.safe_load(f)


def validate_row(row, rules):
    errors = []

    for field, rule in rules.items():
        value = row.get(field)

        # Required check
        if rule.get("required") and (value is None or str(value).strip() == ""):
            errors.append(f"{field} is required.")
            continue

        # Type checks
        if rule.get("type") == "number":
            try:
                float(value)
            except (ValueError, TypeError):
                errors.append(f"{field} must be a number.")

        elif rule.get("type") == "date":
            try:
                datetime.strptime(value, "%Y-%m-%d")
            except Exception:
                errors.append(f"{field} must be a valid date (YYYY-MM-DD).")

        # Allowed values
        if "allowed_values" in rule and value not in rule["allowed_values"]:
            errors.append(f"{field} must be one of {rule['allowed_values']}.")

    return errors


def validate_csv(csv_file_path, rules_file_path):
    rules = load_rules(rules_file_path)
    all_errors = []

    with open(csv_file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for idx, row in enumerate(reader, start=2):  # header = row 1
            row_errors = validate_row(row, rules)
            for err in row_errors:
                all_errors.append(f"Row {idx}: {err}")

    if all_errors:
        for e in all_errors:
            print(e)
    else:
        print("✅ All validations passed!")

    return all_errors
