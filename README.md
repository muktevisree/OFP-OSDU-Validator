# 🌍 OFP–OSDU ESG Validator

> Open-source Python tool to validate ESG datasets (GHG, CCS, UHS) aligned to Open Footprint (OFP) and Open Subsurface Data Universe (OSDU) schemas.

---

## 🧭 Project Scope

The validator ensures:
- ✅ Schema conformance
- 📏 Rule-based validation (e.g., mass balance)
- 🔄 Modular ESG coverage (GHG → CCS → UHS)
- 📤 FAIR-aligned data formats (CSV + YAML)

Built for:
- Researchers
- Climate-Tech developers
- ESG reporting analysts
- Open-data contributors

---

## 📁 Repository Structure

```text
ofp-osdu-validator/
├── cli/                # CLI entry points (validate_ghg, validate_ccs)
├── core/               # Shared logic for schema and rule validation
├── modules/            # Domain-specific validation rules
├── schemas/            # Schema definitions and OFP/OSDU crosswalks
├── examples/           # Sample notebooks and test datasets
├── tests/              # Unit tests (coming soon)
├── streamlit_app/      # Streamlit UI (Phase 3)
├── LICENSE
├── README.md
├── setup.py (optional)
```

---

## 🚀 How to Use

### 📦 1. Clone the Repository
```bash
git clone https://github.com/muktevisree/OFP-OSDU-Validator.git
cd OFP-OSDU-Validator
```

### 🧪 2. Run Validator for GHG
```bash
python cli/validate_ghg.py examples/sample_ghg_dataset.csv schemas/ofp_schema.yaml
```

### 🛢️ 3. Run Validator for CCS
```bash
python cli/validate_ccs.py examples/sample_ccs_dataset.csv schemas/sccs_schema.yaml
```

Each row will return ✅ Passed or ❌ Failed, with reasoning (e.g., total ≠ sum of scopes).

---

## 📚 Sample Data

Sample CSV and YAML schema files are available in:
- `examples/sample_ghg_dataset.csv`
- `examples/sample_ccs_dataset.csv`
- `schemas/ofp_schema.yaml`
- `schemas/sccs_schema.yaml`

These include both valid and intentionally invalid rows for demonstration.

---

## 🔬 Citation

This tool is cited via Zenodo:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17262927.svg)](https://doi.org/10.5281/zenodo.17262927)

```
Sreekanth Muktevi. (2025). OFP–OSDU ESG Validator [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.17262927
```

---

## 🔮 Roadmap

- ✅ Phase 1: GHG Validator (Scope 1-2-3 logic)
- ✅ Phase 2: CCS Validator (mass balance rule)
- 🔄 Phase 3: UHS Validator (formation types, flow logic)
- 🖥️ Phase 4: Streamlit Web App (interactive validation)
- 🧪 Phase 5: Test Suite + JOSS submission

---

## 🤝 Contributing

Issues and PRs are welcome!
- Fork the repo
- Create your feature branch
- Submit a pull request

---

## 👤 Author
**Sreekanth Muktevi**  
Vice President, IT Services – YASH Technologies  
[GitHub](https://github.com/muktevisree) | [Zenodo](https://zenodo.org/records/17262927)

---

## 🪪 License

This repository is licensed under **MIT License** – see [LICENSE](LICENSE) file.
