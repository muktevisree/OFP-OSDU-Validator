import csv
import sys
from modules.uhs_rules import validate_uhs_row

def main():
    if len(sys.argv) != 3:
        print("Usage: python validate_uhs.py <input_csv> <schema_yaml>")
        sys.exit(1)

    input_csv = sys.argv[1]

    with open(input_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader, start=1):
            # Convert string inputs to appropriate types
            for key in ['reporting_year']:
                row[key] = int(row[key])
            for key in ['cushion_gas_volume', 'working_gas_volume', 'total_storage_capacity',
                        'injection_volume', 'withdrawal_volume', 'net_flow']:
                row[key] = float(row[key])

            errors = validate_uhs_row(row)
            if errors:
                print(f"Row {idx}: ❌ Failed")
                for e in errors:
                    print(f"   - {e}")
            else:
                print(f"Row {idx}: ✅ Passed")

if __name__ == "__main__":
    main()