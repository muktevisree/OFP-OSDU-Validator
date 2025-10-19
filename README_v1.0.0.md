# 🌍 OFP–OSDU ESG Validator

**Version:** v1.0.0  
**Release Date:** October 19, 2025  
**Author:** [Sreekanth Muktevi](https://github.com/muktevisree)  
**DOI:** [10.5281/zenodo.17262927](https://doi.org/10.5281/zenodo.17262927)

---

## 🧭 Overview

The **OFP–OSDU ESG Validator** is a modular, open-source Python toolkit to validate ESG datasets aligned with the **Open Footprint (OFP)** and **Open Subsurface Data Universe (OSDU)** schemas.  
It includes schema + business rule validation for:

- ✅ **GHG Emissions**
- ✅ **Carbon Capture & Storage (CCS)**
- ✅ **Underground Hydrogen Storage (UHS)**

Designed for energy companies, researchers, and regulators building net-zero digital platforms.

---

## 🆕 Major Release v1.0.0 – What’s Included?

### ✅ Dataset Validators
- **GHG (v0.1):** Scope 1/2/3 validation, emission method checks, OFP schema mapping
- **CCS (v0.2):** Mass balance checks, injection monitoring, leak detection validation
- **UHS (v0.3):** Net storage, cushion gas rules, MMV keywords

### ✅ Streamlit UI (v0.4)
- Simple UI to upload files and view errors
- Custom slider for threshold tuning (CCS/UHS mass balance)
- Schema headers and validation notes in expandable panels

### ✅ Modularity & Open Data
- `cli/` for command-line validation
- `modules/` for rules per dataset
- `schemas/` for YAML-based schema structure
- `examples/` for sample test data
- Fully versioned on [GitHub](https://github.com/muktevisree/OFP-OSDU-Validator) and [Zenodo](https://zenodo.org/doi/10.5281/zenodo.17262927)

---

## 🔧 Repository Structure

```
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
│   └── esg_validator_app.py
```

---

## 🚀 Quickstart

### ✅ CLI Usage

```bash
python cli/validate_ghg.py examples/sample_ghg_dataset.csv schemas/ghg_schema.yaml
python cli/validate_ccs.py examples/sample_ccs_dataset.csv schemas/sccs_schema.yaml
python cli/validate_uhs.py examples/sample_uhs_dataset.csv schemas/suhs_schema.yaml
```

### ✅ Streamlit UI

```bash
streamlit run streamlit_app/esg_validator_app.py
```

Open in browser at: `http://localhost:8501`

---

## 🧪 Validation Highlights

| Dataset | Business Rules Implemented |
|---------|-----------------------------|
| GHG     | Scope classification, emissions consistency, OFP schema |
| CCS     | Mass balance: Captured ≈ Stored + Leaks + Losses ± Threshold |
| UHS     | Injected ≈ Withdrawn + Losses; Net vs Cushion gas check |

Mass balance thresholds customizable via UI slider and CLI arg.

---

## 📚 Citation

```bibtex
@software{muktevi_esgvalidator_2025,
  author       = {Sreekanth Muktevi},
  title        = {OFP–OSDU ESG Validator},
  year         = 2025,
  doi          = {10.5281/zenodo.17262927},
  url          = {https://zenodo.org/record/17262927}
}
```

---

## 🤝 Contributions & License

- License: [MIT License](LICENSE)
- Contributions: Welcome via PRs and issues
- Contact: [muktevisree@gmail.com](mailto:muktevisree@gmail.com)

---

## 📅 Roadmap

- ✅ GHG (v0.1)
- ✅ CCS (v0.2)
- ✅ UHS (v0.3)
- ✅ Streamlit App (v0.4)
- 🔜 JOSS Submission (v1.1)
- 🔜 Test suite (v1.2)
