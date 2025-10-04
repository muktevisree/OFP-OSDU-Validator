
import csv
import json
import yaml
import sys
from jsonschema import validate, ValidationError

def load_yaml_schema(schema_path):
    with open(schema_path, 'r') as f:
        return yaml.safe_load(f)

def validate_csv(csv_path, schema):
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=1):
            try:
                validate(instance=row, schema=schema)
                # Example CCS rule: injection - leak = storage
                inj = float(row.get("co2_injected", 0))
                leak = float(row.get("co2_leaked", 0))
                stored = float(row.get("co2_stored", 0))
                if abs((inj - leak) - stored) > 0.01:
                    raise ValueError("Mass balance error in row {}".format(idx))
            except (ValidationError, ValueError) as e:
                print(f"❌ Row {idx} failed validation: {e}")
            else:
                print(f"✅ Row {idx} passed validation")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python validate_ccs.py <csv_file> <schema_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    schema_file = sys.argv[2]
    schema = load_yaml_schema(schema_file)
    validate_csv(csv_file, schema)
