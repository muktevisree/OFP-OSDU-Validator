import argparse
from validate_ghg import run_ghg_validation

def main():
    parser = argparse.ArgumentParser(description="ESG Dataset Validator CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # GHG Validator CLI
    ghg_parser = subparsers.add_parser('validate-ghg', help='Validate GHG dataset')
    ghg_parser.add_argument('filepath', type=str, help='Path to GHG CSV file')

    args = parser.parse_args()

    if args.command == 'validate-ghg':
        run_ghg_validation(args.filepath)

if __name__ == '__main__':
    main()
