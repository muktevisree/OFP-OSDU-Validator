# 🏷️ Release Notes – v0.3-uhs

## 🚀 What’s New
This release delivers **Phase 3 – UHS Validator Module**, extending the ESG dataset validation suite to Underground Hydrogen Storage datasets.

### ✅ Highlights
- Added `validate_uhs.py` CLI script to validate UHS records
- Introduced `suhs_schema.yaml` with expected UHS data fields
- Created `sample_uhs_dataset.csv` with valid and invalid test cases
- Implemented modular validation logic via `uhs_rules.py`
- Updated folder structure and `README.md` for UHS usage

### 📁 Key Files Added
```
cli/validate_uhs.py
schemas/suhs_schema.yaml
examples/sample_uhs_dataset.csv
modules/uhs_rules.py
```

---

## 📦 Release Summary
| Item | Details |
|------|---------|
| Version | v0.3-uhs |
| Date | October 5, 2025 |
| Focus | UHS Dataset Validator (Phase 3) |
| Compatible With | GHG (v0.1), CCS (v0.2) |
| Upcoming | Streamlit UI (v0.4), JOSS Submission (v1.0) |

---

## 📚 Citation
Please cite the tool via Zenodo:

```
Sreekanth Muktevi. (2025). OFP–OSDU ESG Validator [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.17262927
```

> Your citation supports open-source sustainability tools and recognition of public domain contributions.

---

## 🧭 UHS Validation Rules Implemented
- Total Storage = Cushion Gas + Working Gas
- Net Flow = Injection Volume – Withdrawal Volume
- Support for multiple reservoir types: `depleted_gas`, `salt_cavern`, `aquifer`

---

## 📘 UHS CLI Usage
To validate a UHS dataset:
```bash
python cli/validate_uhs.py examples/sample_uhs_dataset.csv schemas/suhs_schema.yaml
```

---

## 📁 Repository Structure (Updated)
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
```

---

## 🛣️ Roadmap
- ✅ Phase 1 – GHG Validator (v0.1)
- ✅ Phase 2 – CCS Validator (v0.2)
- ✅ Phase 3 – UHS Validator (v0.3)
- 🔄 Phase 4 – Streamlit UI (v0.4)
- 🧪 Phase 5 – JOSS Submission, Tests (v1.0)

---

For full tool and source: [https://github.com/muktevisree/OFP-OSDU-Validator](https://github.com/muktevisree/OFP-OSDU-Validator)

Contact [@muktevisree](https://github.com/muktevisree) for issues, suggestions, or contributions.
