# OFP–OSDU ESG Validator Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/123456789.svg)](https://zenodo.org/record/123456789)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Validation](https://img.shields.io/badge/validator-GHG%2FCCS%2FUHS-green)

## Overview

This open-source tool validates synthetic ESG datasets aligned with the Open Footprint (OFP) and Open Subsurface Data Universe (OSDU) schemas. It provides domain-specific rule enforcement for:

- ✅ Greenhouse Gas (GHG) emissions
- ✅ Carbon Capture & Storage (CCS) MRV
- ✅ Underground Hydrogen Storage (UHS) MRV

Designed for academic, ESG, and energy data validation use cases, the tool enforces schema compliance, MRV integrity, and FAIR principles.

## Features

- Schema validation against OFP + OSDU (JSON/YAML)
- Rule-based validation for GHG Scope 1–3, mass balance, flaring
- CCS injection/storage MRV logic (ISO 27916, EPA Subpart RR)
- UHS validation: compression intensity, cushion gas, cycling logic
- Modular architecture: each domain has its own CLI + rules
- Optional Streamlit dashboard for visualization and inspection
- Open-source, FAIR-compliant, and Zenodo-versioned

## Getting Started

```bash
# Clone repo
git clone https://github.com/muktevisree/ofp-osdu-validator.git
cd ofp-osdu-validator

# Run GHG validator (example)
python cli/validate_ghg.py --input examples/sample_ghg.csv --schema schemas/ofp_schema.yaml
```

## Repository Structure

```
ofp-osdu-validator/
├── cli/              # CLI entry points (validate_ghg, validate_ccs, validate_uhs)
├── core/             # Shared logic for schema and rule validation
├── modules/          # Domain-specific validation rules
├── schemas/          # Schema definitions and OFP/OSDU crosswalks
├── streamlit_app/    # Web interface (optional)
├── examples/         # Sample notebooks and test datasets
├── tests/            # Unit tests
```

## Citation

If you use this tool, please cite:

```
Muktevi, S. et al. (2025). OFP–OSDU ESG Validator Tool: Schema-Based Validation for Synthetic GHG, CCS, and UHS Datasets. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

## License

MIT License © 2025 Sreekanth Muktevi
