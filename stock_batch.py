import pandas as pd
import random
from datetime import datetime, timedelta

# Extract the unique medication IDs you have in your med_detail table
# For this simulation, we'll assume IDs 1-50
med_ids = list(range(1, 51))

data = []
for m_id in med_ids:
    # Generate 1-2 batches per medication to show multiple batch handling
    for i in range(random.randint(1, 2)):
        qty = random.randint(200, 1000)
        data.append({
            "med_id": m_id,
            "batch_no": f"BATCH-{random.randint(1000, 9999)}",
            "expiry_date": (datetime.now() + timedelta(days=random.randint(365, 730))).date(),
            "quantity_received": qty,
            "current_quantity": qty,
            "unit_cost_at_purchase": round(random.uniform(20.0, 500.0), 2)
        })

df_batches = pd.DataFrame(data)
df_batches.to_csv("stg_stock_batches.csv", index=False)
print("Staging file 'stg_stock_batches.csv' created with 50+ realistic batches.")