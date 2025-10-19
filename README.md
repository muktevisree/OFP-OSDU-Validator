🏷️ Release Notes – v1.0.0

🚀 What’s New

This is the first full public release (v1.0.0) of the OFP–OSDU ESG Validator – a modular, multi-domain data validation tool for ESG datasets, aligned with Open Footprint (OFP) and Open Subsurface Data Universe (OSDU) schemas.

✅ Key Enhancements

🔄 Modular CLI Validation
	•	✅ GHG Module (v0.1): Scope-based emissions validation, fuel/activity checks
	•	✅ CCS Module (v0.2): Mass balance, reservoir validation, leak tracking
	•	✅ UHS Module (v0.3): Hydrogen injection/withdrawal checks, MMV methods

🌐 Streamlit UI (v0.4)
	•	Upload any ESG dataset (GHG, CCS, UHS)
	•	View dataset-specific header guides
	•	Adjust threshold values for CCS/UHS mass balance
	•	Download detailed error logs

🧠 Rule Engine
	•	Built-in rule checks per domain (Scope 1/2/3, transport modes, MMV keywords)
	•	Date parsing, field completeness, mass balance validation
	•	Slider-enabled threshold override for flexible testing

⸻

🧱 File & Folder Summary

├── cli/
│   ├── validate_ghg.py
│   ├── validate_ccs.py
│   └── validate_uhs.py
├── modules/
│   ├── ghg_rules.py
│   ├── ccs_rules.py
│   └── uhs_rules.py
├── schemas/
│   ├── ghg_schema.yaml
│   ├── sccs_schema.yaml
│   └── suhs_schema.yaml
├── examples/
│   ├── sample_ghg_dataset.csv
│   ├── sample_ccs_dataset.csv
│   └── sample_uhs_dataset.csv
├── streamlit_app/
│   └── ESG_Validator_App.py
├── README.md
└── LICENSE


⸻

🧪 Dataset Compatibility

Module	Schema	Sample File	CLI Support	UI Support
GHG	ghg_schema.yaml	sample_ghg_dataset.csv	✅ Yes	✅ Yes
CCS	sccs_schema.yaml	sample_ccs_dataset.csv	✅ Yes	✅ Yes
UHS	suhs_schema.yaml	sample_uhs_dataset.csv	✅ Yes	✅ Yes


⸻

📚 Citation

Please cite via Zenodo:

Sreekanth Muktevi. (2025). OFP–OSDU ESG Validator [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.17262927

Your citation supports open sustainability science and open-source tooling.

⸻

📘 Example CLI Usage

# GHG
python cli/validate_ghg.py examples/sample_ghg_dataset.csv schemas/ghg_schema.yaml

# CCS
python cli/validate_ccs.py examples/sample_ccs_dataset.csv schemas/sccs_schema.yaml

# UHS
python cli/validate_uhs.py examples/sample_uhs_dataset.csv schemas/suhs_schema.yaml


⸻

🔮 Roadmap

Phase	Feature	Status
Phase 1	GHG Validator	✅ Complete
Phase 2	CCS Validator	✅ Complete
Phase 3	UHS Validator	✅ Complete
Phase 4	Streamlit UI	✅ Complete
Phase 5	JOSS Submission & Testing	🔄 In Progress


⸻

🛠️ Contributors
	•	Lead Developer: Sreekanth Muktevi (@muktevisree)
	•	Dataset creator and validator architect for SGED, SCCS, SUHS mapped to OFP/OSDU
