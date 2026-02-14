import pandas as pd
import random

# 1. Define sample data reflecting the Pakistan pharmaceutical market
meds = [
    {"brand_name": "Panadol", "generic_name": "Paracetamol", "strength": "500mg", "dosage_form": "Tablet"},
    {"brand_name": "Augmentin", "generic_name": "Co-amoxiclav", "strength": "625mg", "dosage_form": "Tablet"},
    {"brand_name": "Softin", "generic_name": "Loratadine", "strength": "10mg", "dosage_form": "Tablet"},
    {"brand_name": "Risek", "generic_name": "Omeprazole", "strength": "20mg", "dosage_form": "Capsule"}
]

def generate_gtin():
    # DRAP/GS1 GTIN-14 usually starts with a country prefix (e.g., 896 for Pakistan)
    return "896" + "".join([str(random.randint(0, 9)) for _ in range(11)])

# 2. Extract/Generate Logic
data = []
for i, med in enumerate(meds):
    data.append({
        "medication_id": i + 1,
        "gtin": generate_gtin(),
        "brand_name": med["brand_name"],
        "generic_name": med["generic_name"],
        "strength": med["strength"],
        "dosage_form": med["dosage_form"],
        "unit_cost": round(random.uniform(10.5, 500.0), 2)
    })

df_meds = pd.DataFrame(data)
print("--- Extracted Medication Data (DRAP Compliant) ---")
print(df_meds.head())

# Save to CSV (This acts as our 'Staging' file)
df_meds.to_csv("stg_med_detail.csv", index=False)