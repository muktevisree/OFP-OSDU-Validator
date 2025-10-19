import os
import sys
import streamlit as st
import pandas as pd

# ✅ Add root directory to path so modules can be found (needed for Streamlit Cloud)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.ghg_rules import validate_ghg_row
from modules.ccs_rules import validate_ccs_row
from modules.uhs_rules import validate_uhs_row

# Mapping of dataset type to validation function
VALIDATORS = {
    "GHG": validate_ghg_row,
    "CCS": validate_ccs_row,
    "UHS": validate_uhs_row
}

st.set_page_config(page_title="OFP–OSDU ESG Validator", layout="wide")
st.title("🌍 ESG Data Validator – GHG | CCS | UHS")

st.markdown(
    "Upload your ESG dataset (CSV) and choose the dataset type. "
    "The validator checks schema and business rule compliance based on OFP and OSDU standards."
)

# Dataset type selection
dataset_type = st.selectbox("Select Dataset Type", ["GHG", "CCS", "UHS"])
uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file and dataset_type:
    df = pd.read_csv(uploaded_file)
    validator_fn = VALIDATORS[dataset_type]

    # ℹ️ Dataset-specific validation notes
    if dataset_type == "GHG":
        st.info(
            "ℹ️ **Note:** GHG validation checks scope classification (1/2/3), emission sources, and activity data "
            "mapped to Open Footprint (OFP) schema. Ensure emission units, fuel/activity types, and years are consistent."
        )
    elif dataset_type == "CCS":
        st.info(
            "ℹ️ **Note:** CCS validation checks capture, transport, and storage values. "
            "Mass balance differences over `1000` tonnes are flagged as errors. "
            "Adjust this threshold in `modules/ccs_rules.py` for your test or real datasets."
        )
    elif dataset_type == "UHS":
        st.info(
            "ℹ️ **Note:** UHS validation checks H₂ injection/withdrawal volumes, cushion gas, and reservoir conditions "
            "based on OSDU storage schema and Open Footprint compatibility. Ensure units and timelines are aligned."
        )

    st.subheader("🔍 Validation Results")
    errors = []
    for idx, row in df.iterrows():
        row_errors = validator_fn(row)
        if row_errors:
            errors.append({"Row": idx + 2, "Errors": "; ".join(row_errors)})

    if errors:
        error_df = pd.DataFrame(errors)
        st.error(f"❌ {len(errors)} rows failed validation.")
        st.dataframe(error_df, use_container_width=True)
        st.download_button("📥 Download Errors", error_df.to_csv(index=False), "errors.csv", "text/csv")
    else:
        st.success("✅ All rows passed validation.")
        st.dataframe(df.head(), use_container_width=True)
else:
    st.info("Please upload a file and select a dataset type.")
