import pandas as pd
import yaml
from datetime import datetime
import os

def validate_csv(file_path):
    rules_path = os.path.join(os.path.dirname(__file__), "rules", "ccs_rules.yaml")

    with open(rules_path, "r") as f:
        rules = yaml.safe_load(f)

    required_columns = rules.get("required_columns", [])
    column_rules = rules.get("column_rules", {})

    df = pd.read_csv(file_path)
    errors = []

    # Check for required columns
    for col in required_columns:
        if col not in df.columns:
            errors.append(f"[Missing] Column '{col}' is missing from the dataset.")

    # If required columns are missing, skip further validation
    if errors:
        print("❌ Validation Errors:")
        for err in errors:
            print(f" - {err}")
        return errors

    # Apply column rules
    for column, rule in column_rules.items():
        if column not in df.columns:
            continue
        series = df[column]

        # Type check
        if rule.get("type") == "number":
            if not pd.api.types.is_numeric_dtype(series):
                errors.append(f"[Type Error] Column '{column}' should be numeric.")
                continue
            if "min" in rule:
                if (series < rule["min"]).any():
                    errors.append(f"[Range Error] Column '{column}' has values below min {rule['min']}")
            if "max" in rule:
                if (series > rule["max"]).any():
                    errors.append(f"[Range Error] Column '{column}' has values above max {rule['max']}")

        elif rule.get("type") == "date":
            fmt = rule.get("format", "%Y-%m-%d")
            try:
                pd.to_datetime(series, format=fmt)
            except ValueError:
                errors.append(f"[Format Error] Column '{column}' has invalid date format. Expected {fmt}")

        elif rule.get("type") == "list":
            separator = rule.get("separator", ",")
            allowed = set(val.strip().lower() for val in rule.get("allowed_values", []))
            for idx, val in series.items():
                items = [v.strip().lower() for v in str(val).split(separator)]
                if not set(items).issubset(allowed):
                    errors.append(f"[Invalid Values] Column '{column}' has invalid values: ['{val}']")
                    break

        elif rule.get("type") == "string":
            allowed = rule.get("allowed_values")
            if allowed:
                invalid = series[~series.astype(str).isin(allowed)]
                if not invalid.empty:
                    errors.append(f"[Invalid Values] Column '{column}' has invalid values: {invalid.unique().tolist()}")

    if errors:
        print("❌ Validation Errors:")
        for err in errors:
            print(f" - {err}")
    else:
        print("✅ All validations passed!")

    return errors
