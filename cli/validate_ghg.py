# cli/validate_ghg.py

import sys
import os

# ✅ Add parent directory to Python path so it can locate the modules folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.ghg_v2.validate_ghg_v2 import validate_csv

def run_ghg_validation(csv_path):
    validate_csv(csv_path, "modules/ghg_v2/rules/ghg_rules.yaml")
