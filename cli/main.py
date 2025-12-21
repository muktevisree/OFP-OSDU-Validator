import argparse
from validate_ghg import run_ghg_validation
from modules.ccs_v2.validate_ccs_v2 import validate_csv as run_ccs_validation

parser = argparse.ArgumentParser()
parser.add_argument('command', choices=['validate-ghg', 'ccs'])
parser.add_argument('filepath', help='Path to CSV file')

args = parser.parse_args()

if args.command == 'validate-ghg':
    run_ghg_validation(args.filepath)
elif args.command == 'ccs':
    run_ccs_validation(args.filepath)


