# cli/validate_ghg.py

import argparse
import pandas as pd
import os
import sys

# ✅ Add path to modules folder for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.ghg_rules import validate_ghg_row

def main():
    parser = argparse.ArgumentParser(description="Validate GHG dataset CSV against OFP–OSDU rules")
    parser.add_argument("csv_file", help="Path to GHG dataset CSV file")

    args = parser.parse_args()
    df = pd.read_csv(args.csv_file)

    print(f"📂 Validating: {args.csv_file}")
    errors = []

    for idx, row in df.iterrows():
        row_errors = validate_ghg_row(row)
        if row_errors:
            errors.append({
                "Row": idx + 2,
                "Errors": "; ".join(row_errors)
            })

    if errors:
        error_df = pd.DataFrame(errors)
        print(f"❌ {len(errors)} rows failed validation:")
        print(error_df.to_string(index=False))
        error_file = "validation_errors.csv"
        error_df.to_csv(error_file, index=False)
        print(f"\n🔽 Errors saved to: {error_file}")
    else:
        print("✅ All rows passed validation!")

if __name__ == '__main__':
    main()
