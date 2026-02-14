import os
import pandas as pd
from sqlalchemy import create_engine

# Optional: load local .env file (do not commit your .env to source control)
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # If python-dotenv isn't installed, environment variables should still work
    pass

# Build DB URL from environment variables. Set either `DATABASE_URL`
# or the individual `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`.
db_url = os.getenv('DATABASE_URL')
if not db_url:
    user = os.getenv('DB_USER', 'postgres')
    password = os.getenv('DB_PASSWORD', '')
    host = os.getenv('DB_HOST', 'localhost')
    port = os.getenv('DB_PORT', '5432')
    db = os.getenv('DB_NAME', 'etl_pharma')
    if password:
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    else:
        db_url = f"postgresql://{user}@{host}:{port}/{db}"

engine = create_engine(db_url)

def bulk_load_batches(csv_path):
    # Load your batch data (ensure column names match your SQL table)
    df_batches = pd.read_csv(csv_path)
    
    try:
        # Loading into stock_batches fires the Trigger for every row!
        df_batches.to_sql('stock_batches', engine, if_exists='append', index=False)
        print("Bulk load complete. Inventory totals have been synced by the Trigger.")
    except Exception as e:
        print(f"Error: {e}")

