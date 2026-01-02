import pandas as pd
import yaml


def load_rules(rule_file_path):
    with open(rule_file_path, "r") as f:
        return yaml.safe_load(f)


def validate_row(row, rules):
    errors = []
    for field, rule in rules.items():
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
    df = pd.read_csv(file_path)

    all_errors = []

    for idx, row in df.iterrows():
        row_dict = row.to_dict()
        errors = validate_row(row_dict, rules)
        if errors:
            all_errors.append({
                "row": idx + 1,
                "errors": errors
            })

    if all_errors:
        print("❌ UHS Validation Failed")
        for err in all_errors:
            print(f"Row {err['row']}:")
            for e in err["errors"]:
                print(f"  - {e}")
    else:
        print("✅ UHS Validation Passed")

    return all_errors
