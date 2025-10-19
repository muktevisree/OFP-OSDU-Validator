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
    "The validator checks schema and business rule compliance based on OFP and OSDU WKS standards."
)

# Dataset type selection
dataset_type = st.selectbox("Select Dataset Type", ["GHG", "CCS", "UHS"])
uploaded_file = st.file_uploader("Upload CSV file", type="csv")

# 📘 Show dataset-specific guidance before validation
if dataset_type == "GHG":
    st.info(
        "ℹ️ **Note:** GHG validation checks scope classification (1/2/3), emission sources, and activity data "
        "mapped to Open Footprint (OFP) schema. Ensure emission units, fuel/activity types, and years are consistent."
    )
    with st.expander("📘 GHG Dataset Header Reference"):
        st.markdown("""
        **Required Columns for GHG Validation (based on OFP schema):**
        ```text
        Asset, Company, Country, Region, Sector, Facility_ID, Facility_Name, Facility_Type,
        Reporting_Year, Month, Emission_Type, Emission_Value_tCO2e, Emission_Method,
        Emission_Factor_Source, Regulator, Scope_1_tCO2e, Scope_2_tCO2e, Scope_3_tCO2e,
        Energy_Consumed_kWh, Flaring_Volume_Mscf, Methane_tons, Production_Volume,
        Production_Unit, Industry_Code, Data_Quality, Data_Type, Dataset_Version, Source,
        Latitude, Longitude, Facility_Status, Notes, Total_Emissions
        ```
        - File must be `.csv` with 1 header row
        - Emissions must be in metric tons CO₂e
        - Reporting year should be between 1990–2100
        """)
elif dataset_type == "CCS":
    st.info(
        "ℹ️ **Note:** CCS validation checks capture, transport, and storage values. "
        "Mass balance differences over `1000` tonnes are flagged as errors. "
        "Adjust this threshold in `modules/ccs_rules.py` for your test or real datasets."
    )
    with st.expander("📘 CCS Dataset Header Reference"):
        st.markdown("""
        **Required Columns for CCS Validation (based on OFP + OSDU WKS):**
        ```text
        record_id, case_id, facility_id, country_code, lat, lon, capture_tech,
        co2_captured_tonnes, capture_energy_MWh, transport_mode, pipeline_length_km,
        transport_loss_tonnes, well_id, injection_start_date, injection_end_date,
        co2_injected_tonnes, co2_produced_tonnes, reservoir_type, avg_reservoir_pressure_MPa,
        avg_reservoir_temp_C, mmv_methods, leak_events_count, leak_mass_tonnes,
        ch4_emissions_tonnes, ogmp_source_category, co2_net_stored_tonnes
        ```
        - Dates must be in ISO format (e.g., `2023-01-01`)
        - Mass balance: captured ≈ stored + transport + leak (±1000 tonnes)
        """)
elif dataset_type == "UHS":
    st.info(
        "ℹ️ **Note:** UHS validation checks H₂ injection/withdrawal volumes, cushion gas, and reservoir conditions "
        "based on OSDU WKS and Open Footprint compatibility. Ensure units and timelines are aligned."
    )
    with st.expander("📘 UHS Dataset Header Reference"):
        st.markdown("""
        **Required Columns for UHS Validation (based on OFP + OSDU WKS):**
        ```text
        record_id, case_id, facility_id, country_code, lat, lon, reservoir_type, well_id,
        injection_start_date, injection_end_date, h2_injected_tonnes, h2_withdrawn_tonnes,
        h2_cushion_gas_tonnes, h2_losses_tonnes, h2_net_stored_tonnes, compression_energy_MWh,
        transport_mode, pipeline_length_km, avg_reservoir_pressure_MPa, avg_reservoir_temp_C,
        mmv_methods, leak_events_count, leak_mass_tonnes, methane_co_produced_tonnes,
        ogmp_source_category, notes
        ```
        - Hydrogen metrics must be in tonnes
        - Energy must be in MWh
        - Dates must be ISO 8601 format
        """)

# 🚀 Perform validation
if uploaded_file and dataset_type:
    df = pd.read_csv(uploaded_file)
    validator_fn = VALIDATORS[dataset_type]

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
