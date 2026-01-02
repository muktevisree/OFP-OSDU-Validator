import argparse

from validate_ghg import run_ghg_validation
from modules.ccs_v2.validate_ccs_v2 import validate_csv as run_ccs_validation
from modules.uhs_v2.validate_uhs_v2 import validate_csv as run_uhs_validation
from modules.water_v2.validate_water_v2 import validate_csv as run_water_validation
from modules.air_v2.validate_air_v2 import validate_csv as run_air_validation
from modules.waste_v2.validate_waste_v2 import validate_csv as run_waste_validation
from modules.energy_v2.validate_energy_v2 import validate_csv as run_energy_validation
from modules.land_v2.validate_land_v2 import validate_csv as run_land_validation
from modules.noise_v2.validate_noise_v2 import validate_csv as run_noise_validation
from modules.emissions_intensity_v2.validate_emissions_intensity_v2 import validate_csv as run_intensity_validation

parser = argparse.ArgumentParser(description="ESG Validator CLI")
parser.add_argument(
    "command",
    choices=[
        "validate-ghg", "ccs", "validate-uhs", "validate-water", "validate-air",
        "validate-waste", "validate-energy", "validate-land", "validate-noise", "validate-intensity"
    ],
    help="Choose validation type",
)
parser.add_argument(
    "--path",
    required=True,
    help="Path to the input CSV file",
)

args = parser.parse_args()

if args.command == "validate-ghg":
    run_ghg_validation(args.path, rule_file_path="modules/ghg_v2/rules/ghg_rules.yaml")
elif args.command == "ccs":
    run_ccs_validation(args.path, rule_file_path="modules/ccs_v2/rules/ccs_rules.yaml")
elif args.command == "validate-uhs":
    run_uhs_validation(args.path, rule_file_path="modules/uhs_rules.yaml")
elif args.command == "validate-water":
    run_water_validation(args.path, rule_file_path="modules/water_v2/rules/water_rules.yaml")
elif args.command == "validate-air":
    run_air_validation(args.path, rule_file_path="modules/air_v2/rules/air_rules.yaml")
elif args.command == "validate-waste":
    run_waste_validation(args.path, rule_file_path="modules/waste_v2/rules/waste_rules.yaml")
elif args.command == "validate-energy":
    run_energy_validation(args.path, rule_file_path="modules/energy_v2/rules/energy_rules.yaml")
elif args.command == "validate-land":
    run_land_validation(args.path, rule_file_path="modules/land_v2/rules/land_rules.yaml")
elif args.command == "validate-noise":
    run_noise_validation(args.path, rule_file_path="modules/noise_v2/rules/noise_rules.yaml")
elif args.command == "validate-intensity":
    run_intensity_validation(args.path, rule_file_path="modules/emissions_intensity_v2/rules/emissions_intensity_rules.yaml")
