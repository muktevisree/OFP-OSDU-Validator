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

        if rule.get("required") and not value:
            errors.append(f"{field} is required.")

        if rule.get("type") == "number":
            try:
                float(value)
            except (ValueError, TypeError):
                errors.append(f"{field} must be a number.")

        if rule.get("type") == "date":
            try:
                datetime.strptime(value, "%Y-%m-%d")
            except Exception:
                errors.append(f"{field} must be a valid date (YYYY-MM-DD).")

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
                print(f"\nRow {idx} errors:")
                for e in errors:
                    print(f"  - {e}")
        else:
            print("\n✅ Validation complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_ghg_v2.py <csv_file>")
        sys.exit(1)

    validate_csv(sys.argv[1], "modules/ghg_v2/rules/ghg_rules.yaml")
