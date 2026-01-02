import csv
import yaml

def load_rules(rule_file_path):
    with open(rule_file_path, 'r') as f:
        return yaml.safe_load(f)

def validate_row(row, rules):
    errors = []
    for field, rule in rules.items():
        rule = rule or {}  # Defensive null check
        value = row.get(field)
        if rule.get("required") and (value is None or str(value).strip() == ""):
            errors.append(f"{field} is required")
            continue
        if "type" in rule and value is not None and str(value).strip() != "":
            try:
                if rule["type"] == "int":
                    int(value)
                elif rule["type"] == "float":
                    float(value)
                elif rule["type"] == "str":
                    str(value)
            except ValueError:
                errors.append(f"{field} must be of type {rule['type']}")
    return errors

def validate_csv(file_path, rule_file_path):
    rules = load_rules(rule_file_path)
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        all_errors = []
        for i, row in enumerate(reader, start=1):
            errors = validate_row(row, rules)
            if errors:
                all_errors.append((i, errors))

        if all_errors:
            print("❌ Validation Failed")
            for row_num, errs in all_errors:
                print(f"Row {row_num}:")
                for e in errs:
                    print(f"  - {e}")
        else:
            print("✅ Validation Passed")
    return all_errors
