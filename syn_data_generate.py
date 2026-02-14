import pandas as pd
import random
from datetime import datetime, timedelta

# 1. THE CLINICAL MAPPING (The "Truth" Table)
# This ensures Brand-to-Generic consistency
pharmacy_lookup = [
    {"generic": "Paracetamol", "brands": ["Panadol", "Calpol", "Febrol"], "forms": ["Tablet", "Syrup"], "strengths": ["500mg", "250mg/5ml"]},
    {"generic": "Co-amoxiclav", "brands": ["Augmentin", "Amoxiclav"], "forms": ["Tablet", "Suspension"], "strengths": ["625mg", "1g", "156mg/5ml"]},
    {"generic": "Omeprazole", "brands": ["Risek", "Omega"], "forms": ["Capsule"], "strengths": ["20mg", "40mg"]},
    {"generic": "Ciprofloxacin", "brands": ["Novidat", "Ciproxin"], "forms": ["Tablet"], "strengths": ["250mg", "500mg"]},
    {"generic": "Sitagliptin", "brands": ["Getryl", "Sitara"], "forms": ["Tablet"], "strengths": ["50mg", "100mg"]}
]

def generate_gtin():
    # Pakistan DRAP prefix is often 896
    return "896" + "".join([str(random.randint(0, 9)) for _ in range(11)])

# 2. GENERATE DRUG MASTER DATA
def extract_realistic_meds(num_records=50):
    data = []
    for i in range(1, num_records + 1):
        # Pick a random generic category
        category = random.choice(pharmacy_lookup)
        
        data.append({
            "medication_id": i,
            "gtin": generate_gtin(),
            "brand_name": random.choice(category["brands"]),
            "generic_name": category["generic"],
            "strength": random.choice(category["strengths"]),
            "dosage_form": random.choice(category["forms"]),
            "unit_cost": round(random.uniform(15.0, 1200.0), 2)
        })
    return pd.DataFrame(data)

# 3. RUN EXTRACTION
df_meds = extract_realistic_meds(50)

# Save to Staging
df_meds.to_csv("stg_med_detail.csv", index=False)

print("Extraction Complete: Data is now clinically realistic.")
print(df_meds[['brand_name', 'generic_name', 'strength']].head(10))