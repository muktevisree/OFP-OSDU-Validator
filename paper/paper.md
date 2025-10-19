
⸻

title: “OFP–OSDU ESG Validator: A Python-based Validation Tool for Synthetic GHG, CCS, and UHS Datasets Aligned to Net-Zero Standards”
authors:
	•	name: Sreekanth Muktevi
affiliation: 1
orcid: 0009-0007-8116-3176
email: muktevisree@gmail.com
affiliations:
	•	index: 1
name: YASH Technologies Inc., Houston, TX, USA
date: 19 October 2025
keywords:
	•	ESG
	•	GHG emissions
	•	Carbon Capture and Storage
	•	Underground Hydrogen Storage
	•	OFP
	•	OSDU
	•	Net-Zero
	•	Data validation
	•	Climate tech
repository: https://github.com/muktevisree/OFP-OSDU-Validator
archive_doi: 10.5281/zenodo.17388732
license: MIT

⸻

Summary

The OFP–OSDU ESG Validator is a lightweight, open-source Python tool designed to validate structured CSV datasets for GHG emissions, Carbon Capture and Storage (CCS), and Underground Hydrogen Storage (UHS). It ensures alignment with data schemas derived from the Open Footprint (OFP) initiative [@openfootprint] and Open Subsurface Data Universe (OSDU) Well-Known Schemas (WKS/WKE) [@osdu], enabling interoperability in digital twin, ESG reporting, and Net-Zero simulations.

By enforcing structural and domain-level rules via modular validators, the tool provides transparent error reporting for each data row. This is especially valuable in climate-tech research where access to high-quality, non-confidential synthetic datasets is crucial.

The validator supports public synthetic datasets (SGED-OFPOSDU, SCCS-OFPOSDU, SUHS-MRV) published on Zenodo [@muktevi2025ghg; @muktevi2025ccs; @muktevi2025uhs]. It helps ensure FAIR data principles (Findable, Accessible, Interoperable, Reusable) are met and is intended for researchers, developers, and ESG solution architects building MRV systems.

Statement of Need

Current ESG and subsurface datasets are often proprietary, fragmented, and inconsistent, limiting their utility for open research, digital modeling, or MRV pipeline development. While synthetic datasets mitigate the confidentiality barrier, they still require schema-level validation for quality and standardization.

This tool fills that gap by:
	•	Providing field-level validation of CSV-based datasets against OFP and OSDU standards
	•	Delivering CLI-based error reporting for rapid feedback
	•	Supporting modular rule definitions for easy extension to new schemas or industries
	•	Enabling researchers to confidently use synthetic datasets in simulations and AI/ML pipelines

The validator supports energy and climate researchers, subsurface engineers, and digital twin developers who rely on structured data integrity for modeling sustainability scenarios.

Functionality

The validator offers two primary interfaces: a Python-based CLI and a user-friendly Streamlit UI. The CLI allows validation of structured CSV files aligned with OFP and OSDU schema standards using commands like:

python cli/validate_ghg.py examples/sample_ghg_dataset.csv schemas/ghg_schema.yaml

The Streamlit web app (streamlit_app/esg_validator_app.py) enables interactive dataset uploads, schema viewing, and error visualization through a browser. A key feature includes adjustable threshold sliders for CCS and UHS mass balance validation, allowing flexible interpretation of injection vs. loss tolerances.

All modules rely on dataset headers conforming to specific schema files (*.yaml) that define required fields and business rules. Test datasets are included under the examples/ directory, with sample records covering both valid and invalid inputs for GHG, CCS, and UHS use cases. These datasets help ensure consistency during rule-based validation and facilitate reproducible results across different usage contexts.

Acknowledgements

This tool was developed by Sreekanth Muktevi as part of his open science contributions in support of digital sustainability platforms. It builds on schema definitions from the Open Footprint Forum [@openfootprint] and OSDU Technical Standards [@osdu].

Special thanks to the open data community, Zenodo, and GitHub for hosting public synthetic datasets and code.

References
