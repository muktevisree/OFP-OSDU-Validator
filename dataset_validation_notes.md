
### Dataset Validation Notes


📘 **Note:** GHG validation checks scope classification (1/2/3), emission sources, and activity data mapped to the Open Footprint (OFP) schema.  
Ensure emission units, fuel/activity types, and years are consistent.  
There is **no mass balance threshold** for GHG data, but structural schema and business rule compliance is enforced.



📘 **Note:** CCS validation checks capture, transport, and storage values.  
Mass balance differences over **1000 tonnes** are flagged as errors (**default threshold**).  
You can adjust this using the **mass balance threshold slider** below or modify it in `modules/ccs_rules.py` for advanced control.



📘 **Note:** UHS validation checks H₂ injection/withdrawal volumes, cushion gas, and reservoir conditions based on OSDU WKS and Open Footprint compatibility.  
Mass balance differences over **500 tonnes** are flagged as errors (**default threshold**).  
You can adjust this using the **mass balance threshold slider** below or modify it in `modules/uhs_rules.py`.

