import argparse
from validate_ghg import run_ghg_validation
from modules.ccs_v2.validate_ccs_v2 import validate_csv as run_ccs_validation
from modules.uhs_v2.validate_uhs_v2 import validate_csv as run_uhs_validation

parser = argparse.ArgumentParser()
parser.add_argument("command", choices=["validate-ghg", "ccs", "validate-uhs"], help="Choose validation type")
parser.add_argument("--path", required=True, help="Path to the input CSV file")
args = parser.parse_args()

if args.command == "validate-ghg":
    run_ghg_validation(args.path)
elif args.command == "ccs":
    run_ccs_validation(args.path, rule_file_path="modules/ccs_rules.yaml")
elif args.command == "validate-uhs":
    run_uhs_validation(args.path, rule_file_path="modules/uhs_rules.yaml")
