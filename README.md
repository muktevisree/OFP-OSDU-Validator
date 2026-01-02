### 🏷️ Release Notes – v1.5.0

🚀 **What’s New**

This v1.5.0 release of the **OFP–OSDU ESG Validator** marks a major milestone — full support for **all 10 Environmental (E) modules** using a unified CLI, modular YAML-based rule engine, and synthetic dataset examples. The validator continues to align with Open Footprint (OFP) and Open Subsurface Data Universe (OSDU) schemas for sustainability-led reporting.

---

✅ **Key Enhancements**

🔄 **Modular CLI Validation**  
• ✅ GHG Module (v0.1)  
• ✅ CCS Module (v0.2)  
• ✅ UHS Module (v0.3)  
• ✅ **Water, Air, Waste, Energy, Land, Noise, Emissions Intensity** – each with domain-specific YAML rules and validation logic

🧠 **Rule Engine (v2)**  
• YAML-based validation rules per module  
• Typed field checking, required fields, unit integrity  
• Modular, reusable rule paths per domain  
• Error logging and modular output structure  

📁 **Example Datasets**  
• Each module includes a sample `.csv` dataset in `/examples`  
• Validated against corresponding rules in `/modules/.../rules/*.yaml`

---

🧱 **File & Folder Summary**

```
├── cli/
│   ├── main.py
│   ├── validate_ghg.py, validate_ccs.py, ...
├── modules/
│   ├── ghg_v2/, ccs_v2/, ..., intensity_v2/
│   └── rules/ per module
├── examples/
│   ├── sample_ghg_dataset.csv, sample_air_dataset.csv, ...
├── shared/
│   └── validator_engine.py
├── schemas/
├── streamlit_app/ (UI under development)
├── tests/
├── README.md
└── LICENSE
```

---

🧪 **Dataset Compatibility**

| Module               | Rules YAML                              | Sample CSV                            | CLI Support |  
|----------------------|------------------------------------------|----------------------------------------|-------------|  
| GHG                 | `ghg_rules.yaml`                         | `sample_ghg_dataset.csv`              | ✅ Yes      |  
| CCS                 | `ccs_rules.yaml`                         | `sample_ccs_dataset.csv`              | ✅ Yes      |  
| UHS                 | `uhs_rules.yaml`                         | `sample_uhs_dataset.csv`              | ✅ Yes      |  
| Water               | `water_rules.yaml`                       | `sample_water_dataset.csv`            | ✅ Yes      |  
| Air                 | `air_rules.yaml`                         | `sample_air_dataset.csv`              | ✅ Yes      |  
| Waste               | `waste_rules.yaml`                       | `sample_waste_dataset.csv`            | ✅ Yes      |  
| Energy              | `energy_rules.yaml`                      | `sample_energy_dataset.csv`           | ✅ Yes      |  
| Land                | `land_rules.yaml`                        | `sample_land_dataset.csv`             | ✅ Yes      |  
| Noise               | `noise_rules.yaml`                       | `sample_noise_dataset.csv`            | ✅ Yes      |  
| Emissions Intensity | `emissions_intensity_rules.yaml`         | `sample_intensity_dataset.csv`        | ✅ Yes      |  

---

📘 **Example CLI Usage**

```bash
# Run GHG Validator
python cli/main.py validate-ghg examples/sample_ghg_dataset.csv

# Run Water Validator
python cli/main.py validate-water examples/sample_water_dataset.csv

# Run Intensity Validator
python cli/main.py validate-intensity examples/sample_intensity_dataset.csv
```

---

📚 **Citation**

Please cite via Zenodo:  
**Sreekanth Muktevi. (2025). OFP–OSDU ESG Validator [Computer software]. Zenodo.**  
https://doi.org/10.5281/zenodo.17262927

---

🛠️ **Contributors**  
• Lead Developer: [Sreekanth Muktevi (@muktevisree)](https://github.com/muktevisree)  
• Architect of synthetic datasets for SGED, SCCS, SUHS, and validator framework
