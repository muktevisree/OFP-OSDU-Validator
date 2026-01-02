# cli/validate_ghg.py

import sys
import os

# Ensure project root is on PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.ghg_v2.validate_ghg_v2 import run_ghg_validation

def run_ghg(csv_path):
    run_ghg_validation(csv_path)
